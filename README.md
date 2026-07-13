<div align="center">

# TrueNAS Prometheus Exporter

Standalone Prometheus exporter for the TrueNAS JSON-RPC WebSocket API, with Docker-first deployment, safe metric defaults, and an included Grafana dashboard.

![TrueNAS SCALE 25.10.2 and 26.0.0](https://img.shields.io/badge/TrueNAS%20SCALE-25.10.2%20%2F%2026.0.0-0095d5?style=flat-square)
![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-3776ab?style=flat-square&logo=python&logoColor=white)
![Docker Ready](https://img.shields.io/badge/Docker-ready-2496ed?style=flat-square&logo=docker&logoColor=white)

[Quick start](#quick-start) • [Configuration](#configuration) • [Grafana dashboard](#grafana-dashboard) • [Testing](#testing)

</div>

Repository: `github.com/Unknowlars/truenas-scale-api-prometheus-exporter`

![System overview and CPU and load dashboard](.github/images/System_overview_and_CPU_and_Load.png)

## Dashboard Preview

The repository includes a ready-to-import Grafana dashboard covering system health, storage pools, disks, ZFS cache, services, apps, tasks, alerts, and virtualization.

| System & Performance | Memory |
| --- | --- |
| ![System overview and CPU and load dashboard](.github/images/System_overview_and_CPU_and_Load.png) | ![Memory dashboard](.github/images/Memory.png) |

| Storage and Pools | Storage Deep Dive |
| --- | --- |
| ![Storage and pools dashboard 1](.github/images/Storage_and_Pools_1.png) | ![Storage and pools dashboard 2](.github/images/Storage_and_Pools_2.png) |

| Dataset Deep Dive | Disks and Temperatures |
| --- | --- |
| ![Dataset deep dive dashboard](.github/images/Dataset_Deep_Dive.png) | ![Disks and temperatures dashboard](.github/images/Disks_Temperatures.png) |

| ZFS ARC Cache | Network Interfaces |
| --- | --- |
| ![ZFS ARC cache dashboard](.github/images/ZFS_ARC_Cache.png) | ![Network interfaces dashboard](.github/images/Network_Interfaces.png) |

| Services and Shares | Apps and Docker |
| --- | --- |
| ![Services and shares dashboard](.github/images/Services_Shares.png) | ![Apps and Docker dashboard](.github/images/Apps_and_Docker.png) |

| Apps and Docker (Details) | Virtualization |
| --- | --- |
| ![Apps and Docker details dashboard](.github/images/Apps_and_Docker_2.png) | ![Virtualization dashboard](.github/images/Virtualization.png) |

| Alerts, Tasks, and Updates | Audit and Directory Services |
| --- | --- |
| ![Alerts, tasks, and updates dashboard](.github/images/Alerts_andTasks_andUpdates.png) | ![Audit and directory services dashboard](.github/images/Audit_Directory_Services.png) |

| Security and Platform | System Configuration |
| --- | --- |
| ![Security and platform dashboard](.github/images/Security_and_Platform.png) | ![System configuration dashboard](.github/images/System_Configuration.png) |

| Advanced Protocols, NVMe-oF, FC, and HA | Boot Environment |
| --- | --- |
| ![Advanced protocols dashboard](.github/images/Advanced_Protocols_NVMe-oF_FC_HA.png) | ![Boot environment dashboard](.github/images/Boot_Environment.png) |

> [!IMPORTANT]
> This exporter was built mostly by AI over a few weeks running on my own truenas setup, its read only and follow the truenas API docs i have made a script to convert to markdown files in docs

## Overview

TrueNAS Prometheus Exporter connects to a TrueNAS system over the JSON-RPC WebSocket API, collects inventory and state data, and exposes Prometheus metrics on `/metrics` with a lightweight `/healthz` endpoint for container health checks.

It is designed to be easy to run publicly and easy to operate:

- single-file Python exporter with minimal runtime dependencies
- Docker and Docker Compose friendly out of the box
- documentation-audited metric coverage across storage, hardware, services, tasks, and alerts
- event-driven realtime updates for supported streams such as `reporting.realtime`, `app.stats`, and profile-eligible virtualization events
- bundled Grafana dashboard JSON and dashboard generator source
- conservative defaults that keep higher-cardinality options disabled unless you opt in

See [`docs/api-exporter-parity.md`](docs/api-exporter-parity.md) for the complete 25.10.2 method/field audit, [`docs/truenas-25-10-2-and-26-0-0-compatibility/api-compatibility-diff.md`](docs/truenas-25-10-2-and-26-0-0-compatibility/api-compatibility-diff.md) for the pinned 25.10.2/26.0.0 diff, and [`docs/modernization/README.md`](docs/modernization/README.md) for the reliability roadmap.

> [!IMPORTANT]
> This exporter is maintained against the pinned TrueNAS SCALE `25.10.2` and `26.0.0` API documentation. It selects a compatibility profile automatically from `system.version_short`; operators should not configure a manual version toggle.

## What You Get

- system identity, version, uptime, readiness, update, and reboot state
- pools, datasets, snapshots, scrub schedules, resilver configuration, expansion progress, and capacity
- documented physical-memory and ZFS ARC/L2ARC demand metrics, plus compatibility parsing for opaque CPU, disk-I/O, interface, and pool event objects
- SMB, NFS, iSCSI, NVMe-oF, services, apps, VMs, jobs, replication, and alerts
- dedicated coverage for DockerHub pull limits, VM capability flags, directory-service health, SMB/NFS security posture, audit retention/capacity, update profiles/downloads, NTP configuration rollups, iSCSI session features, and reporting retention
- exporter health signals such as API call failures and collector error counters

## TrueNAS 25.10.2 API Parity

The committed API snapshot is audited exhaustively, not sampled: 1,011 Markdown documents, 767 methods across 114 method namespaces, and 63 event sources are inventoried in [`docs/api-exporter-parity.md`](docs/api-exporter-parity.md). The runtime catalog contains 398 documentation-classified reads and 112 telemetry candidates. Generic discovery additionally blocks 60 sensitive full responses and 43 non-secret raw, opaque, identity-bearing, or configuration-heavy responses; only the three schema-owned event streams are subscribable.

The exporter exposes 405 contract-owned metrics. Generic method/event extraction remains an opt-in diagnostic feature and is not treated as semantic telemetry coverage. Numeric values under password, token, secret, private-key, and credential paths are suppressed even when generic extraction is enabled.

## TrueNAS 25.10.2 and 26.0.0 Compatibility

On every scrape connection and event-stream connection, the exporter authenticates, calls `system.version_short` once, and then selects one of three profiles before collector calls, discovery, count queries, or event subscriptions are attempted:

| Detected version | Selected profile | Behavior |
| --- | --- | --- |
| `25.10.*` | `25.10` | Uses the pinned 25.10.2 audited method and event surface. |
| `26.0.*` | `26.0` | Uses the pinned 26.0.0 audited surface and suppresses sources removed from v26. |
| anything else, malformed, or detection failure | `unknown` | Fails closed to the reviewed common intersection only. |

The `unknown` profile is intentionally conservative. Failed or unexpected version detection never expands API access, and there is no supported stale/manual API-version configuration knob.

Existing metric names, types, help text, and label sets are preserved across profiles. When a preserved metric declaration has no safe source in the selected profile, when permission is denied, or when a response is absent, malformed, non-finite, or stale, the exporter leaves the series absent or `NaN` according to the existing reset/staleness behavior. It does not emit fabricated zeros for unavailable compatibility data.

The pinned v26.0.0 diff marks these current exporter sources as unavailable under `26.0` and `unknown`, so they are suppressed before transport:

- `virt.instance.query`
- `virt.volume.query`
- `nvmet.global.sessions`
- `reporting.graphs`
- `reporting.netdata_graphs`
- `virt.instance.metrics`

Default event subscriptions are profile-aware:

| Profile | Default event subscriptions |
| --- | --- |
| `25.10` | `reporting.realtime`, `app.stats`, `virt.instance.metrics` |
| `26.0` | `reporting.realtime`, `app.stats` |
| `unknown` | `reporting.realtime`, `app.stats` |

Event lifecycle handling requires a valid string subscription ID from `core.subscribe`. Invalid or missing IDs are treated as subscription failures, and tracked IDs are passed to `core.unsubscribe` during clean shutdown and reconnect cleanup.

`app.image.query` remains eligible for reviewed count use in both pinned documentation sets. `pool.is_upgraded` remains blocked because it requires a pool id, and `pool.ddt_prefetch` remains prohibited because it is action-like and unsuitable for Prometheus collection.

The first 25.10/26.0 compatibility release continues to use the existing API-key authentication transport. Migration away from `auth.login_with_api_key` is a separate v27-readiness project and does not require operators to switch to password authentication for this release.

### Compatibility replacements and unavailable legacy metrics

Existing metric names, types, help text, and label sets remain intact. Where the documented API proved an old metric name or source wrong, use the replacement below; the legacy series is retained as a compatibility alias or becomes unavailable instead of reporting a fabricated zero.

| Legacy metric | Use instead | Compatibility behavior |
| --- | --- | --- |
| `truenas_pool_dedup_ratio` | `truenas_pool_dedup_table_size_bytes` | Legacy metric continues to carry the byte-valued `dedup_table_size` field. |
| `truenas_pool_expand_size_bytes` | `truenas_pool_expand_reflowed_bytes`, `truenas_pool_expand_to_reflow_bytes`, `truenas_pool_expand_percent` | Legacy metric aliases `bytes_to_reflow`; replacements expose the exact documented fields. |
| `truenas_network_gateway_reachable` | `truenas_network_default_gateway_configured` | The API response proves route presence, not reachability; the old metric remains an alias for configured route presence. |
| `truenas_boot_env_size_bytes` | `truenas_boot_environment_used_bytes` | Legacy metric aliases documented `used_bytes`. |
| `truenas_vm_flag_amd_asids` | `truenas_vm_flag_amd_asids_supported` | The API field is boolean; the old metric retains its 0/1 representation. |
| `truenas_certificate_days_to_expiry{name,issuer}` | `truenas_certificate_expiry_timestamp_seconds{name}` | The API does not document issuer data, so the legacy `issuer` label is `unknown`. |
| `truenas_directoryservices_fault_reason` | `truenas_directoryservices_fault_present` | The free-text fault message is redacted from the legacy label. |

The following legacy families are intentionally absent/NaN on 25.10.2 because no safe documented source exists: dataset referenced bytes; physical-memory free/cache/buffer and swap detail; per-disk temperature-alert counts; SMART result/enabled metrics; pool scrub last-run/state; generic task state/last-run and cloud-backup state; vdev error detail; SMB session/open-file/connection counts; NFS operation rate; FC port speed/online detail; virtual-volume size/global state; console-menu/serial-console flags; UPS live status; TrueNAS Connect/TrueCommand config status; and ARC aggregate max/min/hit counters. Secret- or PII-bearing configuration reads are also not used for SSH password-auth, KMIP, mail, proxy, support-contact, directory-service configuration-detail, or advanced-system configuration metrics. The generated dashboard does not reference these unavailable families or replace them with `or vector(0)`.

## Quick Start

If you are new to Prometheus exporters, start with Option 1 and follow the beginner checklist right after it.

### Option 1: Docker Compose

This builds the checked-out source and runs it locally.

```bash
cp .env.example .env
# Edit .env and set TRUENAS_WS_URL and TRUENAS_API_KEY
docker compose up -d --build
curl http://localhost:9108/healthz
curl http://localhost:9108/metrics
```

Compose reads `.env` and publishes `EXPORTER_PORT` on the same host port by default.

### Beginner Setup Checklist (Docker Compose)

1. On your TrueNAS system, create a read-only API key.
   Expected result: the key is created and visible in the TrueNAS API key list.
2. In this repo, run `cp .env.example .env`.
   Expected result: a new `.env` file exists in the project root.
3. Edit `.env` and set `TRUENAS_WS_URL` to your TrueNAS WebSocket endpoint (for example `wss://truenas.example.local/api/current`).
   Expected result: `TRUENAS_WS_URL` points to `/api/current` and has no placeholder value.
4. Set `TRUENAS_API_KEY` in `.env`.
   Expected result: `.env` contains your key and no spaces around `=`.
5. Start the exporter with `docker compose up -d --build`.
   Expected result: `docker compose ps` shows the `truenas-exporter` container as running.
6. Confirm the exporter is healthy at `http://localhost:9108/healthz`.
   Expected result: the endpoint returns `ok`.
7. Confirm metrics are exposed at `http://localhost:9108/metrics`.
   Expected result: output starts with Prometheus text such as `# HELP` and includes `truenas_up`.
8. Add a scrape config in Prometheus (or Grafana Alloy) and verify series appear.
   Expected result: querying `truenas_up` returns `1` for your exporter target.

### Option 2: Docker Image

Run the published container directly:

```bash
cp .env.example .env
docker pull ghcr.io/unknowlars/truenas-scale-api-prometheus-exporter:latest
docker run --rm \
  --env-file .env \
  -p 9108:9108 \
  ghcr.io/unknowlars/truenas-scale-api-prometheus-exporter:latest
```

If you want to build the image locally instead, use:

```bash
docker build -t ghcr.io/unknowlars/truenas-scale-api-prometheus-exporter:latest .
```

### Option 3: Run Locally with Python

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python3 truenas_exporter.py
```

## Configuration

Everything supported by the exporter is documented in `.env.example`. These are the settings most users will care about first:

| Variable | Required | Description |
| --- | --- | --- |
| `TRUENAS_WS_URL` | yes | TrueNAS WebSocket API URL, for example `wss://truenas.example.local/api/current` |
| `TRUENAS_API_KEY` | yes* | TrueNAS API key; use a read-only key. May be replaced by `TRUENAS_API_KEY_FILE`. |
| `TRUENAS_API_KEY_FILE` | no | Path to a mounted file containing the API key |
| `TRUENAS_CA_FILE` | no | Path to a custom CA bundle used for TrueNAS TLS verification |
| `TRUENAS_VERIFY_TLS` | no | Keep `true` in production; set `false` only for controlled testing |
| `EXPORTER_PORT` | no | HTTP port for `/metrics` and `/healthz`; default `9108` |
| `SCRAPE_INTERVAL_SECONDS` | no | Poll interval for regular collectors |
| `TRUENAS_TIMEOUT_SECONDS` | no | Timeout for API call batches |
| `SCRAPE_BUDGET_SECONDS` | no | Total deadline for a collector scrape; default `25` |
| `LOG_LEVEL` | no | `DEBUG`, `INFO`, `WARNING`, or `ERROR` |
| `EXPORTER_MODE` | no | Exporter runtime architecture: `collector` (default) or compatibility `legacy` |
| `ENABLE_EVENT_STREAMS` | no | Enable background event subscriptions |
| `EVENT_SUBSCRIPTIONS` | no | Comma-separated event streams to subscribe to |
| `EVENT_INTERVAL_SECONDS` | no | Interval used for supported realtime streams |
| `EVENT_STALE_AFTER_SECONDS` | no | Omit event metrics older than this many seconds; default `15` |
| `ENABLE_DATASET_METRICS` | no | Enable dataset collectors |
| `ENABLE_TASK_METRICS` | no | Enable task collectors |
| `ENABLE_IPMI_METRICS` | no | Enable IPMI collectors when available |
| `ENABLE_GENERIC_METHOD_METRICS` | no | Emit generic `METHOD_*` series from API responses (high cardinality); default `false` |
| `ENABLE_GENERIC_EVENT_METRICS` | no | Emit generic `EVENT_*` series from event payloads (high cardinality); default `false` |
| `DATASET_SNAPSHOT_FALLBACK_LIMIT` | no | Max per-dataset `snapshot_count` fallback API calls; `0` disables fallback (default) |

> [!NOTE]
> Higher-cardinality and discovery-heavy options are intentionally conservative by default. `AUTO_DISCOVER_METHODS`, `SCRAPE_ALL_METRICS`, and `EXTRA_METHODS` cannot bypass the documentation-derived read/candidate/sensitive-method policy. Review `.env.example` before enabling generic extraction or filesystem list operations in production.

For an intentional, read-only coverage pass, an operator may opt in locally:

```dotenv
SCRAPE_ALL_METRICS=true
DATASET_SNAPSHOT_FALLBACK_LIMIT=100
```

These settings increase API calls and series count; leave generic method/event
metrics and automatic discovery disabled unless they are needed for bounded
diagnostics.

## Architecture Modes

The exporter now supports two runtime modes behind `EXPORTER_MODE`:

- `collector` (default): a background single-flight scrape publishes complete atomic snapshots; HTTP requests never call TrueNAS.
- `legacy`: compatibility mode using the previous global-registry coordinator, retained for the 5.2 release.


Collector snapshots prevent torn reads, allow overlapping scrapes, and keep health and readiness endpoints responsive while TrueNAS is slow.

## Prometheus

Use `deploy/prometheus/prometheus.truenas-example.yml` as a starting point, or add a scrape job like this:

```yaml
scrape_configs:
  - job_name: truenas_exporter
    scrape_interval: 30s
    static_configs:
      - targets:
          - truenas-exporter:9108
```

If Prometheus runs outside Docker, replace `truenas-exporter:9108` with the reachable host or IP of the exporter.

### Grafana Alloy (instead of Prometheus scrape config)

If you use Grafana Alloy to scrape and forward metrics instead of managing `prometheus.yml` directly, add a scrape block like this:

```hcl
prometheus.scrape "truenasexporter" {
  targets = [{
    __address__ = "192.168.0.238:9108",
  }]

  forward_to = [prometheus.remote_write.local.receiver]
}
```

Replace `192.168.0.238:9108` with your exporter host and port. The `forward_to` target should match your existing Alloy `prometheus.remote_write` component name.

The repo also includes `deploy/prometheus/docker-compose.prometheus.yml` and `deploy/prometheus/prometheus.yml` for local experiments. Update those targets before publishing or using them outside your own environment.

## Grafana Dashboards

The repository includes two importable dashboards in `grafana-dashboard/`:

| Dashboard | File | Requires |
| --- | --- | --- |
| TrueNAS · Mission Control (tabbed flagship) | `truenas-mission-control.json` | Grafana 13+ (dynamic dashboards, schema v2) |
| TrueNAS Operations Center (classic rows) | `operations-center-dashboard.json` | Any recent Grafana |

### Mission Control (Grafana 13+)

A 12-tab dynamic dashboard covering the full metric surface, with a hero
Overview tab for the 30-second health check. It uses the Grafana dashboard
schema v2 (`dashboard.grafana.app/v2beta1`), so it needs Grafana 13 or later.

1. Open Grafana and go to `Dashboards` -> `New` -> `Import`.
2. Upload `grafana-dashboard/truenas-mission-control.json`.
3. Choose your Prometheus data source in the `Datasource` variable after import.

Alternatively push it via the App Platform API:

```bash
curl -X POST -H "Authorization: Bearer $GRAFANA_SA_TOKEN" \
  -H "Content-Type: application/json" \
  --data-binary @grafana-dashboard/truenas-mission-control.json \
  "https://<grafana-host>/apis/dashboard.grafana.app/v2beta1/namespaces/default/dashboards"
```

The dashboard is generated code: edit and re-run
`grafana-dashboard/build_mission_control.py` (no dependencies beyond Python 3)
instead of hand-editing the JSON. The builder harvests panel queries from the
classic Operations Center dashboard, so query fixes should land there first.

Builder notes:

- It probes the live exporter (`TRUENAS_EXPORTER_URL`, default
  `http://192.168.0.247:9108/metrics`) and moves panels whose metrics are
  never emitted on your system into a collapsed "Not collected on this
  system" row per tab. Observed metric names accumulate in the gitignored
  `grafana-dashboard/.metric-names-cache.json`.
- To update an already-imported copy, delete the old dashboard in Grafana and
  import the regenerated JSON again (it keeps the same
  `metadata.name`/URL), or `PUT` it to
  `/apis/dashboard.grafana.app/v2beta1/namespaces/default/dashboards/truenas-mission-control`.

### Metric behavior notes (relevant to dashboards)

Observed against TrueNAS SCALE 25.10.3 (July 2026):

- `/metrics` serves a cached in-memory snapshot (~10 ms response). The
  `truenas_scrape_duration_seconds` metric measures the background collection
  cycle (~17 s), not HTTP latency — short Prometheus scrape timeouts are fine.
- Realtime metrics (`truenas_cpu_*_percent`, several
  `truenas_memory_*_bytes`, SMB/NFS activity, ZFS ARC rates) intermittently
  report `NaN` between event updates. Grafana renders NaN samples as line
  breaks; dashboard queries should drop them with a comparison filter, e.g.
  `avg((truenas_cpu_user_percent >= 0))`. The Mission Control builder applies
  this automatically to all timeseries panels.
- The `truenas_zfs_*_hit_ratio` gauges are unreliable (0.0 or NaN even under
  load); compute hit percentages from the corresponding
  `*_hits_per_second` / `*_misses_per_second` gauges instead.
- Some metrics are emitted only when their subject exists or something is
  happening (`truenas_job_*`, `truenas_api_call_errors_total`,
  `truenas_certificate_*`, per-core CPU metrics, Incus/VM metrics). Zero
  samples for these is normal, not an exporter fault.

### Operations Center (classic)

1. Open Grafana and go to `Dashboards` -> `Import`.
2. Upload `grafana-dashboard/operations-center-dashboard.json`.
3. Choose your Prometheus data source.
4. Save the dashboard.


## Included Files

| Path | Purpose |
| --- | --- |
| `truenas_exporter.py` | Source-checkout compatibility launcher |
| `src/truenas_exporter/` | Exporter package implementation |
| `Dockerfile` | Container image build |
| `docker-compose.yml` | Main Docker Compose deployment |
| `.env.example` | Example environment configuration |
| `deploy/prometheus/prometheus.truenas-example.yml` | Minimal Prometheus scrape config |
| `grafana-dashboard/operations-center-dashboard.json` | Importable Grafana dashboard (classic) |
| `grafana-dashboard/truenas-mission-control.json` | Tabbed flagship dashboard (Grafana 13+, schema v2) |
| `grafana-dashboard/build_mission_control.py` | Mission Control dashboard builder |
| `scripts/generate_truenas_dashboard.py` | Dashboard generator source |
| `scripts/convert_truenas_api_docs_to_markdown.py` | Offline API docs converter |
| `scripts/generate_api_exporter_parity.py` | Exhaustive API/exporter parity inventory generator |
| `docs/api-exporter-parity.md` | Human-readable method, event, namespace, and field audit |
| `docs/api-exporter-parity.json` | Machine-readable exhaustive parity audit |
| `docs/metrics-contract.json` | Machine-readable Prometheus metric contract |
| `docs/modernization/README.md` | Tracked reliability and architecture roadmap |
| `docs/realtime-metrics-fix-plan.md` | Diagnosis + fix plan for 25.10 realtime parser gaps (handover) |
| `tests/` | Unit tests for collector and event behavior |

## Testing

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements-dev.txt
./scripts/validate.sh
```

The validation script runs linting, static typing, branch coverage, generated-asset checks, Compose validation, and a container build. Set `RUN_PYTHON_MATRIX=1` to test Python 3.12, 3.13, and 3.14 in local containers. No hosted CI is used by design.

## Cardinality and Series Impact

Not all configuration options produce the same number of Prometheus time series. The table below summarises which toggles increase cardinality and their expected impact on a typical system.

| Option | Default | Cardinality impact |
| --- | --- | --- |
| `ENABLE_GENERIC_METHOD_METRICS` | `false` | **High** — generates `METHOD_*` series with `[method, path]` labels. Can produce 50k–500k+ series with discovery enabled. |
| `ENABLE_GENERIC_EVENT_METRICS` | `false` | **High** — generates `EVENT_*` series with `[event, path]` labels. Grows with event payload complexity. |
| `AUTO_DISCOVER_METHODS` | `false` | **High** — discovers only documentation-classified telemetry candidates and feeds safe, non-sensitive results through generic extraction. |
| `SCRAPE_ALL_METRICS` | `false` | **High** — adds reviewed telemetry candidates beyond the base set; mutation/action, credential, and entity-specific methods remain blocked. |
| `DATASET_SNAPSHOT_FALLBACK_LIMIT` | `0` | **Medium** — each non-zero value adds up to N extra API calls per scrape for per-dataset snapshot counts. |
| `ENABLE_FILESYSTEM_LISTDIR` | `false` | **Medium** — adds per-path directory listing metrics with generic extraction. |
| `ENABLE_DATASET_METRICS` | `true` | **Low–Medium** — one set of labelled gauges per dataset. Grows linearly with dataset count. |
| `ENABLE_TASK_METRICS` | `true` | **Low** — one set per configured task (replication, cloudsync, rsync, snapshot). |
| `ENABLE_IPMI_METRICS` | `true` | **Low** — fixed set of IPMI chassis and SEL gauges. |

When enabling high-cardinality options, monitor `prometheus_tsdb_head_series` and plan TSDB storage accordingly. Start with dedicated metrics (the default) and only enable generic extraction for debugging or gap analysis.

Dedicated collectors remain active regardless of `ENABLE_GENERIC_METHOD_METRICS` and `ENABLE_GENERIC_EVENT_METRICS`; those generic toggles stay opt-in and disabled by default.

## Operational Notes

- `/healthz` confirms the exporter process is serving HTTP; it does not guarantee the last scrape succeeded
- `/readyz` returns `200` only after a recent successful scrape and otherwise returns `503`
- some collectors only produce metrics when the related TrueNAS service or subsystem is enabled
- event-driven metrics depend on supported TrueNAS event streams and API behavior
- enabling discovery-heavy options can increase Prometheus series count quickly on large systems

## Troubleshooting

- verify that `TRUENAS_WS_URL` points to the TrueNAS WebSocket endpoint ending in `/api/current`
- confirm the API key can read the resources you expect to scrape
- if your TrueNAS instance uses a self-signed certificate, trust the CA where possible instead of disabling TLS verification
- check container logs with `docker compose logs -f truenas-exporter` when startup or authentication fails

If you hit a bug or want to request additional coverage, open an issue at `https://github.com/Unknowlars/truenas-scale-api-prometheus-exporter/issues` with your TrueNAS version, the relevant config toggles, and an example of the missing metric or API response.
