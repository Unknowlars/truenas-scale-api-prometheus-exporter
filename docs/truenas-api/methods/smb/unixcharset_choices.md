---
title: smb.unixcharset_choices
kind: method
source_rst: _sources/api_methods_smb.unixcharset_choices.rst.txt
source_html: api_methods_smb.unixcharset_choices.html
required_roles:
  - READONLY_ADMIN | SHARING_SMB_READ
---

# smb.unixcharset_choices

## Required Roles

- `READONLY_ADMIN | SHARING_SMB_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Available character set choices for Unix charset configuration.
#### Additional Properties

Each additional property must conform to the following schema
- Type: enum (of string)

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
