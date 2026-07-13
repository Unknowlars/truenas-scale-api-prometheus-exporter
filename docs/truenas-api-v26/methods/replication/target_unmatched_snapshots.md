---
title: replication.target_unmatched_snapshots
kind: method
source_rst: _sources/api_methods_replication.target_unmatched_snapshots.rst.txt
source_html: api_methods_replication.target_unmatched_snapshots.html
required_roles:
  - REPLICATION_TASK_WRITE
---

# replication.target_unmatched_snapshots

## Summary

Check if target has any snapshots that do not exist on source. Returns these snapshots grouped by dataset.

## Required Roles

- `REPLICATION_TASK_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: direction

#### direction

- Schema name: `direction`
- Type: enum (of string)

Direction of replication to check for unmatched snapshots.

#### Parameter 2: source_datasets

#### source_datasets

- Schema name: `source_datasets`
- Type: array of string

Array of source dataset names.
- Must contain a minimum of `1` items
- No Additional Items

##### Each item of this array must be:

- Type: string

#### Parameter 3: target_dataset

#### target_dataset

- Schema name: `target_dataset`
- Type: string

Target dataset name to check for unmatched snapshots.

#### Parameter 4: transport

#### transport

- Schema name: `transport`
- Type: enum (of string)

Transport method to use for accessing snapshots.

#### Parameter 5: ssh_credentials

#### ssh_credentials

- Schema name: `ssh_credentials`
- Default: null

Keychain credential ID for SSH access. `null` for local transport.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: object

Object mapping dataset names to arrays of unmatched snapshot names on the target side.
Examples:

```json
{
    "backup/games": [
        "auto-2019-10-15_13-00"
    ],
    "backup/work": [
        "auto-2019-10-15_13-00",
        "auto-2019-10-15_09-00"
    ]
}
```
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
