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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the job to download logs for.

#### Parameter 2: filename

#### filename

- Schema name: `filename`
- Type: string

Filename for the downloaded log file.

#### Parameter 3: buffered

#### buffered

- Schema name: `buffered`
- Type: boolean
- Default: false

Whether to buffer the entire log file before download.

### Return value

- Schema name: `Result`
- Type: string

URL for downloading the job log file.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
