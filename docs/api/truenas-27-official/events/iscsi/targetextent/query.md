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

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `iSCSITargetToExtentAddedEvent`
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

- Schema name: `iSCSITargetToExtentEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the target-to-extent association.

<a id="headingADDED_fields_target"></a>
<a id="ADDED_fields_target"></a>
##### target (required)

- Schema name: `Target`
- Type: integer

ID of the iSCSI target to associate with the extent.

<a id="headingADDED_fields_lunid"></a>
<a id="ADDED_fields_lunid"></a>
##### lunid (required)

- Schema name: `Lunid`
- Type: integer

Logical Unit Number (LUN) ID for presenting the extent to the target.

<a id="headingADDED_fields_extent"></a>
<a id="ADDED_fields_extent"></a>
##### extent (required)

- Schema name: `Extent`
- Type: integer

ID of the iSCSI extent to associate with the target.

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `iSCSITargetToExtentChangedEvent`
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

- Schema name: `iSCSITargetToExtentEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the target-to-extent association.

<a id="headingCHANGED_fields_target"></a>
<a id="CHANGED_fields_target"></a>
##### target (required)

- Schema name: `Target`
- Type: integer

ID of the iSCSI target to associate with the extent.

<a id="headingCHANGED_fields_lunid"></a>
<a id="CHANGED_fields_lunid"></a>
##### lunid (required)

- Schema name: `Lunid`
- Type: integer

Logical Unit Number (LUN) ID for presenting the extent to the target.

<a id="headingCHANGED_fields_extent"></a>
<a id="CHANGED_fields_extent"></a>
##### extent (required)

- Schema name: `Extent`
- Type: integer

ID of the iSCSI extent to associate with the target.

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `iSCSITargetToExtentRemovedEvent`
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
