# Knowledge graph — open issues and TODO

*Status as of 2026-10-09. The graph has 71 nodes and 124 edges (97 curated, 22 from RRID, 8 from FAIRsharing);
see `output/stats.md` and `output/gaps.md` (`ecokg report`). Items are ordered by how much they
affect the paper's Fig. 3 / "few cross-community bridges" claim.*

---

## 1. Blockers for using the graph as evidence

### 1.1 FAIRsharing REST API omits record relations
- **Problem.** `GET /fairsharing_records/{id}` and search hits return `linked_records` / `linking_records`,
  but these are incomplete. Example: the DANDI page (https://fairsharing.org/3322) lists NWB, BIDS and
  DOI under "Related content", but its API record has **no** `linked_records`. The NWB record (1131) lists
  "DANDI implements NWB" as an incoming link, while DANDI's own record does not show it as outgoing.
- **Effect.** Of 154 harvested associations for 46 seeds, 145 are `collects` (collection membership,
  dropped) and the other 9 all come from the NWB record. FAIRsharing coverage figures (e.g., "12% of
  curated edges are also in a registry") are therefore **not usable** in the paper yet.
- **Not an option.** The website loads relations through FAIRsharing's internal GraphQL client
  (`api.fairsharing.org/graphql` returns 404/501 to API users). Do not reverse-engineer that client.
- **To do (pick one or both):**
  - [ ] Contact FAIRsharing (contact@fairsharing.org): ask how API users can get record relations, and
        report the incomplete `linked_records` (DANDI example). Also invite them to the curation round
        and possibly the paper. API access/Swagger docs are described on their licence page.
  - [ ] Fallback if there is no answer by **mid-Nov 2026**: copy the "Related content" of the 46 seed
        records from fairsharing.org by hand into a YAML file (e.g., `data/fairsharing_manual.yaml`, same
        fields as `harvested/fairsharing_edges.json`), and load it in `build.load_harvested`. Could be
        split among co-authors.
  - [ ] After either: rerun `ecokg harvest-fairsharing` / `ecokg report` and review the new edges.

### 1.2 Community-scope result depends on the classification rule
- **Problem.** Among edges between domain-specific nodes, **49%** cross community boundaries under the
  *strict* rule (compare home communities), but only **4%** under the *lenient* rule (any shared
  community). As tagged now, the claim can't be stated without picking a rule.
- **To do:**
  - [ ] Define criteria for the `communities` list of a node (what makes a community "home" vs. merely
        supported), and record them in `taxonomy.yaml`.
  - [ ] Review each node's `communities` against those criteria (domain experts, see 2.1).
  - [ ] Decide which rule the paper reports (likely both, with strict as the main one), and describe it
        in Methods.

### 1.3 Curated edges are unverified
- **Problem.** All 97 curated edges are `verified: false`; they were compiled from the poster, notes and
  guideline by Claude. Node seeds are also drafts.
- **To do:**
  - [ ] Assign reviewers per community (NWB, BIDS, microscopy, ontologies, clinical, …) to confirm or
        fix edges and set `verified: true` / `verified_by`.
  - [ ] Review node layer/kind assignments, especially fuzzy ones (DICOM, openMINDS, NIDM, HED).

---

## 2. Data gaps

### 2.1 Seeds without a FAIRsharing record (25)
`nemo, psych_ds, dandi_layout, neuroblueprint, bossdb_dm, ncbi_taxonomy, neurolex, mrio, allen_ccf,
allen_human_atlas, waxholm, julich_brain, hcp_atlas, cde, neurobagel, herd, zarr, mp4, swc, precomputed,
bam_cram, loom, json_schema, rdf_owl, hdmf_spec`

- [ ] Search fairsharing.org by hand for these; FAIRsharing's full-text search ranks poorly, so
      `harvest-fairsharing --resolve` missed some that likely exist (e.g., **NCBI Taxonomy**).
      Add confirmed DOIs to `seeds.yaml`, and their numeric ids to `harvested/fairsharing_candidates.json`
      (or rerun `--resolve`).
- [ ] **NeMO:** the only exact name hit was *NEMO, Neural ElectroMagnetic Ontologies*
      (FAIRsharing.n66krd), a different resource. Rejected; check whether the NeMO archive has a record.
- [ ] **OME-Zarr** was mapped to *NGFF, Next Generation File Formats* (FAIRsharing.9af712), and
      **TSV/CSV** to *CSV* (FAIRsharing.1943d4). Confirm both.
- [ ] Seeds still missing from FAIRsharing after this are themselves a finding (gap report → ask the
      teams to register).

### 2.2 Seeds without an RRID (37)
`dabi, psych_ds, dandi_layout, sparc_sds, neuroblueprint, bossdb_dm, ome_tiff, ome_zarr, dicom, odml,
edf, protein_ontology, mrio, radlex, cogpo, datacite_schema, nbo, hcp_atlas, cde, neurobagel, herd,
hdf5, zarr, tiff, json, tsv_csv, yaml, mp4, swc, precomputed, fastq, bam_cram, loom, linkml,
json_schema, xml_schema, rdf_owl`

- [x] Checked FAIRsharing `metadata.cross_references`: only 8 seed records carry an RRID (all archives
      that already had one) and all 8 **agree** with seeds.yaml. Fills no gaps.
- [x] Checked RRID neighbour names against these seeds: no real matches (only substring noise; "DataCite"
      there is the organisation, not the metadata schema).
- [x] `ecokg rrid-search` implemented (SciCrunch Elasticsearch index `RIN_Tool_pr`, key via
      `SCICRUNCH_API_KEY` header). Our first key gets **403 Forbidden** in every request format
      (`ecokg rrid-search-check`): the key is recognised but lacks registry-search permission.
- [ ] Either ask SciCrunch (support@scicrunch.org) to enable search for the key, or retry later in case
      new keys need time to activate; then run `ecokg rrid-search` and review `rrid_candidates.json`.
- [ ] Meanwhile / alternatively: look the seeds up by hand with **`RRID_LOOKUP.md`** (search links for all
      37 seeds). Many generic formats (JSON, YAML, TIFF) will legitimately have none; mark them as
      checked, not missing.

### 2.3 Registry data-quality issues found (report to registries; mention in paper)
- [ ] **HED** has two RRIDs: SCR_014074 and SCR_017630 ("HED Tags"); handled with `rrid_aliases`.
- [ ] **OpenNeuro** duplicate SCR_016667 no longer resolves (404) but is still linked from other records.
- [ ] **Allen CCF** seed originally used SCR_002978 (Allen Mouse Brain Reference Atlas); corrected to
      SCR_020999.
- [ ] FAIRsharing says **"BIDS extends NWB"** (on the NWB record). Probably wrong or refers to BIDS
      microelectrode extension (BEP032); confirm with NWB/BIDS maintainers.

### 2.4 Seeds with no relationships (4)
`MRIO, Allen Human Brain Atlas, Waxholm (WHS), HCP-MMP`
- [ ] Add curated edges (e.g., which standards/archives use these atlases), or drop them from seeds.

### 2.5 Registry neighbours that are not seeds (326, mostly RRID)
- [ ] Review the top of the list in `output/gaps.md` for missing seeds (e.g., *HDMF Common Schema*,
      *Cognitive Atlas Ontology*, *InterLex*, *NeuroVault*, *BALSA*, *INDI*), and ignore tools/organisations.

---

## 3. Code

- [x] **Fig. 3 draft** (`ecokg figure`, `src/ecokg/figure.py`): layers as rows, home communities as
      columns (cross-cutting on the right), edges styled by community scope, registry-confirmed edges
      marked. Options: `--mode strict|lenient`, `--sources all|curated|registry`, `--verified-only`.
- [ ] Fig. 3 polish once 1.1–1.3 are settled: label collisions in dense cells, decide whether to show
      "shared" edges (they dominate visually) or summarise them, journal size/fonts, colour-blind palette.
- [ ] Optional: loader for manually transcribed FAIRsharing relations (see 1.1).
- [ ] Optional: SciCrunch name search (needs an API key) to resolve RRIDs for seeds automatically.

## 4. Release

- [ ] Merge branch `worktree-knowledge-graph` into `main`.
- [ ] Freeze a snapshot (seeds, edges, harvested data, outputs) with a Zenodo DOI (plan: late Jan 2027).
- [ ] Check FAIRsharing (CC BY-SA) and RRID licence/attribution terms for redistributing harvested data.

---

## Notes for running the harvest

- FAIRsharing needs an account **linked to an organisation** (profiles/edit), otherwise 401.
- GitHub/ORCID logins: export a browser JWT as `FAIRSHARING_TOKEN` (`read -rs`; never commit or paste it).
  It is valid ~24 h. `ecokg fairsharing-check` diagnoses auth without printing the token.
- Raw responses are cached in `data/cache/` (git-ignored); pass `--refresh` to re-fetch.
