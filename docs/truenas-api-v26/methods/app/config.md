---
title: app.config
kind: method
source_rst: _sources/api_methods_app.config.rst.txt
source_html: api_methods_app.config.html
required_roles:
  - APPS_READ
---

# app.config

## Summary

Retrieve user specified configuration of `app_name`.

## Required Roles

- `APPS_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: app_name

#### app_name

- Schema name: `app_name`
- Type: string

Name of the application to retrieve configuration for.
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: object

The current configuration object for the application.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
