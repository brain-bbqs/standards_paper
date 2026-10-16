# Neuroscience data standards paper (BBQS)

> [!WARNING]
> **This paper is in active development.** The draft, figures, and knowledge graph are
> work in progress and change frequently. Content has not yet been reviewed or approved by
> all authors, claims and relationships are still being verified, and nothing here should be
> cited or treated as the authors' final position.

Working repository for the paper *"Navigating neuroscience data standards for multimodal brain behavior
quantification and synchronization"* (target: Scientific Data, Article).

| Path | Content |
|---|---|
| `plan/paper_plan.md` | Decisions not visible in the draft, and the steps and timeline to submission |
| `draft/` | First full draft, one Markdown file per section (`draft/README.md`) |
| `plan/TODO.md` | Review list: decisions, actions, figures, and claims marked `[TODO-Cn]` in the draft |
| `analysis/` | BBQS inventory aggregates for Section 5 and Fig. 4 (`analysis/bbqs_inventory.py`; aggregate data only) |
| `figures/` | One folder per figure and supplementary item (`figures/README.md`); legends in `draft/12_figures_tables.md` |
| `knowledge_graph/` | Ecosystem knowledge graph package `ecokg` (README, `TODO.md`, tests); Fig. 3 |
| `tools/check_todo.py` | Consistency check between `plan/TODO.md` and the draft |
| `tools/pdf/` | pandoc settings for the review PDF |
| `Makefile` | `make figures` rebuilds generated figures; `make pdf` renders the draft as `build/paper.tex` and `build/paper.pdf`; `make check` checks the TODO list |

## Review PDF

The full draft is rendered as one PDF for review by the **Review PDF** GitHub workflow
(`.github/workflows/review-pdf.yml`) on every pull request and push to `main` that touches the draft or
figures. On a pull request, a comment from the workflow links to the latest PDF (updated on each push);
otherwise download it from the workflow run: Actions → Review PDF → latest run → Artifacts → `paper-pdf`.
The PDF has continuous line numbers, so please refer to page and line numbers in comments. The artifact
also contains `paper.tex`, the single LaTeX file the PDF is built from.

To build it locally, run `make pdf` (needs pandoc and XeLaTeX). The PDF uses LaTeX's standard font (Latin
Modern); symbols it lacks (✓, ●, ○, →, ≤) are mapped to LaTeX symbols in `tools/pdf/header.tex`, and the
build fails if the draft uses another character the font does not have.

Source materials (poster, guideline, BBQS inventory, BRAIN KB documents) live in the parent folder and
are not part of this repository.
