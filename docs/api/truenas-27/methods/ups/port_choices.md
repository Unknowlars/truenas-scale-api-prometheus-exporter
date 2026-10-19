---
title: ups.port_choices
kind: method
source_rst: _sources/api_methods_ups.port_choices.rst.txt
source_html: api_methods_ups.port_choices.html
required_roles:
  - READONLY_ADMIN
  - SYSTEM_GENERAL_READ
---

# ups.port_choices

## Summary

Returns available UPS device ports for the system (serial ports, USB HID devices, and "auto").

## Required Roles

- `READONLY_ADMIN`
- `SYSTEM_GENERAL_READ`

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
- Type: array of string

Array of available serial ports and device paths for UPS communication.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
