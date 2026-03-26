---
title: ssh.bindiface_choices
kind: method
source_rst: _sources/api_methods_ssh.bindiface_choices.rst.txt
source_html: api_methods_ssh.bindiface_choices.html
required_roles:
  - NETWORK_INTERFACE_READ | READONLY_ADMIN | SSH_READ
---

# ssh.bindiface_choices

## Summary

Available choices for the bindiface attribute of SSH service.

## Required Roles

- `NETWORK_INTERFACE_READ | READONLY_ADMIN | SSH_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Result of `interface.choices`.
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
