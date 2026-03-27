import time

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
        "event_subscriptions": ["reporting.realtime", "app.stats", "virt.instance.metrics"],
        "scrape_all_metrics": False,
    }
    values.update(overrides)
    return exporter_module.Config(**values)


def reset_metric(metric):
    if getattr(metric, "_labelnames", ()):  # pragma: no branch
        metric.clear()
    else:
        metric.set(0)


def labeled_value(metric, *label_values):
    return metric._metrics[label_values]._value.get()


@pytest.fixture(autouse=True)
def reset_phase2_metrics():
    for metric in (
        exporter_module.EVENT_LAST_MESSAGE_TS,
        exporter_module.APP_CPU_PERCENT,
        exporter_module.APP_MEMORY_BYTES,
        exporter_module.APP_NET_RX_BYTES_RATE,
        exporter_module.APP_NET_TX_BYTES_RATE,
        exporter_module.APP_BLKIO_READ_BYTES,
        exporter_module.APP_BLKIO_WRITE_BYTES,
        exporter_module.VIRT_INSTANCE_CPU,
        exporter_module.VIRT_INSTANCE_MEM,
        exporter_module.CPU_CORE_USAGE_PERCENT,
        exporter_module.CPU_TEMPERATURE_C,
        exporter_module.DISK_READ_BYTES_RATE,
        exporter_module.DISK_WRITE_BYTES_RATE,
        exporter_module.DISK_READ_OPS_RATE,
        exporter_module.DISK_WRITE_OPS_RATE,
        exporter_module.DISK_BUSY_PERCENT,
        exporter_module.NETWORK_RX_BYTES_RATE,
        exporter_module.NETWORK_TX_BYTES_RATE,
        exporter_module.POOL_REALTIME_READ_BYTES,
        exporter_module.POOL_REALTIME_WRITE_BYTES,
    ):
        reset_metric(metric)


def test_load_config_defaults_include_documented_event_streams(monkeypatch):
    for key in ("TRUENAS_WS_URL", "TRUENAS_API_KEY", "EVENT_SUBSCRIPTIONS"):
        monkeypatch.delenv(key, raising=False)

    monkeypatch.setenv("TRUENAS_WS_URL", "wss://nas.example/api/current")
    monkeypatch.setenv("TRUENAS_API_KEY", "secret")

    config = exporter_module._load_config()

    assert "reporting.realtime" in config.event_subscriptions
    assert "app.stats" in config.event_subscriptions
    assert "virt.instance.metrics" in config.event_subscriptions
    assert "container.metrics" not in config.event_subscriptions


def test_event_subscription_formatting_handles_documented_interval_events():
    exporter = exporter_module.TrueNASExporter(make_config(event_interval_seconds=7))

    assert exporter._format_event_subscription("reporting.realtime") == 'reporting.realtime:{"interval": 7}'
    assert exporter._format_event_subscription("app.stats") == 'app.stats:{"interval": 7}'
    assert exporter._format_event_subscription("virt.instance.metrics") == 'virt.instance.metrics:{"interval": 7}'
    assert exporter._format_event_subscription("pool.query") == "pool.query"

    clamped = exporter_module.TrueNASExporter(make_config(event_interval_seconds=1))
    assert clamped._event_interval_seconds() == 2
    assert clamped._format_event_subscription("virt.instance.metrics") == "virt.instance.metrics"


def test_dispatch_routes_virt_instance_metrics_to_dedicated_handler(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config())
    calls = []

    def fake_handle(payload):
        calls.append(("virt", payload))

    def fake_extract(event, payload):
        calls.append(("generic", event, payload))

    monkeypatch.setattr(exporter, "_handle_virt_metrics_event", fake_handle)
    monkeypatch.setattr(exporter, "_replace_generic_event_metrics", fake_extract)

    payload = {"fields": [{"name": "vm1", "cpu_usage": 12.5}]}
    before = time.time()
    exporter._dispatch_event("virt.instance.metrics", payload)

    assert calls == [
        ("virt", payload),
        ("generic", "virt.instance.metrics", payload),
    ]
    assert labeled_value(exporter_module.EVENT_LAST_MESSAGE_TS, "virt.instance.metrics") >= before


