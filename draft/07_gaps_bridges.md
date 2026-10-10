# 7. Gaps and the bridges BBQS needs

*(target ~900 words; Fig. 4c, Fig. 5; Supplementary Fig. S1 = knowledge graph)*

## Behaviors without a home

The BBQS guideline lists, for each common recording technology and behavior type, how to store it in
NWB, BIDS, and Psych-DS. Where no established representation exists, the guideline says so explicitly
("TODO — how to store?"). Comparing these entries with the behaviors BBQS projects actually record
(Section 4) shows a clear mismatch (Fig. 4c) [TODO-C23].

- **Social interactions** (15 of 22 awards), **feeding and drinking** (9), **posture and balance** (8),
  **emotional and stress responses** (8), **facial expressions** (4), **reproductive behaviors** (3),
  **physical activity levels** (3), and **operant conditioning** (3) currently have **no recommended
  representation in any of the three standards**.
- **Locomotion and movement** (16 awards) and **gait** (5) can be stored as positions or pose over time,
  but there is no agreed representation of the derived measures (bouts, speeds, stride parameters).
- Recording technologies including **EMG, force plates, virtual reality systems, automated home-cage
  monitoring, behavioral coding software, thermal imaging, and smartphone or smart-device data** lack
  guidance; for some, extensions are in development (e.g., BIDS BEP042 for surface EMG) [TODO-C24].

In short, the standards support the *raw signals* of behavior well, including video, positions, time
series, and events, but not yet the *behavioral constructs* that BBQS projects study, which are
inherently multi-animal, multi-modal, and defined by annotation. Representing them needs three things
that cut across the map. The first is a data structure for annotated behavior over time, with intervals
and events that carry labels, confidence, and provenance and may involve several individuals. The second
is a shared vocabulary for behavior labels, and the third is a set of conventions for linking these
annotations to the underlying video, pose, and neural data.

## Few bridges across communities

The map also helps locate where integration happens today. Relationships between technologies in
*different layers* within a community are common and well documented. NWB uses HDF5 and HDMF, BIDS uses
JSON and TSV, archives accept the standards of their community. Relationships *between communities* are
rarer. To make this visible, we compiled a knowledge graph of 72 technologies and 133 relationships from
expert curation and the RRID and FAIRsharing registries (Supplementary Fig. S1; Methods). Drawn with
communities as columns, most cross-community links run through a few hubs, which are BIDS (which now
organizes EEG, microscopy, motion, and NWB data), NWB, HED, and multi-modal archives such as EMBER and
DANDI [TODO-C25]. The registries record only a small fraction of these relationships [TODO-C26], so much
of this integration knowledge currently lives in documentation and in the heads of developers.

Integration across modalities is therefore still done largely by users and large consortia, at
considerable cost to each project. For BBQS, where every project is multimodal, this cost is paid over
and over.

## Bridges at every layer

Bridges are being built at every layer of the map, and BBQS can both use and drive them (Fig. 5).

1. **Structural bridges** connect file organization standards and dataset organization standards, for
   example NWB files inside BIDS datasets (BEP032) and BIDS-inspired layouts for NWB data (DANDI
   layout).
2. **Schema-language bridges** express schemas in a common language such as LinkML, which Psych-DS
   already uses, so that equivalent concepts in different standards can be mapped and translated
   [TODO-C27].
3. **Semantic bridges for schema elements** define what a field *means* by linking it to ontology terms,
   so that, for example, "subject species" in NWB, BIDS, and Psych-DS can be recognized as the same
   concept.
4. **Semantic bridges for values** provide shared terminologies for metadata values such as species,
   anatomy, and, most urgently for BBQS, behavior.
5. **Archive bridges** use linked data and cross-references between archives so that a subject's EEG on
   one archive and their video on another can be found together.
6. **Dataset-level bridges** use common data elements to define the minimal shared metadata across
   datasets, as already practiced in clinical research.

For BBQS, the highest-value bridges are (i) a cross-standard representation of annotated behavior,
built once and expressed in NWB, BIDS, and Psych-DS rather than three times independently; (ii) shared
behavior terminologies, building on HED and existing behavior ontologies; and (iii) conversion and
validation tools that move data between the standards without loss [TODO-C28].
