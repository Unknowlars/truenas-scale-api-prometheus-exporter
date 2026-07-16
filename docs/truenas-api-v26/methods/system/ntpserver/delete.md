---
title: system.ntpserver.delete
kind: method
source_rst: _sources/api_methods_system.ntpserver.delete.rst.txt
source_html: api_methods_system.ntpserver.delete.html
required_roles:
  - NETWORK_GENERAL_WRITE
---

# system.ntpserver.delete

## Summary

Delete NTP server of `id`.

## Required Roles

- `NETWORK_GENERAL_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the NTP server to delete.

### Return value

- Schema name: `Result`
- Type: const

Always returns true on successful NTP server deletion.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
