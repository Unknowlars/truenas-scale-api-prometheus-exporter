import json
import runpy
from pathlib import Path

import pytest

from scripts.convert_truenas_api_docs_to_markdown import convert
from scripts.validate_dashboard import (
    DEPRECATED_DASHBOARD_METRICS,
    UNAVAILABLE_DASHBOARD_METRICS,
    dashboard_validation_errors,
    referenced_metric_names,
)


def test_live_smoke_imports_from_source_checkout():
    runpy.run_path("scripts/live_smoke.py", run_name="live_smoke_import_test")


def test_compose_forwards_documented_environment_keys():
    env_text = Path(".env.example").read_text(encoding="utf-8")
    optional_runtime_defaults = {"EVENT_SUBSCRIPTIONS"}
    env_keys = {
        line.split("=", 1)[0]
        for line in env_text.splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    } - optional_runtime_defaults
    compose = Path("docker-compose.yml").read_text(encoding="utf-8")
    missing = {key for key in env_keys if f"      {key}:" not in compose}
    assert not missing


def test_compose_does_not_force_event_subscriptions():
    compose = Path("docker-compose.yml").read_text(encoding="utf-8")
    assert "      EVENT_SUBSCRIPTIONS:" not in compose


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


def test_dashboard_references_only_available_current_metrics():
    dashboard = json.loads(
        Path("grafana-dashboard/operations-center-dashboard.json").read_text(encoding="utf-8")
    )
    contract = json.loads(Path("docs/metrics-contract.json").read_text(encoding="utf-8"))
    contract_names = {metric["name"] for metric in contract["metrics"]}
    referenced = referenced_metric_names(dashboard)

    assert contract_names >= UNAVAILABLE_DASHBOARD_METRICS
    assert contract_names >= DEPRECATED_DASHBOARD_METRICS
    assert not referenced & UNAVAILABLE_DASHBOARD_METRICS
    assert not referenced & DEPRECATED_DASHBOARD_METRICS
    assert dashboard_validation_errors(dashboard, contract) == []


@pytest.mark.parametrize(
    ("metric", "message"),
    [
        ("truenas_zfs_arc_hit_ratio", "unavailable exporter metrics"),
        ("truenas_pool_dedup_ratio", "deprecated exporter metrics"),
    ],
)
def test_dashboard_validator_rejects_compatibility_only_metric(metric, message):
    dashboard = {
        "panels": [
            {
                "id": 1,
                "gridPos": {"x": 0, "w": 1},
                "targets": [{"expr": metric}],
            }
        ]
    }
    contract = {"metrics": [{"name": metric}]}

    assert message in "\n".join(dashboard_validation_errors(dashboard, contract))
