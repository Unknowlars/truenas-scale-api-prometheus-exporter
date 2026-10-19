---
title: failover.disabled.reasons
kind: event
source_rst: _sources/api_events_failover.disabled.reasons.rst.txt
source_html: api_events_failover.disabled.reasons.html
required_roles:
  - FAILOVER_READ
---

# failover.disabled.reasons

## Summary

Sent when failover status reasons change.

## Required Roles

- `FAILOVER_READ`

## Schema

- Type: object

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `FailoverDisabledReasonsChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `FailoverDisabledReasonsChangedEventFields`
- Type: object

Event fields.
- No Additional Properties
<a id="headingCHANGED_fields_disabled_reasons"></a>
<a id="CHANGED_fields_disabled_reasons"></a>
##### disabled_reasons (required)

- Schema name: `Disabled Reasons`
- Type: array of string

Array of reasons why failover is currently disabled.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_disabled_reasons_items"></a>
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
