"""Draft of paper Fig. 3: the ecosystem graph drawn as a layer × community grid.

Rows are the ecosystem layers (archives at the top, schema languages at the bottom); columns are
home communities, with cross-cutting communities (general, biology) on the right. Bridges between
communities therefore run sideways across columns, and links within a community stay in its column.
Edges are styled by community scope; edges also found in a registry get a dot at their midpoint.
"""

from __future__ import annotations

import math
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import FancyArrowPatch  # noqa: E402

from .build import REGISTRIES, BuildResult  # noqa: E402
from .model import Taxonomy  # noqa: E402

EDGE_STYLE = {
    "cross_community": dict(color="#c0392b", lw=1.6, ls="-", alpha=0.9, zorder=3),
    "within_community": dict(color="#555555", lw=0.9, ls="-", alpha=0.6, zorder=2),
    "shared": dict(color="#7f8c8d", lw=0.7, ls=(0, (3, 2)), alpha=0.45, zorder=1),
}
SCOPE_LABEL = {
    "cross_community": "Cross-community bridge",
    "within_community": "Within community",
    "shared": "Link to shared infrastructure",
}


def column_order(taxonomy: Taxonomy, homes: set[str]) -> list[str]:
    """Domain communities in taxonomy order, then cross-cutting ones; only those with nodes."""
    domain = [c for c in taxonomy.communities if c not in taxonomy.cross_cutting]
    shared = [c for c in taxonomy.communities if c in taxonomy.cross_cutting]
    return [c for c in domain + shared if c in homes]


def grid_layout(result: BuildResult, taxonomy: Taxonomy, max_per_row: int = 4) -> tuple[dict, dict, dict]:
    """Return node positions, column spans {community: (x0, x1)}, and row y {layer: y}.

    Cells with more than ``max_per_row`` nodes wrap onto sub-rows within the layer band.
    """
    g = result.graph
    cells: dict[tuple[str, str], list[str]] = defaultdict(list)
    for n, d in g.nodes(data=True):
        cells[(d["layer"], d["home"])].append(n)
    columns = column_order(taxonomy, {d["home"] for _, d in g.nodes(data=True)})
    layers = sorted(taxonomy.layers, key=taxonomy.layer_order)
    rows = {layer: -i for i, layer in enumerate(layers)}

    pos, spans, x = {}, {}, 0.0
    for c in columns:
        width = max(min(len(cells[(layer, c)]), max_per_row) for layer in layers)
        spans[c] = (x, x + width)
        for layer in layers:
            members = sorted(cells[(layer, c)], key=lambda n: g.nodes[n]["label"].lower())
            n_sub = math.ceil(len(members) / max_per_row) if members else 1
            for i, n in enumerate(members):
                row, col = divmod(i, max_per_row)
                in_row = min(max_per_row, len(members) - row * max_per_row)
                pad = (width - in_row) / 2
                if n_sub > 1:  # wrapped cell: spread sub-rows over the band
                    dy = 0.3 - 0.6 * row / (n_sub - 1)
                else:  # stagger alternate nodes so neighbouring labels do not collide
                    dy = (0.12 if col % 2 else -0.12) * (len(members) > 1)
                pos[n] = (x + pad + col + 0.5, rows[layer] + dy)
        x += width + 0.6  # gap between community columns
    return pos, spans, rows


def _arc_midpoint(ax, p0, p1, rad):
    """Midpoint (data coords) of matplotlib's ``arc3`` curve, which is computed in display space."""
    to_disp, to_data = ax.transData, ax.transData.inverted()
    (x0, y0), (x1, y1) = to_disp.transform(p0), to_disp.transform(p1)
    cx, cy = (x0 + x1) / 2 + rad * (y1 - y0), (y0 + y1) / 2 - rad * (x1 - x0)
    mid = (0.25 * x0 + 0.5 * cx + 0.25 * x1, 0.25 * y0 + 0.5 * cy + 0.25 * y1)
    return to_data.transform(mid)


