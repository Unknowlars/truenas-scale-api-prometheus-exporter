---
title: config.upload
kind: method
source_rst: _sources/api_methods_config.upload.rst.txt
source_html: api_methods_config.upload.html
required_roles:
  - FULL_ADMIN
---

# config.upload

## Summary

Accepts a configuration file via job pipe.

The file must be an archive saved by [config.save](save.md) that carries the password secret seed belonging to the database it contains. A bare database, or one accompanied by a different seed, is rejected before anything on this system is replaced.

This method is a job.

*This job MUST be used with file upload.* See [uploading-files](../../shared/jobs.md#uploading-files).

## Required Roles

- `FULL_ADMIN`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the configuration file is successfully uploaded.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
