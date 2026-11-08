"""PRR-02: directoryservices.status missing/malformed data stays unknown.

Each case drives a stubbed RPC response through the collector into a
published snapshot, then reads the families served on /metrics.
"""

from __future__ import annotations

import math

import pytest
from conftest import make_config

import truenas_exporter as m

FAMILIES = (
    "truenas_directoryservices_status",
    "truenas_directoryservices_healthy",
    "truenas_directoryservices_fault_present",
    "truenas_directoryservices_fault_reason",
    "truenas_directoryservices_service_type",
)
ENABLED = "truenas_directoryservices_config_enabled"


def _cycle(exporter, response):
    def fake_call(client, method, params=None, *args, **kwargs):
        assert method == "directoryservices.status"
        if isinstance(response, Exception):
            raise response
        return response

    exporter._call = fake_call
    exporter._collect_directoryservices_metrics(object(), {})
    exporter._publish_metric_snapshot()
    out = {}
    for family in m.TrueNASCollector(exporter).collect():
        if family.name.startswith("truenas_directoryservices_"):
            out[family.name] = [(s.labels, s.value) for s in family.samples]
    return out


def _assert_unknown(snapshot):
    for name in FAMILIES:
        assert snapshot.get(name, []) == [], name
    enabled = snapshot.get(ENABLED, [])
    assert all(math.isnan(v) for _, v in enabled), enabled


HEALTHY = {"type": "ACTIVEDIRECTORY", "status": "HEALTHY", "status_msg": None}


@pytest.mark.parametrize(
    "response",
    [
        {},
        {"status": None},
        {"status": "HEALTHY"},
        {"type": "NIS", "status": "HEALTHY"},
        {"type": "LDAP", "status": "BROKEN"},
        {"type": "LDAP", "status": None},
        {"type": "LDAP"},
        {"type": None, "status": "HEALTHY"},
        {"type": 7, "status": "HEALTHY"},
        [],
        None,
        "DISABLED",
        RuntimeError("rpc failed"),
    ],
)
def test_missing_or_malformed_status_is_unknown_and_clears_previous(response):
    exporter = m.TrueNASExporter(make_config())
    healthy = _cycle(exporter, HEALTHY)
    assert healthy["truenas_directoryservices_healthy"] == [({"service": "activedirectory"}, 1.0)]

    _assert_unknown(_cycle(exporter, response))


@pytest.mark.parametrize("response", [{"type": None}, {"type": None, "status": None, "status_msg": None}])
def test_explicit_null_type_is_disabled_with_valid_zero(response):
    snap = _cycle(m.TrueNASExporter(make_config()), response)
    assert snap[ENABLED] == [({}, 0.0)]
    assert snap["truenas_directoryservices_status"] == [({"service": "none", "status": "DISABLED"}, 1.0)]
    assert snap["truenas_directoryservices_healthy"] == [({"service": "none"}, 0.0)]
    assert snap["truenas_directoryservices_fault_present"] == [({"service": "none"}, 0.0)]
    assert snap.get("truenas_directoryservices_service_type", []) == []


def test_faulted_state_redacts_reason_and_recovers():
    exporter = m.TrueNASExporter(make_config())
    faulted = _cycle(exporter, {"type": "ldap", "status": "faulted", "status_msg": "private detail"})
    assert faulted[ENABLED] == [({}, 1.0)]
    assert faulted["truenas_directoryservices_healthy"] == [({"service": "ldap"}, 0.0)]
    assert faulted["truenas_directoryservices_fault_present"] == [({"service": "ldap"}, 1.0)]
    assert faulted["truenas_directoryservices_fault_reason"] == [
        ({"service": "ldap", "reason": "redacted"}, 1.0)
    ]
    assert faulted["truenas_directoryservices_service_type"] == [({"service_type": "LDAP"}, 1.0)]

    _assert_unknown(_cycle(exporter, {}))

    recovered = _cycle(exporter, {"type": "LDAP", "status": "HEALTHY", "status_msg": None})
    assert recovered["truenas_directoryservices_healthy"] == [({"service": "ldap"}, 1.0)]
    assert recovered["truenas_directoryservices_fault_present"] == [({"service": "ldap"}, 0.0)]
    assert recovered.get("truenas_directoryservices_fault_reason", []) == []
    assert recovered["truenas_directoryservices_status"] == [({"service": "ldap", "status": "HEALTHY"}, 1.0)]
