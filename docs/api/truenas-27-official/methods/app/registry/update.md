---
title: app.registry.update
kind: method
source_rst: _sources/api_methods_app.registry.update.rst.txt
source_html: api_methods_app.registry.update.html
required_roles:
  - APPS_WRITE
---

# app.registry.update

## Summary

Update an app registry entry.

## Required Roles

- `APPS_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the container registry to update.

#### Parameter 2: data

<a id="Call_parameters_items_i1"></a>
#### data

- Schema name: `data`
- Type: object

Updated container registry configuration data.
- No Additional Properties
<a id="headingCall_parameters_items_i1_name"></a>
<a id="Call_parameters_items_i1_name"></a>
##### name

- Schema name: `Name`
- Type: string

Human-readable name for the container registry.

<a id="headingCall_parameters_items_i1_description"></a>
<a id="Call_parameters_items_i1_description"></a>
##### description

- Schema name: `Description`

Optional description of the container registry or `null`.
<a id="Call_parameters_items_i1_description_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_description_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_description_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_description_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_description_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_username"></a>
<a id="Call_parameters_items_i1_username"></a>
##### username

- Schema name: `Username`
- Type: string

Username for registry authentication (masked for security).

<a id="headingCall_parameters_items_i1_password"></a>
<a id="Call_parameters_items_i1_password"></a>
##### password

- Schema name: `Password`
- Type: string

Password or access token for registry authentication (masked for security).

<a id="headingCall_parameters_items_i1_uri"></a>
<a id="Call_parameters_items_i1_uri"></a>
##### uri

- Schema name: `Uri`
- Type: string

Container registry URI endpoint (defaults to Docker Hub).

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `AppRegistryEntry`
- Type: object

The updated container registry configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the container registry configuration.

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the container registry.

<a id="headingReturn_value_description"></a>
<a id="Return_value_description"></a>
#### description

- Schema name: `Description`
- Default: null

Optional description of the container registry or `null`.
<a id="Return_value_description_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_description_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_description_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_description_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_description_anyOf_i1)

- Type: null

<a id="headingReturn_value_username"></a>
<a id="Return_value_username"></a>
#### username (required)

- Schema name: `Username`
- Type: string

Username for registry authentication (masked for security).

<a id="headingReturn_value_password"></a>
<a id="Return_value_password"></a>
#### password (required)

- Schema name: `Password`
- Type: string

Password or access token for registry authentication (masked for security).

<a id="headingReturn_value_uri"></a>
<a id="Return_value_uri"></a>
#### uri (required)

- Schema name: `Uri`
- Type: string

Container registry URI endpoint.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
