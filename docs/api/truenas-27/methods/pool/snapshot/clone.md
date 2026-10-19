---
title: pool.snapshot.clone
kind: method
source_rst: _sources/api_methods_pool.snapshot.clone.rst.txt
source_html: api_methods_pool.snapshot.clone.html
required_roles:
  - DATASET_WRITE
  - SNAPSHOT_WRITE
---

# pool.snapshot.clone

## Summary

Clone a given snapshot to a new dataset.

## Required Roles

- `DATASET_WRITE`
- `SNAPSHOT_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

<a id="Call_parameters_items_i0"></a>
#### data

- Schema name: `data`
- Type: object

PoolSnapshotCloneArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_snapshot"></a>
<a id="Call_parameters_items_i0_snapshot"></a>
##### snapshot (required)

- Schema name: `Snapshot`
- Type: string

Full name of the snapshot to clone from.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_dataset_dst"></a>
<a id="Call_parameters_items_i0_dataset_dst"></a>
##### dataset_dst (required)

- Schema name: `Dataset Dst`
- Type: string

Name for the new dataset created from the snapshot.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_dataset_properties"></a>
<a id="Call_parameters_items_i0_dataset_properties"></a>
##### dataset_properties

- Schema name: `Dataset Properties`
- Type: object
- Default: {}

Object mapping ZFS property names to values to set on the cloned dataset.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: const

Clone succeeded.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
