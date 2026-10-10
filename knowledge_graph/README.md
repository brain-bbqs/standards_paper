# ecokg — neuroscience data standards ecosystem knowledge graph

Evidence for the paper's "bridges within vs. across communities" claim (paper plan, workstream B).
The graph combines expert-curated nodes and edges with relationships harvested from RRID/SciCrunch
and FAIRsharing, and classifies every edge by **layer span** (within/cross layer) and
**community scope** (within/cross community, or shared infrastructure).

## Inputs (`data/`)

| File | Content |
|---|---|
| `taxonomy.yaml` | Layers, communities, relation types, and registry-label → relation mapping |
| `seeds.yaml` | Nodes (standards, archives, formats, …) with RRID / FAIRsharing ids. **Draft — needs expert review** |
| `curated_edges.yaml` | Expert-curated relationships. **Draft — every edge needs `verified: true` before use in the paper** |
| `harvested/` | Registry relationships written by the `harvest-*` commands (committed snapshot) |

## Usage

```sh
uv venv && uv pip install -e '.[test]'
ecokg validate                          # check YAML against the taxonomy
ecokg -v rrid-check                     # resolve every RRID and flag name mismatches
ecokg harvest-rrid                      # no account needed
read -rs FAIRSHARING_TOKEN && export FAIRSHARING_TOKEN   # or FAIRSHARING_LOGIN/PASSWORD (see sources/fairsharing.py)
ecokg harvest-fairsharing --resolve     # list candidate records for seeds without a FAIRsharing id
ecokg harvest-fairsharing               # harvest associations for seeds with a FAIRsharing id
ecokg report                            # output/: graph.{graphml,json}, nodes/edges.csv, stats.md, gaps.md
pytest
```

Registry responses are cached in `data/cache/`; pass `--refresh` to re-fetch.

## Notes

- FAIRsharing API access requires linking your account to an organisation (fairsharing.org/profiles/edit).
  Check the REST association field names on the
  first authenticated run (raw responses are kept in `data/cache/fairsharing/`).
- Community scope is reported in two modes (strict = home community; lenient = any shared community).
  The results are very sensitive to the mode (see `output/stats.md`), so node community tags need careful review.
