import signal
import sys
from types import SimpleNamespace

import pytest
from conftest import make_config
from websocket import WebSocketTimeoutException

import truenas_exporter as exporter_module

runtime = sys.modules[exporter_module.TrueNASExporter.__module__]


class _CallClient:
    def __init__(self, result=None, error=None):
        self.result = result
        self.error = error
        self.calls = []

    def call(self, method, params=None):
        self.calls.append((method, params))
        if self.error is not None:
            raise self.error
        return self.result


class _BootstrapClient:
    def __init__(self, *version_results):
        self.version_results = list(version_results)
        self.calls = []

    def authenticate(self, _key, call=None):
        if call is not None:
            call("auth.login_with_api_key", ["redacted-test-key"])

    def call(self, method, params=None):
        self.calls.append((method, params))
        if method == "auth.login_with_api_key":
            return True
        if method == "system.version_short":
            result = self.version_results.pop(0)
            if isinstance(result, Exception):
                raise result
            return result
        return True


def test_call_diagnostics_fallback_and_count(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config())
    client = _CallClient(result=3)

    assert exporter._call(client, "disk.query", []) == 3
    assert exporter._api_call_success["disk.query"] == 1
    assert exporter._query_count(client, "disk.query", [["name", "!=", ""]]) == 3

    failing = _CallClient(error=RuntimeError("unsupported options"))
    calls = []

    def fallback_call(_client, method, params=None):
        calls.append((method, params))
        if len(calls) == 1:
            raise RuntimeError("unsupported options")
        return ["ok"]

    monkeypatch.setattr(exporter, "_call", fallback_call)
    assert exporter._call_query_with_fallback(failing, "pool.query", {"select": ["name"]}) == ["ok"]
    assert calls == [
        ("pool.query", [[], {"select": ["name"]}]),
        ("pool.query", []),
    ]

    calls.clear()
    with pytest.raises(RuntimeError, match="unsupported options"):
        exporter._call_query_with_fallback(
            failing,
            "disk.query",
            {"select": ["name"]},
            allow_bare_fallback=False,
        )
    assert calls == [("disk.query", [[], {"select": ["name"]}])]

    monkeypatch.setattr(exporter, "_call", lambda *_args, **_kwargs: {})
    with pytest.raises(TypeError):
        exporter._query_count(client, "disk.query")

    broken = _CallClient(error=ValueError("boom"))
    with pytest.raises(ValueError):
        runtime.TrueNASExporter._call(exporter, broken, "pool.query")
    assert exporter._api_call_success["pool.query"] == 0
    assert exporter._api_call_errors[("pool.query", "ValueError")] == 1


def test_bootstrap_failure_does_not_downgrade_detected_concrete_profile():
    exporter = exporter_module.TrueNASExporter(make_config())
    client = _BootstrapClient("25.10.2", RuntimeError("temporary version failure"))

    assert exporter._bootstrap_connection(client) == "25.10.2"
    assert exporter.compatibility_profile.name == "25.10"

    assert exporter._bootstrap_connection(client) is None

    assert exporter.compatibility_profile.name == "25.10"
    assert exporter._collector_errors["version_detection"] == 1


def test_bootstrap_concrete_profile_change_clears_auto_skipped_methods():
    exporter = exporter_module.TrueNASExporter(make_config())
    client = _BootstrapClient("25.10.2", "26.0.0")

    assert exporter._bootstrap_connection(client) == "25.10.2"
    exporter._auto_skipped_methods.add("pool.dataset.query")

    assert exporter._bootstrap_connection(client) == "26.0.0"

    assert exporter.compatibility_profile.name == "26.0"
    assert exporter._auto_skipped_methods == set()


def test_first_bootstrap_failure_still_selects_unknown_profile():
    exporter = exporter_module.TrueNASExporter(make_config())
    client = _BootstrapClient(RuntimeError("version unavailable"))

    assert exporter._bootstrap_connection(client) is None

    assert exporter.compatibility_profile.name == "unknown"
    assert exporter._collector_errors["version_detection"] == 1


