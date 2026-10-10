# 2. A map of the data standards ecosystem

*(~1,450 words; Fig. 1, Table 1)*

We group the technologies that make up the neuroscience data standards ecosystem into six layers (Table
1). Each layer is defined by the **problem it solves** and a typical **use case**, rather than
by a particular technology. To illustrate the layers, we use online video sharing as an analogy
(Fig. 1). Publishing a video on a platform such as YouTube also involves several independently developed
technologies. A codec compresses the images, a container file packages video and sound together, a
playlist organizes related videos, categories and tags describe the content, and the upload form
specifies which information must accompany each video. Sharing neuroscience data relies on an analogous
combination of technologies.

**Data archives** solve the problem of publishing, sharing, and discovering data. Neuroscience archives
such as DANDI, OpenNeuro, EMBER, NEMAR, BossDB, the Brain Image Library, and the NIMH Data Archive store
datasets and usually require them to follow specific standards and to include rich metadata, which they
then expose for search [REF: Subash 2023; archive papers]. A typical use is to publish a series of
datasets on a topic. The video platform (e.g., YouTube) plays the analogous role, storing videos, indexing 
them for search, and accepting only certain file types with certain accompanying information.

**Dataset organization standards** solve the problem of organizing collections of files from whole
experiments. They define folder hierarchies and file names that encode the experimental design, specify
which file organization standards and formats are allowed, and define the dataset-level metadata that
must accompany the files, often in sidecar JSON and TSV files. BIDS is the most widely used example in
neuroscience. Its file names, such as `sub-01_ses-02_task-rest`, encode the subject, session, and task.
Psych-DS adapts the approach to psychological data, and several archives define simplified,
BIDS-inspired layouts such as the DANDI layout, the SPARC Dataset Structure, and NeuroBlueprint. A typical
use is to organize the data from a full experiment. The video counterpart is a playlist or series, which
groups related videos and names them, for example "season 1, episode 2", so that viewers know where each
one belongs.

**File organization standards** solve the problem of organizing data and metadata *within* a file, using
the primitives a data format offers, such as arrays, tables, and dictionaries, and the links between
them. Where dataset organization standards arrange files in folders, file organization standards define
what goes inside each file. An NWB file, for example, holds the neural recordings, behavioral
measurements, stimuli, trials and events, and metadata of one session, all aligned on a common timeline.
OME-TIFF and OME-Zarr (bioimaging), NIX, odML, openMINDS, DICOM, and EDF are further examples. A typical
use is to organize the data from one session or modality. We use "file" in the broad sense of a
self-contained data object, because some of these standards can be stored either as a single file or as a
directory. NWB, for example, can be stored as a single HDF5 file or as a Zarr directory, and the choice
between the two is made at the data format layer, not by the file organization standard. The video
counterpart is a container such as MP4, which holds video, audio, subtitle, and chapter tracks on a
shared timeline so that they stay in sync, regardless of the codec used to compress the video.

**Ontologies and terminologies** solve the problem of defining what terms mean. Terminologies define the
set of valid terms for a metadata field, for example species names from the NCBI Taxonomy or brain
regions from an atlas. Ontologies additionally encode definitions and the relationships between
concepts, so that software can reason about them, for example that the hippocampus is part of the
forebrain in Uberon. Terminologies are often selected from ontologies. Annotation frameworks such as the
Hierarchical Event Descriptors (HED) also belong here, because they define a vocabulary and grammar for
annotating events. Although ontologies and terminologies are distinct concepts, we group them in one
layer because both serve the same purpose in data sharing, which is to give metadata values a shared,
well-defined meaning [TODO-C4]. A typical use is to annotate data so that the meaning of each term is 
defined. Continuing with our analogy, on a video-sharing platform, a fixed list of categories corresponds 
to a terminology and a hierarchy of categories, in which "tennis" is a kind of "sport", corresponds to
an ontology, in contrast to free-form hashtags that anyone can invent.

