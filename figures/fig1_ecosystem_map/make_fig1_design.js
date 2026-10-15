// Design draft for Fig. 1: the data standards ecosystem seen through a video-sharing app.
//
// One screen of a generic video-sharing app (no real platform name, logo, or look) in the
// centre, with six numbered callouts that map each app element to a layer of the map
// (numbered in Table 1 order) and give neuroscience examples. Spec: README.md in this folder;
// legend: draft/12_figures_tables.md.
//
// Build:  NODE_PATH=<dir containing pptxgenjs> node make_fig1_design.js
// Output: fig1_ecosystem_map_design.pptx (editable in PowerPoint / Keynote / Google Slides)

const path = require("path");
const pptxgen = require("pptxgenjs");

// Layer palette (Okabe-Ito, colour-blind safe). Intended to be reused in Figs. 2 and 5.
const LAYER = {
  1: { name: "Data archives", color: "0072B2", ink: "FFFFFF" },
  2: { name: "Dataset organization standards", color: "009E73", ink: "FFFFFF" },
  3: { name: "File organization standards", color: "D55E00", ink: "FFFFFF" },
  4: { name: "Ontologies & terminologies", color: "CC79A7", ink: "FFFFFF" },
  5: { name: "Data formats", color: "E69F00", ink: "1A1A1A" },
  6: { name: "Schema languages", color: "56B4E9", ink: "1A1A1A" },
};

const FONT = "Arial";
const INK = "1F2933";        // main text
const MUTED = "5B6770";      // secondary text
const FRAME = "C9D1D9";      // app chrome lines
const PANEL = "F3F5F7";      // app panels
const PLAYER = "2B2F36";     // video area

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.333" x 7.5"
pres.title = "Fig. 1 design: the data standards ecosystem seen through a video-sharing app";
pres.theme = { headFontFace: FONT, bodyFontFace: FONT };

const slide = pres.addSlide();
slide.background = { color: "FFFFFF" };

const text = (s, o) => slide.addText(s, { fontFace: FONT, isTextBox: true, margin: 0, ...o });

// ---------------------------------------------------------------- title
text("The data standards ecosystem seen through a video-sharing app", {
  x: 0.5, y: 0.3, w: 12.3, h: 0.5, fontSize: 24, bold: true, color: INK, objectName: "Title",
});
text("Fig. 1 design draft: generic app (no real platform name, logo, or look); numbers follow the layer order of Table 1", {
  x: 0.5, y: 0.78, w: 12.3, h: 0.3, fontSize: 11, italic: true, color: MUTED, objectName: "Subtitle",
});

// ---------------------------------------------------------------- app mock-up
const APP = { x: 4.25, y: 1.3, w: 4.85, h: 5.6 };
slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  ...APP, rectRadius: 0.12, fill: { color: "FFFFFF" }, line: { color: FRAME, width: 1.25 },
  shadow: { type: "outer", color: "000000", opacity: 0.12, blur: 8, offset: 2, angle: 90 },
  objectName: "App window",
});

// (1) header: generic play logo + search box
const hx = APP.x + 0.2, hy = APP.y + 0.18;
slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: hx + 0.35, y: hy, w: 0.42, h: 0.3, rectRadius: 0.06, fill: { color: "6B7785" }, line: { color: "6B7785" },
  objectName: "App logo",
});
slide.addShape(pres.shapes.ISOSCELES_TRIANGLE, {
  x: hx + 0.5, y: hy + 0.08, w: 0.14, h: 0.14, rotate: 90, fill: { color: "FFFFFF" }, line: { color: "FFFFFF" },
});
slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: hx + 0.95, y: hy, w: 3.35, h: 0.3, rectRadius: 0.15, fill: { color: PANEL }, line: { color: FRAME },
  objectName: "Search box",
});
text("Search:  mouse foraging", { x: hx + 1.1, y: hy, w: 2.9, h: 0.3, fontSize: 10, color: MUTED, valign: "middle" });
slide.addShape(pres.shapes.LINE, { x: APP.x, y: APP.y + 0.66, w: APP.w, h: 0, line: { color: FRAME, width: 1 } });

// (3, 5) video player with synced tracks and codec chip
const P = { x: APP.x + 0.2, y: APP.y + 0.8, w: APP.w - 0.4, h: 1.85 };
slide.addShape(pres.shapes.RECTANGLE, { ...P, fill: { color: PLAYER }, line: { color: PLAYER }, objectName: "Video player" });
slide.addShape(pres.shapes.ISOSCELES_TRIANGLE, {
  x: P.x + P.w / 2 - 0.22, y: P.y + 0.38, w: 0.48, h: 0.42, rotate: 90,
  fill: { color: "FFFFFF", transparency: 15 }, line: { color: "FFFFFF", transparency: 15 },
});
text("S1E2_open_field.mp4", { x: P.x + 0.15, y: P.y + 0.1, w: 2.4, h: 0.25, fontSize: 9, color: "D8DEE4" });
slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: P.x + P.w - 1.5, y: P.y + 0.1, w: 1.0, h: 0.26, rectRadius: 0.05, fill: { color: "FFFFFF" }, line: { color: "FFFFFF" },
  objectName: "Codec chip",
});
text("H.264 · AV1", { x: P.x + P.w - 1.5, y: P.y + 0.1, w: 1.0, h: 0.26, fontSize: 9, bold: true, color: INK, align: "center", valign: "middle" });

