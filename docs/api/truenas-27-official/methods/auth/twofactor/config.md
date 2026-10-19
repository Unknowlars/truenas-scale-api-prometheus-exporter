---
title: auth.twofactor.config
kind: method
source_rst: _sources/api_methods_auth.twofactor.config.rst.txt
source_html: api_methods_auth.twofactor.config.html
required_roles:
  - SYSTEM_SECURITY_READ
---

# auth.twofactor.config

## Required Roles

- `SYSTEM_SECURITY_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `TwoFactorAuthEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_enabled"></a>
<a id="Return_value_enabled"></a>
#### enabled (required)

- Schema name: `Enabled`
- Type: boolean

Whether two-factor authentication is enabled system-wide.

<a id="headingReturn_value_services"></a>
<a id="Return_value_services"></a>
#### services (required)

- Schema name: `TwoFactorAuthServices`
- Type: object

Configuration for which services require two-factor authentication.
- No Additional Properties
<a id="headingReturn_value_services_ssh"></a>
<a id="Return_value_services_ssh"></a>
##### ssh

- Schema name: `Ssh`
- Type: boolean
- Default: false

Whether two-factor authentication is required for SSH connections.

<a id="headingReturn_value_window"></a>
<a id="Return_value_window"></a>
#### window (required)

- Schema name: `Window`
- Type: integer

Time window in seconds for TOTP token validation (minimum 0).
- Value must be greater or equal to `0`

<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the two-factor authentication configuration.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
