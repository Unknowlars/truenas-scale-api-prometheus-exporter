---
title: truenas.license.fingerprint
kind: method
source_rst: _sources/api_methods_truenas.license.fingerprint.rst.txt
source_html: api_methods_truenas.license.fingerprint.html
required_roles:
  - READONLY_ADMIN
---

# truenas.license.fingerprint

## Summary

Return the system hardware fingerprint as a base64-encoded JSON string.

## Required Roles

- `READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: string

Base64-encoded JSON of the system hardware fingerprint.
- Must be at most `2147483647` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
