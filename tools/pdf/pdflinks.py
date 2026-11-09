r"""Write the links of a one-page PDF figure as a LaTeX overlay for \linkedgraphics.

\includegraphics keeps a PDF's drawing but drops its link annotations, so they are
redrawn over the figure: one \figlink{x}{y}{w}{h}{url} per link, in fractions of the
figure width from its bottom-left corner, with the URL hex-encoded (a PDF hex string,
so no character of it needs escaping for TeX or PDF).
Usage: pdflinks.py FIGURE.pdf > FIGURE.links.tex
"""
import sys
from pypdf import PdfReader

page = PdfReader(sys.argv[1]).pages[0]
x0, y0, x1, y1 = map(float, page.mediabox)
w = x1 - x0
print(f"% Links of {sys.argv[1]}, written by tools/pdf/pdflinks.py")
for annot in page.get("/Annots", []):
    a = annot.get_object()
    if a.get("/Subtype") != "/Link" or "/URI" not in a.get("/A", {}):
        continue
    l, b, r, t = map(float, a["/Rect"])
    l, r = sorted((l, r))
    b, t = sorted((b, t))
    uri = str(a["/A"]["/URI"]).encode().hex().upper()
    print(f"\\figlink{{{(l - x0) / w:.5f}}}{{{(b - y0) / w:.5f}}}{{{(r - l) / w:.5f}}}{{{(t - b) / w:.5f}}}{{{uri}}}")
