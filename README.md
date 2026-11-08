<div align="center">

# TrueNAS Prometheus Exporter

**Is my NAS OK?** Get the answer in two seconds.

A read-only Prometheus exporter for TrueNAS SCALE, with a Grafana dashboard
that shows the health of your whole NAS at a glance. Nothing gets installed
on TrueNAS.

![TrueNAS SCALE 27.0 primary, 25.10 and 26.0 retained](https://img.shields.io/badge/TrueNAS%20SCALE-27.0%20%7C%2026.0%20%7C%2025.10-0095d5?style=flat-square)
![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-3776ab?style=flat-square&logo=python&logoColor=white)
![Docker Ready](https://img.shields.io/badge/Docker-ready-2496ed?style=flat-square&logo=docker&logoColor=white)
![Read-only](https://img.shields.io/badge/access-read--only-3fb950?style=flat-square)
![Grafana 13](https://img.shields.io/badge/Grafana-13%2B-f46800?style=flat-square&logo=grafana&logoColor=white)

[Quick start](#quick-start) • [The dashboard](#the-dashboard) • [Configuration](#configuration) • [Troubleshooting](#troubleshooting)

</div>

![TrueNAS Mission Control: health verdict, key numbers and health checks](grafana-dashboard/screenshots/hero-overview.png)

<sub>Screenshots use made-up demo data (host `nas-demo`, pools `tank` and `flash`).</sub>

## Why use it

| | |
| --- | --- |
| 🛡️ **Read-only, guaranteed** | Every API call is checked against an allow-list *before* it is sent. The exporter cannot change anything on your NAS. |
| 📦 **Nothing to install on TrueNAS** | Run one small container next to Prometheus and give it a read-only API key. |
| 🚦 **Answers, not just graphs** | The dashboard shows a single verdict (healthy, attention or action needed) and tells you *why*. |
| 🩶 **Honest about missing data** | Grey **N/A** means "no data / not present / disabled". A missing value never shows up as a healthy green. |
| 🔢 **400+ metrics** | Pools, datasets, disks and temperatures, ZFS ARC, CPU, memory, network, shares, apps, VMs, alerts, certificates and more. |
| 🔄 **Knows your TrueNAS version** | Detects 25.10, 26.0 and 27.0 automatically and adapts to what each release reports. |

## Quick start

You need a TrueNAS SCALE system (27.0 is the main target; 25.10 and 26.0 are
supported), a machine with Docker, and about five minutes.

### 1. Create a read-only API key on TrueNAS

1. In the TrueNAS web UI, open the account menu (top right) and choose **API Keys**. On some versions it is under **Settings → API Keys** or **Credentials → Users**.
2. Click **Add** and name the key, for example `prometheus-exporter`.
3. If your version supports it, attach the key to an account with a **Read-only** role.
4. Save, and copy the key straight away: TrueNAS shows it only once.

> [!TIP]
> The exporter only ever makes read-only calls, so even a full-access key is used safely. A read-only key is extra protection.

### 2. Configure

```bash
cp .env.example .env
```

Set two values in `.env`:

```dotenv
# Your TrueNAS address with /api/current at the end (wss:// for HTTPS).
TRUENAS_WS_URL=wss://192.168.1.50/api/current

# The read-only API key from step 1.
TRUENAS_API_KEY=1-your-api-key-here
```

> [!IMPORTANT]
> TrueNAS uses a self-signed certificate by default. If the connection fails,
> set `TRUENAS_VERIFY_TLS=false` (only on a trusted LAN), or keep
> verification on and point `TRUENAS_CA_FILE` at your CA bundle.

### 3. Start it

```bash
docker compose up -d --build
```

### 4. Check it works

```bash
curl http://localhost:9108/healthz     # → ok
curl http://localhost:9108/metrics     # → Prometheus metrics
```

If you see `truenas_up 1`, the exporter is connected. 🎉

<details>
<summary>Other ways to run it: plain Docker image or local Python</summary>

**Docker image**

```bash
cp .env.example .env      # set TRUENAS_WS_URL and TRUENAS_API_KEY
docker pull ghcr.io/unknowlars/truenas-scale-api-prometheus-exporter:latest
docker run --rm --env-file .env -p 9108:9108 \
  ghcr.io/unknowlars/truenas-scale-api-prometheus-exporter:latest
```

**Local Python (3.12+)**

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
# The exporter reads the process environment only; it does not load `.env`.
# Keep the key in a file (mode 600) instead of the shell history:
install -m 600 /dev/null ./truenas_api_key   # then paste the key into it
export TRUENAS_WS_URL=wss://truenas.local/api/current
export TRUENAS_API_KEY_FILE="$PWD/truenas_api_key"
python3 truenas_exporter.py
```

Any other setting from `.env.example` can be exported the same way. Do not
put the key file in a directory you commit or build images from.

</details>

### 5. Point Prometheus at it

Add a scrape job (or start from [`deploy/prometheus/prometheus.truenas-example.yml`](deploy/prometheus/prometheus.truenas-example.yml)):

```yaml
scrape_configs:
  - job_name: truenas_exporter
    scrape_interval: 30s
    static_configs:
      - targets:
          - truenas-exporter:9108   # or the exporter host/IP, e.g. 192.168.1.60:9108
```

<details>
<summary>Using Grafana Alloy instead</summary>

```hcl
prometheus.scrape "truenasexporter" {
  targets = [{
    __address__ = "192.168.1.60:9108",
  }]
  forward_to = [prometheus.remote_write.local.receiver]
}
```

Replace the address with your exporter host and port, and point `forward_to`
at your existing `prometheus.remote_write` component. For local experiments
the repo also includes `deploy/prometheus/docker-compose.prometheus.yml` and
`deploy/prometheus/prometheus.yml`; update their targets before use.

</details>

### 6. Import the dashboard

In Grafana, go to **Dashboards → New → Import** and upload
[`grafana-dashboard/truenas-mission-control.json`](grafana-dashboard/truenas-mission-control.json).
Then pick your Prometheus data source. That's it.

## The dashboard

**TrueNAS · Mission Control** is the main dashboard (Grafana 13 or newer).
It opens on one question, *"Is my NAS OK?"*, and lets you drill down from
there.

### How to read it

| Colour | Meaning |
| --- | --- |
| 🟢 **Green** | Healthy, within limits |
| 🟠 **Amber** | Needs attention soon |
| 🔴 **Red** | Something is broken: act now |
| 🔵 **Blue** | Information (counts, sizes, capabilities) |
| ⚪ **Grey N/A** | No data, not present, or turned off on purpose. **Never a hidden "OK".** |

- **The verdict** (*Is my NAS OK?*) is the worst of eight checks: exporter reachable, TrueNAS ready, pools healthy, boot pool healthy, no outstanding alerts, pools below 80 %/90 %, disks below 45/55 °C, and data less than 5/15 minutes old. The **Health checks** table next to it shows which one fired.
- **Click any tile** to jump to the tab with the details. Pool, disk, app and dataset names in tables are links too.
- **"Alerts" means outstanding alerts.** Alerts you dismissed in TrueNAS are not counted.

### What each tab answers

| Tab | Answers |
| --- | --- |
| 🏠 **Overview** | Is everything OK? Which pool fills first, and when? Which disk is hottest? |
| 🚑 **Incident** | What is failing *right now*, and what changed recently? |
| 💻 **Compute** | How busy are the CPU and memory? (RAM is shown with and without the ZFS cache.) |
| 🗄️ **Pools & ZFS** | How full is each pool, how fast is it growing, did the last scrub pass, is the cache working? |
| 📁 **Datasets** | What uses the most space? Where is snapshot space going? |
| 💿 **Disks & Hardware** | Which disks are hot or saturated? What hardware is installed? |
| 🌐 **Network** | How much traffic is on each interface? Are links up? |
| 🔗 **Shares & Protocols** | Which services and shares are running? Who is connected? |
| 📦 **Apps & Docker** | Which apps use the most CPU and memory? Any updates? |
| 🖥️ **VMs & Virt** | Which VMs and containers exist, and how much do they use? |
| 🚨 **Alerts & Jobs** | Which alerts are open? Which tasks and jobs are running? |
| 🔐 **Security & Audit** | Is 2FA on? Are certificates or API keys expiring? Are directory services healthy? |
| ⚙️ **Exporter & Config** | Is the exporter itself healthy, and how fast is it? |

Features you don't use (IPMI, UPS, HA, NVMe-oF, directory services, VMs)
show grey **None** or **N/A**, and their detail sections stay collapsed.

### Screenshots

| Overview | Incident |
| --- | --- |
| ![Overview tab](grafana-dashboard/screenshots/mc-00-overview.png) | ![Incident tab](grafana-dashboard/screenshots/mc-01-incident.png) |

| Pools & ZFS | Disks & Hardware |
| --- | --- |
| ![Pools and ZFS tab](grafana-dashboard/screenshots/mc-03-pools-zfs.png) | ![Disks and hardware tab](grafana-dashboard/screenshots/mc-05-disks-hardware.png) |

<details>
<summary><b>More tabs</b></summary>

| Compute | Datasets |
| --- | --- |
| ![Compute tab](grafana-dashboard/screenshots/mc-02-compute.png) | ![Datasets tab](grafana-dashboard/screenshots/mc-04-datasets.png) |

| Network | Shares & Protocols |
| --- | --- |
| ![Network tab](grafana-dashboard/screenshots/mc-06-network.png) | ![Shares and protocols tab](grafana-dashboard/screenshots/mc-07-shares-protocols.png) |

| Apps & Docker | VMs & Virt |
| --- | --- |
| ![Apps and Docker tab](grafana-dashboard/screenshots/mc-08-apps-docker.png) | ![VMs and virtualization tab](grafana-dashboard/screenshots/mc-09-vms-virt.png) |

| Alerts & Jobs | Security & Audit |
| --- | --- |
| ![Alerts and jobs tab](grafana-dashboard/screenshots/mc-10-alerts-jobs.png) | ![Security and audit tab](grafana-dashboard/screenshots/mc-11-security-audit.png) |

| Exporter & Config | |
| --- | --- |
| ![Exporter and config tab](grafana-dashboard/screenshots/mc-12-exporter-config.png) | |

</details>

<details>
<summary><b>Light theme and the "no data" state</b></summary>

| Light theme | No data at all |
| --- | --- |
| ![Overview in light theme](grafana-dashboard/screenshots/mc-00-overview-light.png) | ![Overview with an empty Prometheus: every value is grey N/A](grafana-dashboard/screenshots/mc-00-overview-empty.png) |

With no data, every value reads grey **N/A**: nothing pretends to be healthy.

</details>

### Two dashboards: which one?

| Dashboard | File | Use it when |
| --- | --- | --- |
| **TrueNAS · Mission Control** ⭐ | `truenas-mission-control.json` | You run **Grafana 13+**. Tabs, health verdict, Incident view. |
| TrueNAS Operations Center | `operations-center-dashboard.json` | You run an older Grafana. The same queries in collapsible rows. |

<details>
<summary>Classic Operations Center screenshots</summary>

| System overview | Storage & pools |
| --- | --- |
| ![Classic system overview row](grafana-dashboard/screenshots/classic-00-system-overview.png) | ![Classic storage and pools row](grafana-dashboard/screenshots/classic-03-storage-pools.png) |

Every row is in [`grafana-dashboard/screenshots/`](grafana-dashboard/screenshots/) (`classic-*.png`).

</details>

<details>
<summary>Good to know about TrueNAS 27</summary>

TrueNAS 27 reports some data differently, and the dashboard adapts:

- **Disk I/O** is reported for all disks together, so disk charts show one "total" line instead of one line per disk.
- **CPU time breakdown** (user/system) is not reported; that panel says *"Not reported by TrueNAS 27"*.
- **Per-pool read/write speed** is not reported; the Overview shows storage throughput from the disks instead.
- **ZFS cache hit rates** are calculated by the dashboard, because TrueNAS 27 reports them as 0 %.

</details>

<details>
<summary>For developers: rebuilding and pushing the dashboards</summary>

Both dashboards are generated; never edit the JSON by hand.

- `scripts/generate_truenas_dashboard.py` owns every query, colour and shared rule.
- `grafana-dashboard/build_mission_control.py` builds Mission Control on top of it.

```bash
python3 scripts/generate_truenas_dashboard.py
python3 grafana-dashboard/build_mission_control.py
python3 scripts/validate_dashboard.py
```

Generation is offline and deterministic. The optional
`--metric-names /private/names.json` takes a local names-only list for a
private layout; do not commit that output.

Push Mission Control through the Grafana App Platform API:

```bash
curl -X POST -H "Authorization: Bearer $GRAFANA_SA_TOKEN" \
  -H "Content-Type: application/json" \
  --data-binary @grafana-dashboard/truenas-mission-control.json \
  "https://<grafana-host>/apis/dashboard.grafana.app/v2beta1/namespaces/default/dashboards"
```

To update an imported copy, delete it and re-import, or `PUT` to
`.../dashboards/truenas-mission-control` (same `metadata.name` and URL).

</details>

## Configuration

Every option is documented in [`.env.example`](.env.example). The settings most people touch:

| Variable | Default | What it does |
| --- | --- | --- |
| `TRUENAS_WS_URL` | — (**required**) | TrueNAS WebSocket URL, e.g. `wss://192.168.1.50/api/current` |
| `TRUENAS_API_KEY` | — (**required**\*) | Read-only API key (\*or use `TRUENAS_API_KEY_FILE`) |
| `TRUENAS_API_KEY_FILE` | unset | Path to a mounted file containing the key (Docker/Kubernetes secrets). Never commit it. |
| `TRUENAS_USERNAME` | unset | Key owner's username; enables `auth.login_ex` with explicit success checking |
| `TRUENAS_VERIFY_TLS` | `true` | Set `false` only on a trusted LAN with a self-signed certificate |
| `TRUENAS_CA_FILE` | — | Custom CA bundle for TLS verification |
| `EXPORTER_PORT` | `9108` | Port for `/metrics`, `/healthz`, `/readyz` |
| `EXPORTER_BIND_ADDRESS` | `""` (all) | Bind host/IP; hostnames, IPv4 and bracket-free IPv6 (e.g. `::1`) |
| `SCRAPE_INTERVAL_SECONDS` | `30` | How often the exporter polls TrueNAS |
| `SCRAPE_BUDGET_SECONDS` | `25` | Hard deadline for one poll |
| `LOG_LEVEL` | `INFO` | `DEBUG`, `INFO`, `WARNING` or `ERROR` |
| `ENABLE_DATASET_METRICS` | `true` | Per-dataset space and quota metrics |
| `ENABLE_TASK_METRICS` | `true` | Replication, cloud sync, rsync and snapshot task metrics |
| `ENABLE_IPMI_METRICS` | `true` | IPMI chassis and sensor metrics when available |
| `MAX_GENERIC_SERIES` | `10000` | Safety cap for the (off-by-default) generic series |

> [!NOTE]
> The defaults are deliberately conservative. The high-volume options
> (`ENABLE_GENERIC_METHOD_METRICS`, `ENABLE_GENERIC_EVENT_METRICS`,
> `AUTO_DISCOVER_METHODS`, `SCRAPE_ALL_METRICS`) are off by default and can
> never bypass the read-only rules. See [How it works](#how-it-works) before
> turning them on.

## Supported TrueNAS versions

| TrueNAS SCALE | Status | Evidence |
| --- | --- | --- |
| **27.0.x** | Primary target | Official 27.0.0 docs and mocked tests; authenticated read-only live checks against `27.0.0-RC.1` (latest 2026-11-07, including the dashboards). GA 27.0 not yet live-verified. |
| 26.0.x | Supported | Pinned 26.0.0 docs and mocked tests; no current live verification. |
| 25.10.x | Supported | Pinned 25.10.2 docs and mocked tests; historical live use on 25.10.3. |
| Other | Conservative | Unknown releases only get the reviewed common API surface. |

More detail: [migration notes](docs/truenas27-migration.md),
[compatibility matrix](docs/reviews/truenas27-api-compatibility.md) and
[metric inventory](docs/reviews/truenas27-metric-coverage.md).

## What gets collected

- **System**: identity, version, uptime, readiness, updates, reboot state.
- **Storage**: pools, datasets, snapshots, scrubs, resilver, expansion, capacity, fragmentation, dedup.
- **Disks**: I/O rates, busy %, temperatures.
- **Memory and ZFS**: physical memory, ARC size, ARC/L2ARC hit and miss rates.
- **Sharing**: SMB, NFS, iSCSI, NVMe-oF.
- **Workloads**: apps and Docker (incl. DockerHub pull limits), VMs, jobs, replication.
- **Health and governance**: alerts, certificates, directory services, audit, NTP, UPS, security settings.
- **Exporter self-health**: API failures, collector errors, poll duration.

The [telemetry expansion](docs/telemetry-expansion.md) adds 47 more metric
families (scan details, dataset tuning, SED status, UPS readings, cloud-backup
results, ZFS tiering). Values your hardware or configuration doesn't provide
stay absent or `NaN`; they never become a fake `0`.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Connection or TLS error with `wss://` | Self-signed certificate: set `TRUENAS_VERIFY_TLS=false` on a trusted LAN, or set `TRUENAS_CA_FILE`. |
| `truenas_up 0` or authentication fails | Check `TRUENAS_API_KEY` and that the URL ends in `/api/current`. |
| Container won't start | `docker compose logs -f truenas-exporter`; usually a `.env` typo. |
| A dashboard tile shows grey **N/A** | No data for it: the feature isn't used, isn't reported by your TrueNAS version, or Prometheus isn't scraping. Grey is never an error by itself. |
| The verdict says **Attention** | Look at the *Health checks* table next to it, or open the **Incident** tab. |
| Disk charts show only a "total" line | Expected on TrueNAS 27, which reports combined disk I/O. |
| Some metrics are missing | Many collectors only report when the related service or hardware is in use. |
| Values flicker to `NaN` in your own queries | Realtime values update between events; filter with e.g. `avg(truenas_cpu_usage_percent >= 0)`. The bundled dashboards already do this. |

Health endpoints:

- `GET /healthz`: the process is serving HTTP (it does not prove the last poll worked).
- `GET /readyz`: `200` while the last *successful* poll is recent (within max(2×budget, 2×interval, 30 s)), otherwise `503`. One failed poll sets `truenas_up 0` without making the exporter unready.
- `truenas_event_stream_up` reports an *active subscription*, not data freshness.

Still stuck? [Open an issue](https://github.com/Unknowlars/truenas-scale-api-prometheus-exporter/issues) with your TrueNAS version, the settings you changed, and what you expected.

## Testing

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements-dev.txt
./scripts/validate.sh
```

`validate.sh` runs linting, type checks, tests with branch coverage,
generated-file checks (including both dashboards), Compose validation and a
container build. Set `RUN_PYTHON_MATRIX=1` to also test Python 3.12, 3.13
and 3.14. No hosted CI is used, by design.

> [!NOTE]
> This project was developed largely with AI assistance, against live home
> TrueNAS SCALE systems (25.10.3 and 27.0.0-RC.1). It is strictly read-only
> and follows the official TrueNAS API documentation.

## How it works

<details>
<summary>Runtime modes (<code>EXPORTER_MODE</code>)</summary>

<br>

- `collector` (default): a background poll publishes complete, atomic snapshots. `/metrics` serves the cached snapshot (about 10 ms) and never waits on TrueNAS, so readings are never half-updated and the health endpoints stay responsive when the NAS is slow.
- `legacy`: the previous global-registry coordinator, kept for the 5.2 release.

`truenas_scrape_duration_seconds` measures the background poll (typically 10–20 s), not HTTP latency, so short Prometheus scrape timeouts are fine.

</details>

<details>
<summary>Version detection and compatibility profiles</summary>

<br>

On every connection the exporter authenticates, calls `system.version_short`
once, and picks a profile before any other call:

| Detected version | Profile | Behavior |
| --- | --- | --- |
| `25.10.*` | `25.10` | Pinned 25.10.2 audited method and event surface. |
| `26.0.*` | `26.0` | Pinned 26.0.0 surface; sources removed in v26 are suppressed. |
| `27.0.*` | `27.0` | 27.0.0 surface (primary target). |
| Anything else or detection failure | `unknown` | Fails closed to the reviewed common intersection only. |

A failed detection never widens API access, and there is no manual version
toggle. Sources removed in v26 (`virt.instance.query`, `virt.volume.query`,
`reporting.graphs`, `reporting.netdata_graphs`, `virt.instance.metrics`) are
suppressed before transport under `26.0`, `27.0` and `unknown`.

| Profile | Default event subscriptions |
| --- | --- |
| `25.10` | `reporting.realtime`, `app.stats`, `virt.instance.metrics` |
| `26.0` / `27.0` / `unknown` | `reporting.realtime`, `app.stats`, `container.metrics` |

</details>

<details>
<summary>Safety model and API parity</summary>

<br>

- **Read-only, enforced before transport.** Every method is checked against a documentation-derived allow-list and a mutating-verb deny-list before the WebSocket call. `AUTO_DISCOVER_METHODS`, `SCRAPE_ALL_METRICS` and `EXTRA_METHODS` cannot bypass this.
- **No fabricated data.** When a value has no safe source, or a response is denied, absent, malformed or stale, the series stays absent or `NaN` instead of a fake `0`.
- **Secrets suppressed.** Values under password, token, secret, private-key and credential paths are never emitted.
- **Audited, not sampled.** The committed API snapshot inventories 767 methods across 114 namespaces and 63 event sources; see [`docs/api-exporter-parity.md`](docs/api-exporter-parity.md), the [25.10/26.0 diff](docs/truenas-25-10-2-and-26-0-0-compatibility/) and the [reliability roadmap](docs/modernization/README.md).

Metric names, types, help text and labels are preserved across releases;
replacements ship as compatibility aliases with documented deprecations.

</details>

<details>
<summary>Cardinality and series impact</summary>

<br>

| Option | Default | Impact |
| --- | --- | --- |
| `ENABLE_GENERIC_METHOD_METRICS` | `false` | High: `METHOD_*` series with `[method, path]` labels; 50k–500k+ with discovery. |
| `ENABLE_GENERIC_EVENT_METRICS` | `false` | High: `EVENT_*` series with `[event, path]` labels. |
| `AUTO_DISCOVER_METHODS` | `false` | High: feeds safe telemetry candidates through generic extraction. |
| `SCRAPE_ALL_METRICS` | `false` | High: adds reviewed telemetry candidates beyond the base set. |
| `DATASET_SNAPSHOT_FALLBACK_LIMIT` | `25` | Medium: up to N extra API calls per poll for per-dataset snapshot counts (on 27 these counts are partial beyond N). |
| `ENABLE_FILESYSTEM_LISTDIR` | `false` | Medium: per-path directory-listing metrics. |
| `ENABLE_DATASET_METRICS` | `true` | Low–medium: one gauge set per dataset. |
| `ENABLE_TASK_METRICS` | `true` | Low: one set per configured task. |
| `ENABLE_IPMI_METRICS` | `true` | Low: fixed IPMI sensor set. |

If you enable the high-cardinality options, watch `prometheus_tsdb_head_series` and plan storage accordingly.

</details>

<details>
<summary>Repository layout</summary>

<br>

| Path | Purpose |
| --- | --- |
| `truenas_exporter.py` | Source-checkout launcher |
| `src/truenas_exporter/` | Exporter package |
| `Dockerfile`, `docker-compose.yml` | Container build and deployment |
| `.env.example` | Example configuration |
| `deploy/prometheus/` | Example Prometheus scrape configs and compose |
| `grafana-dashboard/*.json` | Importable Grafana dashboards |
| `grafana-dashboard/screenshots/` | Dashboard screenshots (demo data) |
| `scripts/generate_truenas_dashboard.py` | Dashboard generator: queries, colours, shared rules |
| `grafana-dashboard/build_mission_control.py` | Mission Control builder |
| `scripts/validate_dashboard.py` | Dashboard structure and honesty checks |
| `scripts/validate.sh` | Local validation suite |
| `docs/api-exporter-parity.md`, `.json` | API/exporter audit |
| `docs/metrics-contract.json` | Machine-readable metric contract |
| `docs/modernization/README.md` | Reliability roadmap and evidence ledger |
| `tests/` | Tests |

</details>
