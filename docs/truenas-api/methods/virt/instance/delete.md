---
title: virt.instance.delete
kind: method
source_rst: _sources/api_methods_virt.instance.delete.rst.txt
source_html: api_methods_virt.instance.delete.html
required_roles:
  - VIRT_INSTANCE_WRITE
---

# virt.instance.delete

## Summary

Delete an instance.

This method is a job.

## Required Roles

- `VIRT_INSTANCE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: string

ID of the virtual instance to delete.

### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the virtual instance is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