def test_timestamp_status_and_generic_extractors_cover_edge_shapes():
    exporter = exporter_module.TrueNASExporter(make_config(max_depth=2, max_list_items=2))

    assert exporter._extract_snapshot_creation_timestamp(None) is None
    assert exporter._extract_snapshot_creation_timestamp({"creation": 12}) == 12
    assert exporter._extract_snapshot_creation_timestamp({"properties": {"creation": 13}}) == 13
    assert exporter._extract_snapshot_creation_timestamp({}) is None
    assert exporter._extract_smart_test_timestamp(None) is None
    assert exporter._extract_smart_test_timestamp({"timestamp": {"parsed": 14}}) == 14
    assert exporter._extract_smart_test_timestamp({"created": "2026-01-01T00:00:00Z"}) is not None
    assert exporter._extract_smart_test_timestamp({}) is None
    assert exporter._status_like("READY")
    assert not exporter._status_like("")
    assert not exporter._status_like("X" * 41)
    assert not exporter._status_like("ARBITRARY")

    value = {
        "boolean": True,
        "number": 2,
        "numeric_string": "3.5",
        "status": "online",
        "ignored": "free text",
        "items": [False, {"nested": 4}, 99],
    }
    exporter._extract_generic_metrics("demo.query", value, "result", 0)
    exporter._extract_generic_metrics("demo.query", value, "result", 3)
    exporter._replace_generic_event_metrics("demo.event", value)


def test_event_cache_expiry_dispatch_and_snapshot(monkeypatch):
    exporter = exporter_module.TrueNASExporter(
        make_config(exporter_mode="collector", enable_generic_event_metrics=True)
    )
    exporter._dispatch_event(
        "reporting.realtime",
        {
            "cpu": {"cpu": {"percent": 25, "system": 5, "iowait": 1, "interrupt": 2,
                              "per_cpu": {"0": 20}, "temperatures": {"0": 45}}},
            "memory": {"total": 100, "available": 60, "free": 20, "cached": 10,
                       "buffers": 5, "swap_total": 20, "swap_free": 15,
                       "arc_size": 8, "arc_free_memory": 3, "arc_available_memory": 4},
            "disks": {"sda": {"read_bytes": 1, "write_bytes": 2, "read_ops": 3,
                                "write_ops": 4, "busy": 5}},
            "interfaces": {"eth0": {"received_bytes": 6, "sent_bytes": 7}},
            "pools": {"tank": {"read_bytes_per_second": 8, "write_bytes_per_second": 9}},
        },
    )
    exporter._dispatch_event(
        "app.stats",
        {"fields": [None, {"app_name": "demo", "cpu": 1, "memory": 2,
                           "networks": [None, {"interface_name": "eth0", "rx_bytes": 3, "tx_bytes": 4}],
                           "blkio": {"read": 5, "write": 6}}]},
    )
    exporter._dispatch_event(
        "virt.instance.metrics",
        {"fields": [None, {"name": "vm", "cpu_usage": 7, "memory_usage": 8}]},
    )
    snapshot = {"scalar": {}, "series": {}}
    exporter._merge_event_snapshot(snapshot)
    assert snapshot["scalar"]
    assert snapshot["series"]

    monkeypatch.setattr(runtime.time, "monotonic", lambda: 1_000_000_000_000.0)
    exporter._expire_stale_events(force=True)
    stale = {"scalar": {}, "series": {}}
    exporter._merge_event_snapshot(stale)
    assert not stale["scalar"]

    legacy = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy"))
    legacy._dispatch_event("app.stats", {"fields": []})
    legacy._expire_stale_events(force=True)


class _EventClient:
    instances = []

    def __init__(self, messages, fail_subscription=False, subscribe_result="sub-1"):
        self.messages = iter(messages)
        self.fail_subscription = fail_subscription
        self.subscribe_result = subscribe_result
        self.calls = []
        self.__class__.instances.append(self)

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return None

    def authenticate(self, _key, call=None):
        if call is not None:
            call("auth.login_with_api_key", ["redacted-test-key"])

    def call(self, method, params=None):
        self.calls.append((method, params))
        if method == "auth.login_with_api_key":
            return True
        if method == "system.version_short":
            return "25.10.2"
        if self.fail_subscription:
            raise RuntimeError("subscription failed")
        if method == "core.subscribe":
            return self.subscribe_result
        if method == "core.unsubscribe":
            return True
        return True

    def recv_json(self):
        value = next(self.messages)
        if isinstance(value, Exception):
            raise value
        return value


