---
title: support.is_available_and_enabled
kind: method
source_rst: _sources/api_methods_support.is_available_and_enabled.rst.txt
source_html: api_methods_support.is_available_and_enabled.html
required_roles:
  - SUPPORT_READ
---

# support.is_available_and_enabled

## Summary

Returns whether Proactive Support is available and enabled.

## Required Roles

- `SUPPORT_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: boolean

Whether support functionality is both available and enabled.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
