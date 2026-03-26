---
title: initshutdownscript.delete
kind: method
source_rst: _sources/api_methods_initshutdownscript.delete.rst.txt
source_html: api_methods_initshutdownscript.delete.html
required_roles:
  - SYSTEM_CRON_WRITE
---

# initshutdownscript.delete

## Summary

Delete init/shutdown task of `id`.

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

ID of the init/shutdown script to delete.

### Return value

- Schema name: `Result`
- Type: const

Always return `True`.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
