---
title: filesystem.acltemplate.delete
kind: method
source_rst: _sources/api_methods_filesystem.acltemplate.delete.rst.txt
source_html: api_methods_filesystem.acltemplate.delete.html
required_roles:
  - FILESYSTEM_ATTRS_WRITE
---

# filesystem.acltemplate.delete

## Summary

Delete the ACL template identified by `id`.

Built-in ACL templates may not be deleted; attempting to delete one returns a JSON-RPC `error` response (code `-32001`, *Method call error*).

## Required Roles

- `FILESYSTEM_ATTRS_WRITE`

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

ID of the ACL template to delete.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the ACL template is successfully deleted.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
