---
title: zfs.resource.snapshot.release
kind: method
source_rst: _sources/api_methods_zfs.resource.snapshot.release.rst.txt
source_html: api_methods_zfs.resource.snapshot.release.html
required_roles:
  - SNAPSHOT_WRITE
---

# zfs.resource.snapshot.release

## Summary

Release hold(s) from a ZFS snapshot.

A validation error is raised when:

- the snapshot does not exist

- the hold cannot be released

Examples:

Release a specific hold:

.. code:: json

{"path": "tank/data@backup", "tag": "replication"}

Release all holds from a snapshot:

.. code:: json

{"path": "tank/data@backup"}

Release a hold from matching snapshots in child datasets:

.. code:: json

{"path": "tank@backup", "tag": "backup", "recursive": true}

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

Release parameters for releasing holds on ZFS snapshots.
- No Additional Properties
<a id="headingCall_parameters_items_i0_path"></a>
<a id="Call_parameters_items_i0_path"></a>
##### path (required)

- Schema name: `Path`
- Type: string

Snapshot path to release holds from (e.g., 'pool/dataset@snapshot').
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_tag"></a>
<a id="Call_parameters_items_i0_tag"></a>
##### tag

- Schema name: `Tag`
- Default: null

Specific tag to release. If None, releases all hold tags.
<a id="Call_parameters_items_i0_tag_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_tag_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_tag_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_tag_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_tag_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_recursive"></a>
<a id="Call_parameters_items_i0_recursive"></a>
##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Release holds recursively from matching snapshots in child datasets.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
