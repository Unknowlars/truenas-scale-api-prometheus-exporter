---
title: iscsi.targetextent.query
kind: event
source_rst: _sources/api_events_iscsi.targetextent.query.rst.txt
source_html: api_events_iscsi.targetextent.query.html
required_roles:
  - SHARING_ISCSI_TARGETEXTENT_READ
---

# iscsi.targetextent.query

## Summary

Sent on iscsi.targetextent changes.

## Required Roles

- `SHARING_ISCSI_TARGETEXTENT_READ`

## Schema

- Type: object

### ADDED

- Schema name: `IscsiTargetToExtentAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `IscsiTargetToExtentEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the target-to-extent association.

##### target (required)

- Schema name: `Target`
- Type: integer

ID of the iSCSI target to associate with the extent.

##### lunid (required)

- Schema name: `Lunid`
- Type: integer

Logical Unit Number (LUN) ID for presenting the extent to the target.

##### extent (required)

- Schema name: `Extent`
- Type: integer

ID of the iSCSI extent to associate with the target.

### CHANGED

- Schema name: `IscsiTargetToExtentChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `IscsiTargetToExtentEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the target-to-extent association.

##### target (required)

- Schema name: `Target`
- Type: integer

ID of the iSCSI target to associate with the extent.

##### lunid (required)

- Schema name: `Lunid`
- Type: integer

Logical Unit Number (LUN) ID for presenting the extent to the target.

##### extent (required)

- Schema name: `Extent`
- Type: integer

ID of the iSCSI extent to associate with the target.

### REMOVED

- Schema name: `IscsiTargetToExtentRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
