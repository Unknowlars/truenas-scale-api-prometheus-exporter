import truenas_exporter as exporter_module


def make_config(**overrides):
    values = {
        "ws_url": "wss://truenas.example/api/current",
        "api_key": "test-key",
        "interval_seconds": 30,
        "timeout_seconds": 20,
        "verify_tls": True,
        "exporter_port": 9108,
        "auto_discover_methods": False,
        "query_limit": 200,
        "max_method_calls": 250,
        "max_list_items": 200,
        "max_depth": 6,
        "max_entity_calls": 50,
        "max_datasets": 100,
        "extra_methods": [],
        "exclude_methods": [],
        "filesystem_paths": ["/mnt"],
        "enable_filesystem_listdir": False,
        "enable_event_streams": False,
        "enable_dataset_metrics": True,
        "enable_task_metrics": False,
        "enable_ipmi_metrics": False,
        "event_interval_seconds": 2,
        "event_read_timeout_seconds": 60,
        "event_subscriptions": ["reporting.realtime"],
        "scrape_all_metrics": False,
        "enable_generic_method_metrics": False,
        "enable_generic_event_metrics": False,
        "dataset_snapshot_fallback_limit": 0,
        "exporter_mode": "collector",
    }
    values.update(overrides)
    return exporter_module.Config(**values)


class FakeClient:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return None


def _family_by_name(families, name):
    for family in families:
        if family.name == name:
            return family
    raise AssertionError(f"missing family: {name}")


def _build_exporter(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config())
    monkeypatch.setattr(exporter_module, "JsonRpcWsClient", lambda **_: FakeClient())
    return exporter


def test_collector_mode_returns_fresh_families_without_stale_pool_series(monkeypatch):
    exporter = _build_exporter(monkeypatch)

    state = {"round": 0}

    def fake_call(_client, method, params=None):
        if method == "auth.login_with_api_key":
            return True
        if method == "system.state":
            return "READY"
        if method == "system.info":
            return {"hostname": "nas", "version": "TrueNAS-25.10.2", "product_type": "SCALE"}
        if method == "pool.dataset.query":
            return []
        if method == "alert.list":
            return []
        raise AssertionError(f"unexpected call {method} {params}")

    def fake_query_with_fallback(_client, method, _preferred):
        if method == "pool.query":
            if state["round"] == 0:
                return [{"name": "tank", "healthy": True, "status": "ONLINE", "size": 100.0, "allocated": 20.0, "free": 80.0}]
            return []
        if method == "service.query":
            return []
        raise AssertionError(f"unexpected query {method}")

    monkeypatch.setattr(exporter, "_call", fake_call)
    monkeypatch.setattr(exporter, "_call_query_with_fallback", fake_query_with_fallback)

    collector = exporter_module.TrueNASCollector(exporter)

    first = list(collector.collect())
    first_pool_size = _family_by_name(first, "truenas_pool_size_bytes")
    assert any(sample.labels.get("pool") == "tank" for sample in first_pool_size.samples)

    state["round"] = 1
    second = list(collector.collect())
    second_pool_size = _family_by_name(second, "truenas_pool_size_bytes")
    assert second_pool_size.samples == []


def test_collector_mode_exposes_up_and_scrape_duration(monkeypatch):
    exporter = _build_exporter(monkeypatch)

    def fake_call(_client, method, params=None):
        if method == "auth.login_with_api_key":
            return True
        if method == "system.state":
            return "READY"
        if method == "system.info":
            return {"hostname": "nas", "version": "TrueNAS-25.10.2", "product_type": "SCALE"}
        if method == "pool.dataset.query":
            return []
        if method == "alert.list":
            return []
        raise AssertionError(f"unexpected call {method} {params}")

    monkeypatch.setattr(exporter, "_call", fake_call)
    monkeypatch.setattr(exporter, "_call_query_with_fallback", lambda *_: [])

    families = list(exporter_module.TrueNASCollector(exporter).collect())
    up_family = _family_by_name(families, "truenas_up")
    duration_family = _family_by_name(families, "truenas_scrape_duration_seconds")

    assert up_family.samples and up_family.samples[0].value == 1.0
    assert duration_family.samples and duration_family.samples[0].value >= 0.0


