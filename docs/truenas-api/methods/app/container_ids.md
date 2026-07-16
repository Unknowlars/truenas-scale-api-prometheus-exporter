---
title: app.container_ids
kind: method
source_rst: _sources/api_methods_app.container_ids.rst.txt
source_html: api_methods_app.container_ids.html
required_roles:
  - APPS_READ
---

# app.container_ids

## Summary

Returns container IDs for `app_name`.

## Required Roles

- `APPS_READ`

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

Name of the application to get container IDs for.
- Must be at least `1` characters long

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object
- Default: {"alive_only": true}

Options for filtering the returned container list.
- No Additional Properties
##### alive_only

- Schema name: `Alive Only`
- Type: boolean
- Default: true

Whether to return only running/active containers (`true`) or include all containers (`false`).

### Return value

- Schema name: `AppContainerResponse`
- Type: object

Object containing container ID to details mappings.
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
