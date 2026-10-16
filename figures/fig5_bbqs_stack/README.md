# Fig. 5 — The BBQS standards stack on the map

| | |
|---|---|
| Cited in | Section 6 |
| Status | design draft (`fig5_bbqs_stack_design.pptx`, preview `fig5_bbqs_stack_design.png`); edit the .pptx directly; final artwork by designer |
| Concept | The layers of the map as a stack in Table 1 order, from data formats (1) at the bottom to data archives (5) at the top, with the technologies BBQS recommends in each layer. Arrows climb from typical raw data through these technologies to EMBER, showing that the stack is complete in the vertical direction (Section 6). |
| Rows | 1 HDF5/Zarr + MP4, NIfTI + JSON/TSV, CSV + JSON · 2 NWB · 3 DANDI layout, BIDS, Psych-DS · 4 NCBI Taxonomy, brain atlases, Cell Ontology; HED · 5 EMBER. Schema languages (6) are a box over rows 2–3, as in Fig. 2: HDMF defines NWB, the BIDS schema defines BIDS, LinkML defines Psych-DS. |
| Paths | Video + pose + ephys → NWB → DANDI layout → EMBER; MRI + EEG + events → BIDS (+ HED) → EMBER; questionnaires + task responses → Psych-DS → EMBER. A path crossing a row without a chip does not use that layer. |
| Draft choices | Styled like Fig. 2: Arial; layer rows with a light tint, coloured outline, top band, and numbered badge in the Fig. 1 colours (palette in `../fig1_ecosystem_map/README.md`); technologies as white chips outlined in their layer colour; raw data in grey (as Level 0 in Fig. 2); slate arrows. Stack geometry (D8): five stacked rows with schema languages as a box across rows 2–3, consistent with Fig. 2, rather than ontologies and schema languages as cross-cutting columns. The speaker notes describe the rows and paths. |
| Source | Spec and legend in `draft/12_figures_tables.md`; content from Section 6 and Table 3. |
| Build | Not generated; the design draft .pptx is the editable source. The PNG preview is exported at 300 dpi; re-export it after editing the .pptx. Place the final artwork here. |
| Legend | `draft/12_figures_tables.md` (single source for all legends) |
| Open tasks | `plan/TODO.md`, section "3. Figures" (F3, F10) |
