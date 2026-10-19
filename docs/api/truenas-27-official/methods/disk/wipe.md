---
title: disk.wipe
kind: method
source_rst: _sources/api_methods_disk.wipe.rst.txt
source_html: api_methods_disk.wipe.html
required_roles:
  - DISK_WRITE
---

# disk.wipe

## Summary

Performs a wipe of a disk `dev`.

This method is a job.

## Required Roles

- `DISK_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: dev

<a id="Call_parameters_items_i0"></a>
#### dev

- Schema name: `dev`
- Type: string

The device to perform the disk wipe operation on. May be passed as /dev/sda or just sda.
- Must be at least `1` characters long

#### Parameter 2: mode

<a id="Call_parameters_items_i1"></a>
#### mode

- Schema name: `mode`
- Type: enum (of string)

QUICK: Write zeros to the first and last 32MB of device. FULL: Write whole disk with zeros. FULL_RANDOM: Write whole disk with random bytes.
##### Must be one of:

- "QUICK"
- "FULL"
- "FULL_RANDOM"

#### Parameter 3: synccache

<a id="Call_parameters_items_i2"></a>
#### synccache

- Schema name: `synccache`
- Type: boolean
- Default: true

Synchronize the device with the database.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the disk wipe operation is successfully started.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
