from truenas_exporter import Config


def make_config(**overrides):
    values = {
        "ws_url": "wss://nas.example/api/current",
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
        "scrape_budget_seconds": 25,
        "event_stale_after_seconds": 15,
        "ca_file": None,
    }
    values.update(overrides)
    return Config(**values)
