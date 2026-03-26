---
title: virt.instance.device_update
kind: method
source_rst: _sources/api_methods_virt.instance.device_update.rst.txt
source_html: api_methods_virt.instance.device_update.html
required_roles:
  - VIRT_INSTANCE_WRITE
---

# virt.instance.device_update

## Summary

Update a device in an instance.

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

ID of the virtual instance to update device for.

#### Parameter 2: device

#### device

- Schema name: `device`

Updated device configuration.

### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the device is successfully updated.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
