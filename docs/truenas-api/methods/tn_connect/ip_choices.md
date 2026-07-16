---
title: tn_connect.ip_choices
kind: method
source_rst: _sources/api_methods_tn_connect.ip_choices.rst.txt
source_html: api_methods_tn_connect.ip_choices.html
required_roles:
  - READONLY_ADMIN | TRUENAS_CONNECT_READ
---

# tn_connect.ip_choices

## Summary

Returns IP choices which can be used with TrueNAS Connect.

## Required Roles

- `READONLY_ADMIN | TRUENAS_CONNECT_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Object of available IP addresses and their associated interface descriptions.
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
