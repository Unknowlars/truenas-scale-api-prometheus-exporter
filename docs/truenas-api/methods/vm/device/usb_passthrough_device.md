---
title: vm.device.usb_passthrough_device
kind: method
source_rst: _sources/api_methods_vm.device.usb_passthrough_device.rst.txt
source_html: api_methods_vm.device.usb_passthrough_device.html
required_roles:
  - VM_DEVICE_READ
---

# vm.device.usb_passthrough_device

## Summary

Retrieve details about `device` USB device.

## Required Roles

- `VM_DEVICE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: device

#### device

- Schema name: `device`
- Type: string

USB device identifier to get passthrough information for.
- Must be at least `1` characters long

### Return value

- Schema name: `USBPassthroughDevice`
- Type: object

Detailed information about the specified USB passthrough device.
- No Additional Properties
#### capability (required)

- Schema name: `USBCapability`
- Type: object

USB device capability and identification information.
- No Additional Properties
##### product (required)

- Schema name: `Product`

USB product name. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### product_id (required)

- Schema name: `Product Id`

USB product identifier. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### vendor (required)

- Schema name: `Vendor`

USB vendor name. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### vendor_id (required)

- Schema name: `Vendor Id`

USB vendor identifier. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### bus (required)

- Schema name: `Bus`

USB bus number. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### device (required)

- Schema name: `Device`

USB device number on bus. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

#### available (required)

- Schema name: `Available`
- Type: boolean

Whether the USB device is available for passthrough to virtual machines.

#### error (required)

- Schema name: `Error`

Error message if the device cannot be used for passthrough. `null` if no error.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
