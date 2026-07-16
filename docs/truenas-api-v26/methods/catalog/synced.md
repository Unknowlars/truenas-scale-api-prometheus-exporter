---
title: catalog.synced
kind: method
source_rst: _sources/api_methods_catalog.synced.rst.txt
source_html: api_methods_catalog.synced.html
required_roles:
  - CATALOG_READ
---

# catalog.synced

## Summary

Return whether the catalog has been synced at least once.

## Required Roles

- `CATALOG_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` if the catalog has been synced at least once, `false` otherwise.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
