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

*This job MUST produce a file for download.* See [downloading-files](https://api.truenas.com/v27.0/jsonrpc.html#downloading-files).

## Required Roles

- `VM_READ`

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

ID of the virtual machine to download log file for.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
