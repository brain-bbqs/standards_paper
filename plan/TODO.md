# Paper TODO

*Last updated 2026-10-09. Draft: `draft/` (Sections 1–10, statements, Methods, figure registry,
references; main text ≈ 7,700 words incl. tables, abstract 169/170 words). Figures: `figures/`.
Knowledge-graph issues: `knowledge_graph/TODO.md` (summarized in section 5 below).*

## How to use this list

- Tick `[x]` when done and move the item to **6. Resolved** with a one-line note and date.
- **Owner** says who has to act: **OR** (Oliver Rübel), **core** (core writing team), **authors**
  (all co-authors), **WG** (BBQS Data Standards Working Group), **BBQS** (BARD.CC / DCAIC / program
  staff), **teams** (NWB, BIDS, Psych-DS, HED, EMBER, DANDI maintainers), **Claude** (can be done by
  Claude on request, e.g., literature or web checks, text edits, scripts).
- In the draft, `[TODO-Cn]` marks a claim listed in section 4, and `[REF: …]` a citation still to be
  inserted (see `draft/13_references.md`).
- Run `make check` after editing. It reports claim markers without an entry, entries without a marker,
  and file paths in this list that no longer exist.

## Summary

| Section | Open items | Blocking submission? |
|---|---|---|
| 1. Decisions | D2, D4, D5, D8, D9, D10 | D4, D8, D10 |
| 2. Actions | A1–A8, S1–S6 | A1, A2, A4, A5, A6, S1–S5 |
| 3. Figures | F2–F6 | all |
| 4. Claims | C1–C38 (38) | all, before submission |
| 5. Knowledge graph | see `knowledge_graph/TODO.md` | 1.1–1.3 (Fig. 3, Section 4 results) |

---

## 1. Decisions (open)

- [ ] **D2 — Length and tables** No word limit at Scientific Data, so
      no cuts are required. Tighten for readability; Tables 2 and 3 already sit in the text as formal
      tables.
- [ ] **D4 — How prescriptive are the recommendations?** *(OR, WG, BBQS)*. Section 7 gives R1–R11
      "derived from the BBQS guideline". Confirm the framing (community guidance vs. program
      requirements) with the WG and program staff.
- [ ] **D5 — Ontology layer wording** *(core)*. One layer with the ontology/terminology distinction
      explained (Section 2, video analogy: fixed category list vs. category hierarchy). Confirm wording
      (claim C4).
- [ ] **D8 — Six layers vs. the literature**. Remaining sub-decisions
      (the layer-3 name is resolved, see section 6):
      - [ ] The introduction now says we "use [FAIRsharing and RRID] as the basis for the map". Keep that
            claim only if Section 2 makes the link explicit (see the next item).
      - [ ] Add a short "relation to existing classifications" paragraph to Section 2. The usual
            life-science distinction is reporting guidelines / models and formats / terminologies, plus
            repositories and policies [REF: Sansone 2012; Sansone 2019]; FAIRsharing record types match it
            (our harvest: 314 model/format, 257 terminology, 62 reporting guideline, 14 identifier
            schema). Our contribution is splitting FAIRsharing's single "model and format" type into
            dataset organization, file organization, formats, and schema languages.
      - [ ] Cover what the map leaves out (reporting guidelines / minimum information such as COBIDAS,
            ARRIVE, CDEs; persistent identifiers; access protocols / APIs; provenance; policies and
            licences) in one paragraph and a note under Table 1, not as more layers. State that
            modelling standards (NeuroML, SONATA, PyNN) are out of scope.
      - [ ] Stack geometry for Fig. 5, now the only stack diagram (Figs. 1 and 2 have none): keep six stacked
            layers, or draw a four-level structural stack (archives, dataset organization, file
            organization, formats) with ontologies/terminologies and schema languages as cross-cutting
            columns. The design draft (F10, v3) uses the four-level structural stack, with ontologies (4) and
            schema languages (6) as side panels next to the file and dataset organization rows.
- [ ] **D9 — Journal logistics** *(OR)*. Scientific Data APC and who pays (plan Q6); whether to send a
      pre-submission enquiry (planned ~Nov 17) or submit directly.
- [ ] **D10 — Community rule for bridges** *(OR, core)*. Adopt the proposal in
      `knowledge_graph/TODO.md` 1.2: a technology's *home* community is where it originated and is
      governed; other tags mean "communities served" and are reported separately. Determines the
      numbers in Section 4 (claim C25) and Fig. 3.

