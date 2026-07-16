---
title: container.device.nic_attach_choices
kind: method
source_rst: _sources/api_methods_container.device.nic_attach_choices.rst.txt
source_html: api_methods_container.device.nic_attach_choices.html
required_roles:
  - CONTAINER_DEVICE_READ | READONLY_ADMIN
---

# container.device.nic_attach_choices

## Summary

Available choices for NIC Attach attribute.

## Required Roles

- `CONTAINER_DEVICE_READ | READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `ContainerDeviceNicAttachChoicesResult`
- Type: object

ContainerDeviceNicAttachChoicesResult return fields.
- No Additional Properties
#### BRIDGE (required)

- Schema name: `Bridge`
- Type: array of string

Available bridge interfaces for NIC attachment.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### MACVLAN (required)

- Schema name: `Macvlan`
- Type: array of string

Available parent interfaces for creating MACVLAN NIC devices.
- No Additional Items

##### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
