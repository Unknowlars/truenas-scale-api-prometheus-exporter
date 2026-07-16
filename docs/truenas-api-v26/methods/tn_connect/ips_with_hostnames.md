---
title: tn_connect.ips_with_hostnames
kind: method
source_rst: _sources/api_methods_tn_connect.ips_with_hostnames.rst.txt
source_html: api_methods_tn_connect.ips_with_hostnames.html
required_roles:
  - TRUENAS_CONNECT_READ
---

# tn_connect.ips_with_hostnames

## Summary

Returns current mapping of ips configured with truenas connect against their hostnames.

## Required Roles

- `TRUENAS_CONNECT_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
