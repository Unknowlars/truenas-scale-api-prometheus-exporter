---
title: container.device.update
kind: method
source_rst: _sources/api_methods_container.device.update.rst.txt
source_html: api_methods_container.device.update.html
required_roles:
  - CONTAINER_DEVICE_WRITE
---

# container.device.update

## Summary

Update a container device of `id`.

## Required Roles

- `CONTAINER_DEVICE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the container device to update.

#### Parameter 2: container_device_update

#### container_device_update

- Schema name: `container_device_update`
- Type: object

Updated configuration for the container device.
- No Additional Properties
##### attributes

- Schema name: `Attributes`
- Type: object

Device-specific configuration attributes.

##### container

- Schema name: `Container`
- Type: integer

ID of the container this device belongs to.

### Return value

- Schema name: `ContainerDeviceEntry`
- Type: object

The updated container device configuration.
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
