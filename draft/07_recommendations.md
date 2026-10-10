# 7. Recommendations for multimodal brain–behavior data

*(target ~1,200 words; Table 3)*

We developed the below recommendations as part of the BBQS Data Standards Working Group
as part of the BBQS data standards guideline [REF: BBQS guideline]. Although they
were developed for BBQS, they apply much more broadly to any study that combines neural 
and behavioral data, so we state them in general terms. We then describe afterwards
how BBQS implements these recommendation at the end of this section. They are
community guidance, not a ranking of standards, and the guideline is updated as standards evolve.
Table 3 gives an overview by data type.

**Table 3. Recommended standards for common BBQS data types** (✓ supported; ext. = via an extension or
proposal in progress; — no established representation yet). *Draft; to be checked by the NWB, BIDS, and
Psych-DS teams* [TODO-C17].

| Data type | NWB | BIDS | Psych-DS | Notes |
|---|---|---|---|---|
| Extracellular ephys (spikes, LFP) | ✓ (recommended) | ext. (BEP032) | — | |
| Intracellular ephys (patch clamp) | ✓ (recommended) | — | — | |
| Calcium / optical physiology | ✓ (recommended) | — | — | |
| EEG / MEG / iEEG, standalone | ✓ (combined studies) | ✓ (recommended) | — | EDF as interchange format |
| MRI / fMRI / PET | — | ✓ (recommended) | — | |
| Optogenetic / electrical stimulation | ✓ (recommended) | — | — | |
| Raw behavioral video | ✓ (linked MP4 etc.) | ext. (proposals in progress) | ✓ (raw folder) | |
| Pose / motion tracking | ✓ (ndx-pose) | ✓ (Motion-BIDS) | tabular only | |
| Eye tracking | ✓ | ext. (BEP020) | tabular only | |
| Wearable sensors | ✓ (TimeSeries) | ✓ (physio recordings) | ✓ (CSV) | |
| Audio / vocalizations | ✓ (TimeSeries + intervals) | — | — | |
| Structured tasks / events | ✓ (core events since NWB 2.10; ndx-structured-behavior) | ✓ (task events) | — | HED in both |
| Questionnaires / surveys | — | partial | ✓ (recommended) | |
| Social interactions, feeding, facial expressions, home-cage monitoring, VR, force plates, EMG | — | — / ext. | — | **Gaps** (Section 8) |

## Choosing standards

**R1. Choose by the structure of the experiment, not only by modality.** If behavior must be aligned
precisely with neural recordings from the same session, store both in **NWB**, which keeps all streams
on one timeline in one file. If the study is organized around many subjects and sessions with imaging or
EEG, use **BIDS** as the dataset organization and include other data (including NWB files) within it
where supported. If behavioral data are mainly tables, such as questionnaires, task responses, or
ratings, use **Psych-DS**. The guideline gives detailed choices by recording technology and by behavior
type [REF: BBQS guideline].

**R2. Expect to combine standards, and link them explicitly.** Multimodal studies will often need
more than one standard, for example BIDS for MRI and NWB for electrophysiology in the same
participants. Use the same subject and session identifiers throughout, and record how datasets relate.
Emerging integrations such as BEP032 (NWB within BIDS) make this easier and should be used where they
apply [TODO-C15].

**R3. Keep raw video in standard formats and link it.** Store video in widely supported containers
(e.g., MP4) rather than embedding it in other files, and reference it from the file organization
standard (an `ImageSeries` in NWB) with timestamps that tie frames to the experiment clock. Store
derived pose estimates in a standard representation (ndx-pose in NWB, or Motion-BIDS), not as bare
arrays, so the link between keypoints, video, and the pose model is preserved [TODO-C18].

**R4. Make synchronization explicit.** Record which clock each device used, how clocks were aligned,
and with what precision. NWB stores all data on a common session timeline; in BIDS and Psych-DS,
timing columns and sidecar metadata should state the reference clock. Synchronization cannot be
reconstructed after the fact if it is not documented [TODO-C19].

## Describing data

**R5. Annotate events with HED.** Use the Hierarchical Event Descriptors to annotate stimuli,
behaviors, and experimental events in both BIDS and NWB. Because HED works across standards, it is
the most direct way to make behavioral annotations comparable between projects [REF: Robbins 2022].

**R6. Use shared terminologies for common metadata.** Use NCBI Taxonomy terms for species, a standard
atlas for anatomical locations, and the Cell Ontology for cell types. For behavior, ontologies such as
the Neuro Behavior Ontology exist but are not yet widely used [TODO-C20]; projects should at
least define their behavior labels in machine-readable form so they can be mapped later.

**R7. Describe every custom field.** All three standards allow custom metadata, for example additional
table columns in NWB, custom JSON fields and TSV columns in BIDS, and user-defined variables in
Psych-DS. Each custom field should have a clear name, a definition, units, type, and allowed values (a
*data field descriptor*), so that it can be interpreted without the original lab.

## When the standard does not fit

**R8. Extend before you invent.** If data mostly fit a standard but need a few more fields, use the
standard's built-in mechanisms, such as custom columns or generic `TimeSeries` in NWB, custom sidecar
fields or "unspecified data" files following BIDS naming in BIDS, and documented variables in Psych-DS.
If a new data type is needed, check the NWB Extension Catalog and the list of BIDS Extension Proposals
before creating a new one, and develop extensions in the open, as Neurodata Extensions (NDX) and NWB
Enhancement Proposals for NWB, as BIDS Extension Proposals for BIDS [REF: BBQS guideline; NWB
extensions; BIDS BEP process]. Contact the standards' help desks, and the data coordination center of
the program if there is one, early; others may already be working on the same data type.

## Validating and sharing

**R9. Validate before you deposit.** Use the NWB Inspector, the BIDS Validator, and the Psych-DS
validator during the project, not only at the end. Validation catches problems while the people who
can fix them still remember the details.

**R10. Plan for scale and continuity.** For very large recordings, separate raw and processed data into
different files that share metadata. For continuous, multi-day recordings, decide early how to split
data into manageable pieces while keeping annotations that span them [TODO-C21].

**R11. Deposit in an archive that accepts the standards, and standardize early.** Choose an archive
that accepts the chosen standards and the privacy requirements of the data, for example DANDI for NWB,
or OpenNeuro, NEMAR, or DABI for BIDS [TODO-C36]. Converting data at the end of a project is costly and
error-prone. Projects that adopt standards during acquisition and analysis also benefit from the
standards' analysis tools, and can share data with collaborators through the archive rather than
through general cloud storage [TODO-C22].

## Implementation in BBQS

In BBQS, several of these recommendations are made concrete by the program's infrastructure. All BBQS
data are deposited in EMBER, which accepts NWB, BIDS, Psych-DS, and DANDI-layout datasets and supports
the privacy levels needed for identifiable human data (Section 6), so archive choice (R11) is settled
for BBQS projects. The BBQS Data Coordination and AI Center (DCAIC) is the first point of contact for
questions about standards and extensions (R8) and connects projects with standards developers.
Synchronization (R4) is central to the program's scientific goals and is the "S" in its name.

The process behind the guideline can also be adopted by other programs. A working group of project
representatives and standards developers places the program's data types on the map, chooses a small
set of interoperable standards for each layer, records where no standard yet exists, and maintains the
guideline as a living document.
