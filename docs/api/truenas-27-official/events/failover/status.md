---
title: failover.status
kind: event
source_rst: _sources/api_events_failover.status.rst.txt
source_html: api_events_failover.status.html
required_roles:
  - FAILOVER_READ
---

# failover.status

## Summary

Sent when failover status changes.

## Required Roles

- `FAILOVER_READ`

## Schema

- Type: object

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `FailoverStatusChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `FailoverStatusChangedEventFields`
- Type: object

Event fields.
- No Additional Properties
<a id="headingCHANGED_fields_status"></a>
<a id="CHANGED_fields_status"></a>
##### status (required)

- Schema name: `Status`
- Type: string

Current status of the failover system.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
