---
title: interface.rollback
kind: method
source_rst: _sources/api_methods_interface.rollback.rst.txt
source_html: api_methods_interface.rollback.html
required_roles:
  - NETWORK_INTERFACE_WRITE
---

# interface.rollback

## Summary

Rollback pending interfaces changes.

## Required Roles

- `NETWORK_INTERFACE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: null

No return value for successful rollback operation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