const tracks = [["Video", 0.92], ["Audio", 0.8], ["Subtitles", 0.55]];
tracks.forEach(([label, frac], i) => {
  const ty = P.y + 1.05 + i * 0.25;
  text(label, { x: P.x + 0.25, y: ty - 0.03, w: 0.75, h: 0.2, fontSize: 8.5, color: "D8DEE4" });
  slide.addShape(pres.shapes.RECTANGLE, { x: P.x + 0.95, y: ty + 0.03, w: (P.w - 1.15), h: 0.11, fill: { color: "4A505A" }, line: { color: "4A505A" } });
  slide.addShape(pres.shapes.RECTANGLE, { x: P.x + 0.95, y: ty + 0.03, w: (P.w - 1.15) * frac, h: 0.11, fill: { color: "9AA5B1" }, line: { color: "9AA5B1" } });
});
slide.addShape(pres.shapes.LINE, { x: P.x + 0.95 + (P.w - 1.15) * 0.4, y: P.y + 0.99, w: 0, h: 0.78, line: { color: "FFFFFF", width: 1.25 } });

// (4) title, category, hashtags
const ty = P.y + P.h + 0.13;
text("S1E2 · Foraging in the open field", { x: P.x, y: ty, w: P.w, h: 0.3, fontSize: 12, bold: true, color: INK });
const chips = ["Science & Nature", "#mouse", "#foraging", "#behavior"];
let cx = P.x;
const chipY = ty + 0.36;
chips.forEach((c, i) => {
  const w = 0.25 + c.length * 0.075;
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: cx, y: chipY, w, h: 0.26, rectRadius: 0.13,
    fill: { color: i === 0 ? "E4E7EB" : PANEL }, line: { color: FRAME }, objectName: `Tag ${c}`,
  });
  text(c, { x: cx, y: chipY, w, h: 0.26, fontSize: 9, color: INK, align: "center", valign: "middle" });
  cx += w + 0.08;
});

// (2) series panel with episodes
const S = { x: P.x, y: chipY + 0.38, w: P.w, h: 1.0 };
slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { ...S, rectRadius: 0.06, fill: { color: PANEL }, line: { color: FRAME }, objectName: "Series panel" });
text("Series: Mouse foraging · Season 1", { x: S.x + 0.15, y: S.y + 0.08, w: S.w - 0.3, h: 0.24, fontSize: 10, bold: true, color: INK });
["S1E1 · Habituation", "S1E2 · Foraging in the open field", "S1E3 · Social foraging"].forEach((ep, i) => {
  const ey = S.y + 0.33 + i * 0.21;
  if (i === 1) {
    slide.addShape(pres.shapes.RECTANGLE, { x: S.x + 0.1, y: ey - 0.01, w: S.w - 0.2, h: 0.23, fill: { color: "E4E7EB" }, line: { color: "E4E7EB" } });
  }
  text(ep, { x: S.x + 0.2, y: ey, w: S.w - 0.4, h: 0.21, fontSize: 9.5, color: INK, bold: i === 1 });
});

// (6) upload form backed by a specification
const U = { x: P.x, y: S.y + S.h + 0.1, w: P.w, h: 0.85 };
slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { ...U, rectRadius: 0.06, fill: { color: "FFFFFF" }, line: { color: FRAME, dashType: "dash" }, objectName: "Upload form" });
text("Upload a video", { x: U.x + 0.15, y: U.y + 0.07, w: 2.0, h: 0.22, fontSize: 10, bold: true, color: INK });
[["Title *", 0.15], ["Category ▾", 1.5], ["Tags", 2.85]].forEach(([f, dx]) => {
  slide.addShape(pres.shapes.RECTANGLE, { x: U.x + dx, y: U.y + 0.33, w: 1.25, h: 0.24, fill: { color: PANEL }, line: { color: FRAME } });
  text(f, { x: U.x + dx + 0.07, y: U.y + 0.33, w: 1.1, h: 0.24, fontSize: 8.5, color: MUTED, valign: "middle" });
});
text("Fields and rules defined by a specification", { x: U.x + 0.15, y: U.y + 0.6, w: 3.6, h: 0.2, fontSize: 8.5, italic: true, color: MUTED });

