import pytest

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
        "enable_event_streams": True,
        "enable_dataset_metrics": True,
        "enable_task_metrics": True,
        "enable_ipmi_metrics": True,
        "event_interval_seconds": 2,
        "event_read_timeout_seconds": 60,
        "event_subscriptions": ["reporting.realtime"],
        "scrape_all_metrics": False,
    }
    values.update(overrides)
    return exporter_module.Config(**values)


def gauge_value(gauge):
    return gauge._value.get()


def reset_metric(metric):
    if getattr(metric, "_labelnames", ()):  # pragma: no branch
        metric.clear()
    else:
        metric.set(0)


@pytest.fixture(autouse=True)
def reset_gauges():
    for metric in (
        exporter_module.SNAPSHOT_TOTAL_COUNT,
        exporter_module.SNAPSHOT_OLDEST_TS,
        exporter_module.DATASET_USED_BYTES,
        exporter_module.DATASET_REFERENCED_BYTES,
        exporter_module.DATASET_SNAPSHOT_COUNT,
        exporter_module.BOOT_ENV_SIZE_BYTES,
        exporter_module.CERT_DAYS_TO_EXPIRY,
        exporter_module.SSH_ENABLED,
        exporter_module.SSH_PASSWORD_AUTH,
        exporter_module.FTP_ENABLED,
        exporter_module.SNMP_ENABLED,
        exporter_module.REPORTING_ENABLED,
        exporter_module.LOCAL_USER_COUNT,
        exporter_module.LOCAL_GROUP_COUNT,
        exporter_module.STATIC_ROUTE_COUNT,
        exporter_module.TUNABLE_COUNT,
        exporter_module.PRIVILEGE_COUNT,
        exporter_module.INITSHUTDOWNSCRIPT_COUNT,
        exporter_module.KEYCHAIN_CREDENTIAL_COUNT,
        exporter_module.ISCSI_TARGET_COUNT,
        exporter_module.ISCSI_PORTAL_COUNT,
        exporter_module.ISCSI_EXTENT_COUNT,
        exporter_module.ISCSI_INITIATOR_COUNT,
        exporter_module.NVMET_HOST_COUNT,
        exporter_module.NVMET_NAMESPACE_COUNT,
        exporter_module.DOCKER_IMAGE_COUNT,
        exporter_module.DNS_RESOLVER_COUNT,
        exporter_module.REPORTING_EXPORTER_COUNT,
        exporter_module.NETWORK_HTTPPROXY_CONFIGURED,
        exporter_module.REPLICATION_MAX_PARALLEL,
    ):
        reset_metric(metric)


def test_snapshot_count_uses_exact_count_query(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config())
    calls = []

    def fake_call(client, method, params=None):
        calls.append((method, params))
        assert method == "pool.snapshot.query"
        options = params[1]
        if options.get("count"):
            return 321
        return []

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_snapshot_metrics(object(), {})

    assert gauge_value(exporter_module.SNAPSHOT_TOTAL_COUNT) == 321
    assert calls[0][1][1] == {"count": True}


def test_oldest_snapshot_timestamp_uses_ordered_exact_query(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config())
    calls = []

    def fake_call(client, method, params=None):
        calls.append((method, params))
        options = params[1]
        if options.get("count"):
            return 4
        return [{"creation_parsed": 1700000000}]

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_snapshot_metrics(object(), {})

    assert gauge_value(exporter_module.SNAPSHOT_OLDEST_TS) == 1700000000
    oldest_options = calls[1][1][1]
    assert oldest_options["limit"] == 1
    assert oldest_options["order_by"] == ["properties.creation.parsed"]
    assert oldest_options["select"] == [["properties.creation.parsed", "creation_parsed"]]


