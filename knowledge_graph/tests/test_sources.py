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
    raw = fixture_json("fairsharing_record.json")
    rec = fairsharing.parse_record(raw)
    assert rec.id == 1131
    assert rec.name == "Neurodata Without Borders"  # "FAIRsharing record for: " prefix stripped
    assert rec.doi == "FAIRsharing.nPfuTE"
    assert (rec.registry, rec.type, rec.status) == ("Standard", "model_and_format", "ready")
    assert rec.subjects == ["Neurophysiology"]
    assert rec.associations == [
        ("related_to", "out", 55, "Hierarchical Data Format"),
        ("implements", "in", 3322, "Distributed Archives for Neurophysiology Data Integration"),
        ("collects", "in", 900, "INCF Endorsed standards"),
    ]
    # Search hits are the bare record objects (no "data" wrapper).
    assert fairsharing.parse_record(raw["data"]) == rec


def test_resolve_matches_name_without_prefix(monkeypatch, tmp_path, fixture_json):
    from ecokg.http import CachedJsonClient

    nwb = fixture_json("fairsharing_record.json")["data"]
    other = {"id": "7", "attributes": {"name": "FAIRsharing record for: Nucleic acid format", "abbreviation": None}}
    client = fairsharing.FairsharingClient(CachedJsonClient(tmp_path), token="t")
    queries = []
    monkeypatch.setattr(client, "search", lambda q, refresh=False: queries.append(q) or [
        fairsharing.parse_record(other), fairsharing.parse_record(nwb)])
    hits = client.resolve("Neurodata Without Borders", "NWB")
    assert queries == ["NWB", "Neurodata Without Borders"]
    assert [r.id for r in hits] == [1131]


def test_strip_doi():
    assert fairsharing.strip_doi("https://doi.org/10.25504/FAIRsharing.abc") == "FAIRsharing.abc"
    assert fairsharing.strip_doi(None) is None


def test_fairsharing_token_auth_skips_sign_in(monkeypatch, tmp_path):
    from ecokg.http import CachedJsonClient

    monkeypatch.setenv("FAIRSHARING_TOKEN", "  Bearer eyJabc.def  ")
    http = CachedJsonClient(tmp_path)
    monkeypatch.setattr(http.session, "post", lambda *a, **k: (_ for _ in ()).throw(AssertionError("sign_in called")))
    client = fairsharing.FairsharingClient(http)
    client._authenticate()
    assert http.session.headers["Authorization"] == "Bearer eyJabc.def"


def test_fairsharing_requires_credentials(monkeypatch, tmp_path):
    from ecokg.http import CachedJsonClient

    for var in ("FAIRSHARING_TOKEN", "FAIRSHARING_LOGIN", "FAIRSHARING_PASSWORD"):
        monkeypatch.delenv(var, raising=False)
    try:
        fairsharing.FairsharingClient(CachedJsonClient(tmp_path))._authenticate()
    except RuntimeError as exc:
        assert "FAIRSHARING_TOKEN" in str(exc)
    else:
        raise AssertionError("expected RuntimeError")


def test_fairsharing_get_record_uses_rest(monkeypatch, tmp_path):
    from ecokg.http import CachedJsonClient

    http = CachedJsonClient(tmp_path)
    calls = []

    def fake_request(method, url, **kwargs):
        calls.append((method, url))
        return {"data": {"id": "5", "attributes": {"name": "X", "record_associations": []}}}

    monkeypatch.setattr(http, "request", fake_request)
    rec = fairsharing.FairsharingClient(http, token="t").get_record(5)
    assert calls == [("GET", f"{fairsharing.API_URL}/fairsharing_records/5")]
    assert (rec.id, rec.name) == (5, "X")


def test_clean_token_and_summary():
    import base64
    import json
    import time

    payload = base64.urlsafe_b64encode(json.dumps({"exp": time.time() + 600, "sub": "1"}).encode()).decode().rstrip("=")
    jwt = f"eyJhbGciOiJIUzI1NiJ9.{payload}.sig"
    for pasted in (jwt, f"Bearer {jwt}", f"Authorization: Bearer {jwt}", f'"Bearer {jwt}"\n'):
        assert fairsharing._clean_token(pasted) == jwt
    info = fairsharing.token_summary(jwt)
    assert info["segments"] == 3 and info["starts_with_eyJ"] and info["claims"] == ["exp", "sub"]
    assert 8 <= info["expires_in_minutes"] <= 10
    assert jwt not in str(info) and payload not in str(info)
    assert fairsharing.token_summary(None) == {"present": False}