def test_app_stats_event_removes_stale_app_and_interface_series():
    exporter = exporter_module.TrueNASExporter(make_config())

    exporter._handle_app_stats_event(
        {
            "fields": [
                {
                    "app_name": "plex",
                    "cpu_usage": 12.5,
                    "memory": 100,
                    "networks": [{"interface_name": "eth0", "rx_bytes": 10, "tx_bytes": 20}],
                    "blkio": {"read": 30, "write": 40},
                },
                {
                    "app_name": "nextcloud",
                    "cpu_usage": 22.5,
                    "memory": 200,
                    "networks": [{"interface_name": "eth1", "rx_bytes": 50, "tx_bytes": 60}],
                    "blkio": {"read": 70, "write": 80},
                },
            ]
        }
    )

    assert labeled_value(exporter_module.APP_CPU_PERCENT, "plex") == 12.5
    assert labeled_value(exporter_module.APP_NET_RX_BYTES_RATE, "nextcloud", "eth1") == 50

    exporter._handle_app_stats_event(
        {
            "fields": [
                {
                    "app_name": "plex",
                    "cpu_usage": 33.0,
                    "memory": 300,
                    "networks": [{"interface_name": "eth2", "rx_bytes": 15, "tx_bytes": 25}],
                    "blkio": {"read": 35, "write": 45},
                }
            ]
        }
    )

    assert labeled_value(exporter_module.APP_CPU_PERCENT, "plex") == 33.0
    assert ("nextcloud",) not in exporter_module.APP_CPU_PERCENT._metrics
    assert ("nextcloud",) not in exporter_module.APP_MEMORY_BYTES._metrics
    assert ("plex", "eth0") not in exporter_module.APP_NET_RX_BYTES_RATE._metrics
    assert ("nextcloud", "eth1") not in exporter_module.APP_NET_TX_BYTES_RATE._metrics
    assert ("plex", "eth2") in exporter_module.APP_NET_RX_BYTES_RATE._metrics


def test_realtime_event_removes_stale_disk_interface_pool_and_core_series():
    exporter = exporter_module.TrueNASExporter(make_config())

    exporter._handle_realtime_event(
        {
            "cpu": {
                "cpu": {"per_cpu": [10.0, 20.0]},
                "temperature": {"0": 41.0, "1": 42.0},
            },
            "disks": {
                "sda": {"read_bytes": 1, "write_bytes": 2, "read_ops": 3, "write_ops": 4, "busy": 5},
            },
            "interfaces": {
                "eth0": {"received_bytes": 100, "sent_bytes": 200},
            },
            "pools": {
                "tank": {"read_bytes": 300, "write_bytes": 400},
            },
        }
    )

    assert labeled_value(exporter_module.CPU_CORE_USAGE_PERCENT, "1") == 20.0
    assert labeled_value(exporter_module.DISK_READ_BYTES_RATE, "sda") == 1.0
    assert labeled_value(exporter_module.NETWORK_RX_BYTES_RATE, "eth0") == 100.0
    assert labeled_value(exporter_module.POOL_REALTIME_READ_BYTES, "tank") == 300.0

    exporter._handle_realtime_event(
        {
            "cpu": {
                "cpu": {"per_cpu": [30.0]},
                "temperature": {"0": 51.0},
            },
            "disls": {"read_bytes": 11, "write_bytes": 12, "read_ops": 13, "write_ops": 14, "busy": 15},
            "interfaces": {
                "eth1": {"received_bytes_rate": 500, "sent_bytes_rate": 600},
            },
            "pools": {
                "fast": {"read_bytes_per_second": 700, "write_bytes_per_second": 800},
            },
        }
    )

    assert labeled_value(exporter_module.CPU_CORE_USAGE_PERCENT, "0") == 30.0
    assert ("1",) not in exporter_module.CPU_CORE_USAGE_PERCENT._metrics
    assert ("1",) not in exporter_module.CPU_TEMPERATURE_C._metrics
    assert ("sda",) not in exporter_module.DISK_READ_BYTES_RATE._metrics
    assert labeled_value(exporter_module.DISK_READ_BYTES_RATE, "total") == 11.0
    assert ("eth0",) not in exporter_module.NETWORK_RX_BYTES_RATE._metrics
    assert labeled_value(exporter_module.NETWORK_TX_BYTES_RATE, "eth1") == 600.0
    assert ("tank",) not in exporter_module.POOL_REALTIME_READ_BYTES._metrics
    assert labeled_value(exporter_module.POOL_REALTIME_WRITE_BYTES, "fast") == 800.0


def test_realtime_event_accepts_alternative_cpu_core_and_temperature_shapes():
    exporter = exporter_module.TrueNASExporter(make_config())

    exporter._handle_realtime_event(
        {
            "cpu": {
                "cpu": {
                    "usage": {
                        "cpu0": {"percent": 14.5},
                        "core1": {"usage": 27.0},
                    },
                    "temperatures": [
                        {"core": "cpu0", "celsius": 44.0},
                        {"core": "core1", "temperature": 46.5},
                    ],
                },
            },
        }
    )

    assert labeled_value(exporter_module.CPU_CORE_USAGE_PERCENT, "0") == 14.5
    assert labeled_value(exporter_module.CPU_CORE_USAGE_PERCENT, "1") == 27.0
    assert labeled_value(exporter_module.CPU_TEMPERATURE_C, "0") == 44.0
    assert labeled_value(exporter_module.CPU_TEMPERATURE_C, "1") == 46.5
