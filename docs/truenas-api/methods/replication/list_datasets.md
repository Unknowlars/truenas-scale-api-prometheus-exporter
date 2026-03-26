---
title: replication.list_datasets
kind: method
source_rst: _sources/api_methods_replication.list_datasets.rst.txt
source_html: api_methods_replication.list_datasets.html
required_roles:
  - REPLICATION_TASK_WRITE
---

# replication.list_datasets

## Summary

List datasets on remote side

## Required Roles

- `REPLICATION_TASK_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: transport

#### transport

- Schema name: `transport`
- Type: enum (of string)

Transport method to use for listing datasets.

#### Parameter 2: ssh_credentials

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
- Type: array of string

Array of dataset names available for replication.
- No Additional Items

#### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
