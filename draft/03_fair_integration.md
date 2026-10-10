# 3. FAIR data requires integration across layers

*(~850 words; Fig. 2, Table 2)*

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
layers**. A neurophysiology dataset on DANDI is a concrete example. The DANDI archive makes the dataset
findable and accessible. Within the dataset, files are organized in the DANDI layout, and each file
follows NWB, which defines its structure and metadata. The NWB schema is written in the HDMF schema
language, and the files are stored in HDF5 or Zarr, which makes the bytes machine-readable. Species are
annotated with NCBI Taxonomy terms, which gives the metadata a shared meaning. The video analogy makes the 
same point. A video is easy to find and reuse only when it uses a common codec, sits in a standard container,
carries meaningful tags, and is published on a platform, and no single one of these steps makes it shareable on
its own.

Large consortia show the same pattern at the scale of whole programs. The BRAIN Initiative Cell Census
Network (BICCN) [REF: BICCN 2021] distributed its data by modality across specialized archives, with
omics data going to NeMO, microscopy to BIL, neurophysiology to DANDI, and volumetric electron
microscopy and X-ray data to BossDB. Each archive has its own standards, and BICCN connected them
through a central data inventory. Its successor, the BRAIN Initiative Cell Atlas Network (BICAN),
follows the same model and adds a data catalog and a specimen metadata system that tracks provenance and
terminology across archives [REF: BICAN data page; BICCN data page] [TODO-C33]. Such stacks work, but
each consortium builds and maintains the integration itself.

## Levels of FAIRness, and where each layer contributes

To illustrate why integration across layers is needed, Table 2 describes six levels of FAIRness for neuroscience data. 
The levels are not a new metric. Their purpose is to illustrate which layer of the map
contributes at each step, so each level is defined by what a third party can do with the data, mapped to
the FAIR principles it mainly addresses, and tied to the layer whose technologies make it possible (Fig.
2) [TODO-C6]. The idea of a staged scale is familiar from five-star Linked Open Data [REF: Berners-Lee
2006] and from Data Readiness Levels, which adapt the Technology Readiness Levels used in engineering to
data [REF: Lawrence 2017; Mankins 1995]. For assessing the FAIRness of a specific dataset, the community
has developed maturity indicators, the Research Data Alliance FAIR Data Maturity Model, and automated
tools such as F-UJI, which score each principle separately [REF: Wilkinson 2019; Bahim 2020; Devaraju
2021].

| Level | What the data offer | Layer that adds it | FAIR principles mainly addressed | Example |
|---|---|---|---|---|
| 0, opaque | Bytes that can only be read with the original software or documentation | None | None | Proprietary acquisition files without a public specification; raw `.bin` voltage traces |
| 1, readable | Data in an open, documented format that generic tools can read, with technical metadata such as data types and dimensions | Data formats | I1 (formal, shared representation) | Bare HDF5, Zarr, TIFF, or CSV files |
| 2, interpretable files | Each file, for example one recording session, has a standardized structure and contains the metadata needed to understand it | File organization standards\* | R1 (rich metadata), R1.3 (community standards) | A validated NWB file |
| 3, organized dataset | The whole experiment can be navigated, with consistent file names, folder structure, and dataset-level metadata | Dataset organization standards\* | R1, R1.3, F2 (data described with rich metadata) | A validated BIDS or DANDI-layout dataset |
| 4, interoperable | Metadata values are drawn from shared terminologies and ontologies, so that datasets can be searched and combined with others | Ontologies and terminologies | I2 (FAIR vocabularies), I3 (qualified references) | NWB or BIDS data with species from the NCBI Taxonomy, locations from an atlas, and events annotated with HED |
| 5, findable and reusable record | Data are deposited with a persistent identifier, searchable metadata, licence, and provenance, and can be retrieved through a standard protocol | Data archives (with persistent identifiers) | F1–F4, A1–A2, R1.1 (licence), R1.2 (provenance) | An annotated BIDS and NWB dataset with a DOI on DANDI or EMBER |

File and dataset organization standards are defined in schema languages, which make conformance at
levels 2 and 3 machine-checkable by validators such as the NWB Inspector and the BIDS Validator. Schema
languages therefore do not add a level of their own but make levels 2 and 3 verifiable.

Two caveats apply. First, the levels describe a typical path, not a strict sequence. Levels 2 and 3
complement each other. In a BIDS dataset of NIfTI images, for example, much of the metadata lives in
dataset-level sidecar files rather than inside the images. Depositing an opaque file in a
general-purpose repository makes it findable and accessible but not interoperable or reusable, which is
why formal assessments score each principle separately. Second, the levels describe data, not the
standards themselves. The maturity of a standard, including its specification, tools, validators, and
adoption, is a separate question that technology readiness scales are better suited to [TODO-C34].

Read from top to bottom, the table shows that each step up requires technologies from an additional
layer of the map. A format alone reaches level 1, a file organization standard is needed for level 2, a
dataset organization standard for level 3, terminologies and ontologies for level 4, and an archive for
level 5. This is the practical reason why **integration across the ecosystem matters more than the
choice of any single standard**, and why the recommendations for BBQS in Section 7 cover several layers
at once.
