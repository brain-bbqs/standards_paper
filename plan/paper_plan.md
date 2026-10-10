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
| Journal and type | **Nature Scientific Data, Article.** No word limit; abstract ≤170 words; ≤8 figures, ≤10 tables; legends ≤350 words in total; title ≤110 characters without colons, parentheses, or uncommon acronyms; Data and Code Availability required; Nature reference style with DOIs |
| Working Title | "Navigating neuroscience data standards for multimodal brain behavior quantification and synchronization" (103 characters) |
| Preprint | bioRxiv at submission |
| Target submission | 12/2026 - 03/2027 |
| Fees and pre-submission enquiry | Open (D9) |



### Figures

- Fig. 3, Suppl. Fig. S1, Fig. 4 are built from code (`make figures`)
- Other figures are currently only described as ideas/concepts in README files and captions but need to be prepared

### Authorship

* Need to decide on authorship 
   - BBQS Standard Working Group members?
   - A subset of BBQS folks?
   - Full ist of authors from the poster?

---

## 2. Steps to finish

### Phase 1 — Core-team review (Oct 13 – Nov 14, 2026)
1. Complete the knowledge-graph inputs: FAIRsharing relations (KG 1.1), RRID gaps (KG 2.x). Re-run
   `make figures` and update Section 4 numbers (C25, C26, C35).
2. Core team reads the full draft and comments section by section; OR assigns section leads (A3).
3. Settle the open framing decisions: D4 (how prescriptive), D5 (ontology wording), D8 (relation to
   existing classifications, what the map leaves out, stack geometry), D10 (community rule).
4. General check of all claims (`TODO.md` §4, C1–C37). For each claim, verify it against a source,
   add the citation, or soften or remove it. Claude does a first pass (literature and web checks,
   proposed citations and wording) and records the result in each row; claims that need expert input
   (e.g., C27 LinkML efforts, C37 ongoing NWB/BIDS work, Table 3 entries) go to OR or the teams.
5. Resolve references marked ? or — in `draft/13_references.md` (A7).
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
