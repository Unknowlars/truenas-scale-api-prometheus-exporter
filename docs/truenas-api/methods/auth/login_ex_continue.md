---
title: auth.login_ex_continue
kind: method
source_rst: _sources/api_methods_auth.login_ex_continue.rst.txt
source_html: api_methods_auth.login_ex_continue.html
required_roles:
  []
---

# auth.login_ex_continue

## Summary

Continue in-progress authentication attempt. This endpoint should be called to continue an auth.login_ex attempt that returned OTP_REQUIRED.

This is a convenience wrapper around auth.login_ex for API consumers.

params: mechanism: the mechanism by which to continue authentication. Currently the only supported mechanism here is OTP_TOKEN.

OTP_TOKEN otp_token: one-time password token. This is only permitted if a previous auth.login_ex call responded with "OTP_REQUIRED".

returns: JSON object containing the following keys:

`response_type` - will be one of the following: SUCCESS - continued auth was required

OTP_REQUIRED - otp token was rejected. API consumer may call this endpoint again with correct OTP token.

AUTH_ERR - invalid OTP token submitted too many times.

## Required Roles

- None documented.

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: login_data

#### login_data

- Schema name: `login_data`
- Type: object

OTP token data to continue two-factor authentication flow.
- No Additional Properties
##### mechanism (required)

- Schema name: `Mechanism`
- Type: const

Authentication mechanism identifier for one-time password tokens.

##### otp_token (required)

- Schema name: `Otp Token`
- Type: string

One-time password token for authentication.

##### login_options

- Schema name: `AuthCommonOptions`
- Type: object
- Default: {"user_info": true}

Additional options for the authentication process.
- No Additional Properties
###### user_info

- Schema name: `User Info`
- Type: boolean
- Default: true

Whether to include detailed user information in the authentication response.

### Return value

- Schema name: `Result`

Authentication response after continuing with OTP token.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
