---
title: nvmet.subsys.delete
kind: method
source_rst: _sources/api_methods_nvmet.subsys.delete.rst.txt
source_html: api_methods_nvmet.subsys.delete.html
required_roles:
  - SHARING_NVME_TARGET_WRITE
---

# nvmet.subsys.delete

## Summary

Delete NVMe target subsystem (`subsys`) of `id`.

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

ID of the subsystem to delete.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

Options for subsystem deletion behavior.
- No Additional Properties
##### force

- Schema name: `Force`
- Type: boolean
- Default: false

Force subsystem deletion, even if currently associated with one or more namespaces or ports.

### Return value

- Schema name: `Result`
- Type: const

Indicates successful deletion of the subsystem.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
