---
title: system.general.ui_restart
kind: method
source_rst: _sources/api_methods_system.general.ui_restart.rst.txt
source_html: api_methods_system.general.ui_restart.html
required_roles:
  - SYSTEM_GENERAL_WRITE
---

# system.general.ui_restart

## Summary

Restart HTTP server to use latest UI settings.

HTTP server will be restarted after `delay` seconds.

## Required Roles

- `SYSTEM_GENERAL_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: delay

#### delay

- Schema name: `delay`
- Type: integer
- Default: 3

How long to wait before the UI is restarted.
- Value must be greater or equal to `0`

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful UI restart initiation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
