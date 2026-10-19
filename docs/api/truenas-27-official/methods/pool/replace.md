---
title: pool.replace
kind: method
source_rst: _sources/api_methods_pool.replace.rst.txt
source_html: api_methods_pool.replace.html
required_roles:
  - POOL_WRITE
---

# pool.replace

## Summary

Replace a disk on a pool.

Replace missing ZFS device with disk {serial}FOO::

{ "jsonrpc": "2.0", "id": 1, "method": "pool.replace", "params": [1, { "label": "80802394992848654", "disk": "{serial}FOO" }] }

This method is a job.

## Required Roles

- `POOL_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the pool to replace a disk in.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Configuration for the disk replacement operation.
- No Additional Properties
<a id="headingCall_parameters_items_i1_label"></a>
<a id="Call_parameters_items_i1_label"></a>
##### label (required)

- Schema name: `Label`
- Type: string

GUID or device name of the disk to replace.

<a id="headingCall_parameters_items_i1_disk"></a>
<a id="Call_parameters_items_i1_disk"></a>
##### disk (required)

- Schema name: `Disk`
- Type: string

Name of the new disk to use as replacement.

<a id="headingCall_parameters_items_i1_force"></a>
<a id="Call_parameters_items_i1_force"></a>
##### force

- Schema name: `Force`
- Type: boolean
- Default: false

Force the replacement even if the new disk appears to be in use.

<a id="headingCall_parameters_items_i1_preserve_settings"></a>
<a id="Call_parameters_items_i1_preserve_settings"></a>
##### preserve_settings

- Schema name: `Preserve Settings`
- Type: boolean
- Default: true

Whether to preserve disk settings from the replaced disk.

<a id="headingCall_parameters_items_i1_preserve_description"></a>
<a id="Call_parameters_items_i1_preserve_description"></a>
##### preserve_description

- Schema name: `Preserve Description`
- Type: boolean
- Default: true

Whether to preserve the description from the replaced disk.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: const

Indicates successful disk replacement initiation.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
