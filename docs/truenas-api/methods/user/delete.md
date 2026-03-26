---
title: user.delete
kind: method
source_rst: _sources/api_methods_user.delete.rst.txt
source_html: api_methods_user.delete.html
required_roles:
  - ACCOUNT_WRITE
---

# user.delete

## Summary

Delete user `id`.

The `delete_group` option deletes the user primary group if it is not being used by any other user.

## Required Roles

- `ACCOUNT_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the user account to delete.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

Options controlling the user deletion process.
- No Additional Properties
##### delete_group

- Schema name: `Delete Group`
- Type: boolean
- Default: true

Delete the user primary group if it is not being used by any other user.

### Return value

- Schema name: `Result`
- Type: integer

ID of the deleted user account.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
