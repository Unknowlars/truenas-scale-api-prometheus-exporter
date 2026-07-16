import sys

from conftest import make_config

import truenas_exporter as exporter_module

runtime = sys.modules[exporter_module.TrueNASExporter.__module__]
http_module = sys.modules[exporter_module._start_http_server.__module__]


class FakeClient:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return None

    def authenticate(self, api_key, call=None):
        if call is not None:
            call("auth.login_with_api_key", [api_key])


def _family_by_name(families, name):
    for family in families:
        if family.name == name:
            return family
    raise AssertionError(f"missing family: {name}")


def _sample_value(families, family_name, labels=None):
    expected = labels or {}
    family = _family_by_name(families, family_name)
    for sample in family.samples:
        if sample.name == family_name and dict(sample.labels) == expected:
            return sample.value
    raise AssertionError(f"missing sample: {family_name}{expected}")


def _has_sample(families, family_name, labels=None):
    expected = labels or {}
    try:
        family = _family_by_name(families, family_name)
    except AssertionError:
        return False
    return any(
        sample.name == family_name and dict(sample.labels) == expected
        for sample in family.samples
    )


def _build_exporter(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config())
    monkeypatch.setattr(exporter_module, "JsonRpcWsClient", lambda **_: FakeClient())
    return exporter


def test_exporter_mode_toggle_supports_legacy_and_collector(monkeypatch):
    monkeypatch.setenv("TRUENAS_WS_URL", "wss://nas.example/api/current")
    monkeypatch.setenv("TRUENAS_API_KEY", "secret")

    monkeypatch.setenv("EXPORTER_MODE", "legacy")
    assert exporter_module._load_config().exporter_mode == "legacy"

    monkeypatch.setenv("EXPORTER_MODE", "collector")
    assert exporter_module._load_config().exporter_mode == "collector"


class _CountingLock:
    def __init__(self):
        self.enter_count = 0

    def __enter__(self):
        self.enter_count += 1
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


def _capture_http_stack(monkeypatch):
    captured = {}

    def fake_make_wsgi_app(*args, **kwargs):
        captured["make_wsgi_kwargs"] = kwargs

        def metrics_app(environ, start_response):
            captured["metrics_called"] = True
            start_response("200 OK", [("Content-Type", "text/plain; charset=utf-8")])
            return [b"metrics\n"]

        return metrics_app

    class FakeServer:
        def serve_forever(self):
            return

    def fake_make_server(host, port, app, handler_class, server_class=None):
        captured["http_app"] = app
        captured["server_class"] = server_class
        return FakeServer()

    monkeypatch.setattr(http_module, "make_wsgi_app", fake_make_wsgi_app)
    monkeypatch.setattr(http_module, "make_server", fake_make_server)
    return captured


def test_start_http_server_legacy_can_use_snapshot_registry_without_lock(monkeypatch):
    captured = _capture_http_stack(monkeypatch)
    lock = _CountingLock()
    registry = exporter_module.CollectorRegistry(auto_describe=True)

    exporter_module._start_http_server(9108, lock, registry=registry, lock_metrics=False)

    status_codes = []

    def start_response(status, _headers):
        status_codes.append(status)

    body = captured["http_app"]({"PATH_INFO": "/metrics"}, start_response)

    assert captured["make_wsgi_kwargs"].get("registry") is registry
    assert body == [b"metrics\n"]
    assert status_codes and status_codes[0] == "200 OK"
    assert lock.enter_count == 0


def test_start_http_server_collector_uses_custom_registry_without_lock(monkeypatch):
    captured = _capture_http_stack(monkeypatch)
    lock = _CountingLock()
    registry = exporter_module.CollectorRegistry(auto_describe=True)

    exporter_module._start_http_server(9108, lock, registry=registry, lock_metrics=False)

    status_codes = []

    def start_response(status, _headers):
        status_codes.append(status)

    body = captured["http_app"]({"PATH_INFO": "/metrics"}, start_response)

    assert captured["make_wsgi_kwargs"].get("registry") is registry
    assert body == [b"metrics\n"]
    assert status_codes and status_codes[0] == "200 OK"
    assert lock.enter_count == 0


def test_main_legacy_registers_snapshot_registry_without_lock(monkeypatch):
    captured = {}

    class FakeExporter:
        def __init__(self):
            self._lock = _CountingLock()
            self._event_thread = None
            self._scrape_thread = None
            self.ran_forever = False

        def metric_snapshot(self):
            return ()

        def is_ready(self):
            return True

        def run_forever(self):
            self.ran_forever = True

        def stop(self):
            return None

    fake_exporter = FakeExporter()

    def fake_start_http_server(port, lock, **kwargs):
        captured["port"] = port
        captured["lock"] = lock
        captured.update(kwargs)

        class FakeServer:
            def shutdown(self):
                return None

        return FakeServer()

    monkeypatch.setattr(runtime, "_load_config", lambda: make_config(exporter_mode="legacy"))
    monkeypatch.setattr(runtime, "TrueNASExporter", lambda _config: fake_exporter)
    monkeypatch.setattr(runtime, "_start_http_server", fake_start_http_server)
    monkeypatch.setattr(runtime.signal, "signal", lambda *_args: None)

    runtime.main()

    assert captured["lock"] is fake_exporter._lock
    assert captured["lock_metrics"] is False
    assert captured["readiness_check"]() is True
    assert captured["registry"] is not None
    assert fake_exporter.ran_forever is True


