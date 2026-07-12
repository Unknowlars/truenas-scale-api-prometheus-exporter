import threading
import urllib.error
import urllib.request

import pytest

import truenas_exporter as exporter_module


def test_real_http_server_liveness_and_readiness():
    ready = {"value": False}
    try:
        server = exporter_module._start_http_server(
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
