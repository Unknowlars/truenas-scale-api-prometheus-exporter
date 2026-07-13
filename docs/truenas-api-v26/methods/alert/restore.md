---
title: alert.restore
kind: method
source_rst: _sources/api_methods_alert.restore.rst.txt
source_html: api_methods_alert.restore.html
required_roles:
  - ALERT_LIST_WRITE
---

# alert.restore

## Summary

Restore `id` alert which had been dismissed.

## Required Roles

- `ALERT_LIST_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: uuid

#### uuid

- Schema name: `uuid`
- Type: string

UUID of the dismissed alert to restore.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the alert is successfully restored.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
