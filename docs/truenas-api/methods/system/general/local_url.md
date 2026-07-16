---
title: system.general.local_url
kind: method
source_rst: _sources/api_methods_system.general.local_url.rst.txt
source_html: api_methods_system.general.local_url.html
required_roles:
  - SYSTEM_GENERAL_READ
---

# system.general.local_url

## Summary

Returns configured local url in the format of protocol://host:port

## Required Roles

- `SYSTEM_GENERAL_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: string

The local URL for accessing the web UI.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
