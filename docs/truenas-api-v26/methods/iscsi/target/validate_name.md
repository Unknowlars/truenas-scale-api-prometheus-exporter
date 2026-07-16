---
title: iscsi.target.validate_name
kind: method
source_rst: _sources/api_methods_iscsi.target.validate_name.rst.txt
source_html: api_methods_iscsi.target.validate_name.html
required_roles:
  - SHARING_ISCSI_TARGET_WRITE
---

# iscsi.target.validate_name

## Summary

Return a validation error message for the given iSCSI target name or `null` if the name is valid.

## Required Roles

- `SHARING_ISCSI_TARGET_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: name

#### name

- Schema name: `name`
- Type: string

Target name to validate.

#### Parameter 2: existing_id

#### existing_id

- Schema name: `existing_id`
- Default: null

ID of existing target to exclude from validation or `null` for new targets.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

### Return value

- Schema name: `Result`

Error message if name is invalid or `null` if name is valid.
#### Any of

##### Option 1

- Type: string

##### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
