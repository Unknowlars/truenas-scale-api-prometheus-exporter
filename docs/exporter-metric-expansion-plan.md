# Exporter Metric Expansion Plan

This document tracks the next round of dedicated Prometheus metrics to add to
the TrueNAS exporter after comparing `truenas_exporter.py` against
`docs/truenas-api`.

## Goals

- add high-signal operational metrics that already exist in the TrueNAS API
- prefer low-cardinality rollups over per-object labels with unstable values
- use exact `count` queries where the API supports them
- keep dedicated metrics readable even when generic `truenas_method_*` metrics
  already expose the raw fields

## Priorities

### Phase 1 - In Progress

Focus on the biggest monitoring gaps that already have stable read-only API
coverage and low-cardinality shapes.

1. `core.get_jobs`
   - active job counts by state and method
   - abortable and transient active job counts
   - oldest active job timestamps
   - running job progress by method
2. `alert.list`
   - counts by source, class, and node
   - dismissed and one-shot rollups
   - oldest alert and last-occurrence timestamps
3. `app.query`
   - upgrade availability
   - image update availability
   - custom-app and migrated flags
   - active workload container and exposure counts
   - per-app container state counts
4. `pool.dataset.query`
   - reservation and used-by breakdowns
   - key-loaded and locked state for encrypted datasets
   - readonly / atime / exec flags
   - quota warning / critical thresholds
   - dataset creation timestamps
5. Existing declared-but-underfilled metrics
   - populate scrub task state and last-run timestamp

### Phase 2 - Next

1. richer replication, cloud sync, cloud backup, and rsync task posture metrics
2. per-VM config metrics from `vm.query`
3. richer Incus/LXD inventory from `virt.instance.query`
4. negotiated network interface media and queue metrics from `interface.query`

### Phase 3 - Candidate Additions

1. API key inventory and expiry posture from `api_key.query`
2. additional app exposure and workload inventory if cardinality stays small
3. dataset policy rollups such as ACL mode, compression, checksum, and sync

## Implementation Rules

- Do not add labels from free-form fields like alert text, exception text, job
  description, or URLs.
- Prefer bounded labels like `state`, `method`, `klass`, `source`, and `node`.
- For query methods, request only the fields needed with `select`.
- For counters that can disappear between scrapes, use Gauges with fresh values
  per scrape rather than exporter-lifetime Counters.
- Keep the default scrape safe on larger systems; only request larger result sets
  when exact rollups need them.

## Source Docs Used

- `docs/truenas-api/events/core/get_jobs.md`
- `docs/truenas-api/events/alert/list.md`
- `docs/truenas-api/events/app/query.md`
- `docs/truenas-api/events/pool/dataset/query.md`
- `docs/truenas-api/events/pool/scrub/query.md`
- `docs/truenas-api/shared/query_methods.md`

## Progress Notes

- This plan starts with dedicated metrics that provide immediate dashboard and
  alerting value without relying on high-cardinality identity labels.
- Future phases should extend the Grafana dashboard after each metric batch is
  merged and validated against a live TrueNAS system.
