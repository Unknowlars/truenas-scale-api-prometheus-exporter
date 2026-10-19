---
title: fcport.delete
kind: method
source_rst: _sources/api_methods_fcport.delete.rst.txt
source_html: api_methods_fcport.delete.html
required_roles:
  - SHARING_ISCSI_TARGET_WRITE
---

# fcport.delete

## Summary

Delete FC port mapping `id`.

## Required Roles

- `SHARING_ISCSI_TARGET_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the Fibre Channel port to delete.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the Fibre Channel port is successfully deleted.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
