"""Threaded HTTP exposition for immutable Prometheus snapshots."""

from __future__ import annotations

import logging
import socketserver
import threading
from collections.abc import Callable
from typing import Any
from wsgiref.simple_server import WSGIRequestHandler, WSGIServer, make_server

from prometheus_client import CollectorRegistry, make_wsgi_app

LOG = logging.getLogger("truenas_exporter")


class _QuietHandler(WSGIRequestHandler):
    def log_message(self, fmt: str, *args: Any) -> None:
        pass


class _ThreadingWSGIServer(socketserver.ThreadingMixIn, WSGIServer):
    daemon_threads = True


_LANDING_PAGE = b"""\
<html><head><title>TrueNAS Exporter</title></head><body>
<h1>TrueNAS Exporter</h1>
<p><a href="/metrics">Metrics</a></p>
<p><a href="/healthz">Liveness</a></p>
<p><a href="/readyz">Readiness</a></p>
</body></html>
"""


def start_http_server(
    port: int,
    lock: Any,
    registry: CollectorRegistry | None = None,
    lock_metrics: bool = True,
    readiness_check: Callable[[], bool] | None = None,
) -> Any:
    metrics_app = make_wsgi_app() if registry is None else make_wsgi_app(registry=registry)

    def app(environ: dict[str, Any], start_response: Any) -> list[bytes]:
        path = environ.get("PATH_INFO", "")
        if path == "/":
            start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
            return [_LANDING_PAGE]
        if path == "/healthz":
            start_response("200 OK", [("Content-Type", "text/plain; charset=utf-8")])
            return [b"ok\n"]
        if path == "/readyz":
            ready = readiness_check() if readiness_check is not None else False
            status = "200 OK" if ready else "503 Service Unavailable"
            body = b"ready\n" if ready else b"not ready\n"
            start_response(status, [("Content-Type", "text/plain; charset=utf-8")])
            return [body]
        if lock_metrics:
            with lock:
                return metrics_app(environ, start_response)
        return metrics_app(environ, start_response)

    server = make_server(
        "", port, app, server_class=_ThreadingWSGIServer, handler_class=_QuietHandler
    )
    thread = threading.Thread(target=server.serve_forever, name="http-server", daemon=True)
    thread.start()
    LOG.info("HTTP server started on :%d (GET /, GET /metrics, GET /healthz, GET /readyz)", port)
    return server


_start_http_server = start_http_server
