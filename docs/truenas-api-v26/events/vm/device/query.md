---
title: vm.device.query
kind: event
source_rst: _sources/api_events_vm.device.query.rst.txt
source_html: api_events_vm.device.query.html
required_roles:
  - VM_DEVICE_READ
---

# vm.device.query

## Summary

Sent on vm.device changes.

## Required Roles

- `VM_DEVICE_READ`

## Schema

- Type: object

### ADDED

- Schema name: `VMDeviceAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `VMDeviceEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the VM device.

##### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.

##### vm (required)

- Schema name: `Vm`
- Type: integer

ID of the virtual machine this device belongs to.

##### order (required)

- Schema name: `Order`
- Type: integer

Boot order priority for this device (lower numbers boot first).

### CHANGED

- Schema name: `VMDeviceChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `VMDeviceEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the VM device.

##### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.

##### vm (required)

- Schema name: `Vm`
- Type: integer

ID of the virtual machine this device belongs to.

##### order (required)

- Schema name: `Order`
- Type: integer

Boot order priority for this device (lower numbers boot first).

### REMOVED

- Schema name: `VMDeviceRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
