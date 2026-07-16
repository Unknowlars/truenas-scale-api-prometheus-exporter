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

Invalid input is returned to the client as a JSON-RPC `error` response (code `-32602`, *Invalid params*); each failing condition appears in the error's `data.extra` array with its own `errno`. A validation error is raised when:

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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`
- Type: object

Release parameters for releasing holds on ZFS snapshots.
- No Additional Properties
##### path (required)

- Schema name: `Path`
- Type: string

Snapshot path to release holds from (e.g., 'pool/dataset@snapshot').
- Must be at least `1` characters long

##### tag

- Schema name: `Tag`
- Default: null

Specific tag to release. If None, releases all hold tags.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Release holds recursively from matching snapshots in child datasets.

### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
