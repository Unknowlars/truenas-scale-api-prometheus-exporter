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

The active (currently running) and activated (next boot) boot environments cannot be destroyed; attempting to do so returns an `EINVAL` error.

## Required Roles

- `BOOT_ENV_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: boot_environment_destroy

<a id="Call_parameters_items_i0"></a>
#### boot_environment_destroy

- Schema name: `boot_environment_destroy`
- Type: object

BootEnvironmentDestroyArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_id"></a>
<a id="Call_parameters_items_i0_id"></a>
##### id (required)

- Schema name: `Id`
- Type: string

Name of the boot environment to destroy.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the boot environment is successfully destroyed.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
