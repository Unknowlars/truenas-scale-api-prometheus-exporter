# T18 — Configurable bind address + stop hostname leaking via tracebacks

- **Priority:** P3 (security polish)
- **Size:** S
- **Depends on:** nothing
- **Review reference:** review-report.md items (e)1 and (e)2

## Problem A — bind address

`make_server("", port, ...)` (`src/truenas_exporter/http.py` ~64) binds all interfaces with no
way to restrict. `/metrics` exposes a full system inventory (hostnames, dataset names, versions,
GPU/PCI identifiers) unauthenticated. Containers are fine; bare-metal installs deserve a knob.

## Problem B — hostname leak in logs

`main()` carefully redacts the host from its startup log (`runtime.py` ~5045–5052, "safety
invariant: no hostname is ever logged"), but `LOG.warning(..., exc_info=True)` in the event
reconnect path (~2105) and `LOG.exception("Scrape failed")` (~3764) print tracebacks whose
connection-error messages typically embed the target host/IP (`ConnectionRefusedError`,
websocket handshake errors include the URL).

## Code to read (only this)

- `src/truenas_exporter/http.py` (all), `src/truenas_exporter/config.py` (env parsing patterns),
  `src/truenas_exporter/runtime.py` ~2095–2108, ~3763–3765, ~5039–5075.
- `tests/test_http_integration.py`, `tests/test_reliability.py` (config test patterns),
  `.env.example` and the repo root `README.md` env-var table (grep for `EXPORTER_PORT` to find
  where to document the new var).

## Required behavior

1. **Bind address:** add `EXPORTER_BIND_ADDRESS` (default `""` = all interfaces — do NOT change
   the default; existing deployments must not break). Thread it `config.py` →
   `start_http_server(host, port, ...)` → `make_server(host, port, ...)`. Validate it's a plain
   host/IP string (no port). Document in `.env.example` + README env table.
2. **Log hygiene:** create one helper (e.g. `_log_exception_redacted(logger, msg)` or a logging
   `Filter`) that replaces occurrences of the configured WS host (from `urlparse(config.ws_url)
   .hostname`, and host:port) with `<redacted-host>` in the formatted exception text, and use it
   at the two sites above (and `LOG.warning("Dynamic method discovery failed", exc_info=True)`
   ~3111). A `logging.Filter` installed on the `truenas_exporter` logger in `main()` that scrubs
   `record.exc_text`/args is the cleanest single-point fix — choose that if it stays under ~30
   lines.
3. Do not remove the tracebacks — operators need them; only scrub the host string.

## Compatibility rules

- New env var = minor-worthy; defaults unchanged. No metric changes.

## Tests

1. Config: `EXPORTER_BIND_ADDRESS=127.0.0.1` parsed; invalid value (contains `:` port or spaces)
   raises ValueError; unset → `""`.
2. HTTP: server started with `127.0.0.1` binds loopback (assert via the returned server's
   `server_address`).
3. Log scrub: configure the filter with host `nas.example`, log an exception whose message
   contains `wss://nas.example:443/api/current` → captured log output (pytest `caplog`) contains
   `<redacted-host>` and not `nas.example`.

## Verification

```
python3 -m pytest tests/test_http_integration.py tests/test_reliability.py tests/test_cli.py -q
./scripts/validate.sh
```

Note: `scripts/public_release_audit.py` runs in validate.sh and may scan docs/env files — if it
flags the new env var documentation, follow its rules (read the script if it fails).

## Definition of done

- Bind address configurable and documented; default behavior unchanged; no code path logs the
  target hostname (filter proven by test); validate.sh green; TASKS.md updated (minor-worthy).

## Outcome

_(fill in when done)_
