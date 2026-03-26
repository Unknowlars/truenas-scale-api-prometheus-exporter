---
title: truenas.is_production
kind: method
source_rst: _sources/api_methods_truenas.is_production.rst.txt
source_html: api_methods_truenas.is_production.html
required_roles:
  - READONLY_ADMIN
---

# truenas.is_production

## Summary

Returns if system is marked as production.

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

Whether this TrueNAS system is configured for production use.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
