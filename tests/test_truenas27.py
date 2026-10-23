"""Behavior regressions at transport and snapshot interfaces; synthetic data only."""

import json
import math
import sys
import threading
from pathlib import Path

import pytest
from conftest import make_config

import truenas_exporter as exporter_module

runtime = sys.modules[exporter_module.TrueNASExporter.__module__]
transport = sys.modules[runtime.JsonRpcWsClient.__module__]
API27 = json.loads((Path(__file__).parent / "fixtures/api_27_0_0/read_only_responses.json").read_text())


class Socket:
    def __init__(self, result=True):
        self.sent = []
        self.result = result
        self.timeouts = []

    def send(self, raw):
        self.sent.append(json.loads(raw))

    def recv(self):
        return json.dumps({"id": self.sent[-1]["id"], "result": self.result})

    def settimeout(self, timeout):
        self.timeouts.append(timeout)

    def close(self):
        pass


def test_expired_deadline_does_not_connect(monkeypatch):
    attempts = []
    monkeypatch.setattr(transport.time, "monotonic", lambda: 11)
    monkeypatch.setattr(transport, "create_connection", lambda *a, **k: attempts.append(k))
    with pytest.raises(TimeoutError), transport.JsonRpcWsClient("wss://nas.example/api/current", 20, True, deadline_monotonic=10):
        pass
    assert attempts == []


def test_deadline_bounds_connect_and_prevents_late_send(monkeypatch):
    now = [9]
    socket = Socket()
    kwargs = {}
    monkeypatch.setattr(transport.time, "monotonic", lambda: now[0])

    def connect(*_args, **options):
        kwargs.update(options)
        return socket

    monkeypatch.setattr(transport, "create_connection", connect)
    with transport.JsonRpcWsClient("wss://nas.example/api/current", 20, True, deadline_monotonic=10) as client:
        now[0] = 11
        with pytest.raises(TimeoutError):
            client.call("system.state")
    assert kwargs["timeout"] == 1
    assert socket.sent == []


@pytest.mark.parametrize(
    ("response", "diagnostic"),
    [
        ({"response_type": "AUTH_ERR"}, "AUTH_ERR"),
        ({"response_type": "OTP_REQUIRED"}, "OTP_REQUIRED"),
        ({}, "UNKNOWN"),
        (True, "UNKNOWN"),
        ({"response_type": "unsafe value synthetic-secret"}, "UNKNOWN"),
    ],
)
def test_modern_auth_requires_explicit_success_with_safe_diagnostic(
    monkeypatch, response, diagnostic
):
    socket = Socket(response)
    monkeypatch.setattr(transport, "create_connection", lambda *a, **k: socket)
    with (
        transport.JsonRpcWsClient("wss://nas.example/api/current", 5, True) as client,
        pytest.raises(transport.JsonRpcError) as error,
    ):
        client.authenticate("synthetic-key", username="monitor")
    assert f"response_type={diagnostic}" in str(error.value)
    assert "synthetic-secret" not in str(error.value)
    assert len(socket.sent) == 1  # rejection must never downgrade to legacy auth


def test_modern_auth_uses_documented_mechanism(monkeypatch):
    socket = Socket(API27["auth.login_ex"])
    monkeypatch.setattr(transport, "create_connection", lambda *a, **k: socket)
    with transport.JsonRpcWsClient("wss://nas.example/api/current", 5, True) as client:
        client.authenticate("synthetic-key", username="monitor")
    request = socket.sent[0]
    assert request["method"] == "auth.login_ex"
    assert request["params"] == [{"mechanism": "API_KEY_PLAIN", "username": "monitor", "api_key": "synthetic-key", "login_options": {"user_info": False, "reconnect_token": False}}]


def test_snapshot_expiry_does_not_require_republication(monkeypatch):
    now = [100.0]
    monkeypatch.setattr(exporter_module.time, "monotonic", lambda: now[0])
    exporter = exporter_module.TrueNASExporter(make_config(event_stale_after_seconds=15))
    exporter._dispatch_event("reporting.realtime", {"cpu": {"cpu": {"usage": 25.0}}})
    exporter._publish_cached_events_to_default_registry()
    exporter._publish_metric_snapshot()
    collector = exporter_module.TrueNASCollector(exporter)

    def cpu():
        return next(s.value for f in collector.collect() for s in f.samples if s.name == "truenas_cpu_usage_percent")

    assert cpu() == 25
    now[0] = 116
    assert math.isnan(cpu())


