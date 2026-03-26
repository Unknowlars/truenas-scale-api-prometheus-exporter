---
title: kerberos.realm.delete
kind: method
source_rst: _sources/api_methods_kerberos.realm.delete.rst.txt
source_html: api_methods_kerberos.realm.delete.html
required_roles:
  - DIRECTORY_SERVICE_WRITE
---

# kerberos.realm.delete

## Summary

Delete a kerberos realm by ID.

## Required Roles

- `DIRECTORY_SERVICE_WRITE`

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

ID of the Kerberos realm to delete.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the Kerberos realm is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