**Data formats** solve the problem of mapping data to storage. Formats such as HDF5, Zarr, TIFF, NIfTI,
JSON, YAML, CSV/TSV, and MP4 define how generic data structures such as arrays, tables, key–value pairs,
images, and video are encoded as bytes. They are usually domain-agnostic and used across all of
science. A typical use is to serialize generic data structures. The video counterpart is the codec, such
as H.264 or AV1, which defines how pixels are encoded as bytes and is supported across platforms.

**Schema languages** solve the problem of describing the structure and rules of data formally. Languages
such as JSON Schema, XML Schema, RDF/OWL, LinkML, and the HDMF specification language specify which
elements exist, which are required, and which values each may take, in a form that software can check.
They allow standards to be documented, validated, and processed by software. NWB is defined in the HDMF
language, Psych-DS in LinkML, and BIDS in a custom YAML-based schema. A typical use is to formally define
file organization standards, dataset organization standards, and ontologies. The video counterpart is
the specification behind a platform's upload form, which determines which fields exist, which are
required, and which values each may take.

The analogy also shows why these distinctions matter. The video ecosystem works because of a clear
separation of concerns. Nobody expects YouTube to invent a video codec, or H.264 to decide which
playlist a video belongs in. Each layer does one job well and integrates with the layers around it
through shared conventions, which is why a video recorded on any phone can be played on any platform. In
neuroscience, many technologies were developed independently within individual subdomains, such as
neurophysiology, neuroimaging, and microscopy, to meet the immediate needs of each community. As a
result, a single technology often takes on the roles of several layers, and similar problems are solved
separately in different communities. We argue that separating concerns across layers, combined with
deliberate integration between them, is what makes data FAIR (Section 3) and what multimodal programs
such as BBQS need (Sections 5–8). Section 4 first examines how well technologies are connected across
layers and communities today.

## Boundaries are fuzzy, and that is useful

No categorization is perfect, and many technologies span layers. DICOM defines both how medical imaging
data and metadata are organized (a file organization standard) and its own binary encoding (a data
format), much as an animated GIF is both a container and an encoding. BIDS is primarily a dataset
organization standard, but it also specifies the contents of many sidecar files. NWB and OME build on
existing formats (HDF5, Zarr, TIFF) rather than defining their own, while the NWB ecosystem also
provides a dataset-level layout through DANDI. The layer a technology belongs to can also depend on the
point of view. In the analogy, MP4 is the container, but for a neuroscientist a behavioral video stored
as MP4 is simply data in a generic media format, which a file organization standard such as NWB
references and places on the experiment's timeline.

The point of the map is not to put each technology in exactly one box. It is to make clear which
*problem* a given part of a technology addresses. Distinguishing "how bytes are written to disk" (DICOM
as a format) from "which metadata fields are required" (DICOM as a file organization standard) makes it
easier to discuss each aspect, to compare it with alternatives, and to reuse it. The map also makes
boundary crossings visible. When a file organization standard starts to define its own folder layout, or
a dataset organization standard starts to define the internal structure of binary files, the developers
are crossing a layer boundary. That is sometimes the right choice, but it should be a deliberate one,
weighed against building a bridge to an existing technology in the other layer, in the same way that a
video platform adopts existing codecs rather than designing its own.

## Stakeholders shape standards

Standards also differ in who drives them. NWB and BIDS grew out of research communities and are largely
publicly funded; DICOM is driven by industry and clinical vendors; others are tied to a specific archive
or consortium (Supplementary Table S1) [TODO-C5]. Whatever their origin, standards that succeed
eventually have to serve stakeholders across the whole data lifecycle. Video codecs succeeded because
camera makers, software developers, and platforms all adopted them, and neuroscience standards face the
same test. Research-driven standards need support from acquisition-system vendors, and vendor-driven
standards need to meet researchers' needs for analysis and sharing. Being explicit about which problem a
standard solves and for whom gives it scope and helps set its future direction.
