---
title: service.update
kind: method
source_rst: _sources/api_methods_service.update.rst.txt
source_html: api_methods_service.update.html
required_roles:
  - SERVICE_WRITE
  - SHARING_FTP_WRITE
  - SHARING_ISCSI_WRITE
  - SHARING_NFS_WRITE
  - SHARING_NVME_TARGET_WRITE
  - SHARING_S3_WRITE
  - SHARING_SMB_WRITE
---

# service.update

## Summary

Update service entry of `id_or_name`.

## Required Roles

- `SERVICE_WRITE`
- `SHARING_FTP_WRITE`
- `SHARING_ISCSI_WRITE`
- `SHARING_NFS_WRITE`
- `SHARING_NVME_TARGET_WRITE`
- `SHARING_S3_WRITE`
- `SHARING_SMB_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id_or_name

<a id="Call_parameters_items_i0"></a>
#### id_or_name

- Schema name: `id_or_name`

ID or name of the service to update.
<a id="Call_parameters_items_i0_anyOf"></a>
##### Any of

<a id="tab-pane_Call_parameters_items_i0_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i0_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_anyOf_i1)

- Type: string

#### Parameter 2: service_update

<a id="Call_parameters_items_i1"></a>
#### service_update

- Schema name: `service_update`
- Type: object

Updated configuration for the service.
- No Additional Properties
<a id="headingCall_parameters_items_i1_enable"></a>
<a id="Call_parameters_items_i1_enable"></a>
##### enable (required)

- Schema name: `Enable`
- Type: boolean

Whether the service should start on boot.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: integer

The service ID.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
