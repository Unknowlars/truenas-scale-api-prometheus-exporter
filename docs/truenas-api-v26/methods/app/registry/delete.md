---
title: app.registry.delete
kind: method
source_rst: _sources/api_methods_app.registry.delete.rst.txt
source_html: api_methods_app.registry.delete.html
required_roles:
  - APPS_WRITE
---

# app.registry.delete

## Summary

Delete an app registry entry.

## Required Roles

- `APPS_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the container registry to delete.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the container registry is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
