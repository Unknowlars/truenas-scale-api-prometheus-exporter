---
title: pool.offline
kind: method
source_rst: _sources/api_methods_pool.offline.rst.txt
source_html: api_methods_pool.offline.html
required_roles:
  - POOL_WRITE
---

# pool.offline

## Summary

Offline a disk from pool of id `id`.

Example::

{ "jsonrpc": "2.0", "id": 1, "method": "pool.offline", "params": [1, { "label": "80802394992848654" }] }

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

ID of the pool to modify.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Disk identifier to take offline.
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
- Type: const
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
