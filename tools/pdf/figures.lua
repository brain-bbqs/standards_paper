-- Render each figure as a plain centered image, without the caption pandoc builds from its alt text (e.g.
-- "Figure 1: Fig. 1 design draft"). In the draft, each figure's "Fig. N — title" heading and the legend
-- paragraphs after the image already serve as its caption.
function Figure(fig)
  local blocks = pandoc.Blocks({ pandoc.RawBlock("latex", "\\begin{center}") })
  blocks:extend(fig.content)
  blocks:insert(pandoc.RawBlock("latex", "\\end{center}"))
  return blocks
end
