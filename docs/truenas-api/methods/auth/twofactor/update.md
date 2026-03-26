---
title: auth.twofactor.update
kind: method
source_rst: _sources/api_methods_auth.twofactor.update.rst.txt
source_html: api_methods_auth.twofactor.update.html
required_roles:
  - SYSTEM_SECURITY_WRITE
---

# auth.twofactor.update

## Summary

`window` extends the validity to `window` many counter ticks before and after the current one.

Update Two-Factor Authentication Service Configuration.

## Required Roles

- `SYSTEM_SECURITY_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: auth_twofactor_update

#### auth_twofactor_update

- Schema name: `auth_twofactor_update`
- Type: object

Updated two-factor authentication configuration settings.
- No Additional Properties
##### enabled

- Schema name: `Enabled`
- Type: boolean

Whether two-factor authentication is enabled system-wide.

##### services

- Schema name: `TwoFactorAuthServices`
- Type: object

Configuration for which services require two-factor authentication.
- No Additional Properties
###### ssh

- Schema name: `Ssh`
- Type: boolean
- Default: false

Whether two-factor authentication is required for SSH connections.

##### window

- Schema name: `Window`
- Type: integer

Time window in seconds for TOTP token validation (minimum 0).
- Value must be greater or equal to `0`

### Return value

- Schema name: `TwoFactorAuthEntry`
- Type: object

The updated two-factor authentication configuration.
- No Additional Properties
#### enabled (required)

- Schema name: `Enabled`
- Type: boolean

Whether two-factor authentication is enabled system-wide.

#### services (required)

- Schema name: `TwoFactorAuthServices`
- Type: object

Configuration for which services require two-factor authentication.
- No Additional Properties
##### ssh

- Schema name: `Ssh`
- Type: boolean
- Default: false

Whether two-factor authentication is required for SSH connections.

#### window (required)

- Schema name: `Window`
- Type: integer

Time window in seconds for TOTP token validation (minimum 0).
- Value must be greater or equal to `0`

#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the two-factor authentication configuration.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
