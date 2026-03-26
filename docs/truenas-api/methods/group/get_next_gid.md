---
title: group.get_next_gid
kind: method
source_rst: _sources/api_methods_group.get_next_gid.rst.txt
source_html: api_methods_group.get_next_gid.html
required_roles:
  - ACCOUNT_READ
---

# group.get_next_gid

## Summary

Get the next available/free gid.

## Required Roles

- `ACCOUNT_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: integer

The next available group ID number.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
