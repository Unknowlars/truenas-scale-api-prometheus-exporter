---
title: virt.instance.device_list
kind: method
source_rst: _sources/api_methods_virt.instance.device_list.rst.txt
source_html: api_methods_virt.instance.device_list.html
required_roles:
  - VIRT_INSTANCE_READ
---

# virt.instance.device_list

## Summary

List all devices associated to an instance.

## Required Roles

- `VIRT_INSTANCE_READ`

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

ID of the virtual instance to list devices for.

### Return value

- Schema name: `Result`
- Type: array

Array of devices attached to the virtual instance.
- No Additional Items

#### Each item of this array must be:

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