def test_collector_events_publish_continuously_between_poll_cycles(monkeypatch):
    now = [100.0]
    monkeypatch.setattr(exporter_module.time, "monotonic", lambda: now[0])
    exporter = exporter_module.TrueNASExporter(make_config(event_stale_after_seconds=15))
    collector = exporter_module.TrueNASCollector(exporter)

    for step in range(9):
        now[0] = 100.0 + step * 2
        exporter._dispatch_event(
            "reporting.realtime", {"cpu": {"cpu": {"usage": 25 + step}}}
        )

    cpu = next(
        sample.value
        for family in collector.collect()
        for sample in family.samples
        if sample.name == "truenas_cpu_usage_percent"
    )
    assert cpu == 33
    assert exporter._snapshot_event_times["reporting.realtime"] == 116


def test_collector_event_publication_recovers_after_real_expiry(monkeypatch):
    now = [100.0]
    monkeypatch.setattr(exporter_module.time, "monotonic", lambda: now[0])
    exporter = exporter_module.TrueNASExporter(make_config(event_stale_after_seconds=15))
    collector = exporter_module.TrueNASCollector(exporter)

    def cpu():
        return next(
            sample.value
            for family in collector.collect()
            for sample in family.samples
            if sample.name == "truenas_cpu_usage_percent"
        )

    exporter._dispatch_event("reporting.realtime", {"cpu": {"cpu": {"usage": 25}}})
    assert cpu() == 25
    now[0] = 116
    assert math.isnan(cpu())
    exporter._dispatch_event("reporting.realtime", {"cpu": {"cpu": {"usage": 40}}})
    assert cpu() == 40


def test_event_snapshot_publication_is_bounded_and_shutdown_cancels_timer(monkeypatch):
    now = [100.0]
    timers = []

    class Timer:
        def __init__(self, delay, target):
            self.delay = delay
            self.target = target
            self.daemon = False
            self.started = False
            self.cancelled = False
            timers.append(self)

        def start(self):
            self.started = True

        def is_alive(self):
            return self.started and not self.cancelled

        def cancel(self):
            self.cancelled = True

    monkeypatch.setattr(exporter_module.time, "monotonic", lambda: now[0])
    monkeypatch.setattr(runtime.threading, "Timer", Timer)
    exporter = exporter_module.TrueNASExporter(make_config())
    exporter._dispatch_event("reporting.realtime", {"cpu": {"cpu": {"usage": 1}}})
    now[0] = 100.1
    exporter._dispatch_event("reporting.realtime", {"cpu": {"cpu": {"usage": 2}}})
    exporter._dispatch_event("reporting.realtime", {"cpu": {"cpu": {"usage": 3}}})

    assert len(timers) == 1
    assert timers[0].started and timers[0].daemon
    assert timers[0].delay == pytest.approx(0.9)
    assert exporter._collector_event_scalars["truenas_cpu_usage_percent"] == 3

    exporter.stop()
    assert timers[0].cancelled
    assert exporter._metric_snapshot_publish_timer is None


@pytest.mark.parametrize("method", ["vm.get_available_memory", "pool.query", "interface.query"])
@pytest.mark.parametrize("code", [-32601, -32001])
@pytest.mark.parametrize("mode", ["collector", "legacy"])
def test_failed_source_does_not_hide_later_services(monkeypatch, method, code, mode):
    class API:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        def authenticate(self, key, call=None):
            pass

        def call(self, name, params=None):
            if name == method:
                raise transport.JsonRpcError("synthetic source failure", code=code)
            if name == "system.version_short":
                return "25.10.2"
            if name == "service.query":
                return [{"service": "cifs", "enable": True, "state": "RUNNING"}]
            if name.endswith(".query"):
                return 0 if params and len(params) > 1 and params[1].get("count") else []
            return None

    monkeypatch.setattr(runtime, "JsonRpcWsClient", lambda **kwargs: API())
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode=mode))
    exporter.scrape_once()
    samples = {s.name: s.value for f in exporter.metric_snapshot() for s in f.samples if not s.labels}
    assert samples["truenas_service_count"] == 1
    assert samples["truenas_up"] == 0  # required source failure remains visible


@pytest.mark.parametrize("freeing", [0, 4096, None])
def test_pool_pending_free_bytes_uses_real_nullable_field(monkeypatch, freeing):
    class API:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        def authenticate(self, *args, **kwargs):
            pass

        def call(self, name, params=None):
            if name == "system.version_short":
                return API27[name]
            if name == "pool.query":
                assert "freeing" in params[1]["select"]
                return [{**API27[name][0], "freeing": freeing}]
            if name.endswith(".query"):
                return 0 if params and len(params) > 1 and params[1].get("count") else []
            return None

    monkeypatch.setattr(runtime, "JsonRpcWsClient", lambda **kwargs: API())
    exporter = exporter_module.TrueNASExporter(make_config())
    exporter.scrape_once()
    samples = [s for f in exporter.metric_snapshot() for s in f.samples if s.name == "truenas_pool_freeing_bytes"]
    assert [s.value for s in samples] == ([] if freeing is None else [freeing])
    assert any(s.value == 1 for f in exporter.metric_snapshot() for s in f.samples if s.name == "truenas_pool_count")


