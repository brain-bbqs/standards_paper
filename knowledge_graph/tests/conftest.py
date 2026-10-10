import json
from pathlib import Path

import pytest

from ecokg.model import Edge, Node, Taxonomy, load_taxonomy

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def fixture_json():
    return lambda name: json.loads((FIXTURES / name).read_text())


@pytest.fixture
def taxonomy() -> Taxonomy:
    return load_taxonomy()


@pytest.fixture
def nodes() -> dict[str, Node]:
    """A tiny ecosystem: archive -> standard -> format, plus a cross-cutting ontology."""
    ns = [
        Node("dandi", "DANDI Archive", "archive", ["neurophysiology"], rrid="SCR_017571"),
        Node("nwb", "Neurodata Without Borders", "data_standard", ["neurophysiology", "behavior"],
             abbreviation="NWB", rrid="SCR_015242", fairsharing="FAIRsharing.nwb000"),
        Node("bids", "Brain Imaging Data Structure", "dataset_organization", ["neuroimaging", "behavior"],
             abbreviation="BIDS", rrid="SCR_016124", rrid_aliases=["SCR_999999"]),
        Node("hdf5", "Hierarchical Data Format 5", "data_format", ["general"],
             abbreviation="HDF5", fairsharing="FAIRsharing.hdf500"),
        Node("hdmf_spec", "HDMF specification language", "schema_language", ["neurophysiology"],
             rrid="SCR_021303"),
        Node("ncbi_taxonomy", "NCBI Taxonomy", "ontology_terminology", ["biology"]),
    ]
    return {n.id: n for n in ns}


@pytest.fixture
def curated() -> list[Edge]:
    return [
        Edge("nwb", "hdf5", "uses_format", "notes", confidence="high"),
        Edge("nwb", "hdmf_spec", "defined_with", "notes", confidence="high"),
        Edge("dandi", "nwb", "accepts", "poster", confidence="high"),
        Edge("bids", "nwb", "organizes", "docs"),
        Edge("nwb", "ncbi_taxonomy", "uses_terminology", "notes"),
    ]
