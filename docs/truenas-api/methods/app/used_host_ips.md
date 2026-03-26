---
title: app.used_host_ips
kind: method
source_rst: _sources/api_methods_app.used_host_ips.rst.txt
source_html: api_methods_app.used_host_ips.html
required_roles:
  - APPS_READ
---

# app.used_host_ips

## Summary

Returns host IPs in use by applications.

## Required Roles

- `APPS_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Object mapping application names to arrays of host IP addresses they use.
#### Additional Properties

Each additional property must conform to the following schema
- Type: array of string
- No Additional Items

##### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
