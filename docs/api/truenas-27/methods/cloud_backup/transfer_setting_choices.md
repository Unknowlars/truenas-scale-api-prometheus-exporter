---
title: cloud_backup.transfer_setting_choices
kind: method
source_rst: _sources/api_methods_cloud_backup.transfer_setting_choices.rst.txt
source_html: api_methods_cloud_backup.transfer_setting_choices.html
required_roles:
  - CLOUD_BACKUP_READ
  - READONLY_ADMIN
---

# cloud_backup.transfer_setting_choices

## Summary

Return all possible choices for `cloud_backup.create.transfer_setting`.

## Required Roles

- `CLOUD_BACKUP_READ`
- `READONLY_ADMIN`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of enum (of string)

All possible values for `cloud_backup.create.transfer_setting`.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
- Type: enum (of string)
##### Must be one of:

- "DEFAULT"
- "PERFORMANCE"
- "FAST_STORAGE"

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
