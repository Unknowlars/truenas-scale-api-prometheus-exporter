---
title: virt.device.gpu_choices
kind: method
source_rst: _sources/api_methods_virt.device.gpu_choices.rst.txt
source_html: api_methods_virt.device.gpu_choices.html
required_roles:
  - READONLY_ADMIN | VIRT_INSTANCE_READ
---

# virt.device.gpu_choices

## Summary

Provide choices for GPU devices.

## Required Roles

- `READONLY_ADMIN | VIRT_INSTANCE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: gpu_type

#### gpu_type

- Schema name: `gpu_type`
- Type: enum (of string)

Type of GPU virtualization to filter available choices.

### Return value

- Schema name: `Result`
- Type: object

Object of available GPU devices with their hardware information.
#### Additional Properties

Each additional property must conform to the following schema
- Schema name: `GPUChoice`
- Type: object
- No Additional Properties
##### bus (required)

- Schema name: `Bus`
- Type: string

PCI bus identifier for the GPU device.

##### slot (required)

- Schema name: `Slot`
- Type: string

PCI slot identifier for the GPU device.

##### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the GPU device.

##### vendor

- Schema name: `Vendor`
- Default: null

GPU vendor name. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### pci (required)

- Schema name: `Pci`
- Type: string

Complete PCI address of the GPU device.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
