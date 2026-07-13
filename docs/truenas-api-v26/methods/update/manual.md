---
title: update.manual
kind: method
source_rst: _sources/api_methods_update.manual.rst.txt
source_html: api_methods_update.manual.html
required_roles:
  - SYSTEM_UPDATE_WRITE
---

# update.manual

## Summary

Update the system using a manual update file.

This method is a job.

## Required Roles

- `SYSTEM_UPDATE_WRITE`

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

The absolute path to the update file.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object
- Default:
```json
{
  "dataset_name": null,
  "resume": false,
  "cleanup": true
}
```

Options for controlling the manual update process.
- No Additional Properties
##### dataset_name

- Schema name: `Dataset Name`
- Default: null

Name of the ZFS dataset to use for the new boot environment. `null` for automatic naming.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### resume

- Schema name: `Resume`
- Type: boolean
- Default: false

Should be set to `true` if a previous call to this method returned a `CallError` with `errno=EAGAIN` meaning that an upgrade can be performed with a warning and that warning is accepted.

##### cleanup

- Schema name: `Cleanup`
- Type: boolean
- Default: true

If set to `false`, the manual update file won't be removed on update success and newly created BE won't be removed on update failure (useful for debugging purposes).

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful manual update initiation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
