---
title: virt.instance.set_bootable_disk
kind: method
source_rst: _sources/api_methods_virt.instance.set_bootable_disk.rst.txt
source_html: api_methods_virt.instance.set_bootable_disk.html
required_roles:
  - VIRT_INSTANCE_WRITE
---

# virt.instance.set_bootable_disk

## Summary

Specify `disk` to boot `id_` virt instance OS from.

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

Identifier of the virtual instance to configure.
- Must be at least `1` characters long

#### Parameter 2: disk

#### disk

- Schema name: `disk`
- Type: string

Name or identifier of the disk device to set as bootable.
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: boolean

Whether the bootable disk configuration was successfully applied.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
