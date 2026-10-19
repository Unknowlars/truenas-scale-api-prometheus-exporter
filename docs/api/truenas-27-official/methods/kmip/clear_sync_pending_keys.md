---
title: kmip.clear_sync_pending_keys
kind: method
source_rst: _sources/api_methods_kmip.clear_sync_pending_keys.rst.txt
source_html: api_methods_kmip.clear_sync_pending_keys.html
required_roles:
  - KMIP_WRITE
---

# kmip.clear_sync_pending_keys

## Summary

Clear all keys which are pending to be synced between KMIP server and TN database.

For ZFS/SED keys, we remove the UID from local database with which we are able to retrieve ZFS/SED keys. It should be used with caution.

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

Returns `null` when pending sync keys are successfully cleared.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
