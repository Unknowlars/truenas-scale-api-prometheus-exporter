---
title: iscsi.initiator.query
kind: event
source_rst: _sources/api_events_iscsi.initiator.query.rst.txt
source_html: api_events_iscsi.initiator.query.html
required_roles:
  - SHARING_ISCSI_INITIATOR_READ
---

# iscsi.initiator.query

## Summary

Sent on iscsi.initiator changes.

## Required Roles

- `SHARING_ISCSI_INITIATOR_READ`

## Schema

- Type: object

### ADDED

- Schema name: `IscsiInitiatorAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `IscsiInitiatorEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the authorized initiator group.

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

### CHANGED

- Schema name: `IscsiInitiatorChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `IscsiInitiatorEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the authorized initiator group.

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

### REMOVED

- Schema name: `IscsiInitiatorRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
