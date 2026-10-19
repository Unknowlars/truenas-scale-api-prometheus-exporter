---
title: idmap.clear_idmap_cache
kind: method
source_rst: _sources/api_methods_idmap.clear_idmap_cache.rst.txt
source_html: api_methods_idmap.clear_idmap_cache.html
required_roles:
  - DIRECTORY_SERVICE_WRITE
---

# idmap.clear_idmap_cache

## Summary

Stop samba, remove the winbindd_cache.tdb file, start samba, flush samba's cache. This should be performed after finalizing idmap changes.

This method is a job.

## Required Roles

- `DIRECTORY_SERVICE_WRITE`

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

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
