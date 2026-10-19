---
title: zfs.resource.snapshot.clone
kind: method
source_rst: _sources/api_methods_zfs.resource.snapshot.clone.rst.txt
source_html: api_methods_zfs.resource.snapshot.clone.html
required_roles:
  - SNAPSHOT_WRITE
---

# zfs.resource.snapshot.clone

## Summary

Clone a ZFS snapshot to create a new dataset.

A validation error is raised when:

- the source snapshot does not exist

- the destination dataset already exists

- the source is not a snapshot

A filesystem clone that cannot be mounted is kept, and the error names it.

Examples:

Clone a snapshot to a new dataset:

.. code:: json

{"snapshot": "tank/data@backup", "dataset": "tank/data_clone"}

Clone with properties:

.. code:: json

{ "snapshot": "tank/data@backup", "dataset": "tank/data_clone", "properties": {"compression": "lz4", "quota": "10G"} }

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

#### Parameter 1: data

<a id="Call_parameters_items_i0"></a>
#### data

- Schema name: `data`
- Type: object

Clone parameters for cloning ZFS snapshots.
- No Additional Properties
<a id="headingCall_parameters_items_i0_snapshot"></a>
<a id="Call_parameters_items_i0_snapshot"></a>
##### snapshot (required)

- Schema name: `Snapshot`
- Type: string

Source snapshot path to clone (e.g., 'pool/dataset@snapshot').
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_dataset"></a>
<a id="Call_parameters_items_i0_dataset"></a>
##### dataset (required)

- Schema name: `Dataset`
- Type: string

Destination dataset path for the clone (e.g., 'pool/clone').
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_properties"></a>
<a id="Call_parameters_items_i0_properties"></a>
##### properties

- Schema name: `Properties`
- Type: object
- Default: {}

ZFS properties to set on the cloned dataset.
<a id="headingCall_parameters_items_i0_properties_additionalProperties"></a>
<a id="Call_parameters_items_i0_properties_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
<a id="Call_parameters_items_i0_properties_additionalProperties_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_properties_additionalProperties_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_properties_additionalProperties_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_properties_additionalProperties_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_properties_additionalProperties_anyOf_i1)

- Type: integer

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
