---
title: service.query
kind: event
source_rst: _sources/api_events_service.query.rst.txt
source_html: api_events_service.query.html
required_roles:
  - SERVICE_READ
---

# service.query

## Summary

Sent on service changes.

## Required Roles

- `SERVICE_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `ServiceAddedEvent`
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

- Schema name: `ServiceEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the service.

<a id="headingADDED_fields_service"></a>
<a id="ADDED_fields_service"></a>
##### service (required)

- Schema name: `Service`
- Type: string

Name of the system service.

<a id="headingADDED_fields_enable"></a>
<a id="ADDED_fields_enable"></a>
##### enable (required)

- Schema name: `Enable`
- Type: boolean

Whether the service is enabled to start on boot.

<a id="headingADDED_fields_state"></a>
<a id="ADDED_fields_state"></a>
##### state (required)

- Schema name: `State`
- Type: string

Current state of the service (e.g., 'RUNNING', 'STOPPED').

<a id="headingADDED_fields_pids"></a>
<a id="ADDED_fields_pids"></a>
##### pids (required)

- Schema name: `Pids`
- Type: array of integer

Array of process IDs associated with this service.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_pids_items"></a>
- Type: integer

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `ServiceChangedEvent`
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

- Schema name: `ServiceEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the service.

<a id="headingCHANGED_fields_service"></a>
<a id="CHANGED_fields_service"></a>
##### service (required)

- Schema name: `Service`
- Type: string

Name of the system service.

<a id="headingCHANGED_fields_enable"></a>
<a id="CHANGED_fields_enable"></a>
##### enable (required)

- Schema name: `Enable`
- Type: boolean

Whether the service is enabled to start on boot.

<a id="headingCHANGED_fields_state"></a>
<a id="CHANGED_fields_state"></a>
##### state (required)

- Schema name: `State`
- Type: string

Current state of the service (e.g., 'RUNNING', 'STOPPED').

<a id="headingCHANGED_fields_pids"></a>
<a id="CHANGED_fields_pids"></a>
##### pids (required)

- Schema name: `Pids`
- Type: array of integer

Array of process IDs associated with this service.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_pids_items"></a>
- Type: integer

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `ServiceRemovedEvent`
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
