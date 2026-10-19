---
title: pool.dataset.delete
kind: method
source_rst: _sources/api_methods_pool.dataset.delete.rst.txt
source_html: api_methods_pool.dataset.delete.html
required_roles:
  - DATASET_DELETE
---

# pool.dataset.delete

## Summary

Delete dataset/zvol `id`.

.. examples(websocket)::

Delete "tank/myuser" dataset.

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "pool.dataset.delete", "params": ["tank/myuser"] }

## Required Roles

- `DATASET_DELETE`

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
- Type: string

The dataset ID (full path) to delete.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Options controlling the deletion behavior such as recursive and force flags.
- No Additional Properties
<a id="headingCall_parameters_items_i1_recursive"></a>
<a id="Call_parameters_items_i1_recursive"></a>
##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Also delete/destroy all children datasets. When root dataset is specified as `id` with `recursive`, it will destroy all the children of the root dataset present leaving root dataset intact.

<a id="headingCall_parameters_items_i1_force"></a>
<a id="Call_parameters_items_i1_force"></a>
##### force

- Schema name: `Force`
- Type: boolean
- Default: false

Delete datasets even if they are busy.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: enum (of boolean or null)

Return true on successful deletion or null if the `zfs destroy` command fails with "dataset does not exist".
#### Must be one of:

- null
- true

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
