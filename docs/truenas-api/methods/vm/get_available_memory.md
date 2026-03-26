---
title: vm.get_available_memory
kind: method
source_rst: _sources/api_methods_vm.get_available_memory.rst.txt
source_html: api_methods_vm.get_available_memory.html
required_roles:
  - VM_READ
---

# vm.get_available_memory

## Summary

Get the current maximum amount of available memory to be allocated for VMs.

In case of `overcommit` being `true`, calculations are done in the following manner: 1. If a VM has requested 10G but is only consuming 5G, only 5G will be counted 2. System will consider shrinkable ZFS ARC as free memory ( shrinkable ZFS ARC is current ZFS ARC minus ZFS ARC minimum )

In case of `overcommit` being `false`, calculations are done in the following manner: 1. Complete VM requested memory will be taken into account regardless of how much actual physical memory the VM is consuming 2. System will not consider shrinkable ZFS ARC as free memory

Memory is of course a very "volatile" resource, values may change abruptly between a second but I deem it good enough to give the user a clue about how much memory is available at the current moment and if a VM should be allowed to be launched.

## Required Roles

- `VM_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: overcommit

#### overcommit

- Schema name: `overcommit`
- Type: boolean
- Default: false

Whether to include overcommitted memory in available memory calculation.

### Return value

- Schema name: `Result`
- Type: integer

Available memory for virtual machines in megabytes.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