def test_dataset_metrics_request_parsed_properties_and_snapshot_fallback(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config())
    calls = []

    def fake_call(client, method, params=None):
        calls.append((method, params))
        if method == "pool.dataset.query":
            return [{"name": "tank/data", "used": 123.0, "available": 456.0, "referenced": 78.0}]
        if method == "pool.dataset.snapshot_count":
            assert params == ["tank/data"]
            return 9
        raise AssertionError(f"Unexpected call: {method} {params}")

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_dataset_metrics(object())

    dataset_options = calls[0][1][1]
    assert dataset_options["extra"]["properties"] == [
        "used",
        "available",
        "referenced",
        "quota",
        "refquota",
        "compressratio",
    ]
    assert dataset_options["select"] == [
        "name",
        ["used.parsed", "used"],
        ["available.parsed", "available"],
        ["referenced.parsed", "referenced"],
        ["quota.parsed", "quota"],
        ["refquota.parsed", "refquota"],
        ["compressratio.parsed", "compressratio"],
        "encrypted",
    ]
    assert exporter_module.DATASET_USED_BYTES.labels(dataset="tank/data")._value.get() == 123.0
    assert exporter_module.DATASET_REFERENCED_BYTES.labels(dataset="tank/data")._value.get() == 78.0
    assert exporter_module.DATASET_SNAPSHOT_COUNT.labels(dataset="tank/data")._value.get() == 9.0


def test_boot_env_metrics_use_used_bytes_field(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config())
    calls = []

    def fake_call(client, method, params=None):
        calls.append((method, params))
        assert method == "boot.environment.query"
        return [{"id": "default", "active": True, "keep": True, "used_bytes": 2048}]

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_boot_env_metrics(object(), {})

    assert calls[0][1][1]["select"] == ["id", "active", "activated", "keep", "created", "used_bytes"]
    assert exporter_module.BOOT_ENV_SIZE_BYTES.labels(name="default")._value.get() == 2048.0


def test_certificate_metrics_do_not_request_undocumented_issuer_field(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config())
    calls = []

    def fake_call(client, method, params=None):
        calls.append((method, params))
        assert method == "certificate.query"
        return [{"name": "ui_cert", "organization": "Example Org", "until": "2099-01-01T00:00:00+00:00", "CSR": None}]

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_certificate_metrics(object())

    assert calls[0][1][1]["select"] == ["name", "organization", "common", "until", "CSR"]
    assert exporter_module.CERT_DAYS_TO_EXPIRY.labels(name="ui_cert", issuer="Example Org")._value.get() > 0


def test_inventory_collectors_accept_numeric_count_results(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config())

    counts = {
        "user.query": 11,
        "group.query": 12,
        "staticroute.query": 13,
        "tunable.query": 14,
        "privilege.query": 15,
        "initshutdownscript.query": 16,
        "keychaincredential.query": 17,
        "iscsi.target.query": 21,
        "iscsi.portal.query": 22,
        "iscsi.extent.query": 23,
        "iscsi.initiator.query": 24,
        "nvmet.host.query": 31,
        "nvmet.namespace.query": 32,
        "app.image.query": 41,
        "dns.query": 42,
        "reporting.exporters.query": 43,
    }

    def fake_call(client, method, params=None):
        if method in counts:
            assert params[1] == {"count": True}
            return counts[method]
        if method == "network.configuration.config":
            return {"httpproxy": ""}
        if method == "replication.config.config":
            return {"max_parallel_replication_tasks": 6}
        if method == "service.query":
            return [{"service": "netdata", "enable": False}]
        raise AssertionError(f"Unexpected call: {method} {params}")

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_inventory_counts(object(), {})
    exporter._collect_iscsi_inventory(object(), {})
    exporter._collect_nvmet_extended(object(), {})
    exporter._collect_misc_configs(object(), {})

    assert gauge_value(exporter_module.LOCAL_USER_COUNT) == 11
    assert gauge_value(exporter_module.LOCAL_GROUP_COUNT) == 12
    assert gauge_value(exporter_module.STATIC_ROUTE_COUNT) == 13
    assert gauge_value(exporter_module.TUNABLE_COUNT) == 14
    assert gauge_value(exporter_module.PRIVILEGE_COUNT) == 15
    assert gauge_value(exporter_module.INITSHUTDOWNSCRIPT_COUNT) == 16
    assert gauge_value(exporter_module.KEYCHAIN_CREDENTIAL_COUNT) == 17
    assert gauge_value(exporter_module.ISCSI_TARGET_COUNT) == 21
    assert gauge_value(exporter_module.ISCSI_PORTAL_COUNT) == 22
    assert gauge_value(exporter_module.ISCSI_EXTENT_COUNT) == 23
    assert gauge_value(exporter_module.ISCSI_INITIATOR_COUNT) == 24
    assert gauge_value(exporter_module.NVMET_HOST_COUNT) == 31
    assert gauge_value(exporter_module.NVMET_NAMESPACE_COUNT) == 32
    assert gauge_value(exporter_module.DOCKER_IMAGE_COUNT) == 41
    assert gauge_value(exporter_module.DNS_RESOLVER_COUNT) == 42
    assert gauge_value(exporter_module.REPORTING_EXPORTER_COUNT) == 43


