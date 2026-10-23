"""One bounded source poll; keep private values in memory, report counts only."""

import json
import logging
import math
import sys
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from truenas_exporter import runtime
from truenas_exporter.compat_profiles import PROFILE_27_0, TRANSPORT_METHOD_ALLOWLIST
from truenas_exporter.config import load_config

logging.disable(logging.CRITICAL)
original = runtime.JsonRpcWsClient
calls = Counter()
responses = {}


class Client(original):
    def call(self, method, params=None):
        if method not in PROFILE_27_0.reviewed_methods | TRANSPORT_METHOD_ALLOWLIST or sum(calls.values()) >= 250:
            raise RuntimeError("bounded read-only verification policy")
        calls[method] += 1
        value = super().call(method, params)
        if method in {"pool.dataset.query", "pool.query", "zfs.tier.config", "cloud_backup.query", "disk.query"}:
            responses[method] = value
        return value


runtime.JsonRpcWsClient = Client
exporter = runtime.TrueNASExporter(load_config())
started = time.monotonic()
exporter.scrape_once()
samples = [s for f in exporter.metric_snapshot() for s in f.samples]
contract = json.loads(Path("/tmp/truenas-telemetry-contract-before.json").read_text())
old = {m["name"] for m in contract["metrics"]}
added = [s for s in samples if s.name.startswith("truenas_") and s.name not in old]
comparisons = Counter()


def check(metric, value, labels=None):
    actual = next((s.value for s in samples if s.name == metric and s.labels == (labels or {})), None)
    comparisons["match" if actual is not None and math.isclose(actual, value, rel_tol=1e-9) else "mismatch"] += 1


datasets = responses.get("pool.dataset.query", [])
if isinstance(datasets, list):
    for dataset in datasets:
        if not isinstance(dataset, dict):
            continue
        for field, metric in (("logicalused", "truenas_dataset_logical_used_bytes"), ("logicalreferenced", "truenas_dataset_logical_referenced_bytes"), ("usedbyrefreservation", "truenas_dataset_used_by_refreservation_bytes"), ("recordsize", "truenas_dataset_recordsize_bytes"), ("copies", "truenas_dataset_copies"), ("referenced", "truenas_dataset_referenced_bytes"), ("volsize", "truenas_dataset_volsize_bytes"), ("volblocksize", "truenas_dataset_volblocksize_bytes")):
            value = runtime._as_float(dataset.get(field))
            if value is None:
                continue
            check(metric, value, {"dataset": dataset.get("id")})
        sync, dedup = dataset.get("sync"), dataset.get("deduplication")
        if isinstance(sync, str) and sync.upper() in ("STANDARD", "ALWAYS", "DISABLED"):
            check("truenas_dataset_sync_mode", 1, {"dataset": dataset.get("id"), "mode": sync.upper()})
        if isinstance(dedup, str) and dedup.upper() in ("ON", "OFF", "VERIFY"):
            check("truenas_dataset_dedup_enabled", int(dedup.upper() != "OFF"), {"dataset": dataset.get("id")})
config = responses.get("zfs.tier.config")
if isinstance(config, dict):
    for field, metric in (("enabled", "truenas_zfs_tier_enabled"), ("max_concurrent_jobs", "truenas_zfs_tier_max_concurrent_jobs"), ("max_used_percentage", "truenas_zfs_tier_max_used_percent"), ("special_class_metadata_reserve_pct", "truenas_zfs_tier_metadata_reserve_percent")):
        value = config.get(field)
        if type(value) in (int, float, bool):
            check(metric, float(value))
disks = responses.get("disk.query", [])
if isinstance(disks, list):
    for disk in disks:
        if isinstance(disk, dict) and type(disk.get("sed")) is bool:
            check("truenas_disk_sed_capable", int(disk["sed"]), {"disk": disk.get("name")})
summary = {"profile": exporter.compatibility_profile.name, "elapsed": round(time.monotonic() - started, 3),
    "ready": exporter.is_ready(), "up": next(s.value for s in samples if s.name == "truenas_up"),
    "samples": len(samples), "new_finite_samples": sum(math.isfinite(s.value) for s in added),
    "new_finite_families": sorted({s.name for s in added if math.isfinite(s.value)}),
    "rpc_calls": sum(calls.values()), "comparisons": dict(comparisons),
    "tier_config_available": isinstance(responses.get("zfs.tier.config"), dict),
    "backup_tasks_observed": len(responses.get("cloud_backup.query", [])),
    "api_failures": sum(s.value == 0 for s in samples if s.name == "truenas_api_call_success")}
print(json.dumps(summary, sort_keys=True))
if not summary["ready"] or summary["up"] != 1 or comparisons["mismatch"]:
    raise SystemExit(1)