def draw(result: BuildResult, taxonomy: Taxonomy, out_base: Path, mode: str = "strict",
         sources: str = "all", verified_only: bool = False, title: str | None = None) -> list[Path]:
    """Draw the figure and save it as PDF, SVG, and PNG (``out_base`` without suffix)."""
    g = result.graph
    pos, spans, rows = grid_layout(result, taxonomy)
    columns = list(spans)
    cmap = plt.get_cmap("tab10")
    colour = {c: cmap(i % 10) for i, c in enumerate(columns)}

    width = max(x1 for _, x1 in spans.values())
    fig, ax = plt.subplots(figsize=(max(10.0, 0.62 * width + 2.5), 1.25 * len(rows) + 1.6))

    # Row bands and layer labels.
    for i, (layer, y) in enumerate(rows.items()):
        if i % 2 == 0:
            ax.axhspan(y - 0.5, y + 0.5, color="#f4f6f7", zorder=0)
        ax.text(-0.4, y, taxonomy.layers[layer]["label"], ha="right", va="center", fontsize=9, weight="bold")
    # Column headers and separators.
    top = max(rows.values()) + 0.5
    for c, (x0, x1) in spans.items():
        ax.text((x0 + x1) / 2, top + 0.12, c.replace("_", " "), ha="center", va="bottom", fontsize=8.5,
                color=colour[c], weight="bold", rotation=0)
        if c in taxonomy.cross_cutting:
            ax.axvspan(x0 - 0.3, x1 + 0.3, color="#fbf3e4", zorder=0, alpha=0.6)

    # Edges (one line per node pair; a pair with several relations is drawn once).
    drawn = set()
    counts = defaultdict(int)
    markers = []
    for u, v, d in g.edges(data=True):
        if verified_only and not d.get("verified"):
            continue
        is_registry = bool(d["sources"] & set(REGISTRIES))
        if sources == "curated" and "curated" not in d["sources"]:
            continue
        if sources == "registry" and not is_registry:
            continue
        pair = frozenset((u, v))
        if pair in drawn:
            continue
        drawn.add(pair)
        scope = d[f"scope_{mode}"]
        counts[scope] += 1
        style = EDGE_STYLE[scope]
        same_row = g.nodes[u]["layer"] == g.nodes[v]["layer"]
        arrow = FancyArrowPatch(pos[u], pos[v], arrowstyle="-", shrinkA=6, shrinkB=6,
                                connectionstyle=f"arc3,rad={0.35 if same_row else 0.08}",
                                color=style["color"], lw=style["lw"], ls=style["ls"], alpha=style["alpha"],
                                zorder=style["zorder"])
        ax.add_patch(arrow)
        if is_registry:
            markers.append((pos[u], pos[v], 0.35 if same_row else 0.08, style["color"]))

    # Nodes and labels.
    for n, (x, y) in pos.items():
        d = g.nodes[n]
        ax.scatter([x], [y], s=70, color=colour[d["home"]], edgecolor="white", linewidth=0.8, zorder=5)
        ax.text(x, y - 0.17, d["label"], ha="center", va="top", fontsize=6.5, zorder=6,
                bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none", alpha=0.7))

    handles = [Line2D([0], [0], color=EDGE_STYLE[s]["color"], lw=EDGE_STYLE[s]["lw"] + 0.4,
                      ls=EDGE_STYLE[s]["ls"], label=f"{SCOPE_LABEL[s]} ({counts[s]})")
               for s in ("cross_community", "within_community", "shared")]
    handles.append(Line2D([0], [0], marker="o", color="#555555", lw=0, ms=4, label="Also recorded in a registry"))
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.02), ncol=4, frameon=False, fontsize=8)

    ax.set_xlim(-0.4, width + 0.2)
    ax.set_ylim(min(rows.values()) - 0.6, top + 0.5)
    ax.axis("off")
    fig.tight_layout()
    for p0, p1, rad, col in markers:
        ax.plot(*_arc_midpoint(ax, p0, p1, rad), "o", ms=3.5, color=col, zorder=4)
    filters = [f"community scope: {mode}", f"evidence: {sources}"] + (["verified edges only"] if verified_only else [])
    ax.set_title(title or "Neuroscience data standards ecosystem — DRAFT (" + "; ".join(filters) + ")",
                 fontsize=10, loc="left")
    fig.tight_layout()

    out_base = Path(out_base)
    out_base.parent.mkdir(parents=True, exist_ok=True)
    paths = []
    for suffix in (".pdf", ".svg", ".png"):
        path = out_base.with_suffix(suffix)
        fig.savefig(path, dpi=200 if suffix == ".png" else None, bbox_inches="tight")
        paths.append(path)
    plt.close(fig)
    return paths
