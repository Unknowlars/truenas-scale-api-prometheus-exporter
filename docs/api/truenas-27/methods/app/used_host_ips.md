---
title: app.used_host_ips
kind: method
source_rst: _sources/api_methods_app.used_host_ips.rst.txt
source_html: api_methods_app.used_host_ips.html
required_roles:
  - APPS_READ
---

# app.used_host_ips

## Summary

Returns host IPs in use by applications.

## Required Roles

- `APPS_READ`

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

Object mapping application names to arrays of host IP addresses they use.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Type: array of string
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_additionalProperties_items"></a>
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
