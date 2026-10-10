from ecokg.build import build_graph
from ecokg.figure import draw, grid_layout


def test_grid_layout_rows_and_columns(taxonomy, nodes, curated):
    result = build_graph(taxonomy, nodes, curated)
    pos, spans, rows = grid_layout(result, taxonomy)
    assert set(pos) == set(nodes)
    # Cross-cutting communities come last; each node sits in its layer band and community column.
    assert list(spans)[-2:] == ["biology", "general"]
    for n, (x, y) in pos.items():
        x0, x1 = spans[nodes[n].home]
        assert x0 <= x <= x1
        assert abs(y - rows[nodes[n].layer]) <= 0.35


def test_draw_writes_files(tmp_path, taxonomy, nodes, curated):
    result = build_graph(taxonomy, nodes, curated)
    for kwargs in ({}, {"mode": "lenient", "sources": "curated"}, {"verified_only": True}):
        paths = draw(result, taxonomy, tmp_path / "fig", **kwargs)
        assert [p.suffix for p in paths] == [".pdf", ".svg", ".png"]
        assert all(p.stat().st_size > 0 for p in paths)
