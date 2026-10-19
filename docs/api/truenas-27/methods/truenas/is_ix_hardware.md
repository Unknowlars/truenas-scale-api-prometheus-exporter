---
title: truenas.is_ix_hardware
kind: method
source_rst: _sources/api_methods_truenas.is_ix_hardware.rst.txt
source_html: api_methods_truenas.is_ix_hardware.html
required_roles:
  - READONLY_ADMIN
---

# truenas.is_ix_hardware

## Summary

Return a boolean value on whether this is hardware that iXsystems sells.

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
- Type: boolean

Whether this system is running on iXsystems hardware.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
