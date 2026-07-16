---
title: app.stop
kind: method
source_rst: _sources/api_methods_app.stop.rst.txt
source_html: api_methods_app.stop.html
required_roles:
  - APPS_WRITE
---

# app.stop

## Summary

Stop `app_name` app.

This method is a job.

## Required Roles

- `APPS_WRITE`

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

Name of the application to stop.
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the application is successfully stopped.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
