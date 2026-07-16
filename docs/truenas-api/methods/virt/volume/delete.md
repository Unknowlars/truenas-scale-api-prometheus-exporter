---
title: virt.volume.delete
kind: method
source_rst: _sources/api_methods_virt.volume.delete.rst.txt
source_html: api_methods_virt.volume.delete.html
required_roles:
  - VIRT_IMAGE_WRITE
---

# virt.volume.delete

## Required Roles

- `VIRT_IMAGE_WRITE`

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

Identifier of the virtualization volume to delete.
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: const

Always returns true on successful volume deletion.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
