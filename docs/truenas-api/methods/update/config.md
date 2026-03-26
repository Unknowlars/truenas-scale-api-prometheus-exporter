---
title: update.config
kind: method
source_rst: _sources/api_methods_update.config.rst.txt
source_html: api_methods_update.config.html
required_roles:
  - SYSTEM_UPDATE_READ
---

# update.config

## Required Roles

- `SYSTEM_UPDATE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `UpdateEntry`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the update configuration.

#### autocheck (required)

- Schema name: `Autocheck`
- Type: boolean

Automatically check and download updates every night.

#### profile (required)

- Schema name: `Profile`
- Type: string

Update profile used for the system.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
