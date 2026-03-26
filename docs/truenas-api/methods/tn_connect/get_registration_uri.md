---
title: tn_connect.get_registration_uri
kind: method
source_rst: _sources/api_methods_tn_connect.get_registration_uri.rst.txt
source_html: api_methods_tn_connect.get_registration_uri.html
required_roles:
  - TRUENAS_CONNECT_READ
---

# tn_connect.get_registration_uri

## Summary

Return the registration URI for TrueNAS Connect.

Before this endpoint is called, tn_connect must be enabled and a claim token must be generated - based off which this endpoint will return the registration URI for TrueNAS Connect.

## Required Roles

- `TRUENAS_CONNECT_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: string

Registration URI for connecting this TrueNAS system to TrueNAS Connect.
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
