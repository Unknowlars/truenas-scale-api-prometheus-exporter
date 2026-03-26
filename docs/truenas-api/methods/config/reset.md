---
title: config.reset
kind: method
source_rst: _sources/api_methods_config.reset.rst.txt
source_html: api_methods_config.reset.html
required_roles:
  - FULL_ADMIN
---

# config.reset

## Summary

Reset database to configuration defaults.

If `reboot` is true this job will reboot the system after its completed with a delay of 10 seconds.

This method is a job.

## Required Roles

- `FULL_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: options

#### options

- Schema name: `options`
- Type: object
- Default: {"reboot": true}

Options controlling the configuration reset behavior.
- No Additional Properties
##### reboot

- Schema name: `Reboot`
- Type: boolean
- Default: true

Whether to reboot the system after resetting configuration.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the configuration reset is successfully initiated.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
