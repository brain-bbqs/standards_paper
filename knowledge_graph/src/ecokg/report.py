"""Export the graph and write the statistics and gap reports."""

from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import date
from pathlib import Path

import networkx as nx

from .build import REGISTRIES, BuildResult
from .classify import SCOPES, SPANS
from .model import Node, Taxonomy


def _plain(value):
    if isinstance(value, (set, frozenset, list, tuple)):
        return ";".join(sorted(str(v) for v in value))
    return value


def export(result: BuildResult, out_dir: Path) -> None:
    g = result.graph
    out_dir.mkdir(parents=True, exist_ok=True)

    node_fields = ["id", "label", "name", "layer", "also_layers", "home", "communities", "kind",
                   "rrid", "fairsharing", "degree", "registry_degree"]
    with open(out_dir / "nodes.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=node_fields)
        w.writeheader()
        for n, d in sorted(g.nodes(data=True)):
            reg = sum(1 for *_, e in g.edges(n, data=True) if e["sources"] & set(REGISTRIES))
            reg += sum(1 for *_, e in g.in_edges(n, data=True) if e["sources"] & set(REGISTRIES))
            w.writerow({"id": n, **{k: _plain(d.get(k, "")) for k in node_fields[1:-2]},
                        "degree": g.degree(n), "registry_degree": reg})

    edge_fields = ["source", "target", "relation", "span", "scope_strict", "scope_lenient",
                   "sources", "in_registry", "provenance", "confidence", "verified",
                   "registry_labels", "evidence"]
    with open(out_dir / "edges.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=edge_fields)
        w.writeheader()
        for u, v, d in sorted(g.edges(data=True), key=lambda x: (x[0], x[1], x[2]["relation"])):
            w.writerow({"source": u, "target": v, **{k: _plain(d.get(k, "")) for k in edge_fields[2:]}})

    plain = nx.MultiDiGraph()
    for n, d in g.nodes(data=True):
        plain.add_node(n, **{k: _plain(v) for k, v in d.items()})
    for u, v, k, d in g.edges(keys=True, data=True):
        plain.add_edge(u, v, key=k, **{a: _plain(b) for a, b in d.items()})
    nx.write_graphml(plain, out_dir / "graph.graphml")
    with open(out_dir / "graph.json", "w") as f:
        json.dump(nx.node_link_data(plain, edges="edges"), f, indent=1)


def _table(header: list[str], rows: list[list]) -> str:
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    lines += ["| " + " | ".join(str(c) for c in row) + " |" for row in rows]
    return "\n".join(lines)


def _pct(a: int, b: int) -> str:
    return f"{a} ({100 * a / b:.0f}%)" if b else "0"


def stats_markdown(result: BuildResult, taxonomy: Taxonomy) -> str:
    g = result.graph
    edges = list(g.edges(data=True))
    layers = sorted(taxonomy.layers, key=taxonomy.layer_order)
    out = [f"# Ecosystem knowledge graph — summary statistics\n",
           f"*Generated {date.today().isoformat()} by `ecokg report`. Draft: curated edges are not yet "
           f"expert-verified; registry coverage is incomplete.*\n",
           f"**{g.number_of_nodes()} nodes, {len(edges)} edges** "
           f"({sum('curated' in d['sources'] for *_, d in edges)} curated, "
           + ", ".join(f"{sum(r in d['sources'] for *_, d in edges)} from {r}" for r in REGISTRIES)
           + "; an edge may have several sources).\n"]

    out.append("## Nodes per layer\n")
    layer_counts = Counter(d["layer"] for _, d in g.nodes(data=True))
    out.append(_table(["Layer", "Nodes"], [[taxonomy.layers[l]["label"], layer_counts[l]] for l in layers]))

    out.append("\n\n## Nodes per home community\n")
    home_counts = Counter(d["home"] for _, d in g.nodes(data=True))
    out.append(_table(["Community", "Nodes"], [[c, home_counts[c]] for c in taxonomy.communities if home_counts[c]]))

    for mode in ("strict", "lenient"):
        out.append(f"\n\n## Edges: layer span × community scope ({mode})\n")
        counts = Counter((d["span"], d[f"scope_{mode}"]) for *_, d in edges)
        rows = [[span] + [counts[(span, s)] for s in SCOPES] + [sum(counts[(span, s)] for s in SCOPES)]
                for span in SPANS]
        rows.append(["total"] + [sum(counts[(sp, s)] for sp in SPANS) for s in SCOPES] + [len(edges)])
        out.append(_table(["", *SCOPES, "total"], rows))
        within = sum(counts[(sp, "within_community")] for sp in SPANS)
        cross = sum(counts[(sp, "cross_community")] for sp in SPANS)
        out.append(f"\n\nAmong edges between domain-specific nodes, **{_pct(cross, within + cross)} "
                   f"cross community boundaries** ({mode} classification).")

    out.append("\n\n## Edges by relation\n")
    rel_counts = Counter(d["relation"] for *_, d in edges)
    out.append(_table(["Relation", "Edges"], sorted(rel_counts.items(), key=lambda x: -x[1])))

    out.append("\n\n## Registry coverage\n")
    curated = [d for *_, d in edges if "curated" in d["sources"]]
    nodes = [d for _, d in g.nodes(data=True)]
    out.append(_table(["Measure", "Value"], [
        ["Seeds with an RRID", _pct(sum(bool(d["rrid"]) for d in nodes), len(nodes))],
        ["Seeds with a FAIRsharing record", _pct(sum(bool(d["fairsharing"]) for d in nodes), len(nodes))],
        ["Curated edges also linked in a registry", _pct(sum(d["in_registry"] for d in curated), len(curated))],
        ["Curated edges expert-verified", _pct(sum(bool(d.get("verified")) for d in curated), len(curated))],
    ]))

    out.append("\n\n## Cross-community bridges (strict)\n")
    rows = [[g.nodes[u]["label"], d["relation"], g.nodes[v]["label"],
             f"{g.nodes[u]['home']} → {g.nodes[v]['home']}", _plain(d["sources"])]
            for u, v, d in sorted(edges, key=lambda x: (x[0], x[1])) if d["scope_strict"] == "cross_community"]
    out.append(_table(["Source", "Relation", "Target", "Communities", "Evidence source"], rows) if rows else "_none_")
    return "\n".join(out) + "\n"


def gap_markdown(result: BuildResult, nodes: dict[str, Node]) -> str:
    g = result.graph
    out = ["# Ecosystem knowledge graph — gap report\n",
           f"*Generated {date.today().isoformat()} by `ecokg report`. Use this list to ask standard/archive "
           f"teams to complete their FAIRsharing and RRID records.*\n"]

    missing_rrid = [n for n in nodes.values() if not n.rrid]
    missing_fs = [n for n in nodes.values() if not n.fairsharing]
    out.append(f"## Seeds without a verified RRID ({len(missing_rrid)})\n")
    out.append(", ".join(f"{n.label}" for n in missing_rrid) or "_none_")
    out.append(f"\n\n## Seeds without a FAIRsharing record ({len(missing_fs)})\n")
    out.append(", ".join(f"{n.label}" for n in missing_fs) or "_none_")

    not_in_registry = [(u, v, d) for u, v, d in g.edges(data=True)
                       if "curated" in d["sources"] and not d["in_registry"]]
    out.append(f"\n\n## Curated relationships missing from registries ({len(not_in_registry)})\n")
    out.append("Relationships documented by the community but not recorded in FAIRsharing or RRID. "
               "These are candidates for record updates by the respective teams.\n")
    out.append(_table(["Source", "Relation", "Target", "Confidence", "Evidence"],
                      [[g.nodes[u]["label"], d["relation"], g.nodes[v]["label"], d.get("confidence", ""),
                        d.get("evidence", "")] for u, v, d in sorted(not_in_registry, key=lambda x: (x[0], x[1]))]))

    isolated = [g.nodes[n]["label"] for n in g.nodes if g.degree(n) == 0]
    out.append(f"\n\n## Seeds with no relationships ({len(isolated)})\n")
    out.append(", ".join(isolated) or "_none_")

    out.append(f"\n\n## Registry neighbours that are not seeds ({len(result.candidates)})\n")
    out.append("Records linked from seeds in a registry. Review whether any belong in seeds.yaml.\n")
    out.append(_table(["Registry", "ID", "Name", "Linked from", "Labels"],
                      [[c.registry, c.other_id, c.name, ", ".join(sorted(c.linked_from)),
                        ", ".join(sorted(c.labels))] for c in result.candidates[:100]]))

    if result.unknown_labels:
        out.append("\n\n## Unmapped registry relation labels\n")
        out.append("Add these to `relation_label_map` in taxonomy.yaml:\n")
        for reg, labels in result.unknown_labels.items():
            out.append(f"- {reg}: {', '.join(sorted(labels))}")
    return "\n".join(out) + "\n"
