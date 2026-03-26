---
title: jbof.reapply_config
kind: method
source_rst: _sources/api_methods_jbof.reapply_config.rst.txt
source_html: api_methods_jbof.reapply_config.html
required_roles:
  - JBOF_WRITE
---

# jbof.reapply_config

## Summary

Reapply the JBOF configuration to attached JBOFs.

If an IOM is replaced in a JBOF, then it is expected to be configured to have the same redfish IP, user & password as was previously the case.

This API can then be called to configure each JBOF with the expected data-plane IP configuration, and then attach NVMe drives.

## Required Roles

- `JBOF_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the JBOF configuration is successfully reapplied.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
