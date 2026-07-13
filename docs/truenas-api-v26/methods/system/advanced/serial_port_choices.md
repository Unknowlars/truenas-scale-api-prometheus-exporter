---
title: system.advanced.serial_port_choices
kind: method
source_rst: _sources/api_methods_system.advanced.serial_port_choices.rst.txt
source_html: api_methods_system.advanced.serial_port_choices.html
required_roles:
  - READONLY_ADMIN | SYSTEM_ADVANCED_READ
---

# system.advanced.serial_port_choices

## Summary

Get available choices for `serialport`.

## Required Roles

- `READONLY_ADMIN | SYSTEM_ADVANCED_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Available serial ports for console configuration.
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
