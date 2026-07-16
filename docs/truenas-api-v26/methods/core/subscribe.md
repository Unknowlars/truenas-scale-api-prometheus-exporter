---
title: core.subscribe
kind: method
source_rst: _sources/api_methods_core.subscribe.rst.txt
source_html: api_methods_core.subscribe.html
required_roles:
  []
---

# core.subscribe

## Summary

Subscribe the current connection to the named `event` and return a subscription identifier.

Matching event notifications are pushed to this connection until the subscription is removed with :doc:`core.unsubscribe <api_methods_core.unsubscribe>`. A JSON-RPC `error` response (code `-32001`, *Method call error*) is returned if the caller is not authorized to subscribe to the event.

## Required Roles

- None documented.

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: event

#### event

- Schema name: `event`
- Type: string

Event name to subscribe to for real-time updates.

### Return value

- Schema name: `Result`
- Type: string

CoreSubscribeResult return fields.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
