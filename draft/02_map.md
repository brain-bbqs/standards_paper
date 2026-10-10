# 2. A map of the data standards ecosystem

*(target ~1,100 words; Fig. 1, Table 1)*

We group the technologies that make up the neuroscience data standards ecosystem into six layers (Fig.
1, Table 1). Each layer is defined by the **problem it solves** and a typical **use case**, rather than
by a particular technology. We describe them in order, from the user toward the bytes on disk.

**Data archives** solve the problem of publishing, sharing, and discovering content. A typical use is
to publish a series of datasets on a topic. Neuroscience archives such as DANDI, OpenNeuro, EMBER,
NEMAR, BossDB, the Brain Image Library, and the NIMH Data Archive usually require data to follow
specific standards and to include rich metadata, which they then expose for search [REF: Subash 2023;
archive papers].

**Dataset organization standards** solve the problem of organizing a collection of files from a whole
experiment. They define folder hierarchies, file-naming conventions, which file organization standards
and formats are allowed, and additional dataset-level metadata, often in sidecar JSON and TSV files.
BIDS is the most widely used example in neuroscience; Psych-DS adapts the approach to psychological
data; and several archives define simplified, BIDS-inspired layouts such as the DANDI layout, the SPARC
Dataset Structure, and NeuroBlueprint.

**File organization standards** solve the problem of organizing data and metadata *within* a file, using
the primitives a data format offers, such as arrays, tables, and dictionaries, and the links between
them. Where dataset organization standards arrange files in folders, file organization standards define
what goes inside each file. A typical use is to store all data from one recording session or modality.
We use "file" in the broad sense of a self-contained data object, because some of these standards can be
stored either as a single file or as a directory, as NWB and OME do with Zarr; that choice is made at
the data format layer. NWB (neurophysiology and behavior), OME-TIFF and OME-Zarr (bioimaging), NIX,
odML, openMINDS, DICOM, and EDF are examples.

**Ontologies and terminologies** solve the problem of defining what terms mean. Terminologies define the
set of valid terms for a field, for example species names from the NCBI Taxonomy or brain regions from
an atlas. Ontologies additionally encode definitions and the relationships between concepts, so that
software can reason about them (e.g., that the hippocampus is part of the forebrain in Uberon).
Terminologies are often selected from ontologies. Annotation frameworks such as the Hierarchical Event
Descriptors (HED) also belong here, because they define a vocabulary and grammar for annotating events.
We keep ontologies and terminologies in one layer because, from a user's perspective, both are used the
same way, namely to give metadata values a shared meaning, while making the distinction explicit
[TODO-C4].

**Data formats** solve the problem of mapping data to storage. They define how generic data structures
such as arrays, tables, key–value pairs, images, and video are encoded in bytes. HDF5, Zarr, TIFF,
NIfTI, JSON, YAML, CSV/TSV, and MP4 are examples. Formats are usually domain-agnostic and shared across
all of science.

**Schema languages** solve the problem of describing the structure and rules of data formally, so
that standards can be documented, validated, and processed by software. JSON Schema, XML Schema,
RDF/OWL, LinkML, and the HDMF specification language are examples. NWB is defined in the HDMF language,
Psych-DS in LinkML, and BIDS in a custom YAML-based schema.

## An analogy

The layers have familiar counterparts in online video (Fig. 1b). A video platform such as YouTube is the
*archive*; playlists and channels are the *dataset organization*; the MP4 container that packages video,
audio, and subtitles is the *file organization standard*; hashtags and categories are the *terminology*;
the H.264 or AV1 encoding of the pixels is the *data format*; and the upload form that specifies which
fields a video needs is the *schema*. Nobody expects YouTube to define a video codec, or H.264 to decide
which playlist a video belongs in. Yet in neuroscience the equivalent roles are often discussed as if
they were one thing.

## Boundaries are fuzzy, and that is useful

No categorization is perfect, and many technologies span layers. DICOM defines both how medical imaging
data and metadata are organized (a file organization standard) and its own binary encoding (a data
format). BIDS is primarily a dataset organization standard, but it also specifies the contents of many
sidecar files. NWB and OME build on existing formats (HDF5, Zarr, TIFF) rather than defining their own,
while the NWB ecosystem also provides a dataset-level layout through DANDI.

The point of the map is not to put each technology in exactly one box. It is to make clear which
*problem* a given part of a technology addresses. Distinguishing "how bytes are written to disk" (DICOM
as a format) from "which metadata fields are required" (DICOM as a file organization standard) makes it
easier to discuss each aspect, to compare it with alternatives, and to reuse it. The map also makes
boundary crossings visible. When a file organization standard starts to define its own folder layout, or
a dataset organization standard starts to define the internal structure of binary files, the developers
are crossing a layer boundary. That is sometimes the right choice, but it should be a deliberate one,
weighed against building a bridge to an existing technology in the other layer.

## Stakeholders shape standards

Standards also differ in who drives them. NWB and BIDS grew out of research communities and are largely
publicly funded; DICOM is driven by industry and clinical vendors; others are tied to a specific archive
or consortium (Supplementary Table S1) [TODO-C5]. Whatever their origin, standards that succeed
eventually have to serve stakeholders across the whole data lifecycle. Research-driven standards need
support from acquisition-system vendors, and vendor-driven standards need to meet researchers' needs for
analysis and sharing. Being explicit about which problem a standard solves and for whom gives it scope
and helps set its future direction.