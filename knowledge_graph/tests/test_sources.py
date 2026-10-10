import requests

from ecokg.sources import fairsharing, rrid


def test_parse_rrid_record(fixture_json):
    rec = rrid.parse_record(fixture_json("rrid_record.json"))
    assert rec.rrid == "SCR_015242"
    assert rec.name == "Neurodata Without Borders"
    assert rec.abbreviations == ["NWB"]
    assert rec.keywords == ["data standard"]
    # Duplicates (same label + normalized target) are kept once.
    assert sorted(rec.relations) == [
        ("has_parent_organization", "SCR_004257", "Janelia Research"),
        ("is_related_to", "SCR_021303", "Hierarchical Data Modeling Framework"),
        ("is_used_by", "SCR_017571", "DANDI"),
    ]


def test_parse_rrid_record_empty():
    assert rrid.parse_record({"hits": {"hits": []}}) is None
    assert rrid.normalize_rrid(" rrid:scr_123 ") == "SCR_123"


class _FakeHttp:
    def __init__(self, status):
        self.status = status

    def request(self, *args, **kwargs):
        resp = requests.Response()
        resp.status_code = self.status
        raise requests.HTTPError(response=resp)


def test_rrid_fetch_404_returns_none():
    assert rrid.RridClient(_FakeHttp(404)).fetch("SCR_016667") is None


def test_rrid_fetch_other_errors_raise():
    try:
        rrid.RridClient(_FakeHttp(403)).fetch("SCR_1")
    except requests.HTTPError:
        pass
    else:
        raise AssertionError("expected HTTPError")


def test_parse_fairsharing_record(fixture_json):
    rec = fairsharing.parse_record(fixture_json("fairsharing_record.json"))
    assert rec.id == 1234
    assert rec.doi == "FAIRsharing.nwb000"
    assert rec.registry == "Standard"
    assert rec.subjects == ["Neurophysiology"]
    assert rec.associations == [
        ("uses", "out", 55, "FAIRsharing.hdf500", "Hierarchical Data Format 5"),
        ("implements", "in", 77, None, "DANDI Archive"),
    ]


def test_parse_fairsharing_rest_snake_case():
    raw = {"data": {"id": "9", "attributes": {
        "name": "X", "fairsharing_registry": {"name": "Standard"}, "record_type": "terminology_artefact",
        "record_associations": [{"record_assoc_label": {"relation": "extends"},
                                 "linked_record": {"id": "3", "name": "Y"}}]}}}
    rec = fairsharing.parse_record(raw)
    assert (rec.id, rec.registry, rec.type) == (9, "Standard", "terminology_artefact")
    assert rec.associations == [("extends", "out", 3, None, "Y")]


def test_strip_doi():
    assert fairsharing.strip_doi("https://doi.org/10.25504/FAIRsharing.abc") == "FAIRsharing.abc"
    assert fairsharing.strip_doi(None) is None
