---
title: sharing.webshare.delete
kind: method
source_rst: _sources/api_methods_sharing.webshare.delete.rst.txt
source_html: api_methods_sharing.webshare.delete.html
required_roles:
  - SHARING_WEBSHARE_WRITE
---

# sharing.webshare.delete

## Summary

Delete SMB Share of `id`. This will forcibly disconnect SMB clients that are accessing the share.

## Required Roles

- `SHARING_WEBSHARE_WRITE`

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

ID of the Webshare share to delete.

### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
