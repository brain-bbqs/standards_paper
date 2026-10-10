# 8. Gaps and the bridges BBQS needs

*(target ~800 words; Fig. 4c, Fig. 6)*

## Behaviors without a home

The BBQS guideline lists, for each common recording technology and behavior type, how to store it in
NWB, BIDS, and Psych-DS. Where no established representation exists, the guideline says so explicitly.
Comparing these entries with the behaviors BBQS projects actually record
(Section 5) shows a clear mismatch (Fig. 4c) [TODO-C23].

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
inherently multi-animal, multi-modal, and defined by annotation. This reflects a general pattern.
Standardization usually begins with raw signals, whose structure is largely determined by the
acquisition hardware, and slows as data become more derived, because there is often no agreed way to
perform a given analysis and many tools exist for each step. Behavioral constructs such as a social
interaction are the result of such analyses, from pose estimation to classification and manual
annotation. Extending standards toward derived data therefore requires more than common data
structures. It also requires agreement on analysis protocols, and tools that produce and consume
standardized results.

Representing behavioral constructs needs three things that cut across the map. The first is a data
structure for annotated behavior over time, with intervals and events that carry labels, confidence, and
provenance and may involve several individuals. The second is a shared vocabulary for behavior labels,
and the third is a set of conventions for linking these annotations to the underlying video, pose, and
neural data.

Several of these gaps are recognized and are being actively addressed. Standards communities are
extending their support for events and annotations, for links to external vocabularies, and for data
from several interacting subjects, through NWB Enhancement Proposals and extensions and through BIDS
Extension Proposals [REF: e.g., NWBEP001 and PyNWB 4.0 release; relevant BEPs] [TODO-C37]. Much remains
to be done, in particular a shared vocabulary for behavior labels and a representation of annotated
behavior that works across NWB, BIDS, and Psych-DS.

## Few bridges across communities

The knowledge graph in Section 4 showed that connections between layers are common, while bridges
between communities are concentrated in a few hubs, namely BIDS, NWB, HED, and EMBER (Fig. 3). Every
BBQS project combines data from several communities, so BBQS depends on these hubs and is exposed
wherever they do not reach, for example for behavioral annotations, pose, and audio.

Integration across modalities is therefore still done largely by users and large consortia, at
considerable cost to each project. For BBQS, where every project is multimodal, this cost is paid over
and over.

## Bridges at every layer

Bridges between technologies are being built at every layer of the map, and BBQS can both use and drive
them (Fig. 6).

1. **Structural bridges** connect file organization standards and dataset organization standards, for
   example NWB files inside BIDS datasets (BEP032) and BIDS-inspired layouts for NWB data (DANDI
   layout).
2. **Schema-language bridges** express schemas in a common language such as LinkML, so that equivalent
   concepts in different standards can be mapped and translated. Psych-DS is already defined in LinkML,
   efforts are under way to express the NWB schema in LinkML, and exploratory work has begun for BIDS
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
