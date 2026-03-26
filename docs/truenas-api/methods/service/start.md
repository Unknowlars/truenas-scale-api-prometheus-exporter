---
title: service.start
kind: method
source_rst: _sources/api_methods_service.start.rst.txt
source_html: api_methods_service.start.html
required_roles:
  - SERVICE_WRITE | SHARING_FTP_WRITE | SHARING_ISCSI_WRITE | SHARING_NFS_WRITE | SHARING_SMB_WRITE
---

# service.start

## Summary

Start the service specified by `service`.

*DEPRECATED: this method is scheduled to be removed in v26.04.*

## Required Roles

- `SERVICE_WRITE | SHARING_FTP_WRITE | SHARING_ISCSI_WRITE | SHARING_NFS_WRITE | SHARING_SMB_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: service

#### service

- Schema name: `service`
- Type: string

Name of the service to start.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

Options for controlling the start operation behavior.
- No Additional Properties
##### ha_propagate

- Schema name: `Ha Propagate`
- Type: boolean
- Default: true

Whether to propagate the service operation to the HA peer in a high-availability setup.

##### silent

- Schema name: `Silent`
- Type: boolean
- Default: true

Return `false` instead of an error if the operation fails.

##### timeout

- Schema name: `Timeout`
- Default: 120

Maximum time in seconds to wait for the service operation to complete. `null` for no timeout.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: boolean

`true` if the service started successfully.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
