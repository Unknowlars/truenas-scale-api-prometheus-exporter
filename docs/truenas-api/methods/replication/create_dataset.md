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

Creates dataset on remote side

## Required Roles

- `REPLICATION_TASK_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: dataset

#### dataset

- Schema name: `dataset`
- Type: string

Name of the dataset to create.

#### Parameter 2: transport

#### transport

- Schema name: `transport`
- Type: enum (of string)

Transport method to use for dataset creation.

#### Parameter 3: ssh_credentials

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
- Type: null

Returns `null` on successful dataset creation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
