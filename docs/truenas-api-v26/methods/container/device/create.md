---
title: container.device.create
kind: method
source_rst: _sources/api_methods_container.device.create.rst.txt
source_html: api_methods_container.device.create.html
required_roles:
  - CONTAINER_DEVICE_WRITE
---

# container.device.create

## Summary

Create a new device for the container of id `container`.

## Required Roles

- `CONTAINER_DEVICE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: container_device_create

#### container_device_create

- Schema name: `container_device_create`
- Type: object

ContainerDeviceCreateArgs parameters.
- No Additional Properties
##### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.

##### container (required)

- Schema name: `Container`
- Type: integer

ID of the container this device belongs to.

### Return value

- Schema name: `ContainerDeviceEntry`
- Type: object

The newly created container device configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the containers device.

#### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.

#### container (required)

- Schema name: `Container`
- Type: integer

ID of the container this device belongs to.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
