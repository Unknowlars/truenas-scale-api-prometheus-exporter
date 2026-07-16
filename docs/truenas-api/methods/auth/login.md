---
title: auth.login
kind: method
source_rst: _sources/api_methods_auth.login.rst.txt
source_html: api_methods_auth.login.html
required_roles:
  []
---

# auth.login

## Summary

Authenticate session using username and password. `otp_token` must be specified if two factor authentication is enabled.

## Required Roles

- None documented.

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

Username for authentication.

#### Parameter 2: password

#### password

- Schema name: `password`
- Type: string

Password for authentication.

#### Parameter 3: otp_token

#### otp_token

- Schema name: `otp_token`
- Default: null

One-time password token for two-factor authentication or `null`.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` if login was successful, `false` otherwise.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
