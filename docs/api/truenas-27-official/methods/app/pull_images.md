---
title: app.pull_images
kind: method
source_rst: _sources/api_methods_app.pull_images.rst.txt
source_html: api_methods_app.pull_images.html
required_roles:
  - APPS_WRITE
---

# app.pull_images

## Summary

Pulls docker images for the specified app `name`.

This method is a job.

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

#### Parameter 1: app_name

<a id="Call_parameters_items_i0"></a>
#### app_name

- Schema name: `app_name`
- Type: string

Name of the application to pull images for.
- Must be at least `1` characters long

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object
- Default: {"redeploy": true}

Options for pulling images including whether to redeploy.
- No Additional Properties
<a id="headingCall_parameters_items_i1_redeploy"></a>
<a id="Call_parameters_items_i1_redeploy"></a>
##### redeploy

- Schema name: `Redeploy`
- Type: boolean
- Default: true

Whether to redeploy the application after pulling new images.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the application images are successfully pulled.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
