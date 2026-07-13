---
title: webshare.bindip_choices
kind: method
source_rst: _sources/api_methods_webshare.bindip_choices.rst.txt
source_html: api_methods_webshare.bindip_choices.html
required_roles:
  - READONLY_ADMIN | SHARING_WEBSHARE_READ
---

# webshare.bindip_choices

## Summary

Returns ip choices for Webshare service to use.

## Required Roles

- `READONLY_ADMIN | SHARING_WEBSHARE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Available IP addresses that Webshare service can bind to.
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
