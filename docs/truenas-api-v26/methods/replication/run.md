---
title: replication.run
kind: method
source_rst: _sources/api_methods_replication.run.rst.txt
source_html: api_methods_replication.run.html
required_roles:
  - REPLICATION_TASK_WRITE
---

# replication.run

## Summary

Run Replication Task of `id`.

This method is a job.

## Required Roles

- `REPLICATION_TASK_WRITE`

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

ID of the replication task to run.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful replication task execution.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
