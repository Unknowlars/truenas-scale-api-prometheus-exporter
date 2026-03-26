---
title: truenas.get_eula
kind: method
source_rst: _sources/api_methods_truenas.get_eula.rst.txt
source_html: api_methods_truenas.get_eula.html
required_roles:
  - READONLY_ADMIN
---

# truenas.get_eula

## Summary

Returns the TrueNAS End-User License Agreement (EULA).

## Required Roles

- `READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`

Full text of the End User License Agreement. `null` if no EULA is required.
#### Any of

##### Option 1

- Type: string

##### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
