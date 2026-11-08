# Diagnosis and cardinality

Distinguish /healthz (HTTP process), /readyz (recent successful polling), truenas_up,
scrape duration/age, API/collector errors, event stream state and message age.
A healthy HTTP process does not prove NAS connectivity or fresh event values.

TRUENAS_USERNAME selects auth.login_ex with API_KEY_PLAIN and explicit SUCCESS.
Without a username the legacy key-only mechanism remains available. Never infer
success from a nonempty response object. Prefer TLS and protected key files;
the root api file is a local secret, never a project artifact to stage.

Trace missing telemetry through declaration, producer, profile permission,
actual field, snapshot freshness and PromQL. Distinguish absent methods,
permission errors, unsupported options, malformed data, stale events and
exhausted budgets. Never replace these conditions with plausible zeroes. Use
bounded type/count/status summaries, not real labels, arguments or payloads.

For high cardinality inspect the family and labels before proposing changes.
Generic families combine method/event with JSON paths; status is another
label dimension. Dynamic object keys can explode even with short lists.

Generic extraction is off by default. MAX_GENERIC_SERIES defaults to10000
separately for polling and the combined retained event set. Inspect
truenas_generic_series and truenas_generic_series_limit_hits_total; their source
label is limited to method/event. Limit hits count pruned branches, not every
possible descendant sample. Reduce/disable generic extraction, narrow reviewed
method selection and apply entity/list/depth limits. Test wide dictionaries and
changing keys, not only lists.

Never add usernames, UUIDs, paths, command lines, alert text, arguments or
arbitrary strings as new labels. Preserve contractual labels while documenting
any necessary migration. Use the diagnosing-bugs skill when installed: reproduce
through the real interface, test falsifiable hypotheses and preserve a regression.

Known 27.0.0-RC.1 shapes (live, 2026-11-07), so do not chase them as exporter bugs:
- `reporting.realtime` has no CPU user/system split (NaN), aggregate disk I/O
  (`disk="total"`) only, and pool capacity but no pool read/write rates.
- `virt.instance.metrics` is suppressed by the 27.0 profile
  (`container.metrics` replaces it), yet its `event_stream_up` series stays at 0.
- `pool.dataset.query` as currently projected returns no
  encrypted/key_loaded/locked fields.
- Alert, cron and snapshot-task `name` labels are numeric IDs.
- Data age from `last_scrape_timestamp` is normally 25–60 s with 30 s polling.
