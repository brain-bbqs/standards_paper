# Methods

*(target ~500 words; check whether the journal counts Methods toward the word limit — TODO D1)*

## BBQS project inventory

We used the BBQS project inventory maintained by the BBQS coordinating center, which combines (i) a
consolidated workbook with award information (title, award number, species, data modalities, sensors
and devices, tools) and (ii) answers to a questionnaire completed by project teams (behaviors measured,
data standards, data sharing plans). The inventory contains 47 rows for 28 awards (24 workbook rows, 19
questionnaire rows, 4 rows from NIH RePORTER) [TODO-C7].

All statistics are counted **per award**, meaning that an award is counted once for a category if any of
its rows mentions it. Species and behaviors were taken from the corresponding fields, split on commas
and semicolons, and normalized for case. Behaviors use the common list from the questionnaire; 22 awards
answered this field. Modalities, devices, tools, standards, and sharing locations were identified by
case-insensitive keyword matching over the modality, device, tool, and data-sharing fields (keywords in
`analysis/bbqs_inventory.py`). Data standards were taken from the "Standards:" statement in the
data-sharing field, which 18 awards answered. Keyword matching can over- or under-count; the counts are
being checked against the source entries [TODO-C10].

Only aggregate counts are reported; no project-level information is shown [TODO-C7].

## Guideline coverage of behavior types

For each behavior type in the questionnaire list, we recorded whether the BBQS data standards guideline
(version of 2026-10-09) [REF: BBQS guideline] gives a recommended representation in NWB, BIDS, and
Psych-DS (supported), points to an extension or proposal in progress (in progress), or marks the
entry as "TODO" or gives no entry (no guidance). The coding is in `analysis/behavior_coverage.csv`
[TODO-C23].

## Ecosystem knowledge graph (Fig. 3, Supplementary Fig. S1)

Nodes are technologies selected from the SfN 2025 poster, the guideline, and the BBQS inventory, each
assigned to one primary layer (with optional secondary layers) and to one or more research communities;
the first community is the node's home community. Edges are typed relationships (e.g., *uses format*,
*defined with*, *uses terminology*, *accepts*, *organizes*, *extends*) from two sources, expert curation
(with provenance and confidence) and relationships harvested from the RRID registry (SciCrunch resolver)
and FAIRsharing (REST API) on 2026-10-09. Registry relation labels were mapped to the same relation
types; organizational relations (e.g., parent organization, collection membership) were dropped. Each
edge is classified by **layer span** (within or across layers) and **community scope** (within or across
home communities, or *shared* when one end is domain-agnostic infrastructure such as HDF5 or a
cross-species ontology). Code and data are available as the `ecokg` package [REF: Zenodo DOI, TODO-A6] [TODO-C25, C26].