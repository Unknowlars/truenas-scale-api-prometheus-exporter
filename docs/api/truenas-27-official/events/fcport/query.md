---
title: fcport.query
kind: event
source_rst: _sources/api_events_fcport.query.rst.txt
source_html: api_events_fcport.query.html
required_roles:
  - SHARING_ISCSI_TARGET_READ
---

# fcport.query

## Summary

Sent on fcport changes.

## Required Roles

- `SHARING_ISCSI_TARGET_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `FCPortAddedEvent`
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

- Schema name: `FCPortEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Fibre Channel port configuration.

<a id="headingADDED_fields_port"></a>
<a id="ADDED_fields_port"></a>
##### port (required)

- Schema name: `Port`
- Type: string

Alias name for the Fibre Channel port, or `alias/number` for an NPIV port.
- Must match regular expression: `^[a-zA-Z0-9,\-_:]+(/[1-9][0-9]*)?$`
- Must be at least `1` characters long
- Must be at most `40` characters long

<a id="headingADDED_fields_wwpn"></a>
<a id="ADDED_fields_wwpn"></a>
##### wwpn (required)

- Schema name: `Wwpn`

World Wide Port Name for port A or `null` if not configured.
<a id="ADDED_fields_wwpn_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_wwpn_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_wwpn_anyOf_i0)

- Type: string
- Must match regular expression: `^naa.[0-9a-fA-F]{16}$`

<a id="tab-pane_ADDED_fields_wwpn_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_wwpn_anyOf_i1)

- Type: null

<a id="headingADDED_fields_wwpn_b"></a>
<a id="ADDED_fields_wwpn_b"></a>
##### wwpn_b (required)

- Schema name: `Wwpn B`

World Wide Port Name for port B or `null` if not configured.
<a id="ADDED_fields_wwpn_b_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_wwpn_b_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_wwpn_b_anyOf_i0)

- Type: string
- Must match regular expression: `^naa.[0-9a-fA-F]{16}$`

<a id="tab-pane_ADDED_fields_wwpn_b_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_wwpn_b_anyOf_i1)

- Type: null

<a id="headingADDED_fields_target"></a>
<a id="ADDED_fields_target"></a>
##### target (required)

- Schema name: `Target`

Target configuration object or `null` if not configured.
<a id="ADDED_fields_target_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_target_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_target_anyOf_i0)

- Type: object

<a id="tab-pane_ADDED_fields_target_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_target_anyOf_i1)

- Type: null

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `FCPortChangedEvent`
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

- Schema name: `FCPortEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Fibre Channel port configuration.

<a id="headingCHANGED_fields_port"></a>
<a id="CHANGED_fields_port"></a>
##### port (required)

- Schema name: `Port`
- Type: string

Alias name for the Fibre Channel port, or `alias/number` for an NPIV port.
- Must match regular expression: `^[a-zA-Z0-9,\-_:]+(/[1-9][0-9]*)?$`
- Must be at least `1` characters long
- Must be at most `40` characters long

<a id="headingCHANGED_fields_wwpn"></a>
<a id="CHANGED_fields_wwpn"></a>
##### wwpn (required)

- Schema name: `Wwpn`

World Wide Port Name for port A or `null` if not configured.
<a id="CHANGED_fields_wwpn_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_wwpn_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_wwpn_anyOf_i0)

- Type: string
- Must match regular expression: `^naa.[0-9a-fA-F]{16}$`

<a id="tab-pane_CHANGED_fields_wwpn_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_wwpn_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_wwpn_b"></a>
<a id="CHANGED_fields_wwpn_b"></a>
##### wwpn_b (required)

- Schema name: `Wwpn B`

World Wide Port Name for port B or `null` if not configured.
<a id="CHANGED_fields_wwpn_b_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_wwpn_b_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_wwpn_b_anyOf_i0)

- Type: string
- Must match regular expression: `^naa.[0-9a-fA-F]{16}$`

<a id="tab-pane_CHANGED_fields_wwpn_b_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_wwpn_b_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_target"></a>
<a id="CHANGED_fields_target"></a>
##### target (required)

- Schema name: `Target`

Target configuration object or `null` if not configured.
<a id="CHANGED_fields_target_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_target_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_target_anyOf_i0)

- Type: object

<a id="tab-pane_CHANGED_fields_target_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_target_anyOf_i1)

- Type: null

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `FCPortRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
