---
title: vm.maximum_supported_vcpus
kind: method
source_rst: _sources/api_methods_vm.maximum_supported_vcpus.rst.txt
source_html: api_methods_vm.maximum_supported_vcpus.html
required_roles:
  - VM_READ
---

# vm.maximum_supported_vcpus

## Summary

Returns maximum supported VCPU's.

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

- Schema name: `Result`
- Type: integer

Maximum number of virtual CPUs supported by the host system.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
