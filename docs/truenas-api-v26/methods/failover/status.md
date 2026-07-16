---
title: failover.status
kind: method
source_rst: _sources/api_methods_failover.status.rst.txt
source_html: api_methods_failover.status.html
required_roles:
  - FAILOVER_READ
---

# failover.status

## Summary

Get the current HA status.

Returns one of:

* "MASTER"

* "BACKUP"

* "ELECTING"

* "IMPORTING"

* "ERROR"

* "SINGLE"

## Required Roles

- `FAILOVER_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: string

Current status of the failover system.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
