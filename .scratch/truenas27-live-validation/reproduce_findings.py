"""Synthetic reproductions only; makes no network calls and changes no behavior.

Run: python3 .scratch/truenas27-live-validation/reproduce_findings.py
Outputs observed defects rather than treating them as passing product tests.
"""

import json
import logging
import math
import sys
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT), str(ROOT / "src"), str(ROOT / "tests")]

from conftest import make_config  # noqa: E402

import truenas_exporter as exporter_module  # noqa: E402

runtime = sys.modules[exporter_module.TrueNASExporter.__module__]
logging.disable(logging.CRITICAL)


def reproduce(*, version="27.0.0-RC.1", minimum_protocol="SMB1", expire_late=False):
    now = [100.0]
    counts = {
        "successful_calls": 0,
        "deadline_rejections": 0,
        "late_transport_calls": 0,
    }

    class API:
        def __init__(self, **kwargs):
            self.deadline = kwargs.get("deadline_monotonic", float("inf"))

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return None

        def authenticate(self, key, call=None, **kwargs):
            return None

        def ensure_within_deadline(self, operation):
            if now[0] >= self.deadline:
                counts["deadline_rejections"] += 1
                raise TimeoutError(f"{operation}: synthetic total scrape budget exhausted")

        def call(self, method, params=None):
            if now[0] >= self.deadline:
                counts["late_transport_calls"] += 1
                raise TimeoutError("synthetic total scrape budget exhausted")
            counts["successful_calls"] += 1
            if method == "system.version_short":
                return version
            if method == "system.state":
                return "READY"
            if method == "system.ready":
                return True
            if method == "system.info":
                return {"physmem": 1073741824, "uptime_seconds": 1234}
            if method == "system.product_type":
                return "SCALE"
            if method == "vm.get_available_memory":
                return 0
            if method == "vm.get_vmemory_in_use":
                return {"RNP": 0, "PRD": 0, "RPRD": 0}
            if method == "update.status":
                if expire_late:
                    now[0] += 26
                return {"status": {"new_version": None}}
            if method == "smb.config":
                return {"minimum_protocol": minimum_protocol, "multichannel": False,
                        "ntlmv1_auth": False, "encryption": "DEFAULT"}
            if method.endswith(".query") or method in {
                "core.get_jobs", "route.system_routes", "nfs.get_nfs3_clients",
                "nfs.get_nfs4_clients", "auth.sessions", "iscsi.global.sessions",
            }:
                if params and len(params) > 1 and isinstance(params[1], dict) and params[1].get("count"):
                    return 0
                return []
            return {}

    exporter = runtime.TrueNASExporter(make_config())
    with patch.object(runtime, "JsonRpcWsClient", API), patch.object(runtime.time, "monotonic", lambda: now[0]):
        exporter.scrape_once()
        samples = [sample for family in exporter.metric_snapshot() for sample in family.samples]
        up = next(sample.value for sample in samples if sample.name == "truenas_up")
        smb = next((sample.value for sample in samples if sample.name == "truenas_smb1_enabled"), None)
        return {
            "version": version, "profile": exporter.compatibility_profile.name,
            "expire_late": expire_late, **counts, "up": up, "ready": exporter.is_ready(),
            "expected_smb1_enabled": int(minimum_protocol == "SMB1"),
            "smb1_metric_finite": smb is not None and math.isfinite(smb),
            "smb1_metric": smb if smb is not None and math.isfinite(smb) else None,
        }


def reproduce_event_snapshot(mode="collector", republish=False, ttl=15):
    now = [100.0]
    exporter = runtime.TrueNASExporter(make_config(exporter_mode=mode, event_stale_after_seconds=ttl))
    collector = runtime.TrueNASCollector(exporter)
    with patch.object(runtime.time, "monotonic", lambda: now[0]):
        exporter._dispatch_event("reporting.realtime", {"cpu": {"cpu": {"usage": 25}}})
        # This is the existing bridge used when a polling generation completes.
        exporter._publish_cached_events_to_default_registry()
        exporter._publish_metric_snapshot()
        for step in range(1, 9):
            now[0] = 100.0 + step * 2
            exporter._dispatch_event("reporting.realtime", {"cpu": {"cpu": {"usage": 25 + step}}})
        if republish:
            exporter._publish_cached_events_to_default_registry()
            exporter._publish_metric_snapshot()
        cpu = next(s.value for family in collector.collect() for s in family.samples
                   if s.name == "truenas_cpu_usage_percent")
        return {
            "scenario": "continuous_events_between_polls", "mode": mode,
            "republish_control": republish, "ttl_seconds": ttl,
            "latest_event_age_seconds": now[0] - exporter._event_last_monotonic["reporting.realtime"],
            "snapshot_event_age_seconds": now[0] - exporter._snapshot_event_times["reporting.realtime"],
            "expected_cpu": 33, "cpu_finite": math.isfinite(cpu),
            "observed_cpu": cpu if math.isfinite(cpu) else None,
        }


if __name__ == "__main__":
    if "--assert-event-freshness" in sys.argv:
        result = reproduce_event_snapshot()
        print(json.dumps(result, sort_keys=True))
        assert result["observed_cpu"] == result["expected_cpu"], "continuously arriving events vanished from collector snapshot"
        raise SystemExit(0)
    for args in [
        {"expire_late": True},
        {"minimum_protocol": "SMB1"},
        {"minimum_protocol": "SMB2"},
        {"version": "26.0.0", "minimum_protocol": "SMB1"},
    ]:
        print(json.dumps(reproduce(**args), sort_keys=True))
    for mode in ("collector", "legacy"):
        print(json.dumps(reproduce_event_snapshot(mode), sort_keys=True))
    print(json.dumps(reproduce_event_snapshot(republish=True), sort_keys=True))
    print(json.dumps(reproduce_event_snapshot(ttl=60), sort_keys=True))
