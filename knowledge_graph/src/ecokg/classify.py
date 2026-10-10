"""Edge classification used for the paper's "vertical vs. horizontal bridges" analysis.

Two independent dimensions:

* layer span     - ``within_layer`` or ``cross_layer`` (vertical links through the stack)
* community scope - ``within_community``, ``cross_community`` (a bridge between research
  communities/modalities), or ``shared`` (one end is cross-cutting infrastructure, e.g.,
  HDF5, JSON, LinkML, NCBI Taxonomy)

Community scope is computed in two modes so the result's sensitivity to how broadly
nodes are tagged can be reported:

* ``strict``  - compare home communities (first listed community of each node)
* ``lenient`` - compare all non-cross-cutting communities; any overlap = within
"""

from __future__ import annotations

from .model import Node, Taxonomy

SCOPES = ("within_community", "cross_community", "shared")
SPANS = ("within_layer", "cross_layer")


def layer_span(a: Node, b: Node) -> str:
    return "within_layer" if a.layer == b.layer else "cross_layer"


def community_scope(a: Node, b: Node, taxonomy: Taxonomy, mode: str = "strict") -> str:
    cc = taxonomy.cross_cutting
    if mode == "strict":
        if a.home in cc or b.home in cc:
            return "shared"
        return "within_community" if a.home == b.home else "cross_community"
    if mode == "lenient":
        ca = set(a.communities) - cc
        cb = set(b.communities) - cc
        if not ca or not cb:
            return "shared"
        return "within_community" if ca & cb else "cross_community"
    raise ValueError(f"unknown mode {mode!r}")


def infer_relation(src: Node, tgt: Node) -> str:
    """Pick a normalized relation from the endpoint layers (for ambiguous registry labels)."""
    s, t = src.layer, tgt.layer
    if t == "schema_language" and s != "schema_language":
        return "defined_with"
    if t == "ontology_terminology" and s != "ontology_terminology":
        return "uses_terminology"
    if s == "archive" and t in ("dataset_organization", "data_standard", "data_format"):
        return "accepts"
    if s == "dataset_organization" and t in ("data_standard", "data_format"):
        return "organizes"
    if t == "data_format" and s in ("data_standard", "schema_language"):
        return "uses_format"
    return "related_to"
