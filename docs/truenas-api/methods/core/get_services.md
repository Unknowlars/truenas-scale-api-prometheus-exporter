---
title: core.get_services
kind: method
source_rst: _sources/api_methods_core.get_services.rst.txt
source_html: api_methods_core.get_services.html
required_roles:
  []
---

# core.get_services

## Summary

Returns a list of all registered services.

## Required Roles

- None documented.

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: target

#### target

- Schema name: `target`
- Type: enum (of string)
- Default: "WS"

Target interface to get services for. `WS` for WebSocket, `CLI` for command line, `REST` for HTTP API.

### Return value

- Schema name: `Result`
- Type: object

Object mapping service names to their configuration and available methods.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
