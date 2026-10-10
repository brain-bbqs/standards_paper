# Paper plan

*Updated 2026-10-10. A full first draft exists, so this plan no longer describes content. It records
(1) decisions that are not visible in the draft itself and (2) the steps needed to finish and submit.
Item IDs (D, A, S, F, C) refer to `TODO.md`, which holds the details and owners.*

| What | Where |
|---|---|
| Draft (one file per section) | `draft/` |
| Open decisions, actions, claims to check | `TODO.md` (run `make check`) |
| Figures and legends | `figures/`, `draft/12_figures_tables.md` |
| Knowledge graph code, data, and open issues | `knowledge_graph/`, `knowledge_graph/TODO.md` |
| BBQS inventory analysis (aggregates only) | `analysis/` |

---

## 1. Decisions

### Publication

| Decision | Choice |
|---|---|
| Journal and type | **Scientific Data, Article.** No word limit; abstract ≤170 words; ≤8 figures, ≤10 tables; legends ≤350 words in total; title ≤110 characters without colons, parentheses, or uncommon acronyms; Data and Code Availability required; Nature reference style with DOIs |
| Title | "Navigating neuroscience data standards for multimodal brain behavior quantification and synchronization" (103 characters) |
| Preprint | bioRxiv at submission |
| Target submission | ~March 1, 2027 |
| Fees and pre-submission enquiry | Open (D9) |

### Scope and framing

| Decision | Choice |
|---|---|
| Structure | Part I (Sections 1–4) maps the ecosystem and is descriptive. Part II (Sections 5–8) applies the map to BBQS and gives recommendations |
| Recommendations | Community guidance derived from the BBQS guideline, not a ranking of standards. Stated in general terms for multimodal brain–behavior studies; BBQS specifics (EMBER, DCAIC) in "Implementation in BBQS". How prescriptive: open (D4) |
| BBQS guideline | Presented as our own work ("we developed"), since Working Group members are key authors; acknowledgements thank only non-author members (check against final author list, A1) |
| Knowledge graph | A main result (Section 4, Fig. 3). Counts connections (pairs of technologies); undirected relations stored once per pair; lenient community rule as a sensitivity analysis (Suppl. Fig. S1). Community rule: open (D10) |
| FAIR levels | Six levels (0–5), an illustration of why integration across layers is needed, not a new metric |
| BRAIN Knowledge Base | Mentioned only as a future direction, without a program-specific claim unless a public source exists (C32). The roundtable materials are background only and are never quoted or cited |
| Tone on funding | Describe scientific needs and where investment helps; no criticism of current funding |

### Terminology and style

| Decision | Choice |
|---|---|
| Layer names | Data archives; dataset organization standards; **file organization standards** ("file" in the broad sense); ontologies & terminologies (one layer, distinction explained); data formats; schema languages |
| Video analogy | Used only in Section 2 and Fig. 1; later sections use the layer terms |
| Style | No colons or em-dash asides in prose; no judgmental statements about other approaches; avoid framing that could read as controversial |

### Figures

| Decision | Choice |
|---|---|
| Fig. 1 | Single panel: a generic video-sharing app with callouts to the six layers. No real platform name, logo, or look |
| Fig. 2 | The six layers as a stack beside the FAIR staircase. The only general stack diagram; Fig. 5 reuses it with BBQS technologies highlighted |
| Generated figures | Fig. 3, Suppl. Fig. S1, Fig. 4 are built from code (`make figures`); the others are designed |

### Data handling

| Decision | Choice |
|---|---|
| BBQS inventory | Aggregate statistics only. The workbook stays outside the repository; publication needs BBQS clearance (A2) |
| Credentials | FAIRsharing and SciCrunch tokens are never stored in the repository; credentialed harvests are run by OR |
| Release | Code and data on Zenodo with a DOI at submission (A6); licences to be set (S1, S3) |
| Writing platform | Markdown + git for the core team; move to Google Docs for the full author group (A8) |

### Authorship

| Decision | Choice |
|---|---|
| Authors | Poster authors plus confirmed contributors ("2025 SfN – Standards" sheet); list closes **Nov 14, 2026** (A1) |
| Roles | CRediT; corresponding authors O. Rübel and Y. Halchenko |
| Perspective | Make international efforts (EBRAINS/openMINDS, UK, EU) visible, not only NIH |

---

## 2. Steps to finish

### Phase 1 — Core-team review (Oct 13 – Nov 14, 2026)
1. Core team reads the full draft and comments section by section; OR assigns section leads (A3).
2. Settle the open framing decisions: D4 (how prescriptive), D5 (ontology wording), D8 (relation to
   existing classifications, what the map leaves out, stack geometry), D10 (community rule).
3. Complete the knowledge-graph inputs: FAIRsharing relations (KG 1.1), RRID gaps (KG 2.x). Re-run
   `make figures` and update Section 4 numbers (C25, C26, C35).
4. Claude-owned claims and references: web and literature checks, resolve references marked ? or —
   (A7).
5. OR-owned claims that need expert input: C27 (LinkML efforts), C37 (ongoing NWB/BIDS work to cite).
6. Request BBQS clearance for the aggregate statistics (A2) and a versioned guideline release (A5).
7. Close the author list (A1, Nov 14). Brief the figure designer (F2, F3).

### Phase 2 — Journal and author review (Nov 17 – Dec 19, 2026)
1. Decide on a pre-submission enquiry and the fee source (D9).
2. Move to Google Docs and open author review round 1 (A8).
3. Standards teams check Section 6, Table 3, and R1–R11 (A4); domain experts verify knowledge-graph
   edges and node assignments (KG 1.3).
4. Designed figures in first versions (F2, F3); review Fig. 4 (F4).

### Phase 3 — Revision (Jan 5 – Feb 6, 2027)
1. Incorporate review round 1 and the teams' feedback.
2. Freeze the knowledge graph (versioned harvest), regenerate figures, finalize Fig. 3 (F5).
3. Final figures and legends within 350 words (F6).
4. Zenodo release of code and data (A6); licences (S1, S3); data access contact (S2).

### Phase 4 — Sign-off and submission (Feb 8 – Mar 1, 2027)
1. Author review round 2 and sign-off.
2. Statements: competing interests (S4), funding (S5), contributions; all claims in `TODO.md` §4
   resolved (`make check` shows no open claims).
3. References in Nature style with DOIs (S6); format, supplementary material, cover letter.
4. Submit to Scientific Data and post to bioRxiv.

---

## 3. Open questions not tracked elsewhere

- **Leads.** Who leads the knowledge graph and the BBQS case study after the core-team review (domain
  verification, final numbers, responses to reviewers)?
- **Large source files.** The poster `.pptx`, BBQS workbook, and BRAIN KB materials stay outside the
  repository (in the parent folder). Confirm this before the repository is shared or made public.

## 4. Risks

| Risk | Mitigation |
|---|---|
| Knowledge-graph results depend on incomplete registry data | Complete FAIRsharing relations (KG 1.1), report coverage, keep the sensitivity analysis, frame as a first version |
| BBQS clearance delayed or restricted | Only aggregate counts in the paper; Section 5 can be reduced to qualitative statements if needed |
| Standards teams disagree with Table 3 or the recommendations | Early review by the teams (A4); recommendations framed as community guidance |
| 30+ authors slow the review rounds | Fixed review windows, section leads, silence-is-consent sign-off |
| Overlap with the BRAIN KB community paper | Mention knowledge bases only as a future direction; cite the KB paper when public |
