---
title: iscsi.extent.delete
kind: method
source_rst: _sources/api_methods_iscsi.extent.delete.rst.txt
source_html: api_methods_iscsi.extent.delete.html
required_roles:
  - SHARING_ISCSI_EXTENT_WRITE
---

# iscsi.extent.delete

## Summary

Delete iSCSI Extent of `id`.

If `id` iSCSI Extent's `type` was configured to FILE, `remove` can be set to remove the configured file.

## Required Roles

- `SHARING_ISCSI_EXTENT_WRITE`

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

ID of the iSCSI extent to delete.

#### Parameter 2: remove

<a id="Call_parameters_items_i1"></a>
#### remove

- Schema name: `remove`
- Type: boolean
- Default: false

Whether to remove the underlying file for file-based extents.

#### Parameter 3: force

<a id="Call_parameters_items_i2"></a>
#### force

- Schema name: `force`
- Type: boolean
- Default: false

Whether to force deletion even if the extent is in use.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the iSCSI extent is successfully deleted.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