def test_event_stream_filters_messages_and_stops(monkeypatch):
    exporter = exporter_module.TrueNASExporter(
        make_config(enable_event_streams=True, event_subscriptions=["reporting.realtime"])
    )
    messages = [
        WebSocketTimeoutException(),
        {"method": "notice"},
        {"method": "collection_update", "params": []},
        {"method": "collection_update", "params": {"collection": "other", "fields": {}}},
        {"method": "collection_update", "params": {
            "collection": "reporting.realtime", "fields": {"cpu": {"percent": 1}}
        }},
    ]
    client = _EventClient(messages)
    monkeypatch.setattr(runtime, "JsonRpcWsClient", lambda **_kwargs: client)
    original_dispatch = exporter._dispatch_event

    def dispatch_and_stop(collection, payload):
        original_dispatch(collection, payload)
        exporter.stop()

    monkeypatch.setattr(exporter, "_dispatch_event", dispatch_and_stop)
    exporter._event_stream_loop()
    assert exporter._event_message_counts["reporting.realtime"] == 1
    assert ("core.unsubscribe", ["sub-1"]) in client.calls
    assert exporter._collector_event_stream_up["reporting.realtime"] == 0


def test_event_stream_subscription_failure_and_thread_guards(monkeypatch):
    exporter = exporter_module.TrueNASExporter(
        make_config(enable_event_streams=True, event_subscriptions=["app.stats"])
    )
    client = _EventClient([], fail_subscription=True)
    monkeypatch.setattr(runtime, "JsonRpcWsClient", lambda **_kwargs: client)
    monkeypatch.setattr(exporter._stop_event, "wait", lambda _seconds: True)
    exporter._event_stream_loop()
    assert exporter._collector_event_stream_up["app.stats"] == 0

    disabled = exporter_module.TrueNASExporter(make_config(enable_event_streams=False))
    disabled._ensure_event_thread()
    assert disabled._event_thread is None
    disabled._event_thread = SimpleNamespace(is_alive=lambda: True)
    disabled.config = make_config(enable_event_streams=True)
    disabled._ensure_event_thread()


def test_event_stream_rejects_invalid_subscription_ids(monkeypatch):
    exporter = exporter_module.TrueNASExporter(
        make_config(enable_event_streams=True, event_subscriptions=["app.stats"])
    )
    client = _EventClient([], subscribe_result=True)
    monkeypatch.setattr(runtime, "JsonRpcWsClient", lambda **_kwargs: client)
    monkeypatch.setattr(exporter._stop_event, "wait", lambda _seconds: True)

    exporter._event_stream_loop()

    assert exporter._collector_event_stream_up["app.stats"] == 0
    assert ("core.unsubscribe", [True]) not in client.calls
    assert exporter._collector_errors["event_subscribe"] == 1


def test_event_stream_cleanup_unsubscribes_and_clears_cached_series(monkeypatch):
    exporter = exporter_module.TrueNASExporter(
        make_config(enable_event_streams=True, event_subscriptions=["app.stats"])
    )
    exporter._dispatch_event("app.stats", {"fields": [{"app_name": "demo", "cpu_usage": 1}]})
    assert exporter._collector_event_series[exporter_module.APP_CPU_PERCENT._name]

    client = _EventClient([RuntimeError("connection dropped")])
    monkeypatch.setattr(runtime, "JsonRpcWsClient", lambda **_kwargs: client)
    monkeypatch.setattr(exporter._stop_event, "wait", lambda _seconds: True)

    exporter._event_stream_loop()

    assert ("core.unsubscribe", ["sub-1"]) in client.calls
    assert exporter._collector_event_stream_up["app.stats"] == 0
    assert exporter_module.APP_CPU_PERCENT._name not in exporter._collector_event_series
    assert "app.stats" not in exporter._event_last_monotonic


def test_event_stream_v25_virt_subscription_is_tracked_and_unsubscribed(monkeypatch):
    exporter = exporter_module.TrueNASExporter(
        make_config(enable_event_streams=True, event_subscriptions=["virt.instance.metrics"])
    )
    client = _EventClient([])
    monkeypatch.setattr(runtime, "JsonRpcWsClient", lambda **_kwargs: client)
    monkeypatch.setattr(exporter._stop_event, "wait", lambda _seconds: True)

    exporter._event_stream_loop()

    assert ("core.subscribe", ["virt.instance.metrics"]) in client.calls
    assert ("core.unsubscribe", ["sub-1"]) in client.calls
    assert exporter._collector_event_stream_up["virt.instance.metrics"] == 0


class _Server:
    def __init__(self):
        self.shutdown_calls = 0

    def shutdown(self):
        self.shutdown_calls += 1


