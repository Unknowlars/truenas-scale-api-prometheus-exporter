---
title: app.container_console_choices
kind: method
source_rst: _sources/api_methods_app.container_console_choices.rst.txt
source_html: api_methods_app.container_console_choices.html
required_roles:
  - APPS_READ | READONLY_ADMIN
---

# app.container_console_choices

## Summary

Returns container console choices for `app_name`.

## Required Roles

- `APPS_READ | READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: app_name

#### app_name

- Schema name: `app_name`
- Type: string

Name of the application to get console choices for.
- Must be at least `1` characters long

### Return value

- Schema name: `AppContainerResponse`
- Type: object

Object containing container choices available for console access.
#### Additional Properties

Each additional property must conform to the following schema
- Schema name: `ContainerDetails`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the container.
- Must be at least `1` characters long

##### service_name (required)

- Schema name: `Service Name`
- Type: string

Name of the service this container provides.
- Must be at least `1` characters long

##### image (required)

- Schema name: `Image`
- Type: string

Docker image name and tag used by this container.
- Must be at least `1` characters long

##### state (required)

- Schema name: `State`
- Type: enum (of string)

Current state of the container.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
