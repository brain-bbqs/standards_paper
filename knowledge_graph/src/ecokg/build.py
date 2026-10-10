"""Assemble the knowledge graph from seeds, curated edges, and harvested registry edges.

Harvested edges are stored as JSON lists in data/harvested/ (one file per registry),
written by the ``harvest-*`` CLI commands. Each item:

    {"registry": "rrid" | "fairsharing",
     "node": <seed id the record belongs to>,
     "label": <raw relation label>,
     "direction": "out" | "in",          # "in" = the other record points at this seed
     "other_id": <registry id of the other record>,
     "other_name": <name of the other record>}
"""

from __future__ import annotations

import json
import logging
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import networkx as nx

from . import HARVEST_DIR
from .classify import community_scope, infer_relation, layer_span
from .model import Edge, Node, Taxonomy

log = logging.getLogger(__name__)

REGISTRIES = ("rrid", "fairsharing")


@dataclass
class Candidate:
    """A registry record linked from seeds but not itself a seed (possible addition)."""
    registry: str
    other_id: str
    name: str
    linked_from: set[str] = field(default_factory=set)
    labels: set[str] = field(default_factory=set)


@dataclass
class BuildResult:
    graph: nx.MultiDiGraph
    candidates: list[Candidate]
    unknown_labels: dict[str, set[str]]


def load_harvested(harvest_dir: Path = HARVEST_DIR) -> list[dict]:
    items = []
    for registry in REGISTRIES:
        path = Path(harvest_dir) / f"{registry}_edges.json"
        if path.exists():
            items.extend(json.loads(path.read_text()))
    return items


def _registry_index(nodes: dict[str, Node]) -> dict[tuple[str, str], str]:
    """Map (registry, registry id) -> seed id."""
    index = {}
    for n in nodes.values():
        for rrid in n.rrids:
            index[("rrid", rrid.upper())] = n.id
        if n.fairsharing:
            index[("fairsharing", n.fairsharing)] = n.id
    return index


def normalize_label(taxonomy: Taxonomy, registry: str, label: str,
                    unknown: dict[str, set[str]]) -> str | None:
    mapping = taxonomy.relation_label_map.get(registry, {})
    if label in mapping:
        return mapping[label]
    unknown[registry].add(label)
    return "related_to"


def build_graph(taxonomy: Taxonomy, nodes: dict[str, Node], curated: list[Edge],
                harvested: list[dict] | None = None,
                fairsharing_ids: dict[str, str] | None = None) -> BuildResult:
    """Build a MultiDiGraph with one edge per (source, target, relation).

    ``fairsharing_ids`` maps numeric FAIRsharing record ids to seed ids, for harvested
    associations that only carry the numeric id of the other record.
    """
    harvested = harvested or []
    g = nx.MultiDiGraph()
    for n in nodes.values():
        g.add_node(n.id, label=n.label, name=n.name, layer=n.layer, home=n.home,
                   communities=n.communities, also_layers=n.also_layers, kind=n.kind or "",
                   rrid=n.rrid or "", fairsharing=n.fairsharing or "")

    def add(src: str, tgt: str, relation: str, **attrs):
        if g.has_edge(src, tgt, key=relation):
            data = g.edges[src, tgt, relation]
            data["sources"] |= attrs.pop("sources")
            data["registry_labels"] |= attrs.pop("registry_labels", set())
            for k, v in attrs.items():
                data.setdefault(k, v)
            return
        a, b = nodes[src], nodes[tgt]
        g.add_edge(src, tgt, key=relation, relation=relation,
                   span=layer_span(a, b),
                   scope_strict=community_scope(a, b, taxonomy, "strict"),
                   scope_lenient=community_scope(a, b, taxonomy, "lenient"),
                   registry_labels=attrs.pop("registry_labels", set()),
                   **attrs)

    for e in curated:
        add(e.source, e.target, e.relation, sources={"curated"}, provenance=e.provenance,
            evidence=e.evidence, confidence=e.confidence, verified=e.verified)

    index = _registry_index(nodes)
    for fs_id, seed in (fairsharing_ids or {}).items():
        index[("fairsharing", str(fs_id))] = seed
    candidates: dict[tuple[str, str], Candidate] = {}
    unknown: dict[str, set[str]] = defaultdict(set)

    for item in harvested:
        registry, seed, label = item["registry"], item["node"], item["label"]
        relation = normalize_label(taxonomy, registry, label, unknown)
        if relation is None:
            continue  # not an ecosystem relationship (tool listing, parent organization, ...)
        other_key = (registry, str(item["other_id"]).upper() if registry == "rrid" else str(item["other_id"]))
        other = index.get(other_key)
        if other is None:
            cand = candidates.setdefault(other_key, Candidate(registry, other_key[1], item.get("other_name", "")))
            cand.linked_from.add(seed)
            cand.labels.add(label)
            continue
        if other == seed:
            continue
        src, tgt = (seed, other) if item.get("direction", "out") == "out" else (other, seed)
        if relation == "by_layer":
            relation = infer_relation(nodes[src], nodes[tgt])
        add(src, tgt, relation, sources={registry}, registry_labels={f"{registry}:{label}"})

    _mark_registry_confirmation(g)
    return BuildResult(g, sorted(candidates.values(), key=lambda c: (-len(c.linked_from), c.name)),
                       dict(unknown))


def _mark_registry_confirmation(g: nx.MultiDiGraph) -> None:
    """Flag curated edges whose node pair is linked in at least one registry (any relation)."""
    registry_pairs = set()
    for u, v, d in g.edges(data=True):
        if d["sources"] & set(REGISTRIES):
            registry_pairs.add(frozenset((u, v)))
    for u, v, d in g.edges(data=True):
        d["in_registry"] = frozenset((u, v)) in registry_pairs
