import pytest

from ecokg.classify import community_scope, infer_relation, layer_span


def test_layer_span(nodes):
    assert layer_span(nodes["nwb"], nodes["hdf5"]) == "cross_layer"
    assert layer_span(nodes["nwb"], nodes["nwb"]) == "within_layer"


def test_community_scope_strict_vs_lenient(nodes, taxonomy):
    # BIDS (home neuroimaging) and NWB (home neurophysiology) both list behavior.
    assert community_scope(nodes["bids"], nodes["nwb"], taxonomy, "strict") == "cross_community"
    assert community_scope(nodes["bids"], nodes["nwb"], taxonomy, "lenient") == "within_community"
    assert community_scope(nodes["dandi"], nodes["nwb"], taxonomy, "strict") == "within_community"
    # Cross-cutting endpoints (general/biology) are "shared" in both modes.
    for mode in ("strict", "lenient"):
        assert community_scope(nodes["nwb"], nodes["hdf5"], taxonomy, mode) == "shared"
        assert community_scope(nodes["nwb"], nodes["ncbi_taxonomy"], taxonomy, mode) == "shared"
    with pytest.raises(ValueError):
        community_scope(nodes["nwb"], nodes["hdf5"], taxonomy, "fuzzy")


@pytest.mark.parametrize("src,tgt,expected", [
    ("nwb", "hdmf_spec", "defined_with"),
    ("nwb", "ncbi_taxonomy", "uses_terminology"),
    ("dandi", "nwb", "accepts"),
    ("bids", "nwb", "organizes"),
    ("nwb", "hdf5", "uses_format"),
    ("hdf5", "dandi", "related_to"),
])
def test_infer_relation(nodes, src, tgt, expected):
    assert infer_relation(nodes[src], nodes[tgt]) == expected
