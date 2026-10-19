---
title: app.image.delete
kind: method
source_rst: _sources/api_methods_app.image.delete.rst.txt
source_html: api_methods_app.image.delete.html
required_roles:
  - APPS_WRITE
---

# app.image.delete

## Summary

Delete docker image `image_id`.

## Required Roles

- `APPS_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: image_id

<a id="Call_parameters_items_i0"></a>
#### image_id

- Schema name: `image_id`
- Type: string

Container image ID or reference to delete.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object
- Default: {"force": false}

Deletion options controlling force removal behavior.
- No Additional Properties
<a id="headingCall_parameters_items_i1_force"></a>
<a id="Call_parameters_items_i1_force"></a>
##### force

- Schema name: `Force`
- Type: boolean
- Default: false

Whether to force deletion even if the image is in use by containers.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the container image is successfully deleted.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
