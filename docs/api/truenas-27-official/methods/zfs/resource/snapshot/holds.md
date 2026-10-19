---
title: zfs.resource.snapshot.holds
kind: method
source_rst: _sources/api_methods_zfs.resource.snapshot.holds.rst.txt
source_html: api_methods_zfs.resource.snapshot.holds.html
required_roles:
  - SNAPSHOT_READ
---

# zfs.resource.snapshot.holds

## Summary

Get holds on a ZFS snapshot.

Examples:

Get the holds on a snapshot:

.. code:: json

{"path": "tank/data@backup"}

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

Query parameters for getting holds on a ZFS snapshot.
- No Additional Properties
<a id="headingCall_parameters_items_i0_path"></a>
<a id="Call_parameters_items_i0_path"></a>
##### path (required)

- Schema name: `Path`
- Type: string

Snapshot path to query holds for (e.g., 'pool/dataset@snapshot').
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of string

List of hold tag names on the snapshot.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
