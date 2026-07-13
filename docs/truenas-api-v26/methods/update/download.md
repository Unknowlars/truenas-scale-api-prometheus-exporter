---
title: update.download
kind: method
source_rst: _sources/api_methods_update.download.rst.txt
source_html: api_methods_update.download.html
required_roles:
  - SYSTEM_UPDATE_WRITE
---

# update.download

## Summary

Download updates.

This method is a job.

## Required Roles

- `SYSTEM_UPDATE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: train

#### train

- Schema name: `train`
- Default: null

Specifies the train from which to download the update. If both `train` and `version` are `null``, the most recent version that matches the currently selected update profile is used.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### Parameter 2: version

#### version

- Schema name: `version`
- Default: null

Specific version to download. `null` to download the latest version from the specified train.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: boolean

Whether the update download was successfully initiated.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
