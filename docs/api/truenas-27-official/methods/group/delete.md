---
title: group.delete
kind: method
source_rst: _sources/api_methods_group.delete.rst.txt
source_html: api_methods_group.delete.html
required_roles:
  - ACCOUNT_WRITE
---

# group.delete

## Summary

Delete group `id`.

## Required Roles

- `ACCOUNT_WRITE`

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

API identifier of the group to delete.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object
- Default: {"delete_users": false}

Options controlling group deletion behavior.
- No Additional Properties
<a id="headingCall_parameters_items_i1_delete_users"></a>
<a id="Call_parameters_items_i1_delete_users"></a>
##### delete_users

- Schema name: `Delete Users`
- Type: boolean
- Default: false

Deletes all users that have this group as their primary group.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: integer

The API identifier of the deleted group.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
