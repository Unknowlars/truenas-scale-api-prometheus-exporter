---
title: container.device.gpu_choices
kind: method
source_rst: _sources/api_methods_container.device.gpu_choices.rst.txt
source_html: api_methods_container.device.gpu_choices.html
required_roles:
  - CONTAINER_DEVICE_READ | READONLY_ADMIN
---

# container.device.gpu_choices

## Summary

Available choices for GPU devices.

## Required Roles

- `CONTAINER_DEVICE_READ | READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Available GPU(s) for container attachment.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
