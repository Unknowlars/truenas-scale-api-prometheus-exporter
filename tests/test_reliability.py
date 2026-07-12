import math

import pytest
from conftest import make_config

import truenas_exporter as exporter_module


def _scalar_sample(families, name):
    family = next(family for family in families if family.name == name)
    assert family.samples
    return family.samples[0].value


def test_collector_realtime_zero_replaces_previous_value():
    exporter = exporter_module.TrueNASExporter(make_config())

    exporter._dispatch_event("reporting.realtime", {"cpu": {"cpu": {"usage": 50.0}}})
    exporter._dispatch_event("reporting.realtime", {"cpu": {"cpu": {"usage": 0.0}}})

    assert exporter._collector_event_scalars[exporter_module.CPU_USAGE_PERCENT._name] == 0.0
    assert exporter._collector_event_scalars[exporter_module.CPU_USER_PERCENT._name] == 0.0
    assert exporter._collector_event_scalars[exporter_module.CPU_IDLE_PERCENT._name] == 100.0


def test_legacy_app_and_vm_zero_values_are_exported():
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy"))

    exporter._dispatch_event("app.stats", {"fields": [{"app_name": "demo", "cpu_usage": 0.0}]})
    exporter._dispatch_event("virt.instance.metrics", {"fields": [{"name": "vm", "cpu": 0.0, "memory": 0.0}]})

    assert exporter_module.APP_CPU_PERCENT.labels(app="demo")._value.get() == 0.0
    assert exporter_module.VIRT_INSTANCE_CPU.labels(name="vm")._value.get() == 0.0
    assert exporter_module.VIRT_INSTANCE_MEM.labels(name="vm")._value.get() == 0.0


def test_collector_omits_expired_event_metrics(monkeypatch):
    now = {"value": 100.0}
    monkeypatch.setattr(exporter_module.time, "monotonic", lambda: now["value"])
    exporter = exporter_module.TrueNASExporter(make_config(event_stale_after_seconds=15))
    exporter._dispatch_event("reporting.realtime", {"cpu": {"cpu": {"usage": 25.0}}})

    fresh = {"scalar": {}, "series": {}}
    exporter._merge_event_snapshot(fresh)
    assert fresh["scalar"][exporter_module.CPU_USAGE_PERCENT._name] == 25.0

    now["value"] = 116.0
    stale = {"scalar": {}, "series": {}}
    exporter._merge_event_snapshot(stale)
    assert exporter_module.CPU_USAGE_PERCENT._name not in stale["scalar"]


def test_readiness_requires_recent_success(monkeypatch):
    now = {"value": 100.0}
    monkeypatch.setattr(exporter_module.time, "monotonic", lambda: now["value"])
    exporter = exporter_module.TrueNASExporter(make_config())
    assert exporter.is_ready() is False

    exporter._last_scrape_success_monotonic = 100.0
    assert exporter.is_ready() is True
    now["value"] = 200.0
    assert exporter.is_ready() is False


def test_load_config_supports_api_key_file(monkeypatch, tmp_path):
    key_file = tmp_path / "api-key"
    key_file.write_text("secret-from-file\n", encoding="utf-8")
    monkeypatch.setenv("TRUENAS_WS_URL", "wss://nas.example/api/current")
    monkeypatch.delenv("TRUENAS_API_KEY", raising=False)
    monkeypatch.setenv("TRUENAS_API_KEY_FILE", str(key_file))

    config = exporter_module._load_config()

    assert config.api_key == "secret-from-file"


def test_load_config_supports_custom_ca_file(monkeypatch, tmp_path):
    ca_file = tmp_path / "ca.pem"
    ca_file.write_text("test-ca", encoding="utf-8")
    monkeypatch.setenv("TRUENAS_WS_URL", "wss://nas.example/api/current")
    monkeypatch.setenv("TRUENAS_API_KEY", "secret")
    monkeypatch.setenv("TRUENAS_CA_FILE", str(ca_file))

    assert exporter_module._load_config().ca_file == str(ca_file)


def test_load_config_rejects_invalid_url_and_boolean(monkeypatch):
    monkeypatch.setenv("TRUENAS_WS_URL", "https://nas.example/api/current")
    monkeypatch.setenv("TRUENAS_API_KEY", "secret")
    with pytest.raises(ValueError, match="ws:// or wss://"):
        exporter_module._load_config()

    monkeypatch.setenv("TRUENAS_WS_URL", "wss://nas.example/api/current")
    monkeypatch.setenv("TRUENAS_VERIFY_TLS", "sometimes")
    with pytest.raises(ValueError, match="TRUENAS_VERIFY_TLS must be a boolean"):
        exporter_module._load_config()


