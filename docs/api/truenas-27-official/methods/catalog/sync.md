---
title: catalog.sync
kind: method
source_rst: _sources/api_methods_catalog.sync.rst.txt
source_html: api_methods_catalog.sync.html
required_roles:
  - CATALOG_WRITE
---

# catalog.sync

## Summary

Sync truenas catalog to retrieve latest changes from upstream.

This method is a job.

## Required Roles

- `CATALOG_WRITE`

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

Returns `null` when the catalog sync is successfully completed.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
