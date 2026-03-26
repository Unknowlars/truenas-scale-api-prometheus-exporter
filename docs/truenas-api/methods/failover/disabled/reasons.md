---
title: failover.disabled.reasons
kind: method
source_rst: _sources/api_methods_failover.disabled.reasons.rst.txt
source_html: api_methods_failover.disabled.reasons.html
required_roles:
  - FAILOVER_READ
---

# failover.disabled.reasons

## Summary

Returns a list of reasons why failover is not enabled/functional. See `DisabledReasonsEnum` for the reasons and their explanation.

## Required Roles

- `FAILOVER_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: array of string

Array of reasons why failover is currently disabled.
- No Additional Items

#### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
