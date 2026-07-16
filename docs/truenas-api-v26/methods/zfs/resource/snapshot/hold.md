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

Invalid input is returned to the client as a JSON-RPC `error` response (code `-32602`, *Invalid params*); each failing condition appears in the error's `data.extra` array with its own `errno`. A validation error is raised when:

- the snapshot does not exist

- the hold cannot be created

Examples:

Hold a snapshot:

.. code:: json

{"path": "tank/data@backup"}

Hold with a custom tag:

.. code:: json

{"path": "tank/data@backup", "tag": "replication"}

Hold matching snapshots in child datasets:

.. code:: json

{"path": "tank@backup", "recursive": true}

## Required Roles

- `SNAPSHOT_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`
- Type: object

Hold parameters for holding ZFS snapshots.
- No Additional Properties
##### path (required)

- Schema name: `Path`
- Type: string

Snapshot path to hold (e.g., 'pool/dataset@snapshot').
- Must be at least `1` characters long

##### tag

- Schema name: `Tag`
- Type: string
- Default: "truenas"

Hold tag name to apply.

##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Apply hold recursively to matching snapshots in child datasets.

### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
