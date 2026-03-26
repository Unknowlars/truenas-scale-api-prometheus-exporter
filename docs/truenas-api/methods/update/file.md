---
title: update.file
kind: method
source_rst: _sources/api_methods_update.file.rst.txt
source_html: api_methods_update.file.html
required_roles:
  - SYSTEM_UPDATE_WRITE
---

# update.file

## Summary

Updates the system using the uploaded .tar file.

This method is a job.

## Required Roles

- `SYSTEM_UPDATE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: options

#### options

- Schema name: `options`
- Type: object
- Default: {"resume": false, "destination": null}

Options for controlling the manual update file upload process.
- No Additional Properties
##### resume

- Schema name: `Resume`
- Type: boolean
- Default: false

Should be set to `true` if a previous call to this method returned a `CallError` with `errno=EAGAIN` meaning that an upgrade can be performed with a warning and that warning is accepted. In that case, re-uploading the file is not necessary.

##### destination

- Schema name: `Destination`
- Default: null

Create a temporary location by default.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful update file upload and validation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
