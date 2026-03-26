---
title: nvmet.host.delete
kind: method
source_rst: _sources/api_methods_nvmet.host.delete.rst.txt
source_html: api_methods_nvmet.host.delete.html
required_roles:
  - SHARING_NVME_TARGET_WRITE
---

# nvmet.host.delete

## Summary

Delete NVMe target `host` of `id`.

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

ID of the NVMe-oF host to delete.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

Options controlling host deletion behavior.
- No Additional Properties
##### force

- Schema name: `Force`
- Type: boolean
- Default: false

Force host deletion, even if currently associated with one or more subsystems.

### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the NVMe-oF host is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
