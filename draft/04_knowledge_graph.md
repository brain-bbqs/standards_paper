# 4. Mapping the connections in the ecosystem

*(~600 words; Fig. 3, Supplementary Fig. S1)*

The map describes the layers of the ecosystem, but FAIR data depend on how technologies in different
layers connect. To see where these connections exist, we compiled a knowledge graph of the ecosystem
(Fig. 3; Methods). Its nodes are 72 technologies taken from the map, from the BBQS guideline, and from
the standards that BBQS projects report. Each node is assigned to a layer and to the research community
in which it originated, such as neurophysiology, neuroimaging, microscopy, behavior, or psychology, or
to shared, domain-agnostic infrastructure such as HDF5, JSON, and cross-species ontologies. Its edges
are 122 typed relationships, for example that NWB *uses the format* HDF5, that BIDS *organizes* EEG data
in EDF, or that DANDI *accepts* NWB. They come from expert curation, documented with their source, and
from the RRID and FAIRsharing registries [REF: Bandrowski 2016; Sansone 2019]. Together, these
relationships connect 110 pairs of technologies, which we call connections. A pair can be linked by
several relationships, as BIDS and NWB are, but counts as one connection. Each connection is classified
by whether it links different layers and whether it links different communities. Fig. 3 draws the graph
with layers as rows and communities as columns, so that connections between layers run vertically and
connections between communities run across the columns.

Three patterns stand out [TODO-C25].

**Connections between layers are the norm.** Four in five connections (88 of 110) link technologies in
different layers, for example a file organization standard and the format it uses, or an archive and the
standards it accepts. Within each community, the vertical stack from archive to bytes is well connected,
which is what allows datasets in that community to reach the higher levels of FAIRness in Table 2.

**Shared infrastructure ties the ecosystem together.** Almost half of all connections (52 of 110) link a
domain-specific technology to shared infrastructure, such as a data format, a schema language, or a
cross-species ontology like the NCBI Taxonomy. These shared layers are where the communities already
meet, and they are the natural foundation for further integration.

**Bridges between communities are concentrated in a few hubs.** Of the 58 connections between
domain-specific technologies, 26 link technologies from different communities. Twenty-three of these 26
involve one of only four technologies, namely BIDS, NWB, HED, and the EMBER archive, and BIDS alone
takes part in 14. BIDS, which began in neuroimaging, now organizes EEG, MEG, iEEG, microscopy, motion,
and NWB data. HED, which began in EEG, is used by BIDS, NWB, and several archives. EMBER accepts NWB,
BIDS, Psych-DS, and the DANDI layout. Most other technologies connect only within their own community or
to shared infrastructure.

These patterns suggest that integration across communities currently depends on a small number of
technologies that have grown beyond their original community, rather than on bridges designed
systematically between communities. This makes the hubs critical for programs that span communities,
such as BBQS, and it means that much of the integration work is still left to users and consortia
(Section 8).

The graph also shows how much of this knowledge is recorded in public registries. Many of the
relationships we curated from the documentation of each technology are not yet recorded in RRID or
FAIRsharing [TODO-C26], so software that relies on these registries cannot discover them. Recording
these relationships in the registries would make the connections between technologies machine-findable,
in the same way that the registries already make the technologies themselves findable.

The graph is a first version and has limitations. Its coverage reflects the technologies most relevant
to this paper rather than the whole of neuroscience. Curated relationships are still being confirmed by
domain experts, and registry coverage is incomplete. Whether a connection crosses communities also
depends on how each technology's community is assigned. We classify by the community in which a
technology originated. A more lenient classification, which treats any shared community as within
community, hides most bridges because technologies are often tagged with the communities they have
reached through exactly these bridges (Supplementary Fig. S1) [TODO-C35]. The graph, the code, and the
gap report are released so that the community can extend and correct it (Data Availability).