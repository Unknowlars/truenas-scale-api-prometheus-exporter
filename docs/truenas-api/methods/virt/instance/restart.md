---
title: virt.instance.restart
kind: method
source_rst: _sources/api_methods_virt.instance.restart.rst.txt
source_html: api_methods_virt.instance.restart.html
required_roles:
  - VIRT_INSTANCE_WRITE
---

# virt.instance.restart

## Summary

Restart an instance.

Timeout is how long it should wait for the instance to shutdown cleanly.

This method is a job.

## Required Roles

- `VIRT_INSTANCE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: string

ID of the virtual instance to stop.

#### Parameter 2: stop_args

#### stop_args

- Schema name: `stop_args`
- Type: object
- Default: {"timeout": -1, "force": false}

Arguments controlling how the instance is stopped.
- No Additional Properties
##### timeout

- Schema name: `Timeout`
- Type: integer
- Default: -1

Timeout in seconds to wait for graceful shutdown (-1 for no timeout when `force = true`).

##### force

- Schema name: `Force`
- Type: boolean
- Default: false

Whether to force stop the instance immediately without graceful shutdown.

### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` if the instance was successfully restarted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
