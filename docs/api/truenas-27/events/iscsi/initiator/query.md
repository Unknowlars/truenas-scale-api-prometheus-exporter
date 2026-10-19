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

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `iSCSITargetAuthorizedInitiatorAddedEvent`
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

- Schema name: `iSCSITargetAuthorizedInitiatorEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the authorized initiator group.

<a id="headingADDED_fields_initiators"></a>
<a id="ADDED_fields_initiators"></a>
##### initiators

- Schema name: `Initiators`
- Type: array of string
- Default: []

Array of iSCSI Qualified Names (IQNs) or IP addresses of authorized initiators.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_initiators_items"></a>
- Type: string

<a id="headingADDED_fields_comment"></a>
<a id="ADDED_fields_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the authorized initiator group.

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `iSCSITargetAuthorizedInitiatorChangedEvent`
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

- Schema name: `iSCSITargetAuthorizedInitiatorEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the authorized initiator group.

<a id="headingCHANGED_fields_initiators"></a>
<a id="CHANGED_fields_initiators"></a>
##### initiators

- Schema name: `Initiators`
- Type: array of string
- Default: []

Array of iSCSI Qualified Names (IQNs) or IP addresses of authorized initiators.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_initiators_items"></a>
- Type: string

<a id="headingCHANGED_fields_comment"></a>
<a id="CHANGED_fields_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the authorized initiator group.

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `iSCSITargetAuthorizedInitiatorRemovedEvent`
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
