-- Turn each figure's legend into its caption. In the draft a figure is written as a "## Fig. N — title" heading,
-- the image (whose alt text, e.g. "Fig. 1 design draft", pandoc would otherwise use as the caption), and the
-- legend paragraphs. The caption becomes "Fig. N." (number taken from the heading) followed by the legend;
-- the heading is kept for the table of contents.
local function label(header)
  local text = pandoc.utils.stringify(header)
  return text:match("^(Supplementary Fig%. [^%s]+)") or text:match("^(Fig%. [^%s]+)")
end

-- An SVG figure goes into the PDF as the PDF which make renders from it under build/ (where paper.tex is
-- compiled), with its links (\linkedgraphics in tools/pdf/header.tex): "../figures/x/y.svg" -> "figures/x/y.pdf".
function Image(img)
  if FORMAT:match("latex") and img.src:match("%.svg$") then
    local pdf = img.src:gsub("^%.%./", ""):gsub("%.svg$", ".pdf")
    local links = pdf:gsub("%.pdf$", ".links.tex")
    return pandoc.RawInline("latex", "\\linkedgraphics{" .. pdf .. "}{" .. links .. "}")
  end
end

function Pandoc(doc)
  local blocks = doc.blocks
  local out = pandoc.Blocks({})
  local i = 1
  while i <= #blocks do
    local b = blocks[i]
    local fig = blocks[i + 1]
    if b.t == "Header" and fig and fig.t == "Figure" and label(b) then
      local inlines = pandoc.Inlines({ pandoc.Strong({ pandoc.Str(label(b) .. ".") }) })
      local j = i + 2
      while blocks[j] and blocks[j].t == "Para" do
        inlines:insert(pandoc.Space())
        inlines:extend(blocks[j].content)
        j = j + 1
      end
      fig.caption = { long = { pandoc.Plain(inlines) } }
      out:insert(b)
      out:insert(fig)
      i = j
    else
      out:insert(b)
      i = i + 1
    end
  end
  doc.blocks = out
  return doc
end
