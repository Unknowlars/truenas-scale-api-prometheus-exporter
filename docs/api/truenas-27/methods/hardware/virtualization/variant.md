---
title: hardware.virtualization.variant
kind: method
source_rst: _sources/api_methods_hardware.virtualization.variant.rst.txt
source_html: api_methods_hardware.virtualization.variant.html
required_roles:
  - SYSTEM_GENERAL_READ
---

# hardware.virtualization.variant

## Summary

Report the virtualization variation of TrueNAS system

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
- Type: string

The hardware virtualization variant available on this system.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
