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

1. Call `core.download` with the target job method, arguments, and desired filename

2. Receive an array containing the job ID and download URL

3. Make an HTTP GET request to the download URL to retrieve the data

4. The download URL expires after a timeout and can only be used once

**Jobs that can be downloaded:**

- :doc:`audit.download_report <api_methods_audit.download_report>`

- :doc:`config.save <api_methods_config.save>`

- :doc:`filesystem.get <api_methods_filesystem.get>`

- :doc:`pool.dataset.export_key <api_methods_pool.dataset.export_key>`

- :doc:`pool.dataset.export_keys <api_methods_pool.dataset.export_keys>`

- :doc:`pool.dataset.export_keys_for_replication <api_methods_pool.dataset.export_keys_for_replication>`

- :doc:`system.debug <api_methods_system.debug>`

- :doc:`vm.log_file_download <api_methods_vm.log_file_download>`

## Required Roles

- None documented.

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: method

#### method

- Schema name: `method`
- Type: string

Name of the job method to execute.
Examples:

```json
"config.save"
```

#### Parameter 2: args

#### args

- Schema name: `args`
- Type: array

Arguments to pass to the job method.
- No Additional Items

##### Each item of this array must be:

- Type: object

#### Parameter 3: filename

#### filename

- Schema name: `filename`
- Type: string

Suggested filename for the downloaded file. Sets the `Content-Disposition` header.
Examples:

```json
"system-config-backup.db"
```

#### Parameter 4: buffered

#### buffered

- Schema name: `buffered`
- Type: boolean
- Default: false

Whether to buffer the job's output. `false` (default): Job starts writing immediately to the download stream. The job blocks until the client downloads the data or 60 seconds elapses. Use for large files or streaming data. `true`: Job output is buffered in RAM until completion, then made available for download. The download URL remains valid for 3600 seconds. Use for small files when you need to ensure the job completes before downloading.

### Return value

- Schema name: `Result`
- Type: array

Array containing the job ID and download URL. First element: Job ID that can be used with `core.get_jobs` to monitor progress Second element: Download URL in the format `/_download/{job_id}?auth_token={token}`
- Must contain a minimum of `2` items
- Must contain a maximum of `2` items
- No Additional Items
- Schema name: `Tuple Validation`

#### Item at 1 must be:

- Type: integer

#### Item at 2 must be:

- Type: string

Examples:

```json
[
    86,
    "/_download/86?auth_token=9WIqYg4jAYEOGQ4g319Bkr64Oj8CZk1VACfyN68M7hgjGTdeSSgZjSf5lJEshS8M"
]
```

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
