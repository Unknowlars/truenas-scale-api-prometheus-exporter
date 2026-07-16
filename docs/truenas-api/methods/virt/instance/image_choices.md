---
title: virt.instance.image_choices
kind: method
source_rst: _sources/api_methods_virt.instance.image_choices.rst.txt
source_html: api_methods_virt.instance.image_choices.html
required_roles:
  - READONLY_ADMIN | VIRT_INSTANCE_READ
---

# virt.instance.image_choices

## Summary

Provide choices for instance image from a remote repository.

## Required Roles

- `READONLY_ADMIN | VIRT_INSTANCE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: virt_instances_image_choices

#### virt_instances_image_choices

- Schema name: `virt_instances_image_choices`
- Type: object
- Default: {"remote": "LINUX_CONTAINERS"}

Options for filtering available images.
- No Additional Properties
##### remote

- Schema name: `Remote`
- Type: const
- Default: "LINUX_CONTAINERS"

Remote image source to query for available images.

### Return value

- Schema name: `Result`
- Type: object

Available images indexed by image identifier.
#### Additional Properties

Each additional property must conform to the following schema
- Schema name: `ImageChoiceItem`
- Type: object
- No Additional Properties
##### label (required)

- Schema name: `Label`
- Type: string

Human-readable label for the image.

##### os (required)

- Schema name: `Os`
- Type: string

Operating system family of the image.

##### release (required)

- Schema name: `Release`
- Type: string

Version or release name of the operating system.

##### archs (required)

- Schema name: `Archs`
- Type: array of string

Array of supported hardware architectures.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### variant (required)

- Schema name: `Variant`
- Type: string

Image variant (default, cloud, minimal, etc.).

##### instance_types (required)

- Schema name: `Instance Types`
- Type: array of enum (of string)

Array of instance types this image supports.
- No Additional Items

###### Each item of this array must be:

- Type: enum (of string)

##### secureboot (required)

- Schema name: `Secureboot`

Whether the image supports UEFI Secure Boot or `null` if not applicable.
###### Any of

####### Option 1

- Type: boolean

####### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
