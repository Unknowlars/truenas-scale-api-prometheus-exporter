---
title: cronjob.delete
kind: method
source_rst: _sources/api_methods_cronjob.delete.rst.txt
source_html: api_methods_cronjob.delete.html
required_roles:
  - SYSTEM_CRON_WRITE
---

# cronjob.delete

## Summary

Delete cronjob of `id`.

## Required Roles

- `SYSTEM_CRON_WRITE`

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

ID of the cron job to delete.

### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the cron job is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
