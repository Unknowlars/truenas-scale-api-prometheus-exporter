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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: count_eligible_manual_snapshots

<a id="Call_parameters_items_i0"></a>
#### count_eligible_manual_snapshots

- Schema name: `count_eligible_manual_snapshots`
- Type: object

ReplicationCountEligibleManualSnapshotsArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_datasets"></a>
<a id="Call_parameters_items_i0_datasets"></a>
##### datasets (required)

- Schema name: `Datasets`
- Type: array of string

Array of dataset names to count snapshots for.
- Must contain a minimum of `1` items
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_datasets_items"></a>
- Type: string

<a id="headingCall_parameters_items_i0_naming_schema"></a>
<a id="Call_parameters_items_i0_naming_schema"></a>
##### naming_schema

- Schema name: `Naming Schema`
- Type: array of string
- Default: []

Array of naming schema patterns to match against.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_naming_schema_items"></a>
- Type: string

<a id="headingCall_parameters_items_i0_name_regex"></a>
<a id="Call_parameters_items_i0_name_regex"></a>
##### name_regex

- Schema name: `Name Regex`
- Default: null

Regular expression to match snapshot names. `null` to match all names.
<a id="Call_parameters_items_i0_name_regex_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_name_regex_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_name_regex_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_name_regex_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_name_regex_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_transport"></a>
<a id="Call_parameters_items_i0_transport"></a>
##### transport (required)

- Schema name: `Transport`
- Type: enum (of string)

Transport method to use for accessing snapshots.
###### Must be one of:

- "SSH"
- "SSH+NETCAT"
- "LOCAL"

<a id="headingCall_parameters_items_i0_ssh_credentials"></a>
<a id="Call_parameters_items_i0_ssh_credentials"></a>
##### ssh_credentials

- Schema name: `Ssh Credentials`
- Default: null

Keychain credential ID for SSH access. `null` for local transport.
<a id="Call_parameters_items_i0_ssh_credentials_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_ssh_credentials_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_ssh_credentials_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i0_ssh_credentials_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_ssh_credentials_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `ReplicationCountEligibleManualSnapshotsResult`
- Type: object

ReplicationCountEligibleManualSnapshotsResult return fields.
- No Additional Properties
<a id="headingReturn_value_total"></a>
<a id="Return_value_total"></a>
#### total (required)

- Schema name: `Total`
- Type: integer

Total number of snapshots found.

<a id="headingReturn_value_eligible"></a>
<a id="Return_value_eligible"></a>
#### eligible (required)

- Schema name: `Eligible`
- Type: integer

Number of snapshots eligible for replication.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
