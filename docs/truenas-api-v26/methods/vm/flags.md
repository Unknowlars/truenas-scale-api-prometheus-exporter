---
title: vm.flags
kind: method
source_rst: _sources/api_methods_vm.flags.rst.txt
source_html: api_methods_vm.flags.html
required_roles:
  - VM_READ
---

# vm.flags

## Summary

Returns a dictionary with CPU flags for the hypervisor.

## Required Roles

- `VM_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `VMFlagsResult`
- Type: object

VMFlagsResult return fields.
- No Additional Properties
#### intel_vmx (required)

- Schema name: `Intel Vmx`
- Type: boolean

Whether Intel VT-x (VMX) virtualization is available.

#### unrestricted_guest (required)

- Schema name: `Unrestricted Guest`
- Type: boolean

Whether Intel unrestricted guest mode is supported.

#### amd_rvi (required)

- Schema name: `Amd Rvi`
- Type: boolean

Whether AMD Rapid Virtualization Indexing (RVI/NPT) is available.

#### amd_asids (required)

- Schema name: `Amd Asids`
- Type: boolean

Whether AMD Address Space Identifiers (ASIDs) are supported.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
