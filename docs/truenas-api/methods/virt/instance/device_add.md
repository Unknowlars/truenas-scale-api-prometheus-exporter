---
title: virt.instance.device_add
kind: method
source_rst: _sources/api_methods_virt.instance.device_add.rst.txt
source_html: api_methods_virt.instance.device_add.html
required_roles:
  - VIRT_INSTANCE_WRITE
---

# virt.instance.device_add

## Summary

Add a device to an instance.

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

ID of the virtual instance to add device to.

#### Parameter 2: device

#### device

- Schema name: `device`

Device configuration to add to the instance.

### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the device is successfully added.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
