---
title: system.debug
kind: method
source_rst: _sources/api_methods_system.debug.rst.txt
source_html: api_methods_system.debug.html
required_roles:
  - READONLY_ADMIN
---

# system.debug

## Summary

Download a debug file.

This method is a job.

*This job MUST be used with* [core.download](../core/download.md).

## Required Roles

- `READONLY_ADMIN`

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

Debug information collection completed successfully.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