## 2. Actions (open)

**People and authorship**
- [ ] **A1** Author list and CRediT roles: to be decided (not necessarily all poster authors); close Nov 14 *(OR)*.
      The draft says "we developed" the BBQS guideline (Sections 1, 7) and thanks WG members "who are not
      authors" (Acknowledgements). Check this still fits once the author list is final *(OR)*.
- [ ] **A3** Assign section leads from the contributor list to review each section *(OR)*.
- [ ] **S4** Competing-interest statements from all authors; several authors lead standards or archives
      discussed in the paper *(authors)*.
- [ ] **S5** Complete funding list for all authors (`draft/10_statements.md`) *(authors)*.
- [ ] **A8** Move to Google Docs for the full author group once the core team has reviewed *(OR)*.
- [ ] **A9** *(later)* Consider a BBQS FAIR Implementation Profile (Schultes 2020) as a supplement: one row per
      FAIR principle with the BBQS technology choices from Sections 6–7; needs BBQS WG endorsement (D4) and EMBER
      for archive-policy rows (access, metadata longevity, licence, provenance) *(OR, WG, EMBER)*.

**External input**
- [ ] **A2** BBQS clearance to publish the **aggregate** inventory statistics (Section 5, Fig. 4), and
      agreed wording for the source *(BBQS)*.
- [ ] **A4** NWB, BIDS, Psych-DS, HED, and EMBER teams check Section 6, Table 3, and R1–R11 *(teams)*.
- [ ] **A5** Versioned release of the BBQS guideline (e.g., Zenodo) to cite; the guideline still has many
      "TODO — how to store?" entries *(WG)*.
- [ ] **S2** Contact for access to the BBQS project inventory (Data Availability statement) *(BBQS)*.

**Release and licensing**
- [ ] **A6** Zenodo DOI for code and data (`knowledge_graph/`, `analysis/`, `figures/`) *(OR; Claude can prepare)*.
- [ ] **S1** Licence terms for redistributing RRID and FAIRsharing data (FAIRsharing CC BY-SA?) *(OR; Claude can check)*.
- [ ] **S3** Licences for code (e.g., BSD-3 or MIT) and data (e.g., CC BY 4.0) *(OR)*.

**References**
- [ ] **A7** Resolve references marked ? or — in `draft/13_references.md` *(Claude)*.
- [ ] **S6** Convert references to Nature style with DOIs (BibTeX/Zotero) *(Claude)*.

**Submission files**
- [ ] **A10** Add a submission build (e.g., `make submission`) next to the review build (`make pdf`), which
      already has line numbers *(Claude)*:
      - Leave out working notes: `[TODO-Cn]` and `[REF: …]` markers, word-count targets, draft-status
        lines, the display-items table in `draft/12_figures_tables.md`, and the table of contents.
      - References in Nature style, cited by number in the text (after S6); leave out the working list in
        `draft/13_references.md`.
      - Suppl. Table S1 (RDA indicators): Scientific Data discourages supplementary files unless they add
        ~10 pages or more, so keep it in the manuscript as a regular table (or decide otherwise).
      - Initial submission: PDF is accepted. Revision: `.docx` or one self-contained `.tex` with the
        references written into it (no separate `.bib`/`.bbl` files or style files).
      - Check the required headings for an Article (Data Availability, Code Availability, Author
        Contributions, Competing Interests) and the figure-legend limit (F6).

## 3. Figures (open)

Files: `figures/` (one folder per item, see `figures/README.md`). Legends: `draft/12_figures_tables.md`.
Rebuild generated figures with `make figures`.

- [ ] **F2** Design Fig. 1 as a single panel: a generic video-sharing app with callouts to the six
      layers and neuroscience examples (`figures/fig1_ecosystem_map/README.md`; analogy from poster slide 6).
      No real platform name, logo, or look in the artwork. Redraw from the poster: Fig. 6b
      (`figures/fig6_bridges_future/`).
      Use "file organization standards" and the outcome of D8 *(designer / figure lead)*.
- [ ] **F3** Final artwork for Fig. 2 (FAIR staircase, `figures/fig2_fair_levels/`) and Fig. 5 (BBQS stack,
      `figures/fig5_bbqs_stack/`); design drafts exist for both *(designer)*.
