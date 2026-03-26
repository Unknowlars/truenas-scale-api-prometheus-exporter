---
title: pool.validate_name
kind: method
source_rst: _sources/api_methods_pool.validate_name.rst.txt
source_html: api_methods_pool.validate_name.html
required_roles:
  - POOL_READ
---

# pool.validate_name

## Summary

Validates `pool_name` is a valid name for a pool.

## Required Roles

- `POOL_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: pool_name

#### pool_name

- Schema name: `pool_name`
- Type: string

Pool name to validate for compliance with naming rules.
- Must be at least `1` characters long
- Must be at most `50` characters long

### Return value

- Schema name: `Result`
- Type: const

Indicates the pool name is valid.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
