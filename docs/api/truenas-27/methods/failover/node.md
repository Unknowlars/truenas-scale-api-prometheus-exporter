---
title: failover.node
kind: method
source_rst: _sources/api_methods_failover.node.rst.txt
source_html: api_methods_failover.node.html
required_roles:
  - FAILOVER_READ
---

# failover.node

## Summary

Returns the slot position in the chassis that the controller is located.

* "A" - First node * "B" - Seconde Node * "MANUAL" - Slot position in chassis could not be determined

## Required Roles

- `FAILOVER_READ`

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
- Type: string

Identifier of the current failover node (A or B).

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
