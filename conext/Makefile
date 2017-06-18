
LATEX=pdflatex

BIBTEX=bibtex
BIBFILE=reference.bib
PAPER=main

TEXFILES = main.tex \
	reference.bib \
	analysis.tex \
	intro.tex \
	background.tex \
	abstract.tex \
	solution.tex \
	conclusion.tex \
	related.tex

EPSFIGS = \

EPSGRAPHS = $(wildcard figs/*.eps)

all: $(PAPER).pdf $(TEXTFILES)

$(PAPER).pdf:
	$(LATEX)  $(PAPER).tex
	$(BIBTEX) $(PAPER)
	$(LATEX) $(PAPER).tex
	$(LATEX)  $(PAPER).tex

clean:
	/bin/rm -f *.dvi *.aux *.ps *~ *.log *.lot *.lof *.toc *.blg *.bbl *.pdf
