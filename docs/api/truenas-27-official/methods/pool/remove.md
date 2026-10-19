---
title: pool.remove
kind: method
source_rst: _sources/api_methods_pool.remove.rst.txt
source_html: api_methods_pool.remove.html
required_roles:
  - POOL_WRITE
---

# pool.remove

## Summary

Remove a disk from pool of id `id`.

Example::

{ "jsonrpc": "2.0", "id": 1, "method": "pool.remove", "params": [1, { "label": "80802394992848654" }] }

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

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the pool to remove a disk from.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Disk identifier to remove from the pool.
- No Additional Properties
<a id="headingCall_parameters_items_i1_label"></a>
<a id="Call_parameters_items_i1_label"></a>
##### label (required)

- Schema name: `Label`
- Type: string

The vdev guid or device name.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful disk removal.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
