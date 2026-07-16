---
title: app.ix_volume.exists
kind: method
source_rst: _sources/api_methods_app.ix_volume.exists.rst.txt
source_html: api_methods_app.ix_volume.exists.html
required_roles:
  - APPS_READ
---

# app.ix_volume.exists

## Summary

Check if ix-volumes exist for `app_name`.

## Required Roles

- `APPS_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: name

#### name

- Schema name: `name`
- Type: string

Name of the iX volume to check for existence.
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` if the iX volume exists, `false` otherwise.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