def test_legacy_event_dispatch_republishes_metrics_snapshot(monkeypatch):
    captured = {}

    def fake_make_server(host, port, app, handler_class, server_class=None):
        captured["http_app"] = app

        class FakeServer:
            def serve_forever(self):
                return

        return FakeServer()

    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy"))
    registry = exporter_module.CollectorRegistry(auto_describe=False)
    registry.register(exporter_module.TrueNASCollector(exporter))
    exporter_module.POOL_REALTIME_USED_BYTES.clear()
    exporter._publish_metric_snapshot()
    timer_delays = []

    class FakeTimer:
        daemon = False

        def __init__(self, delay, callback):
            self.delay = delay
            self.callback = callback
            timer_delays.append(delay)

        def is_alive(self):
            return False

        def cancel(self):
            return None

        def start(self):
            self.callback()

    monkeypatch.setattr(http_module, "make_server", fake_make_server)
    monkeypatch.setattr(runtime.threading, "Timer", FakeTimer)
    exporter_module._start_http_server(
        9108,
        exporter._lock,
        registry=registry,
        lock_metrics=False,
        readiness_check=exporter.is_ready,
    )

    exporter._dispatch_event(
        "reporting.realtime",
        {"pools": {"tank": {"used": 123}}},
    )

    responses = []
    body = b"".join(
        captured["http_app"](
            {"PATH_INFO": "/metrics", "REQUEST_METHOD": "GET", "QUERY_STRING": ""},
            lambda status, headers: responses.append((status, headers)),
        )
    )

    assert responses[0][0] == "200 OK"
    assert len(timer_delays) == 1
    assert 0 <= timer_delays[0] <= 1
    assert b'truenas_pool_realtime_used_bytes{pool="tank"} 123.0' in body
    exporter_module.POOL_REALTIME_USED_BYTES.clear()


def test_http_auxiliary_endpoints_without_socket_binding(monkeypatch):
    captured = _capture_http_stack(monkeypatch)
    ready = {"value": False}
    exporter_module._start_http_server(
        9108,
        _CountingLock(),
        readiness_check=lambda: ready["value"],
    )

    def request(path):
        responses = []
        body = captured["http_app"](
            {"PATH_INFO": path},
            lambda status, headers: responses.append((status, headers)),
        )
        return responses[0][0], body

    assert request("/") == ("200 OK", [http_module._LANDING_PAGE])
    assert request("/healthz") == ("200 OK", [b"ok\n"])
    assert request("/readyz") == ("503 Service Unavailable", [b"not ready\n"])
    ready["value"] = True
    assert request("/readyz") == ("200 OK", [b"ready\n"])


def test_full_parity_collector_exposes_declared_metric_families(monkeypatch):
    from scripts.generate_metric_contract import build_contract

    exporter = exporter_module.TrueNASExporter(make_config())
    monkeypatch.setattr(exporter, "scrape_once", lambda: None)

    family_names = {
        family.name for family in exporter_module.TrueNASCollector(exporter).collect()
    }
    contract = build_contract()
    expected = {
        metric["name"].removesuffix("_total")
        if metric["type"] == "counter"
        else metric["name"]
        for metric in contract["metrics"]
    }

    assert expected <= family_names


def test_full_parity_collector_never_scrapes_on_request(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config())
    monkeypatch.setattr(exporter, "scrape_once", lambda: (_ for _ in ()).throw(AssertionError("scrape")))
    assert list(exporter_module.TrueNASCollector(exporter).collect())


def test_collector_snapshot_keeps_polled_metrics_on_pre_auth_failure(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="collector"))
    labels = {"pool": "tank", "status": "ONLINE"}
    exporter_module.POOL_STATUS.clear()
    exporter_module.POOL_STATUS.labels(**labels).set(1)
    exporter_module.SCRAPE_SUCCESS.set(1)
    exporter._publish_metric_snapshot()

    def fail_connect(**_kwargs):
        raise RuntimeError("connection refused")

    monkeypatch.setattr(runtime, "JsonRpcWsClient", fail_connect)

    exporter.scrape_once()
    snapshot = exporter.metric_snapshot()

    assert _sample_value(snapshot, exporter_module.POOL_STATUS._name, labels) == 1
    assert _sample_value(snapshot, exporter_module.SCRAPE_SUCCESS._name) == 0

    exporter_module.POOL_STATUS.clear()


def test_collector_snapshot_wipes_stale_polled_metrics_on_pre_auth_failure(monkeypatch):
    exporter = exporter_module.TrueNASExporter(
        make_config(exporter_mode="collector", interval_seconds=30)
    )
    labels = {"pool": "tank", "status": "ONLINE"}
    exporter_module.POOL_STATUS.clear()
    exporter_module.POOL_STATUS.labels(**labels).set(1)
    exporter._last_scrape_success_monotonic = 0
    exporter._publish_metric_snapshot()

    def fail_connect(**_kwargs):
        raise RuntimeError("connection refused")

    monkeypatch.setattr(runtime, "JsonRpcWsClient", fail_connect)
    monkeypatch.setattr(runtime.time, "monotonic", lambda: 301)

    exporter.scrape_once()
    snapshot = exporter.metric_snapshot()

    assert not _has_sample(snapshot, exporter_module.POOL_STATUS._name, labels)
    assert _sample_value(snapshot, exporter_module.SCRAPE_SUCCESS._name) == 0


def test_link_state_enums_are_mapped_explicitly():
    assert exporter_module._link_is_up("LINK_STATE_UP") is True
    assert exporter_module._link_is_up("LINK_STATE_DOWN") is False
