---
title: system.general.checkin_waiting
kind: method
source_rst: _sources/api_methods_system.general.checkin_waiting.rst.txt
source_html: api_methods_system.general.checkin_waiting.html
required_roles:
  - SYSTEM_GENERAL_WRITE
---

# system.general.checkin_waiting

## Summary

Determines whether we are waiting user to check in the applied UI settings changes before they are rolled back. Returns a number of seconds before the automatic rollback or null if there are no changes pending.

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

Seconds remaining until automatic rollback. `null` if no rollback is pending.
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [Option 2](#tab-pane_Return_value_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
