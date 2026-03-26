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

This method is a job.

*This job MUST be used with file upload.* See :ref:`uploading-files`.

## Required Roles

- `FULL_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the configuration file is successfully uploaded.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
