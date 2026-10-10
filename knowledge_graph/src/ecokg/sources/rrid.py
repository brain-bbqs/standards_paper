"""RRID / SciCrunch Registry harvesting.

Records are fetched anonymously from the public resolver
(https://scicrunch.org/resolver/RRID:SCR_xxxxxx.json). Each record lists typed
relationships to other registry resources under ``_source.graph`` (e.g.,
``is_related_to``, ``works_with``, ``lists``, ``has_parent_organization``).

Searching the registry by name (``ecokg rrid-search``) uses the SciCrunch Elasticsearch API
(``SEARCH_URL``) and needs a free API key (scicrunch.org > My Account > API Keys), read from the
``SCICRUNCH_API_KEY`` environment variable. The key is sent only in the ``apikey`` request header,
never in the URL, so it does not appear in error messages, logs, or the cache.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import os

import requests

from ..http import CachedJsonClient

RESOLVER_URL = "https://scicrunch.org/resolver/RRID:{rrid}.json"
SEARCH_URL = "https://api.scicrunch.io/elastic/v1/RIN_Tool_pr/_search"  # SciCrunch tools/resources index


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
    """Parse a resolver response (first hit)."""
    hits = raw.get("hits", {}).get("hits", [])
    return parse_source(hits[0]["_source"]) if hits else None


def parse_search(raw: dict) -> list[RridRecord]:
    """Parse all hits of a registry search response."""
    return [parse_source(h["_source"]) for h in raw.get("hits", {}).get("hits", []) if "_source" in h]


def parse_source(src: dict) -> RridRecord:
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


def search_query(text: str, size: int = 10) -> dict:
    """Elasticsearch query: match name/abbreviation/synonyms, boosting exact name matches."""
    return {
        "size": size,
        "query": {"bool": {"should": [
            {"multi_match": {"query": text, "type": "phrase", "boost": 3,
                             "fields": ["item.name", "item.abbreviations.name", "item.synonyms.name"]}},
            {"multi_match": {"query": text,
                             "fields": ["item.name^2", "item.abbreviations.name^2", "item.synonyms.name"]}},
        ]}},
    }


class RridClient:
    def __init__(self, http: CachedJsonClient, api_key: str | None = None):
        self.http = http
        self.api_key = (api_key or os.environ.get("SCICRUNCH_API_KEY") or "").strip() or None

    def search(self, text: str, refresh: bool = False) -> list[RridRecord]:
        """Search the registry by name or abbreviation (needs an API key unless cached)."""
        cache_key = f"rrid_search_{text}"
        raw = None if refresh else self.http.cached(cache_key)
        if raw is None:
            if not self.api_key:
                raise RuntimeError("Registry search needs a SciCrunch API key: set SCICRUNCH_API_KEY "
                                   "(scicrunch.org > My Account > API Keys).")
            self.http.session.headers["apikey"] = self.api_key
            raw = self.http.request("POST", SEARCH_URL, json=search_query(text), cache_key=cache_key, refresh=True)
        return parse_search(raw)

    def resolve(self, name: str, abbreviation: str | None) -> list[RridRecord]:
        """Candidate records for a seed: exact name/abbreviation matches first, else the top hits."""
        wanted = {s.lower() for s in (name, abbreviation) if s}
        hits: dict[str, RridRecord] = {}
        for query in dict.fromkeys(q for q in (abbreviation, name) if q):
            for r in self.search(query):
                hits.setdefault(r.rrid, r)
        exact = [r for r in hits.values() if {r.name.lower(), *(a.lower() for a in r.abbreviations)} & wanted]
        return exact or list(hits.values())[:5]

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