// ---------------------------------------------------------------- callouts
// Anchor points on the mock-up where each numbered badge sits.
const ANCHOR = {
  1: { x: hx + 0.12, y: hy + 0.15 },                       // platform (left of logo)
  3: { x: P.x, y: P.y + 1.3 },                             // synced tracks
  2: { x: S.x, y: S.y + 0.5 },                             // series panel
  5: { x: P.x + P.w - 0.3, y: P.y + 0.23 },                // right of codec chip
  4: { x: cx + 0.1, y: chipY + 0.13 },                     // after the hashtags
  6: { x: U.x + U.w, y: U.y + 0.48 },                      // upload form
};

const CALLOUT = {
  1: { side: "L", y: 1.3, app: "The platform hosts, searches, and streams the videos", neuro: "DANDI, EMBER, OpenNeuro" },
  3: { side: "L", y: 3.15, app: "The MP4 file keeps video, audio, and subtitles in sync", neuro: "NWB, OME-Zarr" },
  2: { side: "L", y: 5.0, app: "A series with numbered episodes (S1E1, S1E2)", neuro: "BIDS, Psych-DS" },
  5: { side: "R", y: 1.3, app: "The codec (H.264, AV1) encodes the bytes", neuro: "HDF5, Zarr" },
  4: { side: "R", y: 3.15, app: "Categories and hashtags give content a shared meaning", neuro: "NCBI Taxonomy, HED" },
  6: { side: "R", y: 5.0, app: "The upload form's fields and rules come from a specification", neuro: "LinkML, JSON Schema" },
};

const BOX_W = 3.4, BOX_H = 1.6, BADGE = 0.34;

function badge(n, x, y, size = BADGE) {
  const L = LAYER[n];
  slide.addShape(pres.shapes.OVAL, {
    x: x - size / 2, y: y - size / 2, w: size, h: size,
    fill: { color: L.color }, line: { color: "FFFFFF", width: 1.25 }, objectName: `Badge ${n}`,
  });
  text(String(n), { x: x - size / 2, y: y - size / 2, w: size, h: size, fontSize: 12, bold: true, color: L.ink, align: "center", valign: "middle" });
}

for (const [key, c] of Object.entries(CALLOUT)) {
  const n = Number(key);
  const L = LAYER[n];
  const bx = c.side === "L" ? 0.5 : 13.333 - 0.5 - BOX_W;
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: bx, y: c.y, w: BOX_W, h: BOX_H, rectRadius: 0.08,
    fill: { color: L.color, transparency: 88 }, line: { color: L.color, width: 1 }, objectName: `Callout ${n}: ${L.name}`,
  });
  badge(n, bx + 0.32, c.y + 0.33);
  text(L.name, { x: bx + 0.6, y: c.y + 0.1, w: BOX_W - 0.75, h: 0.48, fontSize: 13, bold: true, color: INK, valign: "middle" });
  text(c.app, { x: bx + 0.18, y: c.y + 0.64, w: BOX_W - 0.33, h: 0.48, fontSize: 11, color: MUTED, valign: "top" });
  text([{ text: "Neuroscience: ", options: { color: MUTED } }, { text: c.neuro, options: { bold: true, color: INK } }],
    { x: bx + 0.18, y: c.y + 1.16, w: BOX_W - 0.33, h: 0.32, fontSize: 11.5, valign: "middle" });

  // connector from callout edge to the anchor, then the anchor badge
  const a = ANCHOR[n];
  const sx = c.side === "L" ? bx + BOX_W : bx;
  const sy = c.y + BOX_H / 2;
  slide.addShape(pres.shapes.LINE, {
    x: Math.min(sx, a.x), y: Math.min(sy, a.y), w: Math.abs(a.x - sx), h: Math.abs(a.y - sy),
    flipH: (a.x < sx) !== (a.y < sy) ? true : false,
    line: { color: L.color, width: 1.5 }, objectName: `Connector ${n}`,
  });
  badge(n, a.x, a.y, 0.3);
}

// ---------------------------------------------------------------- footer note
text("Layer definitions: Table 1 · Legend: draft/12_figures_tables.md · Analogy adapted from the SfN 2025 poster", {
  x: 0.5, y: 7.1, w: 12.3, h: 0.25, fontSize: 9, color: MUTED, objectName: "Source note",
});

slide.addNotes(
  "Design draft for Fig. 1 (task F2). One screen of a generic video-sharing app; each numbered element maps to a " +
  "layer of the ecosystem map (Table 1 order) with neuroscience examples. Final artwork: replace the mock-up with " +
  "designer artwork, keep the layer colours (Okabe-Ito) consistent with Figs. 2 and 5, and avoid any real platform's " +
  "name, logo, or look."
);

pres.writeFile({ fileName: path.join(__dirname, "fig1_ecosystem_map_design.pptx") })
  .then((f) => console.log("wrote", f));
