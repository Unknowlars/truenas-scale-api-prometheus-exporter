# Persona Mapping — Metric Analysis & Targeted Dashboard Design

This reference defines how to analyse available metrics, map them to audience
personas, and produce a focused dashboard plan before writing any JSON.

---

## Why persona-first matters

A dashboard that serves everyone serves no one well. When all available metrics
land in a single dashboard, operators can't find the signal during an incident,
developers lose the application-level context they need, and managers see noise
instead of SLO health. Persona-first design constrains scope intentionally.

**Rule: propose a dashboard plan and confirm the audience before building.**

---

## Phase 0 workflow

```
1. Collect metric inventory          — list every metric / field / log stream
2. Classify by signal category       — infrastructure, application, SLO, etc.
3. Map categories to personas        — who cares, and why
4. Propose a focused dashboard set   — one dashboard per audience
5. Confirm with user which to build  — build one at a time
```

Never skip step 5. Do not output dashboard JSON until the user has confirmed
the target audience and scope.

---

## Step 1 — Metric inventory

When given raw Prometheus metrics, a scrape output, a dashboard JSON, or a
description of available metrics, produce a structured inventory table:

| Metric / field | Category | Signal type | Example labels |
|---|---|---|---|
| `http_requests_total` | Application | Counter | `method`, `status`, `handler` |
| `process_resident_memory_bytes` | Infrastructure | Gauge | `job`, `instance` |
| `go_gc_duration_seconds` | Runtime | Summary | `quantile` |
| `pg_stat_activity_count` | Database | Gauge | `state`, `datname` |

Group by category before mapping. Categories:

| Category | Description | Common metric names |
|---|---|---|
| **Infrastructure / System** | Host-level resources | CPU, memory, disk I/O, network I/O, filesystem |
| **Application / Service** | Service behaviour | Request rate, error rate, latency histograms, active connections |
| **Runtime** | Language/process internals | GC, goroutines, threads, heap, class loading |
| **Database / Storage** | DB + object storage health | Query time, connections, cache hit ratio, replication lag |
| **Queue / Pipeline** | Async workloads | Queue depth, consumer lag, processing rate, DLQ size |
| **SLO / Business** | Reliability commitments | Availability %, error budget, throughput, SLA breach indicator |
| **Collector / Agent** | Observability pipeline health | Scrape duration, dropped samples, Alloy components |
| **Security / Audit** | Auth and access | Auth failures, cert expiry, RBAC violations |

---

## Step 2 — Persona definitions

### OPS / SRE — On-call incident responder

**Job to be done:** Detect, triage, contain. Answer in under 30 seconds:
- Is the service degraded?
- What is the blast radius?
- When did it start and is it getting worse?

**What they need:**
- RED overview: rate, error rate, latency p95/p99
- USE infrastructure: CPU/memory/disk/network utilisation and saturation
- Error budget or SLO status at a glance
- Annotation markers for deployments and config changes
- Drill-down links to the developer dashboard and log/trace explorers
- Alert context: what alert fired, what threshold, when

**Panel budget:** 15–25 panels. Tabs or rows mandatory above 12 panels.
**Suggested tab groups:** Overview · Traffic · Errors · Latency · Resources · Dependencies · Logs

**Anti-patterns to avoid:**
- Raw log tables at the top
- High-cardinality dropdowns (per-pod, per-request)
- Panels without thresholds
- Averages without percentiles for latency

---

### Developer / Engineer — Service owner debugging their code

**Job to be done:** Understand if their code is behaving correctly, diagnose
a regression, or assess a deployment impact.

**What they need:**
- Service-scoped RED: broken down by endpoint/handler/operation
- Error details: error type, status code distribution, stack-trace excerpt from logs
- Latency by operation: p50/p95/p99 with histogram breakdown
- Deployment markers (annotations) aligned to latency/error trends
- Trace links: exemplars or data links into Tempo
- Log correlation: filtered to service + time window

**Panel budget:** 10–18 panels. One tab per major concern area.
**Suggested tab groups:** Overview · Endpoints · Errors · Latency · Traces · Logs

**Anti-patterns to avoid:**
- Infrastructure panels (CPU/memory) that belong in the OPS dashboard
- Global error rates without service scoping
- Missing exemplar configuration on histogram panels

---

### General / Management — Team lead, product owner, stakeholder

**Job to be done:** Confirm the system is meeting its commitments. No jargon.

**What they need:**
- Availability percentage over the reporting period
- SLO status: passing / at risk / breached
- Error budget remaining or burn rate (simple %)
- Throughput trend (requests/day or transactions/hour)
- Top-level health: single green/yellow/red status panel per service

**Panel budget:** 4–8 panels max. No rows or tabs. Should fit one screen.
**Layout:** Stat panels top row → single time-series trend → optional table of services

**Anti-patterns to avoid:**
- Any panel showing raw system metrics
- High-frequency refresh (every 5s is noise; 5m is fine)
- Dropdowns for instance/pod selection — management sees aggregate

---

## Step 3 — Persona relevance mapping

After classifying metrics by category, map each category to the personas it serves.

