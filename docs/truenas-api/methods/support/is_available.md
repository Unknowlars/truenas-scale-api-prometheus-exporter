---
title: support.is_available
kind: method
source_rst: _sources/api_methods_support.is_available.rst.txt
source_html: api_methods_support.is_available.html
required_roles:
  - SUPPORT_READ
---

# support.is_available

## Summary

Returns whether Proactive Support is available for this product type and current license.

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

Whether support functionality is available on this system.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
