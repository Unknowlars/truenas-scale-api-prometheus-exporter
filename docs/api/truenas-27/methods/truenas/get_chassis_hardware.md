---
title: truenas.get_chassis_hardware
kind: method
source_rst: _sources/api_methods_truenas.get_chassis_hardware.rst.txt
source_html: api_methods_truenas.get_chassis_hardware.html
required_roles:
  - READONLY_ADMIN
---

# truenas.get_chassis_hardware

## Summary

Returns what type of hardware this is, detected from dmidecode.

## Required Roles

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
- Type: string

Hardware chassis model identifier for this TrueNAS system.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
