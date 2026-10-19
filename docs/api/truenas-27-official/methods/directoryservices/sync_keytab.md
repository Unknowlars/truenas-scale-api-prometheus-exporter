---
title: directoryservices.sync_keytab
kind: method
source_rst: _sources/api_methods_directoryservices.sync_keytab.rst.txt
source_html: api_methods_directoryservices.sync_keytab.html
required_roles:
  - DIRECTORY_SERVICE_WRITE
---

# directoryservices.sync_keytab

## Summary

Sync local keytab with remote domain controller. This is required if additional kerberos SPNs were added to the truenas account in the remote domain controller after joining the directory service.

This is currently only implemented for active directory.

This method is a job.

## Required Roles

- `DIRECTORY_SERVICE_WRITE`

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

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
