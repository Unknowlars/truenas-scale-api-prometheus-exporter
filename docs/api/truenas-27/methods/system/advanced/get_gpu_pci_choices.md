---
title: system.advanced.get_gpu_pci_choices
kind: method
source_rst: _sources/api_methods_system.advanced.get_gpu_pci_choices.rst.txt
source_html: api_methods_system.advanced.get_gpu_pci_choices.html
required_roles:
  - READONLY_ADMIN
  - SYSTEM_ADVANCED_READ
---

# system.advanced.get_gpu_pci_choices

## Summary

This endpoint gives all the gpu pci ids/slots that can be isolated.

## Required Roles

- `READONLY_ADMIN`
- `SYSTEM_ADVANCED_READ`

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
- Type: object

Available GPU PCI devices that can be isolated for VM passthrough.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
