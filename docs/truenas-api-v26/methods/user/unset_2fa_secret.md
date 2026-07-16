---
title: user.unset_2fa_secret
kind: method
source_rst: _sources/api_methods_user.unset_2fa_secret.rst.txt
source_html: api_methods_user.unset_2fa_secret.html
required_roles:
  - ACCOUNT_WRITE
---

# user.unset_2fa_secret

## Summary

Unset two-factor authentication secret for `username`.

## Required Roles

- `ACCOUNT_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: username

#### username

- Schema name: `username`
- Type: string

Username to disable two-factor authentication for.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful two-factor authentication removal.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
