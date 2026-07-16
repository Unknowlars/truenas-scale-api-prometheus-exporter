---
title: alert.list_policies
kind: method
source_rst: _sources/api_methods_alert.list_policies.rst.txt
source_html: api_methods_alert.list_policies.html
required_roles:
  - ALERT_LIST_READ
---

# alert.list_policies

## Summary

List all alert policies which indicate the frequency of the alerts.

## Required Roles

- `ALERT_LIST_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: array of string

Array of available notification policies for alert classes.
- No Additional Items

#### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