- [ ] **F4** Review Fig. 4 (`figures/fig4_bbqs_data/fig4_bbqs_data.pdf`): keep the species panel? show
      "exploratory behavior" (no guideline entry) as a gap? *(OR, core)*.
- [ ] **F5** Polish Fig. 3 (`figures/fig3_knowledge_graph/`): label collisions, how to show shared
      infrastructure edges, colour-blind palette; after D10 and edge verification *(Claude, then OR)*.
- [ ] **F6** Shorten legends to ≤350 words in total; sans-serif fonts, white backgrounds *(Claude)*.
- [ ] **F7** Review the Fig. 2 design draft (`figures/fig2_fair_levels/fig2_fair_levels_design.pptx`): staircase only,
      steps styled and numbered like Fig. 1, climbing arrow and summit flag; check the FAIR principles per step (definitions in
      the speaker notes; the RDA mapping is only in Suppl. Table S1) *(OR)*.
- [ ] **F9** Re-export the PNG previews of Fig. 1 and Fig. 2 from PowerPoint after the layer renumbering
      (the .pptx files are updated; the PNGs still show the old numbers) *(OR)*.
- [ ] **F10** Review the Fig. 5 design draft v2 (`figures/fig5_bbqs_stack/fig5_bbqs_stack_design.pptx`): stack
      geometry (D8), the data groups and paths (Table 3), and the status of each in-progress item (NWBEPs, BEPs,
      Neuro Termsets, BIDS PR #2367, Psych-DS extensions; status as of the Oct 2026 forum). Check with the
      BBQS WG and the NWB, BIDS, and Psych-DS teams (C17, C37); recheck status before submission *(OR, WG)*.
      Table 3 follow-ups the figure raises: raw video and audio in BIDS → "ext. (BEP047)"; questionnaires in
      BIDS "partial" (phenotype/); a row or note for multi-subject data (ndx-multisubjects, planned BEP).
- [ ] **F8** Suppl. Table S1 (in `draft/12_figures_tables.md`): review the layer contributions
      with a FAIR expert (C6); export as a spreadsheet for the supplement *(core, Claude)*.

## 4. Claims that need support

| ID | Section | Claim / text | What is needed | Owner |
|---|---|---|---|---|
| C1 | 1 | Experiments now generate terabytes each | Citations with concrete numbers (Neuropixels, whole-brain imaging, multi-camera video) | Claude |
| C2 | 1 | BRAIN archive sizes | **DANDI** 1,197 Dandisets, 2.44 PB from `api.dandiarchive.org/api/stats/` (authoritative; cite with access date). **BossDB** ~1.03 PB, >10 petavoxels and **NeMO** >1 PB, >3 M files: from search snippets, verify. **BIL** petascale, ~7,000 datasets (Kenney 2024): verify. **OpenNeuro**: get an official figure. Consider DABI, NEMAR, EMBER. Do not use the BRAIN KB roundtable summary (not for distribution) | core (archive contacts); Claude for re-checks |
| C3 | 1 | AI raises the value of consistently structured data | Citation (AI-readiness / foundation models) or soften | Claude |
| C4 | 2 | Ontologies and terminologies in one layer | Team confirmation (D5); optional citation | core |
| C5 | 2 | Origin and funding of standards (research vs. vendor vs. archive) | NWB, BIDS, and DICOM are cited; name and cite one or two archive- or consortium-specific standards (e.g., DANDI layout, SPARC SDS) | Claude |
| C6 | 3 | Six levels of FAIRness (Table 2), one per layer that adds a capability; mapped to the RDA FAIR Data Maturity Model in Suppl. Table S1; schema languages enable levels 2–3 | Check the level and layer assignments of the RDA indicators in Suppl. Table S1 with a FAIR expert; check FAIRsFAIR v0.8 metric IDs against the specification. F-UJI demonstration on example datasets deferred until after this review | core (FAIR expert); Claude for F-UJI |
| C7 | 5, Methods | BBQS inventory statistics | Clearance (A2); name, date, and maintainer of the inventory | BBQS |
| C8 | 5 | 13 species groups | Check "fish" and "fly" entries (is "fish" zebrafish?) and whether any award is missed | Claude |
| C9 | 5 | Terminologies and atlases are sparse for many BBQS species | Citation or examples (atlases for mouse, rat, human, marmoset; few for cowbird, cichlid, acoel) | Claude |
| C10 | 5, Methods | Modality counts from keyword matching (video 25, wearables 18, pose 13, audio 13, eye tracking 10, ephys 13, EEG 8, ophys 5) | Manual check against the source entries; adjust keywords | Claude |
| C11 | 5 | 18 standards answers: NWB 11, BIDS 4, none 3; 3D pose stored as NumPy | Check; the questionnaire may be outdated (re-survey?) | Claude; BBQS |
| C12 | 5 | Sharing: archive 13/18, cloud drives 14/18, GitHub 14/18 | Check; are cloud drives and GitHub used for data or code? | Claude; BBQS |
| C13 | 6 | Why these standards were chosen (open, community-governed, BRAIN-supported, accepted by EMBER, extensible) | Confirm with the WG; cite charter or minutes if any | WG |
| C14 | 6 | EMBER privacy levels; many projects record identifiable human data | EMBER documentation; aggregate count of human projects with video or audio | teams (EMBER); Claude for count |
| C15 | 6, 7 | BEP032 would bring NWB into BIDS | Not in a released BIDS version as of v1.11.2 (2026-09-29; checked against the BIDS changelog on 2026-10-17). Draft specification in bids-specification PR #2307. Cite the BEP032 page or pull request; update Sections 6, 7, and 8 if it is released before submission | Claude; teams |
| C16 | 6 | HED for NWB via ndx-hed; "one of few annotation systems that work across standards" | ndx-hed citation; soften or support "one of few" | Claude; teams (HED) |
| C17 | 7 | Table 3 entries | Check by NWB/BIDS/Psych-DS teams (A4); BIDS status for video (BEP044, issue 1771), audio, GPS | teams; Claude for web check |
| C18 | 7 | Store pose with ndx-pose or Motion-BIDS | Does Motion-BIDS suit 2D/3D pose from video (it targets motion capture)? Cite ndx-pose | Claude; teams |
| C19 | 7 | Synchronization must be documented; cannot be reconstructed afterwards | Citation or soften; does any standard define clock-alignment metadata? | core; Claude for search |
| C20 | 7 | Behavior ontologies (NBO) exist but are rarely used in BBQS | Cite NBO; check other behavior vocabularies; inventory shows one award considering NBO | Claude |
| C21 | 7 | Large and continuous recordings (split raw/processed; multi-day data) | Guideline section is unfinished; needs WG content | WG |
| C22 | 7 | Early standardization is cheaper than conversion at the end | Citation or soften | Claude |
| C23 | 8, Methods | Behavior × guideline coverage (`analysis/behavior_coverage.csv`) | Check coding against the guideline; "cognitive tasks" Psych-DS entry is TODO in the guideline although Psych-DS lists task data; truncated "reproductive b" entry may be a 4th award | Claude; WG |
| C24 | 8 | Technologies without guidance (EMG, force plates, VR, home cage, coding software, thermal, smart devices); EMG supported in BIDS since v1.11.0 (BEP042; released in v1.11.0, 2026-02-04) | Check the NWB status for EMG (Table 3 keeps "—"); ask the WG to add EMG and BIDS eye tracking (BEP020, also in v1.11.0) to the guideline, then update `analysis/behavior_coverage.csv` (eye movements, BIDS) and Fig. 4c | Claude; teams; WG |
| C25 | 4, 8, Methods | Knowledge-graph results, counted per connection (pair of technologies; decided 2026-10-09): 72 technologies, 122 relationships forming 110 connections; 88/110 connect layers; 52/110 involve shared infrastructure; 26 of 58 domain-specific connections cross communities, 23 of them through BIDS, NWB, HED, or EMBER (BIDS alone in 14). Two of the 26 are generic RRID "related to" links (BossDB–EMBER, DANDI–EMBER) whose meaning is unconfirmed | Resolve `knowledge_graph/TODO.md` 1.1–1.3 and D10, then update the numbers (`knowledge_graph/output/stats.md`) | core; Claude for re-run |
| C26 | 4 | Many documented relationships are not recorded in registries | Do not state a number until the FAIRsharing relations are complete (`knowledge_graph/TODO.md` 1.1); some "missing" relations may only be missing from the REST API. Decide whether we submit the missing relationships to FAIRsharing/RRID ourselves (and say so in the paper) or leave it to the technology teams | OR (FAIRsharing contact) |
| C27 | 8 | LinkML as a bridge; Psych-DS is defined in LinkML; NWB schema being expressed in LinkML; exploratory LinkML work for BIDS | Cite LinkML; cite the NWB-in-LinkML effort(s) and the BIDS LinkML exploration (OR to name which projects to cite and how to describe their status) | OR, Claude |
| C28 | 8 | Highest-value bridges for BBQS | Team agreement (a recommendation of the paper) | core |
| C29 | 9 | Reuse at scale needs remote/partial access, virtual datasets, curation | Citations (cloud-native formats, DataLad) | Claude |
| C30 | 9 | Minimal required metadata still needed with AI-generated annotation | Citation, or frame as our position | core |
| C31 | 9 | Standards are long-lived infrastructure; software changes faster | Citation (research software sustainability) or frame as position | Claude |
| C32 | 9 | Knowledge bases connecting data, metadata, and derived findings across archives are a natural next step (BRAIN Initiative mention removed by OR) | Cite a public source only (e.g., the BRAIN KB paper when available); never the roundtable summary | core |
| C33 | 3 | BICCN/BICAN multi-archive stacks (NeMO, BIL, DANDI, BossDB; catalog; NIMP) | Confirm NIMP description and whether BICAN uses BossDB; cite BICCN 2021 and the portals | core (BICAN contact); Claude for citations |
| C34 | 3 | Maturity of standards is better described by technology readiness scales | Citation, or remove | Claude |
| C36 | 7 | R11: DANDI accepts NWB; OpenNeuro, NEMAR, and DABI accept BIDS | Check which standards each archive accepts (DABI: BIDS and NWB?); cite archive pages | Claude |
| C38 | 3 | General FAIR assessments can test only whether data follow a community standard; whether data have the structure, units, timing, and metadata a standard requires can be checked only with that standard's validators | FAIR-expert check; optionally cite a discussion of domain-specific FAIR assessment (e.g., FAIR-IMPACT discipline-specific metrics) | core (FAIR expert); Claude |
| C37 | 8 | Gaps are being addressed: events/annotations, links to external vocabularies, multi-subject data, via NWB proposals/extensions and BIDS BEPs | OR to pick 2–4 representative examples to cite (e.g., NWBEP001 / PyNWB 4.0 core events; relevant behavior/multi-subject BEPs; NWB multi-subject work) | OR |

## 5. Knowledge graph (summary of `knowledge_graph/TODO.md`)

These carry the Section 4 results and Fig. 3, so they block submission. Details and the full checklist
are in `knowledge_graph/TODO.md`, section 0.

- [ ] **1.1 FAIRsharing relations.** The REST API omits relations shown on fairsharing.org. Contact
      FAIRsharing and/or transcribe the relations of the 46 seed records by hand *(OR)*.
- [ ] **1.2 Community rule** = decision D10 above *(OR, core)*.
- [ ] **1.3 Expert verification** of all curated edges and node layers/communities *(domain reviewers)*.
- [ ] **2.1–2.5 Data gaps:** RRIDs by hand (`knowledge_graph/RRID_LOOKUP.md`) or via SciCrunch API
      permission; 25 seeds without FAIRsharing record; candidate seeds to add or drop *(OR / Claude)*.

---

## 6. Resolved

| Date | Item | Resolution |
|---|---|---|
| 2026-10-09 | Pivot | Map of the ecosystem first, then recommendations for BBQS (`plan/paper_plan.md` §1) |
| 2026-10-09 | D1 Journal | Scientific Data, article type "Article". No word limit; Methods unlimited; abstract ≤170 words; ≤8 figures, ≤10 tables; legends ≤350 words in total; title ≤110 characters without colons, parentheses, or uncommon acronyms; required statements (Data/Code Availability, contributions, competing interests, funding, ethics) in `draft/10_statements.md`; Nature reference style with DOIs; data/code sharing required where relevant to results |
| 2026-10-09 | D7 Title | "Navigating neuroscience data standards for multimodal brain behavior quantification and synchronization" (103 characters) |
| 2026-10-09 | D8 layer name | Layer 3 renamed "file organization standards" (parallel to "dataset organization standards"); "file" in the broad sense, single file vs. directory is a format choice; knowledge-graph taxonomy label updated (node id `data_standard` unchanged) |
| 2026-10-09 | FAIR levels | Six levels (0–5) mapped to layers and FAIR principles; presented as an illustration of integration, not a new metric; related to 5-star Linked Open Data, Data Readiness Levels, and FAIR assessment tools |
| 2026-10-15 | Layer order | Layers numbered bottom-up to match the levels of FAIRness: 1 data formats, 2 file organization, 3 dataset organization, 4 ontologies & terminologies, 5 data archives, 6 schema languages. Applied to Table 1 (new # column), Section 2 (paragraph order), Fig. 1 and Fig. 2 badges, Fig. 1 caption, Fig. 5 legend, Sections 1 and 9 |
| 2026-10-15 | Fig. 2 | Layer stack removed (repeated Fig. 1 and the step labels); steps styled and numbered like Fig. 1; climbing arrow and summit flag; full mapping in the speaker notes. Fig. 5 is now the only stack diagram |
| 2026-10-15 | FAIR alignment | Levels aligned with the RDA FAIR Data Maturity Model in Suppl. Table S2 only (level and contributing layers for all 41 indicators; removed from Table 2 and Fig. 2 as too complex for the main text) (not one level per indicator, which under-credited standards); F-UJI named as one implementation (tools disagree, Sun 2022). Five-star Open Data removed (open/linked data, not FAIR). Tables 2 and 3 moved to `draft/12_figures_tables.md` |
| 2026-10-16 | Suppl. Fig. S1 | Dropped (lenient community rule not needed as a supplementary figure). Section 4 no longer discusses the lenient rule (C35 removed); it explains that each technology is assigned to the community in which it originated so the graph shows which connections cross communities. The lenient-rule graph is kept for review as an alternate figure, `figures/alternates/kg_lenient_community_rule/` (`make alt-kg-lenient`) |
| 2026-10-16 | Suppl. Table S1 | Dropped (standards comparison from the poster: modalities, formats, languages, funding/origin; supported one sentence in Section 2, which now cites NWB, BIDS, and DICOM directly). The RDA indicator table (Suppl. Table S2 in earlier entries) is renumbered Suppl. Table S1 |
| 2026-10-09 | D3 Knowledge graph | Main result: Section 4 and Fig. 3; lenient rule as Suppl. Fig. S1 (dropped 2026-10-16) |
| 2026-10-09 | D6, F1 Display items | 6 figures, 3 tables, 1 supplementary figure and table (Suppl. Fig. S1 dropped 2026-10-16); numbered in order of first citation; within journal limits |
| 2026-10-09 | Figures folder | `figures/` with one folder per item, `make figures`, `make check` |
| 2026-10-09 | KG counting | Undirected relations (*related to*, *interoperates with*) counted once per pair; 11 RRID links had been stored in both directions (133 → 122 relationships, 33 → 31 bridges) |
| 2026-10-09 | KG unit | Section 4 counts connections (pairs of technologies), matching Fig. 3; the stats report gives both connections and relationships |
| 2026-10-09 | Style | Prose colons and em-dash asides removed; opening reframed around the complexity of the ecosystem; video analogy woven through Section 2 with callbacks |
| 2026-10-10 | Fig. 1 | Single panel: a generic video-sharing app with callouts to the six layers, not a layered diagram. Layers are defined in Table 1 and shown as a stack in Fig. 2 and Fig. 5; Section 2 cites Fig. 1 for the analogy and Table 1 for the layers |
| 2026-10-10 | Fig. 2 | Shows the six layers as a stack beside the FAIR staircase, with connectors from each step to its layer; the only general stack diagram, reused for Fig. 5 |
| 2026-10-10 | Analogy | The video analogy is used only in Section 2 and Fig. 1; callbacks in Sections 3, 6, 8, and 10 removed |
| 2026-10-10 | Section 7 scope | Recommendations stated in general terms for multimodal brain–behavior studies; BBQS specifics (EMBER, DCAIC, synchronization) in a closing "Implementation in BBQS" subsection; title changed accordingly |

## Notes for reviewers

- Part I (Sections 1–4) maps the ecosystem; Part II (Sections 5–8) applies it to BBQS; Section 9 is the
  outlook and Section 10 the conclusion. See `plan/paper_plan.md` for decisions and the timeline.
- The BRAIN KB roundtable materials in `../brain_knowledge_base/` are marked "not for further
  distribution" and are used only as background; nothing from them is quoted or cited.
- BBQS inventory: only aggregate counts are in the repository (`analysis/output/bbqs_aggregates.json`);
  the workbook stays outside it.
