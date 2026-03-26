---
title: system.advanced.update_gpu_pci_ids
kind: method
source_rst: _sources/api_methods_system.advanced.update_gpu_pci_ids.rst.txt
source_html: api_methods_system.advanced.update_gpu_pci_ids.html
required_roles:
  - SYSTEM_ADVANCED_WRITE
---

# system.advanced.update_gpu_pci_ids

## Summary

`isolated_gpu_pci_ids` is a list of PCI ids which are isolated from host system.

## Required Roles

- `SYSTEM_ADVANCED_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`
- Type: array of string

List of GPU PCI IDs to isolate for VM passthrough.
- No Additional Items

##### Each item of this array must be:

- Type: string

### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
