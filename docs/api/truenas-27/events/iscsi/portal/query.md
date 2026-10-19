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

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `ISCSIPortalAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `ISCSIPortalEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI portal.

<a id="headingADDED_fields_listen"></a>
<a id="ADDED_fields_listen"></a>
##### listen (required)

- Schema name: `Listen`
- Type: array of object

Array of IP address and port combinations for the portal to listen on.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_listen_items"></a>
###### IscsiPortalIPInfo

- Schema name: `IscsiPortalIPInfo`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_listen_items_ip"></a>
<a id="ADDED_fields_listen_items_ip"></a>
###### ip (required)

- Schema name: `Ip`
- Type: string

IP address for the iSCSI portal to listen on.
- Must be at least `1` characters long

<a id="headingADDED_fields_listen_items_port"></a>
<a id="ADDED_fields_listen_items_port"></a>
###### port (required)

- Schema name: `Port`
- Type: integer

TCP port number for the iSCSI portal.

<a id="headingADDED_fields_tag"></a>
<a id="ADDED_fields_tag"></a>
##### tag (required)

- Schema name: `Tag`
- Type: integer

Numeric tag used to associate this portal with iSCSI targets.

<a id="headingADDED_fields_comment"></a>
<a id="ADDED_fields_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the portal.

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `ISCSIPortalChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `ISCSIPortalEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI portal.

<a id="headingCHANGED_fields_listen"></a>
<a id="CHANGED_fields_listen"></a>
##### listen (required)

- Schema name: `Listen`
- Type: array of object

Array of IP address and port combinations for the portal to listen on.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_listen_items"></a>
###### IscsiPortalIPInfo

- Schema name: `IscsiPortalIPInfo`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_listen_items_ip"></a>
<a id="CHANGED_fields_listen_items_ip"></a>
###### ip (required)

- Schema name: `Ip`
- Type: string

IP address for the iSCSI portal to listen on.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_listen_items_port"></a>
<a id="CHANGED_fields_listen_items_port"></a>
###### port (required)

- Schema name: `Port`
- Type: integer

TCP port number for the iSCSI portal.

<a id="headingCHANGED_fields_tag"></a>
<a id="CHANGED_fields_tag"></a>
##### tag (required)

- Schema name: `Tag`
- Type: integer

Numeric tag used to associate this portal with iSCSI targets.

<a id="headingCHANGED_fields_comment"></a>
<a id="CHANGED_fields_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the portal.

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `ISCSIPortalRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
