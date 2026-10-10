"""Command-line interface: ``ecokg <command>``.

Commands
    validate             check seeds.yaml / curated_edges.yaml against taxonomy.yaml
    rrid-check           resolve every seed RRID and flag name mismatches
    harvest-rrid         harvest RRID relationships -> data/harvested/rrid_edges.json
    harvest-fairsharing  harvest FAIRsharing associations -> data/harvested/fairsharing_edges.json
                         (--resolve: list candidate records for seeds without a FAIRsharing id)
    report               build the graph; write output/ (graph, CSVs, stats.md, gaps.md)
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

from . import CACHE_DIR, HARVEST_DIR, OUTPUT_DIR
from .build import build_graph, load_harvested
from .http import CachedJsonClient
from .model import load_curated_edges, load_seeds, load_taxonomy, validate
from .report import export, gap_markdown, stats_markdown
from .sources.fairsharing import FairsharingClient
from .sources.rrid import RridClient

log = logging.getLogger("ecokg")

FAIRSHARING_IDS = "fairsharing_ids.json"   # numeric FAIRsharing record id -> seed id


def _load_all():
    taxonomy, nodes, edges = load_taxonomy(), load_seeds(), load_curated_edges()
    errors = validate(taxonomy, nodes, edges)
    return taxonomy, nodes, edges, errors


def _write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=1, sort_keys=True) + "\n")


def _names_match(node, record_name: str, record_abbrevs: list[str]) -> bool:
    wanted = {s.lower() for s in (node.name, node.abbreviation) if s}
    found = {s.lower() for s in (record_name, *record_abbrevs) if s}
    return bool(wanted & found) or any(w in f or f in w for w in wanted for f in found)


def cmd_validate(args) -> int:
    _, nodes, edges, errors = _load_all()
    for e in errors:
        print(e)
    print(f"{len(nodes)} nodes, {len(edges)} curated edges, {len(errors)} problems")
    return 1 if errors else 0


def cmd_rrid_check(args) -> int:
    _, nodes, _, _ = _load_all()
    client = RridClient(CachedJsonClient(CACHE_DIR / "rrid"))
    problems = 0
    checked = 0
    for n in nodes.values():
        for rrid in n.rrids:
            checked += 1
            try:
                rec = client.fetch(rrid, refresh=args.refresh)
            except Exception as exc:  # network/HTTP errors are reported per seed
                print(f"ERROR     {n.id:24} {rrid}: {exc}")
                problems += 1
                continue
            if rec is None:
                print(f"NOT FOUND {n.id:24} {rrid}")
                problems += 1
            elif not _names_match(n, rec.name, rec.abbreviations):
                print(f"MISMATCH  {n.id:24} {rrid}: registry name {rec.name!r}")
                problems += 1
            elif args.verbose:
                print(f"ok        {n.id:24} {rrid}: {rec.name}")
    print(f"{checked} RRIDs checked, {problems} problems")
    return 1 if problems else 0


def cmd_harvest_rrid(args) -> int:
    _, nodes, _, _ = _load_all()
    client = RridClient(CachedJsonClient(CACHE_DIR / "rrid"))
    items = []
    for n in nodes.values():
        for rrid in n.rrids:
            rec = client.fetch(rrid, refresh=args.refresh)
            if rec is None:
                log.warning("%s: RRID %s not found", n.id, rrid)
                continue
            for label, other, other_name in rec.relations:
                items.append({"registry": "rrid", "node": n.id, "label": label, "direction": "out",
                              "other_id": other, "other_name": other_name})
    _write_json(HARVEST_DIR / "rrid_edges.json", items)
    print(f"{len(items)} RRID relations harvested -> {HARVEST_DIR / 'rrid_edges.json'}")
    return 0


def cmd_harvest_fairsharing(args) -> int:
    _, nodes, _, _ = _load_all()
    client = FairsharingClient(CachedJsonClient(CACHE_DIR / "fairsharing"))

    if args.resolve:
        resolved = {}
        for n in nodes.values():
            if n.fairsharing:
                continue
            hits = client.resolve(n.name, n.abbreviation)
            resolved[n.id] = [{"doi": r.doi, "id": r.id, "name": r.name, "abbreviation": r.abbreviation,
                               "registry": r.registry, "type": r.type, "status": r.status} for r in hits]
            print(f"{n.id:24} " + ("; ".join(f"{r.doi} {r.abbreviation or r.name}" for r in hits) or "-"))
        out = HARVEST_DIR / "fairsharing_candidates.json"
        _write_json(out, resolved)
        print(f"Candidates written to {out}. Copy confirmed DOIs into seeds.yaml (`fairsharing:`).")
        return 0

    ids: dict[str, str] = {}
    items = []
    for n in nodes.values():
        if not n.fairsharing:
            continue
        match = [r for r in client.resolve(n.name, n.abbreviation) if r.doi == n.fairsharing and r.id]
        if not match:
            log.warning("%s: could not find numeric id for %s", n.id, n.fairsharing)
            continue
        rec = client.get_record(match[0].id, refresh=args.refresh)
        ids[str(rec.id)] = n.id
        for label, direction, other_id, other_doi, other_name in rec.associations:
            items.append({"registry": "fairsharing", "node": n.id, "label": label, "direction": direction,
                          "other_id": other_doi or other_id, "other_name": other_name})
    _write_json(HARVEST_DIR / FAIRSHARING_IDS, ids)
    _write_json(HARVEST_DIR / "fairsharing_edges.json", items)
    print(f"{len(ids)} records, {len(items)} associations -> {HARVEST_DIR / 'fairsharing_edges.json'}")
    return 0


def cmd_fairsharing_check(args) -> int:
    """Diagnose FAIRsharing authentication without printing the token."""
    from .sources import fairsharing as fs

    client = fs.FairsharingClient(CachedJsonClient(CACHE_DIR / "fairsharing"))
    for k, v in fs.token_summary(client._jwt).items():
        print(f"token {k}: {v}")
    client._authenticate()
    session = client.http.session
    probes = [
        ("GET", "/fairsharing_records/1", {}, "fairsharing_check_record"),
        ("POST", "/search/fairsharing_records", {"params": {"q": "NWB"}}, "fairsharing_check_search"),
    ]
    ok = True
    for method, path, kwargs, cache_key in probes:
        resp = session.request(method, fs.API_URL + path, timeout=60, **kwargs)
        print(f"{method:4} {path}: {resp.status_code}")
        if not resp.ok:
            print(f"     {resp.text[:200]!r}")
            ok = False
            continue
        data = resp.json()
        client.http.store(cache_key, data)  # kept for inspecting the response structure
        print(f"     structure: {_shape(data)}")
    return 0 if ok else 1


def _shape(value, depth: int = 0):
    """Key names (not values) of a JSON response, a few levels deep."""
    if depth > 2:
        return "..."
    if isinstance(value, dict):
        return {k: _shape(v, depth + 1) for k, v in list(value.items())[:40]}
    if isinstance(value, list):
        return [_shape(value[0], depth + 1), f"({len(value)} items)"] if value else []
    return type(value).__name__


def cmd_report(args) -> int:
    taxonomy, nodes, edges, errors = _load_all()
    if errors:
        for e in errors:
            print(e)
        print("Fix validation problems first (ecokg validate).")
        return 1
    ids_path = HARVEST_DIR / FAIRSHARING_IDS
    fs_ids = json.loads(ids_path.read_text()) if ids_path.exists() else {}
    result = build_graph(taxonomy, nodes, edges, load_harvested(HARVEST_DIR), fs_ids)
    out = Path(args.out)
    export(result, out)
    (out / "stats.md").write_text(stats_markdown(result, taxonomy))
    (out / "gaps.md").write_text(gap_markdown(result, nodes))
    g = result.graph
    print(f"{g.number_of_nodes()} nodes, {g.number_of_edges()} edges -> {out}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="ecokg", description=__doc__.splitlines()[0])
    parser.add_argument("-v", "--verbose", action="store_true")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate", help="validate the curated YAML inputs").set_defaults(func=cmd_validate)
    for name, func, help_ in (("rrid-check", cmd_rrid_check, "check seed RRIDs resolve to the right resource"),
                              ("harvest-rrid", cmd_harvest_rrid, "harvest RRID relationships"),
                              ("harvest-fairsharing", cmd_harvest_fairsharing, "harvest FAIRsharing associations")):
        p = sub.add_parser(name, help=help_)
        p.add_argument("--refresh", action="store_true", help="ignore the on-disk cache")
        p.set_defaults(func=func)
        if name == "harvest-fairsharing":
            p.add_argument("--resolve", action="store_true",
                           help="list candidate records for seeds without a FAIRsharing id")
    sub.add_parser("fairsharing-check", help="diagnose FAIRsharing authentication (never prints the token)"
                   ).set_defaults(func=cmd_fairsharing_check)
    p = sub.add_parser("report", help="build the graph and write output files")
    p.add_argument("--out", default=str(OUTPUT_DIR))
    p.set_defaults(func=cmd_report)

    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING, format="%(levelname)s %(message)s")
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
