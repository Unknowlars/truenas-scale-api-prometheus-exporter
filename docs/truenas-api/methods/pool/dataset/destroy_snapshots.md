---
title: pool.dataset.destroy_snapshots
kind: method
source_rst: _sources/api_methods_pool.dataset.destroy_snapshots.rst.txt
source_html: api_methods_pool.dataset.destroy_snapshots.html
required_roles:
  - SNAPSHOT_WRITE
---

# pool.dataset.destroy_snapshots

## Summary

Destroy specified snapshots of a given dataset.

This method is a job.

*DEPRECATED: this method is scheduled to be removed in v26.04.*

## Required Roles

- `SNAPSHOT_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: name

#### name

- Schema name: `name`
- Type: string

The dataset name to destroy snapshots for.

#### Parameter 2: snapshots

#### snapshots

- Schema name: `snapshots`
- Type: object

Specification of which snapshots to destroy (all, specific ones, or ranges).
- No Additional Properties
##### all

- Schema name: `All`
- Type: boolean
- Default: false

Whether to destroy all snapshots for the dataset.

##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively destroy snapshots of child datasets.

##### snapshots

- Schema name: `Snapshots`
- Type: array
- Default: []

Array of specific snapshot names or snapshot range specifications to destroy.
- No Additional Items

###### Each item of this array must be:

####### Any of

######## PoolDatasetDestroySnapshotsArgsSnapshotSpec

- Schema name: `PoolDatasetDestroySnapshotsArgsSnapshotSpec`
- Type: object
- No Additional Properties
######### start

- Schema name: `Start`
- Default: null

Starting snapshot name for the range. Null to start from the beginning.
########## Any of

########### Option 1

- Type: string

########### Option 2

- Type: null

######### end

- Schema name: `End`
- Default: null

Ending snapshot name for the range. Null to continue to the end.
########## Any of

########### Option 1

- Type: string

########### Option 2

- Type: null

######## Option 2

- Type: string

######## Option 1

- Type: null

######## Option 2

- Type: string

######## Option 1

- Type: null

######## Option 2

- Type: string

### Return value

- Schema name: `Result`
- Type: array of string

Array of snapshot names that were successfully destroyed.
- No Additional Items

#### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
