# Display items (plan: ≤6 main items)

Status: **spec** = described only; **draft** = generated draft exists; **poster** = redraw from poster.

| # | Item | Status | Source / file |
|---|---|---|---|
| Fig. 1 | Ecosystem map + analogy | poster | SfN poster, layers + video-platform analogy |
| Table 1 | Layer definitions | spec (text below) | poster table |
| Fig. 2 | FAIR ladder and example stack | poster | poster "FAIR Data Score" |
| Fig. 3 | BBQS standards stack on the map | spec | Section 5 |
| Table 2 | Recommended standards by BBQS data type | draft (in `06_recommendations.md`) | guideline |
| Fig. 4 | BBQS data: (a) species, (b) behaviors and modalities, (c) behaviors × guideline coverage | draft | `analysis/bbqs_inventory.py` → `analysis/output/fig4_bbqs.*` |
| Fig. 5 | Bridges at every layer + future directions wheel | spec / poster | Section 7–8, poster wheel |
| Suppl. Fig. S1 | Ecosystem knowledge graph (layers × communities) | draft | `knowledge_graph/`, `ecokg figure` → `knowledge_graph/output/fig3_ecosystem.*` |
| Suppl. Table S1 | Standards and archives comparison (modalities, formats, languages, funding/origin) | poster | poster tables |

Table 2 is the seventh main item; if the journal limit is 6, move Table 1 to the Supplement or merge it
into Fig. 1 [TODO-F1].

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

## Fig. 2 — FAIR data require integration across layers

Ladder of five levels (0 opaque → 4 FAIR-aligned scientific record; see table in Section 3), showing
for each level which layers of the map are needed, and an example stack for level 4 (DANDI/EMBER →
BIDS/DANDI layout → NWB + HED → HDF5/Zarr, HDMF schema, NCBI Taxonomy).

## Fig. 3 — The BBQS standards stack

The map from Fig. 1 with BBQS technologies highlighted: EMBER (archive); BIDS, Psych-DS, DANDI layout
(dataset organization); NWB (file organization standard); HED, NCBI Taxonomy, atlases, Cell Ontology
(terminologies); HDF5/Zarr, JSON/TSV/CSV, MP4, NIfTI (formats); HDMF, LinkML, BIDS schema (schema
languages). Arrows show supported paths for typical BBQS data (e.g., video + pose + ephys → NWB → DANDI
layout → EMBER; MRI + EEG + events → BIDS + HED → EMBER; questionnaires → Psych-DS → EMBER).

## Fig. 4 — BBQS data and standards coverage

**(a)** Species groups across 28 awards. **(b)** Behavioral and neural modalities (awards mentioning
each). **(c)** Behavior types reported by projects (bars: number of awards, n = 22) and, for each, the
level of guidance in NWB, BIDS, and Psych-DS (supported / in progress / no guidance). Aggregate data
only.

## Fig. 5 — Bridges and future directions

**(a)** Six types of bridges placed on the map (structural; schema language; semantic — schema
elements; semantic — values; archive linking; dataset-level common data elements). **(b)** Future
directions (living data, data reuse, multimodal data, AI and new technologies, coordination centers)
and cross-cutting needs (education and training, outreach and community engagement, maintenance and
support), redrawn from the poster.

## Supplementary Fig. S1 — Ecosystem knowledge graph

Technologies (nodes) arranged by layer (rows) and home community (columns; cross-cutting communities on
the right). Edges styled by community scope (cross-community, within community, shared infrastructure);
dots mark relationships also recorded in a registry (RRID or FAIRsharing).
