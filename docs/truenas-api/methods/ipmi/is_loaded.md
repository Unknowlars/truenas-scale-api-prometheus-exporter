---
title: ipmi.is_loaded
kind: method
source_rst: _sources/api_methods_ipmi.is_loaded.rst.txt
source_html: api_methods_ipmi.is_loaded.html
required_roles:
  - READONLY_ADMIN
---

# ipmi.is_loaded

## Summary

Returns a boolean value indicating if /dev/ipmi0 is loaded.

## Required Roles

- `READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` if IPMI modules are loaded and available, `false` otherwise.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
