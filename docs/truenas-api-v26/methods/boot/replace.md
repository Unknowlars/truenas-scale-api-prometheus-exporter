---
title: boot.replace
kind: method
source_rst: _sources/api_methods_boot.replace.rst.txt
source_html: api_methods_boot.replace.html
required_roles:
  - DISK_WRITE
---

# boot.replace

## Summary

Replace device `label` on boot pool with `dev`.

This method is a job.

## Required Roles

- `DISK_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: label

#### label

- Schema name: `label`
- Type: string

Label of the disk in the boot pool to replace.

#### Parameter 2: dev

#### dev

- Schema name: `dev`
- Type: string

Device name or path of the replacement disk.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the disk replacement is successfully initiated.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
