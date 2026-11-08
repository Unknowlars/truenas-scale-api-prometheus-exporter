"""PRR-05: pin the two distinct lifetimes the documentation describes.

* ``/readyz`` (``is_ready``) means *a recent successful poll cycle*. A later
  failed cycle sets ``truenas_up=0`` but does not clear readiness until the
  last success is older than max(2*budget, 2*interval, 30) seconds.
* ``truenas_event_stream_up`` means *the subscription is active*. Event data
  expires by TTL independently, so a live subscription can coexist with NaN
  event values.

These tests characterize existing behavior; they do not redefine it.
"""

from __future__ import annotations

import math
import sys

from conftest import make_config

import truenas_exporter as exporter_module

runtime = sys.modules[exporter_module.TrueNASExporter.__module__]


def _fake_api(state):
    class API:
        def __init__(self, **_kwargs):
            pass

        def __enter__(self):
            if state["fail"]:
                raise ConnectionError("synthetic NAS unavailable")
            return self

        def __exit__(self, *_args):
            return None

        def authenticate(self, _key, call=None, **_kwargs):
            return None

        def ensure_within_deadline(self, _method):
            return None

        def call(self, method, params=None):
            if method == "system.version_short":
                return "27.0.0"
            if method == "system.state":
                return "READY"
            if method == "system.product_type":
                return "SCALE"
            if method == "system.ready":
                return True
            if method == "system.info":
                return {"physmem": 1, "uptime_seconds": 1}
            if method == "vm.get_available_memory":
                return 0
            if method == "vm.get_vmemory_in_use":
                return {"RNP": 0, "PRD": 0, "RPRD": 0}
            if method.endswith(".query"):
                if params and len(params) > 1 and params[1].get("count"):
                    return 0
                return []
            return {}

    return API


def _up(exporter):
    samples = [s for f in exporter.metric_snapshot() for s in f.samples]
    return next(s.value for s in samples if s.name == "truenas_up")


def test_readiness_survives_failed_poll_until_last_success_expires(monkeypatch):
    now = [1000.0]
    state = {"fail": False}
    monkeypatch.setattr(runtime, "JsonRpcWsClient", _fake_api(state))
    monkeypatch.setattr(runtime.time, "monotonic", lambda: now[0])
    config = make_config()
    exporter = exporter_module.TrueNASExporter(config)
    max_age = max(config.scrape_budget_seconds * 2, config.interval_seconds * 2, 30)

    exporter.scrape_once()
    assert _up(exporter) == 1
    assert exporter.is_ready() is True

    state["fail"] = True
    now[0] += 1
    exporter.scrape_once()
    # The failed cycle is visible in truenas_up, but readiness deliberately
    # still reflects the recent prior success.
    assert _up(exporter) == 0
    assert exporter.is_ready() is True

    now[0] = 1000.0 + max_age
    assert exporter.is_ready() is True
    now[0] = 1000.0 + max_age + 0.001
    assert exporter.is_ready() is False

    state["fail"] = False
    exporter.scrape_once()
    assert _up(exporter) == 1
    assert exporter.is_ready() is True


def test_active_subscription_coexists_with_expired_event_data(monkeypatch):
    now = [500.0]
    monkeypatch.setattr(runtime.time, "monotonic", lambda: now[0])
    exporter = exporter_module.TrueNASExporter(make_config())
    exporter._collector_event_stream_up["reporting.realtime"] = 1.0
    exporter._dispatch_event("reporting.realtime", {"cpu": {"cpu": {"usage": 25.0}}})

    def snapshot():
        exporter._publish_cached_events_to_default_registry()
        exporter._publish_metric_snapshot()
        out = {}
        for family in exporter_module.TrueNASCollector(exporter).collect():
            for s in family.samples:
                if s.name == "truenas_cpu_usage_percent":
                    out["cpu"] = s.value
                if s.name == "truenas_event_stream_up" and s.labels.get("event") == "reporting.realtime":
                    out["stream_up"] = s.value
        return out

    fresh = snapshot()
    assert fresh == {"cpu": 25.0, "stream_up": 1.0}

    now[0] += 16  # beyond the 15-second realtime TTL
    expired = snapshot()
    assert math.isnan(expired["cpu"])
    assert expired["stream_up"] == 1.0
