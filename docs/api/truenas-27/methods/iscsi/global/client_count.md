---
title: iscsi.global.client_count
kind: method
source_rst: _sources/api_methods_iscsi.global.client_count.rst.txt
source_html: api_methods_iscsi.global.client_count.html
required_roles:
  - SHARING_ISCSI_GLOBAL_READ
---

# iscsi.global.client_count

## Summary

Return currently connected clients count.

## Required Roles

- `SHARING_ISCSI_GLOBAL_READ`

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
- Type: integer

Number of currently connected iSCSI clients.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
