---
title: pool.snapshot.update
kind: method
source_rst: _sources/api_methods_pool.snapshot.update.rst.txt
source_html: api_methods_pool.snapshot.update.html
required_roles:
  - SNAPSHOT_WRITE
---

# pool.snapshot.update

## Summary

Update the user properties of the snapshot identified by `snap_id`.

## Required Roles

- `SNAPSHOT_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: string

ID of the snapshot to update.

#### Parameter 2: data

#### data

- Schema name: `data`
- Type: object

The property updates to apply to the snapshot.
- No Additional Properties
##### user_properties_update

- Schema name: `User Properties Update`
- Type: array of object
- Default: []

Properties to update.
- No Additional Items

###### Each item of this array must be:

###### PoolSnapshotUserPropertyUpdate

- Schema name: `PoolSnapshotUserPropertyUpdate`
- Type: object
- No Additional Properties
####### key (required)

- Schema name: `Key`
- Type: string

The property name in namespace:property format.

####### value (required)

- Schema name: `Value`
- Type: string

The new value to assign to the user property.
- Must be at most `2147483647` characters long

##### user_properties_remove

- Schema name: `User Properties Remove`
- Type: array of string
- Default: []

Properties to remove.
- No Additional Items

###### Each item of this array must be:

- Type: string

ZFS user property key in namespace:property format (e.g., 'custom:backup*policy', 'org:created*by').

### Return value

- Type: object

Information about the updated snapshot.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
