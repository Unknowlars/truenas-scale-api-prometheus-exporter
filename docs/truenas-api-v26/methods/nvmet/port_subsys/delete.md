---
title: nvmet.port_subsys.delete
kind: method
source_rst: _sources/api_methods_nvmet.port_subsys.delete.rst.txt
source_html: api_methods_nvmet.port_subsys.delete.html
required_roles:
  - SHARING_NVME_TARGET_WRITE
---

# nvmet.port_subsys.delete

## Summary

Delete `port`/`subsys` association of `id`.

The specified subsystem will no longer be accessible on the `port`.

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

ID of the port-subsystem association to delete.

### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the port-subsystem association is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
