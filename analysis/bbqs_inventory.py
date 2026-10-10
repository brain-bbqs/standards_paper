"""Aggregate statistics from the BBQS project inventory and draft of Fig. 4.

Reads the inventory workbook (kept outside this repository; project-level data are not committed) and
writes only aggregate, per-award counts:

    analysis/output/bbqs_aggregates.json               counts used in the paper text (Section 5)
    figures/fig4_bbqs_data/fig4_bbqs_data.{pdf,png}    draft Fig. 4

Run from the paper root with `make fig4`, or:
    uv run --no-project --with openpyxl --with matplotlib python analysis/bbqs_inventory.py
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
INVENTORY = HERE.parents[1] / "bbqs_projects" / "Information ingest-BBQS_All_Projects_OneSheet.xlsx"
COVERAGE = HERE / "behavior_coverage.csv"
OUT = HERE / "output"
FIG_OUT = HERE.parent / "figures" / "fig4_bbqs_data" / "fig4_bbqs_data"

# Case-insensitive patterns matched against the modality, device, tool, and data-sharing fields.
MODALITY_PATTERNS = {
    "Video": r"video|camera",
    "Wearable / inertial sensors": r"wearable|imu\b|acceleromet",
    "Pose estimation": r"\bpose\b",
    "Audio": r"audio|microphone|acoustic|vocal",
    "Eye tracking": r"eye[- ]?track",
    "Extracellular ephys": r"ephys|electrophysiolog|neuropixel|single[- ]unit|spike",
    "EEG": r"\beeg\b",
    "Optical physiology": r"calcium|two[- ]photon|2p\b|miniscope|optical imaging|ophys",
    "EMG": r"\bemg\b",
    "GPS": r"\bgps\b",
    "RFID": r"rfid",
}
TOOL_PATTERNS = {"DeepLabCut": r"deeplabcut|\bdlc\b", "SLEAP": r"\bsleap\b"}
SHARING_PATTERNS = {
    "Neuroscience archive (DANDI, EMBER, OpenNeuro, NDA)": r"dandi|ember|openneuro|\bnda\b",
    "Cloud drive (Dropbox, Box, Google Drive)": r"dropbox|\bbox\b|google drive|onedrive",
    "GitHub": r"github",
}
TEXT_FIELDS = ("Data Modalities", "Sensors / Devices", "Data sharing", "Tools / software")


def load_awards(path: Path = INVENTORY) -> dict[str, list[dict]]:
    import openpyxl

    ws = openpyxl.load_workbook(path, read_only=True, data_only=True).worksheets[0]
    rows = list(ws.iter_rows(values_only=True))
    header, records = rows[0], [dict(zip(rows[0], r)) for r in rows[1:] if any(r)]
    awards = defaultdict(list)
    for r in records:
        awards[r["Award #"]].append(r)
    return dict(awards)


def _split(value) -> set[str]:
    return {v.strip(" -—.").strip().lower() for v in re.split(r"[,;\n]", str(value or "")) if v.strip(" -—.")}


def per_award_values(awards: dict, field: str) -> Counter:
    counts = Counter()
    for rows in awards.values():
        counts.update(set().union(*(_split(r.get(field)) for r in rows)))
    return counts


def aggregate(awards: dict) -> dict:
    text = {a: " ".join(str(r.get(f) or "") for r in rows for f in TEXT_FIELDS).lower()
            for a, rows in awards.items()}
    sharing = {a: " ".join(str(r.get("Data sharing") or "") for r in rows) for a, rows in awards.items()}
    std = {a: re.search(r"standards:([^.]*)", s.lower()).group(1) for a, s in sharing.items()
           if "standards:" in s.lower()}
    species = {a: set().union(*(_split(r.get("Species")) for r in rows)) for a, rows in awards.items()}
    behaviors = per_award_values(awards, "Behaviors")
    behavior_awards = sum(any(str(r.get("Behaviors") or "").strip() for r in rows) for rows in awards.values())
    return {
        "awards": len(awards),
        "mechanisms": dict(Counter(re.match(r"[A-Z]+\d+", a).group(0) for a in awards)),
        "species": dict(Counter(s for v in species.values() for s in v).most_common()),
        "species_groups": len(set().union(*species.values())),
        "human_only_awards": sum(v == {"human"} for v in species.values()),
        "nonhuman_only_awards": sum(bool(v) and "human" not in v for v in species.values()),
        "behavior_awards": behavior_awards,
        "behaviors": dict(behaviors.most_common()),
        "modalities": {k: sum(bool(re.search(p, t)) for t in text.values()) for k, p in MODALITY_PATTERNS.items()},
        "tools": {k: sum(bool(re.search(p, t)) for t in text.values()) for k, p in TOOL_PATTERNS.items()},
        "standards_answers": len(std),
        "standards": {"NWB": sum("nwb" in v for v in std.values()),
                      "BIDS": sum("bids" in v for v in std.values()),
                      "HED (any field)": sum(bool(re.search(r"\bhed\b", t)) for t in text.values()),
                      "Psych-DS": sum(bool(re.search(r"psych-?ds", v)) for v in std.values()),
                      "none yet": sum("none" in v for v in std.values())},
        "sharing_among_standards_answers": {k: sum(bool(re.search(p, sharing[a].lower())) for a in std)
                                            for k, p in SHARING_PATTERNS.items()},
    }


def load_coverage(path: Path = COVERAGE) -> list[dict]:
    with open(path) as f:
        return list(csv.DictReader(f))


def figure(agg: dict, coverage: list[dict], out_base: Path) -> list[Path]:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap
    from matplotlib.patches import Patch

    fig = plt.figure(figsize=(13, 6.2))
    gs = fig.add_gridspec(2, 4, width_ratios=[1, 0.62, 1.5, 0.55], height_ratios=[1, 1], wspace=0.05, hspace=0.45)

    # (a) species
    ax = fig.add_subplot(gs[0, 0])
    sp = sorted(agg["species"].items(), key=lambda x: (-x[1], x[0]))
    labels = [s.split(" (")[0].capitalize() for s, _ in sp]
    ax.barh(labels[::-1], [n for _, n in sp][::-1], color="#5b8db8")
    ax.set_title(f"a  Species ({agg['awards']} awards)", loc="left", fontsize=10, weight="bold")
    ax.tick_params(labelsize=7.5)
    ax.set_xlabel("Awards", fontsize=8)

    # (b) modalities
    ax = fig.add_subplot(gs[1, 0])
    mods = sorted(agg["modalities"].items(), key=lambda x: -x[1])
    ax.barh([m for m, _ in mods][::-1], [n for _, n in mods][::-1], color="#7a9e6e")
    ax.set_title("b  Modalities (awards mentioning)", loc="left", fontsize=10, weight="bold")
    ax.tick_params(labelsize=7.5)
    ax.set_xlabel("Awards", fontsize=8)

    # (c) behaviors x guideline coverage
    beh = agg["behaviors"]
    rows = sorted(coverage, key=lambda r: -beh.get(r["behavior"], 0))
    names = [r["behavior"].capitalize() for r in rows]
    counts = [beh.get(r["behavior"], 0) for r in rows]
    ax = fig.add_subplot(gs[:, 2])  # column 1 is a spacer for the long y labels
    ax.barh(names[::-1], counts[::-1], color="#c97b63")
    ax.set_title(f"c  Behaviors recorded (n = {agg['behavior_awards']} awards) and guideline coverage",
                 loc="left", fontsize=10, weight="bold")
    ax.set_xlabel("Awards", fontsize=8)
    ax.tick_params(labelsize=8)
    hm = fig.add_subplot(gs[:, 3], sharey=ax)
    level = {"supported": 2, "in_progress": 1, "none": 0}
    grid = [[level[r[k]] for k in ("nwb", "bids", "psychds")] for r in rows[::-1]]
    cmap = ListedColormap(["#eeeeee", "#f2c46d", "#3a8f5c"])
    # Row 0 of grid is the bottom bar (barh draws names[::-1] bottom-up), hence origin="lower".
    hm.imshow(grid, aspect="auto", cmap=cmap, vmin=0, vmax=2, origin="lower",
              extent=(-0.5, 2.5, -0.5, len(rows) - 0.5))
    hm.set_xticks([0, 1, 2], ["NWB", "BIDS", "Psych-DS"], fontsize=8)
    hm.tick_params(axis="y", left=False, labelleft=False)
    hm.legend(handles=[Patch(color="#3a8f5c", label="Supported"), Patch(color="#f2c46d", label="In progress"),
                       Patch(color="#eeeeee", label="No guidance")],
              loc="upper center", bbox_to_anchor=(0.5, -0.05), fontsize=7, frameon=False)
    fig.suptitle("DRAFT — BBQS data and standards coverage (aggregate counts)", fontsize=9, x=0.01, ha="left")

    out_base.parent.mkdir(parents=True, exist_ok=True)
    paths = []
    for suffix in (".pdf", ".png"):
        p = out_base.with_suffix(suffix)
        fig.savefig(p, dpi=200 if suffix == ".png" else None, bbox_inches="tight")
        paths.append(p)
    plt.close(fig)
    return paths


def main() -> None:
    agg = aggregate(load_awards())
    OUT.mkdir(exist_ok=True)
    (OUT / "bbqs_aggregates.json").write_text(json.dumps(agg, indent=1) + "\n")
    for p in figure(agg, load_coverage(), FIG_OUT):
        print(p)


if __name__ == "__main__":
    main()
