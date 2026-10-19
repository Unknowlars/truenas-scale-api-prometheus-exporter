---
title: app.available_space
kind: method
source_rst: _sources/api_methods_app.available_space.rst.txt
source_html: api_methods_app.available_space.html
required_roles:
  - CATALOG_READ
---

# app.available_space

## Summary

Returns space available in bytes in the configured apps pool which apps can consume.

## Required Roles

- `CATALOG_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: integer

Available disk space in bytes for application storage.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
