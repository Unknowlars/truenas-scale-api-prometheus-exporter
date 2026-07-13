---
title: kerberos.keytab.delete
kind: method
source_rst: _sources/api_methods_kerberos.keytab.delete.rst.txt
source_html: api_methods_kerberos.keytab.delete.html
required_roles:
  - DIRECTORY_SERVICE_WRITE
---

# kerberos.keytab.delete

## Summary

Delete kerberos keytab by id, and force regeneration of system keytab.

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

ID of the Kerberos keytab entry to delete.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the Kerberos keytab entry is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
