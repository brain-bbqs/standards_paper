"""FAIRsharing harvesting.

The FAIRsharing API requires a (free) account. Credentials are read from the
``FAIRSHARING_LOGIN`` and ``FAIRSHARING_PASSWORD`` environment variables and exchanged
for a JWT via ``POST /users/sign_in`` (same flow as the ``fairsharing-client`` package).

Record relationships are requested through the GraphQL endpoint using the field names
used by FAIRsharing's own web front-end (``recordAssociations`` /
``reverseRecordAssociations`` with ``linkedRecord`` / ``fairsharingRecord`` and
``recordAssocLabel``). ``parse_record`` also accepts snake_case variants so REST
responses can be parsed if the GraphQL route is unavailable.

NOTE: written without live credentials; verify field names on first authenticated run
(raw responses are cached under data/cache/fairsharing/ for inspection).
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field

from ..http import CachedJsonClient

API_URL = "https://api.fairsharing.org"
DOI_PREFIX = "10.25504/"

RECORD_QUERY = """
query($id: Int!) {
  fairsharingRecord(id: $id) {
    id name abbreviation doi registry type status homepage
    subjects { label } domains { label } taxonomies { label }
    recordAssociations {
      recordAssocLabel
      linkedRecord { id name abbreviation doi registry type status }
    }
    reverseRecordAssociations {
      recordAssocLabel
      fairsharingRecord { id name abbreviation doi registry type status }
    }
  }
}
"""


@dataclass
class FairsharingRecord:
    id: int | None
    name: str
    abbreviation: str | None = None
    doi: str | None = None              # e.g. FAIRsharing.abc123 (prefix stripped)
    registry: str | None = None         # Standard | Database | Policy | Collection
    type: str | None = None             # e.g. model_and_format, terminology_artefact, repository
    status: str | None = None
    subjects: list[str] = field(default_factory=list)
    domains: list[str] = field(default_factory=list)
    # (raw relation label, direction 'out'|'in', other record id, other DOI, other name)
    associations: list[tuple[str, str, int | None, str | None, str]] = field(default_factory=list)


def strip_doi(doi: str | None) -> str | None:
    if not doi:
        return None
    doi = doi.replace("https://doi.org/", "")
    return doi[len(DOI_PREFIX):] if doi.startswith(DOI_PREFIX) else doi


def _get(d: dict, *names, default=None):
    for n in names:
        if isinstance(d, dict) and n in d and d[n] is not None:
            return d[n]
    return default


def _labels(items) -> list[str]:
    out = []
    for it in items or []:
        label = it.get("label") if isinstance(it, dict) else it
        if label:
            out.append(label)
    return out


def _type_name(value) -> str | None:
    if isinstance(value, dict):
        return value.get("name") or value.get("label")
    return value


def parse_record(raw: dict) -> FairsharingRecord:
    """Parse a GraphQL ``fairsharingRecord`` or a REST JSON:API record."""
    rec = raw
    for key in ("data", "fairsharingRecord"):
        if isinstance(rec, dict) and key in rec and isinstance(rec[key], dict):
            rec = rec[key]
    attrs = rec.get("attributes", rec)

    associations = []
    for direction, list_keys, other_keys in (
        ("out", ("recordAssociations", "record_associations"), ("linkedRecord", "linked_record")),
        ("in", ("reverseRecordAssociations", "reverse_record_associations"),
         ("fairsharingRecord", "fairsharing_record")),
    ):
        for assoc in _get(attrs, *list_keys, default=[]) or []:
            other = _get(assoc, *other_keys, default={}) or {}
            label = _get(assoc, "recordAssocLabel", "record_assoc_label", "relation", default="undefined")
            if isinstance(label, dict):
                label = label.get("relation") or label.get("label") or "undefined"
            other_id = _get(other, "id")
            associations.append((
                str(label),
                direction,
                int(other_id) if other_id is not None and str(other_id).isdigit() else None,
                strip_doi(_get(other, "doi")),
                _get(other, "name", default=""),
            ))

    rec_id = _get(rec, "id")
    return FairsharingRecord(
        id=int(rec_id) if rec_id is not None and str(rec_id).isdigit() else None,
        name=_get(attrs, "name", default=""),
        abbreviation=_get(attrs, "abbreviation"),
        doi=strip_doi(_get(attrs, "doi")),
        registry=_type_name(_get(attrs, "registry", "fairsharing_registry")),
        type=_type_name(_get(attrs, "type", "record_type")),
        status=_get(attrs, "status"),
        subjects=_labels(_get(attrs, "subjects", default=[])),
        domains=_labels(_get(attrs, "domains", default=[])),
        associations=associations,
    )


class FairsharingClient:
    def __init__(self, http: CachedJsonClient, login: str | None = None, password: str | None = None):
        self.http = http
        self.login = login or os.environ.get("FAIRSHARING_LOGIN")
        self.password = password or os.environ.get("FAIRSHARING_PASSWORD")
        self._jwt = None

    def _authenticate(self) -> None:
        if self._jwt:
            return
        if not (self.login and self.password):
            raise RuntimeError(
                "FAIRsharing requires an account: set FAIRSHARING_LOGIN and FAIRSHARING_PASSWORD "
                "(register for free at https://fairsharing.org)."
            )
        resp = self.http.session.post(
            f"{API_URL}/users/sign_in",
            json={"user": {"login": self.login, "password": self.password}},
            timeout=60,
        )
        resp.raise_for_status()
        self._jwt = resp.json()["jwt"]
        self.http.session.headers["Authorization"] = f"Bearer {self._jwt}"
        self.http.session.headers["Content-Type"] = "application/json"

    def search(self, query: str, refresh: bool = False) -> list[FairsharingRecord]:
        """Full-text search (REST)."""
        cache_key = f"fairsharing_search_{query}"
        raw = None if refresh else self.http.cached(cache_key)
        if raw is None:
            self._authenticate()
            raw = self.http.request("POST", f"{API_URL}/search/fairsharing_records",
                                    params={"q": query}, cache_key=cache_key, refresh=True)
        items = raw.get("data", raw if isinstance(raw, list) else [])
        return [parse_record(item) for item in items]

    def get_record(self, record_id: int, refresh: bool = False) -> FairsharingRecord:
        """Fetch one record, including associations (GraphQL)."""
        cache_key = f"fairsharing_record_{record_id}"
        raw = None if refresh else self.http.cached(cache_key)
        if raw is None:
            self._authenticate()
            raw = self.http.request("POST", f"{API_URL}/graphql",
                                    json={"query": RECORD_QUERY, "variables": {"id": int(record_id)}},
                                    cache_key=cache_key, refresh=True)
            if raw.get("errors"):
                raise RuntimeError(f"FAIRsharing GraphQL error for {record_id}: {raw['errors']}")
        return parse_record(raw.get("data", raw))

    def resolve(self, name: str, abbreviation: str | None) -> list[FairsharingRecord]:
        """Candidate records whose name or abbreviation matches a seed (case-insensitive)."""
        wanted = {s.lower() for s in (name, abbreviation) if s}
        hits = self.search(abbreviation or name)
        exact = [r for r in hits if {(r.name or "").lower(), (r.abbreviation or "").lower()} & wanted]
        return exact or hits[:5]
