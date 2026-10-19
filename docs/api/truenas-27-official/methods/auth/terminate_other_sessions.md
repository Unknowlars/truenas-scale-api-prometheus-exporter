---
title: auth.terminate_other_sessions
kind: method
source_rst: _sources/api_methods_auth.terminate_other_sessions.rst.txt
source_html: api_methods_auth.terminate_other_sessions.html
required_roles:
  - AUTH_SESSIONS_WRITE
---

# auth.terminate_other_sessions

## Summary

Terminates all other sessions (except the current one).

## Required Roles

- `AUTH_SESSIONS_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: const

Returns `true` when other sessions are successfully terminated.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
