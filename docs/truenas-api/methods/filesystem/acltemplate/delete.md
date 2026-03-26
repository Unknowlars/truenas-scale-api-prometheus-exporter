---
title: filesystem.acltemplate.delete
kind: method
source_rst: _sources/api_methods_filesystem.acltemplate.delete.rst.txt
source_html: api_methods_filesystem.acltemplate.delete.html
required_roles:
  - FILESYSTEM_ATTRS_WRITE
---

# filesystem.acltemplate.delete

## Required Roles

- `FILESYSTEM_ATTRS_WRITE`

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

ID of the ACL template to delete.

### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the ACL template is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
