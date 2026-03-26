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

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: const

Always returns `pong` to confirm system responsiveness.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
