---
title: app.ip_choices
kind: method
source_rst: _sources/api_methods_app.ip_choices.rst.txt
source_html: api_methods_app.ip_choices.html
required_roles:
  - APPS_READ
  - READONLY_ADMIN
---

# app.ip_choices

## Summary

Returns IP choices which can be used by applications.

## Required Roles

- `APPS_READ`
- `READONLY_ADMIN`

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
- Type: object

Object mapping IP addresses to their descriptive names.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Type: string
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
