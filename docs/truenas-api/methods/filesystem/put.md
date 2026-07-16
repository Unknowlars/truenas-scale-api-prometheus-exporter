---
title: filesystem.put
kind: method
source_rst: _sources/api_methods_filesystem.put.rst.txt
source_html: api_methods_filesystem.put.html
required_roles:
  - FULL_ADMIN
---

# filesystem.put

## Summary

Job to put contents to `path`.

This method is a job.

*This job MUST be used with file upload.* See :ref:`uploading-files`.

## Required Roles

- `FULL_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: path

#### path

- Schema name: `path`
- Type: string

Path where the file should be written.
- Must be at least `1` characters long

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object
- Default: {"append": false, "mode": null}

Options controlling file writing behavior.
- No Additional Properties
##### append

- Schema name: `Append`
- Type: boolean
- Default: false

Whether to append to the file instead of overwriting.

##### mode

- Schema name: `Mode`
- Default: null

Unix permissions to set on the file or `null` to use default.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the file is successfully written.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
