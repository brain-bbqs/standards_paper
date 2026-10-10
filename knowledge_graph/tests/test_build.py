from ecokg.build import build_graph


def h(registry, node, label, other_id, direction="out", other_name=""):
    return {"registry": registry, "node": node, "label": label, "direction": direction,
            "other_id": other_id, "other_name": other_name}


def test_curated_only(taxonomy, nodes, curated):
    result = build_graph(taxonomy, nodes, curated)
    g = result.graph
    assert g.number_of_nodes() == len(nodes)
    assert g.number_of_edges() == len(curated)
    d = g.edges["bids", "nwb", "organizes"]
    assert d["sources"] == {"curated"}
    assert d["span"] == "cross_layer"
    assert d["scope_strict"] == "cross_community"
    assert d["scope_lenient"] == "within_community"
    assert not d["in_registry"]


def test_harvested_edges_merge_and_classify(taxonomy, nodes, curated):
    harvested = [
        h("rrid", "nwb", "is_related_to", "scr_021303"),             # case-insensitive RRID match
        h("rrid", "dandi", "uses", "SCR_015242"),                    # by_layer -> accepts, merges with curated
        h("rrid", "nwb", "has_parent_organization", "SCR_004257"),   # dropped (null mapping)
        h("rrid", "nwb", "lists", "SCR_000001", other_name="Tool"),  # dropped before becoming a candidate
        h("rrid", "nwb", "is_related_to", "SCR_888888", other_name="Viewer"),
        h("rrid", "dandi", "is_related_to", "SCR_888888", other_name="Viewer"),
        h("rrid", "nwb", "is_related_to", "SCR_999999"),             # alias of BIDS
        h("rrid", "nwb", "is_related_to", "SCR_015242"),             # self-link ignored
        h("rrid", "nwb", "brand_new_label", "SCR_017571"),           # unknown -> related_to, logged
        h("fairsharing", "nwb", "uses", "FAIRsharing.hdf500"),       # by_layer -> uses_format, merges
        h("fairsharing", "nwb", "implements", "77", direction="in"),  # numeric id via fairsharing_ids
    ]
    result = build_graph(taxonomy, nodes, curated, harvested, fairsharing_ids={"77": "dandi"})
    g = result.graph

    assert g.edges["nwb", "hdmf_spec", "related_to"]["sources"] == {"rrid"}
    accepts = g.edges["dandi", "nwb", "accepts"]
    assert accepts["sources"] == {"curated", "rrid", "fairsharing"}
    assert accepts["registry_labels"] == {"rrid:uses", "fairsharing:implements"}
    assert accepts["provenance"] == "poster"
    assert accepts["in_registry"]
    assert g.edges["nwb", "hdf5", "uses_format"]["sources"] == {"curated", "fairsharing"}
    assert g.has_edge("nwb", "bids", "related_to")
    assert g.has_edge("nwb", "dandi", "related_to")
    assert not any(u == v for u, v in g.edges())

    # Curated edge whose node pair has some registry link (any relation) counts as confirmed.
    assert g.edges["nwb", "hdmf_spec", "defined_with"]["in_registry"]
    assert not g.edges["nwb", "ncbi_taxonomy", "uses_terminology"]["in_registry"]

    assert [(c.other_id, c.linked_from) for c in result.candidates] == [("SCR_888888", {"nwb", "dandi"})]
    assert result.unknown_labels == {"rrid": {"brand_new_label"}}
