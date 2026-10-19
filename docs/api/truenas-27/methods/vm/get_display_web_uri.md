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

ID of the virtual machine to get display web URI for.

#### Parameter 2: host

<a id="Call_parameters_items_i1"></a>
#### host

- Schema name: `host`
- Type: string
- Default: ""

Hostname or IP address to use in the URI. Empty string for automatic detection.

#### Parameter 3: options

<a id="Call_parameters_items_i2"></a>
#### options

- Schema name: `options`
- Type: object
- Default: {"protocol": "HTTP"}

Options for generating the web display URI.
- No Additional Properties
<a id="headingCall_parameters_items_i2_protocol"></a>
<a id="Call_parameters_items_i2_protocol"></a>
##### protocol

- Schema name: `Protocol`
- Type: enum (of string)
- Default: "HTTP"

Protocol to use for the web display URI (HTTP or HTTPS).
###### Must be one of:

- "HTTP"
- "HTTPS"

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `VMGetDisplayWebUriResult`
- Type: object

VMGetDisplayWebUriResult return fields.
- No Additional Properties
<a id="headingReturn_value_error"></a>
<a id="Return_value_error"></a>
#### error (required)

- Schema name: `Error`

Error message if URI generation failed. `null` on success.
<a id="Return_value_error_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_error_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_error_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_error_anyOf_i1)

- Type: null

<a id="headingReturn_value_uri"></a>
<a id="Return_value_uri"></a>
#### uri (required)

- Schema name: `Uri`

Generated web URI for accessing the VM display. `null` on error.
<a id="Return_value_uri_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_uri_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_uri_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_uri_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_uri_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
