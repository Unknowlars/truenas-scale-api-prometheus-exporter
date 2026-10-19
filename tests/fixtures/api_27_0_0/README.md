# Synthetic API 27.0.0 responses

These are synthetic, minimal examples based on the pinned local method/event
schemas in `docs/api/truenas-27/` and the official comparison corpus. They are
not captured NAS responses and prove mocked behavior only. Names and values
are artificial. Selected query responses may omit fields outside their projection.

`freeing` is nullable integer bytes; zero is valid and null is unavailable.
`auth.login_ex` requires explicit SUCCESS. Realtime rates remain gauges. The
historical `disls` spelling and compatibility `disks` spelling are both accepted.
