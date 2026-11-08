"""Dashboard overhaul guards (D1-D15): honest missing data, rate-derived ZFS
percentages, outstanding alerts and readable tiles in both dashboards."""

import json
import re
from pathlib import Path

import pytest

from scripts.validate_dashboard import NEUTRAL_COLOR, dashboard_validation_errors

CLASSIC = Path("grafana-dashboard/operations-center-dashboard.json")
MISSION = Path("grafana-dashboard/truenas-mission-control.json")
OUTSTANDING = (
    'clamp_min(sum(truenas_alert_count{instance=~"$instance"}) - '
    '(sum(truenas_alert_dismissed_count{instance=~"$instance"}) or on() vector(0)), 0)'
)


def _contract(*names):
    return {"metrics": [{"name": n} for n in names]}


def _panel(expr, **extra):
    return {"id": 1, "title": "x", "gridPos": {"x": 0, "w": 3}, "targets": [{"expr": expr}], **extra}


def _all_panels(doc):
    for row in doc["panels"]:
        yield row
        yield from row.get("panels", [])


def test_validator_rejects_upstream_hit_ratio_metrics():
    dash = {"panels": [_panel(OUTSTANDING), _panel("100 * truenas_zfs_demand_data_hit_ratio")]}
    errors = dashboard_validation_errors(dash, _contract(
        "truenas_zfs_demand_data_hit_ratio", "truenas_alert_count", "truenas_alert_dismissed_count"))
    assert any("unreliable upstream ratio" in e for e in errors)


def test_validator_requires_outstanding_alert_expression():
    dash = {"panels": [_panel("max(truenas_alert_count)")]}
    errors = dashboard_validation_errors(dash, _contract("truenas_alert_count"))
    assert any("outstanding-alerts" in e for e in errors)


@pytest.mark.parametrize(("color", "title", "message"), [
    ("green", "OK", "no-data colour is not neutral"),
    (NEUTRAL_COLOR, "A very long tile title", "stat title too long"),
])
def test_validator_rejects_coloured_no_data_and_long_titles(color, title, message):
    stat = _panel(OUTSTANDING, type="stat", title=title,
                  fieldConfig={"defaults": {"thresholds": {"steps": [{"color": color, "value": None}]}}})
    errors = dashboard_validation_errors({"panels": [stat]}, _contract(
        "truenas_alert_count", "truenas_alert_dismissed_count"))
    assert any(message in e for e in errors)


@pytest.mark.parametrize("path", [CLASSIC, MISSION])
def test_committed_dashboards_never_query_unreliable_ratios(path):
    text = path.read_text(encoding="utf-8")
    assert not re.search(r"truenas_zfs_\w*_(hit|miss)_(ratio|percentage)", text)
    assert OUTSTANDING.replace('"', '\\"') in text


def test_classic_stats_default_to_neutral_na():
    doc = json.loads(CLASSIC.read_text(encoding="utf-8"))
    stats = [p for p in _all_panels(doc) if p["type"] == "stat"]
    assert stats
    for p in stats:
        defaults = p["fieldConfig"]["defaults"]
        assert defaults["thresholds"]["steps"][0]["color"] == NEUTRAL_COLOR, p["title"]
        assert defaults["noValue"]
        assert {"null", "nan"} <= {m["options"]["match"] for m in defaults["mappings"] if m["type"] == "special"}


def test_or_vector_zero_is_gated_on_exporter_up():
    """Absence may only read as 0 while the exporter itself is up (D7)."""
    for path in (CLASSIC, MISSION):
        for expr in re.findall(r'"expr": "((?:[^"\\]|\\.)*)"', path.read_text(encoding="utf-8")):
            # vector(0) may only stand in for a subtrahend ("x - (y or on() vector(0))"),
            # where the result still requires x; never as a standalone result.
            stripped = re.sub(r"- \(sum\((?:[^()]|\([^()]*\))*\) or on\(\) vector\(0\)\)", "", expr)
            assert "vector(0)" not in stripped, expr


def test_directory_service_disabled_is_grey_not_red():
    doc = json.loads(CLASSIC.read_text(encoding="utf-8"))
    tiles = [p for p in _all_panels(doc) if p.get("title") == "Directory Svc"]
    assert tiles
    for tile in tiles:
        assert 'status="DISABLED"' in tile["targets"][0]["expr"]
        mapping = tile["fieldConfig"]["defaults"]["mappings"][0]["options"]
        assert mapping["0"]["text"] == "Disabled" and mapping["0"]["color"] == NEUTRAL_COLOR


def test_scan_progress_is_clamped_and_disk_temps_ignore_zero():
    text = CLASSIC.read_text(encoding="utf-8")
    assert "clamp_max(truenas_pool_scan_percent" in text
    for expr in re.findall(r'"expr": "((?:[^"\\]|\\.)*)"', text):
        if "truenas_disk_temperature_celsius" in expr:
            assert "> 0" in expr, expr


def test_disk_io_falls_back_to_aggregate_total():
    text = CLASSIC.read_text(encoding="utf-8")
    assert 'disk=\\"total\\"} unless on (instance)' in text


def test_mission_control_has_hero_incident_and_repeat():
    doc = json.loads(MISSION.read_text(encoding="utf-8"))
    tabs = [t["spec"]["title"] for t in doc["spec"]["layout"]["spec"]["tabs"]]
    assert tabs[:2] == ["🏠 Overview", "🚑 Incident"]
    titles = {e["spec"]["title"] for e in doc["spec"]["elements"].values()}
    assert {"Is my NAS OK?", "Health checks", "What needs attention right now?"} <= titles
    assert '"repeat": {' in MISSION.read_text(encoding="utf-8")
