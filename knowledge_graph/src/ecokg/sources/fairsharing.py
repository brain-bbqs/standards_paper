"""FAIRsharing harvesting.

The FAIRsharing API requires a (free) account. Authentication, in order of preference:

* ``FAIRSHARING_TOKEN`` - a JWT used as-is. Needed for accounts that log in via GitHub/ORCID
  (no password). Copy it from the ``Authorization: Bearer ...`` header of any request to
  api.fairsharing.org in the browser's developer tools while logged in to fairsharing.org.
* ``FAIRSHARING_LOGIN`` / ``FAIRSHARING_PASSWORD`` - exchanged for a JWT via
  ``POST /users/sign_in`` (same flow as the ``fairsharing-client`` package).

The token is only kept in the session headers; it is never written to the cache or logs.

API access also requires the account to be linked to an organisation
(https://fairsharing.org/profiles/edit); otherwise every request returns 401.

Records are fetched from the REST API (``GET /fairsharing_records/{id}``); the GraphQL
endpoint used by the FAIRsharing web front-end is not available to API users (501).
Search hits and records share the same JSON:API shape (see ``parse_record``). Raw responses
are cached under data/cache/fairsharing/.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field

from ..http import CachedJsonClient

API_URL = "https://api.fairsharing.org"
DOI_PREFIX = "10.25504/"
NAME_PREFIX = "FAIRsharing record for: "   # the REST API prepends this to every record name


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
    # (raw relation label, direction 'out'|'in', other record id, other record name)
    associations: list[tuple[str, str, int, str]] = field(default_factory=list)


def strip_doi(doi: str | None) -> str | None:
    if not doi:
        return None
    doi = doi.replace("https://doi.org/", "")
    return doi[len(DOI_PREFIX):] if doi.startswith(DOI_PREFIX) else doi


def strip_name(name: str | None) -> str:
    name = name or ""
    return name[len(NAME_PREFIX):] if name.startswith(NAME_PREFIX) else name


def parse_record(raw: dict) -> FairsharingRecord:
    """Parse a REST JSON:API record (``{"data": {...}}`` or a single search hit).

    Outgoing links are in ``linked_records`` (``linked_record_id``/``_name``), incoming links
    in ``linking_records`` (``linking_record_id``/``_name``); each has a ``relation`` label.
    """
    rec = raw.get("data", raw)
    attrs = rec.get("attributes", {})
    associations = []
    for direction, list_key, prefix in (("out", "linked_records", "linked_record"),
                                        ("in", "linking_records", "linking_record")):
        for link in attrs.get(list_key) or []:
            associations.append((link.get("relation") or "undefined", direction,
                                 int(link[f"{prefix}_id"]), link.get(f"{prefix}_name", "")))
    metadata = attrs.get("metadata") or {}
    return FairsharingRecord(
        id=int(rec["id"]) if str(rec.get("id", "")).isdigit() else None,
        name=strip_name(attrs.get("name")),
        abbreviation=attrs.get("abbreviation"),
        doi=strip_doi(attrs.get("doi")),
        registry=attrs.get("fairsharing_registry"),
        type=attrs.get("record_type"),
        status=metadata.get("status"),
        subjects=list(attrs.get("subjects") or []),
        domains=list(attrs.get("domains") or []),
        associations=associations,
    )


def _clean_token(token: str | None) -> str | None:
    """Accept a bare JWT or a pasted header (``Authorization: Bearer eyJ...``, optionally quoted)."""
    if not token:
        return None
    token = token.strip().strip("'\"").strip()
    if token.lower().startswith("authorization:"):
        token = token.split(":", 1)[1].strip()
    if token.lower().startswith("bearer "):
        token = token.split(None, 1)[1]
    return token.strip().strip("'\"") or None


def token_summary(token: str | None) -> dict:
    """Describe a JWT without revealing it: shape, claim names, and expiry."""
    import base64
    import json
    import time

    if not token:
        return {"present": False}
    parts = token.split(".")
    info = {"present": True, "length": len(token), "segments": len(parts), "starts_with_eyJ": token.startswith("eyJ"),
            "has_whitespace": any(c.isspace() for c in token)}
    if len(parts) == 3:
        try:
            payload = json.loads(base64.urlsafe_b64decode(parts[1] + "=" * (-len(parts[1]) % 4)))
            info["claims"] = sorted(payload)
            if "exp" in payload:
                info["expires_in_minutes"] = round((payload["exp"] - time.time()) / 60)
        except ValueError:
            info["payload_decodable"] = False
    return info


class FairsharingClient:
    def __init__(self, http: CachedJsonClient, login: str | None = None, password: str | None = None,
                 token: str | None = None):
        self.http = http
        self.login = login or os.environ.get("FAIRSHARING_LOGIN")
        self.password = password or os.environ.get("FAIRSHARING_PASSWORD")
        self._jwt = _clean_token(token or os.environ.get("FAIRSHARING_TOKEN"))
        self._authenticated = False

    def _authenticate(self) -> None:
        if self._authenticated:
            return
        if not self._jwt:
            if not (self.login and self.password):
                raise RuntimeError(
                    "FAIRsharing requires an account: set FAIRSHARING_TOKEN (GitHub/ORCID logins) or "
                    "FAIRSHARING_LOGIN and FAIRSHARING_PASSWORD (register for free at https://fairsharing.org)."
                )
            resp = self.http.session.post(
                f"{API_URL}/users/sign_in",
                json={"user": {"login": self.login, "password": self.password}},
                timeout=60,
            )
            resp.raise_for_status()
            self._jwt = resp.json()["jwt"]
        self._authenticated = True
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
        """Fetch one record, including associations (REST)."""
        cache_key = f"fairsharing_record_{record_id}"
        raw = None if refresh else self.http.cached(cache_key)
        if raw is None:
            self._authenticate()
            raw = self.http.request("GET", f"{API_URL}/fairsharing_records/{int(record_id)}",
                                    cache_key=cache_key, refresh=True)
        return parse_record(raw)

    def resolve(self, name: str, abbreviation: str | None) -> list[FairsharingRecord]:
        """Candidate records whose name or abbreviation matches a seed (case-insensitive)."""
        wanted = {s.lower() for s in (name, abbreviation) if s}
        hits: dict[int, FairsharingRecord] = {}
        for query in dict.fromkeys(q for q in (abbreviation, name) if q):  # abbreviation first
            for r in self.search(query):
                hits.setdefault(r.id, r)
        exact = [r for r in hits.values() if {r.name.lower(), (r.abbreviation or "").lower()} & wanted]
        return exact or list(hits.values())[:5]
