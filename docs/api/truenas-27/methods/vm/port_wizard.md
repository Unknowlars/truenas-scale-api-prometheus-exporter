---
title: vm.port_wizard
kind: method
source_rst: _sources/api_methods_vm.port_wizard.rst.txt
source_html: api_methods_vm.port_wizard.html
required_roles:
  - VM_READ
---

# vm.port_wizard

## Summary

It returns the next available Display Server Port and Web Port.

Returns a dict with two keys `port` and `web`.

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

- Schema name: `VMPortWizardResult`
- Type: object

VMPortWizardResult return fields.
- No Additional Properties
<a id="headingReturn_value_port"></a>
<a id="Return_value_port"></a>
#### port (required)

- Schema name: `Port`
- Type: integer

Available server port

<a id="headingReturn_value_web"></a>
<a id="Return_value_web"></a>
#### web (required)

- Schema name: `Web`
- Type: integer

Web port to be used based on available port

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
