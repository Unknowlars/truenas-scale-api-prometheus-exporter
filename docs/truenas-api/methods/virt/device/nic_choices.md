---
title: virt.device.nic_choices
kind: method
source_rst: _sources/api_methods_virt.device.nic_choices.rst.txt
source_html: api_methods_virt.device.nic_choices.html
required_roles:
  - READONLY_ADMIN | VIRT_INSTANCE_READ
---

# virt.device.nic_choices

## Summary

Returns choices for NIC device.

## Required Roles

- `READONLY_ADMIN | VIRT_INSTANCE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: nic_type

#### nic_type

- Schema name: `nic_type`
- Type: enum (of string)

Type of network interface to filter available choices.

### Return value

- Schema name: `Result`
- Type: object

Object of available network interfaces for the specified NIC type.
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
