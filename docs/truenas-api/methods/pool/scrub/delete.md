---
title: pool.scrub.delete
kind: method
source_rst: _sources/api_methods_pool.scrub.delete.rst.txt
source_html: api_methods_pool.scrub.delete.html
required_roles:
  - POOL_SCRUB_WRITE
---

# pool.scrub.delete

## Summary

Delete scrub task of `id`.

## Required Roles

- `POOL_SCRUB_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id_

#### id_

- Schema name: `id_`
- Type: integer

ID of the scrub schedule to delete.

### Return value

- Schema name: `Result`
- Type: const

Indicates successful deletion of the scrub schedule.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
