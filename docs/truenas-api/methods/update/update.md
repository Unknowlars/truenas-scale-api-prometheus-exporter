---
title: update.update
kind: method
source_rst: _sources/api_methods_update.update.rst.txt
source_html: api_methods_update.update.html
required_roles:
  - SYSTEM_UPDATE_WRITE
---

# update.update

## Summary

Update update configuration.

## Required Roles

- `SYSTEM_UPDATE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`
- Type: object

Updated configuration for system update settings.
- No Additional Properties
##### autocheck

- Schema name: `Autocheck`
- Type: boolean

Automatically check and download updates every night.

##### profile

- Schema name: `Profile`
- Type: string

Update profile used for the system.

### Return value

- Schema name: `UpdateEntry`
- Type: object

The updated system update configuration.
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
