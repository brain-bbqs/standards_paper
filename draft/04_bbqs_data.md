# 4. BBQS data are multimodal, naturalistic, and span many species

*(target ~600 words; Fig. 4a–b)*

The NIH BRAIN Initiative's Brain Behavior Quantification and Synchronization (BBQS) program funds
projects that develop tools to measure behavior precisely and to synchronize it with neural activity,
with an emphasis on naturalistic behavior [REF: BBQS program description]. BBQS is a useful test case
for the ecosystem map because its data cut across almost every community the map contains.

To characterize BBQS data, we compiled the program's project inventory, which consists of a consolidated
workbook of award information and a questionnaire completed by project teams, and report aggregate
statistics only (Methods) [TODO-C7]. The inventory covers **28 awards** (15 R34, 10 R61, 3 U01).

**Many species.** Projects study **13 species groups**, mostly humans (11 awards) and mice (8), as well
as rats, gerbils, ferrets, sheep, marmosets, wild capuchin monkeys, songbirds (cowbirds), cichlid fish,
other fish, flies, and an acoel worm (one award each) [TODO-C8]. Seventeen awards study only non-human
animals and eleven only humans. Species diversity matters for standards, because terminologies for
anatomy, atlases, and behavior are well developed for humans and a few model organisms but sparse for
many of these species [TODO-C9].

**Many modalities, captured together.** Video is the dominant behavioral modality (mentioned by 25 of 28
awards), followed by wearable or inertial sensors (18), pose estimation (13; most often with DeepLabCut
[REF: Mathis 2018] or SLEAP [REF: Pereira 2022]), audio (13), and eye tracking (10) [TODO-C10]. Neural
data include extracellular electrophysiology (13 awards), EEG (8), and optical physiology (5), and
several projects add EMG, GPS, RFID, or physiological sensors. Most projects record several of these
streams at once, so that **synchronization across devices**, with a shared time base and metadata that
say how clocks were aligned, is as important as the format of any single stream.

**Naturalistic behavior.** Projects describe the behaviors they measure using a common list (22 awards
answered). The most frequent are locomotion and movement (16 awards), social interactions (15),
exploratory behavior (14), feeding and drinking (9), posture and balance (8), vocalizations and speech
(8), and emotional and stress responses (8); less frequent are cognitive and memory tasks (6), gait (5),
eye movements (5), facial expressions (4), reproductive behaviors, physical activity levels, and operant
conditioning (3 each), sleep (2), and pain indicators (1) (Fig. 4b). Many of these are continuous,
unconstrained, and long-lasting, recorded over hours or days in home cages, aviaries, homes, or the wild
rather than as structured trials in a task.

**Standards and sharing today.** Of 18 awards that reported a data standard, 11 use or plan to use NWB,
4 use BIDS (3 of all awards also mention HED), and 3 had not yet chosen a standard, for example because
no standard was known for 3D pose data, which were stored as NumPy arrays [TODO-C11]. None reported
Psych-DS. For sharing, 13 of these 18 awards named a neuroscience archive (DANDI, EMBER, OpenNeuro, or
NDA), but 14 also listed general cloud storage (Dropbox, Box, or Google Drive) and 14 listed GitHub,
often for code but sometimes for data [TODO-C12].

These numbers point to three challenges that recur in the rest of this paper. First, BBQS projects must
**combine standards** from communities that rarely interact, such as neurophysiology (NWB), neuroimaging
and EEG (BIDS), psychology (Psych-DS), and computer vision (video and pose formats). Second, several of
the **most common BBQS behaviors have no established representation** in any of these standards (Section
7). Third, data often live outside archives during a project, so the **path from the lab to the
archive**, including conversion, validation, and metadata entry, must be easy enough to happen
routinely. All BBQS data are to be deposited in the EMBER archive [REF: EMBER], which accepts NWB, BIDS,
Psych-DS, and the DANDI layout; the question for each project is therefore not *whether* to use a
standard but *which combination*.