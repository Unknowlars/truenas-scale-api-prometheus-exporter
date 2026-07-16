---
title: vmware.dataset_has_vms
kind: method
source_rst: _sources/api_methods_vmware.dataset_has_vms.rst.txt
source_html: api_methods_vmware.dataset_has_vms.html
required_roles:
  - READONLY_ADMIN
---

# vmware.dataset_has_vms

## Summary

Returns "true" if `dataset` is configured with a VMWare snapshot

## Required Roles

- `READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: dataset

#### dataset

- Schema name: `dataset`
- Type: string

ZFS dataset path to check for VMware virtual machines.

#### Parameter 2: recursive

#### recursive

- Schema name: `recursive`
- Type: boolean

Whether to check child datasets recursively.

### Return value

- Schema name: `Result`
- Type: boolean

Whether the dataset contains VMware virtual machines.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
