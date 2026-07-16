# 02 — Runtime Profiles and Safety Plan

## Goal

Make API version differences explicit and centralized so collectors cannot
accidentally call a removed method or interpret a value with the wrong unit.

## Profile interface

Add a typed compatibility profile abstraction, with equivalent names chosen by
the implementer only if behavior is unchanged. It must expose:

- `family`: `25.10`, `26.0`, or `unknown`;
- normalized detected version;
- approved read-only methods;
- approved event subscriptions;
- removed/blocked methods and events;
- query limit constraints;
- unit conversions;
- field aliases/normalizer selection;
- unavailable metric/source declarations.

The profile is policy data, not a collection of scattered `if version` checks.

## Selection sequence

For every scrape connection and every event-stream connection:

1. Open the WebSocket.
2. Authenticate using the existing API-key flow.
3. Call `system.version_short` once and cache the result for that connection.
4. Normalize `25.10.*`, `26.0.*`, or unknown.
5. Select the profile before generic discovery, collector calls, or event subscriptions.
6. Publish only redacted diagnostics: detected version, selected family, and
   profile status. Never log the API key or raw response.

If detection fails, select `unknown`, continue only with the reviewed common
intersection, and expose a diagnostic error. Detection failure must never
expand the method or event allowlist.

## Method safety

All call paths must use profile-aware authorization:

- normal base methods;
- telemetry candidates;
- `EXTRA_METHODS`;
- automatic discovery;
- count queries;
- optional generic reporting calls;
- event subscriptions.

The profile check must happen before transport invocation. A method absent from
the selected profile is intentionally skipped, not called and then classified
as an ordinary API failure.

Keep global mutation, credential, filesystem, entity-ID, and opaque-response
blocks unchanged unless the v26 diff proves a narrower safe rule.

Guard effective query limits per profile so every profile-gated query method
receives a valid positive limit (`query_limit_for` floors the configured limit
to at least 1). The default of 200 is valid for both the 25.10 and v26
families, and neither documented corpus imposes a smaller hard maximum, so no
downward clamp is applied; if a future corpus documents a lower ceiling, add it
to the profile's limit policy so oversized operator configuration cannot
generate invalid requests.

## Authentication scope

Use `auth.login_with_api_key` for the first 25.10/v26 compatibility release and
emit a v26 deprecation diagnostic. Add `auth.login_ex`/SCRAM as a separate v27
readiness project because it requires username handling, a multi-step exchange,
new fixtures, and dependency/TLS decisions.

## Acceptance criteria

- Profile selection is deterministic and unit-tested.
- Unknown versions cannot call v26-only or v25-only methods.
- Removed methods never appear in client call traces for v26 fixtures.
- Existing `EXTRA_METHODS` and discovery cannot bypass profile safety.
- Profile diagnostics contain no secret or identity-bearing payload.
