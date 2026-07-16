---
title: iscsi.portal.query
kind: event
source_rst: _sources/api_events_iscsi.portal.query.rst.txt
source_html: api_events_iscsi.portal.query.html
required_roles:
  - SHARING_ISCSI_PORTAL_READ
---

# iscsi.portal.query

## Summary

Sent on iscsi.portal changes.

## Required Roles

- `SHARING_ISCSI_PORTAL_READ`

## Schema

- Type: object

### ADDED

- Schema name: `IscsiPortalAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `IscsiPortalEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI portal.

##### listen (required)

- Schema name: `Listen`
- Type: array of object

Array of IP address and port combinations for the portal to listen on.
- No Additional Items

###### Each item of this array must be:

###### IscsiPortalIPInfo

- Schema name: `IscsiPortalIPInfo`
- Type: object
- No Additional Properties
####### ip (required)

- Schema name: `Ip`
- Type: string

IP address for the iSCSI portal to listen on.
- Must be at least `1` characters long

####### port (required)

- Schema name: `Port`
- Type: integer

TCP port number for the iSCSI portal.

##### tag (required)

- Schema name: `Tag`
- Type: integer

Numeric tag used to associate this portal with iSCSI targets.

##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the portal.

### CHANGED

- Schema name: `IscsiPortalChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `IscsiPortalEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI portal.

##### listen (required)

- Schema name: `Listen`
- Type: array of object

Array of IP address and port combinations for the portal to listen on.
- No Additional Items

###### Each item of this array must be:

###### IscsiPortalIPInfo

- Schema name: `IscsiPortalIPInfo`
- Type: object
- No Additional Properties
####### ip (required)

- Schema name: `Ip`
- Type: string

IP address for the iSCSI portal to listen on.
- Must be at least `1` characters long

####### port (required)

- Schema name: `Port`
- Type: integer

TCP port number for the iSCSI portal.

##### tag (required)

- Schema name: `Tag`
- Type: integer

Numeric tag used to associate this portal with iSCSI targets.

##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the portal.

### REMOVED

- Schema name: `IscsiPortalRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
