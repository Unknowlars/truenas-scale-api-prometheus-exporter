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

`options.force` when set will force delete the image regardless of the state of containers and should be used cautiously.

## Required Roles

- `APPS_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: image_id

#### image_id

- Schema name: `image_id`
- Type: string

Container image ID or reference to delete.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object
- Default: {"force": false}

Deletion options controlling force removal behavior.
- No Additional Properties
##### force

- Schema name: `Force`
- Type: boolean
- Default: false

Whether to force deletion even if the image is in use by containers.

### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the container image is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
