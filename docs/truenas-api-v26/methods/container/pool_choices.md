---
title: container.pool_choices
kind: method
source_rst: _sources/api_methods_container.pool_choices.rst.txt
source_html: api_methods_container.pool_choices.html
required_roles:
  - CONTAINER_READ | READONLY_ADMIN
---

# container.pool_choices

## Summary

Pool choices for container creation.

## Required Roles

- `CONTAINER_READ | READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Object of available ZFS pools that can be used for container root filesystem.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