def test_load_config_rejects_event_ttl_shorter_than_interval(monkeypatch):
    monkeypatch.setenv("TRUENAS_WS_URL", "wss://nas.example/api/current")
    monkeypatch.setenv("TRUENAS_API_KEY", "secret")
    monkeypatch.setenv("EVENT_INTERVAL_SECONDS", "30")
    monkeypatch.setenv("EVENT_STALE_AFTER_SECONDS", "15")
    with pytest.raises(ValueError, match="must be >="):
        exporter_module._load_config()


def test_busy_event_path_expires_silent_subscription(monkeypatch):
    now = {"value": 100.0}
    monkeypatch.setattr(exporter_module.time, "monotonic", lambda: now["value"])
    exporter = exporter_module.TrueNASExporter(
        make_config(exporter_mode="legacy", event_subscriptions=["app.stats", "reporting.realtime"])
    )
    with exporter._lock:
        exporter._dispatch_event("app.stats", {"fields": [{"app_name": "demo", "cpu_usage": 1.0}]})
    now["value"] = 116.0
    with exporter._lock:
        exporter._expire_stale_events()
        exporter._dispatch_event("reporting.realtime", {"cpu": {"cpu": {"usage": 2.0}}})
    assert "app.stats" in exporter._expired_events

@pytest.mark.parametrize(
    ("environment", "message"),
    [
        ({"TRUENAS_API_KEY": "", "TRUENAS_API_KEY_FILE": "/missing/key"}, "cannot be read"),
        ({"TRUENAS_CA_FILE": "/missing/ca"}, "does not exist"),
        ({"FILESYSTEM_PATHS": "relative/path"}, "must be absolute"),
        ({"EXPORTER_MODE": "other"}, "must be either"),
    ],
)
def test_load_config_rejects_invalid_paths_and_mode(monkeypatch, environment, message):
    monkeypatch.setenv("TRUENAS_WS_URL", "wss://nas.example/api/current")
    monkeypatch.setenv("TRUENAS_API_KEY", "secret")
    for name, value in environment.items():
        monkeypatch.setenv(name, value)

    with pytest.raises(ValueError, match=message):
        exporter_module._load_config()


@pytest.mark.parametrize(
    ("name", "value"),
    [
        ("EXPORTER_PORT", "0"),
        ("SCRAPE_INTERVAL_SECONDS", "-1"),
        ("SCRAPE_BUDGET_SECONDS", "invalid"),
        ("MAX_DATASETS", "0"),
    ],
)
def test_load_config_rejects_invalid_numeric_values(monkeypatch, name, value):
    monkeypatch.setenv("TRUENAS_WS_URL", "wss://nas.example/api/current")
    monkeypatch.setenv("TRUENAS_API_KEY", "secret")
    monkeypatch.setenv(name, value)

    with pytest.raises(ValueError, match=name):
        exporter_module._load_config()


def test_jsonrpc_client_enforces_total_deadline(monkeypatch):
    client = exporter_module.JsonRpcWsClient(
        "ws://nas.example/api/current",
        timeout_seconds=20,
        verify_tls=True,
        deadline_monotonic=10.0,
    )

    class FakeSocket:
        def send(self, _payload):
            return None

        def recv(self):
            raise AssertionError("recv must not run after the deadline")

    client._ws = FakeSocket()
    monkeypatch.setattr(exporter_module.time, "monotonic", lambda: 11.0)

    with pytest.raises(TimeoutError, match="budget exhausted"):
        client.call("system.info")


def test_counter_metric_families_use_prometheus_total_suffix(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config())
    exporter_module.API_CALL_ERRORS_TOTAL.labels(method="system.info", error_type="TimeoutError").inc(2)
    exporter_module.COLLECTOR_ERRORS_TOTAL.labels(collector="system").inc()
    exporter_module.EVENT_MESSAGES_TOTAL.labels(event="reporting.realtime").inc(3)
    exporter._publish_metric_snapshot()

    families = list(exporter_module.TrueNASCollector(exporter).collect())
    samples = {sample.name: sample.value for family in families for sample in family.samples}

    assert samples["truenas_api_call_errors_total"] == 2.0
    assert samples["truenas_collector_errors_total"] == 1.0
    assert samples["truenas_event_messages_total"] == 3.0
    assert all(
        not math.isnan(samples[name])
        for name in (
            "truenas_api_call_errors_total",
            "truenas_collector_errors_total",
            "truenas_event_messages_total",
        )
    )
