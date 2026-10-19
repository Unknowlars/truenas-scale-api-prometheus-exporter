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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: name

<a id="Call_parameters_items_i0"></a>
#### name

- Schema name: `name`
- Type: string

Name of the iX volume to check for existence.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` if the iX volume exists, `false` otherwise.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
