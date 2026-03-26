---
title: pool.snapshottask.max_total_count
kind: method
source_rst: _sources/api_methods_pool.snapshottask.max_total_count.rst.txt
source_html: api_methods_pool.snapshottask.max_total_count.html
required_roles:
  - SNAPSHOT_TASK_READ
---

# pool.snapshottask.max_total_count

## Summary

Returns a maximum amount of snapshots (total) the system can sustain.

## Required Roles

- `SNAPSHOT_TASK_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: integer

Maximum total number of snapshots allowed across all tasks.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
