---
title: vm.random_mac
kind: method
source_rst: _sources/api_methods_vm.random_mac.rst.txt
source_html: api_methods_vm.random_mac.html
required_roles:
  - VM_READ
---

# vm.random_mac

## Summary

Create a random mac address.

Returns: str: with six groups of two hexadecimal digits

## Required Roles

- `VM_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: string

Randomly generated MAC address suitable for virtual machine network interfaces.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
