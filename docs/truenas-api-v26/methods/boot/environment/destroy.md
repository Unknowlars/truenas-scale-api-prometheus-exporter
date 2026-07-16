---
title: boot.environment.destroy
kind: method
source_rst: _sources/api_methods_boot.environment.destroy.rst.txt
source_html: api_methods_boot.environment.destroy.html
required_roles:
  - BOOT_ENV_WRITE
---

# boot.environment.destroy

## Summary

Permanently destroy the boot environment identified by `id`, freeing the space it consumes.

The active (currently running) boot environment cannot be destroyed; attempting to do so returns a JSON-RPC `error` response (code `-32602`, *Invalid params*).

## Required Roles

- `BOOT_ENV_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: boot_environment_destroy

#### boot_environment_destroy

- Schema name: `boot_environment_destroy`
- Type: object

BootEnvironmentDestroyArgs parameters.
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: string

Name of the boot environment to destroy.
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the boot environment is successfully destroyed.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
