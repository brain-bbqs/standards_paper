"""RRID / SciCrunch Registry harvesting.

Records are fetched anonymously from the public resolver
(https://scicrunch.org/resolver/RRID:SCR_xxxxxx.json). Each record lists typed
relationships to other registry resources under ``_source.graph`` (e.g.,
``is_related_to``, ``works_with``, ``lists``, ``has_parent_organization``).

Searching the registry by name requires a SciCrunch API key and is not implemented yet;
RRIDs for seeds are therefore curated in seeds.yaml and checked with ``ecokg rrid-check``.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import requests

from ..http import CachedJsonClient

RESOLVER_URL = "https://scicrunch.org/resolver/RRID:{rrid}.json"


@dataclass
class RridRecord:
    rrid: str
    name: str
    description: str = ""
    abbreviations: list[str] = field(default_factory=list)
    keywords: list[str] = field(default_factory=list)
    types: list[str] = field(default_factory=list)
    # (raw relation label, target RRID, target name)
    relations: list[tuple[str, str, str]] = field(default_factory=list)


def normalize_rrid(rrid: str) -> str:
    rrid = rrid.strip()
    if rrid.upper().startswith("RRID:"):
        rrid = rrid[5:]
    return rrid.upper()


def parse_record(raw: dict) -> RridRecord | None:
    hits = raw.get("hits", {}).get("hits", [])
    if not hits:
        return None
    src = hits[0]["_source"]
    item = src.get("item", {})
    relations = []
    seen = set()
    for group in ("relationships", "related", "parent"):
        for rel in src.get("graph", {}).get(group, []) or []:
            label = rel.get("relationship", {}).get("name")
            target = rel.get("resource", {}).get("identifier")
            if not label or not target:
                continue
            key = (label, normalize_rrid(target))
            if key in seen:
                continue
            seen.add(key)
            relations.append((*key, rel["resource"].get("name", "")))
    return RridRecord(
        rrid=normalize_rrid(item.get("identifier") or item.get("curie", "")),
        name=item.get("name", ""),
        description=item.get("description", ""),
        abbreviations=[a["name"] for a in item.get("abbreviations", []) if a.get("name")],
        keywords=[k["keyword"] for k in item.get("keywords", []) if k.get("keyword")],
        types=[t["name"] for t in item.get("types", []) if t.get("name")],
        relations=relations,
    )


class RridClient:
    def __init__(self, http: CachedJsonClient):
        self.http = http

    def fetch(self, rrid: str, refresh: bool = False) -> RridRecord | None:
        """Return the record, or None if the RRID does not resolve (e.g., retired IDs)."""
        rrid = normalize_rrid(rrid)
        try:
            raw = self.http.request("GET", RESOLVER_URL.format(rrid=rrid),
                                    cache_key=f"rrid_{rrid}", refresh=refresh)
        except requests.HTTPError as exc:
            if exc.response is not None and exc.response.status_code == 404:
                return None
            raise
        return parse_record(raw)
