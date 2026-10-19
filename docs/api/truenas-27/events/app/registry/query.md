---
title: app.registry.query
kind: event
source_rst: _sources/api_events_app.registry.query.rst.txt
source_html: api_events_app.registry.query.html
required_roles:
  - APPS_READ
---

# app.registry.query

## Summary

Sent on app.registry changes.

## Required Roles

- `APPS_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `AppRegistryAddedEvent`
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

- Schema name: `AppRegistryEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the container registry configuration.

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the container registry.

<a id="headingADDED_fields_description"></a>
<a id="ADDED_fields_description"></a>
##### description

- Schema name: `Description`
- Default: null

Optional description of the container registry or `null`.
<a id="ADDED_fields_description_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_description_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_description_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_description_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_description_anyOf_i1)

- Type: null

<a id="headingADDED_fields_username"></a>
<a id="ADDED_fields_username"></a>
##### username (required)

- Schema name: `Username`
- Type: string

Username for registry authentication (masked for security).

<a id="headingADDED_fields_password"></a>
<a id="ADDED_fields_password"></a>
##### password (required)

- Schema name: `Password`
- Type: string

Password or access token for registry authentication (masked for security).

<a id="headingADDED_fields_uri"></a>
<a id="ADDED_fields_uri"></a>
##### uri (required)

- Schema name: `Uri`
- Type: string

Container registry URI endpoint.

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `AppRegistryChangedEvent`
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

- Schema name: `AppRegistryEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the container registry configuration.

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the container registry.

<a id="headingCHANGED_fields_description"></a>
<a id="CHANGED_fields_description"></a>
##### description

- Schema name: `Description`
- Default: null

Optional description of the container registry or `null`.
<a id="CHANGED_fields_description_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_description_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_description_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_description_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_description_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_username"></a>
<a id="CHANGED_fields_username"></a>
##### username (required)

- Schema name: `Username`
- Type: string

Username for registry authentication (masked for security).

<a id="headingCHANGED_fields_password"></a>
<a id="CHANGED_fields_password"></a>
##### password (required)

- Schema name: `Password`
- Type: string

Password or access token for registry authentication (masked for security).

<a id="headingCHANGED_fields_uri"></a>
<a id="CHANGED_fields_uri"></a>
##### uri (required)

- Schema name: `Uri`
- Type: string

Container registry URI endpoint.

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `AppRegistryRemovedEvent`
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
