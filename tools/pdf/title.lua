-- Use the first level-1 heading (the paper title in draft/00_title_abstract.md) as the document title,
-- so the title block comes before the table of contents.
function Pandoc(doc)
  local first = doc.blocks[1]
  if not doc.meta.title and first and first.t == "Header" and first.level == 1 then
    doc.meta.title = first.content
    doc.blocks:remove(1)
  end
  return doc
end
