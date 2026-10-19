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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: direction

<a id="Call_parameters_items_i0"></a>
#### direction

- Schema name: `direction`
- Type: enum (of string)

Direction of replication to check for unmatched snapshots.
##### Must be one of:

- "PUSH"
- "PULL"

#### Parameter 2: source_datasets

<a id="Call_parameters_items_i1"></a>
#### source_datasets

- Schema name: `source_datasets`
- Type: array of string

Array of source dataset names.
- Must contain a minimum of `1` items
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i1_items"></a>
- Type: string

#### Parameter 3: target_dataset

<a id="Call_parameters_items_i2"></a>
#### target_dataset

- Schema name: `target_dataset`
- Type: string

Target dataset name to check for unmatched snapshots.

#### Parameter 4: transport

<a id="Call_parameters_items_i3"></a>
#### transport

- Schema name: `transport`
- Type: enum (of string)

Transport method to use for accessing snapshots.
##### Must be one of:

- "SSH"
- "SSH+NETCAT"
- "LOCAL"

#### Parameter 5: ssh_credentials

<a id="Call_parameters_items_i4"></a>
#### ssh_credentials

- Schema name: `ssh_credentials`
- Default: null

Keychain credential ID for SSH access. `null` for local transport.
<a id="Call_parameters_items_i4_anyOf"></a>
##### Any of

<a id="tab-pane_Call_parameters_items_i4_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i4_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i4_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i4_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
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
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Type: array of string
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_additionalProperties_items"></a>
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
