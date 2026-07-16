"""Environment-backed exporter configuration with strict validation."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

from .api_catalog import DEFAULT_SAFE_EVENT_SUBSCRIPTIONS, SAFE_EVENT_SUBSCRIPTIONS

DEFAULT_EVENT_SUBSCRIPTIONS = DEFAULT_SAFE_EVENT_SUBSCRIPTIONS


@dataclass
class Config:
    ws_url: str
    api_key: str
    interval_seconds: int
    timeout_seconds: int
    verify_tls: bool
    exporter_port: int
    auto_discover_methods: bool
    query_limit: int
    max_method_calls: int
    max_list_items: int
    max_depth: int
    max_entity_calls: int
    max_datasets: int
    extra_methods: list[str]
    exclude_methods: list[str]
    filesystem_paths: list[str]
    enable_filesystem_listdir: bool
    enable_event_streams: bool
    enable_dataset_metrics: bool
    enable_task_metrics: bool
    enable_ipmi_metrics: bool
    event_interval_seconds: int
    event_read_timeout_seconds: int
    event_subscriptions: list[str]
    scrape_all_metrics: bool
    enable_generic_method_metrics: bool
    enable_generic_event_metrics: bool
    dataset_snapshot_fallback_limit: int
    exporter_mode: str
    scrape_budget_seconds: int = 25
    event_stale_after_seconds: int = 15
    ca_file: str | None = None


def _bool_env(name: str, default: str = "true") -> bool:
    raw = os.getenv(name, default).strip().lower()
    if raw in {"1", "true", "yes", "on"}:
        return True
    if raw in {"0", "false", "no", "off"}:
        return False
    raise ValueError(f"{name} must be a boolean, got {raw!r}")


def _list_env(name: str, default: str = "") -> list[str]:
    return [item.strip() for item in os.getenv(name, default).split(",") if item.strip()]


def _int_env(name: str, default: str, minimum: int, maximum: int | None = None) -> int:
    raw = os.getenv(name, default).strip()
    try:
        value = int(raw)
    except ValueError as exc:
        raise ValueError(f"{name} must be an integer, got {raw!r}") from exc
    if value < minimum or (maximum is not None and value > maximum):
        bounds = f"between {minimum} and {maximum}" if maximum is not None else f">= {minimum}"
        raise ValueError(f"{name} must be {bounds}, got {value}")
    return value


def load_config() -> Config:
    ws_url = os.getenv("TRUENAS_WS_URL", "").strip()
    api_key = os.getenv("TRUENAS_API_KEY", "").strip()
    api_key_file = os.getenv("TRUENAS_API_KEY_FILE", "").strip()
    ca_file = os.getenv("TRUENAS_CA_FILE", "").strip() or None

    if not ws_url:
        raise ValueError("TRUENAS_WS_URL is required (example: wss://truenas.local/api/current)")
    parsed_url = urlparse(ws_url)
    if parsed_url.scheme not in {"ws", "wss"} or not parsed_url.hostname:
        raise ValueError("TRUENAS_WS_URL must be an absolute ws:// or wss:// URL")

    if not api_key and api_key_file:
        key_path = Path(api_key_file)
        try:
            api_key = key_path.read_text(encoding="utf-8").strip()
        except OSError as exc:
            raise ValueError(f"TRUENAS_API_KEY_FILE cannot be read: {key_path}") from exc
    if not api_key:
        raise ValueError("TRUENAS_API_KEY or TRUENAS_API_KEY_FILE is required")
    if ca_file and not Path(ca_file).is_file():
        raise ValueError(f"TRUENAS_CA_FILE does not exist or is not a file: {ca_file}")

    filesystem_paths = _list_env("FILESYSTEM_PATHS", "/mnt") or ["/mnt"]
    if any(not path.startswith("/") for path in filesystem_paths):
        raise ValueError("FILESYSTEM_PATHS entries must be absolute TrueNAS paths")

    exporter_mode = os.getenv("EXPORTER_MODE", "collector").strip().lower() or "collector"
    if exporter_mode not in {"legacy", "collector"}:
        raise ValueError("EXPORTER_MODE must be either 'legacy' or 'collector'")

    event_interval_seconds = _int_env("EVENT_INTERVAL_SECONDS", "2", 1)
    event_stale_after_seconds = _int_env("EVENT_STALE_AFTER_SECONDS", "15", 1)
    if event_stale_after_seconds < event_interval_seconds:
        raise ValueError(
            "EVENT_STALE_AFTER_SECONDS must be >= EVENT_INTERVAL_SECONDS"
        )

    event_subscriptions = _list_env(
        "EVENT_SUBSCRIPTIONS", ",".join(DEFAULT_EVENT_SUBSCRIPTIONS)
    )
    unsafe_events = sorted(set(event_subscriptions) - SAFE_EVENT_SUBSCRIPTIONS)
    if unsafe_events:
        raise ValueError(
            "EVENT_SUBSCRIPTIONS contains undocumented or sensitive/raw events: "
            + ", ".join(unsafe_events)
        )

    return Config(
        ws_url=ws_url,
        api_key=api_key,
        interval_seconds=_int_env("SCRAPE_INTERVAL_SECONDS", "30", 1),
        timeout_seconds=_int_env("TRUENAS_TIMEOUT_SECONDS", "20", 1),
        verify_tls=_bool_env("TRUENAS_VERIFY_TLS", "true"),
        exporter_port=_int_env("EXPORTER_PORT", "9108", 1, 65535),
        auto_discover_methods=_bool_env("AUTO_DISCOVER_METHODS", "false"),
        query_limit=_int_env("QUERY_LIMIT", "200", 1),
        max_method_calls=_int_env("MAX_METHOD_CALLS", "250", 1),
        max_list_items=_int_env("MAX_LIST_ITEMS", "200", 1),
        max_depth=_int_env("MAX_METRIC_DEPTH", "6", 0),
        max_entity_calls=_int_env("MAX_ENTITY_CALLS", "50", 1),
        max_datasets=_int_env("MAX_DATASETS", "100", 1),
        extra_methods=_list_env("EXTRA_METHODS"),
        exclude_methods=_list_env("EXCLUDE_METHODS"),
        filesystem_paths=filesystem_paths,
        enable_filesystem_listdir=_bool_env("ENABLE_FILESYSTEM_LISTDIR", "false"),
        enable_event_streams=_bool_env("ENABLE_EVENT_STREAMS", "true"),
        enable_dataset_metrics=_bool_env("ENABLE_DATASET_METRICS", "true"),
        enable_task_metrics=_bool_env("ENABLE_TASK_METRICS", "true"),
        enable_ipmi_metrics=_bool_env("ENABLE_IPMI_METRICS", "true"),
        event_interval_seconds=event_interval_seconds,
        event_read_timeout_seconds=_int_env("EVENT_READ_TIMEOUT_SECONDS", "60", 1),
        event_subscriptions=event_subscriptions,
        scrape_all_metrics=_bool_env("SCRAPE_ALL_METRICS", "false"),
        enable_generic_method_metrics=_bool_env("ENABLE_GENERIC_METHOD_METRICS", "false"),
        enable_generic_event_metrics=_bool_env("ENABLE_GENERIC_EVENT_METRICS", "false"),
        dataset_snapshot_fallback_limit=_int_env("DATASET_SNAPSHOT_FALLBACK_LIMIT", "0", 0),
        exporter_mode=exporter_mode,
        scrape_budget_seconds=_int_env("SCRAPE_BUDGET_SECONDS", "25", 1),
        event_stale_after_seconds=event_stale_after_seconds,
        ca_file=ca_file,
    )
