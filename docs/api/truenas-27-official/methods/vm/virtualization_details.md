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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `VMVirtualizationDetailsResult`
- Type: object

VMVirtualizationDetailsResult return fields.
- No Additional Properties
<a id="headingReturn_value_supported"></a>
<a id="Return_value_supported"></a>
#### supported (required)

- Schema name: `Supported`
- Type: boolean

Whether hardware virtualization is supported and available.

<a id="headingReturn_value_error"></a>
<a id="Return_value_error"></a>
#### error (required)

- Schema name: `Error`

Error message if virtualization is not available. `null` if supported.
<a id="Return_value_error_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_error_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_error_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_error_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
