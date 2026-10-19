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

Get the display devices from a given guest.

## Required Roles

- `VM_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the virtual machine to get display devices for.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of object

Array of display devices configured for the virtual machine.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### DisplayDevice

- Schema name: `DisplayDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_id"></a>
<a id="Return_value_items_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the VM device.

<a id="headingReturn_value_items_attributes"></a>
<a id="Return_value_items_attributes"></a>
##### attributes (required)

- Schema name: `GetDisplayDevice`
- Type: object

Display device attributes including password configuration status.
- No Additional Properties
<a id="headingReturn_value_items_attributes_dtype"></a>
<a id="Return_value_items_attributes_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for display/graphics devices.
- Specific value: `"DISPLAY"`

<a id="headingReturn_value_items_attributes_resolution"></a>
<a id="Return_value_items_attributes_resolution"></a>
###### resolution

- Schema name: `Resolution`
- Type: enum (of string)
- Default: "1024x768"

Screen resolution for the virtual display.
###### Must be one of:

- "1920x1200"
- "1920x1080"
- "1600x1200"
- "1600x900"
- "1400x1050"
- "1280x1024"
- "1280x720"
- "1024x768"
- "800x600"
- "640x480"

<a id="headingReturn_value_items_attributes_port"></a>
<a id="Return_value_items_attributes_port"></a>
###### port

- Schema name: `Port`
- Default: null

VNC/SPICE port number for remote display access. `null` for auto-assignment.
<a id="Return_value_items_attributes_port_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_attributes_port_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_attributes_port_anyOf_i0)

- Type: integer
- Value must be greater or equal to `5900` and lesser or equal to `65535`

<a id="tab-pane_Return_value_items_attributes_port_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_attributes_port_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_attributes_web_port"></a>
<a id="Return_value_items_attributes_web_port"></a>
###### web_port

- Schema name: `Web Port`
- Default: null

Web-based display access port number. `null` for auto-assignment.
<a id="Return_value_items_attributes_web_port_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_attributes_web_port_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_attributes_web_port_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_attributes_web_port_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_attributes_web_port_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_attributes_bind"></a>
<a id="Return_value_items_attributes_bind"></a>
###### bind

- Schema name: `Bind`
- Type: string
- Default: "127.0.0.1"

IP address to bind the display server to.
- Must be at least `1` characters long

<a id="headingReturn_value_items_attributes_wait"></a>
<a id="Return_value_items_attributes_wait"></a>
###### wait

- Schema name: `Wait`
- Type: boolean
- Default: false

Whether to wait for a client connection before starting the VM.

<a id="headingReturn_value_items_attributes_password"></a>
<a id="Return_value_items_attributes_password"></a>
###### password

- Schema name: `Password`
- Default: ""

Password for display server authentication.
<a id="Return_value_items_attributes_password_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_attributes_password_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_attributes_password_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_attributes_password_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_attributes_password_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_attributes_web"></a>
<a id="Return_value_items_attributes_web"></a>
###### web

- Schema name: `Web`
- Type: boolean
- Default: true

Whether to enable web-based display access.

<a id="headingReturn_value_items_attributes_type"></a>
<a id="Return_value_items_attributes_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "SPICE"

Display protocol type.
###### Must be one of:

- "SPICE"
- "VNC"

<a id="headingReturn_value_items_attributes_password_configured"></a>
<a id="Return_value_items_attributes_password_configured"></a>
###### password_configured (required)

- Schema name: `Password Configured`
- Type: boolean

Whether a password has been configured for display access.

<a id="headingReturn_value_items_vm"></a>
<a id="Return_value_items_vm"></a>
##### vm (required)

- Schema name: `Vm`
- Type: integer

ID of the virtual machine this device belongs to.

<a id="headingReturn_value_items_order"></a>
<a id="Return_value_items_order"></a>
##### order (required)

- Schema name: `Order`
- Type: integer

Boot order priority for this device (lower numbers boot first).

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
