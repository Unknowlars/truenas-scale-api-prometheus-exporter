---
title: failover.licensed
kind: method
source_rst: _sources/api_methods_failover.licensed.rst.txt
source_html: api_methods_failover.licensed.html
required_roles:
  []
---

# failover.licensed

## Summary

Checks whether this instance is licensed as an HA unit.

## Required Roles

- None documented.

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` if the system is licensed for high availability, `false` otherwise.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
