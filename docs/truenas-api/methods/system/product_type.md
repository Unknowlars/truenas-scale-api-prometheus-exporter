---
title: system.product_type
kind: method
source_rst: _sources/api_methods_system.product_type.rst.txt
source_html: api_methods_system.product_type.html
required_roles:
  - SYSTEM_PRODUCT_READ
---

# system.product_type

## Summary

Returns the type of the product

## Required Roles

- `SYSTEM_PRODUCT_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: enum (of string)

Product type of this TrueNAS system.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
