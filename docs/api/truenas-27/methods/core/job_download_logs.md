---
title: core.job_download_logs
kind: method
source_rst: _sources/api_methods_core.job_download_logs.rst.txt
source_html: api_methods_core.job_download_logs.html
required_roles:
  []
---

# core.job_download_logs

## Summary

Download logs of the job `id`.

Please see `core.download` method documentation for explanation on `filename` and `buffered` arguments, and return value.

## Required Roles

- None documented.

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the job to download logs for.

#### Parameter 2: filename

<a id="Call_parameters_items_i1"></a>
#### filename

- Schema name: `filename`
- Type: string

Filename for the downloaded log file.

#### Parameter 3: buffered

<a id="Call_parameters_items_i2"></a>
#### buffered

- Schema name: `buffered`
- Type: boolean
- Default: false

Whether to buffer the entire log file before download.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: string

URL for downloading the job log file.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
