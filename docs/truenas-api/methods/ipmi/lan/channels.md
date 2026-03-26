---
title: ipmi.lan.channels
kind: method
source_rst: _sources/api_methods_ipmi.lan.channels.rst.txt
source_html: api_methods_ipmi.lan.channels.html
required_roles:
  - IPMI_READ
---

# ipmi.lan.channels

## Summary

Return a list of available IPMI channels.

## Required Roles

- `IPMI_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: array of integer

Array of available IPMI LAN channel numbers.
- No Additional Items

#### Each item of this array must be:

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
