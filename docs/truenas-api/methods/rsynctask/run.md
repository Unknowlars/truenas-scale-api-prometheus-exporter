---
title: rsynctask.run
kind: method
source_rst: _sources/api_methods_rsynctask.run.rst.txt
source_html: api_methods_rsynctask.run.html
required_roles:
  - SNAPSHOT_TASK_WRITE
---

# rsynctask.run

## Summary

Job to run rsync task of `id`.

Output is saved to job log excerpt (not syslog).

This method is a job.

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

ID of the rsync task to run immediately.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful rsync task execution.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
