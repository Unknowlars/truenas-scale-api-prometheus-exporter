---
title: rsynctask.delete
kind: method
source_rst: _sources/api_methods_rsynctask.delete.rst.txt
source_html: api_methods_rsynctask.delete.html
required_roles:
  - SNAPSHOT_TASK_WRITE
---

# rsynctask.delete

## Summary

Delete Rsync Task of `id`.

## Required Roles

- `SNAPSHOT_TASK_WRITE`

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

ID of the rsync task to delete.

### Return value

- Schema name: `Result`
- Type: boolean

Whether the rsync task was successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
