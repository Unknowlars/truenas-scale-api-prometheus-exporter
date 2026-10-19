---
title: boot.scrub
kind: method
source_rst: _sources/api_methods_boot.scrub.rst.txt
source_html: api_methods_boot.scrub.html
required_roles:
  - BOOT_ENV_WRITE
---

# boot.scrub

## Summary

Scrub on boot pool.

This method is a job.

## Required Roles

- `BOOT_ENV_WRITE`

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

Returns `null` when the boot pool scrub is successfully started.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
