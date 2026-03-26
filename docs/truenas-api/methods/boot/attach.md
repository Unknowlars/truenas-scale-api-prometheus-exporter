---
title: boot.attach
kind: method
source_rst: _sources/api_methods_boot.attach.rst.txt
source_html: api_methods_boot.attach.html
required_roles:
  - DISK_WRITE
---

# boot.attach

## Summary

Attach a disk to the boot pool, turning a stripe into a mirror.

`expand` option will determine whether the new disk partition will be the maximum available or the same size as the current disk.

This method is a job.

## Required Roles

- `DISK_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: dev

#### dev

- Schema name: `dev`
- Type: string

Device name or path to attach to the boot pool.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

Options for the attach operation.
- No Additional Properties
##### expand

- Schema name: `Expand`
- Type: boolean
- Default: false

Whether to expand the boot pool after attaching the disk.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the disk is successfully attached to the boot pool.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
