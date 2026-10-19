---
title: fc.capable
kind: method
source_rst: _sources/api_methods_fc.capable.rst.txt
source_html: api_methods_fc.capable.html
required_roles:
  - SHARING_ISCSI_TARGET_READ
---

# fc.capable

## Summary

Returns `true` if the system is licensed for FIBRECHANNEL and contains one or more Fibre Channel cards. `false` otherwise.

## Required Roles

- `SHARING_ISCSI_TARGET_READ`

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

Returns `true` if the system has Fibre Channel capabilities, `false` otherwise.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
