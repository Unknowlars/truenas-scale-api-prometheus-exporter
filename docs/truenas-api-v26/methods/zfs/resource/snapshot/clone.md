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

Invalid input is returned to the client as a JSON-RPC `error` response (code `-32602`, *Invalid params*); each failing condition appears in the error's `data.extra` array with its own `errno`. A validation error is raised when:

- the source snapshot does not exist

- the destination dataset already exists

- the source is not a snapshot

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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`
- Type: object

Clone parameters for cloning ZFS snapshots.
- No Additional Properties
##### snapshot (required)

- Schema name: `Snapshot`
- Type: string

Source snapshot path to clone (e.g., 'pool/dataset@snapshot').
- Must be at least `1` characters long

##### dataset (required)

- Schema name: `Dataset`
- Type: string

Destination dataset path for the clone (e.g., 'pool/clone').
- Must be at least `1` characters long

##### properties

- Schema name: `Properties`
- Type: object
- Default: {}

ZFS properties to set on the cloned dataset.
###### Additional Properties

Each additional property must conform to the following schema
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: integer

### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
