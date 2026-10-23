"""Bounded, sanitized, read-only live verification for the remediation work."""

from __future__ import annotations

import argparse
import getpass
import json
import math
import os
import sys
import threading
import time
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT), str(ROOT / "src")]

import truenas_exporter as exporter_module  # noqa: E402
from truenas_exporter.config import DEFAULT_EVENT_SUBSCRIPTIONS  # noqa: E402

runtime = sys.modules[exporter_module.TrueNASExporter.__module__]


def sample_value(exporter: Any, name: str) -> float | None:
    for family in exporter.metric_snapshot():
        for sample in family.samples:
            if sample.name == name and not sample.labels:
                return float(sample.value)
    return None


def config(api_key: str, *, historical: bool) -> Any:
    return exporter_module.Config(
        ws_url=os.environ["TRUENAS_WS_URL"],
        api_key=api_key,
        username=os.environ.get("TRUENAS_USERNAME") or None,
        interval_seconds=30,
        timeout_seconds=20,
        verify_tls=False,
        exporter_port=0,
        auto_discover_methods=historical,
        query_limit=200,
        max_method_calls=250,
        max_list_items=200,
        max_depth=6,
        max_entity_calls=50,
        max_datasets=100,
        extra_methods=[],
        exclude_methods=[],
        filesystem_paths=["/mnt"],
        enable_filesystem_listdir=historical,
        enable_event_streams=True,
        enable_dataset_metrics=True,
        enable_task_metrics=True,
        enable_ipmi_metrics=False,
        event_interval_seconds=2,
        event_read_timeout_seconds=60,
        event_subscriptions=list(DEFAULT_EVENT_SUBSCRIPTIONS),
        scrape_all_metrics=historical,
        enable_generic_method_metrics=False,
        enable_generic_event_metrics=False,
        dataset_snapshot_fallback_limit=0 if historical else 25,
        exporter_mode="collector",
        exporter_bind_address="127.0.0.1",
        scrape_budget_seconds=25,
        event_stale_after_seconds=15,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--historical", action="store_true")
    parser.add_argument("--event-seconds", type=int, default=18)
    args = parser.parse_args()
    api_key = getpass.getpass("TrueNAS API key: ")
    if not api_key:
        raise SystemExit("empty key")

    original_client = runtime.JsonRpcWsClient
    call_lock = threading.Lock()
    calls = 0
    event_clients: list[Any] = []

    class CountingClient(original_client):
        def __init__(self, *client_args: Any, **client_kwargs: Any) -> None:
            super().__init__(*client_args, **client_kwargs)
            if client_kwargs.get("deadline_monotonic") is None:
                event_clients.append(self)

        def call(self, method: str, params: list[Any] | None = None) -> Any:
            nonlocal calls
            with call_lock:
                calls += 1
            return super().call(method, params)

    runtime.JsonRpcWsClient = CountingClient
    cfg = config(api_key, historical=args.historical)

    # Independent, bounded source observations. Do not retain or print payloads.
    with original_client(
        cfg.ws_url, cfg.timeout_seconds, cfg.verify_tls, ca_file=cfg.ca_file
    ) as client:
        client.authenticate(api_key, username=cfg.username)
        version = client.call("system.version_short", [])
        smb = client.call("smb.config", [])
    if not isinstance(version, str):
        raise AssertionError("system.version_short was not a string")
    if not isinstance(smb, dict):
        raise AssertionError("smb.config was not an object")
    protocol = smb.get("minimum_protocol")
    expected_smb = 1.0 if protocol == "SMB1" else 0.0 if protocol in {"SMB2", "SMB3"} else None

    exporter = runtime.TrueNASExporter(cfg)
    registry = runtime.CollectorRegistry(auto_describe=False)
    registry.register(runtime.TrueNASCollector(exporter))
    server = runtime._start_http_server(
        "127.0.0.1",
        0,
        exporter._lock,
        registry=registry,
        lock_metrics=False,
        readiness_check=exporter.is_ready,
    )
    base_url = f"http://127.0.0.1:{server.server_port}"
    started = time.monotonic()
    try:
        exporter._ensure_event_thread()
        exporter.scrape_once()
        duration = time.monotonic() - started
        up = sample_value(exporter, "truenas_up")
        smb_metric = sample_value(exporter, "truenas_smb1_enabled")
        if up != 1.0 or not exporter.is_ready():
            raise AssertionError("live polling cycle was not healthy")
        if expected_smb is None or smb_metric != expected_smb:
            raise AssertionError("SMB1 source/metric comparison failed")

        event_observations = []
        deadline = time.monotonic() + args.event_seconds
        while time.monotonic() < deadline:
            time.sleep(min(2.0, max(0.0, deadline - time.monotonic())))
            updated = exporter._snapshot_event_times.get("reporting.realtime")
            cpu = sample_value(exporter, "truenas_cpu_usage_percent")
            event_observations.append(
                {
                    "snapshot_age_seconds": None
                    if updated is None
                    else round(time.monotonic() - updated, 3),
                    "cpu_finite": cpu is not None and math.isfinite(cpu),
                }
            )
        if not event_observations or not all(
            item["cpu_finite"] and item["snapshot_age_seconds"] is not None
            and item["snapshot_age_seconds"] < 5
            for item in event_observations
        ):
            raise AssertionError(
                "event snapshot did not remain fresh: "
                + json.dumps(event_observations, sort_keys=True)
            )

        with call_lock:
            before_http = calls
        for _ in range(10):
            with urllib.request.urlopen(f"{base_url}/metrics", timeout=2) as response:
                body = response.read()
                if response.status != 200 or b"truenas_up 1.0" not in body:
                    raise AssertionError("packaged-style HTTP exposition was unhealthy")
        with call_lock:
            http_rpc_delta = calls - before_http
        if http_rpc_delta != 0:
            raise AssertionError("HTTP metrics requests issued NAS RPCs")

        reconnect_verified = False
        if not args.historical:
            reconnect_deadline = time.monotonic() + 10
            while not event_clients and time.monotonic() < reconnect_deadline:
                time.sleep(0.1)
            prior_clients = len(event_clients)
            if not event_clients or event_clients[-1]._ws is None:
                raise AssertionError("event client was not connected")
            event_clients[-1]._ws.close()
            reconnect_deadline = time.monotonic() + 20
            while len(event_clients) <= prior_clients and time.monotonic() < reconnect_deadline:
                time.sleep(0.2)
            reconnect_verified = len(event_clients) > prior_clients
            if not reconnect_verified:
                raise AssertionError("local event-socket close did not reconnect")

        print(json.dumps({
            "mode": "historical" if args.historical else "current",
            "version": version,
            "profile": exporter.compatibility_profile.name,
            "poll_duration_seconds": round(duration, 3),
            "up": up,
            "ready": exporter.is_ready(),
            "smb1_comparison": "match",
            "event_observations": event_observations,
            "http_requests": 10,
            "http_rpc_delta": http_rpc_delta,
            "local_socket_reconnect": reconnect_verified if not args.historical else "not_requested",
        }, sort_keys=True))
    finally:
        exporter.stop()
        for client in event_clients:
            if client._ws is not None:
                client._ws.close()
        if exporter._event_thread is not None:
            exporter._event_thread.join(timeout=20)
        server.shutdown()
        server.server_close()
        runtime.JsonRpcWsClient = original_client


if __name__ == "__main__":
    main()