def test_query_timeout_is_never_retried(monkeypatch):
    calls = []

    class API:
        def call(self, method, params):
            calls.append(method)
            raise TimeoutError("budget exhausted")

    exporter = exporter_module.TrueNASExporter(make_config())
    with pytest.raises(TimeoutError):
        exporter._call_query_with_fallback(API(), "pool.query", {"select": ["name"]})
    assert calls == ["pool.query"]


def test_late_deadline_failure_marks_cycle_unhealthy_without_late_transport_calls(monkeypatch):
    now = [100.0]
    calls_after_deadline = []

    class API:
        def __init__(self, **kwargs):
            self.deadline = kwargs["deadline_monotonic"]

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return None

        def authenticate(self, _key, call=None, **_kwargs):
            return None

        def ensure_within_deadline(self, method):
            if now[0] >= self.deadline:
                raise TimeoutError(f"{method}: synthetic total scrape budget exhausted")

        def call(self, method, params=None):
            if now[0] >= self.deadline:
                calls_after_deadline.append(method)
                raise TimeoutError("synthetic total scrape budget exhausted")
            if method == "system.version_short":
                return "27.0.0-RC.1"
            if method == "update.status":
                now[0] += 26
                return {"status": {"new_version": None}}
            if method in {"system.state", "system.product_type"}:
                return "READY" if method == "system.state" else "SCALE"
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

    monkeypatch.setattr(runtime, "JsonRpcWsClient", API)
    monkeypatch.setattr(runtime.time, "monotonic", lambda: now[0])
    exporter = exporter_module.TrueNASExporter(make_config())

    exporter.scrape_once()

    samples = [sample for family in exporter.metric_snapshot() for sample in family.samples]
    assert next(sample.value for sample in samples if sample.name == "truenas_up") == 0
    assert exporter.is_ready() is False
    assert calls_after_deadline == []


@pytest.mark.parametrize(
    ("version", "smb", "expected"),
    [
        ("25.10.2", {"enable_smb1": True}, 1),
        ("25.10.2", {"enable_smb1": False}, 0),
        ("26.0.0", {"minimum_protocol": "SMB1"}, 1),
        ("26.0.0", {"minimum_protocol": "SMB2"}, 0),
        ("27.0.0-RC.1", {"minimum_protocol": "SMB3"}, 0),
        ("27.0.0-RC.1", {}, None),
        ("27.0.0-RC.1", {"minimum_protocol": None}, None),
        ("27.0.0-RC.1", {"minimum_protocol": 1}, None),
        ("27.0.0-RC.1", {"minimum_protocol": "UNKNOWN"}, None),
    ],
)
def test_smb1_metric_uses_versioned_source_without_fabricating_unknown(
    monkeypatch, version, smb, expected
):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy"))
    exporter.compatibility_profile = exporter._profile_for_version_short(version)

    def fake_call(_client, method, _params=None):
        if method == "service.query":
            return []
        if method == "smb.config":
            return smb
        raise transport.JsonRpcError("synthetic optional source unavailable", code=-32601)

    monkeypatch.setattr(exporter, "_call", fake_call)
    exporter._reset_poll_metrics()
    exporter._collect_protocol_configs(object(), {})
    values = [
        sample.value
        for family in exporter_module.SMB1_ENABLED.collect()
        for sample in family.samples
    ]
    if expected is None:
        assert values and all(not math.isfinite(value) for value in values)
    else:
        assert values == [expected]


