# Knowledge graph — open issues and TODO

*Status as of 2026-10-09. The graph has 72 nodes and 122 edges (undirected relations counted once);
see `output/stats.md` and `output/gaps.md` (`ecokg report`). Items are ordered by how much they
affect the paper's Section 4 and Fig. 3 ("bridges between communities concentrate in a few hubs").
Paper-level decisions and claims that depend on this list are tracked in `../plan/TODO.md` (D10, C25, C26,
F5).*

---

## 0. Review checklist (decisions and input needed from the team)

Everything that waits on a person, in one place; details are in the sections referenced.

**Decisions**
- [ ] Community rule for bridges: adopt the home-community proposal (1.2)? (= paper decision D10)
- [ ] FAIRsharing relations: contact FAIRsharing and/or transcribe by hand (1.1)?
- [ ] RRID gaps: option A (by hand) or B (API permission via help desk) (2.2)?
- [ ] Show or summarise "shared infrastructure" edges in Fig. 3 (3)?
- [ ] Add or drop candidate seeds: HDMF Common Schema, openMINDS sub-models, NeuroVault, BALSA, INDI (2.5);
      MRIO and Allen Human Brain Atlas have no edges (2.4).

**Reviews**
- [ ] Figure draft: `../figures/fig3_knowledge_graph/fig3_knowledge_graph.pdf` (strict; paper Fig. 3); rebuild with `make figures` from the paper root — layout,
      misplaced nodes, missing bridges (3).
- [ ] Home community of the 21 multi-community nodes (1.2).
- [ ] All 101 curated edges (`verified: false`) and node layers/kinds, by domain experts (1.3).
- [ ] FAIRsharing matches to confirm: OME-Zarr → NGFF, TSV/CSV → CSV; NeMO (rejected match) (2.1).
- [ ] "BIDS extends NWB" in FAIRsharing: confirm with NWB/BIDS maintainers (2.3).
- [ ] Draft edges added 2026-10-09: InterLex extends NeuroLex; openMINDS → Waxholm, → Allen CCF;
      HCP-MMP → NIfTI (2.4, 2.5).

