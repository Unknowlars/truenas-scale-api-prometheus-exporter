---
title: fc.fc_host.query
kind: event
source_rst: _sources/api_events_fc.fc_host.query.rst.txt
source_html: api_events_fc.fc_host.query.html
required_roles:
  - SHARING_ISCSI_TARGET_READ
---

# fc.fc_host.query

## Summary

Sent on fc.fc_host changes.

## Required Roles

- `SHARING_ISCSI_TARGET_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `FCHostAddedEvent`
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

- Schema name: `FCHostEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Fibre Channel host configuration.

<a id="headingADDED_fields_alias"></a>
<a id="ADDED_fields_alias"></a>
##### alias (required)

- Schema name: `Alias`
- Type: string

Human-readable alias for the Fibre Channel host.
- Must match regular expression: `^[a-zA-Z0-9,\-_:]+$`
- Must be at least `1` characters long
- Must be at most `32` characters long

<a id="headingADDED_fields_wwpn"></a>
<a id="ADDED_fields_wwpn"></a>
##### wwpn

- Schema name: `Wwpn`
- Default: null

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
##### wwpn_b

- Schema name: `Wwpn B`
- Default: null

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

<a id="headingADDED_fields_npiv"></a>
<a id="ADDED_fields_npiv"></a>
##### npiv

- Schema name: `Npiv`
- Type: integer
- Default: 0

Number of N_Port ID Virtualization (NPIV) virtual ports to create.

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `FCHostChangedEvent`
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

- Schema name: `FCHostEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Fibre Channel host configuration.

<a id="headingCHANGED_fields_alias"></a>
<a id="CHANGED_fields_alias"></a>
##### alias (required)

- Schema name: `Alias`
- Type: string

Human-readable alias for the Fibre Channel host.
- Must match regular expression: `^[a-zA-Z0-9,\-_:]+$`
- Must be at least `1` characters long
- Must be at most `32` characters long

<a id="headingCHANGED_fields_wwpn"></a>
<a id="CHANGED_fields_wwpn"></a>
##### wwpn

- Schema name: `Wwpn`
- Default: null

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
##### wwpn_b

- Schema name: `Wwpn B`
- Default: null

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

<a id="headingCHANGED_fields_npiv"></a>
<a id="CHANGED_fields_npiv"></a>
##### npiv

- Schema name: `Npiv`
- Type: integer
- Default: 0

Number of N_Port ID Virtualization (NPIV) virtual ports to create.

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `FCHostRemovedEvent`
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
