---
title: vm.stop
kind: method
source_rst: _sources/api_methods_vm.stop.rst.txt
source_html: api_methods_vm.stop.html
required_roles:
  - VM_WRITE
---

# vm.stop

## Summary

Stops a VM.

For unresponsive guests who have exceeded the `shutdown_timeout` defined by the user and have become unresponsive, they required to be powered down using :doc:`vm.poweroff <api_methods_vm.poweroff>`. :doc:`vm.stop <api_methods_vm.stop>` is only going to send a shutdown signal to the guest and wait the desired `shutdown_timeout` value before tearing down guest vmemory.

This method is a job.

## Required Roles

- `VM_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the virtual machine to stop.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object
- Default:
```json
{
  "force": false,
  "force_after_timeout": false
}
```

Options controlling the VM stop process.
- No Additional Properties
##### force

- Schema name: `Force`
- Type: boolean
- Default: false

Whether to force immediate shutdown without graceful shutdown attempt.

##### force_after_timeout

- Schema name: `Force After Timeout`
- Type: boolean
- Default: false

Whether to force shutdown if graceful shutdown times out.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful VM stop initiation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
