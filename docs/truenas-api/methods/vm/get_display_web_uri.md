---
title: vm.get_display_web_uri
kind: method
source_rst: _sources/api_methods_vm.get_display_web_uri.rst.txt
source_html: api_methods_vm.get_display_web_uri.html
required_roles:
  - VM_READ
---

# vm.get_display_web_uri

## Summary

Retrieve Display URI for a given VM or appropriate error if there is no display device available or if it is not configured to use web interface

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

ID of the virtual machine to get display web URI for.

#### Parameter 2: host

#### host

- Schema name: `host`
- Type: string
- Default: ""

Hostname or IP address to use in the URI. Empty string for automatic detection.

#### Parameter 3: options

#### options

- Schema name: `options`
- Type: object
- Default: {"protocol": "HTTP"}

Options for generating the web display URI.
- No Additional Properties
##### protocol

- Schema name: `Protocol`
- Type: enum (of string)
- Default: "HTTP"

Protocol to use for the web display URI (HTTP or HTTPS).

### Return value

- Schema name: `VMGetDisplayWebUriResult`
- Type: object

VMGetDisplayWebUriResult return fields.
- No Additional Properties
#### error (required)

- Schema name: `Error`

Error message if URI generation failed. `null` on success.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### uri (required)

- Schema name: `Uri`

Generated web URI for accessing the VM display. `null` on error.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
