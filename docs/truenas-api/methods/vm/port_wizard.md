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

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `VMPortWizardResult`
- Type: object

VMPortWizardResult return fields.
- No Additional Properties
#### port (required)

- Schema name: `Port`
- Type: integer

Available server port

#### web (required)

- Schema name: `Web`
- Type: integer

Web port to be used based on available port

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
