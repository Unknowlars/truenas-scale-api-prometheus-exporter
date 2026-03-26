---
title: virt.instance.start
kind: method
source_rst: _sources/api_methods_virt.instance.start.rst.txt
source_html: api_methods_virt.instance.start.html
required_roles:
  - VIRT_INSTANCE_WRITE
---

# virt.instance.start

## Summary

Start an instance.

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

ID of the virtual instance to start.

### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` if the instance was successfully started.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