| Metric category | OPS / SRE | Developer | General |
|---|---|---|---|
| Infrastructure / System | ✅ Primary | 🔶 Secondary (resource impact) | ❌ Not useful |
| Application / Service | ✅ Primary | ✅ Primary | 🔶 Aggregates only |
| Runtime | 🔶 Secondary | ✅ Primary | ❌ Not useful |
| Database / Storage | ✅ Primary | ✅ Primary | ❌ Not useful |
| Queue / Pipeline | ✅ Primary | ✅ Primary | 🔶 Throughput only |
| SLO / Business | 🔶 Secondary | 🔶 Secondary | ✅ Primary |
| Collector / Agent | ✅ Primary | ❌ Not useful | ❌ Not useful |
| Security / Audit | ✅ Primary | ❌ Not useful | 🔶 Breach indicator |

**Legend:** ✅ Primary — include as main panels. 🔶 Secondary — include 1–2 summary panels max. ❌ Not useful — omit.

---

## Step 4 — Dashboard plan output format

When Phase 0 is complete, present a structured plan in the conversation (no JSON yet).

```
## 📊 Metric Analysis — Dashboard Plan

### Metric Inventory (N metrics found)

| Category            | Metrics                              | Personas         |
|---------------------|--------------------------------------|------------------|
| Application/Service | http_requests_total, latency_bucket  | OPS, Dev         |
| Infrastructure      | cpu_usage, memory_bytes, disk_io     | OPS              |
| Database            | pg_query_duration, pg_connections    | OPS, Dev         |
| SLO/Business        | availability_ratio, error_budget     | General          |

---

### Proposed Dashboard Set

| # | Dashboard title              | Audience    | Panel count | Focus                                    |
|---|------------------------------|-------------|-------------|------------------------------------------|
| 1 | [Service] Overview           | All         | 6           | 30-second health check — is it healthy?  |
| 2 | [Service] Operations         | OPS / SRE   | 18          | Incident triage — RED+USE+errors+logs    |
| 3 | [Service] Developer          | Engineers   | 14          | Endpoint detail, traces, error breakdown |
| 4 | [Service] SLO Report         | Management  | 6           | Availability, error budget, throughput   |

---

> **Which dashboard should I build first?**
> If you want all four, I can build them one at a time, starting with the Overview.
> Let me know if any dashboard should be skipped or if a different scope is needed.
```

Always offer to build one at a time. Never output all dashboards in one response
unless the user explicitly asks for all of them.

---

## Step 5 — Single-dashboard scoping rules

Once the user confirms an audience, apply these constraints before writing JSON:

### Panel budget by audience

| Audience | Max panels | Tab/row grouping required at |
|---|---|---|
| General / Overview | 8 | Not required |
| OPS / SRE | 25 | Above 12 panels |
| Developer | 18 | Above 10 panels |
| Collector / Platform | 20 | Above 12 panels |

### Variable scoping by audience

| Audience | Variables to include | Variables to exclude |
|---|---|---|
| General | datasource, time range only | Everything else |
| OPS | datasource, cluster, namespace, service/job | pod, instance (use in sub-rows) |
| Developer | datasource, cluster, namespace, service, endpoint/handler | pod, container (except in trace panels) |

### Metric selection rules per audience

**General dashboard:**
- Aggregate only: availability %, error rate %, request volume.
- Max 2 time-series panels; rest are stat/gauge panels.
- No drill-down links needed (link to OPS dashboard instead).

**OPS dashboard:**
- RED overview first (rate, errors, latency p99) — stat row + trend panels.
- USE for each infrastructure resource type — timeseries per resource group.
- Annotations: deployments, alerts, scaling events.
- Dashboard links to Developer dashboard and Explore/Logs/Traces.

**Developer dashboard:**
- Service-scoped RED broken by handler/operation.
- Error detail table: status code or exception type, rate, example.
- Latency histogram panel with exemplars where Tempo is configured.
- Log panel scoped to service + error level.
- Data links on histogram to Tempo trace search.

---

## Recognising when Phase 0 should trigger

Trigger Phase 0 when:
- User provides raw Prometheus metrics output (`# HELP`, `# TYPE`, metric lines).
- User provides an existing dashboard and asks to "improve it", "redesign it",
  or "make it better".
- User asks to "build a dashboard for X" without specifying audience.
- User provides a list of metric names and asks what they can build from them.
- User says "I have these metrics, what dashboards can I make?"

Do NOT trigger Phase 0 when:
- User asks to add a specific panel to an existing dashboard (they know what they want).
- User asks to fix a query or a transformation (surgical task, not design).
- User specifies the exact audience and panels they want.
- User says "just build it" after already seeing a plan.

---

## Progressive build order

When building a dashboard set, suggest this order:

1. **Overview** — validates that metrics are queryable; gives user something to import quickly.
2. **OPS** — most frequently used; covers the common on-call case.
3. **Developer** — adds endpoint/trace detail; builds on top of OPS variable naming.
4. **General/SLO** — derived from simpler aggregates; easiest to build last.

Link dashboards to each other using dashboard links that pass time range and variables.

---

## Dashboard link conventions

When building a set, add cross-dashboard links at the top of each dashboard:

- Overview → links to OPS and Developer dashboards.
- OPS → links to Developer, Explore (Loki), Explore (Tempo).
- Developer → links to OPS, Explore (Tempo), Explore (Loki).
- General → links to OPS dashboard (for drill-down, if permitted).

Link format preserves: `$datasource`, `$cluster`, `$namespace`, `$service`, time range.
