---
title: app.used_ports
kind: method
source_rst: _sources/api_methods_app.used_ports.rst.txt
source_html: api_methods_app.used_ports.html
required_roles:
  - APPS_READ
---

# app.used_ports

## Summary

Returns ports in use by applications.

## Required Roles

- `APPS_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: array of integer

Array of port numbers currently in use by any application.
- No Additional Items

#### Each item of this array must be:

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
