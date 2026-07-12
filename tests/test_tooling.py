import pytest

from scripts.convert_truenas_api_docs_to_markdown import convert


def test_docs_converter_refuses_cleaning_current_working_directory(tmp_path, monkeypatch):
    source = tmp_path / "source"
    source.mkdir()
    monkeypatch.chdir(tmp_path)

    with pytest.raises(ValueError, match="unsafe --clean output path"):
        convert(source, tmp_path, clean=True)


def test_docs_converter_refuses_cleaning_source_parent(tmp_path):
    source = tmp_path / "snapshot"
    source.mkdir()

    with pytest.raises(ValueError, match="unsafe --clean output path"):
        convert(source, tmp_path, clean=True)
