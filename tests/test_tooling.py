import pytest
import runpy

from scripts.convert_truenas_api_docs_to_markdown import convert


def test_live_smoke_imports_from_source_checkout():
    runpy.run_path("scripts/live_smoke.py", run_name="live_smoke_import_test")


def test_compose_forwards_documented_environment_keys():
    env_keys = {
        line.split("=", 1)[0]
        for line in open(".env.example", encoding="utf-8")
        if line.strip() and not line.lstrip().startswith("#")
    }
    compose = open("docker-compose.yml", encoding="utf-8").read()
    missing = {key for key in env_keys if f"      {key}:" not in compose}
    assert not missing


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
