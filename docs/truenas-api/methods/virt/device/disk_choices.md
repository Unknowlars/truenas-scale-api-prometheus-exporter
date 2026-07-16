---
title: virt.device.disk_choices
kind: method
source_rst: _sources/api_methods_virt.device.disk_choices.rst.txt
source_html: api_methods_virt.device.disk_choices.html
required_roles:
  - READONLY_ADMIN | VIRT_INSTANCE_READ
---

# virt.device.disk_choices

## Summary

Returns disk choices available for device type "DISK" for virtual machines. This includes both available virt volumes and zvol choices. Disk choices for containers depend on the mounted file tree (paths).

## Required Roles

- `READONLY_ADMIN | VIRT_INSTANCE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Object of available disk devices and storage volumes for virtualization.
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
