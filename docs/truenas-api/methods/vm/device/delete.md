---
title: vm.device.delete
kind: method
source_rst: _sources/api_methods_vm.device.delete.rst.txt
source_html: api_methods_vm.device.delete.html
required_roles:
  - VM_DEVICE_WRITE
---

# vm.device.delete

## Summary

Delete a VM device of `id`.

## Required Roles

- `VM_DEVICE_WRITE`

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

ID of the VM device to delete.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object
- Default:
```json
{
  "force": false,
  "raw_file": false,
  "zvol": false
}
```

Options controlling the device deletion process.
- No Additional Properties
##### force

- Schema name: `Force`
- Type: boolean
- Default: false

Force deletion even if the device is in use.

##### raw_file

- Schema name: `Raw File`
- Type: boolean
- Default: false

Delete the underlying raw disk file when removing the device.

##### zvol

- Schema name: `Zvol`
- Type: boolean
- Default: false

Delete the underlying ZFS volume when removing the device.

### Return value

- Schema name: `Result`
- Type: boolean

Whether the VM device was successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
