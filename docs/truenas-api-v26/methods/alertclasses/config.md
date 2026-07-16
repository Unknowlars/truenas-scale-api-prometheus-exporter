---
title: alertclasses.config
kind: method
source_rst: _sources/api_methods_alertclasses.config.rst.txt
source_html: api_methods_alertclasses.config.html
required_roles:
  - ALERT_READ
---

# alertclasses.config

## Required Roles

- `ALERT_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `AlertClassesEntry`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the alert classes configuration.

#### classes (required)

- Schema name: `Classes`
- Type: object

Object mapping alert class names to their configuration settings.
##### Additional Properties

Each additional property must conform to the following schema
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
