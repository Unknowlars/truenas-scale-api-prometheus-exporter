---
title: vm.device.create
kind: method
source_rst: _sources/api_methods_vm.device.create.rst.txt
source_html: api_methods_vm.device.create.html
required_roles:
  - VM_DEVICE_WRITE
---

# vm.device.create

## Summary

Create a new device for the VM of id `vm`.

If `attributes.dtype` is the `RAW` type and a new raw file is to be created, `attributes.exists` will be passed as false. This means the API handles creating the raw file and raises the appropriate exception if file creation fails.

If `attributes.dtype` is of `DISK` type and a new Zvol is to be created, `attributes.create_zvol` will be passed as true with valid `attributes.zvol_name` and `attributes.zvol_volsize` values.

## Required Roles

- `VM_DEVICE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: vm_device_create

#### vm_device_create

- Schema name: `vm_device_create`
- Type: object

VMDeviceCreateArgs parameters.
- No Additional Properties
##### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.

##### vm (required)

- Schema name: `Vm`
- Type: integer

ID of the virtual machine this device belongs to.

##### order

- Schema name: `Order`
- Default: null

Boot order priority for this device. `null` for automatic assignment.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

### Return value

- Schema name: `VMDeviceEntry`
- Type: object

The newly created VM device configuration.
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
