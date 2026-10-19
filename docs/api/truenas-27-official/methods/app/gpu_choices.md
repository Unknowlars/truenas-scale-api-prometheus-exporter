---
title: app.gpu_choices
kind: method
source_rst: _sources/api_methods_app.gpu_choices.rst.txt
source_html: api_methods_app.gpu_choices.html
required_roles:
  - APPS_READ
  - READONLY_ADMIN
---

# app.gpu_choices

## Summary

Returns GPU choices which can be used by applications.

## Required Roles

- `APPS_READ`
- `READONLY_ADMIN`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `AppGPUResponse`
- Type: object

Object mapping GPU identifiers to their detailed information.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Schema name: `GPU`
- Type: object
- No Additional Properties
<a id="headingReturn_value_additionalProperties_vendor"></a>
<a id="Return_value_additionalProperties_vendor"></a>
##### vendor (required)

- Schema name: `Vendor`

GPU vendor name. `null` if not detected.
<a id="Return_value_additionalProperties_vendor_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_additionalProperties_vendor_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_additionalProperties_vendor_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_additionalProperties_vendor_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_additionalProperties_vendor_anyOf_i1)

- Type: null

Examples:

```json
"NVIDIA"
```
Examples:

```json
"AMD"
```
Examples:

```json
"Intel"
```

<a id="headingReturn_value_additionalProperties_description"></a>
<a id="Return_value_additionalProperties_description"></a>
##### description (required)

- Schema name: `Description`

Human-readable description of the GPU device. `null` if not available.
<a id="Return_value_additionalProperties_description_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_additionalProperties_description_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_additionalProperties_description_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_additionalProperties_description_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_additionalProperties_description_anyOf_i1)

- Type: null

<a id="headingReturn_value_additionalProperties_error"></a>
<a id="Return_value_additionalProperties_error"></a>
##### error (required)

- Schema name: `Error`

Error message if the GPU cannot be accessed or configured. `null` if no errors.
<a id="Return_value_additionalProperties_error_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_additionalProperties_error_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_additionalProperties_error_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_additionalProperties_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_additionalProperties_error_anyOf_i1)

- Type: null

<a id="headingReturn_value_additionalProperties_vendor_specific_config"></a>
<a id="Return_value_additionalProperties_vendor_specific_config"></a>
##### vendor_specific_config (required)

- Schema name: `Vendor Specific Config`
- Type: object

Configuration options specific to the GPU vendor.

<a id="headingReturn_value_additionalProperties_gpu_details"></a>
<a id="Return_value_additionalProperties_gpu_details"></a>
##### gpu_details (required)

- Schema name: `Gpu Details`
- Type: object

Detailed information about the GPU hardware and capabilities.

<a id="headingReturn_value_additionalProperties_pci_slot"></a>
<a id="Return_value_additionalProperties_pci_slot"></a>
##### pci_slot (required)

- Schema name: `Pci Slot`

PCI slot identifier where the GPU is installed. `null` if not available.
<a id="Return_value_additionalProperties_pci_slot_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_additionalProperties_pci_slot_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_additionalProperties_pci_slot_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_additionalProperties_pci_slot_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_additionalProperties_pci_slot_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
