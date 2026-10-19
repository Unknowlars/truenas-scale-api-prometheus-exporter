---
title: system.general.checkin
kind: method
source_rst: _sources/api_methods_system.general.checkin.rst.txt
source_html: api_methods_system.general.checkin.html
required_roles:
  - SYSTEM_GENERAL_WRITE
---

# system.general.checkin

## Summary

After UI settings are saved with `rollback_timeout` this method needs to be called within that timeout limit to prevent reverting the changes.

This is to ensure user verifies the changes went as planned and its working.

## Required Roles

- `SYSTEM_GENERAL_WRITE`

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

- Schema name: `Result`
- Type: null

Returns `null` on successful configuration check-in.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
