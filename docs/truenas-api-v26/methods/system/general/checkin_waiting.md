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

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`

Seconds remaining until automatic rollback. `null` if no rollback is pending.
#### Any of

##### Option 1

- Type: integer

##### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
