---
title: iscsi.initiator.update
kind: method
source_rst: _sources/api_methods_iscsi.initiator.update.rst.txt
source_html: api_methods_iscsi.initiator.update.html
required_roles:
  - SHARING_ISCSI_INITIATOR_WRITE
---

# iscsi.initiator.update

## Summary

Update iSCSI initiator of `id`.

## Required Roles

- `SHARING_ISCSI_INITIATOR_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the authorized initiator group to update.

#### Parameter 2: iscsi_initiator_update

#### iscsi_initiator_update

- Schema name: `iscsi_initiator_update`
- Type: object

Updated authorized initiator group configuration data.
- No Additional Properties
##### id

- Schema name: `Id`
- Type: integer

Unique identifier for the authorized initiator group.

##### initiators

- Schema name: `Initiators`
- Type: array of string

Array of iSCSI Qualified Names (IQNs) or IP addresses of authorized initiators.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### comment

- Schema name: `Comment`
- Type: string

Optional comment describing the authorized initiator group.

### Return value

- Schema name: `IscsiInitiatorEntry`
- Type: object

The updated authorized initiator group configuration.
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
