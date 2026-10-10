"""Check plan/TODO.md against the draft.

Reports:
  * claim markers [TODO-Cn] in draft/ without a row in plan/TODO.md (missing entries)
  * claim rows in plan/TODO.md whose marker no longer appears in draft/ (stale entries)
  * open (unchecked) items per section of TODO.md
  * paths in backticks in plan/TODO.md and draft/12_figures_tables.md that do not exist

Run from the paper root:  make check   (or: python3 tools/check_todo.py)
"""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "draft"
TODO = ROOT / "plan" / "TODO.md"


def draft_markers() -> dict[str, list[str]]:
    found: dict[str, list[str]] = defaultdict(list)
    for f in sorted(DRAFT.glob("*.md")):
        text = f.read_text()
        for group in re.findall(r"\[TODO-([^\]]+)\]", text):
            for cid in re.findall(r"C(\d+)", group):
                found[f"C{cid}"].append(f.name)
    return found


def todo_claims(text: str) -> dict[str, str]:
    """Map claim id -> table row (rows start with '| Cn |')."""
    rows = {}
    for line in text.splitlines():
        m = re.match(r"^\|\s*(C\d+)\s*\|", line)
        if m:
            rows[m.group(1)] = line
    return rows


def open_items(text: str) -> Counter:
    counts, section = Counter(), "?"
    for line in text.splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
        if re.match(r"^\s*- \[ \]", line):
            counts[section] += 1
        if re.match(r"^\|\s*C\d+\s*\|", line) and "| resolved |" not in line:
            counts[section] += 1
    return counts


def missing_paths(*files: Path) -> list[str]:
    bad = []
    for f in files:
        for p in re.findall(r"`([A-Za-z0-9_./-]+/[A-Za-z0-9_.*{},-]+)`", f.read_text()):
            if any(ch in p for ch in "*{}") or p.startswith(("http", "api.")):
                continue
            candidates = [ROOT / p, ROOT / "draft" / p, ROOT.parent / p]
            if not any(c.exists() for c in candidates):
                bad.append(f"{f.name}: {p}")
    return bad


def main() -> int:
    text = TODO.read_text()
    markers, rows = draft_markers(), todo_claims(text)
    problems = 0

    missing = sorted(set(markers) - set(rows), key=lambda c: int(c[1:]))
    stale = sorted(set(rows) - set(markers), key=lambda c: int(c[1:]))
    for cid in missing:
        print(f"MISSING  {cid} is marked in {', '.join(sorted(set(markers[cid])))} but has no row in plan/TODO.md")
    for cid in stale:
        if "| resolved |" not in rows[cid]:
            print(f"STALE    {cid} has a row in plan/TODO.md but no marker in draft/ (resolve or remove)")
    for p in missing_paths(TODO, DRAFT / "12_figures_tables.md"):
        print(f"PATH     {p} does not exist")
    problems = len(missing) + len(stale)

    print("\nOpen items by section:")
    for section, n in open_items(text).items():
        print(f"  {n:3}  {section}")
    print(f"\n{len(markers)} claim markers in draft/, {len(rows)} claim rows in plan/TODO.md")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
