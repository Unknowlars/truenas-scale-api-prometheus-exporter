---
title: alert.list
kind: method
source_rst: _sources/api_methods_alert.list.rst.txt
source_html: api_methods_alert.list.html
required_roles:
  - ALERT_LIST_READ
---

# alert.list

## Summary

List all types of alerts including active/dismissed currently in the system.

## Required Roles

- `ALERT_LIST_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of object

Array of all current alerts in the system.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### Alert

- Schema name: `Alert`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_id"></a>
<a id="Return_value_items_id"></a>
##### id (required)

- Schema name: `Id`
- Type: string

Alert identifier used for API operations.

<a id="headingReturn_value_items_uuid"></a>
<a id="Return_value_items_uuid"></a>
##### uuid (required)

- Schema name: `Uuid`
- Type: string

Unique identifier for the alert.

<a id="headingReturn_value_items_source"></a>
<a id="Return_value_items_source"></a>
##### source (required)

- Schema name: `Source`
- Type: string

Source component that generated the alert.

<a id="headingReturn_value_items_klass"></a>
<a id="Return_value_items_klass"></a>
##### klass (required)

- Schema name: `Klass`
- Type: string

Alert class identifier for categorization.

<a id="headingReturn_value_items_args"></a>
<a id="Return_value_items_args"></a>
##### args (required)

- Schema name: `Args`
- Type: object

Arguments and parameters specific to the alert type.

<a id="headingReturn_value_items_node"></a>
<a id="Return_value_items_node"></a>
##### node (required)

- Schema name: `Node`
- Type: string

Node identifier in HA systems or hostname for single-node systems.

<a id="headingReturn_value_items_key"></a>
<a id="Return_value_items_key"></a>
##### key (required)

- Schema name: `Key`
- Type: string

Unique key used for alert deduplication and identification.
- Must be at most `2147483647` characters long

<a id="headingReturn_value_items_datetime"></a>
<a id="Return_value_items_datetime"></a>
##### datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Timestamp when the alert was first created.

<a id="headingReturn_value_items_last_occurrence"></a>
<a id="Return_value_items_last_occurrence"></a>
##### last_occurrence (required)

- Schema name: `Last Occurrence`
- Type: string
- Type: Format: date-time

Timestamp of the most recent occurrence of this alert.

<a id="headingReturn_value_items_dismissed"></a>
<a id="Return_value_items_dismissed"></a>
##### dismissed (required)

- Schema name: `Dismissed`
- Type: boolean

Whether the alert has been manually dismissed by a user.

<a id="headingReturn_value_items_mail"></a>
<a id="Return_value_items_mail"></a>
##### mail (required)

- Schema name: `Mail`
- Type: object

Email notification configuration and status for this alert.

<a id="headingReturn_value_items_text"></a>
<a id="Return_value_items_text"></a>
##### text (required)

- Schema name: `Text`
- Type: string

Human-readable description of the alert.
- Must be at most `2147483647` characters long

<a id="headingReturn_value_items_level"></a>
<a id="Return_value_items_level"></a>
##### level (required)

- Schema name: `Level`
- Type: string

Severity level of the alert (INFO, WARNING, ERROR, etc.).

<a id="headingReturn_value_items_formatted"></a>
<a id="Return_value_items_formatted"></a>
##### formatted (required)

- Schema name: `Formatted`

Formatted alert message with HTML.
<a id="Return_value_items_formatted_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_formatted_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_formatted_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_items_formatted_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_formatted_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_one_shot"></a>
<a id="Return_value_items_one_shot"></a>
##### one_shot (required)

- Schema name: `One Shot`
- Type: boolean

Whether this alert will not be dismissed automatically.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
