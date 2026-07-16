---
title: truenas.accept_eula
kind: method
source_rst: _sources/api_methods_truenas.accept_eula.rst.txt
source_html: api_methods_truenas.accept_eula.html
required_roles:
  - FULL_ADMIN
---

# truenas.accept_eula

## Summary

Accept TrueNAS EULA.

## Required Roles

- `FULL_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful EULA acceptance.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
