# 6. The BBQS standards stack

*(target ~700 words; Fig. 5)*

BBQS has converged on a small set of standards that together cover the layers of the map (Fig. 5).
They were selected by the BBQS Data Standards Working Group because they are open, community-governed,
supported by the BRAIN Initiative, accepted by the EMBER archive, and extensible [TODO-C13].

**EMBER (archive).** The Ecosystem for Multi-modal Brain-behavior Experimentation and Research (EMBER)
is the designated archive for BBQS data [REF: EMBER]. It accepts NWB, BIDS, Psych-DS, and DANDI-layout
datasets and supports several privacy levels, which matters because many BBQS projects record
identifiable human data such as faces and voices [TODO-C14]. Projects whose data also fit other
community archives, such as DANDI for neurophysiology or OpenNeuro and NEMAR for imaging and EEG, can
benefit from those archives' tools, but BBQS deposits go to EMBER.

**NWB (file organization standard for neurophysiology and synchronized behavior).** NWB stores the data
of one recording session in one file, including neural recordings (extracellular and intracellular
electrophysiology, optical physiology), stimuli, behavioral time series (positions, pose, eye tracking),
events, trials, and rich metadata about subjects, devices, and processing [REF: Rübel 2022]. Because
everything shares one timeline within the file, NWB is well suited to experiments in which behavior must
be precisely aligned with neural activity. Video is stored in standard formats such as MP4 and
referenced from the NWB file. NWB is defined in the HDMF schema language and stored in HDF5 or Zarr.

**BIDS (dataset organization for imaging, EEG, and multi-subject studies).** BIDS organizes the files of
a whole study into a predictable folder hierarchy with key metadata encoded in file names and JSON and
TSV sidecars [REF: Gorgolewski 2016]. Beyond MRI it covers EEG, MEG, iEEG, PET, microscopy, and motion
capture, as well as behavioral experiments and task events [REF: EEG-BIDS, MEG-BIDS, iEEG-BIDS,
Microscopy-BIDS, Motion-BIDS]. BIDS can include NWB files for some modalities, and a BIDS extension for
microelectrode electrophysiology (BEP032) brings NWB data into BIDS datasets [TODO-C15].

**Psych-DS (dataset organization for psychological and tabular behavioral data).** Psych-DS is a
BIDS-inspired standard for tabular psychological and behavioral data such as questionnaires, task
responses, reaction times, and demographic information [REF: Psych-DS]. It requires CSV data files, a
dataset-level JSON metadata file that defines every variable, and validation; it is defined in LinkML.
It fits BBQS projects whose behavioral measures are mainly tables, especially in humans.

**DANDI layout (archive-specific dataset organization).** For datasets that consist only of NWB files,
the DANDI layout provides a simplified, BIDS-inspired organization with one folder per subject and one
NWB file per session, named by subject, session, and modality [REF: DANDI docs]. It is supported by
EMBER as well as DANDI.

**HED (event annotation).** The Hierarchical Event Descriptors provide a vocabulary and grammar for
annotating what happened during an experiment, such as stimuli, actions, and their context, in a
machine-readable way [REF: Robbins 2022]. HED is integrated in BIDS and available for NWB through an
extension (ndx-hed), which makes it one of the few annotation systems that works **across** the BBQS
standards [TODO-C16].

**Terminologies.** For common metadata, BBQS recommends established terminologies such as the NCBI
Taxonomy for species, brain atlases (e.g., the Allen Mouse Brain Common Coordinate Framework) for
anatomical locations, and the Cell Ontology for cell types [REF: Federhen 2012; Wang 2020; Cell
Ontology].

In the terms of the video analogy, EMBER is the platform, NWB is the container that keeps all streams of
a session in sync, BIDS and Psych-DS are the playlists that organize many recordings, and HED and the
shared terminologies are the categories and tags. Seen on the map, the stack is complete in the vertical
direction. Each layer has at least one recommended technology, and the technologies are connected (EMBER
accepts NWB, BIDS, and Psych-DS; NWB uses HDF5/Zarr and HDMF; Psych-DS uses CSV and LinkML; BIDS uses
JSON/TSV and can include NWB). The gaps are horizontal, between NWB, BIDS, and Psych-DS, and between all
three and the formats used by behavior-tracking tools (Section 8).