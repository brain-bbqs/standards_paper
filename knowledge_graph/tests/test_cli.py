from ecokg import cli


def test_validate_command(capsys):
    assert cli.main(["validate"]) == 0
    assert "0 problems" in capsys.readouterr().out


def test_report_command_offline(tmp_path, monkeypatch):
    """`report` builds from local files only (no network) and writes all outputs."""
    monkeypatch.setattr(cli, "HARVEST_DIR", tmp_path / "harvested")  # no harvested edges
    assert cli.main(["report", "--out", str(tmp_path / "out")]) == 0
    for name in ("nodes.csv", "edges.csv", "graph.graphml", "graph.json", "stats.md", "gaps.md"):
        assert (tmp_path / "out" / name).stat().st_size > 0


def test_names_match():
    from ecokg.model import Node
    n = Node("nwb", "Neurodata Without Borders", "data_standard", ["neurophysiology"], abbreviation="NWB")
    assert cli._names_match(n, "Neurodata Without Borders", [])
    assert cli._names_match(n, "Something else", ["NWB"])
    assert not cli._names_match(n, "Allen Mouse Brain Reference Atlas", ["ABA"])
