---
title: zfs.resource.snapshot.count
kind: method
source_rst: _sources/api_methods_zfs.resource.snapshot.count.rst.txt
source_html: api_methods_zfs.resource.snapshot.count.html
required_roles:
  - SNAPSHOT_READ
---

# zfs.resource.snapshot.count

## Summary

Count ZFS snapshots per dataset.

This method provides a fast way to count snapshots without retrieving full snapshot information. Useful for UI displays and quota checks.

Examples:

Count snapshots for root filesystems only:

.. code:: json

{}

Count all snapshots recursively:

.. code:: json

{"recursive": true}

Count snapshots for a specific dataset:

.. code:: json

{"paths": ["tank/data"]}

Count snapshots for a dataset and all of its children:

.. code:: json

{"paths": ["tank"], "recursive": true}

## Required Roles

- `SNAPSHOT_READ`

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
- Default: {"paths": [], "recursive": false}

Count parameters for counting ZFS snapshots.
- No Additional Properties
<a id="headingCall_parameters_items_i0_paths"></a>
<a id="Call_parameters_items_i0_paths"></a>
##### paths

- Schema name: `Paths`
- Type: array of string
- Default: []

Dataset paths to count snapshots for. If empty, counts all snapshots.
- All items must be unique
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_paths_items"></a>
- Type: string

<a id="headingCall_parameters_items_i0_recursive"></a>
<a id="Call_parameters_items_i0_recursive"></a>
##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Include snapshots from child datasets when counting.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: object

Mapping of dataset names to their snapshot counts.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
