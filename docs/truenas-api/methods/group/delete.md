---
title: group.delete
kind: method
source_rst: _sources/api_methods_group.delete.rst.txt
source_html: api_methods_group.delete.html
required_roles:
  - ACCOUNT_WRITE
---

# group.delete

## Summary

Delete group `id`.

The `delete_users` option deletes all users that have this group as their primary group.

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

API identifier of the group to delete.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object
- Default: {"delete_users": false}

Options controlling group deletion behavior.
- No Additional Properties
##### delete_users

- Schema name: `Delete Users`
- Type: boolean
- Default: false

Deletes all users that have this group as their primary group.

### Return value

- Schema name: `Result`
- Type: integer

The API identifier of the deleted group.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
