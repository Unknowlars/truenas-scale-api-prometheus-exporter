---
title: system.feature_enabled
kind: method
source_rst: _sources/api_methods_system.feature_enabled.rst.txt
source_html: api_methods_system.feature_enabled.html
required_roles:
  - SYSTEM_PRODUCT_READ
---

# system.feature_enabled

## Summary

Returns whether the `feature` is enabled or not

## Required Roles

- `SYSTEM_PRODUCT_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: feature

#### feature

- Schema name: `feature`
- Type: enum (of string)

Feature to check for availability on this system.

### Return value

- Schema name: `Result`
- Type: boolean

Whether the specified feature is enabled on this system.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
