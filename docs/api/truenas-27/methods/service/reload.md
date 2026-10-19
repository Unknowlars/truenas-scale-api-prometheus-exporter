---
title: service.reload
kind: method
source_rst: _sources/api_methods_service.reload.rst.txt
source_html: api_methods_service.reload.html
required_roles:
  - SERVICE_WRITE
  - SHARING_FTP_WRITE
  - SHARING_ISCSI_WRITE
  - SHARING_NFS_WRITE
  - SHARING_SMB_WRITE
---

# service.reload

## Summary

Reload the service specified by `service`.

*DEPRECATED: this method is scheduled to be removed in v26.*

## Required Roles

- `SERVICE_WRITE`
- `SHARING_FTP_WRITE`
- `SHARING_ISCSI_WRITE`
- `SHARING_NFS_WRITE`
- `SHARING_SMB_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: service

<a id="Call_parameters_items_i0"></a>
#### service

- Schema name: `service`
- Type: string

Name of the service to reload.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Options for controlling the reload operation behavior.
- No Additional Properties
<a id="headingCall_parameters_items_i1_ha_propagate"></a>
<a id="Call_parameters_items_i1_ha_propagate"></a>
##### ha_propagate

- Schema name: `Ha Propagate`
- Type: boolean
- Default: true

Whether to propagate the service operation to the HA peer in a high-availability setup.

<a id="headingCall_parameters_items_i1_silent"></a>
<a id="Call_parameters_items_i1_silent"></a>
##### silent

- Schema name: `Silent`
- Type: boolean
- Default: true

Return `false` instead of an error if the operation fails.

<a id="headingCall_parameters_items_i1_timeout"></a>
<a id="Call_parameters_items_i1_timeout"></a>
##### timeout

- Schema name: `Timeout`
- Default: 120

Maximum time in seconds to wait for the service operation to complete. `null` for no timeout.
<a id="Call_parameters_items_i1_timeout_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_timeout_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_timeout_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i1_timeout_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_timeout_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: boolean

The service is running after reload.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
