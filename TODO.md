# Paper TODO — first draft review

*Status 2026-10-09: first full draft in `draft/` (Sections 1–9, Methods, display-item plan, references).
Main text ≈ 5,560 words including the two in-text tables (target ~5,000). Knowledge-graph issues are
tracked separately in `knowledge_graph/TODO.md` on branch `worktree-knowledge-graph`.*

Conventions in the draft: `[TODO-Cn]` = claim needing support (listed below); `[REF: …]` = citation to
insert (see `draft/12_references.md`; entries marked ? or — need work).

---

## D. Decisions for the team

- [ ] **D1 — Journal.** Leading option (2026-10-09): **Scientific Data (Nature Portfolio)**, which has
      published BIDS, its modality extensions, and the FAIR principles.
      - Likely article type: **Article** (fits map + BBQS inventory analysis + knowledge graph +
        recommendations). Alternative: **Comment** (much shorter; would need ~half the length and most
        of the BBQS analysis removed).
      - [ ] Verify on nature.com/sdata (could not be fetched automatically): article types, word /
            display-item / reference limits, whether Methods count, APC and funding source (Q6), and
            whether a pre-submission enquiry is possible or useful.
      - Other options if needed: eLife, PLOS Computational Biology, Neuroinformatics, Nature
        Communications (Perspective; weaker fit after the BBQS pivot).
      - Consequence if Article: keep the knowledge graph as evidence (D3) and resolve
        `knowledge_graph/TODO.md` 1.1–1.3 before submission.
- [ ] **D2 — Length.** Cut ~600 words or move Table 2 / the FAIR-ladder table to display items, depending on D1.
- [ ] **D3 — Role of the knowledge graph.** Draft uses it as supporting evidence (Section 7, Suppl.
      Fig. S1). Keep, shrink to a sentence, or drop? Depends on resolving `knowledge_graph/TODO.md` 1.1–1.3.
- [ ] **D4 — How prescriptive.** Part II now gives recommendations R1–R11 "derived from the BBQS
      guideline". Confirm the framing (community guidance vs. program requirements) with the BBQS
      Data Standards WG and program staff.
- [ ] **D5 — Ontology layer.** Kept as one layer with the distinction explained (Section 2) per Q1;
      confirm wording.
- [ ] **D6 — Figure count.** Seven candidate main items (Fig. 1–5, Tables 1–2); see F1.

## A. Actions

- [ ] **A1** Author list and CRediT roles (poster authors + confirmed contributors; close Nov 14).
- [ ] **A2** BBQS clearance: confirm with BARD.CC / DCAIC and program staff that the **aggregate**
      inventory statistics (Section 4, Fig. 4) may be published; agree on wording for the source.
- [ ] **A3** Section leads to review each section (assign from contributor list).
- [ ] **A4** NWB, BIDS, Psych-DS, HED, and EMBER teams to check Section 5, Table 2, and R1–R11.
- [ ] **A5** Version the BBQS guideline (e.g., Zenodo release) so the paper can cite a fixed version; the
      guideline itself still has many "TODO — how to store?" entries and some unfinished parts.
- [ ] **A6** Zenodo DOI for code and data (`ecokg`, `analysis/`).
- [ ] **A7** Resolve references marked ? or — in `draft/12_references.md`.
- [ ] **A8** Move to Google Docs for the full author group once the core team has reviewed this draft.

## F. Figures

- [ ] **F1** Main-item budget (D6): merge Table 1 into Fig. 1 or move to Supplement if limit is 6.
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
| C2 | 1 | Neuroscience archives hold petabytes | Public figure with citation (archive reports; avoid the BRAIN KB roundtable summary, which is not for distribution) |
| C3 | 1 | AI raises the value of consistently structured data | Citation (AI-readiness / foundation-model papers) or soften |
| C4 | 2 | Ontologies vs. terminologies kept in one layer; "used the same way" | Team confirmation (D5); optional citation |
| C5 | 2 | Origin/funding of standards (research vs. vendor vs. archive-driven) | Suppl. Table S1 from poster; check each entry |
| C6 | 3 | FAIR ladder (levels 0–4) | Our framework from the poster: say so explicitly, or relate to existing FAIR maturity models (e.g., FAIR metrics) with citation |
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
| C17 | 6 | Table 2 entries | Check by NWB/BIDS/Psych-DS teams (A4); BIDS status for video (BEP044 / issue 1771), audio, GPS |
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

---

## Notes for reviewers

- Part I (Sections 1–3) is descriptive; Part II (Sections 4–7) gives BBQS recommendations; Section 8 is
  the outlook. See `plan/paper_plan.md` §0 for the pivot.
- The BRAIN KB roundtable materials in `../brain_knowledge_base/` are marked "not for further
  distribution" and are used only as background; nothing from them is quoted or cited.
- BBQS inventory: only aggregate counts are in the repo (`analysis/output/bbqs_aggregates.json`); the
  workbook stays outside the repo.
