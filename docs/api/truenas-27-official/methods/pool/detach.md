---
title: pool.detach
kind: method
source_rst: _sources/api_methods_pool.detach.rst.txt
source_html: api_methods_pool.detach.html
required_roles:
  - POOL_WRITE
---

# pool.detach

## Summary

Detach a disk from pool of id `id`.

Example::

{ "jsonrpc": "2.0", "id": 1, "method": "pool.detach", "params": [1, { "label": "80802394992848654" }] }

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

ID of the pool to detach a disk from.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Configuration for the disk detachment operation.
- No Additional Properties
<a id="headingCall_parameters_items_i1_label"></a>
<a id="Call_parameters_items_i1_label"></a>
##### label (required)

- Schema name: `Label`
- Type: string

GUID or device name of the vdev to detach.

<a id="headingCall_parameters_items_i1_wipe"></a>
<a id="Call_parameters_items_i1_wipe"></a>
##### wipe

- Schema name: `Wipe`
- Type: boolean
- Default: false

Whether to wipe the detached disk after removal.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: const

Indicates successful disk detachment.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
