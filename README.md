<div align="center">

# 📊 TrueNAS Prometheus Exporter

### Turn your TrueNAS SCALE box into a beautiful, fully-monitored dashboard in minutes — safely, read-only, with zero changes to your NAS.

![TrueNAS SCALE 25.10.2 and 26.0.0](https://img.shields.io/badge/TrueNAS%20SCALE-25.10.2%20%2F%2026.0.0-0095d5?style=flat-square)
![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-3776ab?style=flat-square&logo=python&logoColor=white)
![Docker Ready](https://img.shields.io/badge/Docker-ready-2496ed?style=flat-square&logo=docker&logoColor=white)
![Read-only](https://img.shields.io/badge/access-100%25%20read--only-3fb950?style=flat-square)
![Metrics](https://img.shields.io/badge/metrics-400%2B-8957e5?style=flat-square)

**[⚡ Quick Start](#-quick-start-5-minutes)** • **[📈 Grafana Dashboards](#-see-it-in-grafana)** • **[⚙️ Configuration](#️-configuration)** • **[🩺 Troubleshooting](#-troubleshooting)**

</div>

![System overview and CPU and load dashboard](.github/images/System_overview_and_CPU_and_Load.png)

---

## ✨ Why you'll love it

- 🔒 **100% read-only, zero risk.** The exporter only ever calls documented read-only TrueNAS methods — it can never create, change, or delete anything on your NAS. Every method is checked against an allow-list *before* it ever hits the wire.
- 🚀 **Up and running in ~5 minutes.** Copy one file, paste two values, run one command. No plugins to install on TrueNAS, no config files to hand-write.
- 📊 **400+ metrics out of the box.** Pools, datasets, snapshots, disks & temperatures, ZFS ARC, CPU/RAM/network, SMB/NFS/iSCSI, apps & Docker, VMs, tasks, alerts, certificates, UPS, and more.
- 🎨 **Gorgeous Grafana dashboards included.** Two ready-to-import dashboards — import one JSON file and you have a full mission-control view of your NAS.
- 🧠 **Auto-detects your TrueNAS version.** Works on SCALE `25.10.x` and `26.0.x`, picking the right compatibility profile automatically. Nothing to configure.
- 🛡️ **Hardened by default.** Ships as a locked-down, read-only container (`cap_drop: ALL`, `no-new-privileges`) with conservative, low-cardinality defaults.

> [!NOTE]
> Honesty first: this exporter was built mostly with AI over a few weeks, running against a real home TrueNAS SCALE setup, and validated live against a real `25.10.3` system. It is strictly read-only and follows the official TrueNAS API docs.

---

## ⚡ Quick Start (5 minutes)

The easiest way to run it is **Docker Compose**. If you can copy/paste four commands, you can do this. 🙌

### Before you begin

You need:

- 🖥️ A **TrueNAS SCALE** system (version `25.10.x` or `26.0.x`) you can reach on your network.
- 🐳 A machine with **Docker + Docker Compose** (your NAS, a Raspberry Pi, a VM — anything on the same network).
- 🌐 The IP address or hostname of your TrueNAS (e.g. `192.168.1.50` or `truenas.local`).

---

### Step 1 — Create a read-only API key on TrueNAS 🔑

1. Open the **TrueNAS web UI** in your browser.
2. Click your **account menu in the top-right corner** and choose **API Keys**.
   *(Depending on your version this may live under **Settings ⚙ → API Keys** or **Credentials → Users**.)*
3. Click **Add**, give it a name like `prometheus-exporter`.
4. If your TrueNAS version supports **per-key roles**, attach it to an account with a **Read-only** role — extra peace of mind.
5. Click **Save** and **copy the key now** — TrueNAS shows it **only once**. 📋

> [!TIP]
> The exporter *never* issues anything but read-only calls, so it's safe even with a full-access key — but a read-only-scoped account is good defense-in-depth.

---

### Step 2 — Tell the exporter where your NAS is 📝

In a terminal, from this project folder:

```bash
cp .env.example .env
```

Now open `.env` in any text editor and set just **two** values:

```dotenv
# Your TrueNAS address with /api/current on the end.
# Use wss:// for an HTTPS box (recommended), or ws:// for plain HTTP.
TRUENAS_WS_URL=wss://192.168.1.50/api/current

# The read-only API key you copied in Step 1.
TRUENAS_API_KEY=1-your-long-api-key-here
```

That's it — everything else has sensible defaults.

> [!IMPORTANT]
> **Self-signed certificate?** Most home TrueNAS boxes use one by default. If the exporter can't connect over `wss://`, add this line to `.env` (fine on a trusted home LAN):
> ```dotenv
> TRUENAS_VERIFY_TLS=false
> ```
> For a production setup, instead trust your CA with `TRUENAS_CA_FILE=/path/to/ca.pem` and keep verification on.

---

### Step 3 — Start it 🚀

```bash
docker compose up -d --build
```

Docker builds and launches a small, hardened container named `truenas-exporter`.

---

### Step 4 — Confirm it works ✅

```bash
curl http://localhost:9108/healthz     # → ok
curl http://localhost:9108/metrics     # → lots of "truenas_..." metrics
```

If you see `truenas_up 1` in the metrics output — **🎉 you're done!** Your NAS is now exporting metrics.

<details>
<summary>👀 Prefer to run it without Compose? (plain Docker image or Python)</summary>

**Plain Docker image**

```bash
cp .env.example .env      # edit TRUENAS_WS_URL + TRUENAS_API_KEY
docker pull ghcr.io/unknowlars/truenas-scale-api-prometheus-exporter:latest
docker run --rm --env-file .env -p 9108:9108 \
  ghcr.io/unknowlars/truenas-scale-api-prometheus-exporter:latest
```

**Local Python (3.12+)**

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env       # edit TRUENAS_WS_URL + TRUENAS_API_KEY
python3 truenas_exporter.py
```

</details>

---

## 📈 See it in Grafana

This is the fun part. The repo ships **two ready-to-import dashboards** in [`grafana-dashboard/`](grafana-dashboard/) — no building required, just import a JSON file.

| Dashboard | File | Best for |
| --- | --- | --- |
| 🛰️ **TrueNAS · Mission Control** (tabbed flagship) | `truenas-mission-control.json` | The full experience — 12 tabs covering everything. **Grafana 13+** (schema v2). |
| 🗂️ **TrueNAS Operations Center** (classic rows) | `operations-center-dashboard.json` | Any recent Grafana version. |

**To import** (takes 20 seconds):

1. In Grafana, go to **Dashboards → New → Import**.
2. **Upload** one of the JSON files above.
3. Pick your **Prometheus data source** and click **Import**.

> First, make sure Prometheus (or Grafana Alloy) is scraping the exporter — see [Connect Prometheus](#-connect-prometheus) below.

### A peek at what you get

| System & CPU | Memory | Storage & Pools |
| --- | --- | --- |
| ![System overview and CPU and load dashboard](.github/images/System_overview_and_CPU_and_Load.png) | ![Memory dashboard](.github/images/Memory.png) | ![Storage and pools dashboard 1](.github/images/Storage_and_Pools_1.png) |

| Disks & Temperatures | ZFS ARC Cache | Network Interfaces |
| --- | --- | --- |
| ![Disks and temperatures dashboard](.github/images/Disks_Temperatures.png) | ![ZFS ARC cache dashboard](.github/images/ZFS_ARC_Cache.png) | ![Network interfaces dashboard](.github/images/Network_Interfaces.png) |

| Apps & Docker | Services & Shares | Virtualization |
| --- | --- | --- |
| ![Apps and Docker dashboard](.github/images/Apps_and_Docker.png) | ![Services and shares dashboard](.github/images/Services_Shares.png) | ![Virtualization dashboard](.github/images/Virtualization.png) |

<details>
<summary>🖼️ Show all dashboard tabs (13 more views)</summary>

| Storage Deep Dive | Dataset Deep Dive |
| --- | --- |
| ![Storage and pools dashboard 2](.github/images/Storage_and_Pools_2.png) | ![Dataset deep dive dashboard](.github/images/Dataset_Deep_Dive.png) |

| Apps & Docker (Details) | Alerts, Tasks & Updates |
| --- | --- |
| ![Apps and Docker details dashboard](.github/images/Apps_and_Docker_2.png) | ![Alerts, tasks, and updates dashboard](.github/images/Alerts_andTasks_andUpdates.png) |

| Audit & Directory Services | Security & Platform |
| --- | --- |
| ![Audit and directory services dashboard](.github/images/Audit_Directory_Services.png) | ![Security and platform dashboard](.github/images/Security_and_Platform.png) |

| System Configuration | Advanced Protocols (NVMe-oF, FC, HA) |
| --- | --- |
| ![System configuration dashboard](.github/images/System_Configuration.png) | ![Advanced protocols dashboard](.github/images/Advanced_Protocols_NVMe-oF_FC_HA.png) |

| Boot Environment | |
| --- | --- |
| ![Boot environment dashboard](.github/images/Boot_Environment.png) | |

</details>

<details>
<summary>⚙️ Advanced: rebuild / push the Mission Control dashboard</summary>

The Mission Control dashboard is generated code. Edit and re-run
`grafana-dashboard/build_mission_control.py` (needs only Python 3) rather than hand-editing the JSON. It harvests panel queries from the classic Operations Center dashboard, so query fixes should land there first.

Push it via the Grafana App Platform API:

```bash
curl -X POST -H "Authorization: Bearer $GRAFANA_SA_TOKEN" \
  -H "Content-Type: application/json" \
  --data-binary @grafana-dashboard/truenas-mission-control.json \
  "https://<grafana-host>/apis/dashboard.grafana.app/v2beta1/namespaces/default/dashboards"
```

To update an already-imported copy, delete the old dashboard and re-import the regenerated JSON (it keeps the same `metadata.name`/URL), or `PUT` it to
`/apis/dashboard.grafana.app/v2beta1/namespaces/default/dashboards/truenas-mission-control`.

</details>

---

## 🔌 Connect Prometheus

Point Prometheus at the exporter by adding a scrape job (or start from
[`deploy/prometheus/prometheus.truenas-example.yml`](deploy/prometheus/prometheus.truenas-example.yml)):

```yaml
scrape_configs:
  - job_name: truenas_exporter
    scrape_interval: 30s
    static_configs:
      - targets:
          - truenas-exporter:9108   # or the exporter host/IP, e.g. 192.168.1.60:9108
```

<details>
<summary>Using Grafana Alloy instead of a Prometheus scrape config?</summary>

```hcl
prometheus.scrape "truenasexporter" {
  targets = [{
    __address__ = "192.168.1.60:9108",
  }]
  forward_to = [prometheus.remote_write.local.receiver]
}
```

Replace the address with your exporter host/port, and point `forward_to` at your existing Alloy `prometheus.remote_write` component. The repo also includes `deploy/prometheus/docker-compose.prometheus.yml` and `deploy/prometheus/prometheus.yml` for local experiments — update the targets before using them.

</details>

---

## ⚙️ Configuration

Every option lives in [`.env.example`](.env.example) with inline comments. These are the ones most people touch:

| Variable | Required | Default | Description |
| --- | --- | --- | --- |
| `TRUENAS_WS_URL` | ✅ **yes** | — | TrueNAS WebSocket URL, e.g. `wss://192.168.1.50/api/current` |
| `TRUENAS_API_KEY` | ✅ **yes*** | — | Your read-only API key (*or use `TRUENAS_API_KEY_FILE`) |
| `TRUENAS_API_KEY_FILE` | no | — | Path to a mounted file containing the API key (for Docker/K8s secrets) |
| `TRUENAS_VERIFY_TLS` | no | `true` | Set `false` only for a trusted LAN with a self-signed cert |
| `TRUENAS_CA_FILE` | no | — | Path to a custom CA bundle for TLS verification |
| `EXPORTER_PORT` | no | `9108` | Port for `/metrics`, `/healthz`, `/readyz` |
| `SCRAPE_INTERVAL_SECONDS` | no | `30` | How often the exporter polls TrueNAS |
| `SCRAPE_BUDGET_SECONDS` | no | `25` | Hard deadline for one scrape |
| `LOG_LEVEL` | no | `INFO` | `DEBUG`, `INFO`, `WARNING`, or `ERROR` |
| `ENABLE_DATASET_METRICS` | no | `true` | Per-dataset space/quota metrics |
| `ENABLE_TASK_METRICS` | no | `true` | Replication / cloudsync / snapshot task metrics |
| `ENABLE_IPMI_METRICS` | no | `true` | IPMI chassis/sensor metrics when available |

> [!NOTE]
> The defaults are deliberately safe and low-cardinality. High-cardinality options (`ENABLE_GENERIC_METHOD_METRICS`, `ENABLE_GENERIC_EVENT_METRICS`, `AUTO_DISCOVER_METHODS`, `SCRAPE_ALL_METRICS`) are **off** by default and can never bypass the read-only method policy. See the [Advanced](#-advanced--how-it-works) section before enabling them.

---

## 📦 What you get

A quick tour of the coverage:

- **System** — identity, version, uptime, readiness, pending updates, reboot state.
- **Storage** — pools, datasets, snapshots, scrub schedules, resilver config, expansion progress, capacity, fragmentation, dedup.
- **Disks** — per-disk I/O rates, busy %, temperatures.
- **Memory & ZFS** — physical memory, ZFS ARC size, and ARC/L2ARC demand hit/miss rates.
- **Sharing & protocols** — SMB, NFS, iSCSI, NVMe-oF.
- **Workloads** — apps & Docker (incl. DockerHub pull limits), VMs, jobs, replication.
- **Health & governance** — alerts, certificates, directory-service health, audit retention, NTP, UPS, security posture.
- **Exporter self-health** — API call failures, collector error counters, scrape duration.

---

## 🩺 Troubleshooting

| Symptom | Fix |
| --- | --- |
| ❌ Connection / TLS error over `wss://` | Self-signed cert? Set `TRUENAS_VERIFY_TLS=false` (trusted LAN) or point `TRUENAS_CA_FILE` at your CA. |
| ❌ Auth fails / `truenas_up 0` | Re-check `TRUENAS_API_KEY`; make sure the URL ends in **`/api/current`**. |
| ❌ Container won't start | `docker compose logs -f truenas-exporter` shows the reason (usually a `.env` typo). |
| ⚠️ Some metrics are missing | Many collectors only emit when that TrueNAS service/subsystem is enabled — that's normal, not a fault. |
| ⚠️ Metrics flicker to `NaN` in Grafana | Realtime series update between event ticks; filter them, e.g. `avg((truenas_cpu_user_percent >= 0))`. The Mission Control dashboard already does this. |

**Health endpoints:**
- `GET /healthz` — the process is serving HTTP (does *not* mean the last scrape succeeded).
- `GET /readyz` — returns `200` only after a recent successful scrape, otherwise `503`.

Still stuck? [Open an issue](https://github.com/Unknowlars/truenas-scale-api-prometheus-exporter/issues) with your TrueNAS version, the relevant config toggles, and the metric/API response you expected.

---

## 🧪 Testing & contributing

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements-dev.txt
./scripts/validate.sh
```

`validate.sh` runs linting, static typing, branch-covered tests, generated-asset checks, Compose validation, and a container build. Set `RUN_PYTHON_MATRIX=1` to test Python 3.12 / 3.13 / 3.14 in local containers. No hosted CI is used by design.

Repository: [`github.com/Unknowlars/truenas-scale-api-prometheus-exporter`](https://github.com/Unknowlars/truenas-scale-api-prometheus-exporter)

---

## 🔬 Advanced — how it works

<details>
<summary><b>Runtime modes</b> (<code>EXPORTER_MODE</code>)</summary>

<br>

- **`collector`** (default): a background single-flight scrape publishes complete, atomic snapshots; `/metrics` serves a cached in-memory snapshot (~10 ms) and never blocks on TrueNAS. This prevents torn reads and keeps health/readiness responsive even when the NAS is slow.
- **`legacy`**: the previous global-registry coordinator, retained for the 5.2 release.

`truenas_scrape_duration_seconds` measures the *background* collection cycle (often 15–20 s), **not** HTTP latency — short Prometheus scrape timeouts are fine.

</details>

<details>
<summary><b>Automatic version detection & compatibility profiles</b></summary>

<br>

On every connection the exporter authenticates, calls `system.version_short` once, and selects a profile **before** any collector call, discovery, or event subscription:

| Detected version | Profile | Behavior |
| --- | --- | --- |
| `25.10.*` | `25.10` | Uses the pinned 25.10.2 audited method/event surface. |
| `26.0.*` | `26.0` | Uses the pinned 26.0.0 surface; suppresses sources removed in v26. |
| anything else / malformed / detection failure | `unknown` | Fails closed to the reviewed common intersection only. |

Failed detection never *expands* API access, and there is no manual version knob. Sources removed in v26 (`virt.instance.query`, `virt.volume.query`, `nvmet.global.sessions`, `reporting.graphs`, `reporting.netdata_graphs`, `virt.instance.metrics`) are suppressed before transport under `26.0`/`unknown`.

Default event subscriptions are profile-aware:

| Profile | Default event subscriptions |
| --- | --- |
| `25.10` | `reporting.realtime`, `app.stats`, `virt.instance.metrics` |
| `26.0` / `unknown` | `reporting.realtime`, `app.stats` |

</details>

<details>
<summary><b>Safety model & API parity</b></summary>

<br>

- **Read-only, enforced pre-transport.** Every method is checked against a documentation-derived allow-list and a mutating-verb deny-list *before* the WebSocket call. `AUTO_DISCOVER_METHODS`, `SCRAPE_ALL_METRICS`, and `EXTRA_METHODS` cannot bypass this policy.
- **No fabricated data.** When a metric has no safe source in the active profile, or a response is denied/absent/malformed/stale, the series is left **absent or `NaN`** — never a fake `0`.
- **Secrets suppressed.** Values under password, token, secret, private-key, and credential paths are never emitted, even with generic extraction enabled.
- **Audited, not sampled.** The committed API snapshot inventories 767 methods across 114 namespaces and 63 event sources — see [`docs/api-exporter-parity.md`](docs/api-exporter-parity.md). The pinned 25.10.2/26.0.0 diff is in [`docs/truenas-25-10-2-and-26-0-0-compatibility/`](docs/truenas-25-10-2-and-26-0-0-compatibility/), and the reliability roadmap in [`docs/modernization/README.md`](docs/modernization/README.md).

Existing metric names, types, help text, and label sets are preserved across profiles and releases; replacements ship as compatibility aliases with documented deprecations.

</details>

<details>
<summary><b>Cardinality & series impact</b></summary>

<br>

| Option | Default | Impact |
| --- | --- | --- |
| `ENABLE_GENERIC_METHOD_METRICS` | `false` | **High** — `METHOD_*` series with `[method, path]` labels; 50k–500k+ with discovery. |
| `ENABLE_GENERIC_EVENT_METRICS` | `false` | **High** — `EVENT_*` series with `[event, path]` labels. |
| `AUTO_DISCOVER_METHODS` | `false` | **High** — feeds safe, non-sensitive telemetry candidates through generic extraction. |
| `SCRAPE_ALL_METRICS` | `false` | **High** — adds reviewed telemetry candidates beyond the base set. |
| `DATASET_SNAPSHOT_FALLBACK_LIMIT` | `0` | **Medium** — up to N extra API calls per scrape for per-dataset snapshot counts. |
| `ENABLE_FILESYSTEM_LISTDIR` | `false` | **Medium** — per-path directory-listing metrics. |
| `ENABLE_DATASET_METRICS` | `true` | **Low–Medium** — one gauge set per dataset. |
| `ENABLE_TASK_METRICS` | `true` | **Low** — one set per configured task. |
| `ENABLE_IPMI_METRICS` | `true` | **Low** — fixed IPMI sensor set. |

When enabling high-cardinality options, watch `prometheus_tsdb_head_series` and plan TSDB storage. Start with the defaults; enable generic extraction only for bounded debugging.

</details>

<details>
<summary><b>Included files</b></summary>

<br>

| Path | Purpose |
| --- | --- |
| `truenas_exporter.py` | Source-checkout compatibility launcher |
| `src/truenas_exporter/` | Exporter package implementation |
| `Dockerfile` / `docker-compose.yml` | Container image build & deployment |
| `.env.example` | Example environment configuration |
| `deploy/prometheus/` | Example Prometheus scrape configs & compose |
| `grafana-dashboard/*.json` | Importable Grafana dashboards |
| `grafana-dashboard/build_mission_control.py` | Mission Control dashboard builder |
| `scripts/generate_truenas_dashboard.py` | Dashboard generator source |
| `scripts/validate.sh` | Full local validation suite |
| `docs/api-exporter-parity.md` / `.json` | Human- & machine-readable API/exporter audit |
| `docs/metrics-contract.json` | Machine-readable Prometheus metric contract |
| `docs/modernization/README.md` | Reliability & architecture roadmap |
| `tests/` | Unit tests for collector and event behavior |

</details>

---

<div align="center">

**Made for the TrueNAS community.** ⭐ If this helped you, consider starring the repo!

</div>
