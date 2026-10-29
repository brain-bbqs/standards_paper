"""Convert a one-slide PowerPoint figure into a layered, hyperlinked SVG.

Usage (from the paper root):

    python3 tools/pptx2svg.py figures/fig5_bbqs_stack/fig5_bbqs_stack.yaml

The YAML file names the .pptx (``source``), the SVG to write (``output``), the
links of the shapes (``links``), and which build step (Inkscape layer) each
shape belongs to (``steps``), so that an svgtune file
(https://github.com/yarikoptic/svgtune) can walk through the figure.  The
.pptx stays the editable source: re-run this after editing it.

Supported: shapes with preset geometry rect, roundRect, ellipse and line
(straight, horizontal or vertical, optionally with an arrow at the end), solid
fills with alpha, solid or dashed outlines, and text boxes (Arial, bold,
italic, colour, left/centre alignment, top/centre anchoring, spacing after a
paragraph).  Text is wrapped as PowerPoint does, using the metrics of Arial
or a metric-compatible font (Liberation Sans), and stays editable <text>.
Anything else is reported and skipped.

The configuration::

    source: fig.pptx
    output: fig.svg
    links:                       # shape name -> URL, or phrase -> URL
      EMBER: https://emberarchive.org
      HDF5 Zarr:                 # links per word or phrase of the text
        HDF5: https://www.hdfgroup.org/solutions/hdf5/
        Zarr: https://zarr.dev
        _: https://...           # optional: the rest of the shape
    steps:                       # first matching regex (on shape name) wins
      - [base, '^Layer ']
      - [nwb, '^NWB']
    split:                       # cut a line into segments of other steps
      Path B: {at: [449.3], steps: [bids-format, bids-dataset]}

Each shape becomes ``<g id="<slug of its name>">``; consecutive shapes of the
same step are wrapped in one Inkscape layer labelled with the step, so the
z-order of the slide is kept (a step can therefore have several layers; match
them with ``layer label:re=^<step>$`` in svgtune).
"""

from __future__ import annotations

import re
import subprocess
import sys
import zipfile
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr

import yaml
from lxml import etree
from PIL import ImageFont

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
}
EMU_PT = 12700.0
LINE_SPACING = 1.17  # PowerPoint single line spacing for Arial, in font sizes
ASCENT = 0.905  # Arial ascent, in font sizes
DASH = (4, 3)  # PowerPoint "dash": dash and gap in line widths


def pt(v) -> float:
    return int(v) / EMU_PT


def fmt(v: float) -> str:
    return f"{v:.2f}".rstrip("0").rstrip(".")


@lru_cache(None)
def font(bold: bool, italic: bool) -> ImageFont.FreeTypeFont:
    style = ":bold" * bold + ":italic" * italic
    path = subprocess.run(["fc-match", "-f", "%{file}", "Arial" + style],
                          capture_output=True, text=True, check=True).stdout
    return ImageFont.truetype(path, 100)


def text_width(s: str, size: float, bold: bool, italic: bool) -> float:
    return font(bold, italic).getlength(s) * size / 100.0


