# Adding or replacing telemetry

1. Read the exact method/event page in docs/api/truenas-27 and compare
   docs/api/truenas-27-official. Both identify27.0.0 but disagree materially.
   Inspect parameters, types, units, optionality, roles and source hashes.
   Use release-pinned middleware source when schemas are opaque. Do not invent
   fields or equate documentation presence with live success.
2. Establish read-only semantics and least-privilege access before live calls.
   Do not grant write roles to obtain monitoring data. Never invoke configuration,
   storage, scrub, SMART-test, replication-run or service-control actions.
   Authentication and subscribe/unsubscribe are narrowly reviewed transport
   operations, not blanket permission for other session actions.
3. Prefer an already fetched response. Preserve select projections, list/entity
   limits, total deadlines and expensive-query cadence. Full disk.query responses
   contain credential-bearing fields: keep strict select and generic exclusions.
   Errors and malformed objects must never become empty inventories.
4. Check existing metrics before adding duplicates. Pool capacity is a byte
   gauge; throughput is a bytes/second gauge. Source cumulative values may reset;
   do not increment client counters from each observed total. Select exact
   documented fields and bounded existing entity labels.
5. Declare metrics in src/truenas_exporter/metrics.py, extend existing parsers and
   explicit compatibility policy, and use _call for safety/diagnostics.
   Independent required domains use _source_scope; transport/deadline failures
   must escape. Query fallback is only for documented invalid parameters.
6. For events update events.py ownership and reviewed subscriptions together.
   Require valid string subscription IDs and clean up only acquired IDs. Retain
   interval syntax, aliases, reconnection, payload validation and snapshot TTL.
   Both disls and disks input spellings are intentional compatibility.
7. For removed methods suppress calls before transport in the27 profile and
   preserve earlier profiles and metric declarations. Document absence unless a
   semantically equivalent reviewed replacement exists. Do not rename virt.* to
   container.* blindly; container.metrics is broadly typed and does not prove
   that old virtual telemetry has an equivalent source.

Use docs/reviews/truenas27-api-compatibility.md and its machine inventory to
update mappings. Regenerate using each snapshot README and pinned checksums;
extend the existing converter, never a second scraper. Preserve25/26 snapshots.
Embedded HTML schemas are source material, not recovered canonical JSON Schema.
