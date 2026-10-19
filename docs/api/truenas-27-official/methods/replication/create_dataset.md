---
title: replication.create_dataset
kind: method
source_rst: _sources/api_methods_replication.create_dataset.rst.txt
source_html: api_methods_replication.create_dataset.html
required_roles:
  - REPLICATION_TASK_WRITE
---

# replication.create_dataset

## Summary

Creates dataset on remote side.

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

#### Parameter 1: dataset

<a id="Call_parameters_items_i0"></a>
#### dataset

- Schema name: `dataset`
- Type: string

Name of the dataset to create.

#### Parameter 2: transport

<a id="Call_parameters_items_i1"></a>
#### transport

- Schema name: `transport`
- Type: enum (of string)

Transport method to use for dataset creation.
##### Must be one of:

- "SSH"
- "SSH+NETCAT"
- "LOCAL"

#### Parameter 3: ssh_credentials

<a id="Call_parameters_items_i2"></a>
#### ssh_credentials

- Schema name: `ssh_credentials`
- Default: null

Keychain credential ID for SSH access. `null` for local transport.
<a id="Call_parameters_items_i2_anyOf"></a>
##### Any of

<a id="tab-pane_Call_parameters_items_i2_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i2_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i2_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i2_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful dataset creation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
