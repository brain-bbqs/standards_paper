# 3. FAIR data requires integration across layers

*(target ~600 words; Fig. 2)*

The FAIR principles of findability, accessibility, interoperability, and reusability [REF: Wilkinson
2016] are often used as if they were a property of a standard ("a FAIR format"). The map shows why this
is misleading. FAIRness is a property of **data**, and each layer contributes a different part of it.

- **Data formats** contribute *interoperability* at the level of bytes, because any software that reads
  HDF5 or TIFF can open the file.
- **File organization standards** contribute *structure and required metadata*. They define what the
  arrays mean, their units, how they relate in time, and which metadata must be present, which is the
  basis of *reusability*.
- **Dataset organization standards** make the contents of a collection predictable, so people and
  software can navigate many sessions and subjects.
- **Ontologies and terminologies** give metadata values shared meaning, enabling search and integration
  across datasets (*interoperable* and *findable* metadata).
- **Archives** make data *findable and accessible*, with persistent identifiers, landing pages, access
  control, and search over metadata.
- **Schema languages** make the rules machine-readable so that compliance can be validated
  automatically.

No single technology covers all of these. FAIR data emerge from technologies **integrated across
layers**. A neurophysiology dataset on DANDI is a concrete example. The DANDI archive (findable,
accessible) holds NWB files (structure and metadata) organized in the DANDI layout, whose schema is
defined in the HDMF language and stored in HDF5 or Zarr (machine-readable, interoperable bytes), with
species annotated using NCBI Taxonomy terms (shared meaning).

Large consortia show the same pattern at the scale of whole programs. The BRAIN Initiative Cell Census
Network (BICCN) [REF: BICCN 2021] distributed its data by modality across specialized archives, with
omics data going to NeMO, microscopy to BIL, neurophysiology to DANDI, and volumetric electron
microscopy and X-ray data to BossDB. Each archive has its own standards, and BICCN connected them
through a central data inventory. Its successor, the BRAIN Initiative Cell Atlas Network (BICAN),
follows the same model and adds a data catalog and a specimen metadata system that tracks provenance and
terminology across archives [REF: BICAN data page; BICCN data page] [TODO-C33]. Such stacks work, but
each consortium builds and maintains the integration itself.

## A ladder of FAIRness

To make this concrete, we describe five levels of FAIRness of a dataset (Fig. 2) [TODO-C6].

| Level | Description | Example |
|---|---|---|
| 0 — Opaque | Raw binary data without embedded or linked metadata; cannot be interpreted without external documentation | Raw `.bin` voltage traces; proprietary formats with no public specification |
| 1 — Minimal technical metadata | Basic structural metadata (data type, dimensions, byte order), no experimental context or provenance | Bare HDF5, Zarr, NIfTI-1, or MATLAB arrays |
| 2 — Core experimental metadata | Basic context such as session IDs, acquisition parameters, timestamps; little provenance or standardization | NIfTI with BIDS sidecars; EDF EEG; MEF with header information |
| 3 — Extended domain-specific metadata | Rich, structured metadata on acquisition, design, stimuli, processing and provenance, using controlled vocabularies | NWB or BIDS with complete metadata |
| 4 — FAIR-aligned scientific record | Comprehensive standardized metadata with ontology annotation and persistent access through an archive; reusable without external context | Ontology-annotated BIDS + NWB + HED dataset shared on DANDI or EMBER |

Each step up the ladder requires technologies from additional layers. A format alone reaches level 1; a
file or dataset organization standard is needed for levels 2–3; and level 4 requires ontologies or
terminologies and an archive in addition. This is the practical reason why **integration across the
ecosystem matters more than the choice of any single standard**, and why the recommendations for BBQS in
Section 6 cover several layers at once.