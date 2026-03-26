---
title: sharing.smb.presets
kind: method
source_rst: _sources/api_methods_sharing.smb.presets.rst.txt
source_html: api_methods_sharing.smb.presets.html
required_roles:
  - SHARING_SMB_READ
---

# sharing.smb.presets

## Summary

Retrieve pre-defined configuration sets for specific use-cases. These parameter combinations are often non-obvious, but beneficial in these scenarios.

## Required Roles

- `SHARING_SMB_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Available SMB share preset configurations by purpose.
#### Additional Properties

Each additional property must conform to the following schema
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
