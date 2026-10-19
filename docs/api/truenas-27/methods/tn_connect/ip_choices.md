---
title: tn_connect.ip_choices
kind: method
source_rst: _sources/api_methods_tn_connect.ip_choices.rst.txt
source_html: api_methods_tn_connect.ip_choices.html
required_roles:
  - READONLY_ADMIN
  - TRUENAS_CONNECT_READ
---

# tn_connect.ip_choices

## Summary

Returns IP choices which can be used with TrueNAS Connect.

.. deprecated:: TrueNAS Connect now derives IPs from System > General settings.

*DEPRECATED: this method is scheduled to be removed in v26.*

## Required Roles

- `READONLY_ADMIN`
- `TRUENAS_CONNECT_READ`

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

Object of available IP addresses and their associated interface descriptions.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
