---
title: nvmet.namespace.delete
kind: method
source_rst: _sources/api_methods_nvmet.namespace.delete.rst.txt
source_html: api_methods_nvmet.namespace.delete.html
required_roles:
  - SHARING_NVME_TARGET_WRITE
---

# nvmet.namespace.delete

## Summary

Delete NVMe target namespace of `id`.

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

ID of the NVMe-oF namespace to delete.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

Options controlling namespace deletion behavior.
- No Additional Properties
##### remove

- Schema name: `Remove`
- Type: boolean
- Default: false

Remove file underlying namespace if `device_type` is FILE.

### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the NVMe-oF namespace is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
