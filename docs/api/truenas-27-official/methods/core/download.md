---
title: core.download
kind: method
source_rst: _sources/api_methods_core.download.rst.txt
source_html: api_methods_core.download.html
required_roles:
  []
---

# core.download

## Summary

Call a job that produces downloadable output and get a URL to retrieve the result.

This method executes jobs that generate files or streaming data for download. The job writes its output to a pipe, and this method returns a time-limited, single-use download URL.

1. Call [core.download](download.md) with the target job method, arguments, and desired filename

2. Receive an array containing the job ID and download URL

3. Make an HTTP GET request to the download URL to retrieve the data

4. The download URL expires after a timeout and can only be used once

**Jobs that can be downloaded:**

- [audit.download_report](../audit/download_report.md)

- [config.save](../config/save.md)

- [filesystem.get](../filesystem/get.md)

- [pool.dataset.export_key](../pool/dataset/export_key.md)

- [pool.dataset.export_keys](../pool/dataset/export_keys.md)

- [pool.dataset.export_keys_for_replication](../pool/dataset/export_keys_for_replication.md)

- [system.debug](../system/debug.md)

- [vm.log_file_download](../vm/log_file_download.md)

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

#### Parameter 1: method

<a id="Call_parameters_items_i0"></a>
#### method

- Schema name: `method`
- Type: string

Name of the job method to execute.
Examples:

```json
"config.save"
```

#### Parameter 2: args

<a id="Call_parameters_items_i1"></a>
#### args

- Schema name: `args`
- Type: array

Arguments to pass to the job method.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i1_items"></a>
- Type: object

#### Parameter 3: filename

<a id="Call_parameters_items_i2"></a>
#### filename

- Schema name: `filename`
- Type: string

Suggested filename for the downloaded file. Sets the `Content-Disposition` header.
Examples:

```json
"system-config-backup.db"
```

#### Parameter 4: buffered

<a id="Call_parameters_items_i3"></a>
#### buffered

- Schema name: `buffered`
- Type: boolean
- Default: false

Whether to buffer the job's output. `false` (default): Job starts writing immediately to the download stream. The job blocks until the client downloads the data or 60 seconds elapses. Use for large files or streaming data. `true`: Job output is buffered in RAM until completion, then made available for download. The download URL remains valid for 3600 seconds. Use for small files when you need to ensure the job completes before downloading.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array

Array containing the job ID and download URL. First element: Job ID that can be used with `core.get_jobs` to monitor progress Second element: Download URL in the format `/_download/{job_id}?auth_token={token}`
- Must contain a minimum of `2` items
- Must contain a maximum of `2` items
- No Additional Items
- Schema name: `Tuple Validation`

#### Item at 1 must be:

<a id="Return_value_items_i0"></a>
- Type: integer

#### Item at 2 must be:

<a id="Return_value_items_i1"></a>
- Type: string

Examples:

```json
[
    86,
    "/_download/86?auth_token={token}"
]
```

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
