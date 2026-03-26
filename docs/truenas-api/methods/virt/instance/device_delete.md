---
title: virt.instance.device_delete
kind: method
source_rst: _sources/api_methods_virt.instance.device_delete.rst.txt
source_html: api_methods_virt.instance.device_delete.html
required_roles:
  - VIRT_INSTANCE_DELETE
---

# virt.instance.device_delete

## Summary

Delete a device from an instance.

## Required Roles

- `VIRT_INSTANCE_DELETE`

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

ID of the virtual instance to remove device from.

#### Parameter 2: name

#### name

- Schema name: `name`
- Type: string

Name of the device to remove.

### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the device is successfully removed.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
