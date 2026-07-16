---
title: truenas.set_production
kind: method
source_rst: _sources/api_methods_truenas.set_production.rst.txt
source_html: api_methods_truenas.set_production.html
required_roles:
  - FULL_ADMIN
---

# truenas.set_production

## Summary

Sets system production state and optionally sends initial debug.

This method is a job.

## Required Roles

- `FULL_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: production

#### production

- Schema name: `production`
- Type: boolean

Whether to configure the system for production use.

#### Parameter 2: attach_debug

#### attach_debug

- Schema name: `attach_debug`
- Type: boolean
- Default: false

Whether to attach debug information when transitioning to production mode.

### Return value

- Schema name: `Result`

Result object containing production configuration details. `null` if transition failed.
#### Any of

##### Option 1

- Type: object

##### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
