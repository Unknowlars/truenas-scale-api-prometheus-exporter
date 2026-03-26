---
title: virt.device.pci_choices
kind: method
source_rst: _sources/api_methods_virt.device.pci_choices.rst.txt
source_html: api_methods_virt.device.pci_choices.html
required_roles:
  - READONLY_ADMIN | VIRT_INSTANCE_READ
---

# virt.device.pci_choices

## Summary

Returns choices for PCI devices valid for VM virt instances.

## Required Roles

- `READONLY_ADMIN | VIRT_INSTANCE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Object of available PCI devices that can be passed through to virtual instances.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
