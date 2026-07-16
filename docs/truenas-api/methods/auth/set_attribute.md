---
title: auth.set_attribute
kind: method
source_rst: _sources/api_methods_auth.set_attribute.rst.txt
source_html: api_methods_auth.set_attribute.html
required_roles:
  []
---

# auth.set_attribute

## Summary

Set current user's `attributes` dictionary `key` to `value`.

e.g. Setting key="foo" value="var" will result in {"attributes": {"foo": "bar"}}

## Required Roles

- None documented.

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: key

#### key

- Schema name: `key`
- Type: string

Attribute key name.

#### Parameter 2: value

#### value

- Schema name: `value`
- Type: object

Attribute value to set.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the attribute is successfully set.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
