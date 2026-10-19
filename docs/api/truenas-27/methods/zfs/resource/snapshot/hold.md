---
title: zfs.resource.snapshot.hold
kind: method
source_rst: _sources/api_methods_zfs.resource.snapshot.hold.rst.txt
source_html: api_methods_zfs.resource.snapshot.hold.html
required_roles:
  - SNAPSHOT_WRITE
---

# zfs.resource.snapshot.hold

## Summary

Create a hold on a ZFS snapshot.

A hold prevents a snapshot from being destroyed. Multiple holds can be placed on a snapshot with different tags.

Args: data: Hold parameters containing: - path: Snapshot path to hold (e.g., 'pool/dataset@snapshot'). - tag: Hold tag name (default: 'truenas'). - recursive: Apply hold to matching snapshots in child datasets.

Returns: None on success.

Raises: ValidationError: If snapshot not found or hold creation fails.

Examples: # Hold a single snapshot hold({"path": "tank/data@backup"})

# Hold with custom tag hold({"path": "tank/data@backup", "tag": "replication"})

# Hold recursively hold({"path": "tank@backup", "recursive": True})

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

Hold parameters for holding ZFS snapshots.
- No Additional Properties
<a id="headingCall_parameters_items_i0_path"></a>
<a id="Call_parameters_items_i0_path"></a>
##### path (required)

- Schema name: `Path`
- Type: string

Snapshot path to hold (e.g., 'pool/dataset@snapshot').
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_tag"></a>
<a id="Call_parameters_items_i0_tag"></a>
##### tag

- Schema name: `Tag`
- Type: string
- Default: "truenas"

Hold tag name to apply.

<a id="headingCall_parameters_items_i0_recursive"></a>
<a id="Call_parameters_items_i0_recursive"></a>
##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Apply hold recursively to matching snapshots in child datasets.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
