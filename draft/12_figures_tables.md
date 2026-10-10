# Display items

Files: `figures/` (one folder per item; `figures/README.md`). Status: **spec** = described only; **draft** = generated draft exists; **poster** = redraw from poster.
Scientific Data recommends at most 8 figures and 10 tables; the 6 figures and 3 tables fit. Figure legends
must total ≤350 words (F6).

| # | Item | Section | Status | Source / file |
|---|---|---|---|---|
| Fig. 1 | Ecosystem map + video analogy | 2 | poster | `figures/fig1_ecosystem_map/` |
| Table 1 | Layer definitions | 2 | draft (below) | poster table |
| Fig. 2 | Six levels of FAIRness and the layer that adds each | 3 | spec (poster "FAIR Data Score" to be redrawn to match) | `figures/fig2_fair_levels/` |
| Table 2 | Levels of FAIRness mapped to layers and FAIR principles | 3 | draft (in `03_fair_integration.md`) | |
| Fig. 3 | Ecosystem knowledge graph (layers × communities) | 4 | draft | `figures/fig3_knowledge_graph/` (`make fig3`) |
| Fig. 4 | BBQS data: (a) species, (b) modalities, (c) behaviors × guideline coverage | 5, 8 | draft | `figures/fig4_bbqs_data/` (`make fig4`) |
| Fig. 5 | BBQS standards stack on the map | 6 | spec | `figures/fig5_bbqs_stack/` |
| Table 3 | Recommended standards by BBQS data type | 7 | draft (in `07_recommendations.md`) | BBQS guideline |
| Fig. 6 | Bridges at every layer + future directions | 8, 9 | spec / poster | `figures/fig6_bridges_future/` |
| Suppl. Fig. S1 | Knowledge graph with the lenient community rule (sensitivity) | 4 | draft | `figures/supplementary/figS1_knowledge_graph_lenient/` (`make figS1`) |
| Suppl. Table S1 | Standards and archives comparison (modalities, formats, languages, funding/origin) | 2 | poster | `figures/supplementary/tableS1_standards_comparison/` |

---

## Fig. 1 — A map of the neuroscience data standards ecosystem

**(a)** The six layers, ordered from the user (archives) to storage (data formats) and formal
description (schema languages), with representative neuroscience examples and the main relationships
between layers (archives accept dataset organization and file organization standards; dataset organization standards arrange files that follow file organization standards and formats; file organization standards use formats and terminologies and are
defined with schema languages). **(b)** The video analogy used throughout the text, drawn as the path of one video from phone to platform, with each step aligned to its layer: YouTube (archive), playlist or series with episode names (dataset organization, cf. BIDS file names), MP4 container keeping video, audio, and subtitles in sync (file organization standard, cf. NWB), categories and hashtags (terminologies and ontologies), H.264/AV1 codec (data format), and the specification behind the upload form (schema language).

## Table 1 — Layers of the ecosystem

| Layer | Problem | Use case | Examples |
|---|---|---|---|
| Data archives | Publish, share, and discover content | Publish a series of datasets on a topic | DANDI, EMBER, OpenNeuro, NEMAR, DABI, BIL, BossDB, NDA, EBRAINS, SPARC |
| Dataset organization standards | Organize collections of files in accepted standards and formats | Organize data from a full experiment | BIDS, Psych-DS, DANDI layout, SPARC SDS, NeuroBlueprint |
| File organization standards | Organize data and metadata within a file, using primitives supported by formats | Organize data from one session or modality | NWB, OME-TIFF/OME-Zarr, NIX, odML, openMINDS, DICOM, EDF |
| Ontologies & terminologies | Define terms and represent domain knowledge, incl. relationships | Annotate data to define the meaning of terms | NCBI Taxonomy, Uberon, Cell Ontology, Allen CCF, HED, Cognitive Atlas, NBO |
| Data formats | Map data to storage | Serialize generic data structures | HDF5, Zarr, TIFF, NIfTI, JSON, YAML, CSV/TSV, MP4 |
| Schema languages | Provide a formal language for the structure and rules of data | Formally define file organization standards, dataset organization standards, and ontologies | JSON Schema, XML Schema, RDF/OWL, LinkML, HDMF |

## Fig. 2 — Levels of FAIRness and where each layer contributes

A staircase of six levels (0 opaque, 1 readable, 2 interpretable files, 3 organized dataset,
4 interoperable, 5 findable and reusable record; Table 2). Each step is labeled with the layer of the
map whose technologies make it possible (data formats; file organization standards; dataset organization
standards; ontologies and terminologies; archives with persistent identifiers) and with the FAIR
principles it mainly addresses. A vertical bar beside steps 2–3 marks schema languages, which make these
levels machine-checkable through validators. An example neuroscience dataset is shown climbing the
steps (bare HDF5 → validated NWB file → BIDS or DANDI-layout dataset → NCBI Taxonomy, atlas, and HED
annotations → DOI on DANDI or EMBER). A side note marks that formal assessment scores each principle
separately (RDA indicators, F-UJI).

## Fig. 3 — Connections in the ecosystem

Knowledge graph of 72 technologies (nodes) and the 110 connections between them (edges; one line per pair
of technologies, which may be linked by several relationships), drawn with the six layers as
rows and the community in which each technology originated as columns; shared, domain-agnostic
infrastructure (general, cross-species biology) is on the right. Edges are styled by scope: relationships
between communities (red), within a community (grey), and with shared infrastructure (dashed). Dots mark
relationships also recorded in a registry (RRID or FAIRsharing). Bridges between communities concentrate
on BIDS, NWB, HED, and EMBER.

## Fig. 4 — BBQS data and standards coverage

**(a)** Species groups across 28 awards. **(b)** Behavioral and neural modalities (awards mentioning
each). **(c)** Behavior types reported by projects (bars: number of awards, n = 22) and, for each, the
level of guidance in NWB, BIDS, and Psych-DS (supported / in progress / no guidance). Aggregate data
only.

## Fig. 5 — The BBQS standards stack

The map from Fig. 1 with BBQS technologies highlighted: EMBER (archive); BIDS, Psych-DS, DANDI layout
(dataset organization); NWB (file organization standard); HED, NCBI Taxonomy, atlases, Cell Ontology
(terminologies); HDF5/Zarr, JSON/TSV/CSV, MP4, NIfTI (formats); HDMF, LinkML, BIDS schema (schema
languages). Arrows show supported paths for typical BBQS data (e.g., video + pose + ephys → NWB → DANDI
layout → EMBER; MRI + EEG + events → BIDS + HED → EMBER; questionnaires → Psych-DS → EMBER).

## Fig. 6 — Bridges and future directions

**(a)** Six types of bridges placed on the map (structural; schema language; semantic — schema
elements; semantic — values; archive linking; dataset-level common data elements). **(b)** Future
directions (living data, data reuse, multimodal data, AI and new technologies, coordination centers)
and cross-cutting needs (education and training, outreach and community engagement, maintenance and
support), redrawn from the poster.

## Supplementary Fig. S1 — Sensitivity to the community rule

As Fig. 3, but classifying a relationship as within community whenever the two technologies share any
community tag (lenient rule) instead of comparing the communities in which they originated. Most bridges
disappear, because technologies are often tagged with the communities they reached through those bridges.