@pytest.mark.parametrize("mode", ["collector", "legacy"])
def test_main_lifecycle_for_both_modes(monkeypatch, mode):
    config = make_config(exporter_mode=mode)
    server = _Server()
    captured = {}

    class FakeExporter:
        def __init__(self, received):
            assert received is config
            self._lock = object()
            self._stop_event = SimpleNamespace(wait=lambda: None)
            self._event_thread = None
            self._scrape_thread = None
            self.run_calls = 0
            self.stop_calls = 0
            captured["exporter"] = self

        def metric_snapshot(self):
            return ()

        def is_ready(self):
            return True

        def _ensure_event_thread(self):
            return None

        def run_forever(self):
            self.run_calls += 1

        def stop(self):
            self.stop_calls += 1

    class ImmediateThread:
        def __init__(self, target, **_kwargs):
            self.target = target

        def start(self):
            self.target()

        def join(self, timeout=None):
            captured["join_timeout"] = timeout

    handlers = {}
    monkeypatch.setattr(runtime, "_load_config", lambda: config)
    monkeypatch.setattr(runtime, "TrueNASExporter", FakeExporter)
    monkeypatch.setattr(runtime, "_start_http_server", lambda *_args, **_kwargs: server)
    monkeypatch.setattr(runtime.threading, "Thread", ImmediateThread)
    monkeypatch.setattr(runtime.signal, "signal", lambda sig, handler: handlers.setdefault(sig, handler))
    runtime.main()
    handlers[signal.SIGTERM](signal.SIGTERM, None)

    assert server.shutdown_calls == 1
    assert captured["exporter"].stop_calls == 2
    assert captured["exporter"].run_calls == 1


def test_run_forever_stops_after_first_wait(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config())
    calls = []
    monkeypatch.setattr(exporter, "_ensure_event_thread", lambda: calls.append("events"))
    monkeypatch.setattr(exporter, "scrape_once", lambda: calls.append("scrape"))
    monkeypatch.setattr(exporter._stop_event, "wait", lambda _seconds: True)
    exporter.run_forever()
    assert calls == ["events", "scrape"]


def test_collector_describe_and_collect():
    exporter = exporter_module.TrueNASExporter(make_config())
    collector = runtime.TrueNASCollector(exporter)
    assert collector.describe() == []
    assert tuple(collector.collect()) == exporter.metric_snapshot()


def test_method_safety_auto_params_and_discovery(monkeypatch):
    exporter = exporter_module.TrueNASExporter(
        make_config(
            auto_discover_methods=True,
            extra_methods=["custom.status", "custom.status"],
            exclude_methods=["disk.query"],
            query_limit=7,
            max_method_calls=500,
        )
    )
    assert not exporter._is_safe_read_method("disk.query")
    assert not exporter._is_safe_read_method("pool.dataset.get_instance")
    assert not exporter._is_safe_read_method("vmware.query")
    assert not exporter._is_safe_read_method("filesystem.stat")
    assert not exporter._is_safe_read_method("auth.login")
    assert not exporter._is_safe_read_method("pool.delete")
    assert exporter._is_safe_read_method("system.ready")
    assert not exporter._is_safe_read_method("custom.status")
    assert not exporter._is_safe_read_method("custom.mystery")

    assert exporter._auto_params("pool.query") == [[], {"limit": 7}]
    assert exporter._auto_params("core.get_jobs") == [[], {"limit": 7}]
    assert exporter._auto_params("app.query")[1]["limit"] == 7
    assert exporter._auto_params("reporting.graph") == ["cpu", {"unit": "HOURLY"}]
    assert exporter._auto_params("system.info") == []
    assert exporter._should_runtime_skip_method(RuntimeError("missing required argument: id"))
    assert not exporter._should_runtime_skip_method(RuntimeError("connection reset"))

    monkeypatch.setattr(
        exporter,
        "_safe_call_auto",
        lambda _client, method: {
            "system.ready": {},
            "custom.status": {},
            "unsafe.create": {},
            3: {},
        } if method == "core.get_methods" else None,
    )
    methods = exporter._discover_methods(object())
    assert "system.ready" in methods
    assert "custom.status" not in methods
    assert "unsafe.create" not in methods


def test_safe_call_auto_does_not_retry_without_safe_query_options(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config())
    calls = []

    def query_retry(_client, method, params=None):
        calls.append((method, params))
        if params:
            raise RuntimeError("temporary")
        return ["fallback"]

    monkeypatch.setattr(exporter, "_call", query_retry)
    assert exporter._safe_call_auto(object(), "pool.query") is None
    assert calls == [("pool.query", [[], {"limit": 200}])]

    monkeypatch.setattr(exporter, "_call", lambda *_args, **_kwargs: (_ for _ in ()).throw(RuntimeError("broken")))
    assert exporter._safe_call_auto(object(), "system.info") is None
    assert exporter._safe_call_auto(object(), "pool.query") is None


