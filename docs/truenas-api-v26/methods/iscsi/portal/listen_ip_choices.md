---
title: iscsi.portal.listen_ip_choices
kind: method
source_rst: _sources/api_methods_iscsi.portal.listen_ip_choices.rst.txt
source_html: api_methods_iscsi.portal.listen_ip_choices.html
required_roles:
  - READONLY_ADMIN | SHARING_ISCSI_PORTAL_READ
---

# iscsi.portal.listen_ip_choices

## Summary

Returns possible choices for `listen.ip` attribute of portal create and update.

## Required Roles

- `READONLY_ADMIN | SHARING_ISCSI_PORTAL_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Object mapping IP addresses to their underlying constituents. Only static IP addresses will be included. On ALUA-enabled high availability systems, VIPs will be mapped to the pair of corresponding underlying addresses, one per node.
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
