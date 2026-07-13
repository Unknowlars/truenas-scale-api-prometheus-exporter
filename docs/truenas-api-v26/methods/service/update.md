---
title: service.update
kind: method
source_rst: _sources/api_methods_service.update.rst.txt
source_html: api_methods_service.update.html
required_roles:
  - SERVICE_WRITE | SHARING_FTP_WRITE | SHARING_ISCSI_WRITE | SHARING_NFS_WRITE | SHARING_NVME_TARGET_WRITE | SHARING_SMB_WRITE
---

# service.update

## Summary

Update service entry of `id_or_name`.

## Required Roles

- `SERVICE_WRITE | SHARING_FTP_WRITE | SHARING_ISCSI_WRITE | SHARING_NFS_WRITE | SHARING_NVME_TARGET_WRITE | SHARING_SMB_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id_or_name

#### id_or_name

- Schema name: `id_or_name`

ID or name of the service to update.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: string

#### Parameter 2: service_update

#### service_update

- Schema name: `service_update`
- Type: object

Updated configuration for the service.
- No Additional Properties
##### enable (required)

- Schema name: `Enable`
- Type: boolean

Whether the service should start on boot.

### Return value

- Schema name: `Result`
- Type: integer

The service ID.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
