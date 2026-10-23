"""Bounded read-only schema probe; emit only counts and field/type summaries."""

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from truenas_exporter.transport import JsonRpcWsClient


def describe(value):
    if isinstance(value, list):
        return {"type": "list", "count": len(value), "items": [describe(v) for v in value[:1]]}
    if isinstance(value, dict):
        return {"type": "dict", "fields": {k: type(v).__name__ for k, v in value.items()}}
    return {"type": type(value).__name__}


key = Path("/tmp/truenas-local-test-secrets/api_key").read_text().strip()
calls = [
    ("system.version_short", []),
    ("pool.dataset.query", [[], {"limit": 2, "extra": {"properties": ["logicalused", "logicalreferenced", "referenced", "usedbyrefreservation"]}, "select": ["logicalused", "logicalreferenced", "referenced", "usedbyrefreservation"]}]),
    ("disk.query", [[], {"limit": 2, "extra": {"sed_status": True}, "select": ["sed", "sed_status"]}]),
    ("cloud_backup.query", [[], {"limit": 2, "select": ["id", "enabled", "locked", "job"]}]),
    ("reporting.netdata_graphs", [[], {"limit": 50}]),
    ("zfs.tier.config", []),
    ("zfs.tier.rewrite_job_query", [{"query-filters": [], "query-options": {"limit": 2}}]),
    ("reporting.get_data", [[{"name": "upscharge"}], {"start": int(time.time()) - 90, "end": int(time.time()), "aggregate": False}]),
]
with JsonRpcWsClient("wss://192.168.0.238:449/api/current", 10, False, deadline_monotonic=time.monotonic() + 75) as client:
    client.authenticate(key, username="root")
    for method, params in calls:
        started = time.monotonic()
        try:
            result = client.call(method, params)
            summary = describe(result)
            if method == "system.version_short":
                summary["version"] = result
            if method == "reporting.netdata_graphs" and isinstance(result, list):
                summary["ups_graphs"] = [r.get("name") for r in result if isinstance(r, dict) and str(r.get("name", "")).startswith("ups")]
            print(json.dumps({"method": method, "elapsed": round(time.monotonic() - started, 3), "summary": summary}), flush=True)
        except Exception as exc:
            print(json.dumps({"method": method, "error": type(exc).__name__, "code": getattr(exc, "code", None)}), flush=True)
