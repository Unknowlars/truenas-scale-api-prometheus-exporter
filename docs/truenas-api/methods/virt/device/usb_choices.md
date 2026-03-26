---
title: virt.device.usb_choices
kind: method
source_rst: _sources/api_methods_virt.device.usb_choices.rst.txt
source_html: api_methods_virt.device.usb_choices.html
required_roles:
  - READONLY_ADMIN | VIRT_INSTANCE_READ
---

# virt.device.usb_choices

## Summary

Provide choices for USB devices.

## Required Roles

- `READONLY_ADMIN | VIRT_INSTANCE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Object of available USB devices with their hardware information.
#### Additional Properties

Each additional property must conform to the following schema
- Schema name: `USBChoice`
- Type: object
- No Additional Properties
##### vendor_id (required)

- Schema name: `Vendor Id`
- Type: string

USB vendor identifier for this device.

##### product_id (required)

- Schema name: `Product Id`
- Type: string

USB product identifier for this device.

##### bus (required)

- Schema name: `Bus`
- Type: integer

USB bus number where this device is connected.

##### dev (required)

- Schema name: `Dev`
- Type: integer

USB device number on the bus.

##### product (required)

- Schema name: `Product`

Product name of the USB device. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### manufacturer (required)

- Schema name: `Manufacturer`

Manufacturer name of the USB device. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
