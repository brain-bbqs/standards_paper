# 1. Introduction

*(target ~600 words)*

Neuroscience is producing data faster than it can turn them into knowledge. Large-scale
electrophysiology, whole-brain imaging, and continuous video of freely behaving animals now generate
terabytes per experiment [TODO-C1]. The BRAIN Initiative's data archives alone now hold several
petabytes. As of October 2026, DANDI holds about 2.4 PB of neurophysiology data in nearly 1,200 datasets
[REF: DANDI stats], BossDB about 1 PB of volumetric electron microscopy and X-ray data [REF: Hider 2022;
BossDB], the Neuroscience Multi-Omic Archive (NeMO) more than 1 PB of omics data [REF: Ament 2023], and
the Brain Image Library (BIL) is a petascale microscopy resource [REF: Kenney 2024] [TODO-C2]. Whether
these data can be found, understood, combined, and reused depends less on how much is stored than on how
it is described and organized. Data standards are the community's main tool for this, and they have
clear success stories. The Brain Imaging Data Structure (BIDS) reorganized how neuroimaging data are
shared [REF: Gorgolewski 2016; Poldrack 2024], Neurodata Without Borders (NWB) did the same for
neurophysiology [REF: Teeters 2015; Rübel 2022], DICOM made clinical imaging interoperable across
vendors [REF: Bidgood 1997], and OME did so for bioimaging [REF: Linkert 2010; Moore 2021].

These successes have produced a rich but complex ecosystem. Making a dataset shareable typically
involves several kinds of technology at once, such as an archive with its submission requirements, a
convention for organizing files and folders, a schema for the contents of each file, vocabularies for
metadata values, file formats, and formal languages in which schemas are written. Each solves a
different problem and is often developed by a different community, and in everyday use they are all
referred to as "data standards". As a result, it is often unclear what a data standard is and what it is
expected to do, both for a researcher asked to "use a standard" and for a developer deciding what a
standard should cover. In practice, these technologies are used together. An NWB file uses the HDF5
format, its schema is written in the HDMF schema language, its subject species is a term from the NCBI
Taxonomy, and it is shared on the DANDI archive inside a BIDS-inspired folder layout. Without a shared
picture of how these pieces fit together, users struggle to tell what they actually need, and developers
struggle to tell when a feature belongs in their own technology and when it is better solved by
connecting to another.

The stakes are rising. Programs such as the NIH BRAIN Initiative's Brain Behavior Quantification and
Synchronization (BBQS) program aim to relate neural activity to naturalistic, multimodal behavior
measured with video, pose estimation, audio, wearable sensors, and other devices, often in species and
settings that existing standards were not designed for [REF: BBQS program; Datta 2019; Pereira 2020].
Such projects cannot rely on a single standard. They must combine several, from communities that
developed their tools largely independently. At the same time, machine learning and AI-assisted analysis
make consistent structure and annotation more important. These methods can combine data from many
datasets and laboratories, but only when software can interpret how each dataset is organized and what
it contains. Data without that structure are difficult to include, however valuable they are [TODO-C3].

Here we address these challenges in two parts. In the first part, we develop a **map of the data
standards ecosystem** (Fig. 1, Table 1) that distinguishes six layers by the problem each layer solves,
from public archives to the schema languages in which standards are defined. Community registries
such as FAIRsharing [REF: Sansone 2019] and the Research Resource Identifier (RRID) registry
[REF: Bandrowski 2016] catalog many research standards and resources, and we use them as the basis for
the map, focusing on the technologies used in neuroscience. The map provides a common vocabulary for
developers and users of standards, and it identifies where a technology reaches beyond its layer, the
point at which integrating an existing solution is often preferable to extending its scope. Using this
map, we show that FAIR data [REF: Wilkinson 2016] are achieved not by a single technology but by
integration across layers (Section 3). We then combine the relationships recorded in these registries
with expert curation in a knowledge graph of the ecosystem, which quantifies how technologies are
connected across layers and across research communities (Section 4).

In the second part, we apply this framework to **BBQS** (Sections 5–8). From an inventory of BBQS
projects, we characterize the data modalities, species, and standards in use, and we describe the
standards stack adopted by the program. Building on the BBQS data standards guideline that we developed
in the program's Data Standards Working Group [REF: BBQS guideline], we derive recommendations by data
type and identify where standards support is still missing. We conclude with the bridges and investments
needed to make multimodal brain–behavior data FAIR (Section 9).
