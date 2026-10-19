---
title: ipmi.lan.channels
kind: method
source_rst: _sources/api_methods_ipmi.lan.channels.rst.txt
source_html: api_methods_ipmi.lan.channels.html
required_roles:
  - IPMI_READ
---

# ipmi.lan.channels

## Summary

Return a list of available IPMI channels.

## Required Roles

- `IPMI_READ`

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
- Type: array of integer

Array of available IPMI LAN channel numbers.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
