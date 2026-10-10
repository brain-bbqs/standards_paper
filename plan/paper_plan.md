# Paper Plan: The Neuroscience Data Standards Ecosystem

*Working plan — drafted 2026-10-09; updated 2026-10-09 with answers to open questions, and again on 2026-10-09 with the **BBQS pivot** (see §0). Sources: SfN 2025 poster ("The Ecosystem of Standards in Neuroscience: Which Ones Are For You?"), `data standards perspective paper 2026.md`, `Guidelines_Data_standards.md`, `bbqs_projects/`, `brain_knowledge_base/`.*

---

## 0. Pivot (2026-10-09): from ecosystem survey to BBQS recommendations

The overall direction stays (start with the map and classification of the ecosystem), but the later parts
now focus on **standards for BBQS**: recommendations for the BBQS community derived from the BBQS data
standards guideline, with the ecosystem map as the frame. Consequences:

- **Title:** *"Navigating neuroscience data standards for multimodal brain behavior quantification and synchronization"* (2026-10-09; shortened from "Navigating the neuroscience data standards
  ecosystem: a map and recommendations for multimodal Brain Behavior Quantification and Synchronization
  (BBQS)" to meet Scientific Data's title rules).
- **Q3 reversed for Part II:** the paper now *does* give recommendations (for BBQS data), presented as
  community guidance derived from the guideline, not a universal ranking of standards. Part I stays
  descriptive.
- **Knowledge graph:** supporting evidence (bridges/gaps section and Supplementary), no longer a headline
  result. Its open issues are tracked in `knowledge_graph/TODO.md`.
- **Journal: Scientific Data, Article** (decided 2026-10-09). No word limit; abstract ≤170 words;
  ≤8 figures, ≤10 tables; title ≤110 characters without colons, parentheses, or uncommon acronyms
  (title updated accordingly, `TODO.md` D7); Data and Code Availability statements required.
- **Draft:** `draft/` (one Markdown file per section); open claims and questions in `TODO.md`.
- Sections 1–4 below are kept for history; where they conflict with this section, this section wins.

## 1. Decisions so far

| Decision | Choice |
|---|---|
| Article type | **Perspective + light analysis**: an intuitive map of the ecosystem, plus a perspective on gaps and future needs, backed by one data-driven figure |
| Scope | **Start broad** (neuroscience data standards in general), then **call out BBQS** as the concrete case study; mention emerging efforts such as the BRAIN Knowledgebase (KB) briefly |
| BRAIN KB position paper | **Mention only**: a separate community paper is in progress; we cite it and point to it in Future Directions without coordinating content |
| Knowledge graph (KG) | **One key evidence figure**: build it from FAIRsharing and RRID, release it as a resource, and use it to back the "few cross-community bridges" claim |
| Primary journal | **Nature Communications, Perspective** (open access) |
| Preprint | **bioRxiv at submission** |
| Timeline | **Submit ~late Feb – early Mar 2027** |
| Working title | ~~"The ecosystem of standards in neuroscience: Current state and future directions"~~ → **"Navigating neuroscience data standards for multimodal brain behavior quantification and synchronization"** (2026-10-09) |
| Framing | *Superseded for Part II by §0.* **Landscape, not a selection guide**: the focus is the parts of the ecosystem and how they relate; no single standard does everything, so integration across components is essential |
| Ontology layer | **One layer** ("Ontologies & Terminologies"), with the distinction made explicit: ontologies define terms *and* encode definitions and relationships; terminologies define the set of valid terms, often selected from ontologies |
| Funding tone | **Needs- and science-focused**: say where investment is needed, not criticize current funding |
| Writing platform | **Markdown + git** until an outline and first draft exist, then move to Google Docs for the full author group |

---

## 2. Goals and core message

**Goal 1: An approachable map.** Give the community shared definitions for the *parts* of the standards ecosystem and the *role* each part plays. Each part is defined by the problem it solves, and is made intuitive through analogies such as video platforms: YouTube = archive, playlist = dataset organization, MP4 = data standard, H.264 = data format, hashtags = ontologies, upload form = schema language.

**Goal 2: A perspective on gaps and future directions.** Show where the ecosystem is strong and where the seams are, and what is needed next, with BBQS (multimodal, naturalistic behavior across many species) as the stress test.

**Take-home messages (draft):**
1. **"Data standard" means many different things.** Separating the ecosystem into layers by the *problem* each solves (archives, dataset organization, data standards, ontologies/terminologies, data formats, schema languages) gives technologists and practitioners a common map. It also shows when a project is crossing a boundary, i.e., when to build a bridge rather than expand scope.
2. **FAIR is a property of the data, not of a single technology.** FAIR data emerges from *integrating* technologies across layers (e.g., DANDI ← NWB ← HDMF/HDF5 ← NCBI Taxonomy).
3. **There is no one standard to rule them all.** Each component solves a different part of the problem, and FAIR, multimodal science needs them to work together.
4. **Standards have built bridges *within* communities (BIDS, NWB) but rarely *across* them.** Integration across modalities and communities is still done by users and large consortia at high cost. Bridges at every layer are the next frontier and a key area for future investment.

**Working title:** "The ecosystem of standards in neuroscience: Current state and future directions"

**What this paper is *not*:** a guide to choosing a standard. Selection guidance is already in community resources (e.g., the BBQS data standards guideline) and is cited, not reproduced.

---

## 3. Target journal

### Primary: Nature Communications — Perspective
- Limits (verify against the current guide before drafting): **≤5,000 words, ≤6 display items, ≤60 references**; fully open access.
- Why: broad readership across neuroscience and data science, and the format fits a map-plus-perspective paper.
- Action: send a **pre-submission enquiry** (abstract, outline, figure sketches, author list) in November 2026, before the full draft is complete.
- Note: the fee is substantial (about $6–7k; verify). Funding source to be determined (candidates: BARD.CC / DANDI / EMBER awards, institutional OA agreements).

### Backups, in order
| # | Journal / type | When to switch | Restructuring needed |
|---|---|---|---|
| 1 | **eLife — Review Article** (OA, no formal length limit) | Nature Comms declines the enquiry | Can *expand*: bring the poster's comparison tables back into the main text |
| 2 | **Scientific Data — Analysis** (OA) | We want the KG to carry more weight | KG becomes the backbone (Methods/Results); perspective content moves to Discussion |
| 3 | **PLOS Computational Biology — Perspective** or **Frontiers in Neuroinformatics — Perspective/Review** (OA, lower fees) | Fast, lower-cost fallback | Minimal |
| — | Imaging Neuroscience (OA, about $1,600 fee) / Aperture Neuro (OA, ≤$1,000) | Only if we pivot toward a neuroimaging-centric audience | Moderate |

*Open item:* confirm current article-type limits and fees for each before switching.

---

## 4. Proposed structure (~5,000 words, 6 display items)

| § | Section | ~Words | Content | Source material |
|---|---|---|---|---|
| — | Abstract | 150 | | |
| 1 | **Introduction: one word, many meanings** | 600 | Data abundance versus the knowledge bottleneck; standards success stories (BIDS, NWB, DICOM, OME); confusion caused by "standard" meaning many things; multimodal programs (BBQS) and AI raise the stakes; the paper's two goals | Notes; BRAIN KB slides ("bytes ≠ value ≠ knowledge") |
| 2 | **A map of the ecosystem** | 1,300 | Six layers, each with *Problem / Use case / Description*; video-platform analogy; fuzzy boundaries (DICOM as both format and standard, NWB/OME over HDF5/Zarr/TIFF); ontologies vs. terminologies within one layer (ontologies encode definitions and relationships, terminologies list valid terms, often drawn from ontologies); how the map frames scope ("when do we cross a boundary?") | Poster, notes §"Definitions", guideline glossary |
| 3 | **FAIR requires integration across layers** | 700 | FAIR metadata ladder (0 opaque → 4 FAIR-aligned record); each layer contributes different FAIR facets (formats → interoperability; standards → structure and identifiers; archives → findable/accessible; ontologies → reusable meaning); worked stack example (DANDI/NWB/HDMF/HDF5/NCBI Taxonomy) | Poster FAIR score, notes §"Role of the ecosystem toward FAIR" |
| 4 | **Stakeholders and adoption** | 500 | Standards start from different stakeholders (research-driven NWB/BIDS vs. vendor-driven DICOM), yet must serve the whole data lifecycle; clear problem and stakeholder definitions give scope and future direction | Notes §"Adoption" |
| 5 | **Mapping the connections: an ecosystem knowledge graph** | 700 | KG built from FAIRsharing and RRID records; edges typed as *within-layer*, *cross-layer (vertical)*, and *cross-community/modality (horizontal)*; main finding (hypothesis): dense vertical links, sparse horizontal ones | New analysis (workstream B) |
| 6 | **Building bridges** (with **BBQS case study box**) | 900 | Six bridge types: (1) structural: file-level standards ↔ dataset organization; (2) schema languages (e.g., LinkML) for harmonization; (3) semantic annotation of schema elements (what a field *means*, via ontologies); (4) semantic annotation of metadata values (which terms are valid, via terminologies/controlled vocabularies); (5) archives: linked data and cross-references; (6) dataset level: common data elements. BBQS box: 28 awards, 13+ species, naturalistic multimodal behavior; which standards projects chose; behavior types with no clear home | Notes §"Discussion", BBQS inventory, guideline TODOs |
| 7 | **Future directions and needs** | 600 | From the poster wheel: living data, data reuse, multimodal data, AI and new technologies, coordination centers; cross-cutting needs: education and training, outreach, maintenance and support. Agent-era point: minimal required schema plus flexible annotation still matters. Where investment is needed: integration across standards, maintenance, and the people who do this work (framed as scientific needs, not criticism). Brief pointer to BRAIN KB efforts | Poster; BRAIN KB roundtable summary (cite as context only) |
| 8 | **Conclusion** | 200 | | |
| — | Methods (KG) | ~400, may sit outside the word count (verify) | Data sources, harvest date, schema, edge classification, code/data DOI | |

### Display items (6 max)
1. **Fig. 1 — The ecosystem map.** Layered diagram of the six categories and the relationships between them, side by side with the video-platform analogy. *(Redraw from the poster.)*
2. **Table 1 — Layer definitions.** Problem, use case, description, and key neuroscience examples per layer.
3. **Fig. 2 — The FAIR ladder.** Levels 0–4, with how each level requires technologies from additional layers and an example stack.
4. **Fig. 3 — Ecosystem knowledge graph.** Nodes colored by layer, edges colored within-community vs. cross-community; inset quantifying edge types.
5. **Fig. 4 — BBQS case study.** (a) Species × modality coverage of BBQS projects; (b) standards chosen; (c) heatmap of behavior types × standard support (NWB / BIDS / Psych-DS), showing gaps.
6. **Fig. 5 — Bridges and future directions.** The six bridge types placed on the map, plus the future-needs wheel.

**Supplementary:** full standards and archive comparison tables from the poster (modalities, formats, languages, funding/origin); KG methods and statistics; FAIRsharing collection link. No decision guide: point readers to the BBQS guideline and the standards' own documentation instead.

---

## 5. Workstreams

### A. Writing *(leads: O. Ruebel, Y. Halchenko; section leads TBD)*
- Assign one lead and one or two contributors per section (§1–7), drawn from the confirmed-contributor list.
- Drafting in **Markdown under git** (one file per section, e.g., `draft/01_introduction.md`) while the core team builds the outline and first draft; then move to **Google Docs** for the wider author group's comments and edits.

### B. Ecosystem knowledge graph *(lead TBD — see Q4)*
1. Harvest FAIRsharing records for neuroscience-relevant standards, formats, terminologies, and repositories via the FAIRsharing API, using record-to-record relationships (e.g., "implements", "related to", "recommended by"). Add RRID/SciCrunch records for resources and tools.
2. Map each record to a **layer** (our taxonomy) and a **community/modality** (neuroimaging, neurophysiology, microscopy, behavior, clinical, omics, general).
3. Classify edges: within-layer, cross-layer (same community), cross-community.
4. **Gap report → contributors.** List missing or incomplete records and relationships; ask each standard/archive team to update their FAIRsharing records (deadline mid-December).
5. Create a **FAIRsharing Collection** for the neuroscience standards ecosystem as a maintainable, living index (cite in the paper).
6. Re-harvest, freeze a versioned snapshot, and archive data and code on Zenodo with a DOI.
- *Risk:* FAIRsharing relationship coverage is uneven, which can bias the "sparse horizontal edges" finding. Mitigate with contributor curation and by reporting coverage explicitly.

### C. BBQS case study *(lead TBD — see Q4; data: BBQS data inventory)*
- Source: `Information ingest-BBQS_All_Projects_OneSheet.xlsx` (28 awards: R34, R61, U01) and the R34/R61/U01 data-inventory slides.
- First pass from the sheet: species are human (17 project entries), mouse (14), plus rat, gerbil, ferret, sheep, marmoset, capuchin, songbird, cichlid, fly, fish, and acoel worm. Standards recorded: mostly NWB (~11), BIDS (~4, 2 with HED), and "none yet" (~3, e.g., 3D pose stored as `.npy`). Many projects list Dropbox, Box, or Drive as sharing locations, in addition to or instead of archives.
- Behavior gaps: the BBQS guideline lists many behavior types and devices with "TODO — how to store?" (EMG, force plates, VR, home-cage monitoring, facial expressions, social interactions, feeding, operant conditioning, GPS, acoustic in BIDS/Psych-DS, …). Convert these into a support matrix.
- Report **aggregate** statistics only; confirm with the BBQS coordinating center (BARD.CC) and program staff that project-level information can be used.

### D. Figures *(lead TBD)*
- Redraw poster graphics to journal specifications, keeping one consistent visual language for layers across all figures.

### E. Authorship and community
- Authors: the 33 poster authors plus contributors confirmed in the "2025 SfN – Standards" sheet ("Confirmed Paper Contributor" column). Close the author list by **Nov 14, 2026**.
- Use CRediT roles; corresponding authors O. Ruebel and Y. Halchenko.
- Acknowledge the BBQS Data Standards Working Group; list all grants (from the poster acknowledgements).
- Make sure international perspectives (EBRAINS/openMINDS, UK, EU) are visible, not only NIH.

---

## 6. Timeline (target submission ~Mar 1, 2027)

| When | Milestone |
|---|---|
| **Oct 13–24, 2026** | Finalize this plan; circulate it to contributors; assign section and workstream leads (Q4); set up the git repo and Markdown section files |
| **Oct 27 – Nov 14** | Detailed outline and abstract; figure sketches; KG v0 harvest; author list closed (Nov 14) |
| **~Nov 17** | **Pre-submission enquiry to Nature Communications** |
| **Nov 17 – Dec 12** | Section drafts; FAIRsharing record curation by contributors (deadline Dec 12); BBQS case-study analysis |
| **Dec 18** | **Full draft v1** (all sections, draft figures); move from Markdown to Google Docs for author review |
| **Jan 5 – Jan 23, 2027** | Author review round 1 (3 weeks) |
| **Jan 26 – Feb 6** | Revise; KG frozen snapshot plus Zenodo DOI; final figures |
| **Feb 8 – Feb 19** | Author review round 2 and sign-off (2 weeks); CRediT, competing interests, and funding statements collected |
| **Feb 22 – Mar 1** | Formatting, supplementary material, cover letter |
| **~Mar 1, 2027** | **Submit to Nature Communications and post to bioRxiv** |

---

## 7. Questions

### Resolved (2026-10-09)
| # | Question | Decision |
|---|---|---|
| Q1 | Split the ontology layer? | **No, keep one layer.** Make the distinction explicit in the text: ontologies define terms *and* encode definitions and relationships; terminologies define valid terms, often selected from ontologies |
| Q2 | Title | **"The ecosystem of standards in neuroscience: Current state and future directions"** |
| Q3 | How prescriptive? | **Not prescriptive.** Focus on the broader landscape, the relationships between components, and the need for integration because no single standard does everything. Selection guidance is cited, not reproduced |
| Q5 | Writing platform | **Markdown + git** until outline and first draft exist; then **Google Docs** |
| Q7 | Tone on funding | **Focus on needs and scientific aspects**: describe where investment is needed, not criticism of the lack of funding |

### Still open
- **Q4 — Workstream leads.** Who leads the **knowledge graph** (workstream B: FAIRsharing/RRID harvest and analysis) and the **BBQS case study** (workstream C)? *Note:* the answer given ("the KB effort is currently separate…") reads as being about the BRAIN **Knowledgebase**. That is consistent with the plan (BRAIN KB = future-direction mention only), but the KG and BBQS leads are still unassigned.
- **Q6 — Fee funding.** To be determined.
- **Q8 — Git repository.** Initialize this folder as a git repo now? If so, decide where large source files (the 34 MB poster `.pptx`, BBQS decks, BRAIN KB PDFs) live: committed, git-LFS, or kept out of the repo (`.gitignore`). Some (BBQS inventory, BRAIN KB meeting reports) may not be meant for a shared or public repo.

---

## 8. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Nature Comms declines the enquiry | Pivot to eLife Review (no length limit) with minimal rework; decide by early December |
| Overlap with the BRAIN KB position paper | Stay focused on the *standards map and bridges*; refer to KB only as a future direction; cite it if it is available |
| KG findings driven by incomplete FAIRsharing data | Contributor curation round; report coverage; frame the KG as illustrative evidence |
| 30+ authors slow the review rounds | Fixed review windows, section leads, silence-is-consent sign-off |
| Content exceeds 5,000 words / 6 items | Move comparison tables to Supplementary and the living FAIRsharing collection |
| Unpublished BBQS project details | Aggregate statistics only; get clearance from BBQS leadership |

---

## 9. Immediate next steps

1. Resolve Q4 (KG and BBQS leads) and Q8 (git setup); Q6 can wait until submission.
2. Set up the Markdown drafting structure (one file per section) and draft a detailed outline.
3. Send the plan and a call for section leads to the contributor list (link the "2025 SfN – Standards" sheet).
4. Start the KG harvest (FAIRsharing API) to see real coverage before committing to Fig. 3's framing.
5. Draft the abstract and the one-page pre-submission enquiry.
