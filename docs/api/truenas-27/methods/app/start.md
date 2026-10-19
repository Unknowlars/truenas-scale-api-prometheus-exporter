---
title: app.start
kind: method
source_rst: _sources/api_methods_app.start.rst.txt
source_html: api_methods_app.start.html
required_roles:
  - APPS_WRITE
---

# app.start

## Summary

Start `app_name` app.

This method is a job.

## Required Roles

- `APPS_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: app_name

<a id="Call_parameters_items_i0"></a>
#### app_name

- Schema name: `app_name`
- Type: string

Name of the application to start.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the application is successfully started.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
