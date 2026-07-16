---
title: ipmi.sel.clear
kind: method
source_rst: _sources/api_methods_ipmi.sel.clear.rst.txt
source_html: api_methods_ipmi.sel.clear.html
required_roles:
  - IPMI_WRITE
---

# ipmi.sel.clear

## Summary

This method is a job.

## Required Roles

- `IPMI_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the SEL clear operation completes successfully.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
