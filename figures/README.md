# Figures

One folder per display item, named by its number in the paper. Each folder holds the exported figure
(PDF for submission, PNG for preview, SVG where available) and a README with its status and source.
Legends are kept in one place, `draft/12_figures_tables.md`, so they can be checked against Scientific
Data's limit of 350 words for all legends together.

Generated figures are rebuilt with `make figures` from the paper root (see `../Makefile`). Figures to
be drawn or redrawn by hand should be saved here together with their editable source file.

| Item | Folder | Content | Section | Status |
|---|---|---|---|---|
| Fig. 1 | [`fig1_ecosystem_map/`](fig1_ecosystem_map/) | The data standards ecosystem seen through a video-sharing app (single panel) | 2 | design draft (PowerPoint) |
| Fig. 2 | [`fig2_fair_levels/`](fig2_fair_levels/) | Levels of FAIRness as a staircase, with the layer that adds each level | 3 | design draft (PowerPoint) |
| Fig. 3 | [`fig3_knowledge_graph/`](fig3_knowledge_graph/) | Connections in the ecosystem (knowledge graph, strict community rule) | 4 | generated draft |
| Fig. 4 | [`fig4_bbqs_data/`](fig4_bbqs_data/) | BBQS data: species, modalities, behaviors × guideline coverage | 5, 8 | generated draft |
| Fig. 5 | [`fig5_bbqs_stack/`](fig5_bbqs_stack/) | The BBQS standards stack on the map | 6 | to design (spec only) |
| Fig. 6 | [`fig6_bridges_future/`](fig6_bridges_future/) | Bridges at every layer (a) and future directions and needs (b) | 8, 9 | to design / redraw (designer) |

## Alternate figures

[`alternates/`](alternates/) holds figures that are rendered for the authors to review and choose
from, but are not used in the paper. They are not numbered, have no legend in
`draft/12_figures_tables.md`, and are not cited in the draft. If one is adopted, move it to a
numbered folder above.

| Folder | Content | Related to | Build |
|---|---|---|---|
| [`alternates/kg_lenient_community_rule/`](alternates/kg_lenient_community_rule/) | Fig. 3 with the lenient community rule (any shared community = within community) | Fig. 3 | `make alt-kg-lenient` |

If figures are renumbered, rename the folder and the files in it, and update this table, the
Makefile, `draft/12_figures_tables.md`, and `plan/TODO.md` (`make check` reports broken paths).
