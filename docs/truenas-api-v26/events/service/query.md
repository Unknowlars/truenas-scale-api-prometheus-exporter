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

### ADDED

- Schema name: `ServiceAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `ServiceEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the service.

##### service (required)

- Schema name: `Service`
- Type: string

Name of the system service.

##### enable (required)

- Schema name: `Enable`
- Type: boolean

Whether the service is enabled to start on boot.

##### state (required)

- Schema name: `State`
- Type: string

Current state of the service (e.g., 'RUNNING', 'STOPPED').

##### pids (required)

- Schema name: `Pids`
- Type: array of integer

Array of process IDs associated with this service.
- No Additional Items

###### Each item of this array must be:

- Type: integer

### CHANGED

- Schema name: `ServiceChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `ServiceEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the service.

##### service (required)

- Schema name: `Service`
- Type: string

Name of the system service.

##### enable (required)

- Schema name: `Enable`
- Type: boolean

Whether the service is enabled to start on boot.

##### state (required)

- Schema name: `State`
- Type: string

Current state of the service (e.g., 'RUNNING', 'STOPPED').

##### pids (required)

- Schema name: `Pids`
- Type: array of integer

Array of process IDs associated with this service.
- No Additional Items

###### Each item of this array must be:

- Type: integer

### REMOVED

- Schema name: `ServiceRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
