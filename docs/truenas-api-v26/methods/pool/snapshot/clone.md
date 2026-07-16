---
title: pool.snapshot.clone
kind: method
source_rst: _sources/api_methods_pool.snapshot.clone.rst.txt
source_html: api_methods_pool.snapshot.clone.html
required_roles:
  - DATASET_WRITE | SNAPSHOT_WRITE
---

# pool.snapshot.clone

## Summary

Clone a given snapshot to a new dataset.

## Required Roles

- `DATASET_WRITE | SNAPSHOT_WRITE`

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

PoolSnapshotCloneArgs parameters.
- No Additional Properties
##### snapshot (required)

- Schema name: `Snapshot`
- Type: string

Full name of the snapshot to clone from.
- Must be at least `1` characters long

##### dataset_dst (required)

- Schema name: `Dataset Dst`
- Type: string

Name for the new dataset created from the snapshot.
- Must be at least `1` characters long

##### dataset_properties

- Schema name: `Dataset Properties`
- Type: object
- Default: {}

Object mapping ZFS property names to values to set on the cloned dataset.

### Return value

- Schema name: `Result`
- Type: const

Clone succeeded.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
