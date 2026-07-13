---
title: system.host_id
kind: method
source_rst: _sources/api_methods_system.host_id.rst.txt
source_html: api_methods_system.host_id.html
required_roles:
  - READONLY_ADMIN
---

# system.host_id

## Summary

Retrieve a hex string that is generated based on the contents of the `/etc/hostid` file. This is a permanent value that persists across reboots/upgrades and can be used as a unique identifier for the machine.

## Required Roles

- `READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: string

The system host identifier.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
