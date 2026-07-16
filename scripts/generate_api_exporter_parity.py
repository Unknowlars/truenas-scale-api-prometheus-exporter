#!/usr/bin/env python3
"""Generate target-aware TrueNAS API/exporter parity audits.

The generator treats the committed Markdown API snapshot, the documentation-
derived runtime safety catalog, the public metric contract, exporter source,
tests/fixtures, and the generated Grafana dashboard as its only inputs.  It
performs no network or live-system access.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from collections.abc import Iterable
from dataclasses import dataclass
from functools import cache
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_ROOT = REPO_ROOT / "docs" / "truenas-api"
MANIFEST_PATH = DOCS_ROOT / "MANIFEST.json"
METRIC_CONTRACT_PATH = REPO_ROOT / "docs" / "metrics-contract.json"
DASHBOARD_PATH = REPO_ROOT / "grafana-dashboard" / "operations-center-dashboard.json"
OUTPUT_MD = REPO_ROOT / "docs" / "api-exporter-parity.md"
OUTPUT_JSON = REPO_ROOT / "docs" / "api-exporter-parity.json"
V26_OUTPUT_MD = REPO_ROOT / "docs" / "api-exporter-parity-v26.md"
V26_OUTPUT_JSON = REPO_ROOT / "docs" / "api-exporter-parity-v26.json"
COMPAT_DIFF_MD = (
    REPO_ROOT / "docs" / "truenas-25-10-2-and-26-0-0-compatibility" / "api-compatibility-diff.md"
)
COMPAT_DIFF_JSON = (
    REPO_ROOT / "docs" / "truenas-25-10-2-and-26-0-0-compatibility" / "api-compatibility-diff.json"
)
TARGET_VERSION = "25.10.2"
EXPECTED_MANIFEST_FILE_COUNT = 1011
EXPECTED_TREE_FILE_COUNT = 1012
EXPECTED_MANIFEST_AGGREGATE = "e7870f3036a98d297d204591c2831b6fd7b26013b827634a66225421edd6c614"
EXPECTED_METHOD_COUNT = 767
EXPECTED_EVENT_COUNT = 63
EXPECTED_METHOD_NAMESPACE_COUNT = 114
EXPECTED_EVENT_NAMESPACE_COUNT = 60
EXPECTED_READ_ONLY_COUNT = 398
EXPECTED_TELEMETRY_CANDIDATE_COUNT = 112
EXPECTED_SENSITIVE_READ_COUNT = 60
EXPECTED_UNSAFE_GENERIC_READ_COUNT = 43
EXPECTED_UNSAFE_EVENT_COUNT = 60
EXPECTED_SAFE_EVENT_COUNT = 4
EXPECTED_READ_ONLY_SHA256 = "acaf4e4e414717dad624bd4c8dd18e4e97abb4d2953d32d2ea8a7bef473a6e57"
EXPECTED_EVENT_SHA256 = "b458465c72edaa77f4e6071751c079728b2e8f8e07d13b4021cdea26dcc42c62"
EXPECTED_CANDIDATE_SHA256 = "9ff25130a70d9e67d13b7443c5775e9936b27135f8f0fd17b729b8ceae1960c6"

sys.path.insert(0, str(REPO_ROOT / "src"))
from truenas_exporter.api_catalog import (  # noqa: E402
    API_DOCS_TARGET_VERSION,
    DEFAULT_SAFE_EVENT_SUBSCRIPTIONS,
    DOCUMENTED_EVENT_NAMES,
    READ_ONLY_METHOD_ALLOWLIST,
    SAFE_EVENT_SUBSCRIPTIONS,
    SENSITIVE_READ_METHODS,
    TELEMETRY_CANDIDATE_METHOD_ALLOWLIST,
    UNSAFE_EVENT_SUBSCRIPTIONS,
    UNSAFE_GENERIC_READ_METHODS,
)
from truenas_exporter.compat_profiles import PROFILE_26_0, V26_ADDED_EVENTS  # noqa: E402

try:  # noqa: E402
    from .tooling import TRUENAS_API_VERSION, check_or_write, resolve_api_docs_target
except ImportError:  # direct script execution
    from tooling import TRUENAS_API_VERSION, check_or_write, resolve_api_docs_target


METHOD_COLUMNS = (
    "Namespace",
    "Method",
    "Documented operation/type",
    "Read-only classification",
    "Exporter usage",
    "Parameters verified",
    "Response fields used",
    "Dedicated metrics",
    "Generic coverage",
    "Dashboard usage",
    "Decision",
    "Evidence/notes",
)

UNSAFE_ACTION_OPERATIONS = frozenset(
    {
        "attach_ticket",
        "bulk",
        "debug",
        "download",
        "download_report",
        "export",
        "export_disk_image",
        "export_key",
        "export_keys",
        "export_keys_for_replication",
        "file",
        "generate_claim_token",
        "generate_key",
        "generate_onetime_password",
        "generate_ssh_key_pair",
        "generate_token",
        "get_console",
        "get",
        "import_find",
        "job_abort",
        "job_download_logs",
        "job_wait",
        "list_buckets",
        "log_file_download",
        "login",
        "login_ex",
        "login_ex_continue",
        "login_with_api_key",
        "login_with_token",
        "logout",
        "new_ticket",
        "onedrive_list_drives",
        "ping_remote",
        "remote_ssh_host_key_scan",
        "remote_ssh_semiautomatic_setup",
        "resize_shell",
        "subscribe",
        "test",
        "unsubscribe",
        "verify",
    }
)

EXTERNAL_ENTITY_METHODS = frozenset(
    {
        "catalog.apps",
        "catalog.get_app_details",
        "certificate.acme_server_choices",
        "cloudsync.list_directory",
        "pool.get_disks",
        "replication.list_datasets",
        "replication.list_naming_schemas",
        "replication.list_snapshots",
        "replication.target_unmatched_snapshots",
        "support.similar_issues",
        "vmware.get_datastores",
        "vmware.match_datastores_with_datasets",
    }
)

HIGH_CARDINALITY_METHODS = frozenset(
    {
        "alert.list",
        "app.available",
        "app.container_ids",
        "app.image.query",
        "app.query",
        "auth.sessions",
        "core.arp",
        "core.processes",
        "filesystem.getacl",
        "filesystem.list_directory",
        "filesystem.listdir",
        "filesystem.stat",
        "group.get_group_obj",
        "group.query",
        "iscsi.global.sessions",
        "nfs.get_nfs3_clients",
        "nfs.get_nfs4_clients",
        "nvmet.global.sessions",
        "pool.dataset.get_quota",
        "pool.snapshot.query",
        "reporting.netdata_get_data",
        "service.processes",
        "user.get_user_obj",
        "user.query",
        "zfs.resource.query",
    }
)

RAW_CONTENT_METHODS = frozenset(
    {
        "audit.query",
        "core.get_methods",
        "core.get_services",
        "filesystem.listdir",
        "truenas.get_eula",
        "vm.log_file_path",
    }
)

RAW_EVENTS = frozenset({"app.container_log_follow", "filesystem.file_tail_follow"})
SECRET_EVENTS = frozenset(
    {
        "acme.dns.authenticator.query",
        "alertservice.query",
        "api_key.query",
        "app.query",
        "app.registry.query",
        "certificate.query",
        "cloud_backup.query",
        "cloudsync.credentials.query",
        "cloudsync.query",
        "core.get_jobs",
        "iscsi.auth.query",
        "jbof.query",
        "kerberos.keytab.query",
        "keychaincredential.query",
        "nvmet.host.query",
        "nvmet.host_subsys.query",
        "replication.query",
        "rsynctask.query",
        "user.query",
        "virt.instance.query",
        "vm.query",
        "vmware.query",
    }
)
HIGH_CARDINALITY_EVENTS = frozenset(
    {
        "app.image.query",
        "group.query",
        "pool.dataset.query",
        "pool.snapshot.query",
        "user.query",
        "vm.device.query",
        "vmware.query",
    }
)
TELEMETRY_EVENTS = frozenset(
    {
        "alert.list",
        "app.query",
        "app.stats",
        "container.metrics",
        "core.get_jobs",
        "fcport.query",
        "interface.query",
        "jbof.query",
        "pool.query",
        "pool.scrub.query",
        "reporting.realtime",
        "service.query",
        "update.status",
        "virt.instance.metrics",
        "virt.instance.query",
        "vm.query",
    }
)
SUBSCRIBED_EVENTS = frozenset(DEFAULT_SAFE_EVENT_SUBSCRIPTIONS)
ACTIVE_DEDICATED_EVENT_METRIC_SOURCES = frozenset(
    {"reporting.realtime", "app.stats", "virt.instance.metrics"}
)

MANUAL_GENERIC_METHODS = frozenset(
    {
        "app.outdated_docker_images",
        "filesystem.get_zfs_attributes",
        "filesystem.getacl",
        "filesystem.listdir",
        "filesystem.stat",
        "ipmi.lan.query",
        "reporting.graphs",
        "reporting.netdata_graphs",
        "vm.get_memory_usage",
        "vm.get_vm_memory_info",
    }
)

DEPRECATED_METRICS: dict[str, str] = {
    "POOL_DEDUP_RATIO": (
        "Deprecated compatibility metric: no documented ratio source in TrueNAS "
        "25.10/26.0; declared for one release but intentionally absent. Use "
        "truenas_pool_dedup_table_size_bytes for DDT size."
    ),
    "NETWORK_GATEWAY_REACHABLE": (
        "Compatibility alias: the documented route inventory proves configuration, not "
        "reachability; use truenas_network_default_gateway_configured."
    ),
    "BOOT_ENV_SIZE_BYTES": (
        "Compatibility alias with the historical shorter name; use truenas_boot_environment_used_bytes."
    ),
    "POOL_EXPAND_SIZE_BYTES": ("Compatibility alias for bytes_to_reflow; use truenas_pool_expand_to_reflow_bytes."),
    "VM_FLAG_AMD_ASIDS": (
        "Compatibility numeric flag; use truenas_vm_flag_amd_asids_supported for the bounded boolean."
    ),
    "DIRECTORYSERVICES_FAULT_REASON": (
        "Compatibility label metric; use truenas_directoryservices_fault_present for bounded alerting."
    ),
    "CERT_DAYS_TO_EXPIRY": (
        "Compatibility metric retains an issuer label that 25.10.2 cannot source reliably; "
        "use truenas_certificate_expiry_timestamp_seconds."
    ),
}

GENERIC_METHOD_VARIABLES = frozenset(
    {"METHOD_NUMERIC_VALUE", "METHOD_BOOLEAN_VALUE", "METHOD_STATUS_VALUE", "METHOD_LIST_LENGTH"}
)
GENERIC_EVENT_VARIABLES = frozenset(
    {"EVENT_NUMERIC_VALUE", "EVENT_BOOLEAN_VALUE", "EVENT_STATUS_VALUE", "EVENT_LIST_LENGTH"}
)
INTERNAL_VARIABLES = frozenset(
    {
        "SCRAPE_SUCCESS",
        "LAST_SCRAPE_TS",
        "SCRAPE_DURATION",
        "API_CALL_SUCCESS",
        "API_CALL_DURATION",
        "API_CALL_ERRORS_TOTAL",
        "EXPORTER_INFO",
        "COLLECTOR_ERRORS_TOTAL",
        "FILESYSTEM_PATH_COUNT",
    }
)
EVENT_TRANSPORT_VARIABLES = frozenset({"EVENT_STREAM_UP", "EVENT_LAST_MESSAGE_TS", "EVENT_MESSAGES_TOTAL"})


DOMAIN_GROUPS: dict[str, frozenset[str]] = {
    "system/platform state and security": frozenset(
        {
            "system",
            "system.advanced",
            "system.general",
            "system.global",
            "system.reboot",
            "system.security",
            "system.security.info",
            "truenas",
        }
    ),
    "CPU/memory/load/reporting": frozenset({"reporting", "reporting.exporters"}),
    "storage/pools/disks/snapshots": frozenset(
        {
            "boot",
            "boot.environment",
            "disk",
            "pool",
            "pool.dataset",
            "pool.resilver",
            "pool.scrub",
            "pool.snapshot",
            "pool.snapshottask",
            "systemdataset",
            "zfs.resource",
        }
    ),
    "network/routes/DNS/NTP": frozenset(
        {"dns", "interface", "network.configuration", "network.general", "route", "staticroute", "system.ntpserver"}
    ),
    "file/block sharing protocols": frozenset(
        {
            "fc.fc_host",
            "fcport",
            "ftp",
            "iscsi.auth",
            "iscsi.extent",
            "iscsi.global",
            "iscsi.initiator",
            "iscsi.portal",
            "iscsi.target",
            "iscsi.targetextent",
            "nfs",
            "nvmet.global",
            "nvmet.host",
            "nvmet.host_subsys",
            "nvmet.namespace",
            "nvmet.port",
            "nvmet.port_subsys",
            "nvmet.subsys",
            "sharing.nfs",
            "sharing.smb",
            "smb",
            "snmp",
            "ssh",
        }
    ),
    "services": frozenset({"service"}),
    "apps/containers/catalogs": frozenset(
        {"app", "app.image", "app.ix_volume", "app.registry", "catalog", "docker", "docker.network"}
    ),
    "virtualization": frozenset(
        {
            "hardware.virtualization",
            "virt.device",
            "virt.global",
            "virt.instance",
            "virt.volume",
            "vm",
            "vm.device",
            "vmware",
        }
    ),
    "data protection/scheduled tasks": frozenset(
        {
            "cloud_backup",
            "cloudsync",
            "cloudsync.credentials",
            "cronjob",
            "initshutdownscript",
            "replication",
            "replication.config",
            "rsynctask",
        }
    ),
    "alerts/jobs/audit": frozenset({"alert", "alertclasses", "alertservice", "audit", "core"}),
    "certificates/ACME": frozenset({"acme.dns.authenticator", "certificate"}),
    "directory services/Kerberos": frozenset(
        {"directoryservices", "idmap", "kerberos", "kerberos.keytab", "kerberos.realm"}
    ),
    "identity/auth/security posture": frozenset(
        {"api_key", "auth", "auth.twofactor", "group", "keychaincredential", "privilege", "user"}
    ),
    "hardware/UPS/IPMI/GPU/JBOF": frozenset(
        {"device", "enclosure.label", "ipmi", "ipmi.chassis", "ipmi.lan", "ipmi.sel", "jbof", "ups"}
    ),
    "updates/support/TrueCommand": frozenset({"support", "tn_connect", "truecommand", "update"}),
    "failover/high availability": frozenset({"failover.disabled", "failover.reboot"}),
    "filesystem/path operations": frozenset({"filesystem", "filesystem.acltemplate"}),
    "additional configuration/key management": frozenset({"config", "kmip", "mail", "tunable"}),
}


@dataclass(frozen=True)
class ApiPage:
    path: str
    title: str
    kind: str
    summary: str
    roles: tuple[str, ...]
    parameters: tuple[tuple[int, str], ...]
    return_schema: str
    return_type: str
    fields: dict[str, tuple[str, ...]]
    event_shapes: tuple[str, ...]
    job: bool


@dataclass(frozen=True)
class SourceAnalysis:
    method_references: dict[str, tuple[str, ...]]
    method_call_references: dict[str, tuple[str, ...]]
    method_params: dict[str, tuple[str, ...]]
    metric_functions: dict[str, tuple[str, ...]]
    function_methods: dict[str, tuple[str, ...]]
    metric_lines: dict[str, tuple[int, ...]]
    functional_metric_variables: frozenset[str]
    base_methods: frozenset[str]


@dataclass(frozen=True)
class TargetInventory:
    target_version: str
    docs_root: Path
    manifest_path: Path
    manifest: dict[str, Any]
    file_rows: list[dict[str, Any]]
    methods: list[ApiPage]
    events: list[ApiPage]
    evidence: dict[str, Any]


def _stable_set_sha(values: Iterable[str]) -> str:
    return hashlib.sha256(("\n".join(sorted(values)) + "\n").encode()).hexdigest()


def _clean_text(value: str) -> str:
    return " ".join(value.strip().split())


def _summary_excerpt(value: str, limit: int = 360) -> str:
    # Evidence links and schema metadata remain authoritative. Exclude embedded
    # request examples (which can contain credential-shaped placeholders) and
    # bound prose so the exhaustive table stays reviewable.
    prose = re.split(r"\.\.\s+examples?\b|:::\w+|```", value, maxsplit=1, flags=re.I)[0]
    cleaned = _clean_text(prose)
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[:limit].rsplit(" ", 1)[0] + "…"


def _md_escape(value: Any) -> str:
    text = str(value).replace("|", "\\|").replace("\n", " ")
    return _clean_text(text)


def _frontmatter(text: str) -> dict[str, Any]:
    if not text.startswith("---\n"):
        return {}
    header, marker, _ = text[4:].partition("\n---\n")
    if not marker:
        return {}
    result: dict[str, Any] = {}
    current = ""
    for line in header.splitlines():
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*?)\s*$", line)
        if match:
            current, value = match.groups()
            result[current] = value
        elif current and line.startswith("  - "):
            if not isinstance(result[current], list):
                result[current] = []
            result[current].append(line[4:].strip())
    return result


def _section(text: str, heading: str, next_heading_level: int) -> str:
    pattern = rf"^{re.escape(heading)}\s*$\n(.*?)(?=^#{{1,{next_heading_level}}}\s|\Z)"
    match = re.search(pattern, text, re.M | re.S)
    return match.group(1) if match else ""


def _parse_field_types(schema_text: str) -> dict[str, tuple[str, ...]]:
    fields: dict[str, set[str]] = defaultdict(set)
    headings = list(re.finditer(r"^(#{4,10})\s+(.+?)\s*$", schema_text, re.M))
    ignored = {"Any of", "Additional Properties", "Each item of this array must be:"}
    for index, match in enumerate(headings):
        raw = re.sub(r"\s+\(required\)$", "", match.group(2)).strip()
        if raw in ignored or raw.startswith("Option ") or raw.startswith("Parameter "):
            continue
        end = headings[index + 1].start() if index + 1 < len(headings) else len(schema_text)
        block = schema_text[match.end() : end]
        type_match = re.search(r"^- Type:\s*(.+?)\s*$", block, re.M)
        if type_match:
            fields[raw].add(type_match.group(1).strip())
    return {key: tuple(sorted(values)) for key, values in sorted(fields.items())}


def parse_api_page(path: Path, docs_root: Path = DOCS_ROOT) -> ApiPage:
    text = path.read_text(encoding="utf-8")
    front = _frontmatter(text)
    summary = _section(text, "## Summary", 2)
    call_text = _section(text, "### Call parameters", 3)
    return_text = _section(text, "### Return value", 3)
    params = tuple(
        (int(position), name.strip())
        for position, name in re.findall(r"^#### Parameter (\d+):\s*(.+?)\s*$", call_text, re.M)
    )
    schema_match = re.search(r"^- Schema name:\s*`([^`]+)`\s*$", return_text, re.M)
    type_match = re.search(r"^- Type:\s*(.+?)\s*$", return_text, re.M)
    roles_value = front.get("required_roles", [])
    roles = tuple(roles_value) if isinstance(roles_value, list) else ()
    event_shapes = tuple(re.findall(r"^###\s+([^\n]+)$", _section(text, "## Schema", 2), re.M))
    return ApiPage(
        path=path.relative_to(docs_root).as_posix(),
        title=str(front.get("title", "")),
        kind=str(front.get("kind", "")),
        summary=_summary_excerpt(summary),
        roles=roles,
        parameters=params,
        return_schema=schema_match.group(1) if schema_match else "",
        return_type=type_match.group(1) if type_match else "",
        fields=_parse_field_types(return_text or _section(text, "## Schema", 2)),
        event_shapes=event_shapes,
        job="This method is a job" in text,
    )


def _target_docs_root(target_version: str) -> Path:
    return REPO_ROOT / "docs" / resolve_api_docs_target(target_version).docs_dir


def _manifest_target_version(manifest: dict[str, Any]) -> str:
    return str(manifest.get("target_version") or manifest.get("truenas_version") or "")


def inventory_docs_for_target(target_version: str) -> TargetInventory:
    docs_root = _target_docs_root(target_version)
    manifest_path = docs_root / "MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if _manifest_target_version(manifest) != target_version:
        raise ValueError(f"API manifest target must be {target_version}")

    listed = {entry["path"]: entry for entry in manifest["files"]}
    disk_files = sorted(path for path in docs_root.rglob("*") if path.is_file())
    disk_relative = {path.relative_to(docs_root).as_posix() for path in disk_files}
    if disk_relative - {"MANIFEST.json"} != set(listed):
        raise ValueError(f"{target_version} manifest paths and committed API documentation paths differ")

    aggregate = hashlib.sha256()
    file_rows: list[dict[str, Any]] = []
    pages: list[ApiPage] = []
    for path in disk_files:
        relative = path.relative_to(docs_root).as_posix()
        data = path.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        entry = listed.get(relative)
        if entry is not None:
            if entry["sha256"] != digest or entry["bytes"] != len(data):
                raise ValueError(f"{target_version} API documentation hash/size mismatch: {relative}")
            aggregate.update(relative.encode("utf-8"))
            aggregate.update(b"\0")
            aggregate.update(digest.encode("ascii"))
            aggregate.update(b"\n")

        document_class = "manifest (self-excluded)"
        title = ""
        kind = ""
        if path.suffix == ".md":
            text = data.decode("utf-8")
            front = _frontmatter(text)
            title = str(front.get("title", ""))
            kind = str(front.get("kind", ""))
            if relative == "README.md":
                document_class = "snapshot README"
            elif relative.endswith("/index.md"):
                document_class = f"{relative.split('/', 1)[0]} namespace/index"
            elif kind:
                document_class = f"{kind} leaf"
                pages.append(parse_api_page(path, docs_root))
            else:
                raise ValueError(f"unclassified API Markdown file: {relative}")
        file_rows.append(
            {
                "path": relative,
                "document_class": document_class,
                "title": title,
                "kind": kind,
                "bytes": len(data),
                "sha256": digest,
                "manifest_tracked": entry is not None,
                "manifest_hash_and_size_match": entry is not None,
            }
        )

    if aggregate.hexdigest() != manifest["aggregate_sha256"]:
        raise ValueError(f"{target_version} documentation aggregate changed; regenerate the manifest first")
    if len(listed) != manifest["file_count"]:
        raise ValueError(f"{target_version} manifest file count does not match listed files")

    methods = sorted((page for page in pages if page.kind == "method"), key=lambda page: page.title)
    events = sorted((page for page in pages if page.kind == "event"), key=lambda page: page.title)
    shared = [page for page in pages if page.kind == "shared"]
    if len({page.title for page in methods}) != len(methods):
        raise ValueError(f"duplicate method titles in {target_version} API documentation")
    if len({page.title for page in events}) != len(events):
        raise ValueError(f"duplicate event titles in {target_version} API documentation")

    method_namespaces = {page.title.rsplit(".", 1)[0] for page in methods}
    event_namespaces = {page.title.rsplit(".", 1)[0] for page in events}
    evidence = {
        "target_version": target_version,
        "manifest_schema_version": manifest.get("schema_version"),
        "manifest_file_count": manifest["file_count"],
        "tree_file_count_including_manifest": len(file_rows),
        "manifest_aggregate_sha256": manifest["aggregate_sha256"],
        "method_leaf_count": len(methods),
        "event_leaf_count": len(events),
        "shared_leaf_count": len(shared),
        "method_namespace_count": len(method_namespaces),
        "event_namespace_count": len(event_namespaces),
        "docs_path": docs_root.relative_to(REPO_ROOT).as_posix(),
        "manifest_path": manifest_path.relative_to(REPO_ROOT).as_posix(),
    }
    return TargetInventory(target_version, docs_root, manifest_path, manifest, file_rows, methods, events, evidence)


def inventory_docs() -> tuple[list[dict[str, Any]], list[ApiPage], list[ApiPage], dict[str, Any]]:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if manifest.get("truenas_version") != TARGET_VERSION:
        raise ValueError(f"API manifest target must be {TARGET_VERSION}")
    if manifest.get("file_count") != EXPECTED_MANIFEST_FILE_COUNT:
        raise ValueError("API manifest file count changed; re-audit the complete snapshot")
    if manifest.get("aggregate_sha256") != EXPECTED_MANIFEST_AGGREGATE:
        raise ValueError("API documentation aggregate changed; a new parity audit is required")

    listed = {entry["path"]: entry for entry in manifest["files"]}
    disk_files = sorted(path for path in DOCS_ROOT.rglob("*") if path.is_file())
    if len(disk_files) != EXPECTED_TREE_FILE_COUNT:
        raise ValueError(f"expected {EXPECTED_TREE_FILE_COUNT} API-doc tree files, found {len(disk_files)}")
    disk_relative = {path.relative_to(DOCS_ROOT).as_posix() for path in disk_files}
    if disk_relative - {"MANIFEST.json"} != set(listed):
        raise ValueError("manifest paths and committed API documentation paths differ")

    file_rows: list[dict[str, Any]] = []
    pages: list[ApiPage] = []
    for path in disk_files:
        relative = path.relative_to(DOCS_ROOT).as_posix()
        data = path.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        entry = listed.get(relative)
        if entry is not None and (entry["sha256"] != digest or entry["bytes"] != len(data)):
            raise ValueError(f"API documentation hash/size mismatch: {relative}")

        document_class = "manifest (self-excluded)"
        title = ""
        kind = ""
        if path.suffix == ".md":
            text = data.decode("utf-8")
            front = _frontmatter(text)
            title = str(front.get("title", ""))
            kind = str(front.get("kind", ""))
            if relative == "README.md":
                document_class = "snapshot README"
            elif relative.endswith("/index.md"):
                document_class = f"{relative.split('/', 1)[0]} namespace/index"
            elif kind:
                document_class = f"{kind} leaf"
                pages.append(parse_api_page(path))
            else:
                raise ValueError(f"unclassified API Markdown file: {relative}")
        file_rows.append(
            {
                "path": relative,
                "document_class": document_class,
                "title": title,
                "kind": kind,
                "bytes": len(data),
                "sha256": digest,
                "manifest_tracked": entry is not None,
                "manifest_hash_and_size_match": entry is not None,
            }
        )

    methods = sorted((page for page in pages if page.kind == "method"), key=lambda page: page.title)
    events = sorted((page for page in pages if page.kind == "event"), key=lambda page: page.title)
    shared = [page for page in pages if page.kind == "shared"]
    if len(methods) != EXPECTED_METHOD_COUNT or len(events) != EXPECTED_EVENT_COUNT or len(shared) != 3:
        raise ValueError("API method/event/shared leaf counts changed")
    if len({page.title for page in methods}) != EXPECTED_METHOD_COUNT:
        raise ValueError("duplicate method titles in API documentation")
    if len({page.title for page in events}) != EXPECTED_EVENT_COUNT:
        raise ValueError("duplicate event titles in API documentation")

    method_names = {page.title for page in methods}
    event_names = {page.title for page in events}
    if method_names & set(READ_ONLY_METHOD_ALLOWLIST) != set(READ_ONLY_METHOD_ALLOWLIST):
        raise ValueError("runtime read-only catalog contains undocumented methods")
    if len(READ_ONLY_METHOD_ALLOWLIST) != EXPECTED_READ_ONLY_COUNT:
        raise ValueError("read-only catalog count changed")
    if _stable_set_sha(READ_ONLY_METHOD_ALLOWLIST) != EXPECTED_READ_ONLY_SHA256:
        raise ValueError("read-only catalog changed without a new documentation audit")
    documented_v25_events = set(DOCUMENTED_EVENT_NAMES) - set(V26_ADDED_EVENTS)
    documented_union_events = documented_v25_events | set(V26_ADDED_EVENTS)
    if event_names != documented_v25_events:
        raise ValueError("runtime 25.10 event catalog differs from documented event leaves")
    if set(DOCUMENTED_EVENT_NAMES) != documented_union_events:
        raise ValueError("runtime event catalog contains events outside reviewed target profiles")
    if _stable_set_sha(event_names) != EXPECTED_EVENT_SHA256:
        raise ValueError("25.10 documented event catalog changed without a new audit")
    if len(SENSITIVE_READ_METHODS) != EXPECTED_SENSITIVE_READ_COUNT:
        raise ValueError("sensitive read catalog count changed; re-audit full-response exposure")
    if len(UNSAFE_GENERIC_READ_METHODS) != EXPECTED_UNSAFE_GENERIC_READ_COUNT:
        raise ValueError("unsafe generic-read catalog count changed; re-audit full-response semantics")
    if len(UNSAFE_EVENT_SUBSCRIPTIONS) != EXPECTED_UNSAFE_EVENT_COUNT:
        raise ValueError("unsafe event catalog count changed; re-audit subscription exposure")
    if len(SAFE_EVENT_SUBSCRIPTIONS) != EXPECTED_SAFE_EVENT_COUNT:
        raise ValueError("safe event catalog count changed; re-audit subscription exposure")
    if set(DOCUMENTED_EVENT_NAMES) != SAFE_EVENT_SUBSCRIPTIONS | UNSAFE_EVENT_SUBSCRIPTIONS:
        raise ValueError("safe/unsafe event catalogs must partition every reviewed event")
    if SAFE_EVENT_SUBSCRIPTIONS & UNSAFE_EVENT_SUBSCRIPTIONS:
        raise ValueError("safe and unsafe event catalogs must be disjoint")
    if not SECRET_EVENTS <= UNSAFE_EVENT_SUBSCRIPTIONS:
        raise ValueError("secret-bearing events must be prohibited subscriptions")
    if frozenset({"reporting.realtime", "app.stats", "virt.instance.metrics", "container.metrics"}) != SUBSCRIBED_EVENTS:
        raise ValueError("default subscriptions must remain the bounded dedicated event handlers")
    if not SUBSCRIBED_EVENTS <= SAFE_EVENT_SUBSCRIPTIONS:
        raise ValueError("default event subscriptions must be documentation-reviewed safe events")
    if len(TELEMETRY_CANDIDATE_METHOD_ALLOWLIST) != EXPECTED_TELEMETRY_CANDIDATE_COUNT:
        raise ValueError("telemetry candidate catalog count changed")
    if _stable_set_sha(TELEMETRY_CANDIDATE_METHOD_ALLOWLIST) != EXPECTED_CANDIDATE_SHA256:
        raise ValueError("telemetry candidate catalog differs from the 112-row audit classification")
    if not set(TELEMETRY_CANDIDATE_METHOD_ALLOWLIST) <= set(READ_ONLY_METHOD_ALLOWLIST):
        raise ValueError("telemetry candidates must be a subset of documented reads")
    if API_DOCS_TARGET_VERSION != TARGET_VERSION:
        raise ValueError("runtime API safety catalog target differs from documentation target")

    method_namespaces = {page.title.rsplit(".", 1)[0] for page in methods}
    event_namespaces = {page.title.rsplit(".", 1)[0] for page in events}
    if len(method_namespaces) != EXPECTED_METHOD_NAMESPACE_COUNT:
        raise ValueError("method namespace count changed")
    if len(event_namespaces) != EXPECTED_EVENT_NAMESPACE_COUNT:
        raise ValueError("event namespace count changed")
    grouped_namespaces = set().union(*DOMAIN_GROUPS.values())
    duplicate_namespaces = sum((Counter(ns for values in DOMAIN_GROUPS.values() for ns in values).values()), 0)
    if grouped_namespaces != method_namespaces or duplicate_namespaces != len(grouped_namespaces):
        raise ValueError("required-domain mapping must assign every namespace exactly once")

    evidence = {
        "target_version": TARGET_VERSION,
        "manifest_schema_version": manifest.get("schema_version"),
        "manifest_file_count": manifest["file_count"],
        "tree_file_count_including_manifest": len(file_rows),
        "manifest_aggregate_sha256": manifest["aggregate_sha256"],
        "method_leaf_count": len(methods),
        "event_leaf_count": len(events),
        "shared_leaf_count": len(shared),
        "method_namespace_count": len(method_namespaces),
        "event_namespace_count": len(event_namespaces),
        "read_only_allowlist_count": len(READ_ONLY_METHOD_ALLOWLIST),
        "sensitive_read_count": len(SENSITIVE_READ_METHODS),
        "unsafe_generic_read_count": len(UNSAFE_GENERIC_READ_METHODS),
        "telemetry_candidate_allowlist_count": len(TELEMETRY_CANDIDATE_METHOD_ALLOWLIST),
        "safe_event_count": len(SAFE_EVENT_SUBSCRIPTIONS),
        "unsafe_event_count": len(UNSAFE_EVENT_SUBSCRIPTIONS),
        "default_event_subscription_count": len(SUBSCRIBED_EVENTS),
    }
    return file_rows, methods, events, evidence


def _call_name(call: ast.Call) -> str:
    if isinstance(call.func, ast.Attribute):
        return call.func.attr
    if isinstance(call.func, ast.Name):
        return call.func.id
    return ""


def _auto_params_evidence(method: str) -> str:
    exact = {
        "app.query": (
            "[[], {limit: query_limit, select: [name, state, upgrade_available, "
            "image_updates_available, custom_app, migrated, active_workloads]}]"
        ),
        "disk.query": ("[[], {limit: query_limit, select: [name, identifier, size, type, rotationrate, pool]}]"),
        "vm.query": "[[], {limit: query_limit, select: [id, name, status, autostart, vcpus, memory]}]",
        "alertservice.query": "[[], {limit: query_limit, select: [id, name, type__title, enabled]}]",
        "disk.details": "[{}]",
        "ipmi.chassis.info": "[{}]",
        "zfs.resource.query": "[{}]",
        "vm.get_available_memory": "[false]",
        "reporting.graph": "[cpu, {unit: HOURLY}]",
        "reporting.netdata_graph": "[cpu, {unit: HOURLY}]",
    }
    if method in exact:
        return exact[method]
    if method.endswith(".query"):
        return "[[], {limit: query_limit}]"
    if method in {
        "nfs.get_nfs3_clients",
        "nfs.get_nfs4_clients",
        "iscsi.global.sessions",
        "route.system_routes",
        "core.get_jobs",
    }:
        return "[[], {limit: query_limit}]"
    return "[]"


def _manual_generic_params_evidence(method: str) -> str:
    shapes = {
        "app.outdated_docker_images": "wire [bounded app_name]",
        "filesystem.get_zfs_attributes": "wire [configured_path]",
        "filesystem.getacl": "wire [configured_path, true, false]",
        "filesystem.listdir": ("wire [configured_path, [], {limit: query_limit, select: bounded stat fields}]"),
        "filesystem.stat": "wire [configured_path]",
        "ipmi.lan.query": (
            "wire [{query-filters: [[channel, =, channel_id]], query-options: {limit: 1}, "
            "ipmi-options: {query-remote: false}}]"
        ),
        "reporting.graphs": "wire []",
        "reporting.netdata_graphs": "wire []",
        "vm.get_memory_usage": "wire [bounded vm_id]",
        "vm.get_vm_memory_info": "wire [bounded vm_id]",
    }
    return shapes[method]


def _wire_shape(call_name: str, call: ast.Call, parameter_index: int, method: str) -> str:
    if call_name == "_query_count":
        filters = ast.unparse(call.args[parameter_index]) if parameter_index < len(call.args) else "[]"
        if parameter_index + 1 < len(call.args):
            extra = ast.unparse(call.args[parameter_index + 1])
            return f"wire [{filters}, {{count: true}} merged with {extra}] via _query_count"
        return f"wire [{filters}, {{count: true}}] via _query_count"
    if call_name == "_call_query_with_fallback":
        preferred = ast.unparse(call.args[parameter_index]) if parameter_index < len(call.args) else "{}"
        fail_closed = any(
            keyword.arg == "allow_bare_fallback"
            and isinstance(keyword.value, ast.Constant)
            and keyword.value.value is False
            for keyword in call.keywords
        )
        if fail_closed:
            return f"wire [[], {preferred}]; selected response only, no widening fallback"
        return f"wire [[], {preferred}], then read-only fallback []"
    if call_name == "_safe_call_auto":
        return f"wire {_auto_params_evidence(method)} via _safe_call_auto"
    params = ast.unparse(call.args[parameter_index]) if parameter_index < len(call.args) else "[]"
    return f"wire {params}"


def _method_strings(node: ast.AST, known_names: set[str]) -> set[str]:
    return {
        constant.value
        for constant in ast.walk(node)
        if isinstance(constant, ast.Constant) and isinstance(constant.value, str) and constant.value in known_names
    }


def analyze_source(methods: list[ApiPage], events: list[ApiPage], metric_variables: set[str]) -> SourceAnalysis:
    known_names = {page.title for page in methods} | {page.title for page in events}
    runtime_path = REPO_ROOT / "src" / "truenas_exporter" / "runtime.py"
    runtime_text = runtime_path.read_text(encoding="utf-8")
    runtime_lines = runtime_text.splitlines()
    runtime_tree = ast.parse(runtime_text)

    method_refs: dict[str, set[str]] = defaultdict(set)
    method_call_refs: dict[str, set[str]] = defaultdict(set)
    method_params: dict[str, set[str]] = defaultdict(set)
    metric_functions: dict[str, set[str]] = defaultdict(set)
    function_methods: dict[str, set[str]] = defaultdict(set)
    metric_lines: dict[str, set[int]] = defaultdict(set)
    functional_metric_variables: set[str] = set()

    for node in ast.walk(runtime_tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            node_methods = _method_strings(node, known_names)
            function_methods[node.name].update(node_methods)
            node_metrics = {name.id for name in ast.walk(node) if isinstance(name, ast.Name)} & metric_variables
            for variable in node_metrics:
                metric_functions[variable].add(node.name)
            for name in ast.walk(node):
                if isinstance(name, ast.Name) and name.id in metric_variables:
                    metric_lines[name.id].add(name.lineno)

        if not isinstance(node, ast.Call):
            continue
        call_name = _call_name(node)
        for index, argument in enumerate(node.args):
            if not isinstance(argument, ast.Constant) or not isinstance(argument.value, str):
                continue
            method = argument.value
            if method not in known_names:
                continue
            reference = f"src/truenas_exporter/runtime.py:{node.lineno}"
            method_refs[method].add(reference)
            method_call_refs[method].add(reference)
            if call_name in {
                "_call",
                "call",
                "_call_query_with_fallback",
                "_query_count",
                "_safe_call_auto",
            }:
                param_index = index + 1
                method_params[method].add(_wire_shape(call_name, node, param_index, method))

    transport_relative = "src/truenas_exporter/transport.py"
    transport_tree = ast.parse((REPO_ROOT / transport_relative).read_text(encoding="utf-8"))
    for node in ast.walk(transport_tree):
        if not isinstance(node, ast.Call):
            continue
        call_name = _call_name(node)
        for index, argument in enumerate(node.args):
            if not isinstance(argument, ast.Constant) or argument.value not in known_names:
                continue
            method = str(argument.value)
            reference = f"{transport_relative}:{node.lineno}"
            method_refs[method].add(reference)
            method_call_refs[method].add(reference)
            method_params[method].add(_wire_shape(call_name, node, index + 1, method))

    # Method-plan and config references are exporter usage even when the literal
    # reaches a helper through a loop variable.
    for relative in (
        "src/truenas_exporter/runtime.py",
        "src/truenas_exporter/method_safety.py",
        "src/truenas_exporter/config.py",
        "src/truenas_exporter/events.py",
        "src/truenas_exporter/transport.py",
    ):
        path = REPO_ROOT / relative
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), 1):
            for literal in re.findall(r"['\"]([a-zA-Z0-9_.]+)['\"]", line):
                if literal in known_names:
                    method_refs[literal].add(f"{relative}:{line_number}")

    # A reference outside imports and clear/reset calls is producer evidence.
    import_end = max(
        (node.end_lineno or node.lineno) for node in runtime_tree.body if isinstance(node, (ast.Import, ast.ImportFrom))
    )
    for variable in metric_variables:
        for line_number in metric_lines.get(variable, ()):
            if line_number <= import_end or ".clear()" in runtime_lines[line_number - 1]:
                continue
            functional_metric_variables.add(variable)
            break

    method_safety_tree = ast.parse((REPO_ROOT / "src/truenas_exporter/method_safety.py").read_text(encoding="utf-8"))
    base_methods: set[str] = set()
    for node in method_safety_tree.body:
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and node.target.id == "BASE_METHODS":
            base_methods.update(_method_strings(node.value, known_names))

    return SourceAnalysis(
        method_references={key: tuple(sorted(values)) for key, values in method_refs.items()},
        method_call_references={key: tuple(sorted(values)) for key, values in method_call_refs.items()},
        method_params={key: tuple(sorted(values)) for key, values in method_params.items()},
        metric_functions={key: tuple(sorted(values)) for key, values in metric_functions.items()},
        function_methods={key: tuple(sorted(values)) for key, values in function_methods.items()},
        metric_lines={key: tuple(sorted(values)) for key, values in metric_lines.items()},
        functional_metric_variables=frozenset(functional_metric_variables),
        base_methods=frozenset(base_methods),
    )


@cache
def _metric_source_overrides() -> dict[str, tuple[str, ...]]:
    result: dict[str, tuple[str, ...]] = {}

    def assign(variables: Iterable[str], *sources: str) -> None:
        for variable in variables:
            result[variable] = tuple(sources)

    assign(
        {
            "ALERT_COUNT",
            "ALERT_COUNT_BY_LEVEL",
            "ALERT_COUNT_BY_SOURCE",
            "ALERT_COUNT_BY_CLASS",
            "ALERT_COUNT_BY_NODE",
            "ALERT_DISMISSED_COUNT",
            "ALERT_ONE_SHOT_COUNT",
            "ALERT_OLDEST_TS",
            "ALERT_LAST_OCCURRENCE_TS",
        },
        "alert.list",
    )
    assign(
        {
            "HOST_UPTIME_SECONDS",
            "HOST_PHYSICAL_MEMORY_BYTES",
            "HOST_CPU_CORES",
            "HOST_PHYSICAL_CPU_CORES",
            "HOST_LOAD_AVERAGE",
            "HOST_ECC_MEMORY",
            "HOST_CPU_MODEL",
            "HOST_SYSTEM_INFO",
        },
        "system.info",
    )
    assign({"HOST_INFO"}, "system.info", "system.product_type")
    assign({"SYSTEM_STATE"}, "system.state")
    assign({"SYSTEM_READY"}, "system.ready")
    assign({"VM_AVAILABLE_MEMORY_BYTES"}, "vm.get_available_memory")
    assign({"VM_VMEMORY_IN_USE_BYTES"}, "vm.get_vmemory_in_use")
    assign({"NETWORK_DEFAULT_ROUTES", "NETWORK_NAMESERVERS"}, "network.general.summary")
    assign({"DOCKER_NVIDIA_PRESENT"}, "docker.nvidia_present")
    assign({"DOCKER_NETWORK_COUNT"}, "docker.network.query")
    assign({"DOCKER_STATUS"}, "docker.status")
    assign({"NFS_CLIENT_COUNT"}, "nfs.client_count")
    assign({"NFS_V3_CLIENT_COUNT"}, "nfs.get_nfs3_clients")
    assign({"NFS_V4_CLIENT_COUNT"}, "nfs.get_nfs4_clients")
    assign({"ISCSI_CLIENT_COUNT"}, "iscsi.global.client_count")
    assign(
        {
            "POOL_COUNT",
            "POOL_HEALTHY",
            "POOL_WARNING",
            "POOL_STATUS",
            "POOL_SIZE_BYTES",
            "POOL_ALLOCATED_BYTES",
            "POOL_FREE_BYTES",
            "POOL_SCAN_PERCENT",
            "POOL_FRAGMENTATION",
            "POOL_AUTOTRIM_ENABLED",
            "POOL_DEDUP_RATIO",
            "POOL_DEDUP_TABLE_SIZE_BYTES",
            "POOL_EXPAND_SIZE_BYTES",
            "POOL_EXPAND_REFLOWED_BYTES",
            "POOL_EXPAND_TO_REFLOW_BYTES",
            "POOL_EXPAND_PERCENT",
            "POOL_SCAN_ERRORS",
            "POOL_SCAN_BYTES_PROCESSED",
            "POOL_SCAN_BYTES_TOTAL",
            "POOL_SCAN_SECONDS_REMAINING",
            "POOL_LAST_SCAN_TS",
            "POOL_VDEV_READ_ERRORS",
            "POOL_VDEV_WRITE_ERRORS",
            "POOL_VDEV_CHECKSUM_ERRORS",
        },
        "pool.query",
    )
    assign({"DISK_COUNT", "DISK_SIZE_BYTES", "DISK_IN_USE"}, "disk.query")
    assign({"DISK_TEMPERATURE_C"}, "disk.temperatures")
    assign({"DISK_TEMP_AGG_C"}, "disk.temperature_agg")
    assign({"DISK_TEMP_ALERT_COUNT"}, "disk.temperature_alerts")
    assign({"INTERFACE_COUNT", "INTERFACE_LINK_UP", "INTERFACE_MTU", "INTERFACE_TYPE"}, "interface.query")
    assign({"SERVICE_COUNT", "SERVICE_ENABLED", "SERVICE_RUNNING"}, "service.query")
    assign({"UPDATE_STATUS", "UPDATE_AVAILABLE", "UPDATE_DOWNLOAD_PROGRESS_PERCENT"}, "update.status")
    assign(
        {"TASK_COUNT", "TASK_ENABLED", "TASK_STATE", "TASK_LAST_RUN_TS"},
        "replication.query",
        "cloudsync.query",
        "rsynctask.query",
        "pool.snapshottask.query",
    )
    assign({"POOL_VDEV_READ_ERRORS", "POOL_VDEV_WRITE_ERRORS", "POOL_VDEV_CHECKSUM_ERRORS"}, "pool.query")

    # Count-only inventory loops.
    count_sources = {
        "LOCAL_USER_COUNT": "user.query",
        "LOCAL_GROUP_COUNT": "group.query",
        "STATIC_ROUTE_COUNT": "staticroute.query",
        "TUNABLE_COUNT": "tunable.query",
        "PRIVILEGE_COUNT": "privilege.query",
        "INITSHUTDOWNSCRIPT_COUNT": "initshutdownscript.query",
        "KEYCHAIN_CREDENTIAL_COUNT": "keychaincredential.query",
        "ISCSI_TARGET_COUNT": "iscsi.target.query",
        "ISCSI_PORTAL_COUNT": "iscsi.portal.query",
        "ISCSI_EXTENT_COUNT": "iscsi.extent.query",
        "ISCSI_INITIATOR_COUNT": "iscsi.initiator.query",
        "NVMET_HOST_COUNT": "nvmet.host.query",
        "NVMET_NAMESPACE_COUNT": "nvmet.namespace.query",
    }
    for variable, source in count_sources.items():
        assign({variable}, source)

    # Protocol/config collectors where a helper or an intentionally unavailable
    # compatibility metric obscures the source from simple AST association.
    assign({"SMB_MULTICHANNEL_ENABLED", "SMB1_ENABLED", "SMB_NTLMV1_AUTH_ENABLED", "SMB_ENCRYPTION_MODE"}, "smb.config")
    assign({"NFS_V4_ENABLED", "NFS_SERVERS", "NFS_RDMA_ENABLED"}, "nfs.config")
    assign({"SSH_ENABLED", "FTP_ENABLED", "SNMP_ENABLED", "REPORTING_ENABLED"}, "service.query")
    assign({"SSH_PASSWORD_AUTH"}, "ssh.config")
    assign({"CONSOLEMENU_ENABLED", "SERIALCONSOLE_ENABLED"}, "system.advanced.config")
    assign({"UI_HTTPS_PORT"}, "system.general.config")
    assign({"SYSTEM_GLOBAL_ID"}, "system.global.id")
    assign({"KMIP_ENABLED"}, "kmip.config")
    assign({"SUPPORT_CONFIG_ENABLED"}, "support.config")
    assign({"NETWORK_HTTPPROXY_CONFIGURED"}, "network.configuration.config")
    assign({"MAIL_CONFIGURED"}, "mail.config")
    assign({"TN_CONNECT_ENABLED", "TN_CONNECT_STATUS"}, "tn_connect.config")
    assign({"TRUECOMMAND_STATUS"}, "truecommand.config")
    assign({"UPS_STATUS", "UPS_CONFIGURED"}, "ups.config")
    assign({"APP_WEBDAV_SHARE_COUNT"}, "sharing.webshare.query")
    assign({"SMART_TEST_LAST_RESULT", "SMART_TEST_LAST_TIMESTAMP"}, "smart.test.results")
    assign({"SMB_SESSION_COUNT", "SMB_OPEN_FILE_COUNT", "SMB_CONNECTION_COUNT"}, "smb.status")
    assign({"NFS_SERVER_STAT_OPS"}, "reporting.realtime")
    assign({"EXPORTER_INFO"}, "exporter build metadata")

    # Documented fields currently absent/opaque in 25.10.2 event/query schemas.
    assign(
        {
            "ZFS_ARC_MAX_SIZE_BYTES",
            "ZFS_ARC_MIN_SIZE_BYTES",
            "ZFS_ARC_HIT_RATIO",
            "ZFS_ARC_HITS_RATE",
            "ZFS_ARC_MISSES_RATE",
        },
        "reporting.realtime",
    )
    assign({"VIRT_VOLUME_SIZE_BYTES", "VIRT_GLOBAL_STATE"}, "virt.volume.query", "virt.global.config")
    assign({"FC_PORT_SPEED", "FC_PORT_ONLINE"}, "fcport.status")
    assign(
        {
            "DIRECTORYSERVICES_ACCOUNT_CACHE_ENABLED",
            "DIRECTORYSERVICES_DNS_UPDATES_ENABLED",
            "DIRECTORYSERVICES_TIMEOUT_SECONDS",
            "DIRECTORYSERVICES_KERBEROS_CONFIGURED",
        },
        "directoryservices.config",
    )
    assign({"NTP_SERVER_ACTIVE_COUNT", "NTP_SERVER_REACHABLE_COUNT"}, "system.ntpserver.query")
    assign({"SYSTEM_SECURITY_PASSWORD_WARN_AGE_DAYS"}, "system.security.config")
    assign({"DATASET_REFERENCED_BYTES"}, "pool.dataset.query")
    assign({"DISK_SMART_ENABLED"}, "disk.query")
    assign({"POOL_SCRUB_TASK_STATE", "POOL_SCRUB_LAST_RUN_TS"}, "pool.scrub.query")

    # Collector functions often contain several independent calls. Pin each
    # owned metric to the call that actually supplies its value instead of
    # treating every method literal in the surrounding function as a source.
    assign({"TWOFACTOR_ENABLED"}, "auth.twofactor.config")
    assign({"ALERTSERVICE_COUNT", "ALERTSERVICE_ENABLED"}, "alertservice.query")
    assign({"IOMMU_ENABLED"}, "vm.device.iommu_enabled")
    assign(
        {
            "SYSTEM_SECURITY_FIPS_CONFIGURED",
            "SYSTEM_SECURITY_GPOS_STIG",
            "SYSTEM_SECURITY_PASSWORD_HISTORY_COUNT",
            "SYSTEM_SECURITY_PASSWORD_MAX_AGE_DAYS",
            "SYSTEM_SECURITY_PASSWORD_MIN_AGE_DAYS",
            "SYSTEM_SECURITY_PASSWORD_MIN_LENGTH",
        },
        "system.security.config",
    )
    assign({"APP_AVAILABLE_SPACE_BYTES"}, "app.available_space")
    assign(
        {
            "APP_DOCKERHUB_PULL_LIMIT_REMAINING",
            "APP_DOCKERHUB_PULL_LIMIT_REMAINING_WINDOW_SECONDS",
            "APP_DOCKERHUB_PULL_LIMIT_TOTAL",
            "APP_DOCKERHUB_PULL_LIMIT_WINDOW_SECONDS",
            "APP_DOCKERHUB_RATE_LIMIT_ERROR_PRESENT",
        },
        "app.image.dockerhub_rate_limit",
    )
    assign(
        {
            "APP_COUNT",
            "APP_STATE",
            "APP_UPGRADE_AVAILABLE",
            "APP_IMAGE_UPDATES_AVAILABLE",
            "APP_CUSTOM",
            "APP_MIGRATED",
            "APP_CONTAINER_COUNT",
            "APP_USED_PORT_COUNT",
            "APP_USED_HOST_IP_COUNT",
            "APP_CONTAINER_STATE_COUNT",
        },
        "app.query",
    )
    assign({"VM_COUNT"}, "vm.query")
    assign({"BOOT_POOL_DISK_COUNT"}, "boot.get_disks")
    assign(
        {
            "BOOT_POOL_HEALTHY",
            "BOOT_POOL_STATUS",
            "BOOT_POOL_SIZE_BYTES",
            "BOOT_POOL_ALLOCATED_BYTES",
            "BOOT_POOL_FREE_BYTES",
            "BOOT_POOL_SCAN_STATE",
            "BOOT_POOL_SCAN_PERCENT",
        },
        "boot.get_state",
    )
    assign({"CATALOG_TRAIN_COUNT"}, "catalog.trains")
    assign({"CATALOG_CONFIG_PRESENT", "CATALOG_PREFERRED_TRAIN_COUNT"}, "catalog.config")
    assign(
        {
            "DATASET_COUNT",
            "DATASET_USED_BYTES",
            "DATASET_AVAILABLE_BYTES",
            "DATASET_QUOTA_BYTES",
            "DATASET_REFQUOTA_BYTES",
            "DATASET_COMPRESSION_RATIO",
            "DATASET_ENCRYPTED",
            "DATASET_RESERVATION_BYTES",
            "DATASET_REFRESERVATION_BYTES",
            "DATASET_USED_BY_CHILDREN_BYTES",
            "DATASET_USED_BY_DATASET_BYTES",
            "DATASET_USED_BY_SNAPSHOTS_BYTES",
            "DATASET_READONLY",
            "DATASET_ATIME",
            "DATASET_EXEC",
            "DATASET_KEY_LOADED",
            "DATASET_LOCKED",
            "DATASET_QUOTA_WARNING_PERCENT",
            "DATASET_QUOTA_CRITICAL_PERCENT",
            "DATASET_REFQUOTA_WARNING_PERCENT",
            "DATASET_REFQUOTA_CRITICAL_PERCENT",
            "DATASET_CREATION_TS",
        },
        "pool.dataset.query",
    )
    assign({"DATASET_SNAPSHOT_COUNT"}, "pool.dataset.query", "pool.dataset.snapshot_count")
    assign({"FAILOVER_DISABLED_REASON", "FAILOVER_DISABLED_REASON_COUNT"}, "failover.disabled.reasons")
    assign({"TRUENAS_IS_IX_HARDWARE"}, "truenas.is_ix_hardware")
    assign({"TRUENAS_IS_PRODUCTION"}, "truenas.is_production")
    assign({"SYSTEM_REBOOT_REQUIRED", "SYSTEM_REBOOT_REASON"}, "system.reboot.info")
    assign({"NETWORK_GATEWAY_REACHABLE", "NETWORK_DEFAULT_GATEWAY_CONFIGURED"}, "route.system_routes")
    assign({"FC_HOST_COUNT"}, "fc.fc_host.query")
    assign({"FC_PORT_COUNT"}, "fcport.status")
    assign({"FIPS_AVAILABLE"}, "system.security.info.fips_available")
    assign({"FIPS_ENABLED"}, "system.security.info.fips_enabled")
    assign({"INTERFACE_HAS_PENDING_CHANGES"}, "interface.has_pending_changes")
    assign({"INTERFACE_CHECKIN_WAITING_SECONDS"}, "interface.checkin_waiting")
    assign({"IPMI_LOADED"}, "ipmi.is_loaded")
    assign(
        {
            "IPMI_CHASSIS_POWER_ON",
            "IPMI_CHASSIS_POWER_OVERLOAD",
            "IPMI_CHASSIS_INTRUSION",
            "IPMI_CHASSIS_DRIVE_FAULT",
            "IPMI_CHASSIS_FAN_FAULT",
        },
        "ipmi.chassis.info",
    )
    assign({"IPMI_SEL_ENTRY_COUNT", "IPMI_SEL_FREE_SPACE_BYTES"}, "ipmi.sel.info")
    assign({"ISCSI_ALUA_ENABLED"}, "iscsi.global.alua_enabled")
    assign({"ISCSI_ISER_ENABLED"}, "iscsi.global.iser_enabled")
    assign(
        {
            "ISCSI_SESSION_COUNT",
            "ISCSI_SESSION_ISER_COUNT",
            "ISCSI_SESSION_OFFLOAD_COUNT",
            "ISCSI_SESSION_IMMEDIATE_DATA_COUNT",
        },
        "iscsi.global.sessions",
    )
    assign({"SYSTEM_PRODUCT_TYPE"}, "system.product_type")
    assign({"SYSTEM_VERSION"}, "system.version_short")
    assign({"SYSTEM_HOST_ID"}, "system.host_id")
    assign({"SYSTEM_BOOT_CHANGES_TOTAL"}, "system.boot_id")
    assign({"SYSTEM_MANAGED_BY_TRUECOMMAND"}, "truenas.managed_by_truecommand")
    assign({"NFS_SHARE_COUNT"}, "sharing.nfs.query")
    assign({"SMB_SHARE_COUNT"}, "sharing.smb.query")
    assign({"NVMET_SESSION_COUNT"}, "nvmet.global.sessions")
    assign({"NVMET_SUBSYS_COUNT"}, "nvmet.subsys.query")
    assign({"NVMET_PORT_COUNT"}, "nvmet.port.query")
    assign({"SNAPSHOT_TASK_MAX_COUNT"}, "pool.snapshottask.max_count")
    assign({"SNAPSHOT_TASK_MAX_TOTAL_COUNT"}, "pool.snapshottask.max_total_count")
    assign({"SUPPORT_AVAILABLE"}, "support.is_available")
    assign({"SUPPORT_AVAILABLE_AND_ENABLED"}, "support.is_available_and_enabled")
    assign({"SYSTEMDATASET_POOL"}, "systemdataset.config")
    assign({"DNS_RESOLVER_COUNT"}, "dns.query")
    assign({"DOCKER_IMAGE_COUNT"}, "app.image.query")
    assign({"REPLICATION_MAX_PARALLEL"}, "replication.config.config")
    assign({"REPORTING_EXPORTER_COUNT"}, "reporting.exporters.query")
    assign(
        {
            "REPORTING_TIER0_RETENTION_DAYS",
            "REPORTING_TIER1_RETENTION_DAYS",
            "REPORTING_TIER1_UPDATE_INTERVAL_SECONDS",
        },
        "reporting.config",
    )
    assign(
        {
            "NTP_SERVER_COUNT",
            "NTP_SERVER_PREFER_COUNT",
            "NTP_SERVER_BURST_COUNT",
            "NTP_SERVER_IBURST_COUNT",
            "NTP_SERVER_MIN_POLL_MINUTES",
            "NTP_SERVER_MAX_POLL_MINUTES",
        },
        "system.ntpserver.query",
    )
    assign({"UPDATE_AUTOCHECK_ENABLED", "UPDATE_PROFILE_INFO"}, "update.config")
    assign({"UPDATE_VERSION_AVAILABLE"}, "update.available_versions")
    assign({"VIRT_INSTANCE_COUNT", "VIRT_INSTANCE_RUNNING"}, "virt.instance.query")
    assign({"VIRT_VOLUME_COUNT"}, "virt.volume.query")
    assign({"HW_VIRT_VARIANT"}, "hardware.virtualization.variant")
    assign(
        {
            "VM_FLAG_INTEL_VMX",
            "VM_FLAG_AMD_RVI",
            "VM_FLAG_UNRESTRICTED_GUEST",
            "VM_FLAG_AMD_ASIDS",
            "VM_FLAG_AMD_ASIDS_SUPPORTED",
        },
        "vm.flags",
    )
    assign({"VM_MAX_VCPUS"}, "vm.maximum_supported_vcpus")
    assign({"VM_SUPPORTS_VIRTUALIZATION"}, "vm.supports_virtualization")
    assign(
        {"VM_VIRTUALIZATION_DETAILS_SUPPORTED", "VM_VIRTUALIZATION_DETAILS_ERROR_PRESENT"},
        "vm.virtualization_details",
    )
    return result


EVENT_SOURCE_OVERRIDES: dict[str, str] = {
    **{
        variable: "reporting.realtime"
        for variable in {
            "CPU_USAGE_PERCENT",
            "CPU_USER_PERCENT",
            "CPU_SYSTEM_PERCENT",
            "CPU_IOWAIT_PERCENT",
            "CPU_IDLE_PERCENT",
            "CPU_INTERRUPT_PERCENT",
            "CPU_CORE_USAGE_PERCENT",
            "CPU_TEMPERATURE_C",
            "MEMORY_PHYSICAL_TOTAL_BYTES",
            "MEMORY_PHYSICAL_AVAILABLE_BYTES",
            "MEMORY_PHYSICAL_FREE_BYTES",
            "MEMORY_PHYSICAL_CACHED_BYTES",
            "MEMORY_PHYSICAL_BUFFERS_BYTES",
            "MEMORY_PHYSICAL_USED_BYTES",
            "MEMORY_SWAP_TOTAL_BYTES",
            "MEMORY_SWAP_FREE_BYTES",
            "MEMORY_SWAP_USED_BYTES",
            "DISK_READ_BYTES_RATE",
            "DISK_WRITE_BYTES_RATE",
            "DISK_READ_OPS_RATE",
            "DISK_WRITE_OPS_RATE",
            "DISK_BUSY_PERCENT",
            "NETWORK_RX_BYTES_RATE",
            "NETWORK_TX_BYTES_RATE",
            "ZFS_ARC_SIZE_BYTES",
            "ZFS_ARC_MAX_SIZE_BYTES",
            "ZFS_ARC_MIN_SIZE_BYTES",
            "ZFS_ARC_HIT_RATIO",
            "ZFS_ARC_HITS_RATE",
            "ZFS_ARC_MISSES_RATE",
            "ZFS_ARC_FREE_MEMORY_BYTES",
            "ZFS_ARC_AVAILABLE_BYTES",
            "ZFS_DEMAND_DATA_ACCESSES_RATE",
            "ZFS_DEMAND_DATA_HITS_RATE",
            "ZFS_DEMAND_DATA_MISSES_RATE",
            "ZFS_DEMAND_DATA_HIT_RATIO",
            "ZFS_DEMAND_DATA_IO_HIT_RATIO",
            "ZFS_DEMAND_DATA_MISS_RATIO",
            "ZFS_DEMAND_META_HITS_RATE",
            "ZFS_DEMAND_META_MISSES_RATE",
            "ZFS_DEMAND_META_HIT_RATIO",
            "ZFS_L2ARC_HITS_RATE",
            "ZFS_L2ARC_MISSES_RATE",
            "ZFS_L2ARC_HIT_RATIO",
            "ZFS_L2ARC_READ_BYTES_RATE",
            "ZFS_L2ARC_WRITE_BYTES_RATE",
            "ZFS_DEMAND_ACCESSES_RATE",
            "ZFS_DEMAND_DATA_IO_HITS_RATE",
            "ZFS_DEMAND_META_ACCESSES_RATE",
            "ZFS_DEMAND_META_IO_HITS_RATE",
            "ZFS_DEMAND_META_IO_HIT_RATIO",
            "ZFS_DEMAND_META_MISS_RATIO",
            "ZFS_L2ARC_ACCESSES_RATE",
            "ZFS_L2ARC_MISS_RATIO",
            "POOL_REALTIME_READ_BYTES",
            "POOL_REALTIME_WRITE_BYTES",
        }
    },
    **{
        variable: "app.stats"
        for variable in {
            "APP_CPU_PERCENT",
            "APP_MEMORY_BYTES",
            "APP_NET_RX_BYTES_RATE",
            "APP_NET_TX_BYTES_RATE",
            "APP_BLKIO_READ_BYTES",
            "APP_BLKIO_WRITE_BYTES",
        }
    },
    "VIRT_INSTANCE_CPU": "virt.instance.metrics",
    "VIRT_INSTANCE_MEM": "virt.instance.metrics",
}


def infer_metric_sources(variable: str, analysis: SourceAnalysis) -> tuple[str, tuple[str, ...]]:
    if variable in INTERNAL_VARIABLES:
        return "internal", ()
    if variable in GENERIC_METHOD_VARIABLES:
        return "generic method", tuple(sorted(READ_ONLY_METHOD_ALLOWLIST))
    if variable in GENERIC_EVENT_VARIABLES:
        return "generic event", tuple(sorted(DOCUMENTED_EVENT_NAMES))
    if variable in EVENT_TRANSPORT_VARIABLES:
        return "event transport", tuple(sorted(DOCUMENTED_EVENT_NAMES))
    if variable in EVENT_SOURCE_OVERRIDES:
        return "event", (EVENT_SOURCE_OVERRIDES[variable],)

    overrides = _metric_source_overrides()
    if variable in overrides:
        sources = overrides[variable]
        kind = (
            "method" if all(source in READ_ONLY_METHOD_ALLOWLIST for source in sources) else "unavailable/undocumented"
        )
        return kind, sources

    focused_functions = {
        function
        for function in analysis.metric_functions.get(variable, ())
        if function not in {"scrape_once", "_reset_poll_metrics", "_publish_metric_snapshot"}
    }
    sources = sorted(
        {method for function in focused_functions for method in analysis.function_methods.get(function, ())}
    )
    if sources:
        return "method", tuple(sources)
    return "composed/internal", ()


def _metric_output_unit(metric: dict[str, Any]) -> str:
    name = metric["name"]
    help_text = metric["help"].lower()
    if "timestamp_seconds" in name:
        return "Unix seconds"
    if "_bytes_per_second" in name or "bytes/sec" in help_text or "bytes per second" in help_text:
        return "bytes/second"
    if "_ops_per_second" in name or name.endswith("_per_second"):
        return "operations/second"
    if name.endswith("_seconds") or " seconds" in help_text:
        return "seconds"
    if name.endswith("_bytes") or " bytes" in help_text:
        return "bytes"
    if name.endswith("_celsius"):
        return "degrees Celsius"
    if name.endswith("_percent") or "percent" in help_text:
        return "percent (0-100)"
    if name.endswith("_ratio"):
        return "ratio"
    if name.endswith("_total") and metric["type"] == "counter":
        return "monotonic count"
    if "count" in name or "number of" in help_text:
        return "count"
    if help_text.startswith("1 if") or "flag" in help_text:
        return "boolean gauge (1/0)"
    return "dimensionless gauge"


def _parser_conversion(metric: dict[str, Any], fields: tuple[str, ...], status: str) -> str:
    if status.startswith("unavailable"):
        return "No producer; gauge intentionally remains absent/NaN for compatibility"
    name = metric["name"]
    help_text = metric["help"].lower()
    if metric["variable"] in GENERIC_METHOD_VARIABLES | GENERIC_EVENT_VARIABLES:
        return "Bounded recursive scalar extraction; bool 1/0, numeric float, status allowlist, list length"
    if metric["type"] == "counter":
        return "Exporter-owned monotonic increment"
    if "timestamp_seconds" in name:
        return "_parse_ts accepts numeric seconds, ISO-8601, {$date: milliseconds}, and wrapper objects"
    if "_bytes_per_second" in name:
        return "_as_float preserves the documented instantaneous bytes/second rate"
    if "_ops_per_second" in name or name.endswith("_per_second"):
        return "_as_float preserves the documented instantaneous operations/second rate"
    if any("/ 100" in field for field in fields):
        return "_as_percent accepts finite 0-100 numeric/percent strings, then divides by 100"
    if "percent" in name:
        return "_as_percent accepts only finite 0-100 numeric/percent strings"
    if name.endswith("_ratio"):
        return "_as_ratio/_as_float reject booleans, non-finite, and negative ratios"
    if name.endswith("_bytes") or " bytes" in help_text:
        return "Strict finite/nonnegative byte parsing; explicit MiB/MB sources are multiplied in runtime"
    if "count" in name or "number of" in help_text:
        return "Server-side count mode or bounded len()/aggregation"
    if help_text.startswith("1 if") or "enabled" in name or "healthy" in name or "running" in name:
        return "_as_optional_bool accepts documented booleans/0/1 and omits malformed values"
    if "status" in name or any(field in {"status", "state", "code"} for field in fields):
        return "Bounded enum normalization to uppercase label with sample value 1"
    return "Documented scalar normalized by owned collector; null/missing values omit the sample"


def owned_response_fields(variable: str, sources: tuple[str, ...], analysis: SourceAnalysis) -> tuple[str, ...]:
    """Return the explicit field ownership used by the field-level audit.

    The mappings below are authoritative. AST association establishes producer
    reachability, but never guesses a response field from nearby source text.
    """

    exact: dict[str, tuple[str, ...]] = {
        "SYSTEM_STATE": ("result",),
        "SYSTEM_READY": ("result",),
        "SYSTEM_REBOOT_REQUIRED": ("reboot_required_reasons",),
        "SYSTEM_REBOOT_REASON": ("reboot_required_reasons[].code",),
        "HOST_INFO": ("hostname", "version", "product_type"),
        "HOST_UPTIME_SECONDS": ("uptime_seconds",),
        "HOST_PHYSICAL_MEMORY_BYTES": ("physmem",),
        "HOST_CPU_CORES": ("cores",),
        "HOST_PHYSICAL_CPU_CORES": ("physical_cores",),
        "HOST_LOAD_AVERAGE": ("loadavg",),
        "HOST_ECC_MEMORY": ("ecc_memory",),
        "HOST_CPU_MODEL": ("model",),
        "HOST_SYSTEM_INFO": ("system_manufacturer", "system_product", "system_product_version"),
        "TRUENAS_IS_PRODUCTION": ("result",),
        "TRUENAS_IS_IX_HARDWARE": ("result",),
        "BOOT_POOL_HEALTHY": ("healthy",),
        "BOOT_POOL_STATUS": ("status",),
        "BOOT_POOL_SIZE_BYTES": ("size",),
        "BOOT_POOL_ALLOCATED_BYTES": ("allocated",),
        "BOOT_POOL_FREE_BYTES": ("free",),
        "BOOT_POOL_DISK_COUNT": ("row count",),
        "BOOT_POOL_SCAN_STATE": ("scan.state",),
        "BOOT_POOL_SCAN_PERCENT": ("scan.percentage",),
        "POOL_COUNT": ("row count",),
        "POOL_HEALTHY": ("healthy",),
        "POOL_WARNING": ("warning",),
        "POOL_STATUS": ("status",),
        "POOL_SIZE_BYTES": ("size",),
        "POOL_ALLOCATED_BYTES": ("allocated",),
        "POOL_FREE_BYTES": ("free",),
        "POOL_SCAN_PERCENT": ("scan.percentage",),
        "POOL_FRAGMENTATION": ("fragmentation",),
        "POOL_AUTOTRIM_ENABLED": ("autotrim.value",),
        "POOL_DEDUP_RATIO": (),
        "POOL_DEDUP_TABLE_SIZE_BYTES": ("dedup_table_size",),
        "POOL_EXPAND_SIZE_BYTES": ("expand.bytes_to_reflow",),
        "POOL_EXPAND_REFLOWED_BYTES": ("expand.bytes_reflowed",),
        "POOL_EXPAND_TO_REFLOW_BYTES": ("expand.bytes_to_reflow",),
        "POOL_EXPAND_PERCENT": ("expand.percentage",),
        "POOL_SCAN_ERRORS": ("scan.errors",),
        "POOL_SCAN_BYTES_PROCESSED": ("scan.bytes_processed",),
        "POOL_SCAN_BYTES_TOTAL": ("scan.bytes_to_process",),
        "POOL_SCAN_SECONDS_REMAINING": ("scan.total_secs_left",),
        "POOL_LAST_SCAN_TS": ("scan.end_time",),
        "POOL_VDEV_READ_ERRORS": ("topology.stats.read_errors (schema opaque)",),
        "POOL_VDEV_WRITE_ERRORS": ("topology.stats.write_errors (schema opaque)",),
        "POOL_VDEV_CHECKSUM_ERRORS": ("topology.stats.checksum_errors (schema opaque)",),
        "DATASET_COUNT": ("row count",),
        "DATASET_USED_BYTES": ("used.parsed",),
        "DATASET_AVAILABLE_BYTES": ("available.parsed",),
        "DATASET_REFERENCED_BYTES": ("referenced.parsed (not documented in 25.10.2 result)",),
        "DATASET_QUOTA_BYTES": ("quota.parsed",),
        "DATASET_REFQUOTA_BYTES": ("refquota.parsed",),
        "DATASET_SNAPSHOT_COUNT": ("result",),
        "DATASET_COMPRESSION_RATIO": ("compressratio.parsed",),
        "DATASET_ENCRYPTED": ("encrypted",),
        "DATASET_RESERVATION_BYTES": ("reservation.parsed",),
        "DATASET_REFRESERVATION_BYTES": ("refreservation.parsed",),
        "DATASET_USED_BY_CHILDREN_BYTES": ("usedbychildren.parsed",),
        "DATASET_USED_BY_DATASET_BYTES": ("usedbydataset.parsed",),
        "DATASET_USED_BY_SNAPSHOTS_BYTES": ("usedbysnapshots.parsed",),
        "DATASET_READONLY": ("readonly.parsed",),
        "DATASET_ATIME": ("atime.parsed",),
        "DATASET_EXEC": ("exec.parsed",),
        "DATASET_KEY_LOADED": ("key_loaded",),
        "DATASET_LOCKED": ("locked",),
        "DATASET_QUOTA_WARNING_PERCENT": ("quota_warning.parsed",),
        "DATASET_QUOTA_CRITICAL_PERCENT": ("quota_critical.parsed",),
        "DATASET_REFQUOTA_WARNING_PERCENT": ("refquota_warning.parsed",),
        "DATASET_REFQUOTA_CRITICAL_PERCENT": ("refquota_critical.parsed",),
        "DATASET_CREATION_TS": ("creation.parsed",),
        "DISK_COUNT": ("row count",),
        "DISK_SIZE_BYTES": ("size",),
        "DISK_TEMPERATURE_C": ("result[disk]",),
        "DISK_TEMP_ALERT_COUNT": ("alert row count by disk",),
        "DISK_TEMP_AGG_C": ("result[disk].min/max/avg",),
        "DISK_ROTATIONAL": ("rotationrate/type",),
        "DISK_SMART_ENABLED": ("smartoptions (no documented enabled field)",),
        "DISK_INFO": ("name/model/bus; serial deliberately redacted",),
        "DISK_IN_USE": ("pool",),
        "INTERFACE_COUNT": ("row count",),
        "INTERFACE_LINK_UP": ("state.link_state",),
        "INTERFACE_MTU": ("state.mtu/mtu",),
        "INTERFACE_TYPE": ("type",),
        "NETWORK_DEFAULT_ROUTES": ("default_routes length",),
        "NETWORK_NAMESERVERS": ("nameservers length",),
        "NETWORK_GATEWAY_REACHABLE": ("network matches a default-route sentinel (configuration only)",),
        "NETWORK_DEFAULT_GATEWAY_CONFIGURED": ("network matches a default-route sentinel",),
        "SERVICE_COUNT": ("row count",),
        "SERVICE_ENABLED": ("enable",),
        "SERVICE_RUNNING": ("state.running/state",),
        "NFS_SHARE_COUNT": ("count mode result",),
        "SMB_SHARE_COUNT": ("count mode result",),
        "UPDATE_STATUS": ("code",),
        "UPDATE_AVAILABLE": ("status.new_version",),
        "UPDATE_DOWNLOAD_PROGRESS_PERCENT": ("update_download_progress.percent",),
        "CERT_COUNT": ("row count excluding CSR",),
        "CERT_DAYS_TO_EXPIRY": ("until",),
        "CERT_EXPIRY_TIMESTAMP_SECONDS": ("until",),
        "DIRECTORYSERVICES_STATUS": ("type/status",),
        "DIRECTORYSERVICES_HEALTHY": ("status",),
        "DIRECTORYSERVICES_FAULT_REASON": ("status/message",),
        "DIRECTORYSERVICES_FAULT_PRESENT": ("status",),
        "DIRECTORYSERVICES_CONFIG_ENABLED": ("type",),
        "DIRECTORYSERVICES_SERVICE_TYPE": ("type",),
        "APP_COUNT": ("row count",),
        "APP_STATE": ("name/state",),
        "APP_UPGRADE_AVAILABLE": ("upgrade_available",),
        "APP_IMAGE_UPDATES_AVAILABLE": ("image_updates_available",),
        "APP_CUSTOM": ("custom_app",),
        "APP_MIGRATED": ("migrated",),
        "APP_CONTAINER_COUNT": ("active_workloads.containers",),
        "APP_USED_PORT_COUNT": ("active_workloads.used_ports length",),
        "APP_USED_HOST_IP_COUNT": ("active_workloads.used_host_ips length",),
        "APP_CONTAINER_STATE_COUNT": ("active_workloads.container_details.state",),
        "VM_COUNT": ("row count",),
        "VM_AVAILABLE_MEMORY_BYTES": ("result (documented MiB)",),
        "VM_VMEMORY_IN_USE_BYTES": ("RNP/PRD/RPRD values (documented MiB)",),
        "SNAPSHOT_TASK_MAX_COUNT": ("result",),
        "SNAPSHOT_TASK_MAX_TOTAL_COUNT": ("result",),
        "IPMI_LOADED": ("result",),
        "IPMI_CHASSIS_POWER_ON": ("system_power",),
        "IPMI_CHASSIS_POWER_OVERLOAD": ("power_overload",),
        "IPMI_CHASSIS_INTRUSION": ("chassis_intrusion",),
        "IPMI_CHASSIS_DRIVE_FAULT": ("drive_fault",),
        "IPMI_CHASSIS_FAN_FAULT": ("cooling/fan_fault",),
        "IPMI_SEL_ENTRY_COUNT": ("number_of_log_entries",),
        "IPMI_SEL_FREE_SPACE_BYTES": ("free_space_remaining",),
        "FAILOVER_DISABLED_REASON_COUNT": ("result length",),
        "FAILOVER_DISABLED_REASON": ("result items",),
        "SYSTEM_PRODUCT_TYPE": ("result",),
        "SYSTEM_VERSION": ("result",),
        "SYSTEM_HOST_ID": ("result",),
        "SYSTEM_BOOT_CHANGES_TOTAL": ("result change detection",),
        "SYSTEM_MANAGED_BY_TRUECOMMAND": ("result",),
        "UPDATE_VERSION_AVAILABLE": ("result version items",),
        "BOOT_ENV_COUNT": ("row count",),
        "BOOT_ENV_ACTIVE_COUNT": ("active aggregate",),
        "BOOT_ENV_KEEP_COUNT": ("keep aggregate",),
        "BOOT_ENV_SIZE_BYTES": ("used_bytes",),
        "BOOT_ENV_ACTIVE": ("active",),
        "BOOT_ENV_KEEP": ("keep",),
        "BOOT_ENV_ACTIVATED": ("activated",),
        "BOOT_ENV_ACTIVATED_COUNT": ("activated aggregate",),
        "BOOT_ENV_USED_BYTES": ("used_bytes",),
        "VM_SUPPORTS_VIRTUALIZATION": ("result",),
        "VM_MAX_VCPUS": ("result",),
        "HW_VIRT_VARIANT": ("result",),
        "VM_FLAG_INTEL_VMX": ("intel_vmx",),
        "VM_FLAG_AMD_RVI": ("amd_rvi",),
        "VM_FLAG_UNRESTRICTED_GUEST": ("unrestricted_guest",),
        "VM_FLAG_AMD_ASIDS": ("amd_asids",),
        "VM_FLAG_AMD_ASIDS_SUPPORTED": ("amd_asids",),
        "VM_VIRTUALIZATION_DETAILS_SUPPORTED": ("supported",),
        "VM_VIRTUALIZATION_DETAILS_ERROR_PRESENT": ("error",),
        "VIRT_INSTANCE_COUNT": ("row count",),
        "VIRT_INSTANCE_RUNNING": ("status",),
        "VIRT_VOLUME_COUNT": ("row count",),
        "FC_HOST_COUNT": ("row count",),
        "FC_PORT_COUNT": ("row count",),
        "NVMET_SESSION_COUNT": ("count mode result",),
        "NVMET_SUBSYS_COUNT": ("count mode result",),
        "NVMET_PORT_COUNT": ("count mode result",),
        "ISCSI_ALUA_ENABLED": ("result",),
        "ISCSI_ISER_ENABLED": ("result",),
        "ISCSI_SESSION_COUNT": ("row count",),
        "ISCSI_SESSION_ISER_COUNT": ("count mode with filter iser = true",),
        "ISCSI_SESSION_OFFLOAD_COUNT": ("count mode with filter offload = true",),
        "ISCSI_SESSION_IMMEDIATE_DATA_COUNT": ("count mode with filter immediate_data = true",),
        "INTERFACE_HAS_PENDING_CHANGES": ("result",),
        "INTERFACE_CHECKIN_WAITING_SECONDS": ("result",),
        "APP_AVAILABLE_SPACE_BYTES": ("result",),
        "CATALOG_TRAIN_COUNT": ("row/key count",),
        "CATALOG_CONFIG_PRESENT": ("response presence",),
        "CATALOG_PREFERRED_TRAIN_COUNT": ("preferred_trains length",),
        "FIPS_AVAILABLE": ("result",),
        "FIPS_ENABLED": ("result",),
        "FEATURE_ENABLED": ("result",),
        "CHASSIS_HARDWARE": ("result",),
        "AUDIT_DATASET_USED_BYTES": ("space.used",),
        "AUDIT_DATASET_AVAILABLE_BYTES": ("space.available",),
        "AUDIT_QUOTA_FILL_WARNING_PERCENT": ("quota_fill_warning",),
        "AUDIT_QUOTA_FILL_CRITICAL_PERCENT": ("quota_fill_critical",),
        "AUDIT_RETENTION_DAYS": ("retention",),
        "AUDIT_RESERVATION_BYTES": ("reservation",),
        "AUDIT_QUOTA_BYTES": ("quota",),
        "AUDIT_REMOTE_LOGGING_ENABLED": ("remote_logging_enabled",),
        "TWOFACTOR_ENABLED": ("enabled",),
        "ALERT_COUNT": ("row count",),
        "ALERT_COUNT_BY_CLASS": ("klass", "level"),
        "ALERT_COUNT_BY_LEVEL": ("level",),
        "ALERT_COUNT_BY_NODE": ("node",),
        "ALERT_COUNT_BY_SOURCE": ("source",),
        "ALERT_DISMISSED_COUNT": ("dismissed",),
        "ALERT_LAST_OCCURRENCE_TS": ("last_occurrence",),
        "ALERT_OLDEST_TS": ("datetime",),
        "ALERT_ONE_SHOT_COUNT": ("one_shot",),
        "ALERTSERVICE_COUNT": ("count mode result",),
        "ALERTSERVICE_ENABLED": ("id", "type__title", "enabled"),
        "APP_DOCKERHUB_PULL_LIMIT_REMAINING": ("remaining_pull_limit",),
        "APP_DOCKERHUB_PULL_LIMIT_REMAINING_WINDOW_SECONDS": ("remaining_time_limit_in_secs",),
        "APP_DOCKERHUB_PULL_LIMIT_TOTAL": ("total_pull_limit",),
        "APP_DOCKERHUB_PULL_LIMIT_WINDOW_SECONDS": ("total_time_limit_in_secs",),
        "APP_DOCKERHUB_RATE_LIMIT_ERROR_PRESENT": ("error",),
        "AUTH_SESSIONS_ACTIVE": ("count mode result",),
        "CLOUD_BACKUP_TASK_COUNT": ("count mode result",),
        "CLOUD_BACKUP_TASK_ENABLED": ("id", "enabled"),
        "CLOUD_BACKUP_TASK_STATE": ("id", "job.state"),
        "CONSOLEMENU_ENABLED": ("consolemenu",),
        "CRONJOB_COUNT": ("count mode result",),
        "CRONJOB_ENABLED": ("id", "enabled"),
        "DNS_RESOLVER_COUNT": ("count mode result",),
        "DOCKER_IMAGE_COUNT": ("count mode result",),
        "DOCKER_NETWORK_COUNT": ("count mode result",),
        "DOCKER_NVIDIA_PRESENT": ("result",),
        "DOCKER_STATUS": ("result",),
        "FTP_ENABLED": ("name", "enable"),
        "GPU_AVAILABLE_TO_HOST": ("available_to_host",),
        "GPU_COUNT": ("GPU row count",),
        "GPU_INFO": ("description", "vendor", "devices[].pci_id"),
        "GPU_USES_CRITICAL_DEVICES": ("uses_system_critical_devices",),
        "INITSHUTDOWNSCRIPT_COUNT": ("count mode result",),
        "IOMMU_ENABLED": ("result",),
        "ISCSI_CLIENT_COUNT": ("result",),
        "ISCSI_EXTENT_COUNT": ("count mode result",),
        "ISCSI_INITIATOR_COUNT": ("count mode result",),
        "ISCSI_PORTAL_COUNT": ("count mode result",),
        "ISCSI_TARGET_COUNT": ("count mode result",),
        "JBOF_COUNT": ("count mode result",),
        "JOB_ABORTABLE_ACTIVE_COUNT": ("abortable where state in [WAITING, RUNNING]",),
        "JOB_ACTIVE_COUNT": ("count mode result filtered by state",),
        "JOB_ACTIVE_COUNT_BY_METHOD": ("method", "state"),
        "JOB_ACTIVE_COUNT_BY_STATE": ("count mode result filtered by state",),
        "JOB_OLDEST_ACTIVE_TS": ("time_started",),
        "JOB_PROGRESS_PERCENT": ("progress.percent selected as progress_percent",),
        "JOB_TRANSIENT_ACTIVE_COUNT": ("transient where state in [WAITING, RUNNING]",),
        "KEYCHAIN_CREDENTIAL_COUNT": ("count mode result; no credential fields fetched",),
        "LOCAL_GROUP_COUNT": ("count mode result",),
        "LOCAL_USER_COUNT": ("count mode result",),
        "NFS_CLIENT_COUNT": ("result",),
        "NFS_RDMA_ENABLED": ("rdma",),
        "NFS_SERVERS": ("servers",),
        "NFS_V3_CLIENT_COUNT": ("row count",),
        "NFS_V4_CLIENT_COUNT": ("row count",),
        "NFS_V4_ENABLED": ("protocols contains NFSV4",),
        "NTP_SERVER_BURST_COUNT": ("burst",),
        "NTP_SERVER_COUNT": ("count mode result",),
        "NTP_SERVER_IBURST_COUNT": ("iburst",),
        "NTP_SERVER_MAX_POLL_MINUTES": ("maxpoll exponent; 2**maxpoll / 60",),
        "NTP_SERVER_MIN_POLL_MINUTES": ("minpoll exponent; 2**minpoll / 60",),
        "NTP_SERVER_PREFER_COUNT": ("prefer",),
        "NVMET_HOST_COUNT": ("count mode result",),
        "NVMET_NAMESPACE_COUNT": ("count mode result",),
        "POOL_RESILVER_ENABLED": ("enabled",),
        "POOL_SCRUB_TASK_COUNT": ("count mode result",),
        "POOL_SCRUB_TASK_ENABLED": ("pool_name", "enabled"),
        "PRIVILEGE_COUNT": ("count mode result",),
        "REPLICATION_MAX_PARALLEL": ("max_parallel_replication_tasks",),
        "REPORTING_ENABLED": ("name", "enable"),
        "REPORTING_EXPORTER_COUNT": ("count mode result",),
        "REPORTING_TIER0_RETENTION_DAYS": ("tier0_days/retention_tier0_days",),
        "REPORTING_TIER1_RETENTION_DAYS": ("tier1_days/retention_tier1_days",),
        "REPORTING_TIER1_UPDATE_INTERVAL_SECONDS": ("tier1_update_interval/tier1_update_interval_seconds",),
        "SERIALCONSOLE_ENABLED": ("serialconsole",),
        "SMB1_ENABLED": ("enable_smb1",),
        "SMB_ENCRYPTION_MODE": ("encryption",),
        "SMB_MULTICHANNEL_ENABLED": ("multichannel",),
        "SMB_NTLMV1_AUTH_ENABLED": ("ntlmv1_auth",),
        "SNAPSHOT_TOTAL_COUNT": ("count mode result",),
        "SNAPSHOT_OLDEST_TS": ("properties.creation.parsed selected as creation_parsed",),
        "SNMP_ENABLED": ("name", "enable"),
        "SSH_ENABLED": ("name", "enable"),
        "STATIC_ROUTE_COUNT": ("count mode result",),
        "SUPPORT_AVAILABLE": ("result",),
        "SUPPORT_AVAILABLE_AND_ENABLED": ("result",),
        "SYSTEM_GLOBAL_ID": ("result",),
        "SYSTEM_SECURITY_FIPS_CONFIGURED": ("enable_fips",),
        "SYSTEM_SECURITY_GPOS_STIG": ("enable_gpos_stig",),
        "SYSTEM_SECURITY_PASSWORD_HISTORY_COUNT": ("password_history_length",),
        "SYSTEM_SECURITY_PASSWORD_MAX_AGE_DAYS": ("max_password_age",),
        "SYSTEM_SECURITY_PASSWORD_MIN_AGE_DAYS": ("min_password_age",),
        "SYSTEM_SECURITY_PASSWORD_MIN_LENGTH": ("min_password_length",),
        "SYSTEMDATASET_POOL": ("pool",),
        "TASK_COUNT": ("count mode result per task query",),
        "TASK_ENABLED": ("id/name", "enabled"),
        "TASK_LAST_RUN_TS": ("job.time_finished/lastrun/last_run",),
        "TASK_STATE": ("job.state/state",),
        "TUNABLE_COUNT": ("count mode result",),
        "UI_HTTPS_PORT": ("ui_httpsport",),
        "UPDATE_AUTOCHECK_ENABLED": ("autocheck",),
        "UPDATE_PROFILE_INFO": ("profile/update_profile/train",),
        "DIRECTORYSERVICES_ACCOUNT_CACHE_ENABLED": ("enable_account_cache (secret-bearing config is not fetched)",),
        "DIRECTORYSERVICES_DNS_UPDATES_ENABLED": ("enable_dns_updates (secret-bearing config is not fetched)",),
        "DIRECTORYSERVICES_KERBEROS_CONFIGURED": ("kerberos_realm (secret-bearing config is not fetched)",),
        "DIRECTORYSERVICES_TIMEOUT_SECONDS": ("timeout (secret-bearing config is not fetched)",),
        "FC_PORT_ONLINE": ("opaque fcport.status entry; no documented online field",),
        "FC_PORT_SPEED": ("opaque fcport.status entry; no documented speed field",),
        "KMIP_ENABLED": ("enabled (credential-bearing config is not fetched)",),
        "MAIL_CONFIGURED": ("smtp/outgoingserver/oauth (credential-bearing config is not fetched)",),
        "NETWORK_HTTPPROXY_CONFIGURED": ("httpproxy (may embed credentials; config is not fetched)",),
        "NFS_SERVER_STAT_OPS": ("schema absent from reporting.realtime 25.10.2",),
        "NTP_SERVER_ACTIVE_COUNT": ("no documented active/reachability field",),
        "NTP_SERVER_REACHABLE_COUNT": ("no documented active/reachability field",),
        "POOL_SCRUB_LAST_RUN_TS": ("no documented last-run result field",),
        "POOL_SCRUB_TASK_STATE": ("no documented task-state result field",),
        "SMART_TEST_LAST_RESULT": ("smart.test.results method absent from 25.10.2",),
        "SMART_TEST_LAST_TIMESTAMP": ("smart.test.results method absent from 25.10.2",),
        "SMB_CONNECTION_COUNT": ("smb.status method absent from 25.10.2",),
        "SMB_OPEN_FILE_COUNT": ("smb.status method absent from 25.10.2",),
        "SMB_SESSION_COUNT": ("smb.status method absent from 25.10.2",),
        "SSH_PASSWORD_AUTH": ("passwordauth (private-key-bearing config is not fetched)",),
        "SUPPORT_CONFIG_ENABLED": ("enabled (operator-contact config is not fetched)",),
        "SYSTEM_SECURITY_PASSWORD_WARN_AGE_DAYS": ("no documented password warning-age field",),
        "TN_CONNECT_ENABLED": ("enabled (integration config is not fetched)",),
        "TN_CONNECT_STATUS": ("status (integration config is not fetched)",),
        "TRUECOMMAND_STATUS": ("status (integration config is not fetched)",),
        "UPS_CONFIGURED": ("driver/port/remotehost (password-bearing config is not fetched)",),
        "UPS_STATUS": ("no documented live-status read field",),
        "VIRT_GLOBAL_STATE": ("no operational state field in virt.global.config",),
        "VIRT_VOLUME_SIZE_BYTES": ("no documented size field in virt.volume.query",),
        "APP_WEBDAV_SHARE_COUNT": ("sharing.webshare.query method absent from 25.10.2",),
    }

    if variable in INTERNAL_VARIABLES:
        return ("exporter-owned state",)
    if variable in GENERIC_METHOD_VARIABLES | GENERIC_EVENT_VARIABLES:
        return ("bounded dynamic JSON path",)
    if variable in EVENT_TRANSPORT_VARIABLES:
        return ("subscription connection/message state",)
    if variable in exact:
        return exact[variable]
    if variable in EVENT_SOURCE_OVERRIDES:
        # Event field names are explicit and stable by metric ownership; the
        # source schemas leave CPU/interface/pool objects opaque where noted.
        event_fields = {
            "APP_CPU_PERCENT": "cpu_usage",
            "APP_MEMORY_BYTES": "memory_usage",
            "APP_NET_RX_BYTES_RATE": "network.rx_bytes",
            "APP_NET_TX_BYTES_RATE": "network.tx_bytes",
            "APP_BLKIO_READ_BYTES": "blkio.read",
            "APP_BLKIO_WRITE_BYTES": "blkio.write",
            "VIRT_INSTANCE_CPU": "schema opaque; compatibility parser key cpu",
            "VIRT_INSTANCE_MEM": "schema opaque; compatibility parser key memory",
            "CPU_USAGE_PERCENT": "schema opaque; compatibility parser key cpu.usage",
            "CPU_USER_PERCENT": "schema opaque; compatibility parser key cpu.user",
            "CPU_SYSTEM_PERCENT": "schema opaque; compatibility parser key cpu.system",
            "CPU_IOWAIT_PERCENT": "schema opaque; compatibility parser key cpu.iowait",
            "CPU_IDLE_PERCENT": "schema opaque; compatibility parser key cpu.idle",
            "CPU_INTERRUPT_PERCENT": "schema opaque; compatibility parser key cpu.interrupt",
            "CPU_CORE_USAGE_PERCENT": "schema opaque; compatibility parser key cpu.cores",
            "CPU_TEMPERATURE_C": "schema opaque; compatibility parser key cpu.temperature",
            "MEMORY_PHYSICAL_TOTAL_BYTES": "memory.physical_memory_total",
            "MEMORY_PHYSICAL_AVAILABLE_BYTES": "memory.physical_memory_available",
            "MEMORY_PHYSICAL_FREE_BYTES": "memory.physical_memory_free (schema opaque)",
            "MEMORY_PHYSICAL_CACHED_BYTES": "memory.cached (schema opaque)",
            "MEMORY_PHYSICAL_BUFFERS_BYTES": "memory.buffers (schema opaque)",
            "MEMORY_PHYSICAL_USED_BYTES": "memory total - available",
            "MEMORY_SWAP_TOTAL_BYTES": "memory.swap_total (not enumerated)",
            "MEMORY_SWAP_FREE_BYTES": "memory.swap_free (not enumerated)",
            "MEMORY_SWAP_USED_BYTES": "swap_total - swap_free",
            "DISK_READ_BYTES_RATE": "disls.read_bytes",
            "DISK_WRITE_BYTES_RATE": "disls.write_bytes",
            "DISK_READ_OPS_RATE": "disls.read_ops",
            "DISK_WRITE_OPS_RATE": "disls.write_ops",
            "DISK_BUSY_PERCENT": "disls.busy",
            "NETWORK_RX_BYTES_RATE": "schema opaque; compatibility parser key interfaces.received_bytes",
            "NETWORK_TX_BYTES_RATE": "schema opaque; compatibility parser key interfaces.sent_bytes",
            "ZFS_ARC_SIZE_BYTES": "memory.arc_size",
            "ZFS_ARC_MAX_SIZE_BYTES": "schema absent from reporting.realtime 25.10.2",
            "ZFS_ARC_MIN_SIZE_BYTES": "schema absent from reporting.realtime 25.10.2",
            "ZFS_ARC_HIT_RATIO": "schema absent from reporting.realtime 25.10.2",
            "ZFS_ARC_HITS_RATE": "schema absent from reporting.realtime 25.10.2",
            "ZFS_ARC_MISSES_RATE": "schema absent from reporting.realtime 25.10.2",
            "ZFS_ARC_FREE_MEMORY_BYTES": "memory.arc_free_memory",
            "ZFS_ARC_AVAILABLE_BYTES": "memory.arc_available_memory",
            "ZFS_DEMAND_ACCESSES_RATE": "zfs.demand_accesses_per_second",
            "ZFS_DEMAND_DATA_ACCESSES_RATE": "zfs.demand_data_accesses_per_second",
            "ZFS_DEMAND_DATA_HITS_RATE": "zfs.demand_data_hits_per_second",
            "ZFS_DEMAND_DATA_IO_HITS_RATE": "zfs.demand_data_io_hits_per_second",
            "ZFS_DEMAND_DATA_MISSES_RATE": "zfs.demand_data_misses_per_second",
            "ZFS_DEMAND_DATA_HIT_RATIO": "zfs.demand_data_hit_percentage / 100",
            "ZFS_DEMAND_DATA_IO_HIT_RATIO": "zfs.demand_data_io_hit_percentage / 100",
            "ZFS_DEMAND_DATA_MISS_RATIO": "zfs.demand_data_miss_percentage / 100",
            "ZFS_DEMAND_META_ACCESSES_RATE": "zfs.demand_metadata_accesses_per_second",
            "ZFS_DEMAND_META_HITS_RATE": "zfs.demand_metadata_hits_per_second",
            "ZFS_DEMAND_META_IO_HITS_RATE": "zfs.demand_metadata_io_hits_per_second",
            "ZFS_DEMAND_META_MISSES_RATE": "zfs.demand_metadata_misses_per_second",
            "ZFS_DEMAND_META_HIT_RATIO": "zfs.demand_metadata_hit_percentage / 100",
            "ZFS_DEMAND_META_IO_HIT_RATIO": "zfs.demand_metadata_io_hit_percentage / 100",
            "ZFS_DEMAND_META_MISS_RATIO": "zfs.demand_metadata_miss_percentage / 100",
            "ZFS_L2ARC_HITS_RATE": "zfs.l2arc_hits_per_second",
            "ZFS_L2ARC_MISSES_RATE": "zfs.l2arc_misses_per_second",
            "ZFS_L2ARC_ACCESSES_RATE": "zfs.total_l2arc_accesses_per_second",
            "ZFS_L2ARC_HIT_RATIO": "zfs.l2arc_access_hit_percentage / 100",
            "ZFS_L2ARC_MISS_RATIO": "zfs.l2arc_miss_percentage / 100",
            "ZFS_L2ARC_READ_BYTES_RATE": "zfs.bytes_read_per_second_from_the_l2arc",
            "ZFS_L2ARC_WRITE_BYTES_RATE": "zfs.bytes_written_per_second_to_the_l2arc",
            "POOL_REALTIME_READ_BYTES": "schema opaque; compatibility parser key pools.read_bytes",
            "POOL_REALTIME_WRITE_BYTES": "schema opaque; compatibility parser key pools.write_bytes",
        }
        if variable in event_fields:
            return (event_fields[variable],)
        raise ValueError(f"event-backed metric lacks an explicit field mapping: {variable}")

    if variable.endswith("_COUNT") or "COUNT" in variable:
        return ("count/length aggregate",)
    if sources:
        return ("entire scalar response or owned aggregate",)
    return ("not applicable (internal/composed metric)",)


def load_metric_contract() -> list[dict[str, Any]]:
    contract = json.loads(METRIC_CONTRACT_PATH.read_text(encoding="utf-8"))
    if contract.get("truenas_version") != TARGET_VERSION:
        raise ValueError("metric contract target differs from API documentation target")
    metrics = sorted(contract.get("metrics", []), key=lambda metric: metric["name"])
    names = [metric["name"] for metric in metrics]
    variables = [metric["variable"] for metric in metrics]
    if len(names) != len(set(names)) or len(variables) != len(set(variables)):
        raise ValueError("metric contract contains duplicate names or variables")

    source_tree = ast.parse((REPO_ROOT / "src/truenas_exporter/metrics.py").read_text(encoding="utf-8"))
    declarations: dict[str, str] = {}
    for node in source_tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
            continue
        if not isinstance(node.value, ast.Call) or _call_name(node.value) not in {"declare_gauge", "declare_counter"}:
            continue
        if len(node.value.args) < 2:
            continue
        variable_arg, name_arg = node.value.args[:2]
        if isinstance(variable_arg, ast.Constant) and isinstance(name_arg, ast.Constant):
            declarations[str(variable_arg.value)] = str(name_arg.value)
    if declarations != {metric["variable"]: metric["name"] for metric in metrics}:
        raise ValueError("metrics.py declarations and docs/metrics-contract.json differ")
    return metrics


def dashboard_metric_references(metrics: list[dict[str, Any]]) -> dict[str, tuple[str, ...]]:
    dashboard = json.loads(DASHBOARD_PATH.read_text(encoding="utf-8"))
    contract_names = {metric["name"] for metric in metrics}
    metric_pattern = re.compile(r"\btruenas_[a-zA-Z_:][a-zA-Z0-9_:]*\b")
    references: dict[str, set[str]] = defaultdict(set)

    def visit_panels(panels: Any) -> None:
        if not isinstance(panels, list):
            return
        for panel in panels:
            if not isinstance(panel, dict):
                continue
            context = str(panel.get("title") or f"panel {panel.get('id', 'unknown')}")
            targets = panel.get("targets")
            if isinstance(targets, list):
                for target in targets:
                    expression = target.get("expr") if isinstance(target, dict) else None
                    if isinstance(expression, str):
                        for name in metric_pattern.findall(expression):
                            if name in contract_names:
                                references[name].add(context)
            visit_panels(panel.get("panels"))

    visit_panels(dashboard.get("panels"))
    templating = dashboard.get("templating", {}).get("list", [])
    if isinstance(templating, list):
        for variable in templating:
            if not isinstance(variable, dict):
                continue
            query = variable.get("definition") or variable.get("query")
            if isinstance(query, dict):
                query = query.get("query")
            if isinstance(query, str):
                for name in metric_pattern.findall(query):
                    if name in contract_names:
                        references[name].add(f"template variable {variable.get('name', 'unknown')}")
    return {name: tuple(sorted(contexts)) for name, contexts in references.items()}


@cache
def _test_corpus() -> tuple[tuple[str, str], ...]:
    return tuple(
        (path.relative_to(REPO_ROOT).as_posix(), path.read_text(encoding="utf-8"))
        for path in sorted((REPO_ROOT / "tests").rglob("*.py"))
    )


@cache
def _fixture_paths() -> tuple[str, ...]:
    return tuple(
        path.relative_to(REPO_ROOT).as_posix() for path in sorted((REPO_ROOT / "tests" / "fixtures").rglob("*.json"))
    )


def _test_fixture_evidence(
    metric: dict[str, Any],
    sources: tuple[str, ...],
    status: str,
    analysis: SourceAnalysis,
) -> str:
    if status.startswith("unavailable"):
        return "No API fixture by design; compatibility declaration is covered by metric-contract generation"
    test_hits: list[str] = []
    needles = {
        metric["variable"],
        metric["name"],
        *sources,
        *analysis.metric_functions.get(metric["variable"], ()),
    }
    for relative, text in _test_corpus():
        if any(needle and needle in text for needle in needles):
            test_hits.append(relative)
    fixture_hits: list[str] = []
    for relative in _fixture_paths():
        stem = Path(relative).stem
        if any(source.replace(".", "_") in stem or stem in source.replace(".", "_") for source in sources):
            fixture_hits.append(relative)
    evidence = [*fixture_hits[:2], *test_hits[:2]]
    if evidence:
        return "; ".join(evidence)
    if status.startswith("internal") or status.startswith("generic"):
        return "tests/test_reliability.py; tests/test_phase3_collector_mode.py (internal/generic behavior)"
    return "Metric-contract coverage only; no dedicated fixture/test reference found"


def _documented_type_unit(
    sources: tuple[str, ...],
    fields: tuple[str, ...],
    pages_by_kind_and_title: dict[tuple[str, str], ApiPage],
    source_kind: str,
    output_unit: str,
) -> str:
    evidence: list[str] = []
    page_kind = "event" if source_kind in {"event", "generic event", "event transport"} else "method"
    for source in sources:
        page = pages_by_kind_and_title.get((page_kind, source))
        if page is None:
            evidence.append(f"{source}: undocumented/unavailable")
            continue
        matched_types: set[str] = set()
        for field in fields:
            core = re.split(
                r"\s+\(|\s+selected\s+|\s+where\s+|\s+contains\s+|\s+matches\s+|\s+exponent|\s+/\s+\d+",
                field,
            )[0].strip()
            direct_candidates = {core, core.rsplit(".", 1)[-1].replace("[]", "")}
            direct_matches = {
                documented_field for documented_field in page.fields if documented_field in direct_candidates
            }
            if direct_matches:
                for documented_field in direct_matches:
                    matched_types.update(page.fields[documented_field])
                continue
            for alternative in core.split("/"):
                alternative = alternative.strip()
                candidates = {alternative, alternative.rsplit(".", 1)[-1].replace("[]", "")}
                for documented_field, types in page.fields.items():
                    if documented_field in candidates:
                        matched_types.update(types)
        root = page.return_type or page.return_schema or "schema union/object"
        type_text = "/".join(sorted(matched_types)) if matched_types else root
        evidence.append(f"{source}: {type_text}")
    if not evidence:
        evidence.append("not applicable: exporter-owned state")
    return "; ".join(evidence) + f"; Prometheus unit: {output_unit}"


def build_metric_mappings(
    metrics: list[dict[str, Any]],
    methods: list[ApiPage],
    events: list[ApiPage],
    analysis: SourceAnalysis,
    dashboard_refs: dict[str, tuple[str, ...]],
) -> list[dict[str, Any]]:
    pages_by_kind_and_title = {(page.kind, page.title): page for page in [*methods, *events]}
    forced_unavailable = {
        "CLOUD_BACKUP_TASK_STATE",
        "CONSOLEMENU_ENABLED",
        "POOL_VDEV_READ_ERRORS",
        "POOL_VDEV_WRITE_ERRORS",
        "POOL_VDEV_CHECKSUM_ERRORS",
        "MEMORY_PHYSICAL_FREE_BYTES",
        "MEMORY_PHYSICAL_CACHED_BYTES",
        "MEMORY_PHYSICAL_BUFFERS_BYTES",
        "MEMORY_SWAP_TOTAL_BYTES",
        "MEMORY_SWAP_FREE_BYTES",
        "MEMORY_SWAP_USED_BYTES",
        "SERIALCONSOLE_ENABLED",
        "TASK_LAST_RUN_TS",
        "TASK_STATE",
    }
    mappings: list[dict[str, Any]] = []
    for metric in metrics:
        variable = metric["variable"]
        source_kind, sources = infer_metric_sources(variable, analysis)
        if variable in INTERNAL_VARIABLES | EVENT_TRANSPORT_VARIABLES:
            status = "internal/config/transport"
        elif variable in GENERIC_METHOD_VARIABLES | GENERIC_EVENT_VARIABLES:
            status = "generic extraction"
        elif variable in DEPRECATED_METRICS:
            status = "deprecated compatibility"
        elif variable in forced_unavailable or variable not in analysis.functional_metric_variables:
            status = "unavailable: no reachable 25.10.2 producer"
        else:
            status = "active dedicated"

        fields = owned_response_fields(variable, sources, analysis)
        notes: list[str] = []
        if variable in DEPRECATED_METRICS:
            notes.append(DEPRECATED_METRICS[variable])
        if variable == "CERT_DAYS_TO_EXPIRY":
            notes.append("Issuer label is forced to unknown because the 25.10.2 selected response does not source it.")
        if variable == "DISK_INFO":
            notes.append("Serial label is deliberately redacted; only disk/model/bus are sourced.")
        if source_kind == "unavailable/undocumented":
            notes.append("Named source is absent from the pinned method/event leaves or deliberately not called.")
        if status.startswith("unavailable") and not notes:
            notes.append(
                "Declared contract retained; source field is absent/opaque, sensitive, or producer is unreachable."
            )

        mapping = {
            "variable": variable,
            "source_kind": source_kind,
            "api_method_or_event": list(sources) if sources else ["exporter-owned state"],
            "response_field": list(fields),
            "documented_type_unit": _documented_type_unit(
                sources,
                fields,
                pages_by_kind_and_title,
                source_kind,
                _metric_output_unit(metric),
            ),
            "parser_conversion": _parser_conversion(metric, fields, status),
            "prometheus_metric": metric["name"],
            "metric_type": metric["type"],
            "labels": list(metric["labels"]),
            "fixture_test": _test_fixture_evidence(metric, sources, status, analysis),
            "implementation_status": status,
            "dashboard_usage": list(dashboard_refs.get(metric["name"], ())),
            "runtime_evidence": [
                f"src/truenas_exporter/runtime.py:{line}" for line in analysis.metric_lines.get(variable, ())[:4]
            ],
            "notes": " ".join(notes)
            or "Owned metric mapping; absent/null/malformed values fail closed by omitting the sample.",
        }
        mappings.append(mapping)

    if len(mappings) != len(metrics) or {row["variable"] for row in mappings} != {m["variable"] for m in metrics}:
        raise ValueError("field audit must cover every metric contract specification exactly once")
    dispositions = Counter(row["implementation_status"] for row in mappings)
    if sum(dispositions.values()) != len(metrics):
        raise ValueError("metric disposition partition is incomplete")
    active_event_sources = {
        source
        for row in mappings
        if row["source_kind"] == "event" and row["implementation_status"] == "active dedicated"
        for source in row["api_method_or_event"]
    }
    if active_event_sources != ACTIVE_DEDICATED_EVENT_METRIC_SOURCES:
        raise ValueError("only the 25.10 dedicated event handlers may own active event metrics")
    return mappings


def _operation_type(page: ApiPage, read_only: bool) -> str:
    if page.title == "auth.login_with_api_key":
        return "session-scoped authentication transport"
    operation = page.title.rsplit(".", 1)[-1]
    if page.title == "core.subscribe":
        return "session-scoped read subscription transport"
    if read_only:
        if operation in {"query", "get_instance"}:
            return "CRUD read/query"
        if operation == "config":
            return "singleton configuration read"
        if (
            operation.endswith("_choices")
            or operation.endswith("_schemas")
            or operation in {"choices", "roles", "fields"}
        ):
            return "metadata/choice discovery read"
        if page.job:
            return "read-only job/query"
        return "read/status/inventory"
    if operation in UNSAFE_ACTION_OPERATIONS:
        return "action/job" if page.job else "action/workflow"
    return "mutation/job" if page.job else "mutation/action"


def _metric_reverse_index(metric_mappings: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    result: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for mapping in metric_mappings:
        for source in mapping["api_method_or_event"]:
            result[source].append(mapping)
    return result


def build_method_rows(
    methods: list[ApiPage],
    analysis: SourceAnalysis,
    metric_mappings: list[dict[str, Any]],
) -> tuple[list[dict[str, str]], dict[str, int], dict[str, int]]:
    reverse_metrics = _metric_reverse_index(metric_mappings)
    rows: list[dict[str, str]] = []
    safety = Counter()
    decisions = Counter()
    for page in methods:
        method = page.title
        namespace = method.rsplit(".", 1)[0]
        operation = method.rsplit(".", 1)[-1]
        read_only = method in READ_ONLY_METHOD_ALLOWLIST
        if read_only:
            safety_class = "documented read-only"
        elif operation in UNSAFE_ACTION_OPERATIONS:
            safety_class = "unsafe/action or session workflow"
        else:
            safety_class = "mutating/state-changing"
        safety[safety_class] += 1

        mappings = [
            mapping
            for mapping in reverse_metrics.get(method, [])
            if mapping["source_kind"] in {"method", "generic method", "unavailable/undocumented"}
        ]
        active_mappings = [
            mapping
            for mapping in mappings
            if mapping["implementation_status"] in {"active dedicated", "deprecated compatibility"}
        ]
        unavailable_mappings = [
            mapping for mapping in mappings if mapping["implementation_status"].startswith("unavailable")
        ]
        dedicated_metrics = sorted({mapping["prometheus_metric"] for mapping in active_mappings})
        response_fields = sorted({field for mapping in active_mappings for field in mapping["response_field"]})
        dashboard_metrics = sorted(
            {mapping["prometheus_metric"] for mapping in active_mappings if mapping["dashboard_usage"]}
        )
        refs = analysis.method_references.get(method, ())
        call_refs = analysis.method_call_references.get(method, ())
        observed_params = analysis.method_params.get(method, ())

        if method == "auth.login_with_api_key" and refs:
            decision = "used only for session authentication transport"
        elif method == "core.subscribe" and refs:
            decision = "used only for bounded read-only event transport"
        elif not read_only:
            decision = (
                "excluded: requires an unsafe/entity-specific action"
                if safety_class.startswith("unsafe")
                else "excluded: mutating"
            )
        elif dedicated_metrics:
            decision = "exported through dedicated metric"
        elif method in SENSITIVE_READ_METHODS:
            decision = "excluded: secret or credential exposure"
        elif method in UNSAFE_GENERIC_READ_METHODS:
            decision = (
                "excluded: high cardinality"
                if method in HIGH_CARDINALITY_METHODS
                else "excluded: unsuitable for Prometheus"
            )
        elif method in MANUAL_GENERIC_METHODS:
            decision = "available only through generic extraction"
        elif method in TELEMETRY_CANDIDATE_METHOD_ALLOWLIST:
            decision = (
                "available only through generic extraction"
                if method in analysis.base_methods
                else "useful but deferred"
            )
        elif method in EXTERNAL_ENTITY_METHODS:
            decision = "excluded: requires an unsafe/entity-specific action"
        elif method in HIGH_CARDINALITY_METHODS:
            decision = "excluded: high cardinality"
        elif method in RAW_CONTENT_METHODS:
            decision = "excluded: unsuitable for Prometheus"
        elif method in analysis.base_methods:
            decision = "available only through generic extraction"
        else:
            decision = "excluded: unsuitable for Prometheus"
        decisions[decision] += 1

        documented_params = ", ".join(f"{position}:{name}" for position, name in page.parameters) or "none"
        if observed_params:
            parameters_verified = (
                f"documented [{documented_params}]; source call shape(s): {'; '.join(observed_params)}"
            )
        elif method in SENSITIVE_READ_METHODS | UNSAFE_GENERIC_READ_METHODS:
            parameters_verified = (
                f"documented [{documented_params}]; full response is policy-blocked and exporter does not call it"
            )
        elif method in MANUAL_GENERIC_METHODS:
            parameters_verified = f"documented [{documented_params}]; {_manual_generic_params_evidence(method)}"
        elif method in analysis.base_methods:
            parameters_verified = (
                f"documented [{documented_params}]; generic BASE_METHODS {_auto_params_evidence(method)}"
            )
        else:
            parameters_verified = f"documented [{documented_params}]; exporter does not call this method"

        if call_refs:
            exporter_usage = "runtime call(s): " + ", ".join(call_refs[:6])
        elif method in SENSITIVE_READ_METHODS | UNSAFE_GENERIC_READ_METHODS:
            exporter_usage = "safety-policy reference only; full response is not called"
        elif method in MANUAL_GENERIC_METHODS:
            exporter_usage = "opt-in bounded manual generic collector: " + ", ".join(refs[:6])
        elif method in analysis.base_methods:
            exporter_usage = "opt-in generic BASE_METHODS plan: " + ", ".join(refs[:6])
        elif refs:
            exporter_usage = "safety-policy reference only; not called: " + ", ".join(refs[:6])
        else:
            exporter_usage = "not referenced by runtime/config/method plan"
        if method == "auth.login_with_api_key" and refs:
            response_fields_used = "authentication success boolean; transport only, not a Prometheus sample"
        elif method == "core.subscribe" and refs:
            response_fields_used = "subscription identifier; transport state only, not a Prometheus sample"
        elif response_fields:
            response_fields_used = ", ".join(response_fields)
        elif unavailable_mappings:
            unavailable = sorted({mapping["prometheus_metric"] for mapping in unavailable_mappings})
            response_fields_used = "no reachable producer; retained compatibility declarations: " + ", ".join(
                unavailable
            )
        else:
            response_fields_used = "none in an owned dedicated collector"

        if method in SENSITIVE_READ_METHODS:
            generic_coverage = "blocked: full response is sensitive; owned count/select calls only"
        elif method in UNSAFE_GENERIC_READ_METHODS:
            generic_coverage = "blocked: full response is raw, opaque, identity-bearing, or configuration-heavy"
        elif method in MANUAL_GENERIC_METHODS:
            generic_coverage = (
                "opt-in bounded manual generic extraction; entity/path/query limits and safety guards apply"
            )
        elif method in analysis.base_methods:
            generic_coverage = (
                "opt-in generic method extraction via BASE_METHODS; safety/entity/sensitivity guards apply"
            )
        elif read_only and method in TELEMETRY_CANDIDATE_METHOD_ALLOWLIST:
            generic_coverage = "candidate catalog only; guarded discovery or owned collector parameters required"
        else:
            generic_coverage = "none; not in the generic base plan"

        note_parts = [
            f"[docs](truenas-api/{page.path})",
            page.summary or "No prose summary; schema and operation name are the evidence.",
            "roles: " + (" / ".join(page.roles) if page.roles else "none documented"),
            f"return: {page.return_schema or 'schema union'} / {page.return_type or 'union or schema-defined type'}",
        ]
        if method in SENSITIVE_READ_METHODS:
            note_parts.append("Full response is sensitive; count mode or a strict non-sensitive select is mandatory.")
        if method == "core.subscribe" and refs:
            note_parts.append(
                "Session-scoped transport call is restricted to profile-reviewed defaults: reporting.realtime, "
                "app.stats, virt.instance.metrics on 25.10, and container.metrics on 26.0/unknown; it performs "
                "no persistent appliance mutation."
            )
        if method == "auth.login_with_api_key" and refs:
            note_parts.append(
                "Required session authentication transport; the API key is supplied from runtime configuration "
                "and is never exported, logged, persisted, or included in fixtures."
            )
        if unavailable_mappings and not dedicated_metrics:
            note_parts.append("Retained metric declarations are explicitly unavailable rather than active telemetry.")

        row = {
            "Namespace": namespace,
            "Method": method,
            "Documented operation/type": _operation_type(page, read_only),
            "Read-only classification": safety_class,
            "Exporter usage": exporter_usage,
            "Parameters verified": parameters_verified,
            "Response fields used": response_fields_used,
            "Dedicated metrics": ", ".join(dedicated_metrics) if dedicated_metrics else "none",
            "Generic coverage": generic_coverage,
            "Dashboard usage": ", ".join(dashboard_metrics) if dashboard_metrics else "none",
            "Decision": decision,
            "Evidence/notes": " ".join(note_parts),
        }
        if tuple(row) != METHOD_COLUMNS:
            raise ValueError("method row does not have the required 12-column schema")
        rows.append(row)

    expected_safety = {
        "documented read-only": 398,
        "mutating/state-changing": 325,
        "unsafe/action or session workflow": 44,
    }
    if dict(safety) != expected_safety:
        raise ValueError(f"method safety partition changed: {dict(safety)}")
    if len(rows) != EXPECTED_METHOD_COUNT or sum(decisions.values()) != EXPECTED_METHOD_COUNT:
        raise ValueError("method decision partition is incomplete")
    return rows, dict(sorted(safety.items())), dict(sorted(decisions.items()))


def build_event_rows(
    events: list[ApiPage],
    analysis: SourceAnalysis,
    metric_mappings: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    reverse_metrics = _metric_reverse_index(metric_mappings)
    rows: list[dict[str, Any]] = []
    decisions = Counter()
    for page in events:
        event = page.title
        mappings = [
            mapping
            for mapping in reverse_metrics.get(event, [])
            if mapping["source_kind"] in {"event", "generic event", "event transport"}
        ]
        active_metrics = sorted(
            {
                mapping["prometheus_metric"]
                for mapping in mappings
                if mapping["implementation_status"] in {"active dedicated", "deprecated compatibility"}
            }
        )
        dashboard_metrics = sorted(
            {
                mapping["prometheus_metric"]
                for mapping in mappings
                if mapping["dashboard_usage"] and mapping["implementation_status"] == "active dedicated"
            }
        )
        if active_metrics:
            decision = "exported through dedicated metric"
        elif event in RAW_EVENTS:
            decision = "excluded: unsuitable for Prometheus"
        elif event in SECRET_EVENTS:
            decision = "excluded: secret or credential exposure"
        elif event in HIGH_CARDINALITY_EVENTS:
            decision = "excluded: high cardinality"
        elif event in TELEMETRY_EVENTS:
            decision = "useful but deferred"
        else:
            decision = "excluded: unsuitable for Prometheus"
        decisions[decision] += 1
        refs = (
            tuple(
                reference
                for reference in analysis.method_references.get(event, ())
                if reference.startswith("src/truenas_exporter/events.py:")
            )
            if event in SUBSCRIBED_EVENTS
            else ()
        )
        if event in SUBSCRIBED_EVENTS:
            event_safety = "read-only event; safe default dedicated subscription"
        elif event in SECRET_EVENTS:
            event_safety = "read-only event; secret/credential-bearing payload — subscription prohibited"
        else:
            event_safety = "read-only event; unowned full payload — subscription prohibited"
        rows.append(
            {
                "namespace": event.rsplit(".", 1)[0],
                "event": event,
                "documentation_path": page.path,
                "documented_shapes": list(page.event_shapes),
                "read_only_classification": event_safety,
                "exporter_usage": list(refs),
                "dedicated_metrics": active_metrics,
                "dashboard_usage": dashboard_metrics,
                "decision": decision,
                "evidence_notes": page.summary,
            }
        )
    if len(rows) != EXPECTED_EVENT_COUNT or sum(decisions.values()) != EXPECTED_EVENT_COUNT:
        raise ValueError("event decision partition is incomplete")
    return rows, dict(sorted(decisions.items()))


def build_namespace_rows(method_rows: list[dict[str, str]], event_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_namespace: dict[str, list[dict[str, str]]] = defaultdict(list)
    event_counts = Counter(row["namespace"] for row in event_rows)
    domain_by_namespace = {
        namespace: domain for domain, namespaces in DOMAIN_GROUPS.items() for namespace in namespaces
    }
    for row in method_rows:
        by_namespace[row["Namespace"]].append(row)
    rows: list[dict[str, Any]] = []
    for namespace in sorted(by_namespace):
        methods = by_namespace[namespace]
        rows.append(
            {
                "domain": domain_by_namespace[namespace],
                "namespace": namespace,
                "method_count": len(methods),
                "event_count": event_counts[namespace],
                "documented_read_only": sum(
                    row["Read-only classification"] == "documented read-only" for row in methods
                ),
                "mutating": sum(row["Read-only classification"] == "mutating/state-changing" for row in methods),
                "unsafe_action": sum(row["Read-only classification"].startswith("unsafe") for row in methods),
                "decisions": dict(sorted(Counter(row["Decision"] for row in methods).items())),
            }
        )
    if len(rows) != EXPECTED_METHOD_NAMESPACE_COUNT:
        raise ValueError("namespace evidence must contain exactly 114 rows")
    return rows


def _markdown_table(headers: Iterable[str], rows: Iterable[Iterable[Any]]) -> str:
    header_list = list(headers)
    lines = [
        "| " + " | ".join(header_list) + " |",
        "|" + "|".join("---" for _ in header_list) + "|",
    ]
    for row in rows:
        lines.append("| " + " | ".join(_md_escape(value) for value in row) + " |")
    return "\n".join(lines)


def _dashboard_summary(metric_mappings: list[dict[str, Any]]) -> dict[str, int]:
    dashboard = json.loads(DASHBOARD_PATH.read_text(encoding="utf-8"))

    def panel_count(value: Any) -> int:
        if isinstance(value, dict):
            return (1 if "type" in value and "gridPos" in value else 0) + sum(
                panel_count(item) for item in value.values()
            )
        if isinstance(value, list):
            return sum(panel_count(item) for item in value)
        return 0

    referenced = [mapping for mapping in metric_mappings if mapping["dashboard_usage"]]
    unavailable_referenced = [
        mapping for mapping in referenced if mapping["implementation_status"].startswith("unavailable")
    ]
    return {
        "recursive_panel_count": panel_count(dashboard),
        "unique_contract_metrics_referenced": len(referenced),
        "contract_metrics_not_referenced": len(metric_mappings) - len(referenced),
        "unavailable_metrics_referenced": len(unavailable_referenced),
    }


def render_markdown(audit: dict[str, Any]) -> str:
    evidence = audit["evidence"]
    metric_dispositions = audit["metric_disposition_partition"]
    file_classes = Counter(row["document_class"] for row in audit["files"])

    domain_rows: list[list[Any]] = []
    namespaces_by_domain: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in audit["namespaces"]:
        namespaces_by_domain[row["domain"]].append(row)
    for domain in DOMAIN_GROUPS:
        rows = namespaces_by_domain[domain]
        domain_rows.append(
            [
                domain,
                len(rows),
                sum(row["method_count"] for row in rows),
                sum(row["event_count"] for row in rows),
                sum(row["documented_read_only"] for row in rows),
                sum(row["mutating"] for row in rows),
                sum(row["unsafe_action"] for row in rows),
                ", ".join(row["namespace"] for row in rows),
            ]
        )

    method_table = _markdown_table(
        METHOD_COLUMNS,
        ([row[column] for column in METHOD_COLUMNS] for row in audit["methods"]),
    )
    event_table = _markdown_table(
        (
            "Namespace",
            "Event",
            "Documented shapes",
            "Read-only classification",
            "Exporter usage",
            "Dedicated metrics",
            "Dashboard usage",
            "Decision",
            "Evidence/notes",
        ),
        (
            (
                row["namespace"],
                row["event"],
                ", ".join(row["documented_shapes"]),
                row["read_only_classification"],
                ", ".join(row["exporter_usage"]) or "not referenced",
                ", ".join(row["dedicated_metrics"]) or "none",
                ", ".join(row["dashboard_usage"]) or "none",
                row["decision"],
                f"[docs](truenas-api/{row['documentation_path']}) {row['evidence_notes']}",
            )
            for row in audit["events"]
        ),
    )
    field_table = _markdown_table(
        (
            "API method/event",
            "Response field",
            "Documented type/unit",
            "Parser/conversion",
            "Prometheus metric",
            "Labels",
            "Fixture/test",
            "Disposition/evidence",
        ),
        (
            (
                ", ".join(row["api_method_or_event"]),
                ", ".join(row["response_field"]),
                row["documented_type_unit"],
                row["parser_conversion"],
                f"{row['prometheus_metric']} ({row['metric_type']})",
                ", ".join(row["labels"]) or "none",
                row["fixture_test"],
                f"{row['implementation_status']}; {row['notes']}",
            )
            for row in audit["field_mappings"]
        ),
    )

    parts = [
        "# TrueNAS SCALE 25.10.2 API-to-exporter parity audit",
        "",
        "This file is generated by `python3 scripts/generate_api_exporter_parity.py`. "
        "It inventories every committed API document and classifies every method/event "
        "without contacting a live TrueNAS system.",
        "",
        "## Pinned evidence",
        "",
        _markdown_table(
            ("Evidence", "Value"),
            (
                ("TrueNAS target", evidence["target_version"]),
                ("Manifest-tracked Markdown files", evidence["manifest_file_count"]),
                ("Tree files including self-excluded MANIFEST.json", evidence["tree_file_count_including_manifest"]),
                ("Manifest aggregate SHA-256", evidence["manifest_aggregate_sha256"]),
                ("Documented method leaves", evidence["method_leaf_count"]),
                ("Documented event leaves", evidence["event_leaf_count"]),
                ("Method namespaces", evidence["method_namespace_count"]),
                ("Event namespaces", evidence["event_namespace_count"]),
                ("Documented read-only allowlist", evidence["read_only_allowlist_count"]),
                ("Sensitive full-response reads", evidence["sensitive_read_count"]),
                ("Non-secret full responses blocked from generic extraction", evidence["unsafe_generic_read_count"]),
                ("Conservative telemetry candidate allowlist", evidence["telemetry_candidate_allowlist_count"]),
                ("Documentation-reviewed safe events", evidence["safe_event_count"]),
                ("Prohibited unsafe event payloads", evidence["unsafe_event_count"]),
                ("Default dedicated event subscriptions", evidence["default_event_subscription_count"]),
                ("Metric contract specifications", evidence["metric_contract_count"]),
            ),
        ),
        "",
        "The machine-readable companion contains one hash/size/classification object for all 1,012 files. "
        "The manifest intentionally tracks the 1,011 Markdown files and excludes itself.",
        "",
        _markdown_table(("File class", "Count"), sorted(file_classes.items())),
        "",
        "## Complete partitions",
        "",
        _markdown_table(("Method safety class", "Count"), audit["method_safety_partition"].items()),
        "",
        _markdown_table(("Method decision", "Count"), audit["method_decision_partition"].items()),
        "",
        _markdown_table(("Event decision", "Count"), audit["event_decision_partition"].items()),
        "",
        _markdown_table(("Metric disposition", "Count"), metric_dispositions.items()),
        "",
        "## Dashboard evidence",
        "",
        _markdown_table(("Dashboard check", "Count"), audit["dashboard_evidence"].items()),
        "",
        "Dashboard coverage and exporter coverage are reported independently. A dashboard reference to an "
        "unavailable compatibility declaration does not make that metric produced.",
        "",
        "## Required-domain namespace coverage",
        "",
        _markdown_table(
            (
                "Domain",
                "Namespaces",
                "Methods",
                "Events",
                "Reads",
                "Mutations",
                "Unsafe actions",
                "Namespace inventory",
            ),
            domain_rows,
        ),
        "",
        "All 114 method namespaces are assigned exactly once. The method rows below give the explicit "
        "reason for every exclusion, deferral, generic-only surface, or dedicated export.",
        "",
        "## Documentation/parser edge evidence",
        "",
        "- `methods/nfs/get_nfs4_clients.md` contains nine NUL bytes and one `0x14`; byte-safe parsing is required and plain `rg` undercounts methods.",
        "- 111 method leaves have no prose summary; classification therefore also uses front matter, operation, schema, and roles.",
        "- `reporting.realtime` documents required key `disls` and leaves CPU/interface/pool objects opaque; the audit preserves that spelling rather than silently rewriting it.",
        "- Standard query count/get/select options change response shape; count returns a number and get returns one object rather than the default array.",
        "- `disk.query` keeps `extra.passwords` false and `app.query` keeps `extra.retrieve_config` false; sensitive queries require count or strict select.",
        "- Dynamic `app.stats`, `reporting.realtime`, `virt.instance.metrics`, and `container.metrics` events are ADDED-only; exporter stale-timeout/recovery handling is required.",
        "- The shared jobs guide mentions `filesystem.copy`, but no corresponding method leaf exists; examples do not become inventory rows.",
        "",
        "## Every documented API method (767 rows)",
        "",
        method_table,
        "",
        "## Every documented API event (63 rows)",
        "",
        event_table,
        "",
        f"## Field-level metric ownership ({evidence['metric_contract_count']} rows)",
        "",
        "Every public metric contract specification has one explicit disposition. Multi-field and multi-source "
        "metrics list all owned inputs; exporter-internal, generic, deprecated, and unavailable declarations are explicit.",
        "",
        field_table,
        "",
    ]
    rendered = "\n".join(parts)
    # Preserve verbatim documentation summaries (some upstream pages contain a
    # literal TODO) while forbidding unresolved audit checkboxes of our own.
    if "[ ]" in rendered:
        raise ValueError("generated parity audit contains unresolved language or checkboxes")
    return rendered


def _page_signature(page: ApiPage) -> dict[str, Any]:
    return {
        "roles": list(page.roles),
        "parameters": [[position, name] for position, name in page.parameters],
        "return_schema": page.return_schema,
        "return_type": page.return_type,
        "fields": {field: list(types) for field, types in page.fields.items()},
        "event_shapes": list(page.event_shapes),
        "job": page.job,
    }


def _signature_changes(old: ApiPage, new: ApiPage) -> list[str]:
    old_sig = _page_signature(old)
    new_sig = _page_signature(new)
    changes = [key for key in old_sig if old_sig[key] != new_sig[key]]
    return changes


def _current_exporter_methods(v25_audit: dict[str, Any]) -> set[str]:
    result: set[str] = set()
    for row in v25_audit["methods"]:
        if (
            not row["Exporter usage"].startswith("not referenced")
            or row["Dedicated metrics"] != "none"
            or row["Generic coverage"] != "none; not in the generic base plan"
            or row["Response fields used"].startswith("no reachable producer")
        ):
            result.add(row["Method"])
    return result


def _current_exporter_events(v25_audit: dict[str, Any]) -> set[str]:
    result: set[str] = set()
    for row in v25_audit["events"]:
        if row["exporter_usage"] or row["dedicated_metrics"]:
            result.add(row["event"])
    return result


def _required_surface_checks(
    v25_methods: dict[str, ApiPage],
    v26_methods: dict[str, ApiPage],
    v25_events: dict[str, ApiPage],
    v26_events: dict[str, ApiPage],
) -> list[dict[str, str]]:
    expectations = [
        ("method", "app.image.query", "present in v26; keep eligible only after schema/permission review"),
        ("method", "pool.is_upgraded", "present in v26; keep blocked because a pool id is required"),
        ("method", "pool.ddt_prefetch", "present in v26; keep prohibited because it is action-like"),
        (
            "method",
            "nvmet.global.sessions",
            "absent from pinned v26 docs; keep bounded count source under v26/unknown because live 26.0.0-BETA.2 serves it",
        ),
        ("method", "reporting.graphs", "absent in v26; do not auto-substitute singular reporting.graph"),
        (
            "method",
            "reporting.netdata_graphs",
            "absent in v26; do not auto-substitute singular reporting.netdata_graph",
        ),
        ("method", "virt.instance.query", "absent in v26; suppress under v26 profile"),
        ("method", "virt.volume.query", "absent in v26; suppress under v26 profile"),
        ("event", "virt.instance.metrics", "absent in v26; do not subscribe under v26 profile"),
        (
            "event",
            "container.metrics",
            "absent in 25.10; subscribe only under v26/unknown as the reviewed instance-metrics replacement",
        ),
    ]
    rows: list[dict[str, str]] = []
    for kind, name, decision in expectations:
        old_pages = v25_events if kind == "event" else v25_methods
        new_pages = v26_events if kind == "event" else v26_methods
        rows.append(
            {
                "kind": kind,
                "name": name,
                "v25": "present" if name in old_pages else "absent",
                "v26": "present" if name in new_pages else "absent",
                "decision": decision,
            }
        )
    return rows


def build_v26_parity(v25_audit: dict[str, Any] | None = None) -> dict[str, Any]:
    if v25_audit is None:
        v25_audit = build_audit()
    inventory = inventory_docs_for_target("26.0.0")
    current_methods = _current_exporter_methods(v25_audit)
    current_events = _current_exporter_events(v25_audit)
    current_v26_events = set(PROFILE_26_0.default_event_subscriptions)
    v25_method_names = {row["Method"] for row in v25_audit["methods"]}
    v25_event_names = {row["event"] for row in v25_audit["events"]}

    method_rows: list[dict[str, Any]] = []
    for page in inventory.methods:
        if page.title in current_methods:
            exporter_relevance = "current exporter surface; requires COMPAT-02 profile review before v26 use"
        elif page.title in v25_method_names:
            exporter_relevance = "common documented method; no current exporter ownership"
        else:
            exporter_relevance = "v26-only method; inventory only, no first-release metric mapping approved"
        method_rows.append(
            {
                "namespace": page.title.rsplit(".", 1)[0],
                "method": page.title,
                "documentation_path": page.path,
                "roles": list(page.roles),
                "parameter_count": len(page.parameters),
                "parameters": [[position, name] for position, name in page.parameters],
                "return_schema": page.return_schema,
                "return_type": page.return_type,
                "field_count": len(page.fields),
                "current_exporter_surface": page.title in current_methods,
                "present_in_25_10_2": page.title in v25_method_names,
                "decision": exporter_relevance,
            }
        )

    event_rows: list[dict[str, Any]] = []
    for page in inventory.events:
        if page.title in current_v26_events:
            exporter_relevance = "current exporter event; reviewed v26 profile default subscription"
        elif page.title in current_events:
            exporter_relevance = "current exporter event in 25.10 only; suppressed under v26 profile"
        elif page.title in v25_event_names:
            exporter_relevance = "common documented event; no current dedicated exporter ownership"
        else:
            exporter_relevance = "v26-only event; inventory only, subscription prohibited until reviewed"
        event_rows.append(
            {
                "namespace": page.title.rsplit(".", 1)[0],
                "event": page.title,
                "documentation_path": page.path,
                "roles": list(page.roles),
                "documented_shapes": list(page.event_shapes),
                "current_exporter_surface": page.title in current_v26_events,
                "present_in_25_10_2": page.title in v25_event_names,
                "decision": exporter_relevance,
            }
        )

    method_decisions = Counter(row["decision"] for row in method_rows)
    event_decisions = Counter(row["decision"] for row in event_rows)
    return {
        "schema_version": 1,
        "target_version": "26.0.0",
        "source_target": TRUENAS_API_VERSION,
        "generator": "scripts/generate_api_exporter_parity.py --target 26.0.0",
        "evidence": inventory.evidence,
        "method_decision_partition": dict(sorted(method_decisions.items())),
        "event_decision_partition": dict(sorted(event_decisions.items())),
        "files": inventory.file_rows,
        "methods": method_rows,
        "events": event_rows,
    }


def render_v26_parity_markdown(audit: dict[str, Any]) -> str:
    evidence = audit["evidence"]
    file_classes = Counter(row["document_class"] for row in audit["files"])
    parts = [
        "# TrueNAS SCALE 26.0.0 API parity inventory",
        "",
        "This file is generated by `python3 scripts/generate_api_exporter_parity.py --target 26.0.0`. "
        "It pins the checked-in v26 documentation corpus for compatibility work and performs no live API access.",
        "",
        "## Pinned evidence",
        "",
        _markdown_table(
            ("Evidence", "Value"),
            (
                ("TrueNAS target", evidence["target_version"]),
                ("Manifest path", evidence["manifest_path"]),
                ("Manifest-tracked Markdown files", evidence["manifest_file_count"]),
                ("Tree files including self-excluded MANIFEST.json", evidence["tree_file_count_including_manifest"]),
                ("Manifest aggregate SHA-256", evidence["manifest_aggregate_sha256"]),
                ("Documented method leaves", evidence["method_leaf_count"]),
                ("Documented event leaves", evidence["event_leaf_count"]),
                ("Method namespaces", evidence["method_namespace_count"]),
                ("Event namespaces", evidence["event_namespace_count"]),
            ),
        ),
        "",
        _markdown_table(("File class", "Count"), sorted(file_classes.items())),
        "",
        "## Exporter relevance partitions",
        "",
        _markdown_table(("Method decision", "Count"), audit["method_decision_partition"].items()),
        "",
        _markdown_table(("Event decision", "Count"), audit["event_decision_partition"].items()),
        "",
        "## Every documented v26 API method",
        "",
        _markdown_table(
            (
                "Namespace",
                "Method",
                "Path",
                "Parameters",
                "Return schema/type",
                "Fields",
                "Current exporter surface",
                "Present in 25.10.2",
                "Decision",
            ),
            (
                (
                    row["namespace"],
                    row["method"],
                    f"truenas-api-v26/{row['documentation_path']}",
                    row["parameter_count"],
                    f"{row['return_schema'] or 'schema union'} / {row['return_type'] or 'schema-defined type'}",
                    row["field_count"],
                    row["current_exporter_surface"],
                    row["present_in_25_10_2"],
                    row["decision"],
                )
                for row in audit["methods"]
            ),
        ),
        "",
        "## Every documented v26 API event",
        "",
        _markdown_table(
            (
                "Namespace",
                "Event",
                "Path",
                "Shapes",
                "Current exporter surface",
                "Present in 25.10.2",
                "Decision",
            ),
            (
                (
                    row["namespace"],
                    row["event"],
                    f"truenas-api-v26/{row['documentation_path']}",
                    ", ".join(row["documented_shapes"]),
                    row["current_exporter_surface"],
                    row["present_in_25_10_2"],
                    row["decision"],
                )
                for row in audit["events"]
            ),
        ),
        "",
    ]
    return "\n".join(parts)


def build_compat_diff(v25_audit: dict[str, Any] | None = None) -> dict[str, Any]:
    if v25_audit is None:
        v25_audit = build_audit()
    v25_inventory = inventory_docs_for_target("25.10.2")
    v26_inventory = inventory_docs_for_target("26.0.0")
    v25_methods = {page.title: page for page in v25_inventory.methods}
    v26_methods = {page.title: page for page in v26_inventory.methods}
    v25_events = {page.title: page for page in v25_inventory.events}
    v26_events = {page.title: page for page in v26_inventory.events}
    current_methods = _current_exporter_methods(v25_audit)
    current_events = _current_exporter_events(v25_audit)

    def compare_pages(kind: str, current_names: set[str], old_pages: dict[str, ApiPage], new_pages: dict[str, ApiPage]):
        rows: list[dict[str, Any]] = []
        for name in sorted(current_names):
            old = old_pages.get(name)
            new = new_pages.get(name)
            if old is None:
                status = "current surface not present in 25.10.2 docs"
                changes = ["missing_25_10_2"]
            elif new is None:
                status = "absent in v26"
                changes = ["removed"]
            else:
                changes = _signature_changes(old, new)
                status = "schema changed in v26" if changes else "present in v26 with unchanged parsed signature"
            rows.append(
                {
                    "kind": kind,
                    "name": name,
                    "status": status,
                    "changed_signature_fields": changes,
                    "v25_path": old.path if old else "",
                    "v26_path": new.path if new else "",
                    "v25_signature": _page_signature(old) if old else {},
                    "v26_signature": _page_signature(new) if new else {},
                }
            )
        return rows

    method_rows = compare_pages("method", current_methods, v25_methods, v26_methods)
    event_rows = compare_pages("event", current_events, v25_events, v26_events)
    all_method_names = set(v25_methods) | set(v26_methods)
    all_event_names = set(v25_events) | set(v26_events)
    corpus_summary = {
        "methods_added_in_v26": len(set(v26_methods) - set(v25_methods)),
        "methods_removed_in_v26": len(set(v25_methods) - set(v26_methods)),
        "events_added_in_v26": len(set(v26_events) - set(v25_events)),
        "events_removed_in_v26": len(set(v25_events) - set(v26_events)),
        "common_methods": len(set(v25_methods) & set(v26_methods)),
        "common_events": len(set(v25_events) & set(v26_events)),
        "common_methods_with_parsed_signature_changes": sum(
            bool(_signature_changes(v25_methods[name], v26_methods[name]))
            for name in sorted(set(v25_methods) & set(v26_methods))
        ),
        "common_events_with_parsed_signature_changes": sum(
            bool(_signature_changes(v25_events[name], v26_events[name]))
            for name in sorted(set(v25_events) & set(v26_events))
        ),
    }
    current_summary = dict(sorted(Counter(row["status"] for row in [*method_rows, *event_rows]).items()))
    return {
        "schema_version": 1,
        "generator": "scripts/generate_api_exporter_parity.py --compat-diff",
        "targets": {
            "source": v25_inventory.evidence,
            "target": v26_inventory.evidence,
        },
        "corpus_summary": corpus_summary,
        "current_exporter_summary": current_summary,
        "required_surface_checks": _required_surface_checks(v25_methods, v26_methods, v25_events, v26_events),
        "current_exporter_methods": method_rows,
        "current_exporter_events": event_rows,
        "all_method_name_partition": {
            "added_in_v26": sorted(set(v26_methods) - set(v25_methods)),
            "removed_in_v26": sorted(set(v25_methods) - set(v26_methods)),
            "common": sorted(set(v25_methods) & set(v26_methods)),
        },
        "all_event_name_partition": {
            "added_in_v26": sorted(set(v26_events) - set(v25_events)),
            "removed_in_v26": sorted(set(v25_events) - set(v26_events)),
            "common": sorted(set(v25_events) & set(v26_events)),
        },
        "all_surface_count": len(all_method_names) + len(all_event_names),
    }


def render_compat_diff_markdown(diff: dict[str, Any]) -> str:
    source = diff["targets"]["source"]
    target = diff["targets"]["target"]
    parts = [
        "# TrueNAS SCALE 25.10.2 to 26.0.0 API compatibility diff",
        "",
        "This file is generated by `python3 scripts/generate_api_exporter_parity.py --compat-diff`. "
        "It compares the pinned local documentation corpora and the current exporter surfaces without live API access.",
        "",
        "## Pinned inputs",
        "",
        _markdown_table(
            ("Input", "Version", "Manifest", "Files", "Aggregate SHA-256"),
            (
                (
                    "source",
                    source["target_version"],
                    source["manifest_path"],
                    source["manifest_file_count"],
                    source["manifest_aggregate_sha256"],
                ),
                (
                    "target",
                    target["target_version"],
                    target["manifest_path"],
                    target["manifest_file_count"],
                    target["manifest_aggregate_sha256"],
                ),
            ),
        ),
        "",
        "## Corpus summary",
        "",
        _markdown_table(("Diff item", "Count"), diff["corpus_summary"].items()),
        "",
        "## Current exporter surface summary",
        "",
        _markdown_table(("Status", "Count"), diff["current_exporter_summary"].items()),
        "",
        "## Required COMPAT-01B surface checks",
        "",
        _markdown_table(
            ("Kind", "Name", "25.10.2", "26.0.0", "Decision"),
            (
                (row["kind"], row["name"], row["v25"], row["v26"], row["decision"])
                for row in diff["required_surface_checks"]
            ),
        ),
        "",
        "## Current exporter methods",
        "",
        _markdown_table(
            ("Method", "Status", "Changed parsed signature fields", "25.10.2 path", "26.0.0 path"),
            (
                (
                    row["name"],
                    row["status"],
                    ", ".join(row["changed_signature_fields"]) or "none",
                    f"truenas-api/{row['v25_path']}" if row["v25_path"] else "",
                    f"truenas-api-v26/{row['v26_path']}" if row["v26_path"] else "",
                )
                for row in diff["current_exporter_methods"]
            ),
        ),
        "",
        "## Current exporter events",
        "",
        _markdown_table(
            ("Event", "Status", "Changed parsed signature fields", "25.10.2 path", "26.0.0 path"),
            (
                (
                    row["name"],
                    row["status"],
                    ", ".join(row["changed_signature_fields"]) or "none",
                    f"truenas-api/{row['v25_path']}" if row["v25_path"] else "",
                    f"truenas-api-v26/{row['v26_path']}" if row["v26_path"] else "",
                )
                for row in diff["current_exporter_events"]
            ),
        ),
        "",
    ]
    return "\n".join(parts)


def build_audit() -> dict[str, Any]:
    file_rows, methods, events, evidence = inventory_docs()
    metrics = load_metric_contract()
    analysis = analyze_source(methods, events, {metric["variable"] for metric in metrics})
    dashboard_refs = dashboard_metric_references(metrics)
    metric_mappings = build_metric_mappings(metrics, methods, events, analysis, dashboard_refs)
    method_rows, safety_partition, method_decisions = build_method_rows(methods, analysis, metric_mappings)
    event_rows, event_decisions = build_event_rows(events, analysis, metric_mappings)
    namespace_rows = build_namespace_rows(method_rows, event_rows)
    evidence["metric_contract_count"] = len(metrics)
    evidence["method_rows_with_exact_12_columns"] = len(method_rows)
    return {
        "schema_version": 1,
        "evidence": evidence,
        "method_safety_partition": safety_partition,
        "method_decision_partition": method_decisions,
        "event_decision_partition": event_decisions,
        "metric_disposition_partition": dict(
            sorted(Counter(row["implementation_status"] for row in metric_mappings).items())
        ),
        "dashboard_evidence": _dashboard_summary(metric_mappings),
        "namespaces": namespace_rows,
        "files": file_rows,
        "methods": method_rows,
        "events": event_rows,
        "field_mappings": metric_mappings,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--target",
        default=TARGET_VERSION,
        help="Parity target to generate/check: 25.10.2 (default) or 26.0.0.",
    )
    parser.add_argument(
        "--compat-diff",
        action="store_true",
        help="Generate/check the 25.10.2-to-26.0.0 compatibility diff artifacts.",
    )
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.compat_diff:
        diff = build_compat_diff()
        rendered_json = json.dumps(diff, indent=2, sort_keys=True) + "\n"
        rendered_markdown = render_compat_diff_markdown(diff)
        check_or_write(
            COMPAT_DIFF_JSON,
            rendered_json,
            check=args.check,
            description="API compatibility diff JSON",
        )
        check_or_write(
            COMPAT_DIFF_MD,
            rendered_markdown,
            check=args.check,
            description="API compatibility diff Markdown",
        )
        print(
            json.dumps(
                {
                    "current_exporter_summary": diff["current_exporter_summary"],
                    "events": len(diff["current_exporter_events"]),
                    "methods": len(diff["current_exporter_methods"]),
                    "required_surface_checks": len(diff["required_surface_checks"]),
                },
                sort_keys=True,
            )
        )
        return

    try:
        target = resolve_api_docs_target(args.target)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    if target.version == "26.0.0":
        audit = build_v26_parity()
        rendered_json = json.dumps(audit, indent=2, sort_keys=True) + "\n"
        rendered_markdown = render_v26_parity_markdown(audit)
        check_or_write(V26_OUTPUT_JSON, rendered_json, check=args.check, description="v26 API parity JSON")
        check_or_write(V26_OUTPUT_MD, rendered_markdown, check=args.check, description="v26 API parity Markdown")
        print(
            json.dumps(
                {
                    "files": len(audit["files"]),
                    "methods": len(audit["methods"]),
                    "events": len(audit["events"]),
                    "method_decisions": audit["method_decision_partition"],
                    "event_decisions": audit["event_decision_partition"],
                },
                sort_keys=True,
            )
        )
        return
    if target.version != TARGET_VERSION:
        raise SystemExit(f"Parity target {target.version} is not supported")

    audit = build_audit()
    rendered_json = json.dumps(audit, indent=2, sort_keys=True) + "\n"
    rendered_markdown = render_markdown(audit)
    check_or_write(OUTPUT_JSON, rendered_json, check=args.check, description="API/exporter parity JSON")
    check_or_write(OUTPUT_MD, rendered_markdown, check=args.check, description="API/exporter parity Markdown")
    print(
        json.dumps(
            {
                "files": len(audit["files"]),
                "methods": len(audit["methods"]),
                "events": len(audit["events"]),
                "namespaces": len(audit["namespaces"]),
                "field_mappings": len(audit["field_mappings"]),
                "method_safety": audit["method_safety_partition"],
                "method_decisions": audit["method_decision_partition"],
                "metric_dispositions": audit["metric_disposition_partition"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
