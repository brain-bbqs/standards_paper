# Paper TODO — first draft review

*Status 2026-10-09: first full draft in `draft/` (Sections 1–9, Methods, display-item plan, references).
Main text ≈ 5,560 words including the two in-text tables (target ~5,000). Knowledge-graph issues are
tracked separately in `knowledge_graph/TODO.md`.*

Conventions in the draft: `[TODO-Cn]` = claim needing support (listed below); `[REF: …]` = citation to
insert (see `draft/12_references.md`; entries marked ? or — need work).

---

## D. Decisions for the team

- [x] **D1 — Journal: Scientific Data, article type "Article"** (confirmed 2026-10-09 against
      nature.com/sdata/submission-guidelines). Requirements found there:
      - Articles cover data standards, repositories, curation, and policy, and may be shorter or
        speculative; the journal no longer has a Comment format. Peer reviewed.
      - **No word limit**; Methods have no length limit.
      - **Abstract ≤170 words** (draft now 160).
      - **≤8 figures and ≤10 tables** recommended; **figure legends ≤350 words in total**.
      - **Title ≤110 characters**, no colons, parentheses, or uncommon acronyms → D7.
      - Required statements: Data Availability, Code Availability, Author Contributions, Competing
        Interests, Funding, Ethics where relevant (draft in `draft/09_statements.md`).
      - Nature reference style, numbered, DOIs as URLs; journal abbreviation *Sci. Data*.
      - Data/code sharing required for Articles "if relevant to the results" → applies to the KG and
        the BBQS aggregates.
      - Not stated on the page: APC amount (Q6) and pre-submission enquiries — check "Open Access Fees
        and Funding" and whether to replace the planned Nov 17 enquiry.
- [ ] **D2 — Length.** No word limit at Scientific Data; no cuts needed for length. Still tighten for
      readability, and move the in-text tables to formal tables (≤10 allowed).
- [ ] **D3 — Role of the knowledge graph.** With Scientific Data (no word limit, 8 figures, analyses
      welcome) it can be a main figure and a Results subsection rather than a supplement. Recommended:
      keep, and resolve `knowledge_graph/TODO.md` 1.1–1.3 before submission.
- [ ] **D4 — How prescriptive.** Part II now gives recommendations R1–R11 "derived from the BBQS
      guideline". Confirm the framing (community guidance vs. program requirements) with the BBQS
      Data Standards WG and program staff.
- [ ] **D5 — Ontology layer.** Kept as one layer with the distinction explained (Section 2) per Q1;
      confirm wording.
- [ ] **D6 — Figure count.** Five figures + Suppl. Fig. S1 (could become main Fig. 6) and two tables:
      within the limits (≤8 figures, ≤10 tables).
- [x] **D7 — Title (decided 2026-10-09):** "Navigating neuroscience data standards for multimodal brain behavior quantification and synchronization" (103 characters).

- [ ] **D8 — Six layers vs. literature (review 2026-10-09).**
      - *Alignment:* the usual life-science distinction is reporting guidelines / models & formats /
        terminologies (+ repositories, policies) [REF: Sansone 2012 Nat Genet 44:121; Sansone 2019].
        FAIRsharing record types match this (in our harvest: 314 model/format, 257 terminology,
        62 reporting guideline, 14 identifier schema). Our ontology and archive layers correspond directly.
      - *Our contribution:* splitting FAIRsharing's single "model and format" bucket into dataset
        organization, data standards, data formats, and schema languages. Say this explicitly and add a
        short "relation to existing classifications" paragraph to Section 2 (currently missing).
      - *Missing vs. literature:* reporting guidelines / minimum information (COBIDAS, ARRIVE, CDEs),
        persistent identifiers (DOI, RRID, ORCID, ROR), access protocols / APIs, provenance, policies /
        licences. Proposal: a cross-cutting band in Fig. 1 plus one paragraph, not more layers. State
        that modelling standards (NeuroML, SONATA, PyNN) are out of scope.
      - [x] *Naming (decided 2026-10-09):* layer 3 renamed from "data standards" to **"file organization
        standards"**, which parallels "dataset organization standards" (files in folders vs. data
        within a file). "File" is used in the broad sense of a self-contained data object; the
        single-file vs. directory (e.g., Zarr) choice belongs to the data format layer. Applied in the
        draft, Table 1, figure specs, and the knowledge-graph taxonomy label (node id `data_standard`
        unchanged). Fig. 1 and the poster-derived figures must use the new name (F2).
      - *Geometry:* archives → dataset organization → data standards → formats is a containment stack;
        ontologies/terminologies (semantics) and schema languages (formal definition) cut across it.
        Option: redraw Fig. 1 as a 4-level stack with two cross-cutting columns (keeps six categories).

## A. Actions

