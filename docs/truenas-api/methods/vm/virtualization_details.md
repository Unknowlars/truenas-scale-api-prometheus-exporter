---
title: vm.virtualization_details
kind: method
source_rst: _sources/api_methods_vm.virtualization_details.rst.txt
source_html: api_methods_vm.virtualization_details.html
required_roles:
  - VM_READ
---

# vm.virtualization_details

## Summary

Retrieve details if virtualization is supported on the system and in case why it's not supported if it isn't.

## Required Roles

- `VM_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `VMVirtualizationDetailsResult`
- Type: object

VMVirtualizationDetailsResult return fields.
- No Additional Properties
#### supported (required)

- Schema name: `Supported`
- Type: boolean

Whether hardware virtualization is supported and available.

#### error (required)

- Schema name: `Error`

Error message if virtualization is not available. `null` if supported.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
