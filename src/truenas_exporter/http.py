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
    host: str | int,
    port: int | Any,
    lock: Any | None = None,
    registry: CollectorRegistry | None = None,
    lock_metrics: bool = True,
    readiness_check: Callable[[], bool] | None = None,
) -> Any:
    if lock is None:
        bind_host = ""
        bind_port = int(host)
        metrics_lock: Any = port
    else:
        bind_host = str(host)
        bind_port = int(port)
        metrics_lock = lock
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
            with metrics_lock:
                return metrics_app(environ, start_response)
        return metrics_app(environ, start_response)

    server = make_server(
        bind_host, bind_port, app, server_class=_ThreadingWSGIServer, handler_class=_QuietHandler
    )
    thread = threading.Thread(target=server.serve_forever, name="http-server", daemon=True)
    thread.start()
    bind_label = bind_host or ""
    LOG.info(
        "HTTP server started on %s:%d (GET /, GET /metrics, GET /healthz, GET /readyz)",
        bind_label,
        bind_port,
    )
    return server


_start_http_server = start_http_server
