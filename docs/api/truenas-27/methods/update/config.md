---
title: update.config
kind: method
source_rst: _sources/api_methods_update.config.rst.txt
source_html: api_methods_update.config.html
required_roles:
  - SYSTEM_UPDATE_READ
---

# update.config

## Required Roles

- `SYSTEM_UPDATE_READ`

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

- Schema name: `UpdateEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the update configuration.

<a id="headingReturn_value_autocheck"></a>
<a id="Return_value_autocheck"></a>
#### autocheck (required)

- Schema name: `Autocheck`
- Type: boolean

Automatically check and download updates every night.

<a id="headingReturn_value_profile"></a>
<a id="Return_value_profile"></a>
#### profile (required)

- Schema name: `Profile`
- Type: string

Update profile used for the system.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
