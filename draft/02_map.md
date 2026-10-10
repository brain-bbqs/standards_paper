# 2. A map of the data standards ecosystem

*(~1,450 words; Fig. 1, Table 1)*

We group the technologies that make up the neuroscience data standards ecosystem into six layers (Fig.
1, Table 1). Each layer is defined by the **problem it solves** and a typical **use case**, rather than
by a particular technology. To make the layers intuitive, we pair each one with its counterpart in a
system almost every reader uses, which is sharing video online (Fig. 1b). Think of a video recorded on a
phone and published on a platform such as YouTube. The pixels are compressed with a codec, the video and
sound are packaged together in a single file, the file is added to a playlist, tagged so that others can
find it, and uploaded through a form that asks for a title and a category. Each of these steps is handled
by a different, independently developed technology, and the same is true for neuroscience data. We
describe the layers in order, from the user toward the bytes on disk.

**Data archives** solve the problem of publishing, sharing, and discovering content. In the video world,
this is the platform itself. YouTube stores videos, makes them searchable, and accepts only certain file
types with certain information attached. Neuroscience archives such as DANDI, OpenNeuro, EMBER, NEMAR,
BossDB, the Brain Image Library, and the NIMH Data Archive play the same role. They usually require data
to follow specific standards and to include rich metadata, which they then expose for search [REF:
Subash 2023; archive papers]. A typical use is to publish a series of datasets on a topic.

**Dataset organization standards** solve the problem of organizing a collection of files from a whole
experiment. Their video counterpart is the playlist or the series, which groups many videos and puts them
in order, often with names such as "season 1, episode 2" that tell the viewer where each one belongs.
BIDS works the same way. It defines folder hierarchies and file names such as `sub-01_ses-02_task-rest`
that encode the subject, session, and task, and it specifies which file organization standards and
formats are allowed and which dataset-level metadata must accompany them, often in sidecar JSON and TSV
files. BIDS is the most widely used example in neuroscience. Psych-DS adapts the approach to
psychological data, and several archives define simplified, BIDS-inspired layouts such as the DANDI
layout, the SPARC Dataset Structure, and NeuroBlueprint.

**File organization standards** solve the problem of organizing data and metadata *within* a file, using
the primitives a data format offers, such as arrays, tables, and dictionaries, and the links between
them. Their video counterpart is the container, such as MP4. An MP4 file holds the video track, one or
more audio tracks, subtitles, and chapter markers, and it keeps all of them on a shared timeline so that
sound and subtitles stay in sync with the picture. NWB does the same for an experiment. One NWB file
holds the neural recordings, the behavioral measurements, the stimuli, the trials and events, and the
metadata of one session, all aligned in time. Where dataset organization standards arrange files in
folders, file organization standards define what goes inside each file. OME-TIFF and OME-Zarr
(bioimaging), NIX, odML, openMINDS, DICOM, and EDF are further examples. We use "file" in the broad sense
of a self-contained data object, because some of these standards can be stored either as a single file
or as a directory, as NWB and OME do with Zarr. As with video, where the same MP4 container can hold
video compressed with different codecs, that choice is made at the data format layer.

**Ontologies and terminologies** solve the problem of defining what terms mean. On a video platform,
this is the difference between free-form hashtags, which anyone can invent, and the platform's fixed list
of categories, which everyone must choose from and which may be arranged in a hierarchy in which
"tennis" is a kind of "sport". Terminologies correspond to the fixed list. They define the set of valid
terms for a field, for example species names from the NCBI Taxonomy or brain regions from an atlas.
Ontologies correspond to the hierarchy. They additionally encode definitions and the relationships
between concepts, so that software can reason about them, for example that the hippocampus is part of
the forebrain in Uberon. Terminologies are often selected from ontologies. Annotation frameworks such as
the Hierarchical Event Descriptors (HED) also belong here, because they define a vocabulary and grammar
for annotating events, much like a structured way of describing what happens in each scene. We keep
ontologies and terminologies in one layer because, from a user's perspective, both are used to give
metadata values a shared meaning, while making the distinction explicit [TODO-C4].

**Data formats** solve the problem of mapping data to storage. In video, this is the codec, such as H.264
or AV1, which defines how the pixels are encoded as bytes. Viewers rarely notice it, and the same codec is
used by every platform. Data formats such as HDF5, Zarr, TIFF, NIfTI, JSON, YAML, CSV/TSV, and MP4
likewise define how generic data structures such as arrays, tables, key–value pairs, images, and video
are encoded in bytes. They are usually domain-agnostic and shared across all of science.

**Schema languages** solve the problem of describing the structure and rules of data formally. Behind a
platform's upload form is a precise specification of which fields exist, which are required, and which
values each may take, written in a form that software can check. Schema languages such as JSON Schema,
XML Schema, RDF/OWL, LinkML, and the HDMF specification language play this role for neuroscience. They
allow standards to be documented, validated, and processed by software. NWB is defined in the HDMF
language, Psych-DS in LinkML, and BIDS in a custom YAML-based schema.

The analogy also explains why the distinctions matter. Nobody expects YouTube to invent a video codec,
or H.264 to decide which playlist a video belongs in, and because each layer does one job well, a video
recorded on any phone can be played on any platform. In neuroscience, the equivalent roles are often
discussed as if they were one thing, and the next sections show what is gained by keeping them apart.

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
