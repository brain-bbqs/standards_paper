"""Load and validate the curated inputs: taxonomy, seed nodes, and curated edges."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml

from . import DATA_DIR

CONFIDENCE_LEVELS = ("high", "medium", "low")
PROVENANCES = ("poster", "notes", "guideline", "docs", "expert", "bbqs_inventory")


@dataclass
class Taxonomy:
    layers: dict
    communities: dict
    cross_cutting: set[str]
    relations: dict
    relation_label_map: dict
    symmetric: set[str] = field(default_factory=set)

    def layer_order(self, layer: str) -> int:
        return self.layers[layer]["order"]


@dataclass
class Node:
    id: str
    name: str
    layer: str
    communities: list[str]
    abbreviation: str | None = None
    also_layers: list[str] = field(default_factory=list)
    kind: str | None = None
    rrid: str | None = None
    rrid_aliases: list[str] = field(default_factory=list)
    fairsharing: str | None = None
    homepage: str | None = None
    sources: list[str] = field(default_factory=list)

    @property
    def label(self) -> str:
        return self.abbreviation or self.name

    @property
    def rrids(self) -> list[str]:
        """Primary RRID first, then aliases (duplicate registry records)."""
        return [r for r in [self.rrid, *self.rrid_aliases] if r]

    @property
    def home(self) -> str:
        return self.communities[0]


@dataclass
class Edge:
    source: str
    target: str
    relation: str
    provenance: str
    evidence: str = ""
    confidence: str = "medium"
    verified: bool = False
    verified_by: str | None = None


def _read_yaml(path: Path) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def load_taxonomy(path: Path = DATA_DIR / "taxonomy.yaml") -> Taxonomy:
    d = _read_yaml(path)
    return Taxonomy(
        layers=d["layers"],
        communities=d["communities"],
        cross_cutting=set(d.get("cross_cutting_communities", [])),
        relations=d["relations"],
        relation_label_map=d.get("relation_label_map", {}),
        symmetric=set(d.get("symmetric_relations", [])),
    )


def load_seeds(path: Path = DATA_DIR / "seeds.yaml") -> dict[str, Node]:
    nodes = {}
    for raw in _read_yaml(path)["nodes"]:
        node = Node(**raw)
        if node.id in nodes:
            raise ValueError(f"duplicate node id: {node.id}")
        nodes[node.id] = node
    return nodes


def load_curated_edges(path: Path = DATA_DIR / "curated_edges.yaml") -> list[Edge]:
    return [Edge(**raw) for raw in _read_yaml(path)["edges"]]


def validate(taxonomy: Taxonomy, nodes: dict[str, Node], edges: list[Edge]) -> list[str]:
    """Return a list of human-readable problems (empty list = valid)."""
    errors = []
    for n in nodes.values():
        for layer in [n.layer, *n.also_layers]:
            if layer not in taxonomy.layers:
                errors.append(f"node {n.id}: unknown layer {layer!r}")
        if not n.communities:
            errors.append(f"node {n.id}: needs at least one community")
        for c in n.communities:
            if c not in taxonomy.communities:
                errors.append(f"node {n.id}: unknown community {c!r}")
        for rrid in n.rrids:
            if not rrid.startswith("SCR_"):
                errors.append(f"node {n.id}: RRID should look like SCR_xxxxxx, got {rrid!r}")
        if n.rrid_aliases and not n.rrid:
            errors.append(f"node {n.id}: rrid_aliases given without a primary rrid")
        for s in n.sources:
            if s not in PROVENANCES:
                errors.append(f"node {n.id}: unknown source {s!r}")
    seen = set()
    for e in edges:
        where = f"edge {e.source} -{e.relation}-> {e.target}"
        for end in (e.source, e.target):
            if end not in nodes:
                errors.append(f"{where}: unknown node {end!r}")
        if e.relation not in taxonomy.relations:
            errors.append(f"{where}: unknown relation {e.relation!r}")
        if e.provenance not in PROVENANCES:
            errors.append(f"{where}: unknown provenance {e.provenance!r}")
        if e.confidence not in CONFIDENCE_LEVELS:
            errors.append(f"{where}: confidence must be one of {CONFIDENCE_LEVELS}")
        if e.source == e.target:
            errors.append(f"{where}: self-loop")
        key = ((min(e.source, e.target), max(e.source, e.target), e.relation)
               if e.relation in taxonomy.symmetric else (e.source, e.target, e.relation))
        if key in seen:
            errors.append(f"{where}: duplicate edge")
        seen.add(key)
    return errors
