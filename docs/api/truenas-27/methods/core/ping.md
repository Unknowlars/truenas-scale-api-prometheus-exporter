---
title: core.ping
kind: method
source_rst: _sources/api_methods_core.ping.rst.txt
source_html: api_methods_core.ping.html
required_roles:
  []
---

# core.ping

## Summary

Respond to WebSocket ping frames with "pong".

This endpoint can be used to keep connections alive as outlined in the WebSocket specification. It does not require authentication but is rate limited to prevent abuse.

Returns: str: Always returns "pong"

## Required Roles

- None documented.

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

Always returns `pong` to confirm system responsiveness.
- Specific value: `"pong"`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
