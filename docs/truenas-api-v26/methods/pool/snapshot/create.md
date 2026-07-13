---
title: pool.snapshot.create
kind: method
source_rst: _sources/api_methods_pool.snapshot.create.rst.txt
source_html: api_methods_pool.snapshot.create.html
required_roles:
  - SNAPSHOT_WRITE
---

# pool.snapshot.create

## Summary

Take a snapshot from a given dataset.

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

Configuration for creating a snapshot with either an explicit name or naming schema.
##### Any of

###### PoolSnapshotCreateWithName

- Schema name: `PoolSnapshotCreateWithName`
- Type: object
- No Additional Properties
####### dataset (required)

- Schema name: `Dataset`
- Type: string

Name of the dataset to create a snapshot of.
- Must be at least `1` characters long

####### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively snapshot child datasets.

####### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Array of dataset patterns to exclude from recursive snapshots.
- No Additional Items

######## Each item of this array must be:

- Type: string

####### vmware_sync

- Schema name: `Vmware Sync`
- Type: boolean
- Default: false

Whether to sync VMware VMs before taking the snapshot.

####### suspend_vms

- Schema name: `Suspend Vms`
- Type: boolean
- Default: false

Temporarily suspend VMs before taking snapshot.

####### properties

- Schema name: `Properties`
- Type: object
- Default: {}

Object mapping ZFS property names to values to set on the snapshot.

####### name (required)

- Schema name: `Name`
- Type: string

Explicit name for the snapshot.
- Must be at least `1` characters long

###### PoolSnapshotCreateWithSchema

- Schema name: `PoolSnapshotCreateWithSchema`
- Type: object
- No Additional Properties
####### dataset (required)

- Schema name: `Dataset`
- Type: string

Name of the dataset to create a snapshot of.
- Must be at least `1` characters long

####### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively snapshot child datasets.

####### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Array of dataset patterns to exclude from recursive snapshots.
- No Additional Items

######## Each item of this array must be:

- Type: string

####### vmware_sync

- Schema name: `Vmware Sync`
- Type: boolean
- Default: false

Whether to sync VMware VMs before taking the snapshot.

####### suspend_vms

- Schema name: `Suspend Vms`
- Type: boolean
- Default: false

Temporarily suspend VMs before taking snapshot.

####### properties

- Schema name: `Properties`
- Type: object
- Default: {}

Object mapping ZFS property names to values to set on the snapshot.

####### naming_schema (required)

- Schema name: `Naming Schema`
- Type: string

Naming schema pattern to generate the snapshot name automatically.
- Must be at least `1` characters long

### Return value

- Type: object

Information about the newly created snapshot.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
