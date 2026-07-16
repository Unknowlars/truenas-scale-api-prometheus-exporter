---
title: container.device.query
kind: event
source_rst: _sources/api_events_container.device.query.rst.txt
source_html: api_events_container.device.query.html
required_roles:
  - CONTAINER_DEVICE_READ
---

# container.device.query

## Summary

Sent on container.device changes.

## Required Roles

- `CONTAINER_DEVICE_READ`

## Schema

- Type: object

### ADDED

- Schema name: `ContainerDeviceAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `ContainerDeviceEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the containers device.

##### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.

##### container (required)

- Schema name: `Container`
- Type: integer

ID of the container this device belongs to.

### CHANGED

- Schema name: `ContainerDeviceChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `ContainerDeviceEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the containers device.

##### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.

##### container (required)

- Schema name: `Container`
- Type: integer

ID of the container this device belongs to.

### REMOVED

- Schema name: `ContainerDeviceRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
