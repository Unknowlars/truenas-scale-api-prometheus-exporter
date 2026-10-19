#!/usr/bin/env python3
"""Generate offline TrueNAS 27 compatibility and complete metric inventories.

Reuses the existing parity audit's explicit ownership mappings. Source references
are static evidence, never live-server success or permission validation.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import generate_api_exporter_parity as parity  # noqa: E402
from tooling import check_or_write  # noqa: E402

OUT = ROOT / "docs/reviews"
INPUTS = {
    "25.10.2": ROOT / "docs/truenas-api",
    "26.0.0": ROOT / "docs/truenas-api-v26",
    "27-local": ROOT / "docs/api/truenas-27",
    "27-official": ROOT / "docs/api/truenas-27-official",
}
DASHBOARDS = (
    "grafana-dashboard/operations-center-dashboard.json",
    "grafana-dashboard/truenas-mission-control.json",
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot(root: Path) -> dict[str, Any]:
    manifest = json.loads((root / "MANIFEST.json").read_text())
    for entry in manifest["files"]:
        path = root / entry["path"]
        if sha(path) != entry["sha256"]:
            raise ValueError(f"Documentation integrity mismatch: {path}")
    index = {(row["kind"], row["name"]): row for row in manifest.get("inventory", [])}
    raw = {entry["path"]: entry["sha256"] for entry in manifest.get("source_files", [])}
    pages = {}
    for kind in ("method", "event"):
        for path in sorted((root / f"{kind}s").rglob("*.md")):
            page = parity.parse_api_page(path, root)
            if page.kind != kind:
                continue
            entry = index.get((kind, page.title), {})
            fields = entry.get("fields")
            pages[(kind, page.title)] = {
                "page": page,
                "path": path.relative_to(ROOT).as_posix(),
                "markdown_sha256": sha(path),
                "source_sha256": raw.get(entry.get("source_rst", "")),
                "schema_sha256": entry.get("schema_sha256"),
                "roles": sorted({role.strip() for combined in entry.get("required_roles", page.roles)
                                 for role in re.split(r"[,|]", combined) if role.strip()}),
                "parameters": [[position, name] for position, name in page.parameters],
                "return_type": page.return_type,
                "fields": fields if fields is not None else [
                    {"name": name, "type": " | ".join(types), "required": None, "schema_id": None}
                    for name, types in page.fields.items()
                ],
                "event_shapes": list(page.event_shapes),
            }
    return {"manifest": manifest, "pages": pages, "manifest_sha256": sha(root / "MANIFEST.json")}


def signature(row: dict[str, Any] | None) -> dict[str, Any] | None:
    if row is None:
        return None
    return {key: row[key] for key in ("roles", "parameters", "return_type", "fields", "event_shapes")}


def changed(old: dict[str, Any] | None, new: dict[str, Any] | None) -> list[str]:
    if not old or not new:
        return ["added" if new else "absent"]
    # Historical Markdown has no full schema paths/required flags. Compare only
    # the evidence both generations carry, without pretending it is exhaustive.
    keys = [key for key in ("roles", "parameters", "return_type", "event_shapes") if old[key] != new[key]]
    old_fields = {field["name"] for field in old["fields"] if not field.get("schema_id")
                  or str(field["schema_id"]).startswith(("Return_value", "ADDED", "CHANGED", "REMOVED"))}
    new_fields = {field["name"] for field in new["fields"] if not field.get("schema_id")
                  or str(field["schema_id"]).startswith(("Return_value", "ADDED", "CHANGED", "REMOVED"))}
    if old_fields != new_fields:
        keys.append("documented field names (hierarchy/converter differences possible)")
    return keys


def panel_references() -> dict[str, dict[str, list[str]]]:
    refs: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))

    def walk(value: Any, dashboard: str, panel: str = "dashboard variables/metadata") -> None:
        if isinstance(value, dict):
            if isinstance(value.get("title"), str):
                panel = value["title"]
            for item in value.values():
                walk(item, dashboard, panel)
        elif isinstance(value, list):
            for item in value:
                walk(item, dashboard, panel)
        elif isinstance(value, str):
            for metric in re.findall(r"\btruenas_[a-zA-Z0-9_:]+\b", value):
                refs[metric][dashboard].add(panel)

    for relative in DASHBOARDS:
        walk(json.loads((ROOT / relative).read_text()), relative)
    return {name: {dashboard: sorted(panels) for dashboard, panels in sorted(dashboards.items())}
            for name, dashboards in sorted(refs.items())}


def current_contract() -> list[dict[str, Any]]:
    """Read declarations without instantiating the global Prometheus registry."""
    path = ROOT / "src/truenas_exporter/metrics.py"
    result = []
    for node in ast.walk(ast.parse(path.read_text())):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name):
            continue
        if node.func.id not in {"declare_gauge", "declare_counter"}:
            continue
        args = [ast.literal_eval(arg) for arg in node.args]
        result.append({"variable": args[0], "name": args[1], "help": args[2],
                       "type": "gauge" if node.func.id == "declare_gauge" else "counter",
                       "labels": args[3] if len(args) > 3 else []})
    if len({metric["name"] for metric in result}) != len(result):
        raise ValueError("Duplicate metric declarations")
    return sorted(result, key=lambda row: row["name"])


def cardinality(labels: list[str]) -> dict[str, str]:
    if not labels:
        return {"risk": "low", "estimate": "1 per exporter"}
    sensitive = {"path", "dataset", "entity", "name", "reason", "serial", "hostname", "address", "guid"}
    risk = "high/review" if sensitive.intersection(labels) else "bounded by entity/enumeration count"
    return {"risk": risk,
            "estimate": "at most product of observed distinct label values: " + " × ".join(labels)}


def metric_unit(metric: dict[str, Any]) -> str:
    name, help_text = metric["name"], metric["help"].lower()
    for suffix, unit in (("_days", "days (legacy unit)"), ("_minutes", "minutes (legacy unit)"),
                         ("_gbit", "gigabits/second (legacy unit)"), ("_mbits", "megabits/second (legacy unit)")):
        if name.endswith(suffix):
            return unit
    if "numeric_value" in name:
        return "source-dependent; see field schema (generic extraction)"
    if "boolean" in name or "1 when" in help_text or "1 =" in help_text:
        return "boolean gauge (1/0)"
    if "bytes" in help_text or "_bytes_" in name:
        return "bytes/second" if "per_second" in name else "bytes"
    if "list_length" in name or "errors" in name or "cores" in name or "vcpus" in name:
        return "count"
    return parity._metric_output_unit(metric)


def schedule(sources: list[str], kind: str) -> tuple[str, str]:
    if "event" in kind:
        return ("on reviewed event messages; interval max(2, EVENT_INTERVAL_SECONDS); TTL EVENT_STALE_AFTER_SECONDS",
                "persistent subscription; source payload size/interval dependent")
    if kind in {"internal", "composed/internal"} or sources == ["exporter-owned state"]:
        return "exporter lifecycle/scrape or call/event transition", "no additional API calls"
    if "disk.temperature_agg" in sources or "pool.snapshot.query" in sources:
        return ("polling; heavy aggregates/oldest snapshot refresh every 10 cycles; cache expires after 30 cycles",
                "shared cached call; snapshot sort/temperature history can be expensive")
    if any(source in {"reporting.get_data", "reporting.netdata_get_data"} for source in sources):
        return "configured polling cycle (shared reporting request)", "reporting history/graph work; server cost unmeasured"
    if "generic" in kind:
        return "opt-in configured polling cycle with call/depth/item limits", "bounded by call budget; payload cost unmeasured"
    return ("configured polling cycle; feature/profile/budget gates apply",
            "shared method result where cached; per-entity methods increase cost; server cost unmeasured")


def field_evidence(sources: list[str], fields: list[str], pages: dict[tuple[str, str], dict[str, Any]], kind: str) -> list[dict[str, Any]]:
    result = []
    for source in sources:
        if source == "exporter-owned state":
            continue
        page = pages.get(("event" if "event" in kind else "method", source))
        for field in fields:
            tokens = set(re.findall(r"[a-zA-Z_][a-zA-Z0-9_]*", field))
            prefixes = ("ADDED", "CHANGED", "REMOVED") if "event" in kind else ("Return_value",)
            matches = [row for row in page["fields"] if row["name"] in tokens
                       and str(row.get("schema_id", "")).startswith(prefixes)] if page else []
            result.append({"source": source, "consumed_field": field,
                           "status": "named field documented; hierarchy/type compatibility needs owned tests" if matches else
                           "UNCONFIRMED: field not individually typed, aggregate/result primitive, or absent source",
                           "matching_schema_nodes": matches})
    return result


def build_inventory() -> dict[str, Any]:
    snapshots = {name: snapshot(path) for name, path in INPUTS.items()}
    for target, snap in snapshots.items():
        expected = "27.0.0" if target.startswith("27-") else target
        if snap["manifest"].get("truenas_version", snap["manifest"].get("target_version")) != expected:
            raise ValueError(f"Snapshot {target} does not identify API {expected}")
    pages = {}
    for snap in snapshots.values():
        pages.update(snap["pages"])
    methods = [row["page"] for (kind, _), row in pages.items() if kind == "method"]
    events = [row["page"] for (kind, _), row in pages.items() if kind == "event"]
    metrics = current_contract()
    contract = json.loads((ROOT / "docs/metrics-contract.json").read_text())["metrics"]
    if sorted(contract, key=lambda row: row["name"]) != metrics:
        raise ValueError("Metric contract differs from source declarations; regenerate the existing contract first")
    analysis = parity.analyze_source(methods, events, {metric["variable"] for metric in metrics})
    literal_refs: dict[tuple[str, str], list[str]] = defaultdict(list)
    for relative in ("runtime.py", "transport.py", "events.py", "method_safety.py"):
        source_path = ROOT / "src/truenas_exporter" / relative
        for node in ast.walk(ast.parse(source_path.read_text())):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                for kind in ("method", "event"):
                    if (kind, node.value) in pages:
                        literal_refs[(kind, node.value)].append(
                            f"src/truenas_exporter/{relative}:{node.lineno}")
    historical = json.loads((ROOT / "docs/api-exporter-parity.json").read_text())
    mappings = {row["variable"]: row for row in historical["field_mappings"]}
    references = panel_references()
    metric_rows = []
    for metric in metrics:
        mapping = mappings.get(metric["variable"])
        if mapping:
            sources = mapping["api_method_or_event"]
            kind = mapping["source_kind"]
            fields = mapping["response_field"]
            status = mapping["implementation_status"]
            explicit = (metric["variable"] in parity._metric_source_overrides()
                        or metric["variable"] in parity.EVENT_SOURCE_OVERRIDES
                        or metric["variable"] in parity.INTERNAL_VARIABLES)
            mapping_evidence = ("explicit existing parity ownership mapping; static, not live verification" if explicit
                                else "historical static AST/function candidate association; ownership requires source/test review")
        else:
            kind, inferred = parity.infer_metric_sources(metric["variable"], analysis)
            sources = list(inferred) or ["exporter-owned state"]
            fields = list(parity.owned_response_fields(metric["variable"], tuple(inferred), analysis))
            status = "current source declaration; new mapping requires owned test"
            mapping_evidence = "static current AST/function association; verify ownership in tests"
        if metric["variable"] == "POOL_FREEING_BYTES":
            sources, kind, fields = ["pool.query"], "method", ["freeing"]
            status = "new TrueNAS26/27 producer; not part of historical 25.10 contract"
            mapping_evidence = "explicit nullable integer byte field in 26 and both 27 pool.query schemas; same selected call, no additional request"
        if metric["variable"] in {"GENERIC_SERIES", "GENERIC_SERIES_LIMIT_HITS"}:
            sources, kind, fields = ["exporter-owned state"], "internal", ["generic extraction series budget state"]
            mapping_evidence = "explicit current generic extraction accounting; no additional API call"
        if metric["variable"] == "WEBSHARE_ENABLED":
            sources, kind, fields = ["webshare.config"], "method", ["enabled"]
            mapping_evidence = "explicit current _collect_app_extras webshare.config call"
        if metric["variable"] in {"VIRT_INSTANCE_CPU", "VIRT_INSTANCE_MEM"}:
            sources = ["container.metrics", "virt.instance.metrics"]
            kind = "event"
            mapping_evidence = "explicit current INSTANCE_METRICS_WIRE_ALIASES dispatch; payload leaf fields remain opaque/UNCONFIRMED"
        if metric["variable"] in {"VIRT_INSTANCE_COUNT", "VIRT_INSTANCE_RUNNING"}:
            sources = ["container.query", "virt.instance.query"]
            if metric["variable"] == "VIRT_INSTANCE_RUNNING":
                fields = ["status", "status.state"]
            mapping_evidence = "explicit version branch in current _collect_virt_metrics; container status.state versus legacy status"
        # Generic catalog lists are eligibility policies, not proof of calls.
        frequency, cost = schedule(sources, kind)
        status27 = {}
        for source in sources:
            if source == "exporter-owned state":
                continue
            key = ("event" if "event" in kind else "method", source)
            status27[source] = {name: key in snap["pages"] for name, snap in snapshots.items()}
        metric_rows.append({**metric, "unit": metric_unit(metric), "source_kind": kind,
                            "api_method_or_event": sources, "response_fields": fields,
                            "mapping_evidence": mapping_evidence, "historical_25_10_disposition": status,
                            "fixture_test_evidence": mapping["fixture_test"] if mapping else "new behavior; see current test suite",
                            "runtime_references": [f"src/truenas_exporter/runtime.py:{line}"
                                                   for line in analysis.metric_lines.get(metric["variable"], ())],
                            "frequency": frequency, "estimated_cost": cost,
                            "cardinality": cardinality(metric["labels"]),
                            "availability": status27, "dashboards": references.get(metric["name"], {}),
                            "field_verification_27_local": field_evidence(sources, fields, snapshots["27-local"]["pages"], kind),
                            "field_verification_27_official": field_evidence(sources, fields, snapshots["27-official"]["pages"], kind),
                            "live_verification": "NOT VERIFIED by this offline inventory"})
    used_methods = set(analysis.method_call_references) | set(analysis.base_methods)
    used_methods.update(name for kind, name in literal_refs if kind == "method")
    used_events = set(parity.SUBSCRIBED_EVENTS)
    used_events.update(name for kind, name in literal_refs if kind == "event" and ("method", name) not in pages)
    metric_by_source: dict[tuple[str, str], list[str]] = defaultdict(list)
    fields_by_source: dict[tuple[str, str], set[str]] = defaultdict(set)
    for metric in metric_rows:
        for source in metric["api_method_or_event"]:
            source_key = ("event" if "event" in metric["source_kind"] else "method", source)
            metric_by_source[source_key].append(metric["name"])
            fields_by_source[source_key].update(metric["response_fields"])
            if metric["source_kind"] == "event":
                used_events.add(source)
            elif ("generic" not in metric["source_kind"] and "event transport" not in metric["source_kind"]
                  and source != "exporter-owned state"):
                used_methods.add(source)
    used_methods = {name for name in used_methods if ("method", name) in pages or ("event", name) not in pages}
    # Include auth and event transport independently of dedicated metric mapping.
    for source in ("auth.login_with_api_key", "auth.login_ex", "core.subscribe", "core.unsubscribe", "system.version_short"):
        if source in analysis.method_call_references:
            used_methods.add(source)
    api_rows = []
    for kind, names in (("method", used_methods), ("event", used_events)):
        for name in sorted(names):
            key = kind, name
            evidence = {target: snap["pages"].get(key) for target, snap in snapshots.items()}
            local, official = evidence["27-local"], evidence["27-official"]
            if local and official:
                status = "documented in both 27 snapshots"
            elif local:
                status = "documented locally; absent from official 27 snapshot"
            elif official:
                status = "documented officially; absent from local 27 snapshot"
            else:
                status = "absent from both 27 snapshots; preserve contract and skip unsupported source"
            changes = {target: changed(evidence[target], local) for target in ("25.10.2", "26.0.0")}
            decisions = []
            if not local or not official:
                decisions.append("do not infer a replacement or live absence; retain metric family")
            if name.startswith("virt."):
                decisions.append("retain 25.10 profile; 26/27 use only explicitly owned container replacement fields")
            if name == "auth.login_ex":
                decisions.append("API_KEY_PLAIN requires username+key; require explicit response_type SUCCESS; never downgrade after rejection")
            if name == "auth.login_with_api_key":
                decisions.append("retain tested key-only compatibility; a documented method does not prove credential/server acceptance")
            if name in {"reporting.realtime", "app.stats", "container.metrics"}:
                decisions.append("resubscribe after reconnect, parse documented ADDED fields and enforce event TTL")
            if any(changes.values()):
                decisions.append("review changed metadata and test consumed fields; documentation digest changes alone are not breakage")
            if not decisions:
                decisions.append("retain reviewed read-only call; exercise selected fields with sanitized fixtures")
            api_rows.append({"kind": kind, "name": name,
                             "existing_use": ("reviewed subscription/owned event" if kind == "event" else
                                              "runtime reference/owned metric source" if name in analysis.method_call_references else
                                              "opt-in generic base plan" if name in analysis.base_methods else
                                              "static literal reference/retained ownership; producer availability requires source review"),
                             "source_references": sorted(set(literal_refs.get(key, ()))
                                                         | set(analysis.method_call_references.get(name, ()))),
                             "wire_parameter_evidence": list(analysis.method_params.get(name, ())),
                             "status": status, "affected_metrics": sorted(set(metric_by_source[key])),
                             "consumed_fields": sorted(fields_by_source[key]),
                             "required_change": decisions,
                             "changes_against_27_local": changes,
                             "local_official_signature_equal": signature(local) == signature(official),
                             "evidence": {target: None if row is None else {
                                 key: value for key, value in row.items() if key != "page"}
                                 for target, row in evidence.items()},
                             "verification": "offline documentation and static source; live behavior/permissions NOT VERIFIED"})
    manifests = {name: {"path": (root / "MANIFEST.json").relative_to(ROOT).as_posix(),
                        "sha256": snapshots[name]["manifest_sha256"],
                        "source_url": snapshots[name]["manifest"].get("source_url"),
                        "archive_sha256": snapshots[name]["manifest"].get("archive_sha256"),
                        "api_version": snapshots[name]["manifest"].get("truenas_version"),
                        "method_count": sum(kind == "method" for kind, _ in snapshots[name]["pages"]),
                        "event_count": sum(kind == "event" for kind, _ in snapshots[name]["pages"])}
                 for name, root in INPUTS.items()}
    digest_paths = [*DASHBOARDS, "docs/api-exporter-parity.json", "docs/metrics-contract.json",
                    "scripts/generate_api_exporter_parity.py", "scripts/generate_truenas27_review.py"]
    digest_paths += [path.relative_to(ROOT).as_posix() for path in sorted((ROOT / "src/truenas_exporter").glob("*.py"))]
    version_differences: dict[str, dict[str, Any]] = {}
    for old_target, new_target in (("25.10.2", "27-local"), ("26.0.0", "27-local"), ("27-local", "27-official")):
        version_differences[f"{old_target}_to_{new_target}"] = {}
        for kind in ("method", "event"):
            old_names = {name for page_kind, name in snapshots[old_target]["pages"] if page_kind == kind}
            new_names = {name for page_kind, name in snapshots[new_target]["pages"] if page_kind == kind}
            version_differences[f"{old_target}_to_{new_target}"][kind] = {
                "added": sorted(new_names - old_names), "removed": sorted(old_names - new_names)}
    config_defaults = {}
    for node in ast.walk(ast.parse((ROOT / "src/truenas_exporter/config.py").read_text())):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id == "_int_env" and len(node.args) >= 2):
            config_defaults[ast.literal_eval(node.args[0])] = int(ast.literal_eval(node.args[1]))
    return {"schema_version": 1, "generator": "scripts/generate_truenas27_review.py",
            "collection_defaults": dict(sorted(config_defaults.items())),
            "version_differences": version_differences,
            "evidence_boundary": "offline documentation/static ownership, never live acceptance",
            "snapshots": manifests, "input_sha256": {path: sha(ROOT / path) for path in digest_paths},
            "summary": {"metrics": len(metric_rows),
                        "local_official_used_signature_disagreements": sum(not row["local_official_signature_equal"] for row in api_rows),
                        "common_26_to27_parameter_changes": [row["name"] for row in api_rows
                            if row["evidence"]["26.0.0"] and row["evidence"]["27-local"]
                            and row["evidence"]["26.0.0"]["parameters"] != row["evidence"]["27-local"]["parameters"]],
                        "common_26_to27_role_changes": [row["name"] for row in api_rows
                            if row["evidence"]["26.0.0"] and row["evidence"]["27-local"]
                            and row["evidence"]["26.0.0"]["roles"] != row["evidence"]["27-local"]["roles"]], "used_or_retained_api_methods": len(used_methods),
                        "used_or_retained_events": len(used_events),
                        "metric_types": dict(Counter(metric["type"] for metric in metric_rows)),
                        "absent_both27": [row["kind"] + ":" + row["name"] for row in api_rows
                                          if not row["evidence"]["27-local"] and not row["evidence"]["27-official"]]},
            "api": api_rows, "metrics": metric_rows}


def escape(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def table(headers: list[str], rows: list[list[Any]]) -> str:
    return "\n".join(["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |",
                      *("| " + " | ".join(escape(cell) for cell in row) + " |" for row in rows)])


def compatibility_markdown(data: dict[str, Any]) -> str:
    sources = []
    for name, row in data["snapshots"].items():
        sources.append(f"- **{name}**: [{row['path']}](../../{row['path']}); {row['method_count']} methods, "
                       f"{row['event_count']} events. Manifest SHA256 `{row['sha256']}`; archive SHA256 `{row['archive_sha256'] or 'not recorded in historical snapshot'}`.")
    differences = [[name, kind, len(changes["added"]), len(changes["removed"])]
                   for name, kinds in data["version_differences"].items() for kind, changes in kinds.items()]
    rows = []
    for row in data["api"]:
        doc = row["evidence"]["27-local"] or row["evidence"]["27-official"]
        roles = (", ".join(doc["roles"]) or "not specified") if doc else "undocumented"
        parameters = ", ".join(f"{position}:{name}" for position, name in doc["parameters"]) if doc else "undocumented"
        proof = f"[27 schema](../../{doc['path']}); roles {roles}; params {parameters or 'none'}" if doc else "no 27 method/event leaf"
        rows.append([f"`{row['name']}` ({row['kind']})", row["existing_use"], row["status"],
                     ", ".join(f"`{name}`" for name in row["affected_metrics"]),
                     "; ".join(row["required_change"]), proof + "; live UNVERIFIED"])
    return "\n".join([
        "# TrueNAS 27 API compatibility", "", "Generated by `python3 scripts/generate_truenas27_review.py`; "
        "append `--check` for deterministic offline verification. Signature summaries, field metadata, schema references, source hashes, wire parameters "
        "and both dashboard mappings: [machine inventory](truenas27-inventory.json).", "",
        "## Evidence boundary", "", "The local and official documentation both identify API 27.0.0. That API identifier does not prove the exact appliance release. "
        "This report performs no network/API calls and records no operational payloads or credentials. Method presence proves documentation availability, "
        "not permissions, performance, response completeness, or live support. Existing 25/26 fixture successes are not live 27 evidence. "
        "The baseline key-only authentication attempt was rejected; read-only authorization and exact appliance release remain unverified.", "",
        *sources, "", "Historical Markdown records less schema hierarchy than the new converter. Field-name changes are review candidates, "
        "not automatic API breakage. `UNCONFIRMED` consumed-field entries deliberately preserve this distinction. "
        "Required roles are documentation requirements, not evidence the supplied account has those roles.", "",
        "## Documentation surface changes", "",
        table(["Comparison", "Kind", "Added", "Removed"], differences), "",
        "The complete added/removed-name lists are in the machine inventory. These include mutating and sensitive APIs: "
        "documentation discovery never authorizes them for collection. Names missing from a snapshot are documented absence, not proof of runtime removal.", "",
        "## Local and official disagreements", "",
        f"{data['summary']['local_official_used_signature_disagreements']} referenced method/event signatures differ between local and official snapshots "
        "(including absent surfaces). Expanded query-result variants account for many schema differences; they do not by themselves establish runtime breakage. "
        "The official reporting.realtime schema types additional per-core CPU/interface fields while the local snapshot leaves those objects opaque. "
        "Official zpool.query adds nested stats_ex fields; local audit.config includes an S3 enabled-service branch absent officially. "
        "Both signature summaries and source hashes remain in the machine inventory; full constraints and examples remain in the linked owning schema pages.", "",
        "Common 26-to-local-27 top-level parameter changes: " + (", ".join(data["summary"]["common_26_to27_parameter_changes"]) or "none found") + ". "
        "Required-role changes after normalizing historical separators: " + (", ".join(data["summary"]["common_26_to27_role_changes"]) or "none found") + ". "
        "This comparison does not prove nested schema/unit compatibility.", "",
        "## Migration decisions", "", "- Keep version-selected 25.10, 26.0 and 27 profiles. Never route unknown versions to the most permissive catalog.",
        "- Prefer documented `auth.login_ex`/`API_KEY_PLAIN` when a username is configured. Authentication succeeds only for explicit `SUCCESS`. "
        "Preserve the existing key-only path for older deployments, without automatic downgrade after rejection.",
        "- `virt.*` instance surfaces disappeared after 25.10. Use only reviewed `container.*` replacements and retain historical metric declarations; "
        "do not translate opaque payload fields by name similarity.",
        "- Reporting graph names must come from the pinned enum. Historical `reporting.graphs` prose references are not proof that a method exists; "
        "the 27 reporting graph enum omits historical ARC graphs `arcactualrate`, `arcrate`, `arcresult`.",
        "- Calls remain read-only and count/select projections remain mandatory for sensitive inventories. Optional failure must not suppress unrelated metrics.",
        "", "## Compatibility matrix", "", table(["API method/event", "Existing use", "TrueNAS 27 status", "Affected metrics", "Required change", "Verification"], rows),
        "", "## Validation and remaining acceptance", "", "The generator verifies documentation file digests, unique metric names and complete static inventory coverage. "
        "It does not execute JSON-RPC, authenticate, subscribe, or benchmark middleware. See [verification log](../modernization/README.md) for actual mocked/live runs. "
        "Authenticated read-only checks must independently verify the exact server release, role sufficiency, method responses and event recovery.", "",
    ])


def metrics_markdown(data: dict[str, Any]) -> str:
    rows = []
    for row in data["metrics"]:
        panels = "; ".join(f"{Path(path).name}: {', '.join(titles)}" for path, titles in row["dashboards"].items()) or "none"
        availability = "exporter state" if not row["availability"] else "; ".join(
            f"{source}: " + ("both 27 docs" if targets["27-local"] and targets["27-official"] else "UNCONFIRMED/absent in a 27 snapshot")
            for source, targets in row["availability"].items())
        # Generic catalog lists can contain hundreds of sources. They remain
        # complete in JSON without duplicating entire policy catalogs per cell.
        sources = ", ".join(row["api_method_or_event"])
        if "candidate association" in row["mapping_evidence"]:
            sources = "Static candidate: " + sources
        if "generic" in row["source_kind"] or "event transport" in row["source_kind"]:
            sources = f"{len(row['api_method_or_event'])} catalog entries; full list in machine inventory; runtime safety/profile gates apply"
            availability = "per-catalog-entry in machine inventory; eligibility does not imply enabled collection"
        rows.append([f"`{row['name']}`", row["help"], row["type"], row["unit"], ", ".join(row["labels"]) or "none",
                     sources, row["frequency"], row["cardinality"]["risk"] + "; " + row["cardinality"]["estimate"],
                     availability, panels])
    coverage = [
        ["System, uptime, CPU, memory", "system.info/system.state and reporting.realtime", "Retain owned system fields; omit unknown data, enforce reporting TTL", "low shared call + event stream"],
        ["Pools, VDEVs, scrub/resilver", "pool.query, zpool.query, pool.scrub.query", "Prioritize typed health/errors/capacity and bounded task outcomes", "shared query; topology grows with disks"],
        ["Datasets and snapshots", "pool.dataset.query, pool.snapshot.query", "Keep configured dataset/query limits and oldest snapshot cache; no per-snapshot identity labels", "medium/high; inventory/order-by costs unmeasured"],
        ["ZFS ARC/cache", "reporting.realtime documented payload and reporting.get_data enum", "Do not fabricate removed historical ARC graph ratios; keep only typed realtime fields", "shared event; unavailable graph semantics remain absent"],
        ["Disks, SMART, temperatures", "disk.query, disk.temperatures, disk.temperature_agg", "Read-only temperature/status only; no SMART test invocation; preserve cached history", "inventory plus batched/cached temperatures; hardware dependent"],
        ["Network/interfaces", "interface.query and reporting.realtime", "Retain rates as gauges; do not rate() instantaneous byte/s twice", "shared event; per-interface cardinality"],
        ["Services, SMB, NFS, iSCSI/NVMe", "service.query, smb.status, nfs.get_nfs3_clients/nfs.get_nfs4_clients and session counts", "Prefer count/select; no client usernames, peer addresses or share paths", "bounded server counts; session cost load dependent"],
        ["Apps and containers", "app.query/app.stats/container.query/container.metrics", "Typed app metrics are useful; container event payload fields can be opaque; no invented resource mapping", "event interval + bounded entities"],
        ["Virtual machines/instances", "vm.query and container.query/metrics; removed virt.*", "Retain prior version profile; test only explicitly documented replacement fields", "bounded entity reads; memory units require version fixtures"],
        ["Replication/scheduled jobs/alerts", "replication.query, core.get_jobs, alert.list, cronjob.query", "Use selected state/timestamps and bounded method enums; avoid arguments, logs and alert text", "bounded polling, no per-job UUID label"],
        ["UPS/hardware", "ups.config, reporting.get_data UPS enum, ipmi read surfaces", "Config availability is not measured battery/runtime; telemetry conditional on documented data and hardware", "hardware-specific; opt-in IPMI and reporting graphs"],
        ["Boot environments, updates, config", "boot.environment.query, update.* reviewed reads and selected config", "Retain bounded health/count/status; do not run update checks/actions that modify state", "low inventory; no proactive download/update"],
        ["Other 27 namespaces", "full method inventory in pinned docs", "Feature presence is not permission to export it; require typed useful scalar and sensitive-field review", "defer without a concrete low-cost signal"],
    ]
    legacy_gauges = [row["name"] for row in data["metrics"] if row["type"] == "gauge" and
                     any(term in row["help"].lower() for term in ("cumulative", "counter semantics"))]
    return "\n".join([
        "# TrueNAS 27 metric coverage", "", f"The current source declares **{len(data['metrics'])} metric families**. "
        "Every declaration appears once below and in [truenas27-inventory.json](truenas27-inventory.json), including exact HELP/type/labels, units, "
        "API sources, consumed fields, both dashboard references, frequency, cardinality risk and estimated cost. "
        "Source ownership reuses the explicit historical parity mappings; inferred associations and untyped fields are labelled. "
        "Documentation presence does not establish live availability.", "",
        "## Recommendations and priorities", "",
        "1. Restore compatibility and trustworthy freshness before expanding metric count: authenticate explicitly, isolate failures, bound call deadlines and expire event-only samples. "
        "This candidate adds `truenas_pool_freeing_bytes{pool}` from the nullable integer byte field `pool.query.freeing` for the 26/27 profiles, "
        "using the existing selected query; absent/null values are omitted and valid zero remains zero. It does not add middleware requests.",
        "2. Keep existing public names/types/HELP/labels. Existing cumulative app I/O gauges have counter-like semantics; dashboards should use rate()/increase() with resets. "
        "A future canonical `_total` counter requires an alias plus documented deprecation, not an in-place type change.",
        "3. Keep generic extraction opt-in and enforce a total series budget in addition to recursion/list limits; entity/path combinations multiply even when each response is bounded.",
        "4. Prefer bounded exporter self-monitoring (source series counts/drops, errors, durations and staleness) and typed storage health. Avoid user/share/session/path identifiers and arbitrary status/error text.",
        "5. Treat missing/null as absent or NaN, preserving valid zero/false. Do not replace unsupported hardware metrics with zero. Units are documented expectations; opaque response fields remain UNCONFIRMED.",
        "", "Legacy cumulative gauges: " + (", ".join(f"`{name}`" for name in legacy_gauges) or "none identified by HELP") + ".", "",
        "Current collection defaults (configuration may override them): " + ", ".join(
            f"`{name}={data['collection_defaults'][name]}`" for name in ("SCRAPE_INTERVAL_SECONDS", "SCRAPE_BUDGET_SECONDS",
                "QUERY_LIMIT", "MAX_METHOD_CALLS", "MAX_LIST_ITEMS", "MAX_ENTITY_CALLS", "MAX_DATASETS", "MAX_GENERIC_SERIES")
            if name in data["collection_defaults"]) + ". Per-source API work and generated series must remain inside these limits.", "",
        "## Domain coverage and collection costs", "", table(["Domain", "Documented sources", "Decision/gaps", "Estimated cost"], coverage),
        "", "Costs are qualitative code/documentation estimates, not server measurements. Polling results are shared where the existing cache does so; "
        "some optional collector paths can repeat calls. `/metrics` serves an in-memory snapshot rather than initiating middleware requests. "
        "The heavy temperature-history and oldest-snapshot refreshes occur every 10 polling cycles with a maximum 30-cycle cache age; "
        "general polling snapshots and event payloads have separate freshness policies. See runtime source for configurable budgets and gates.", "",
        "## Metric inventory", "", table(["Metric", "HELP", "Type", "Unit", "Labels", "API source", "Frequency", "Cardinality", "27 documentation", "Grafana references"], rows),
        "", "## Validation criteria", "", "Check all existing metric contracts for name/type/HELP/label stability; parse emitted exposition for duplicate series; "
        "test counters across scrapes and restarts, rates as gauges, absent/malformed values, TTL expiry and concurrent snapshots. "
        "Cardinality estimates describe label-domain products, not production sample counts. Dashboard string references prove static linkage, not successful rendering or PromQL behavior.", "",
        "## Primary guidance", "", "- [Prometheus exporter guidance](https://prometheus.io/docs/instrumenting/writing_exporters/): useful bounded metrics, base units and deliberate compatibility tradeoffs.",
        "- [Prometheus naming](https://prometheus.io/docs/practices/naming/): stable units, meaningful metric dimensions and limited label cardinality.",
        "- [Python client custom collectors](https://prometheus.github.io/client_python/collector/custom/): explicit collection families and avoiding unexpected collection at registration.",
        "- [Pinned local API](../api/truenas-27/README.md) and [official API](../api/truenas-27-official/README.md): source of method/schema claims.",
        "", "Regenerate: `python3 scripts/generate_truenas27_review.py`; verify without writing: `python3 scripts/generate_truenas27_review.py --check`. "
        "No network calls or live telemetry are used. Actual mocked/live checks belong in [verification evidence](../modernization/README.md).", "",
    ])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = build_inventory()
    if not args.check:
        OUT.mkdir(parents=True, exist_ok=True)
    for name, rendered in (
        ("truenas27-inventory.json", json.dumps(data, indent=2, sort_keys=True) + "\n"),
        ("truenas27-api-compatibility.md", compatibility_markdown(data)),
        ("truenas27-metric-coverage.md", metrics_markdown(data)),
    ):
        check_or_write(OUT / name, rendered, check=args.check, description=name)
    print(f"TrueNAS 27 reviews: {data['summary']['metrics']} metrics, "
          f"{data['summary']['used_or_retained_api_methods']} methods, {data['summary']['used_or_retained_events']} events")


if __name__ == "__main__":
    main()
