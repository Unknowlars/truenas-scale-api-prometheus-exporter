---
title: pool.import_pool
kind: method
source_rst: _sources/api_methods_pool.import_pool.rst.txt
source_html: api_methods_pool.import_pool.html
required_roles:
  - POOL_WRITE
---

# pool.import_pool

## Summary

Import a pool found with `pool.import_find`.

Errors: ENOENT - Pool not found

.. examples(websocket)::

Import pool of guid 5571830764813710860.

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "pool.import_pool, "params": [{ "guid": "5571830764813710860" }] }

This method is a job.

## Required Roles

- `POOL_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: pool_import

<a id="Call_parameters_items_i0"></a>
#### pool_import

- Schema name: `pool_import`
- Type: object

PoolImportPoolArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_guid"></a>
<a id="Call_parameters_items_i0_guid"></a>
##### guid (required)

- Schema name: `Guid`
- Type: string

GUID of the pool to import.

<a id="headingCall_parameters_items_i0_name"></a>
<a id="Call_parameters_items_i0_name"></a>
##### name

- Schema name: `Name`
- Default: null

If specified, import the pool using this name.
<a id="Call_parameters_items_i0_name_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_name_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_name_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: const

Indicates successful pool import.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