def test_smb1_metric_stays_unknown_when_smb_config_fails(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy"))
    exporter.compatibility_profile = exporter._profile_for_version_short("27.0.0-RC.1")

    def fake_call(_client, method, _params=None):
        if method == "service.query":
            return []
        raise transport.JsonRpcError("synthetic unavailable", code=-32001)

    monkeypatch.setattr(exporter, "_call", fake_call)
    exporter._reset_poll_metrics()
    exporter._collect_protocol_configs(object(), {})
    values = [
        sample.value
        for family in exporter_module.SMB1_ENABLED.collect()
        for sample in family.samples
    ]
    assert values and all(not math.isfinite(value) for value in values)


def test_config_repr_redacts_api_key():
    assert "test-key" not in repr(make_config())


@pytest.mark.parametrize("release", ["27.0.0", "27.0.0-RC.1", "TrueNAS-SCALE-27.0.0", "27.0.1"])
def test_explicit_27_profile_suppresses_removed_sources(release):
    exporter = exporter_module.TrueNASExporter(make_config())
    profile = exporter._profile_for_version_short(release)
    assert profile.name == "27.0"
    assert profile.allows_method("pool.query")
    assert not profile.allows_method("virt.instance.query")
    assert not profile.allows_method("vm.device.pptdev_choices")
    assert profile.allows_event("container.metrics")


def test_generic_wide_object_is_bounded_at_exposition():
    exporter = exporter_module.TrueNASExporter(make_config(enable_generic_method_metrics=True, max_generic_series=3))
    exporter._extract_generic_metrics("system.info", {f"field_{n}": n for n in range(100)}, "result", 0)
    exporter._publish_metric_snapshot()
    samples = [s for f in exporter.metric_snapshot() for s in f.samples if s.name == "truenas_method_numeric_value"]
    assert len(samples) == 3
    assert {s.value for s in samples} == {0, 1, 2}


def test_generic_events_share_one_bounded_budget():
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", enable_generic_event_metrics=True, max_generic_series=3))
    exporter._dispatch_event("reporting.realtime", {"cpu": {"cpu": {"usage": 1, "idle": 99}}})
    exporter._dispatch_event("app.stats", {"fields": [{"app_name": "demo", "cpu_usage": 2}]})
    exporter._publish_metric_snapshot()
    samples = [s for f in exporter.metric_snapshot() for s in f.samples if s.name.startswith("truenas_event_") and "path" in s.labels]
    assert 0 < len(samples) <= 3


@pytest.mark.parametrize("field", ["disls", "disks"])
def test_disk_only_event_accepts_both_documented_and_compatibility_spellings(field):
    exporter = exporter_module.TrueNASExporter(make_config())
    exporter._dispatch_event("reporting.realtime", {field: {"demo": {"read_bytes": 42}}})
    exporter._publish_cached_events_to_default_registry()
    exporter._publish_metric_snapshot()
    assert any(s.value == 42 for f in exporter.metric_snapshot() for s in f.samples if s.name == "truenas_disk_read_bytes_per_second")


def test_stale_event_exposition_does_not_wait_for_poll_lock(monkeypatch):
    now = [100.0]
    monkeypatch.setattr(exporter_module.time, "monotonic", lambda: now[0])
    exporter = exporter_module.TrueNASExporter(make_config(event_stale_after_seconds=15))
    exporter._dispatch_event("reporting.realtime", {"cpu": {"cpu": {"usage": 25}}})
    exporter._publish_cached_events_to_default_registry()
    exporter._publish_metric_snapshot()
    locked, release, collected = threading.Event(), threading.Event(), threading.Event()

    def poll():
        with exporter._lock:
            locked.set()
            release.wait(2)

    def collect():
        try:
            values.extend(s.value for f in exporter_module.TrueNASCollector(exporter).collect() for s in f.samples if s.name == "truenas_cpu_usage_percent")
        finally:
            collected.set()

    values = []
    worker = threading.Thread(target=poll)
    worker.start()
    assert locked.wait(1)
    now[0] = 116
    reader = threading.Thread(target=collect)
    reader.start()
    try:
        assert collected.wait(1), "exposition blocked on polling lock"
        assert len(values) == 1 and math.isnan(values[0])
    finally:
        release.set()
        worker.join(2)
        reader.join(2)


def test_rpc_errors_do_not_expose_server_error_data(monkeypatch):
    socket = Socket()
    socket.recv = lambda: json.dumps({"id": 1, "error": {"code": -32001, "message": "synthetic-secret-value", "data": {"api_key": "synthetic-secret-value"}}})
    monkeypatch.setattr(transport, "create_connection", lambda *a, **k: socket)
    with transport.JsonRpcWsClient("wss://nas.example/api/current", 5, True) as client, pytest.raises(transport.JsonRpcError) as error:
        client.call("system.info")
    assert error.value.code == -32001
    assert "synthetic-secret-value" not in str(error.value)


def test_authentication_rejection_stops_all_telemetry(monkeypatch):
    socket = Socket(False)
    monkeypatch.setattr(transport, "create_connection", lambda *a, **k: socket)
    exporter = exporter_module.TrueNASExporter(make_config())
    exporter.scrape_once()
    assert [call["method"] for call in socket.sent] == ["auth.login_with_api_key"]
    assert any(s.value == 0 for f in exporter.metric_snapshot() for s in f.samples if s.name == "truenas_up")