def test_exporter_mode_toggle_supports_legacy_and_collector(monkeypatch):
    monkeypatch.setenv("TRUENAS_WS_URL", "wss://nas.example/api/current")
    monkeypatch.setenv("TRUENAS_API_KEY", "secret")

    monkeypatch.setenv("EXPORTER_MODE", "legacy")
    assert exporter_module._load_config().exporter_mode == "legacy"

    monkeypatch.setenv("EXPORTER_MODE", "collector")
    assert exporter_module._load_config().exporter_mode == "collector"


def test_collector_mode_core_metric_names_are_stable(monkeypatch):
    exporter = _build_exporter(monkeypatch)

    def fake_call(_client, method, params=None):
        if method == "auth.login_with_api_key":
            return True
        if method == "system.state":
            return "READY"
        if method == "system.info":
            return {
                "hostname": "nas",
                "version": "TrueNAS-25.10.2",
                "product_type": "SCALE",
                "uptime_seconds": 100.0,
                "physmem": 1024.0,
                "cores": 8,
                "physical_cores": 4,
            }
        if method == "pool.dataset.query":
            return [{"name": "tank/data", "used": 1.0, "available": 2.0, "referenced": 1.0, "quota": 0.0, "refquota": 0.0, "snapshot_count": 3}]
        if method == "alert.list":
            return [{"level": "WARNING", "source": "SMART", "klass": "DiskTemp", "node": "A"}]
        raise AssertionError(f"unexpected call {method} {params}")

    def fake_query_with_fallback(_client, method, _preferred):
        if method == "pool.query":
            return [{"name": "tank", "healthy": True, "status": "ONLINE", "size": 100.0, "allocated": 20.0, "free": 80.0}]
        if method == "service.query":
            return [{"service": "ssh", "enable": True, "state": {"running": True}}]
        raise AssertionError(f"unexpected query {method}")

    monkeypatch.setattr(exporter, "_call", fake_call)
    monkeypatch.setattr(exporter, "_call_query_with_fallback", fake_query_with_fallback)

    exporter._dispatch_event(
        "reporting.realtime",
        {
            "cpu": {"cpu": {"usage": 33.0, "per_cpu": [10.0, 20.0]}},
            "memory": {"physical_memory_total": 1000, "physical_memory_available": 400},
            "disls": {"read_bytes": 10, "write_bytes": 20, "read_ops": 1, "write_ops": 2, "busy": 3},
            "interfaces": {"eth0": {"received_bytes_rate": 100, "sent_bytes_rate": 200}},
            "pools": {"tank": {"read_bytes_per_second": 11, "write_bytes_per_second": 22}},
        },
    )

    names = {family.name for family in exporter_module.TrueNASCollector(exporter).collect()}
    expected = {
        "truenas_up",
        "truenas_scrape_duration_seconds",
        "truenas_system_state",
        "truenas_system_ready",
        "truenas_pool_count",
        "truenas_pool_size_bytes",
        "truenas_dataset_count",
        "truenas_dataset_used_bytes",
        "truenas_service_count",
        "truenas_service_running",
        "truenas_alert_count",
        "truenas_alert_count_by_level",
        "truenas_cpu_usage_percent",
        "truenas_memory_physical_total_bytes",
        "truenas_disk_read_bytes_per_second",
        "truenas_network_rx_bytes_per_second",
        "truenas_pool_realtime_read_bytes_per_second",
    }
    assert expected.issubset(names)


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

    def fake_make_server(host, port, app, handler_class):
        captured["http_app"] = app
        return FakeServer()

    monkeypatch.setattr(exporter_module, "make_wsgi_app", fake_make_wsgi_app)
    monkeypatch.setattr(exporter_module, "make_server", fake_make_server)
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
