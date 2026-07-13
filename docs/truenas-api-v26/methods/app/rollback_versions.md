---
title: app.rollback_versions
kind: method
source_rst: _sources/api_methods_app.rollback_versions.rst.txt
source_html: api_methods_app.rollback_versions.html
required_roles:
  - APPS_READ
---

# app.rollback_versions

## Summary

Retrieve versions available for rollback for `app_name` app.

## Required Roles

- `APPS_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: app_name

#### app_name

- Schema name: `app_name`
- Type: string

Name of the application to get rollback versions for.
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: array of string

Array of version strings available for rollback.
- No Additional Items

#### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
