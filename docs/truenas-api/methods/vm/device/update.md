---
title: vm.device.update
kind: method
source_rst: _sources/api_methods_vm.device.update.rst.txt
source_html: api_methods_vm.device.update.html
required_roles:
  - VM_DEVICE_WRITE
---

# vm.device.update

## Summary

Update a VM device of `id`.

Pass `attributes.size` to resize a `dtype` `RAW` device. The raw file will be resized.

## Required Roles

- `VM_DEVICE_WRITE`

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

ID of the VM device to update.

#### Parameter 2: vm_device_update

#### vm_device_update

- Schema name: `vm_device_update`
- Type: object

Updated configuration for the VM device.
- No Additional Properties
##### attributes

- Schema name: `Attributes`
- Type: object

Device-specific configuration attributes.

##### vm

- Schema name: `Vm`
- Type: integer

ID of the virtual machine this device belongs to.

##### order

- Schema name: `Order`

Boot order priority for this device. `null` for automatic assignment.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

### Return value

- Schema name: `VMDeviceEntry`
- Type: object

The updated VM device configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the VM device.

#### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.

#### vm (required)

- Schema name: `Vm`
- Type: integer

ID of the virtual machine this device belongs to.

#### order (required)

- Schema name: `Order`
- Type: integer

Boot order priority for this device (lower numbers boot first).

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
