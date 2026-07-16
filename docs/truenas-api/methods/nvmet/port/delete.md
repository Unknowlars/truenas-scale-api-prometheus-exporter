---
title: nvmet.port.delete
kind: method
source_rst: _sources/api_methods_nvmet.port.delete.rst.txt
source_html: api_methods_nvmet.port.delete.html
required_roles:
  - SHARING_NVME_TARGET_WRITE
---

# nvmet.port.delete

## Summary

Delete NVMe target `port` of `id`.

## Required Roles

- `SHARING_NVME_TARGET_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the NVMe-oF port to delete.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

Options controlling port deletion behavior.
- No Additional Properties
##### force

- Schema name: `Force`
- Type: boolean
- Default: false

Optional `boolean` to force port deletion, even if currently associated with one or more subsystems.

### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the NVMe-oF port is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