**Actions needing credentials or people**
- [ ] Next authenticated FAIRsharing run (token, user's terminal): harvest InterLex and any new DOIs (2.1, 2.5).
- [ ] Hand searches on fairsharing.org for the 25 seeds without a record (2.1).
- [ ] Assign domain reviewers per community (1.3).
- [ ] Licence/attribution check for redistributing harvested data; Zenodo snapshot (4).

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
- **Analysis (2026-10-09).** 30 edges are cross-community under strict but not under lenient. In every
  case the overlap comes from a node having been tagged with *extra* communities **because it reaches
  into them** (BIDS is tagged microscopy because it organizes OME-TIFF/OME-Zarr; EMBER is tagged
  neurophysiology because it accepts NWB; HED is tagged neurophysiology/behavior because NWB uses it).
  The lenient rule is therefore **circular**: it counts exactly the bridges the paper is about as
  "within community". Overlaps come mostly via neurophysiology (17 edges) and behavior (15).
- **Proposal for review:**
  - `home` (first community) = where the resource **originated and is governed**, decided independently
    of its edges. The strict rule on home communities is the measure of bridges.
  - The remaining `communities` = communities the resource **supports/serves** (an outcome of
    bridging). Report it separately, e.g., "BIDS now serves 5 communities", to show which resources have
    become cross-community hubs (BIDS, NWB, HED, EMBER, openMINDS, EBRAINS), and stop using it to
    classify edges.
  - In Methods: home community assigned by origin/governance; checked by the domain reviewers.
- **To do:**
  - [ ] Agree on the proposal above (or an alternative).
  - [ ] Review each node's home community against it (domain experts, see 1.3); multi-community nodes
        to check first: DANDI, EMBER, OpenNeuro, DABI, EBRAINS, SPARC, TCIA, NDA, BIDS, Psych-DS, SPARC SDS,
        NeuroBlueprint, NWB, DICOM, openMINDS, EDF, RadLex, Cognitive Atlas, CogPO, HED, Neurobagel.
  - [ ] If adopted: replace the lenient mode in `classify.py` / stats / figure with a per-node
        "communities served" summary, and describe the rule in Methods.

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
- [ ] Fill the remaining RRIDs. Two options (choose when we get to it):
  - **Option A — by hand:** use **`RRID_LOOKUP.md`** (search links for all 37 seeds on rrid.site, no
    login). Record found RRIDs in the table, copy them into `seeds.yaml`, and run `ecokg rrid-check`.
  - **Option B — API:** request registry-search permission for our SciCrunch API key via the SciCrunch
    help desk (support@scicrunch.org); then run `ecokg rrid-search-check` (expect 200) and
    `ecokg rrid-search`, and review `data/harvested/rrid_candidates.json`.
  - Either way, many generic formats (JSON, YAML, TIFF) will legitimately have no RRID; tick them as
    checked, not missing.

### 2.3 Registry data-quality issues found (report to registries; mention in paper)
- [ ] **HED** has two RRIDs: SCR_014074 and SCR_017630 ("HED Tags"); handled with `rrid_aliases`.
- [ ] **OpenNeuro** duplicate SCR_016667 no longer resolves (404) but is still linked from other records.
- [ ] **Allen CCF** seed originally used SCR_002978 (Allen Mouse Brain Reference Atlas); corrected to
      SCR_020999.
- [ ] Generic RRID `is_related_to` links between archives, **BossDB–EMBER** and **DANDI–EMBER**, count as
      bridges between communities. They probably reflect shared infrastructure or teams (EMBER "extends
      established BRAIN Initiative data infrastructure") rather than a data-standards relationship. Confirm
      with the EMBER, BossDB, and DANDI teams; replace with a typed curated edge or drop.
- [ ] FAIRsharing says **"BIDS extends NWB"** (on the NWB record). Probably wrong or refers to BIDS
      microelectrode extension (BEP032); confirm with NWB/BIDS maintainers.

### 2.4 Seeds with no relationships (2)
- [x] Added draft edges: openMINDS → Waxholm and → Allen CCF (SANDS), HCP-MMP → NIfTI (low confidence).
- [ ] `MRIO, Allen Human Brain Atlas` still have no relationships: add edges (who uses them?) or drop them.

### 2.5 Registry neighbours that are not seeds (326, mostly RRID)
- [x] Reviewed the top of the list: mostly tools and organisations. Added **InterLex** as a seed
      (RRID SCR_016178, FAIRsharing.67sssf; linked from NeuroLex, NIFSTD, SPARC) with edge
      InterLex extends NeuroLex.
- [ ] Decide on: *HDMF Common Schema* (component of HDMF; HERD lives there), openMINDS sub-models
      (components of openMINDS; probably keep them merged), *NeuroVault*, *BALSA*, *INDI* (neuroimaging
      archives, from FAIRsharing search).
- [ ] Harvest InterLex's FAIRsharing record on the next authenticated `ecokg harvest-fairsharing` run.

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

- [x] Merged into `main` (2026-10-09).
- [ ] Freeze a snapshot (seeds, edges, harvested data, outputs) with a Zenodo DOI (plan: late Jan 2027).
- [ ] Check FAIRsharing (CC BY-SA) and RRID licence/attribution terms for redistributing harvested data.

---

## Notes for running the harvest

- FAIRsharing needs an account **linked to an organisation** (profiles/edit), otherwise 401.
- GitHub/ORCID logins: export a browser JWT as `FAIRSHARING_TOKEN` (`read -rs`; never commit or paste it).
  It is valid ~24 h. `ecokg fairsharing-check` diagnoses auth without printing the token.
- Raw responses are cached in `data/cache/` (git-ignored); pass `--refresh` to re-fetch.
