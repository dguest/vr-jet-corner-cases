BIBTEX   = bibtex
PDFTEX = pdflatex -interaction=nonstopmode -halt-on-error -shell-escape

.PHONY: all clean

ALLSRC := radii.tex
all: $(ALLSRC:.tex=.pdf)
	@rm -f TMP-*

TEXFILES := $(shell find -L . -name '*.tex')
FIGURES := $(shell find -L inkfigs rafaelfigs genfigs -name '*.pdf')

GENFIGS := genfigs/radii-vs-pt-jets.pdf genfigs/radii-vs-pt.pdf
$(GENFIGS): ../plot_them.py
	$<

%.bbl: %.tex $(TEXFILES) *.bib
	$(PDFTEX) radii.tex --draftmode
	$(BIBTEX) radii.tex

IGNORE_WARNINGS := 'Marginpar on page|float specifier changed'
COLOR_WARNINGS := '^LaTeX Warning:|Fatal error'
FILTER_WARN := egrep -v $(IGNORE_WARNINGS) | egrep --color $(COLOR_WARNINGS)
%.pdf: %.tex $(TEXFILES) $(FIGURES) $(GENFIGS)
	$(PDFTEX) $< --draftmode
	$(PDFTEX) $<

clean:
	rm *.aux *.log *.nav *.out *.pdf *.snm *.toc
