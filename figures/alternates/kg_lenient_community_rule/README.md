# Alternate — Knowledge graph with the lenient community rule

Not used in the paper (formerly Suppl. Fig. S1, dropped 2026-10-16); rendered for the authors to review.

| | |
|---|---|
| Related to | Fig. 3 (strict community rule) |
| Status | generated draft |
| Source | `knowledge_graph/` (`ecokg figure --mode lenient`). |
| Build | `make alt-kg-lenient` (also part of `make figures`). |
| Content | As Fig. 3, but a connection is within community whenever the two technologies share any community tag, instead of comparing the communities in which they originated. Most bridges disappear, because technologies are often tagged with the communities they reached through those bridges. |
