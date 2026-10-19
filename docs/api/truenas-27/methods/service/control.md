---
title: service.control
kind: method
source_rst: _sources/api_methods_service.control.rst.txt
source_html: api_methods_service.control.html
required_roles:
  - SERVICE_WRITE
  - SHARING_FTP_WRITE
  - SHARING_ISCSI_WRITE
  - SHARING_NFS_WRITE
  - SHARING_NVME_TARGET_WRITE
  - SHARING_S3_WRITE
  - SHARING_SMB_WRITE
---

# service.control

## Summary

This method is a job.

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

#### Parameter 1: verb

<a id="Call_parameters_items_i0"></a>
#### verb

- Schema name: `verb`
- Type: enum (of string)

The service operation to perform.
##### Must be one of:

- "START"
- "STOP"
- "RESTART"
- "RELOAD"

#### Parameter 2: service

<a id="Call_parameters_items_i1"></a>
#### service

- Schema name: `service`
- Type: string

Name of the service to control.

#### Parameter 3: options

<a id="Call_parameters_items_i2"></a>
#### options

- Schema name: `options`
- Type: object

Options for controlling the service operation behavior.
- No Additional Properties
<a id="headingCall_parameters_items_i2_ha_propagate"></a>
<a id="Call_parameters_items_i2_ha_propagate"></a>
##### ha_propagate

- Schema name: `Ha Propagate`
- Type: boolean
- Default: true

Whether to propagate the service operation to the HA peer in a high-availability setup.

<a id="headingCall_parameters_items_i2_silent"></a>
<a id="Call_parameters_items_i2_silent"></a>
##### silent

- Schema name: `Silent`
- Type: boolean
- Default: true

Return `false` instead of an error if the operation fails.

<a id="headingCall_parameters_items_i2_timeout"></a>
<a id="Call_parameters_items_i2_timeout"></a>
##### timeout

- Schema name: `Timeout`
- Default: 120

Maximum time in seconds to wait for the service operation to complete. `null` for no timeout.
<a id="Call_parameters_items_i2_timeout_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i2_timeout_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i2_timeout_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i2_timeout_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i2_timeout_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: boolean

For "START", "RESTART", "RELOAD", indicate whether the service is running after performing the operation. For "STOP", indicate whether the service was successfully stopped.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
