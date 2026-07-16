---
title: zfs.resource.snapshot.rename
kind: method
source_rst: _sources/api_methods_zfs.resource.snapshot.rename.rst.txt
source_html: api_methods_zfs.resource.snapshot.rename.html
required_roles:
  - SNAPSHOT_WRITE
---

# zfs.resource.snapshot.rename

## Summary

Rename a ZFS snapshot.

Invalid input is returned to the client as a JSON-RPC `error` response (code `-32602`, *Invalid params*); each failing condition appears in the error's `data.extra` array with its own `errno`. A validation error is raised when:

- the snapshot does not exist

- the new name already exists

- a supplied path is invalid

Examples:

Rename a single snapshot:

.. code:: json

{"current_name": "tank/data@old", "new_name": "tank/data@new"}

Rename matching snapshots in child datasets:

.. code:: json

{"current_name": "tank@old", "new_name": "tank@new", "recursive": true}

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

Rename parameters for renaming ZFS snapshots.
- No Additional Properties
##### current_name (required)

- Schema name: `Current Name`
- Type: string

Current snapshot path (e.g., 'pool/dataset@old_name').
- Must be at least `1` characters long

##### new_name (required)

- Schema name: `New Name`
- Type: string

New snapshot path (e.g., 'pool/dataset@new_name').
- Must be at least `1` characters long

##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Recursively rename matching snapshots in child datasets.

### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
