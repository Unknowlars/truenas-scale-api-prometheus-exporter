---
title: core.job_abort
kind: method
source_rst: _sources/api_methods_core.job_abort.rst.txt
source_html: api_methods_core.job_abort.html
required_roles:
  []
---

# core.job_abort

## Required Roles

- None documented.

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

ID of the job to abort.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the job is successfully aborted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
