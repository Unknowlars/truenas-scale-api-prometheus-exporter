---
title: app.container_console_choices
kind: method
source_rst: _sources/api_methods_app.container_console_choices.rst.txt
source_html: api_methods_app.container_console_choices.html
required_roles:
  - APPS_READ
  - READONLY_ADMIN
---

# app.container_console_choices

## Summary

Returns container console choices for `app_name`.

## Required Roles

- `APPS_READ`
- `READONLY_ADMIN`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: app_name

<a id="Call_parameters_items_i0"></a>
#### app_name

- Schema name: `app_name`
- Type: string

Name of the application to get console choices for.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `AppContainerResponse`
- Type: object

Object containing container choices available for console access.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Schema name: `ContainerDetails`
- Type: object
- No Additional Properties
<a id="headingReturn_value_additionalProperties_id"></a>
<a id="Return_value_additionalProperties_id"></a>
##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the container.
- Must be at least `1` characters long

<a id="headingReturn_value_additionalProperties_service_name"></a>
<a id="Return_value_additionalProperties_service_name"></a>
##### service_name (required)

- Schema name: `Service Name`
- Type: string

Name of the service this container provides.
- Must be at least `1` characters long

<a id="headingReturn_value_additionalProperties_image"></a>
<a id="Return_value_additionalProperties_image"></a>
##### image (required)

- Schema name: `Image`
- Type: string

Docker image name and tag used by this container.
- Must be at least `1` characters long

<a id="headingReturn_value_additionalProperties_state"></a>
<a id="Return_value_additionalProperties_state"></a>
##### state (required)

- Schema name: `State`
- Type: enum (of string)

Current state of the container.
###### Must be one of:

- "crashed"
- "created"
- "exited"
- "running"
- "starting"

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
