import concurrent.futures
import threading
import time
import urllib.error
import urllib.request

import pytest

import truenas_exporter as exporter_module


def test_real_http_server_liveness_and_readiness():
    ready = {"value": False}
    try:
        server = exporter_module._start_http_server(
            "",
            0,
            threading.Lock(),
            readiness_check=lambda: ready["value"],
        )
    except PermissionError:
        pytest.skip("local sandbox does not permit binding a loopback socket")
    base_url = f"http://127.0.0.1:{server.server_port}"

    try:
        with urllib.request.urlopen(f"{base_url}/healthz", timeout=2) as response:
            assert response.status == 200
            assert response.read() == b"ok\n"

        try:
            urllib.request.urlopen(f"{base_url}/readyz", timeout=2)
        except urllib.error.HTTPError as exc:
            assert exc.code == 503
            assert exc.read() == b"not ready\n"
        else:
            raise AssertionError("unready endpoint unexpectedly returned success")

        ready["value"] = True
        with urllib.request.urlopen(f"{base_url}/readyz", timeout=2) as response:
            assert response.status == 200
            assert response.read() == b"ready\n"
    finally:
        server.shutdown()


def test_real_http_server_binds_ipv6_bracket_free_literal():
    """R05: EXPORTER_BIND_ADDRESS="::1" must actually bind, not just pass
    config validation. wsgiref's WSGIServer defaults to AF_INET regardless of
    the host string, so this exercises the AF_INET6 server class selection.

    Only a genuine environment permission issue is skipped — anything else
    (e.g. the pre-fix AF_INET socket rejecting an IPv6 literal) must fail.
    """
    import socket as socket_module

    if not socket_module.has_ipv6:
        pytest.skip("this host has no IPv6 support")
    try:
        server = exporter_module._start_http_server(
            "::1",
            0,
            threading.Lock(),
            readiness_check=lambda: True,
        )
    except PermissionError:
        pytest.skip("local sandbox does not permit binding a loopback socket")
    base_url = f"http://[::1]:{server.server_port}"
    try:
        with urllib.request.urlopen(f"{base_url}/healthz", timeout=2) as response:
            assert response.status == 200
            assert response.read() == b"ok\n"
    finally:
        server.shutdown()
        server.server_close()


def test_overlapping_metrics_are_consistent_and_health_stays_responsive():
    exporter = exporter_module.TrueNASExporter(
        exporter_module.Config(
            ws_url="wss://nas.example/api/current",
            api_key="test-key",
            interval_seconds=30,
            timeout_seconds=20,
            verify_tls=True,
            exporter_port=9108,
            auto_discover_methods=False,
            query_limit=200,
            max_method_calls=250,
            max_list_items=200,
            max_depth=6,
            max_entity_calls=50,
            max_datasets=100,
            extra_methods=[],
            exclude_methods=[],
            filesystem_paths=["/mnt"],
            enable_filesystem_listdir=False,
            enable_event_streams=False,
            enable_dataset_metrics=True,
            enable_task_metrics=False,
            enable_ipmi_metrics=False,
            event_interval_seconds=2,
            event_read_timeout_seconds=60,
            event_subscriptions=[],
            scrape_all_metrics=False,
            enable_generic_method_metrics=False,
            enable_generic_event_metrics=False,
            dataset_snapshot_fallback_limit=0,
            exporter_mode="collector",
        )
    )
    original_snapshot = exporter.metric_snapshot
    overlap = threading.Barrier(3)

    def blocked_snapshot():
        snapshot = original_snapshot()
        overlap.wait(timeout=2)
        return snapshot

    exporter.metric_snapshot = blocked_snapshot
    registry = exporter_module.CollectorRegistry(auto_describe=False)
    registry.register(exporter_module.TrueNASCollector(exporter))
    try:
        server = exporter_module._start_http_server(
            "",
            0,
            exporter._lock,
            registry=registry,
            lock_metrics=False,
            readiness_check=exporter.is_ready,
        )
    except PermissionError:
        pytest.skip("local sandbox does not permit binding a loopback socket")
    base_url = f"http://127.0.0.1:{server.server_port}"

    def fetch_metrics():
        with urllib.request.urlopen(f"{base_url}/metrics", timeout=3) as response:
            return response.read()

    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            requests = [pool.submit(fetch_metrics) for _ in range(2)]
            started = time.monotonic()
            with urllib.request.urlopen(f"{base_url}/healthz", timeout=1) as response:
                assert response.read() == b"ok\n"
            assert time.monotonic() - started < 1.0
            overlap.wait(timeout=2)
            first, second = (request.result(timeout=3) for request in requests)
        assert first == second
        assert b"truenas_up" in first
    finally:
        server.shutdown()


def test_legacy_metrics_serves_snapshot_while_scrape_lock_is_held():
    exporter = exporter_module.TrueNASExporter(
        exporter_module.Config(
            ws_url="wss://nas.example/api/current",
            api_key="test-key",
            interval_seconds=30,
            timeout_seconds=20,
            verify_tls=True,
            exporter_port=9108,
            auto_discover_methods=False,
            query_limit=200,
            max_method_calls=250,
            max_list_items=200,
            max_depth=6,
            max_entity_calls=50,
            max_datasets=100,
            extra_methods=[],
            exclude_methods=[],
            filesystem_paths=["/mnt"],
            enable_filesystem_listdir=False,
            enable_event_streams=False,
            enable_dataset_metrics=True,
            enable_task_metrics=False,
            enable_ipmi_metrics=False,
            event_interval_seconds=2,
            event_read_timeout_seconds=60,
            event_subscriptions=[],
            scrape_all_metrics=False,
            enable_generic_method_metrics=False,
            enable_generic_event_metrics=False,
            dataset_snapshot_fallback_limit=0,
            exporter_mode="legacy",
        )
    )
    exporter_module.SCRAPE_SUCCESS.set(1)
    exporter._publish_metric_snapshot()
    registry = exporter_module.CollectorRegistry(auto_describe=False)
    registry.register(exporter_module.TrueNASCollector(exporter))
    try:
        server = exporter_module._start_http_server(
            "",
            0,
            exporter._lock,
            registry=registry,
            lock_metrics=False,
            readiness_check=exporter.is_ready,
        )
    except PermissionError:
        pytest.skip("local sandbox does not permit binding a loopback socket")
    base_url = f"http://127.0.0.1:{server.server_port}"

    try:
        with exporter._lock, urllib.request.urlopen(
            f"{base_url}/metrics", timeout=0.5
        ) as response:
            body = response.read()
        assert b"truenas_up" in body
    finally:
        server.shutdown()


def test_http_server_binds_configured_loopback_address():
    try:
        server = exporter_module._start_http_server(
            "127.0.0.1",
            0,
            threading.Lock(),
            readiness_check=lambda: True,
        )
    except PermissionError:
        pytest.skip("local sandbox does not permit binding a loopback socket")

    try:
        assert server.server_address[0] == "127.0.0.1"
    finally:
        server.shutdown()