- [ ] **A1** Author list and CRediT roles (poster authors + confirmed contributors; close Nov 14).
- [ ] **A2** BBQS clearance: confirm with BARD.CC / DCAIC and program staff that the **aggregate**
      inventory statistics (Section 4, Fig. 4) may be published; agree on wording for the source.
- [ ] **A3** Section leads to review each section (assign from contributor list).
- [ ] **A4** NWB, BIDS, Psych-DS, HED, and EMBER teams to check Section 5, Table 3, and R1–R11.
- [ ] **A5** Version the BBQS guideline (e.g., Zenodo release) so the paper can cite a fixed version; the
      guideline itself still has many "TODO — how to store?" entries and some unfinished parts.
- [ ] **A6** Zenodo DOI for code and data (`ecokg`, `analysis/`).
- [ ] **A7** Resolve references marked ? or — in `draft/12_references.md`.
- [ ] **S1** Licence terms for redistributing RRID and FAIRsharing data (FAIRsharing CC BY-SA?).
- [ ] **S2** Contact for access to the BBQS project inventory (Data Availability).
- [ ] **S3** Licence for code (e.g., BSD-3 or MIT) and data (e.g., CC BY 4.0).
- [ ] **S4** Competing-interest statements from all authors.
- [ ] **S5** Complete funding list for all authors.
- [ ] **S6** Convert references to Nature style with DOIs at the end (Zotero/BibTeX).
- [ ] **A8** Move to Google Docs for the full author group once the core team has reviewed this draft.

## F. Figures

- [x] **F1** Main-item budget: fits (≤8 figures, ≤10 tables).
- [ ] **F6** Shorten legends: all figure legends together ≤350 words (draft legends in
      `draft/11_figures_tables.md` are longer). Sans-serif fonts, white backgrounds.
- [ ] **F2** Fig. 1, Fig. 2, Fig. 5b, Suppl. Table S1: redraw from the poster (designer / figure lead).
- [ ] **F3** Fig. 3 (BBQS stack on the map): design from the spec in `draft/11_figures_tables.md`.
- [ ] **F4** Fig. 4 draft (`analysis/output/fig4_bbqs.pdf`): review; decide whether to keep species
      panel (a), and whether "Exploratory behavior" (no guideline entry) should be shown as a gap.
- [ ] **F5** Suppl. Fig. S1 (knowledge graph): depends on D3.

---

## C. Claims that need support

