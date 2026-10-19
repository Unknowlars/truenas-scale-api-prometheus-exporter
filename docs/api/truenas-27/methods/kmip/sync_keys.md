---
title: kmip.sync_keys
kind: method
source_rst: _sources/api_methods_kmip.sync_keys.rst.txt
source_html: api_methods_kmip.sync_keys.html
required_roles:
  - KMIP_WRITE
---

# kmip.sync_keys

## Summary

Sync ZFS/SED keys between KMIP Server and TN database.

## Required Roles

- `KMIP_WRITE`

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

Returns `null` when key synchronization with the KMIP server completes.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
