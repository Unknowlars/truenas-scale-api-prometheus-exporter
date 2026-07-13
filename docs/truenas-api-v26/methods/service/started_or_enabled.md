---
title: service.started_or_enabled
kind: method
source_rst: _sources/api_methods_service.started_or_enabled.rst.txt
source_html: api_methods_service.started_or_enabled.html
required_roles:
  - SERVICE_READ
---

# service.started_or_enabled

## Summary

Test if service specified by `service` is started or enabled to start automatically.

## Required Roles

- `SERVICE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: service

#### service

- Schema name: `service`
- Type: string

Name of the service to check if running or enabled.

### Return value

- Schema name: `Result`
- Type: boolean

Service is running or set to start on boot.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
