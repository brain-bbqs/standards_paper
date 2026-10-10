"""Small HTTP helper with on-disk JSON caching, throttling, and retry on rate limits."""

from __future__ import annotations

import json
import logging
import time
from pathlib import Path

import requests

log = logging.getLogger(__name__)

# SciCrunch rejects the default python-requests/urllib User-Agent with 403.
USER_AGENT = "ecokg/0.1 (neuroscience data standards ecosystem knowledge graph; python-requests)"


class CachedJsonClient:
    def __init__(self, cache_dir: Path, min_interval: float = 1.0, max_retries: int = 5,
                 session: requests.Session | None = None):
        self.cache_dir = Path(cache_dir)
        self.min_interval = min_interval
        self.max_retries = max_retries
        self.session = session or requests.Session()
        self.session.headers.setdefault("User-Agent", USER_AGENT)
        self.session.headers.setdefault("Accept", "application/json")
        self._last_request = 0.0

    def _cache_path(self, key: str) -> Path:
        safe = "".join(c if c.isalnum() or c in "-_." else "_" for c in key)
        return self.cache_dir / f"{safe}.json"

    def cached(self, key: str) -> dict | None:
        path = self._cache_path(key)
        if path.exists():
            return json.loads(path.read_text())
        return None

    def store(self, key: str, data: dict) -> None:
        path = self._cache_path(key)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=1, sort_keys=True))

    def request(self, method: str, url: str, *, cache_key: str | None = None,
                refresh: bool = False, **kwargs) -> dict:
        if cache_key and not refresh:
            hit = self.cached(cache_key)
            if hit is not None:
                return hit
        for attempt in range(self.max_retries):
            wait = self.min_interval - (time.monotonic() - self._last_request)
            if wait > 0:
                time.sleep(wait)
            self._last_request = time.monotonic()
            resp = self.session.request(method, url, timeout=60, **kwargs)
            if resp.status_code == 429 or resp.status_code >= 500:
                backoff = 5 * (attempt + 1)
                log.warning("%s %s -> %s; retrying in %ss", method, url, resp.status_code, backoff)
                time.sleep(backoff)
                continue
            resp.raise_for_status()
            data = resp.json()
            if cache_key:
                self.store(cache_key, data)
            return data
        raise RuntimeError(f"{method} {url}: giving up after {self.max_retries} attempts")
