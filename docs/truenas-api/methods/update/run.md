---
title: update.run
kind: method
source_rst: _sources/api_methods_update.run.rst.txt
source_html: api_methods_update.run.html
required_roles:
  - SYSTEM_UPDATE_WRITE
---

# update.run

## Summary

Downloads (if not already in cache) and apply an update.

This method is a job.

## Required Roles

- `SYSTEM_UPDATE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: attrs

#### attrs

- Schema name: `attrs`
- Type: object
- Default:
```json
{
  "dataset_name": null,
  "resume": false,
  "train": null,
  "version": null,
  "reboot": false
}
```

Attributes controlling the system update execution process.
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

Should be set to `true` if a previous call to this method returned a `CallError` with `errno=EAGAIN` meaning that an upgrade can be performed with a warning and that warning is accepted. In that case, update process will be continued using an already downloaded file without performing any extra checks.

##### train

- Schema name: `Train`
- Default: null

Specifies the train from which to download the update. If both `train` and `version` are `null``, the most recent version that matches the currently selected update profile is used.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### version

- Schema name: `Version`
- Default: null

Specific version to update to. `null` to use the latest version from the specified train.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### reboot

- Schema name: `Reboot`
- Type: boolean
- Default: false

Whether to automatically reboot the system after applying the update.

### Return value

- Schema name: `Result`
- Type: const

Always returns true on successful update process initiation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
