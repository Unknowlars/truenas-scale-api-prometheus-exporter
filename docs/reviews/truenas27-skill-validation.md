# Repository skill independent forward test

Evaluated 2026-10-19 against source HEAD `523686d` and the working-tree skill at
`.agents/skills/truenas-prometheus-exporter/SKILL.md`. The evaluator received
three realistic requests, the skill location, resource boundaries, and an output
path. No intended answers, suspected defects, or proposed application fixes were
provided. This is a constrained behavioral walkthrough with focused existing
tests and one synthetic experiment, not three implemented application changes.

The evaluation used the skill-creator independent forward-testing workflow.
Only this report was written intentionally. No NAS, credential file, production
payload, external service, publication, commit, or application edit was used.

## Request 1: add a useful storage pool capacity metric

**Observed outcome:** the skill's instruction to inspect existing metrics avoids
duplicating `truenas_pool_size_bytes`, `truenas_pool_allocated_bytes`, and
`truenas_pool_free_bytes`. They already have gauge type and the existing `pool`
label. A capacity-used view can already use
`100 * truenas_pool_allocated_bytes / truenas_pool_size_bytes`, with explicit
handling for missing or zero-size pools. No extra API request is justified for
these values.

For a genuinely additive capacity-related metric, the inspected snapshots
document `pool.query.freeing`: bytes currently being freed by ongoing operations.
Both 27 snapshots describe integer-or-null bytes, and the historical 25.10/26.0
pages document the same field. This differs from immediately available `free`
and from an operation throughput. It is absent from current metric declarations
and runtime consumption. A reasonable concrete implementation would:

1. Declare `truenas_pool_freeing_bytes` as a gauge in
   `src/truenas_exporter/metrics.py`, HELP describing bytes being freed, with
   only the existing `pool` label. Do not rename existing capacity families.
2. Extend the existing selected `pool.query` response and pool parsing in
   `src/truenas_exporter/runtime.py`; use `freeing`, not `freeing_str`. Retain
   `_call_query_with_fallback`, source isolation, query limit and scrape budget.
   Clear the new labelled gauge in `_reset_poll_metrics` so removed pools and
   failed subsequent observations cannot retain old values.
3. Add synthetic collection/exposition assertions near
   `tests/test_runtime_api_parity.py::test_main_scrape_uses_documented_params_units_and_nested_shapes`.
   Cover positive bytes, valid zero, null, omitted/malformed fields, removed
   pools, and source failures. Assert no extra pool RPC and unchanged old metric
   metadata. Use the existing parser unless evidence requires a focused change.
4. Extend the existing explicit API/metric mapping in
   `scripts/generate_api_exporter_parity.py`, regenerate metric contracts,
   dashboard sources only if a panel is requested, API parity and 27 inventory;
   run the repository validation gate and record its actual result.

**Unsupported assumptions rejected:** a new API call is needed; pool capacity
is a counter; space being freed is already available; null means zero; local and
official snapshots are identical; documentation proves live schema acceptance.
The additive metric is an implementation proposal, not an implemented/tested new
family or a live claim.

**Skill assessment:** sufficient. Collectors guidance supplies the exact
decision criteria, owned files, source reuse, null semantics and unit distinction.
The caller still has to inspect raw schemas and current code, as intended.

## Request 2: an Incus method is absent on TrueNAS 27

**Observed outcome:** inspect the reported exact method, version selection and
both pinned 27 pages/manifests before replacing anything. Current
`src/truenas_exporter/compat_profiles.py` already contains an explicit `27.0`
profile which removes `virt.instance.query` and other historical reads before
transport. 25.10 retains its historical methods. Unknown versions select the
conservative common profile.

For instance inventory, existing `_collect_virt_metrics` in
`src/truenas_exporter/runtime.py` chooses reviewed `container.query` on profiles
that permit it. It requests only `name` and `status`, with query/entity limits;
`initenv` and other sensitive configuration are not fetched. The parser handles
`status.state` for containers and historical flat status/type for 25.10. Existing
metric declarations remain stable. There is no documented equivalent volume
inventory here, so historical volume metrics remain absent/NaN rather than zero.

An actual missing-method fix would be confined to the exact profile/catalog,
producer and relevant event ownership in `events.py`; changing every `virt.*`
prefix would be incorrect. Both current event sources and current subscriptions
need review. `docs/api/truenas-27/events/container/metrics.md` documents the
`CONTAINER_READ` role and interval parameter, but its broad object-valued fields
do not establish old Incus CPU/memory semantics. Use the pinned middleware source
or bounded authorized evidence before adding a new parser for opaque fields.

Regression work belongs in `tests/test_truenas27.py` and
`tests/test_removed_source_suppression.py`: assert removed reads do not reach a
recording transport through direct calls, discovery, extras, counts or events;
retain 25.10 calls/subscriptions; verify selected container fields, nested status,
unsupported metrics and unknown-version behavior. Regenerate compatibility
evidence, preserve 25/26 snapshots, and run `./scripts/validate.sh`.

**Unsupported assumptions rejected:** missing method means permission error;
requesting a write role repairs monitoring; all Incus telemetry has a renamed
container equivalent; configured CPU/memory equals usage; profile source tests
prove live 27 support. Current code already addresses the core reported example,
so a fresh report must be reproduced rather than patched speculatively.

