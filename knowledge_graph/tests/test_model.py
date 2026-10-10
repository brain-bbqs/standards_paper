from ecokg.model import Edge, Node, load_curated_edges, load_seeds, load_taxonomy, validate


def test_curated_data_is_valid():
    """The real seeds.yaml / curated_edges.yaml must always validate."""
    taxonomy, nodes, edges = load_taxonomy(), load_seeds(), load_curated_edges()
    assert validate(taxonomy, nodes, edges) == []


def test_node_properties():
    n = Node("x", "Long Name", "data_format", ["general", "biology"], rrid="SCR_1", rrid_aliases=["SCR_2"])
    assert n.label == "Long Name"
    assert n.home == "general"
    assert n.rrids == ["SCR_1", "SCR_2"]


def test_validate_reports_problems(taxonomy, nodes):
    bad_nodes = dict(nodes)
    bad_nodes["bad"] = Node("bad", "Bad", "not_a_layer", ["martian"], rrid="1234",
                            rrid_aliases=["nope"], sources=["rumor"])
    bad_nodes["orphan_alias"] = Node("orphan_alias", "O", "archive", ["general"], rrid_aliases=["SCR_3"])
    edges = [
        Edge("nwb", "missing", "uses_format", "notes"),
        Edge("nwb", "hdf5", "eats", "gossip", confidence="certain"),
        Edge("nwb", "nwb", "extends", "docs"),
        Edge("dandi", "nwb", "accepts", "poster"),
        Edge("dandi", "nwb", "accepts", "poster"),
    ]
    errors = "\n".join(validate(taxonomy, bad_nodes, edges))
    for expected in ("unknown layer 'not_a_layer'", "unknown community 'martian'", "got '1234'", "got 'nope'",
                     "unknown source 'rumor'", "rrid_aliases given without a primary rrid",
                     "unknown node 'missing'", "unknown relation 'eats'", "unknown provenance 'gossip'",
                     "confidence must be one of", "self-loop", "duplicate edge"):
        assert expected in errors
