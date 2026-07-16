---
title: core.unsubscribe
kind: method
source_rst: _sources/api_methods_core.unsubscribe.rst.txt
source_html: api_methods_core.unsubscribe.html
required_roles:
  []
---

# core.unsubscribe

## Required Roles

- None documented.

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id_

#### id_

- Schema name: `id_`
- Type: string

Subscription ID to cancel.

### Return value

- Schema name: `Result`
- Type: null

CoreUnsubscribeResult return fields.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
