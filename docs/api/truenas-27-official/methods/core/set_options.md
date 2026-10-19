---
title: core.set_options
kind: method
source_rst: _sources/api_methods_core.set_options.rst.txt
source_html: api_methods_core.set_options.html
required_roles:
  []
---

# core.set_options

## Summary

Set per-connection options for the current API session and return the resulting option values.

Options such as `legacy_jobs`, `private_methods`, and `py_exceptions` change how the middleware formats responses and errors for this connection only; they are not persisted beyond the session.

## Required Roles

- None documented.

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: options

<a id="Call_parameters_items_i0"></a>
#### options

- Schema name: `options`
- Type: object

Core system options to update.
<a id="headingCall_parameters_items_i0_legacy_jobs"></a>
<a id="Call_parameters_items_i0_legacy_jobs"></a>
##### legacy_jobs

- Schema name: `Legacy Jobs`
- Type: boolean

Whether to enable legacy job behavior for backward compatibility.

<a id="headingCall_parameters_items_i0_private_methods"></a>
<a id="Call_parameters_items_i0_private_methods"></a>
##### private_methods

- Schema name: `Private Methods`
- Type: boolean

Whether to expose private methods in API introspection.

<a id="headingCall_parameters_items_i0_py_exceptions"></a>
<a id="Call_parameters_items_i0_py_exceptions"></a>
##### py_exceptions

- Schema name: `Py Exceptions`
- Type: boolean

Whether to include Python exception details in error responses.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `CoreOptions`
- Type: object

The updated core system options.
<a id="headingReturn_value_legacy_jobs"></a>
<a id="Return_value_legacy_jobs"></a>
#### legacy_jobs

- Schema name: `Legacy Jobs`
- Type: boolean

Whether to enable legacy job behavior for backward compatibility.

<a id="headingReturn_value_private_methods"></a>
<a id="Return_value_private_methods"></a>
#### private_methods

- Schema name: `Private Methods`
- Type: boolean

Whether to expose private methods in API introspection.

<a id="headingReturn_value_py_exceptions"></a>
<a id="Return_value_py_exceptions"></a>
#### py_exceptions

- Schema name: `Py Exceptions`
- Type: boolean

Whether to include Python exception details in error responses.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
