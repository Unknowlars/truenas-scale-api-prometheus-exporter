"""Observe the local packaged exporter for 70 seconds; report aggregates only."""

import json
import math
import time
import urllib.request
from pathlib import Path

from prometheus_client.parser import text_string_to_metric_families

old = {m["name"] for m in json.loads(Path("/tmp/truenas-telemetry-contract-before.json").read_text())["metrics"]}
opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
for attempt in range(30):
    try:
        with opener.open("http://127.0.0.1:9108/readyz", timeout=3):
            break
    except Exception:
        if attempt == 29:
            raise SystemExit("Packaged runtime did not become ready")
        time.sleep(2)

observations = []
started = time.monotonic()
for index in range(15):
    with opener.open("http://127.0.0.1:9108/metrics", timeout=5) as response:
        samples = [s for f in text_string_to_metric_families(response.read().decode()) for s in f.samples]
    with opener.open("http://127.0.0.1:9108/readyz", timeout=3) as response:
        ready = response.status
    up = next(s.value for s in samples if s.name == "truenas_up")
    cpu = [s.value for s in samples if s.name == "truenas_cpu_usage_percent"]
    event = next((s.value for s in samples if s.name == "truenas_event_last_message_timestamp_seconds" and s.labels.get("event") == "reporting.realtime"), None)
    observed = {"elapsed": round(time.monotonic() - started, 2), "ready": ready,
        "up": up, "samples": len(samples),
        "new_finite_samples": sum(s.name.startswith("truenas_") and s.name not in old and math.isfinite(s.value) for s in samples),
        "cpu_finite": bool(cpu) and all(math.isfinite(v) for v in cpu),
        "realtime_event_age": round(time.time() - event, 3) if event is not None else None,
        "last_poll": next(s.value for s in samples if s.name == "truenas_last_scrape_timestamp_seconds")}
    observations.append(observed)
    if index in (0, 7, 14):
        print(json.dumps(observed), flush=True)
    if index != 14:
        time.sleep(5)
steady = [r for r in observations if r["elapsed"] >= 15]
summary = {"observations": len(observations), "elapsed": round(time.monotonic() - started, 2),
    "healthy": all(r["ready"] == 200 and r["up"] == 1 for r in observations),
    "realtime_pending_at_start": not observations[0]["cpu_finite"],
    "realtime_healthy_after_startup": bool(steady) and all(r["cpu_finite"] and r["realtime_event_age"] is not None and 0 <= r["realtime_event_age"] <= 15 for r in steady),
    "new_finite_samples_min": min(r["new_finite_samples"] for r in observations),
    "poll_snapshots_observed": len({r["last_poll"] for r in observations}),
    "max_realtime_event_age": max((r["realtime_event_age"] for r in observations if r["realtime_event_age"] is not None), default=None)}
print(json.dumps(summary), flush=True)
if not summary["healthy"] or not summary["realtime_healthy_after_startup"] or summary["new_finite_samples_min"] < 1:
    raise SystemExit(1)
