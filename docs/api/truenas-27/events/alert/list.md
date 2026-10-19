---
title: alert.list
kind: event
source_rst: _sources/api_events_alert.list.rst.txt
source_html: api_events_alert.list.html
required_roles:
  - ALERT_LIST_READ
---

# alert.list

## Summary

Sent on alert changes.

## Required Roles

- `ALERT_LIST_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `AlertListAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Event identifier for the added alert.

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `Alert`
- Type: object

Complete alert data for the newly added alert.
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: string

Alert identifier used for API operations.

<a id="headingADDED_fields_uuid"></a>
<a id="ADDED_fields_uuid"></a>
##### uuid (required)

- Schema name: `Uuid`
- Type: string

Unique identifier for the alert.

<a id="headingADDED_fields_source"></a>
<a id="ADDED_fields_source"></a>
##### source (required)

- Schema name: `Source`
- Type: string

Source component that generated the alert.

<a id="headingADDED_fields_klass"></a>
<a id="ADDED_fields_klass"></a>
##### klass (required)

- Schema name: `Klass`
- Type: string

Alert class identifier for categorization.

<a id="headingADDED_fields_args"></a>
<a id="ADDED_fields_args"></a>
##### args (required)

- Schema name: `Args`
- Type: object

Arguments and parameters specific to the alert type.

<a id="headingADDED_fields_node"></a>
<a id="ADDED_fields_node"></a>
##### node (required)

- Schema name: `Node`
- Type: string

Node identifier in HA systems or hostname for single-node systems.

<a id="headingADDED_fields_key"></a>
<a id="ADDED_fields_key"></a>
##### key (required)

- Schema name: `Key`
- Type: string

Unique key used for alert deduplication and identification.

<a id="headingADDED_fields_datetime"></a>
<a id="ADDED_fields_datetime"></a>
##### datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Timestamp when the alert was first created.

<a id="headingADDED_fields_last_occurrence"></a>
<a id="ADDED_fields_last_occurrence"></a>
##### last_occurrence (required)

- Schema name: `Last Occurrence`
- Type: string
- Type: Format: date-time

Timestamp of the most recent occurrence of this alert.

<a id="headingADDED_fields_dismissed"></a>
<a id="ADDED_fields_dismissed"></a>
##### dismissed (required)

- Schema name: `Dismissed`
- Type: boolean

Whether the alert has been manually dismissed by a user.

<a id="headingADDED_fields_mail"></a>
<a id="ADDED_fields_mail"></a>
##### mail (required)

- Schema name: `Mail`
- Type: object

Email notification configuration and status for this alert.

<a id="headingADDED_fields_text"></a>
<a id="ADDED_fields_text"></a>
##### text (required)

- Schema name: `Text`
- Type: string

Human-readable description of the alert.

<a id="headingADDED_fields_level"></a>
<a id="ADDED_fields_level"></a>
##### level (required)

- Schema name: `Level`
- Type: string

Severity level of the alert (INFO, WARNING, ERROR, etc.).

<a id="headingADDED_fields_formatted"></a>
<a id="ADDED_fields_formatted"></a>
##### formatted (required)

- Schema name: `Formatted`

Formatted alert message with HTML.
<a id="ADDED_fields_formatted_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_formatted_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_formatted_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_formatted_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_formatted_anyOf_i1)

- Type: null

<a id="headingADDED_fields_one_shot"></a>
<a id="ADDED_fields_one_shot"></a>
##### one_shot (required)

- Schema name: `One Shot`
- Type: boolean

Whether this alert will not be dismissed automatically.

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `AlertListChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Event identifier for the changed alert.

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `Alert`
- Type: object

Updated alert data with changes.
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: string

Alert identifier used for API operations.

<a id="headingCHANGED_fields_uuid"></a>
<a id="CHANGED_fields_uuid"></a>
##### uuid (required)

- Schema name: `Uuid`
- Type: string

Unique identifier for the alert.

<a id="headingCHANGED_fields_source"></a>
<a id="CHANGED_fields_source"></a>
##### source (required)

- Schema name: `Source`
- Type: string

Source component that generated the alert.

<a id="headingCHANGED_fields_klass"></a>
<a id="CHANGED_fields_klass"></a>
##### klass (required)

- Schema name: `Klass`
- Type: string

Alert class identifier for categorization.

<a id="headingCHANGED_fields_args"></a>
<a id="CHANGED_fields_args"></a>
##### args (required)

- Schema name: `Args`
- Type: object

Arguments and parameters specific to the alert type.

<a id="headingCHANGED_fields_node"></a>
<a id="CHANGED_fields_node"></a>
##### node (required)

- Schema name: `Node`
- Type: string

Node identifier in HA systems or hostname for single-node systems.

<a id="headingCHANGED_fields_key"></a>
<a id="CHANGED_fields_key"></a>
##### key (required)

- Schema name: `Key`
- Type: string

Unique key used for alert deduplication and identification.

<a id="headingCHANGED_fields_datetime"></a>
<a id="CHANGED_fields_datetime"></a>
##### datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Timestamp when the alert was first created.

<a id="headingCHANGED_fields_last_occurrence"></a>
<a id="CHANGED_fields_last_occurrence"></a>
##### last_occurrence (required)

- Schema name: `Last Occurrence`
- Type: string
- Type: Format: date-time

Timestamp of the most recent occurrence of this alert.

<a id="headingCHANGED_fields_dismissed"></a>
<a id="CHANGED_fields_dismissed"></a>
##### dismissed (required)

- Schema name: `Dismissed`
- Type: boolean

Whether the alert has been manually dismissed by a user.

<a id="headingCHANGED_fields_mail"></a>
<a id="CHANGED_fields_mail"></a>
##### mail (required)

- Schema name: `Mail`
- Type: object

Email notification configuration and status for this alert.

<a id="headingCHANGED_fields_text"></a>
<a id="CHANGED_fields_text"></a>
##### text (required)

- Schema name: `Text`
- Type: string

Human-readable description of the alert.

<a id="headingCHANGED_fields_level"></a>
<a id="CHANGED_fields_level"></a>
##### level (required)

- Schema name: `Level`
- Type: string

Severity level of the alert (INFO, WARNING, ERROR, etc.).

<a id="headingCHANGED_fields_formatted"></a>
<a id="CHANGED_fields_formatted"></a>
##### formatted (required)

- Schema name: `Formatted`

Formatted alert message with HTML.
<a id="CHANGED_fields_formatted_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_formatted_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_formatted_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_formatted_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_formatted_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_one_shot"></a>
<a id="CHANGED_fields_one_shot"></a>
##### one_shot (required)

- Schema name: `One Shot`
- Type: boolean

Whether this alert will not be dismissed automatically.

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `AlertListRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Event identifier for the removed alert.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