def test_dynamic_discovery_filters_mutations_and_handles_failure():
    exporter = exporter_module.TrueNASExporter(make_config(scrape_all_metrics=True))
    client = _CallClient(result={
        "dns.query": {},
        "system.info": {},
        "demo.create": {},
        "demo.update": {},
        "demo.delete": {},
        "demo.set_value": {},
        "demo.do_work": {},
        "auth.me": {},
        "user.has_local_administrator_set_up": {},
    })
    exporter._discover_all_methods(client)
    assert exporter._all_methods_discovered
    assert "dns.query" not in exporter.config.extra_methods  # already a base method
    assert "system.info" not in exporter.config.extra_methods  # already a base method
    assert "user.has_local_administrator_set_up" in exporter.config.extra_methods
    assert "demo.create" not in exporter.config.extra_methods
    before = list(exporter.config.extra_methods)
    exporter._discover_all_methods(client)
    assert exporter.config.extra_methods == before

    failed = exporter_module.TrueNASExporter(make_config(scrape_all_metrics=True))
    failed._discover_all_methods(_CallClient(error=RuntimeError("unavailable")))
    assert not failed._all_methods_discovered
    disabled = exporter_module.TrueNASExporter(make_config(scrape_all_metrics=False))
    disabled._discover_all_methods(client)
    assert not disabled._all_methods_discovered


def test_graph_selection_and_reporting_collection(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(enable_generic_method_metrics=True))
    assert exporter._extract_graph_names([{"name": " cpu "}, "disk", None, {}]) == ["cpu", "disk"]
    assert exporter._extract_graph_names({"arc": {"name": "memory"}, "": {}}) == ["arc", "memory"]
    assert exporter._extract_graph_names(None) == []
    assert exporter._pick_graphs(["other-long", "cpu", "zfs"], limit=2) == [
        {"name": "cpu"}, {"name": "zfs"}
    ]
    monkeypatch.setattr(exporter, "_safe_call_auto", lambda _client, method: [method] if method.endswith("graphs") else None)
    cache = {}
    exporter._collect_reporting_timeseries(object(), cache)
    assert set(cache) == {"reporting.netdata_graphs", "reporting.graphs"}

    disabled = exporter_module.TrueNASExporter(make_config(enable_generic_method_metrics=False))
    disabled._collect_reporting_timeseries(object(), {})


def test_readiness_snapshot_stop_and_interval(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(event_interval_seconds=1))
    assert not exporter.is_ready()
    exporter._last_scrape_success_monotonic = 100
    monkeypatch.setattr(runtime.time, "monotonic", lambda: 110)
    assert exporter.is_ready()
    monkeypatch.setattr(runtime.time, "monotonic", lambda: 1_000)
    assert not exporter.is_ready()
    assert exporter._event_interval_seconds() == 2
    assert exporter._format_event_subscription("reporting.realtime") == "reporting.realtime"
    exporter.config = make_config(event_interval_seconds=5)
    assert '"interval": 5' in exporter._format_event_subscription("reporting.realtime")
    assert exporter._format_event_subscription("other.event") == "other.event"
    exporter._publish_metric_snapshot()
    assert exporter.metric_snapshot()
    exporter.stop()
    assert exporter._stop_event.is_set()


def test_service_enable_map_empty_and_defensive_records(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config())
    assert exporter._query_service_enable_map(object(), ("", "")) == {}
    monkeypatch.setattr(
        exporter,
        "_call",
        lambda *_args, **_kwargs: [None, {}, {"name": "ssh", "enable": "yes"}, {"service": "", "enable": True}],
    )
    assert exporter._query_service_enable_map(object(), ("ssh", "ssh", "")) == {"ssh": True}


def test_event_thread_start_and_series_replacement(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(enable_event_streams=True))
    started = []

    class FakeThread:
        def __init__(self, target, name, daemon):
            started.append((target, name, daemon))

        def start(self):
            started.append("started")

        def is_alive(self):
            return False

    monkeypatch.setattr(runtime.threading, "Thread", FakeThread)
    exporter._ensure_event_thread()
    assert started[-1] == "started"

    class Metric:
        def __init__(self):
            self.removed = []
            self.values = {}

        def remove(self, *labels):
            self.removed.append(labels)

        def labels(self, *labels):
            return SimpleNamespace(set=lambda value: self.values.setdefault(labels, value))

    metric = Metric()
    exporter._event_metric_series[metric] = {("old",)}
    exporter._replace_event_metric_series(metric, {("new",): 2})
    assert metric.removed == [("old",)]
    assert metric.values[("new",)] == 2
