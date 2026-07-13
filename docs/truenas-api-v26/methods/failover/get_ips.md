---
title: failover.get_ips
kind: method
source_rst: _sources/api_methods_failover.get_ips.rst.txt
source_html: api_methods_failover.get_ips.html
required_roles:
  - FAILOVER_READ
---

# failover.get_ips

## Summary

Get a list of IPs for which the Web UI can be accessed.

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

Array of IP addresses configured for failover.
- No Additional Items

#### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
