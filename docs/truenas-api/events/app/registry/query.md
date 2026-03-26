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

### ADDED

- Schema name: `AppRegistryAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `AppRegistryEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the container registry configuration.

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

##### uri (required)

- Schema name: `Uri`
- Type: string

Container registry URI endpoint.

### CHANGED

- Schema name: `AppRegistryChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `AppRegistryEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the container registry configuration.

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

##### uri (required)

- Schema name: `Uri`
- Type: string

Container registry URI endpoint.

### REMOVED

- Schema name: `AppRegistryRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
