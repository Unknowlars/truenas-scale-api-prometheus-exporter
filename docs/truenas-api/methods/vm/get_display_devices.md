---
title: vm.get_display_devices
kind: method
source_rst: _sources/api_methods_vm.get_display_devices.rst.txt
source_html: api_methods_vm.get_display_devices.html
required_roles:
  - VM_READ
---

# vm.get_display_devices

## Summary

Get the display devices from a given guest. If a display device has password configured, `attributes.password_configured` will be set to `true`.

## Required Roles

- `VM_READ`

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

ID of the virtual machine to get display devices for.

### Return value

- Schema name: `Result`
- Type: array of object

Array of display devices configured for the virtual machine.
- No Additional Items

#### Each item of this array must be:

#### DisplayDevice

- Schema name: `DisplayDevice`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the VM device.

##### attributes (required)

- Schema name: `GetDisplayDevice`
- Type: object

Display device attributes including password configuration status.
- No Additional Properties
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for display/graphics devices.

###### resolution

- Schema name: `Resolution`
- Type: enum (of string)
- Default: "1024x768"

Screen resolution for the virtual display.

###### port

- Schema name: `Port`
- Default: null

VNC/SPICE port number for remote display access. `null` for auto-assignment.
####### Any of

######## Option 1

- Type: integer
- Value must be greater or equal to `5900` and lesser or equal to `65535`

######## Option 2

- Type: null

###### web_port

- Schema name: `Web Port`
- Default: null

Web-based display access port number. `null` for auto-assignment.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

###### bind

- Schema name: `Bind`
- Type: string
- Default: "127.0.0.1"

IP address to bind the display server to.
- Must be at least `1` characters long

###### wait

- Schema name: `Wait`
- Type: boolean
- Default: false

Whether to wait for a client connection before starting the VM.

###### password

- Schema name: `Password`
- Default: null

Password for display server authentication.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### web

- Schema name: `Web`
- Type: boolean
- Default: true

Whether to enable web-based display access.

###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "SPICE"

Display protocol type.

###### password_configured (required)

- Schema name: `Password Configured`
- Type: boolean

Whether a password has been configured for display access.

##### vm (required)

- Schema name: `Vm`
- Type: integer

ID of the virtual machine this device belongs to.

##### order (required)

- Schema name: `Order`
- Type: integer

Boot order priority for this device (lower numbers boot first).

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
