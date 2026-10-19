---
title: system.ready
kind: method
source_rst: _sources/api_methods_system.ready.rst.txt
source_html: api_methods_system.ready.html
required_roles:
  - SYSTEM_GENERAL_READ
---

# system.ready

## Summary

Returns whether the system completed boot and is ready to use

## Required Roles

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
- Type: boolean

Whether the system has completed startup and is ready for use.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
