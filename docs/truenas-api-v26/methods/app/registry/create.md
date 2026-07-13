---
title: app.registry.create
kind: method
source_rst: _sources/api_methods_app.registry.create.rst.txt
source_html: api_methods_app.registry.create.html
required_roles:
  - APPS_WRITE
---

# app.registry.create

## Summary

Create an app registry entry.

## Required Roles

- `APPS_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: app_registry_create

#### app_registry_create

- Schema name: `app_registry_create`
- Type: object

Container registry configuration data for the new registry.
- No Additional Properties
##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the container registry.

##### description

- Schema name: `Description`
- Default: null

Optional description of the container registry or `null`.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### username (required)

- Schema name: `Username`
- Type: string

Username for registry authentication (masked for security).

##### password (required)

- Schema name: `Password`
- Type: string

Password or access token for registry authentication (masked for security).

##### uri

- Schema name: `Uri`
- Type: string
- Default: "https://index.docker.io/v1/"

Container registry URI endpoint (defaults to Docker Hub).

### Return value

- Schema name: `AppRegistryEntry`
- Type: object

The created container registry configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the container registry configuration.

#### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the container registry.

#### description

- Schema name: `Description`
- Default: null

Optional description of the container registry or `null`.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### username (required)

- Schema name: `Username`
- Type: string

Username for registry authentication (masked for security).

#### password (required)

- Schema name: `Password`
- Type: string

Password or access token for registry authentication (masked for security).

#### uri (required)

- Schema name: `Uri`
- Type: string

Container registry URI endpoint.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
