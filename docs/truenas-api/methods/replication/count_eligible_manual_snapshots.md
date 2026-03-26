---
title: replication.count_eligible_manual_snapshots
kind: method
source_rst: _sources/api_methods_replication.count_eligible_manual_snapshots.rst.txt
source_html: api_methods_replication.count_eligible_manual_snapshots.html
required_roles:
  - REPLICATION_TASK_WRITE
---

# replication.count_eligible_manual_snapshots

## Summary

Count how many existing snapshots of `dataset` match `naming_schema`.

## Required Roles

- `REPLICATION_TASK_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: count_eligible_manual_snapshots

#### count_eligible_manual_snapshots

- Schema name: `count_eligible_manual_snapshots`
- Type: object

ReplicationCountEligibleManualSnapshotsArgs parameters.
- No Additional Properties
##### datasets (required)

- Schema name: `Datasets`
- Type: array of string

Array of dataset names to count snapshots for.
- Must contain a minimum of `1` items
- No Additional Items

###### Each item of this array must be:

- Type: string

##### naming_schema

- Schema name: `Naming Schema`
- Type: array of string
- Default: []

Array of naming schema patterns to match against.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### name_regex

- Schema name: `Name Regex`
- Default: null

Regular expression to match snapshot names. `null` to match all names.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### transport (required)

- Schema name: `Transport`
- Type: enum (of string)

Transport method to use for accessing snapshots.

##### ssh_credentials

- Schema name: `Ssh Credentials`
- Default: null

Keychain credential ID for SSH access. `null` for local transport.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

### Return value

- Schema name: `ReplicationCountEligibleManualSnapshotsResult`
- Type: object

ReplicationCountEligibleManualSnapshotsResult return fields.
- No Additional Properties
#### total (required)

- Schema name: `Total`
- Type: integer

Total number of snapshots found.

#### eligible (required)

- Schema name: `Eligible`
- Type: integer

Number of snapshots eligible for replication.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
