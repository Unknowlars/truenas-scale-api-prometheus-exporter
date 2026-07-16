---
title: zfs.resource.snapshot.rollback
kind: method
source_rst: _sources/api_methods_zfs.resource.snapshot.rollback.rst.txt
source_html: api_methods_zfs.resource.snapshot.rollback.html
required_roles:
  - SNAPSHOT_WRITE
---

# zfs.resource.snapshot.rollback

## Summary

Rollback a ZFS dataset to a snapshot.

.. warning::

This is a destructive change. All data written since the target snapshot was taken will be discarded.

Invalid input is returned to the client as a JSON-RPC `error` response (code `-32602`, *Invalid params*); each failing condition appears in the error's `data.extra` array with its own `errno`. A validation error is raised when:

- the snapshot does not exist

- the rollback cannot be completed

Examples:

Roll back to a snapshot:

.. code:: json

{"path": "tank/data@backup"}

Roll back, destroying more recent snapshots:

.. code:: json

{"path": "tank/data@backup", "recursive": true}

Roll back all child datasets:

.. code:: json

{"path": "tank@backup", "recursive_rollback": true}

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

Rollback parameters for rolling back to ZFS snapshots.
- No Additional Properties
##### path (required)

- Schema name: `Path`
- Type: string

Snapshot path to rollback to (e.g., 'pool/dataset@snapshot').
- Must be at least `1` characters long

##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Destroy any snapshots and bookmarks more recent than the one specified.

##### recursive_clones

- Schema name: `Recursive Clones`
- Type: boolean
- Default: false

Like recursive, but also destroy any clones.

##### force

- Schema name: `Force`
- Type: boolean
- Default: false

Force unmount of any clones.

##### recursive_rollback

- Schema name: `Recursive Rollback`
- Type: boolean
- Default: false

Do a complete recursive rollback of each child snapshot. Fails if any child lacks the snapshot.

### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
