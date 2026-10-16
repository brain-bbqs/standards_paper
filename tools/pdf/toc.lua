-- Place the table of contents at the first horizontal rule (after the title notes and draft status in
-- draft/00_title_abstract.md, before the abstract) instead of directly after the title.
function Pandoc(doc)
  for i, b in ipairs(doc.blocks) do
    if b.t == "HorizontalRule" then
      doc.blocks[i] = pandoc.RawBlock("latex", "\\setcounter{tocdepth}{2}\n\\tableofcontents\n\\bigskip")
      break
    end
  end
  return doc
end