**Skill assessment:** sufficient. It directed pre-transport suppression,
historical compatibility, selected responses, event review, semantic equivalence
and absent-data preservation without supplying a canned rename.

## Request 3: discovery causes unexpectedly huge generic time-series growth

**Observed outcome:** inspect the metric family and label dimensions first.
`truenas_method_*` combines method and JSON path, with status as another dimension;
`truenas_event_*` similarly combines event/path/status. Wide dictionaries and
dynamic keys can create many paths despite short list and recursion limits.

Current `config.py` defaults both generic flags to false and
`MAX_GENERIC_SERIES=10000`. `runtime.py` enforces this separately for polling and
the combined retained event set. Inspect `truenas_generic_series{source="method"}`
and `{source="event"}`, plus `truenas_generic_series_limit_hits_total`; the source
label has only those two values. Limit hits count pruned branches, not every
possible descendant. The existing declaration contracts must be preserved.

A practical first response is to disable the applicable generic flag, reduce
discovery breadth, or narrow reviewed method selection via existing configuration
(`EXTRA_METHODS`/`EXCLUDE_METHODS`, call/entity/list/depth/series limits). Keep
dedicated metrics and read-only policy intact. Merely reducing `MAX_LIST_ITEMS`
will not bound dictionary width or temporal key churn. If a reproducer still
exceeds the configured current-series cap, fix the existing extractor/reset/event
replacement paths, rather than introduce another collector framework.

The synthetic changing-key experiment reproduced three snapshots of three
current samples each under a limit of three, but nine distinct label sets across
those snapshots. Thus the instantaneous exporter cap does not bound cumulative
TSDB series identities over time. Diagnose changing paths/status labels and
Prometheus retention as well as current exposition. No Prometheus server was
contacted; the experiment establishes label identity churn, not a measured TSDB
memory or storage impact. Disabling extraction does not erase retained history.

For implementation changes, regression cases belong near the generic tests in
`tests/test_truenas27.py` and `tests/test_runtime_api_parity.py`: wide dictionaries,
changing keys across cycles, total budgets shared by retained events, reset and
staleness, zero/false/null, and sensitive paths. Assert samples through
`TrueNASCollector.collect()` without exposing any real labels. Run the full gate
after any fix and record exact evidence.

**Unsupported assumptions rejected:** discovery alone proves generic extraction
is enabled; list depth bounds all cardinality; the cap covers historical TSDB
identity growth; generic count gauges prove all data is retained; failures or
pruning should become zero; production payloads should be stored as fixtures.

**Skill assessment:** sufficient for the immediate safe diagnosis and mitigation.
A narrow improvement would explicitly say that current-series budgets do not
bound TSDB churn across scrapes. Its existing instruction to test changing keys
already led to this experiment; the additional sentence would prevent a false
claim that the current cap resolves every growth report.

## Executed verification

Environment: Python `3.12.3`, pytest `8.4.2`. Commands below completed locally.

- `python3 <local-path> .agents/skills/truenas-prometheus-exporter`:
  PASS, `Skill is valid!`.
- The same validator against `.claude/skills/truenas-prometheus-exporter`:
  PASS, `Skill is valid!`.
- A Python `pathlib`/Markdown-link check over both skill directories resolved
  all **4** file links: the three canonical references and the Claude bridge.
  Supporting references resolve relative to the canonical file as instructed.
- Focused pytest selection over `tests/test_truenas27.py`,
  `tests/test_removed_source_suppression.py` and
  `tests/test_documented_api_shapes.py`, selecting
  `pool_dataset_and_disk or removed_methods or v25_still_transports or v26_virt or v25_still_subscribes or removed_virt_event or subscribes_container or unknown_virt or explicit_27 or generic_wide or generic_events`:
  **18 passed, 44 deselected** in 0.41s.
- `python3 -m pytest -q tests/test_runtime_api_parity.py::test_main_scrape_uses_documented_params_units_and_nested_shapes tests/test_runtime_api_parity.py::test_generic_secret_paths_method_safety_and_poll_reset tests/test_runtime_api_parity.py::test_profile_gate_filters_extra_discovered_reporting_and_count_queries tests/test_api_catalog.py::test_generic_telemetry_candidates_are_a_conservative_read_subset`:
  **4 passed** in 0.69s.
- An inline synthetic Python experiment used `make_config` from `tests/conftest.py`,
  `max_generic_series=3`, `_reset_poll_metrics`, `_extract_generic_metrics`,
  `_publish_metric_snapshot`, and public `TrueNASCollector.collect`. Three cycles
  provided six distinct synthetic numeric dictionary keys each. Assertions
  passed: current sample counts `[3, 3, 3]`, union **9** distinct label sets.
- `git -c safe.directory=<repository-path> rev-parse --short HEAD`:
  `523686d`. The first plain Git status attempt failed on checkout ownership;
  no global Git setting was changed. Two early exploratory reads guessed test
  filenames or a dotted event filename that do not exist; subsequent checks used
  actual discovered paths. These were inspection errors, not test failures.

The full `./scripts/validate.sh` gate was not run by this evaluator; the owning
agent must record its own result separately. No live NAS, browser, PromQL engine,
container, publication or authentication acceptance is established here. Historical
baseline/architecture reports were treated as dated evidence, not present-day
test results. Syntax validation proves packaging structure only; the scenarios
and assertions above supply the behavioral evidence.