def slug(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return s if s and s[0].isalpha() else "s-" + s


@dataclass
class Run:
    text: str
    size: float
    bold: bool
    italic: bool
    color: str
    href: str | None = None


@dataclass
class Para:
    runs: list[Run]
    align: str
    space_after: float


@dataclass
class Shape:
    name: str
    geom: str
    x: float
    y: float
    w: float
    h: float
    flip_h: bool = False
    flip_v: bool = False
    adj: float | None = None
    fill: str | None = None
    fill_opacity: float = 1.0
    stroke: str | None = None
    stroke_width: float = 0.0
    dashed: bool = False
    arrow_end: bool = False
    paras: list[Para] = field(default_factory=list)
    insets: tuple = (7.2, 3.6, 7.2, 3.6)  # l, t, r, b
    anchor: str = "t"
    wrap: bool = True


def color_of(el) -> tuple[str | None, float]:
    if el is None or el.find("a:noFill", NS) is not None:
        return None, 1.0
    c = el.find("a:solidFill/a:srgbClr", NS)
    if c is None:
        return None, 1.0
    alpha = c.find("a:alpha", NS)
    return "#" + c.get("val"), (int(alpha.get("val")) / 1e5 if alpha is not None else 1.0)


def parse_shape(sp, warn) -> Shape | None:
    name = sp.find(".//p:cNvPr", NS).get("name")
    sppr = sp.find("p:spPr", NS)
    xfrm = sppr.find("a:xfrm", NS)
    geom = sppr.find("a:prstGeom", NS)
    if xfrm is None or geom is None:
        warn(f"{name!r}: no position or preset geometry, skipped")
        return None
    off, ext = xfrm.find("a:off", NS), xfrm.find("a:ext", NS)
    shp = Shape(name, geom.get("prst"), pt(off.get("x")), pt(off.get("y")),
                pt(ext.get("cx")), pt(ext.get("cy")),
                xfrm.get("flipH") == "1", xfrm.get("flipV") == "1")
    if shp.geom not in ("rect", "roundRect", "ellipse", "line"):
        warn(f"{name!r}: geometry {shp.geom} not supported, skipped")
        return None
    gd = geom.find("a:avLst/a:gd", NS)
    if gd is not None:
        shp.adj = int(gd.get("fmla").split()[1]) / 1e5
    shp.fill, shp.fill_opacity = color_of(sppr)
    ln = sppr.find("a:ln", NS)
    if ln is not None:
        shp.stroke, _ = color_of(ln)
        shp.stroke_width = pt(ln.get("w", 12700))
        dash = ln.find("a:prstDash", NS)
        shp.dashed = dash is not None and dash.get("val") != "solid"
        tail = ln.find("a:tailEnd", NS)
        shp.arrow_end = tail is not None and tail.get("type", "none") != "none"
        if ln.find("a:headEnd", NS) is not None:
            warn(f"{name!r}: arrow heads at the start are not supported")
    body = sp.find("p:txBody", NS)
    if body is not None:
        bp = body.find("a:bodyPr", NS)
        shp.insets = tuple(pt(bp.get(k, d)) for k, d in
                           (("lIns", 91440), ("tIns", 45720), ("rIns", 91440), ("bIns", 45720)))
        shp.anchor = bp.get("anchor", "t")
        shp.wrap = bp.get("wrap", "square") != "none"
        for p in body.findall("a:p", NS):
            ppr = p.find("a:pPr", NS)
            align = ppr.get("algn", "l") if ppr is not None else "l"
            spc = p.find("a:pPr/a:spcAft/a:spcPts", NS)
            runs = []
            for r in p.findall("a:r", NS):
                rpr = r.find("a:rPr", NS)
                col, _ = color_of(rpr)
                runs.append(Run(r.findtext("a:t", "", NS), int(rpr.get("sz", 1800)) / 100,
                                rpr.get("b") == "1", rpr.get("i") == "1", col or "#000000"))
            if runs:
                shp.paras.append(Para(runs, align, int(spc.get("val")) / 100 if spc is not None else 0))
    return shp


# --------------------------------------------------------------- links
def assign_links(shp: Shape, spec) -> str | None:
    """Give each run (split into words) its href; return the shape's default href."""
    if spec is None:
        default, phrases = None, {}
    elif isinstance(spec, str):
        default, phrases = spec, {}
    else:
        default = spec.get("_")
        phrases = {k: v for k, v in spec.items() if k != "_"}
    used = set()
    for para in shp.paras:
        words: list[Run] = []
        for r in para.runs:
            for tok in re.split(r"( +)", r.text):
                if tok:
                    words.append(Run(tok, r.size, r.bold, r.italic, r.color, default))
        for phrase, href in phrases.items():
            parts = phrase.split()
            nonspace = [i for i, w in enumerate(words) if not w.text.isspace()]
            for k in range(len(nonspace) - len(parts) + 1):
                idx = nonspace[k:k + len(parts)]
                if [words[i].text.strip(".,;:()") for i in idx] == parts:
                    for i in range(idx[0], idx[-1] + 1):
                        words[i].href = href
                    used.add(phrase)
        para.runs = words
    missing = set(phrases) - used
    if missing:
        raise SystemExit(f"{shp.name!r}: link phrases not found in its text: {sorted(missing)}")
    return default


# --------------------------------------------------------------- text
def layout(para: Para, width: float, wrap: bool) -> list[list[Run]]:
    """Break the runs (words and spaces) of a paragraph into lines."""
    lines, cur, cur_w = [], [], 0.0
    for r in para.runs:
        w = text_width(r.text, r.size, r.bold, r.italic)
        if r.text.isspace():
            if cur:
                cur.append(r)
                cur_w += w
            continue
        if wrap and cur and cur_w + w > width + 0.01:
            while cur and cur[-1].text.isspace():
                cur.pop()
            lines.append(cur)
            cur, cur_w = [], 0.0
        cur.append(r)
        cur_w += w
    while cur and cur[-1].text.isspace():
        cur.pop()
    if cur:
        lines.append(cur)
    return lines


def text_svg(shp: Shape) -> str:
    l, t, r, b = shp.insets
    box_w = shp.w - l - r
    blocks = []  # (para, lines)
    total = 0.0
    for para in shp.paras:
        lines = layout(para, box_w, shp.wrap)
        size = max((x.size for x in para.runs), default=10)
        blocks.append((para, lines, size))
        total += len(lines) * size * LINE_SPACING + para.space_after
    if blocks:
        total -= blocks[-1][0].space_after
    if shp.anchor == "ctr":
        y = shp.y + t + (shp.h - t - b - total) / 2
    elif shp.anchor == "b":
        y = shp.y + shp.h - b - total
    else:
        y = shp.y + t
    out = []
    for para, lines, size in blocks:
        for line in lines:
            base = y + size * (LINE_SPACING - 1) / 2 + size * ASCENT
            if para.align == "ctr":
                x, anchor = shp.x + l + box_w / 2, "middle"
            elif para.align == "r":
                x, anchor = shp.x + shp.w - r, "end"
            else:
                x, anchor = shp.x + l, "start"
            # merge neighbouring words of one style and link
            groups: list[list[Run]] = []
            for w in line:
                if groups and (groups[-1][0].size, groups[-1][0].bold, groups[-1][0].italic,
                               groups[-1][0].color, groups[-1][0].href) == (
                        w.size, w.bold, w.italic, w.color, w.href):
                    groups[-1].append(w)
                else:
                    groups.append([w])
            spans = []
            for g in groups:
                r0 = g[0]
                attrs = f' font-size="{fmt(r0.size)}" fill="{r0.color}"'
                if r0.bold:
                    attrs += ' font-weight="bold"'
                if r0.italic:
                    attrs += ' font-style="italic"'
                span = f"<tspan{attrs}>{escape(''.join(w.text for w in g))}</tspan>"
                if r0.href:
                    span = f'<a href={quoteattr(r0.href)} target="_blank">{span}</a>'
                spans.append(span)
            out.append(f'<text x="{fmt(x)}" y="{fmt(base)}" text-anchor="{anchor}" '
                       f'xml:space="preserve">{"".join(spans)}</text>')
            y += size * LINE_SPACING
        y += para.space_after
    return "".join(out)


# --------------------------------------------------------------- shapes
def marker_id(color: str) -> str:
    return "arrow-" + color.lstrip("#").lower()


def line_ends(shp: Shape) -> tuple[float, float, float, float]:
    x1, y1, x2, y2 = shp.x, shp.y, shp.x + shp.w, shp.y + shp.h
    if shp.flip_h:
        x1, x2 = x2, x1
    if shp.flip_v:
        y1, y2 = y2, y1
    return x1, y1, x2, y2


def stroke_attrs(shp: Shape) -> str:
    if not shp.stroke:
        return ' stroke="none"'
    s = f' stroke="{shp.stroke}" stroke-width="{fmt(shp.stroke_width)}"'
    if shp.dashed:
        s += f' stroke-dasharray="{fmt(DASH[0] * shp.stroke_width)},{fmt(DASH[1] * shp.stroke_width)}"'
    return s


def segment_svg(shp: Shape, x1, y1, x2, y2, arrow: bool) -> str:
    extra = ""
    if arrow:
        # the marker tip is at the end point: shorten the line under the arrow head
        import math
        d = math.hypot(x2 - x1, y2 - y1)
        k = 2.5 * shp.stroke_width / d if d else 0
        x2, y2 = x2 - (x2 - x1) * k, y2 - (y2 - y1) * k
        extra = f' marker-end="url(#{marker_id(shp.stroke)})"'
    return (f'<line x1="{fmt(x1)}" y1="{fmt(y1)}" x2="{fmt(x2)}" y2="{fmt(y2)}"'
            f'{stroke_attrs(shp)} fill="none"{extra}/>')


def shape_svg(shp: Shape, default_href: str | None) -> str:
    if shp.geom == "line":
        return segment_svg(shp, *line_ends(shp), shp.arrow_end)
    fill = f' fill="{shp.fill}"' if shp.fill else ' fill="none"'
    if shp.fill and shp.fill_opacity < 1:
        fill += f' fill-opacity="{fmt(shp.fill_opacity)}"'
    common = fill + stroke_attrs(shp)
    if shp.geom == "ellipse":
        el = (f'<ellipse cx="{fmt(shp.x + shp.w / 2)}" cy="{fmt(shp.y + shp.h / 2)}" '
              f'rx="{fmt(shp.w / 2)}" ry="{fmt(shp.h / 2)}"{common}/>')
    else:
        rx = ""
        if shp.geom == "roundRect":
            rad = min(shp.w, shp.h) * (0.16667 if shp.adj is None else shp.adj)
            rx = f' rx="{fmt(rad)}"'
        el = (f'<rect x="{fmt(shp.x)}" y="{fmt(shp.y)}" width="{fmt(shp.w)}" '
              f'height="{fmt(shp.h)}"{rx}{common}/>')
    if default_href and (shp.fill or shp.stroke):
        el = f'<a href={quoteattr(default_href)} target="_blank">{el}</a>'
    return el + text_svg(shp)


def main(cfg_path: str) -> None:
    cfg_file = Path(cfg_path)
    cfg = yaml.safe_load(cfg_file.read_text())
    here = cfg_file.parent
    src, out = here / cfg["source"], here / cfg["output"]
    links = cfg.get("links", {})
    steps = [(name, re.compile(rx)) for name, rx in cfg.get("steps", [])]
    splits = cfg.get("split", {})

    def warn(msg):
        print("WARNING:", msg, file=sys.stderr)

    with zipfile.ZipFile(src) as z:
        pres = etree.fromstring(z.read("ppt/presentation.xml"))
        sld = etree.fromstring(z.read("ppt/slides/slide1.xml"))
    size = pres.find("p:sldSz", NS)
    W, H = pt(size.get("cx")), pt(size.get("cy"))

    items = []  # (step, svg)
    seen_ids: dict[str, int] = {}
    unused_links = set(links)
    colors = set()
    for el in sld.find("p:cSld/p:spTree", NS):
        tag = etree.QName(el).localname
        if tag in ("nvGrpSpPr", "grpSpPr"):
            continue
        if tag != "sp":
            warn(f"element <{tag}> not supported, skipped")
            continue
        shp = parse_shape(el, warn)
        if shp is None:
            continue
        sid = slug(shp.name)
        seen_ids[sid] = seen_ids.get(sid, 0) + 1
        if seen_ids[sid] > 1:
            sid += f"-{seen_ids[sid]}"
        step = next((n for n, rx in steps if rx.search(shp.name)), "base")
        unused_links.discard(shp.name)
        href = assign_links(shp, links.get(shp.name))
        label = quoteattr(shp.name)
        if shp.arrow_end and shp.stroke:
            colors.add(shp.stroke)
        if shp.name in splits and shp.geom == "line":
            sp = splits.pop(shp.name)
            x1, y1, x2, y2 = line_ends(shp)
            # cut points along the line, in order from its start to its end
            cuts = sorted(sp["at"], key=lambda c: abs(c - (y1 if x1 == x2 else x1)))
            pts = [(x1, y1)] + [((x1, c) if x1 == x2 else (c, y1)) for c in cuts] + [(x2, y2)]
            assert len(sp["steps"]) == len(pts) - 1, shp.name
            for i, st in enumerate(sp["steps"]):
                last = i == len(pts) - 2
                body = segment_svg(shp, *pts[i], *pts[i + 1], shp.arrow_end and last)
                items.append((st, f'<g id="{sid}-{i + 1}" inkscape:label={label}>{body}</g>'))
            continue
        items.append((step, f'<g id="{sid}" inkscape:label={label}>{shape_svg(shp, href)}</g>'))
    if unused_links:
        raise SystemExit(f"links for shapes not in the slide: {sorted(unused_links)}")
    if splits:
        raise SystemExit(f"split for lines not in the slide: {sorted(splits)}")

    defs = "".join(
        f'<marker id="{marker_id(c)}" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="3" '
        f'markerHeight="3" orient="auto-start-reverse" markerUnits="strokeWidth">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>' for c in sorted(colors))
    layers, counts = [], {}
    for step, svg in items:
        if layers and layers[-1][0] == step:
            layers[-1][1].append(svg)
        else:
            layers.append((step, [svg]))
    body = []
    for step, svgs in layers:
        counts[step] = counts.get(step, 0) + 1
        lid = f"layer-{slug(step)}" + (f"-{counts[step]}" if counts[step] > 1 else "")
        body.append(f'<g inkscape:groupmode="layer" id="{lid}" inkscape:label="{escape(step)}" '
                    f'style="display:inline">\n' + "\n".join(svgs) + "\n</g>")
    title = escape(cfg.get("title", src.stem))
    svg = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<!-- Generated by tools/pptx2svg.py from {src.name} and {cfg_file.name}: '
        'edit those, not this file. -->\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" '
        f'width="{fmt(W)}pt" height="{fmt(H)}pt" viewBox="0 0 {fmt(W)} {fmt(H)}" '
        'font-family="Arial, \'Liberation Sans\', Helvetica, sans-serif">\n'
        f"<title>{title}</title>\n<defs>{defs}</defs>\n"
        f'<rect id="background" width="{fmt(W)}" height="{fmt(H)}" fill="#ffffff"/>\n'
        + "\n".join(body) + "\n</svg>\n")
    out.write_text(svg)
    n_links = svg.count("<a ")
    print(f"wrote {out} ({len(items)} shapes, {len(layers)} layers, {n_links} links)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