| ID | Section | Claim / text | What is needed |
|---|---|---|---|
| C1 | 1 | Experiments now generate terabytes each | Citation(s) with concrete numbers (e.g., Neuropixels, whole-brain imaging, multi-camera video) |
| C2 | 1 | BRAIN archive sizes (researched 2026-10-09) | **DANDI** 1,197 Dandisets, 2.44 PB — from `api.dandiarchive.org/api/stats/` (authoritative; cite with access date). **BossDB** ~1.03 PB, >10 petavoxels — web search snippet of bossdb.org; site is JS-only, verify. **NeMO** >1 PB, >3 M files — search snippet (NeMO paper, Ament 2023 / NIH newsletter); verify. **BIL** "first petascale brain microscopy resource", ~7,000 datasets — Kenney 2024 *Sci Data* (full text not reachable); verify. **OpenNeuro** ~1,000 datasets, >40,000 participants — only from third-party docs; get an official figure (OpenNeuro team). Consider DABI, NEMAR, EMBER sizes too. Avoid the BRAIN KB roundtable summary (not for distribution). |
| C3 | 1 | AI raises the value of consistently structured data | Citation (AI-readiness / foundation-model papers) or soften |
| C4 | 2 | Ontologies vs. terminologies kept in one layer; "used the same way" | Team confirmation (D5); optional citation |
| C5 | 2 | Origin/funding of standards (research vs. vendor vs. archive-driven) | Suppl. Table S1 from poster; check each entry |
| C6 | 3 | Levels of FAIRness (Table 2), revised 2026-10-09 | Now positioned as a staged communication scale (like 5-star Linked Open Data and Data Readiness Levels) that does **not** replace per-principle assessment (FAIR maturity indicators, RDA FAIR Data Maturity Model, F-UJI). Check the FAIR-principle mapping per level with a FAIR expert; decide whether to show the poster's original "FAIR Data Score" in Supplement; consider running F-UJI on example datasets at each level as a demonstration |
| C34 | 3 | Maturity of standards themselves is better described by technology readiness scales | Citation (TRL; any TRL-like scale for software or standards); or remove |
| C7 | 4, Methods | BBQS inventory statistics | Clearance (A2); name and date of the inventory; who collected it |
| C8 | 4 | 13 species groups; fish/fly entries | Check the source entries for "fish" and "fly" (one award lists "Fly, Fish"; is "fish" zebrafish?) and whether any award is missed |
| C9 | 4 | Terminologies/atlases sparse for many BBQS species | Citation or examples (e.g., atlases exist for mouse, rat, human, marmoset; few for cowbird, cichlid, acoel) |
| C10 | 4, Methods | Modality counts from keyword matching (video 25, wearables 18, pose 13, audio 13, eye tracking 10, ephys 13, EEG 8, ophys 5) | Manual check against source entries; adjust keywords |
| C11 | 4 | 18 standards answers: NWB 11, BIDS 4, none 3; 3D pose stored as NumPy | Check; questionnaire may be outdated — re-survey? |
| C12 | 4 | Sharing: archive 13/18, cloud drives 14/18, GitHub 14/18 | Check; clarify whether cloud/GitHub are for data or code |
| C13 | 5 | Why these standards were selected (open, community-governed, BRAIN-supported, accepted by EMBER, extensible) | Confirm with BBQS Data Standards WG; cite charter/minutes if any |
| C14 | 5 | EMBER privacy levels; many projects record identifiable human data | EMBER documentation/citation; count of human projects with video/audio (aggregate) |
| C15 | 5, 6 | BEP032 brings NWB into BIDS; status | Current BEP032 status and citation |
| C16 | 5 | HED available for NWB via ndx-hed; "one of few annotation systems that works across standards" | ndx-hed citation/link; soften "one of few" or support |
| C17 | 6 | Table 3 entries | Check by NWB/BIDS/Psych-DS teams (A4); BIDS status for video (BEP044 / issue 1771), audio, GPS |
| C18 | 6 | Pose should be stored in ndx-pose or Motion-BIDS | Confirm Motion-BIDS suits 2D/3D pose from video (it targets motion capture); cite ndx-pose |
| C19 | 6 | Synchronization must be documented; "cannot be reconstructed after the fact" | Citation or soften; check whether any standard defines clock-alignment metadata |
| C20 | 6 | Behavior ontologies (NBO) exist but are not widely used in BBQS | Inventory shows 1 award considering NBO; cite NBO; check other behavior vocabularies (e.g., ABO, NeuroBehavior) |
| C21 | 6 | Large/continuous recordings: split raw/processed; multi-day data | Guideline section is unfinished — needs content from the WG |
| C22 | 6 | Early standardization is cheaper than end-of-project conversion | Citation (e.g., NWB/BIDS experience papers) or soften |
| C23 | 7, Methods | Behavior × guideline coverage (`analysis/behavior_coverage.csv`) | Check coding against guideline; note "cognitive tasks" Psych-DS entry is TODO in the guideline although Psych-DS lists task data as supported; "reproductive b" truncated entry in inventory (possibly a 4th award) |
| C24 | 7 | Technologies lacking guidance (EMG, force plates, VR, home-cage, coding software, thermal, smart devices); BEP042 for EMG | Check current status in NWB/BIDS; cite BEP042 |
| C25 | 7, Methods | KG: 72 technologies, 133 relationships; cross-community links run through hubs (BIDS, NWB, HED, EMBER, DANDI) | Depends on knowledge_graph TODO 1.1–1.3 (FAIRsharing relations, community rule, expert verification) |
| C26 | 7 | Registries record only a small fraction of relationships | Currently 7–12% of curated edges, but FAIRsharing API omits relations (KG TODO 1.1) — **do not state a number until resolved** |
| C27 | 7 | LinkML as a bridge; Psych-DS uses LinkML | Cite LinkML; examples of cross-standard mapping |
| C28 | 7 | Highest-value bridges for BBQS (behavior representation, behavior terminology, conversion tools) | Team agreement; this is a recommendation of the paper |
| C29 | 8 | Data reuse at scale needs remote/partial access, virtual datasets, curation | Citations (cloud-native formats, DataLad, etc.) |
| C30 | 8 | Minimal required metadata still needed with AI-generated annotation | Citation, or frame explicitly as our position |
| C31 | 8 | Standards are long-lived infrastructure; software changes faster | Citation (research software sustainability) or frame as position |
| C32 | 8 | BRAIN knowledge base plans | Cite public source only (KB position paper when available) |
| C33 | 3 | BICCN/BICAN multi-archive stacks (NeMO, BIL, DANDI, BossDB; data inventory/catalog; specimen metadata system NIMP) | From brain-bican.org/data and biccn.org/data (read 2026-10-09). Confirm that NIMP is the right name/description and that BICAN still uses BossDB; cite BICCN 2021 *Nature* and the portals |

---

## Notes for reviewers

- Part I (Sections 1–3) is descriptive; Part II (Sections 4–7) gives BBQS recommendations; Section 8 is
  the outlook. See `plan/paper_plan.md` §0 for the pivot.
- The BRAIN KB roundtable materials in `../brain_knowledge_base/` are marked "not for further
  distribution" and are used only as background; nothing from them is quoted or cited.
- BBQS inventory: only aggregate counts are in the repo (`analysis/output/bbqs_aggregates.json`); the
  workbook stays outside the repo.
