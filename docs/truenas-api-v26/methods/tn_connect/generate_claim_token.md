---
title: tn_connect.generate_claim_token
kind: method
source_rst: _sources/api_methods_tn_connect.generate_claim_token.rst.txt
source_html: api_methods_tn_connect.generate_claim_token.html
required_roles:
  - TRUENAS_CONNECT_WRITE
---

# tn_connect.generate_claim_token

## Summary

Generate a claim token for TrueNAS Connect.

This is used to claim the system with TrueNAS Connect. When this endpoint will be called, a token will be generated which will be used to assist with initial setup with truenas connect.

## Required Roles

- `TRUENAS_CONNECT_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: string

Generated claim token for authenticating with TrueNAS Connect services.
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
