---
title: system.license_update
kind: method
source_rst: _sources/api_methods_system.license_update.rst.txt
source_html: api_methods_system.license_update.html
required_roles:
  - SYSTEM_PRODUCT_WRITE
---

# system.license_update

## Summary

Update license file

## Required Roles

- `SYSTEM_PRODUCT_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: license

#### license

- Schema name: `license`
- Type: string

License key to apply to the system.
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful license update.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
