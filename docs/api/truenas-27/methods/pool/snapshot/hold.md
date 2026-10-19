---
title: pool.snapshot.hold
kind: method
source_rst: _sources/api_methods_pool.snapshot.hold.rst.txt
source_html: api_methods_pool.snapshot.hold.html
required_roles:
  - SNAPSHOT_WRITE
---

# pool.snapshot.hold

## Summary

Hold snapshot `id`.

Add `truenas` tag to the snapshot's tag namespace.

## Required Roles

- `SNAPSHOT_WRITE`

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

ID of the snapshot to hold.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Options for controlling snapshot hold behavior.
- No Additional Properties
<a id="headingCall_parameters_items_i1_recursive"></a>
<a id="Call_parameters_items_i1_recursive"></a>
##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Hold snapshots recursively.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful snapshot hold.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
