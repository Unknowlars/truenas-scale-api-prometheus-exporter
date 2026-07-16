import sys

from conftest import make_config

import truenas_exporter as exporter_module

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


def test_start_http_server_legacy_uses_default_registry_and_lock(monkeypatch):
    captured = _capture_http_stack(monkeypatch)
    lock = _CountingLock()

    exporter_module._start_http_server(9108, lock, registry=None, lock_metrics=True)

    status_codes = []

    def start_response(status, _headers):
        status_codes.append(status)

    body = captured["http_app"]({"PATH_INFO": "/metrics"}, start_response)

    assert captured["make_wsgi_kwargs"] == {}
    assert body == [b"metrics\n"]
    assert status_codes and status_codes[0] == "200 OK"
    assert lock.enter_count == 1


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


def test_link_state_enums_are_mapped_explicitly():
    assert exporter_module._link_is_up("LINK_STATE_UP") is True
    assert exporter_module._link_is_up("LINK_STATE_DOWN") is False
