---
title: iscsi.initiator.create
kind: method
source_rst: _sources/api_methods_iscsi.initiator.create.rst.txt
source_html: api_methods_iscsi.initiator.create.html
required_roles:
  - SHARING_ISCSI_INITIATOR_WRITE
---

# iscsi.initiator.create

## Summary

Create an iSCSI Initiator.

`initiators` is a list of initiator hostnames which are authorized to access an iSCSI Target. To allow all possible initiators, `initiators` can be left empty.

## Required Roles

- `SHARING_ISCSI_INITIATOR_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: iscsi_initiator_create

#### iscsi_initiator_create

- Schema name: `iscsi_initiator_create`
- Type: object

Authorized initiator group configuration data for creation.
- No Additional Properties
##### initiators

- Schema name: `Initiators`
- Type: array of string
- Default: []

Array of iSCSI Qualified Names (IQNs) or IP addresses of authorized initiators.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the authorized initiator group.

### Return value

- Schema name: `IscsiInitiatorEntry`
- Type: object

The created authorized initiator group configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the authorized initiator group.

#### initiators

- Schema name: `Initiators`
- Type: array of string
- Default: []

Array of iSCSI Qualified Names (IQNs) or IP addresses of authorized initiators.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the authorized initiator group.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
