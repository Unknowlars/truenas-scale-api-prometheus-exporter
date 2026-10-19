---
title: interface.cancel_rollback
kind: method
source_rst: _sources/api_methods_interface.cancel_rollback.rst.txt
source_html: api_methods_interface.cancel_rollback.html
required_roles:
  - NETWORK_INTERFACE_WRITE
---

# interface.cancel_rollback

## Summary

If this method is called after interface changes have been committed and within the checkin timeout, then the task that automatically rolls back any interface changes is cancelled and the in-memory snapshot of database tables for the various interface tables will NOT be cleared.

## Required Roles

- `NETWORK_INTERFACE_WRITE`

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

No return value for successful cancel rollback operation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
