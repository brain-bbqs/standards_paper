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
annotated with NCBI Taxonomy terms, which gives the metadata a shared meaning. No single one of these technologies makes the
dataset FAIR on its own.

Large consortia show the same pattern at the scale of whole programs. The BRAIN Initiative Cell Census
Network (BICCN) [REF: BICCN 2021] distributed its data by modality across specialized archives, with
omics data going to NeMO, microscopy to BIL, neurophysiology to DANDI, and volumetric electron
microscopy and X-ray data to BossDB. Each archive has its own standards, and BICCN connected them
through a central data inventory. Its successor, the BRAIN Initiative Cell Atlas Network (BICAN),
follows the same model and adds a data catalog and a specimen metadata system that tracks provenance and
terminology across archives [REF: BICAN data page; BICCN data page] [TODO-C33]. Such stacks work, but
each consortium builds and maintains the integration itself.

## Levels of FAIRness, and where each layer contributes

To illustrate why integration across layers is needed, Table 2 describes six levels of FAIRness for
neuroscience data. The levels are not a new metric. Their purpose is to show which layer of the map
contributes at each step, so each level is defined by what a third party can do with the data and tied
to the layer whose technologies make it possible (Fig. 2) [TODO-C6]. To anchor the levels in established
practice, Table 2 lists for each level the main indicators it adds from the Research Data Alliance (RDA)
FAIR Data Maturity Model, which translates the FAIR principles into 41 indicators for data and metadata
[REF: RDA FDMM 2020; Bahim 2020]. The same indicators underlie the FAIRsFAIR metrics implemented by the
automated assessment tool F-UJI [REF: Devaraju 2021a; Devaraju 2021b]. Many indicators depend on more
than one layer, and Suppl. Table S2 shows which layers contribute to each. Staged scales of this kind
are also familiar from Data Readiness Levels, which adapt the Technology Readiness Levels used in
engineering to data [REF: Lawrence 2017; Mankins 1995]. Assessment tools, in contrast, score each
principle separately, and different tools can give different results for the same dataset
[REF: Wilkinson 2019; Sun 2022].

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

The alignment with the RDA indicators also shows where standards carry the most weight. Most indicators
for findability and accessibility concern the published record, are met mainly by archives, and are
well suited to automated testing. The contribution of file and dataset organization standards, by
contrast, is condensed into a few indicators, chiefly that data and metadata comply with a community
standard (RDA-R1.3-01D, RDA-R1.3-01M). Whether data actually have the structure, units, timing, and
required metadata that a standard defines can be checked only with that standard's own validators, such
as the NWB Inspector and the BIDS Validator [TODO-C38].

Read from top to bottom, Table 2 shows that each step up requires technologies from an additional
layer of the map. A format alone reaches level 1, a file organization standard is needed for level 2, a
dataset organization standard for level 3, terminologies and ontologies for level 4, and an archive for
level 5. This is the practical reason why **integration across the ecosystem matters more than the
choice of any single standard**, and why the recommendations in Section 7 cover several layers
at once.
