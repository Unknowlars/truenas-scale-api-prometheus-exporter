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

Continue an in-progress authentication attempt. This endpoint should be called to continue an :doc:`auth.login_ex <api_methods_auth.login_ex>` attempt that returned a `response_type` of `OTP_REQUIRED`, submitting the one-time password via the `OTP_TOKEN` mechanism.

This is a convenience wrapper around :doc:`auth.login_ex <api_methods_auth.login_ex>` for API consumers.

The `response_type` of the result indicates the outcome of this authentication step:

- `SUCCESS` -- authentication completed and a session was established. - `OTP_REQUIRED` -- the one-time password token was rejected; the client may call this endpoint again with a correct token. - `AUTH_ERR` -- an invalid one-time password token was submitted too many times.

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
- Default:
```json
{
  "user_info": true,
  "reconnect_token": false
}
```

Additional options for the authentication process.
- No Additional Properties
###### user_info

- Schema name: `User Info`
- Type: boolean
- Default: true

Whether to include detailed user information in the authentication response.

###### reconnect_token

- Schema name: `Reconnect Token`
- Type: boolean
- Default: false

Whether to include a reauthentication token in the authentication response. The `ttl` for the generated token depends on the TrueNAS webui setting for preferences->lifetime, with a default value of 600 seconds.

### Return value

- Schema name: `Result`

Authentication response after continuing with OTP token.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
