# Build generated figures and check the TODO list against the draft.
#
#   make figures     regenerate all generated figures into figures/ (paper figures and alternates)
#   make alternates  regenerate only the alternate figures (figures/alternates/, not in the paper)
#   make pdf         render the full draft (draft/*.md) as build/paper.tex and build/paper.pdf for review
#   make check       check that every [TODO-Cn] marker in draft/ has an entry in plan/TODO.md and vice versa
#   make kg-env      set up the knowledge-graph Python environment (first time only)

KG       := knowledge_graph
ECOKG    := $(KG)/.venv/bin/ecokg
UVRUN    := uv run -q --no-project --with openpyxl --with matplotlib python
PDF_FONT ?= DejaVu Serif
PDF_DATE := $(shell date +%Y-%m-%d), commit $(shell git rev-parse --short HEAD 2>/dev/null || echo unknown)

.PHONY: figures fig3 fig4 alternates alt-kg-lenient pdf check kg-env

figures: fig3 fig4 alternates

alternates: alt-kg-lenient

kg-env: $(ECOKG)

$(ECOKG):
	cd $(KG) && uv venv -q .venv && uv pip install -q -e '.[test]'

fig3: $(ECOKG)
	$(ECOKG) figure --out figures/fig3_knowledge_graph --name fig3_knowledge_graph

alt-kg-lenient: $(ECOKG)
	$(ECOKG) figure --mode lenient --out figures/alternates/kg_lenient_community_rule \
		--name kg_lenient_community_rule

fig4:
	$(UVRUN) analysis/bbqs_inventory.py

pdf:
	mkdir -p build
	pandoc --defaults tools/pdf/defaults.yaml -V mainfont="$(PDF_FONT)" -M date="Review draft, $(PDF_DATE)" \
		-o build/paper.tex $(sort $(wildcard draft/[0-9][0-9]_*.md))
	cd build && for i in 1 2; do xelatex -interaction=nonstopmode -halt-on-error paper.tex > /dev/null \
		|| { tail -40 paper.log; exit 1; }; done

check:
	python3 tools/check_todo.py
