import json
import runpy
from pathlib import Path

from scripts.validate_dashboard import METRIC_RE, dashboard_validation_errors


def test_tabbed_dashboard_generation_is_offline_and_repeatable(monkeypatch):
    import urllib.request

    def forbidden(*args, **kwargs):
        raise AssertionError("dashboard generation attempted network access")

    monkeypatch.setattr(urllib.request, "urlopen", forbidden)
    builder = runpy.run_path("grafana-dashboard/build_mission_control.py")
    first, _ = builder["build"]()
    second, _ = builder["build"]()
    assert first == second
    contract = json.loads(Path("docs/metrics-contract.json").read_text())
    names = {m["name"] for m in contract["metrics"]}
    assert set(METRIC_RE.findall(json.dumps(first))) <= names


def test_v2_dashboard_validator_checks_element_references():
    doc = {"apiVersion": "dashboard.grafana.app/v2beta1", "spec": {"elements": {}, "layout": {"kind": "GridLayout", "spec": {"items": [{"spec": {"element": {"name": "missing"}}}]}}}}
    assert any("missing" in message for message in dashboard_validation_errors(doc, {"metrics": []}))
