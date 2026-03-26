---
title: app.gpu_choices
kind: method
source_rst: _sources/api_methods_app.gpu_choices.rst.txt
source_html: api_methods_app.gpu_choices.html
required_roles:
  - APPS_READ | READONLY_ADMIN
---

# app.gpu_choices

## Summary

Returns GPU choices which can be used by applications.

## Required Roles

- `APPS_READ | READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `AppGPUResponse`
- Type: object

Object mapping GPU identifiers to their detailed information.
#### Additional Properties

Each additional property must conform to the following schema
- Schema name: `GPU`
- Type: object
- No Additional Properties
##### vendor (required)

- Schema name: `Vendor`

GPU vendor name. `null` if not detected.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

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

##### description (required)

- Schema name: `Description`

Human-readable description of the GPU device. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### error (required)

- Schema name: `Error`

Error message if the GPU cannot be accessed or configured. `null` if no errors.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### vendor_specific_config (required)

- Schema name: `Vendor Specific Config`
- Type: object

Configuration options specific to the GPU vendor.

##### gpu_details (required)

- Schema name: `Gpu Details`
- Type: object

Detailed information about the GPU hardware and capabilities.

##### pci_slot (required)

- Schema name: `Pci Slot`

PCI slot identifier where the GPU is installed. `null` if not available.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