def test_enabled_gauges_follow_service_enable_state(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config())

    def fake_call(client, method, params=None):
        if method == "service.query":
            requested = tuple(params[0][0][2])
            if requested == ("ssh", "ftp", "snmp"):
                return [
                    {"service": "ssh", "enable": False},
                    {"service": "ftp", "enable": True},
                    {"service": "snmp", "enable": False},
                ]
            if requested == ("netdata", "reporting"):
                return [{"service": "netdata", "enable": True}]
        if method == "smb.config":
            return {"multichannel": False}
        if method == "nfs.config":
            return {"v4": True, "servers": 8}
        if method == "ssh.config":
            return {"passwordauth": False}
        if method == "network.configuration.config":
            return {"httpproxy": ""}
        if method == "app.image.query":
            return 0
        if method == "replication.config.config":
            return {"max_parallel_replication_tasks": 2}
        if method == "reporting.exporters.query":
            return 0
        if method == "dns.query":
            return 1
        raise AssertionError(f"Unexpected call: {method} {params}")

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_protocol_configs(object(), {})
    exporter._collect_misc_configs(object(), {})

    assert gauge_value(exporter_module.SSH_ENABLED) == 0
    assert gauge_value(exporter_module.SSH_PASSWORD_AUTH) == 0
    assert gauge_value(exporter_module.FTP_ENABLED) == 1
    assert gauge_value(exporter_module.SNMP_ENABLED) == 0
    assert gauge_value(exporter_module.REPORTING_ENABLED) == 1


def test_load_config_parses_defaults_and_lists(monkeypatch):
    for key in (
        "TRUENAS_WS_URL",
        "TRUENAS_API_KEY",
        "TRUENAS_VERIFY_TLS",
        "FILESYSTEM_PATHS",
        "EXTRA_METHODS",
        "EVENT_SUBSCRIPTIONS",
        "ENABLE_EVENT_STREAMS",
    ):
        monkeypatch.delenv(key, raising=False)

    monkeypatch.setenv("TRUENAS_WS_URL", "wss://nas.example/api/current")
    monkeypatch.setenv("TRUENAS_API_KEY", "secret")
    monkeypatch.setenv("TRUENAS_VERIFY_TLS", "no")
    monkeypatch.setenv("FILESYSTEM_PATHS", "/mnt/data, /mnt/backups")
    monkeypatch.setenv("EXTRA_METHODS", "foo.query, bar.config")
    monkeypatch.setenv("EVENT_SUBSCRIPTIONS", "service.query,reporting.realtime")
    monkeypatch.setenv("ENABLE_EVENT_STREAMS", "0")

    config = exporter_module._load_config()

    assert config.ws_url == "wss://nas.example/api/current"
    assert config.api_key == "secret"
    assert config.verify_tls is False
    assert config.filesystem_paths == ["/mnt/data", "/mnt/backups"]
    assert config.extra_methods == ["foo.query", "bar.config"]
    assert config.event_subscriptions == ["service.query", "reporting.realtime"]
    assert config.enable_event_streams is False
    assert config.query_limit == 200
    assert config.exporter_port == 9108


@pytest.mark.parametrize(
    ("env", "message"),
    [
        ({}, "TRUENAS_WS_URL is required"),
        ({"TRUENAS_WS_URL": "wss://nas.example/api/current"}, "TRUENAS_API_KEY is required"),
    ],
)
def test_load_config_requires_mandatory_env(monkeypatch, env, message):
    monkeypatch.delenv("TRUENAS_WS_URL", raising=False)
    monkeypatch.delenv("TRUENAS_API_KEY", raising=False)
    for key, value in env.items():
        monkeypatch.setenv(key, value)

    with pytest.raises(ValueError, match=message):
        exporter_module._load_config()
