---
title: vm.log_file_download
kind: method
source_rst: _sources/api_methods_vm.log_file_download.rst.txt
source_html: api_methods_vm.log_file_download.html
required_roles:
  - VM_READ
---

# vm.log_file_download

## Summary

Retrieve log file contents of `id` VM.

It will download empty file if log file does not exist.

This method is a job.

*This job MUST be used with* :doc:`core.download <api_methods_core.download>`.

## Required Roles

- `VM_READ`

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

ID of the virtual machine to download log file for.

### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
