# 1. Introduction: a complex ecosystem

*(target ~600 words)*

Neuroscience is producing data faster than it can turn them into knowledge. Large-scale
electrophysiology, whole-brain imaging, and continuous video of freely behaving animals now generate
terabytes per experiment [TODO-C1], and public archives for neuroscience data hold petabytes
[TODO-C2]. Whether these data can be found, understood, combined, and reused depends less on how much
is stored than on how it is described and organized. Data standards are the community's main tool for
this, and they have clear success stories: the Brain Imaging Data Structure (BIDS) reorganized how
neuroimaging data are shared [REF: Gorgolewski 2016; Poldrack 2024], Neurodata Without Borders (NWB)
did the same for neurophysiology [REF: Teeters 2015; Rübel 2022], DICOM made clinical imaging
interoperable across vendors [REF: Bidgood 1997], and OME did so for bioimaging [REF: Linkert 2010;
Moore 2021].

These successes have produced a rich but complex ecosystem. Making a dataset shareable typically
involves several kinds of technology at once: an archive with its submission requirements, a convention
for organizing files and folders, a schema for the contents of each file, vocabularies for metadata
values, file formats, and formal languages in which schemas are written. Each solves a different
problem and is often developed by a different community, and in everyday use they are all referred to
as "data standards". As a result, it is often unclear what a data standard is and what it is expected
to do — for a researcher asked to "use a standard" as much as for a developer deciding what a standard
should cover. In practice the technologies are combined: an NWB file uses the HDF5 format, its schema is written in
the HDMF schema language, its subject species is a term from the NCBI Taxonomy, and it is shared on the
DANDI archive inside a BIDS-inspired folder layout. Without a shared picture of how these pieces fit
together, users struggle to tell what they actually need, and developers struggle to tell when a feature
belongs in their own technology and when it is better solved by connecting to another.

The stakes are rising. Programs such as the NIH BRAIN Initiative's Brain Behavior Quantification and
Synchronization (BBQS) program aim to relate neural activity to naturalistic, multimodal behavior
measured with video, pose estimation, audio, wearable sensors, and other devices, often in species and
settings that existing standards were not designed for [REF: BBQS program; Datta 2019; Pereira 2020].
Such projects cannot rely on a single standard: they must combine several, across communities that
developed their tools largely independently. At the same time, machine learning and AI-assisted
analysis increase the value of data that are consistently structured and annotated, and the cost of
data that are not [TODO-C3].

This paper has two goals. First, we propose a **map of the data standards ecosystem** (Fig. 1,
Table 1) that separates six layers by the problem each solves, and we use it to explain why FAIR data
[REF: Wilkinson 2016] require integration across layers (Section 3). The map is meant to give
technologists and practitioners a shared vocabulary, and to make visible when a project crosses a
boundary — the point at which building a bridge to an existing solution may be better than expanding
scope. Second, we apply the map to **BBQS** (Sections 4–7): we characterize the data BBQS projects
collect, describe the standards stack BBQS has adopted, give recommendations by data type based on the
BBQS data standards guideline developed by the program's Data Standards Working Group [REF: BBQS
guideline], and identify where standards support is still missing. We end with the bridges and
investments needed for multimodal brain–behavior science (Section 8).

This is not a review of every standard. The map and examples focus on technologies used in
neuroscience and, in the second part, on those relevant to BBQS; comprehensive and continuously
updated registries of standards already exist [REF: FAIRsharing, Sansone 2019; RRID, Bandrowski
2016], and we point to them rather than duplicate them.
