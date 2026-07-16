---
title: lxc.bridge_choices
kind: method
source_rst: _sources/api_methods_lxc.bridge_choices.rst.txt
source_html: api_methods_lxc.bridge_choices.html
required_roles:
  - LXC_CONFIG_READ | READONLY_ADMIN
---

# lxc.bridge_choices

## Summary

Bridge choices for virtualization purposes.

Empty means it will be managed/created automatically.

## Required Roles

- `LXC_CONFIG_READ | READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Object of available network bridge interfaces and their configurations.
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
