---
title: vm.device.usb_passthrough_choices
kind: method
source_rst: _sources/api_methods_vm.device.usb_passthrough_choices.rst.txt
source_html: api_methods_vm.device.usb_passthrough_choices.html
required_roles:
  - READONLY_ADMIN | VM_DEVICE_READ
---

# vm.device.usb_passthrough_choices

## Summary

Available choices for USB passthrough devices.

## Required Roles

- `READONLY_ADMIN | VM_DEVICE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `USBPassthroughInfo`
- Type: object

Object of available USB devices for passthrough with their detailed information.
#### Additional Properties

Each additional property must conform to the following schema
- Schema name: `USBPassthroughDevice`
- Type: object
- No Additional Properties
##### capability (required)

- Schema name: `USBCapability`
- Type: object

USB device capability and identification information.
- No Additional Properties
###### product (required)

- Schema name: `Product`

USB product name. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### product_id (required)

- Schema name: `Product Id`

USB product identifier. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### vendor (required)

- Schema name: `Vendor`

USB vendor name. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### vendor_id (required)

- Schema name: `Vendor Id`

USB vendor identifier. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### bus (required)

- Schema name: `Bus`

USB bus number. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### device (required)

- Schema name: `Device`

USB device number on bus. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

##### available (required)

- Schema name: `Available`
- Type: boolean

Whether the USB device is available for passthrough to virtual machines.

##### error (required)

- Schema name: `Error`

Error message if the device cannot be used for passthrough. `null` if no error.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
