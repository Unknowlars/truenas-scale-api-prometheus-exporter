---
title: audit.download_report
kind: method
source_rst: _sources/api_methods_audit.download_report.rst.txt
source_html: api_methods_audit.download_report.html
required_roles:
  - SYSTEM_AUDIT_READ
---

# audit.download_report

## Summary

Download the audit report with the specified name from the server. Note that users will only be able to download reports that they personally generated.

This method is a job.

*This job MUST be used with* [core.download](../core/download.md).

## Required Roles

- `SYSTEM_AUDIT_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

<a id="Call_parameters_items_i0"></a>
#### data

- Schema name: `data`
- Type: object

AuditDownloadReportArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_report_name"></a>
<a id="Call_parameters_items_i0_report_name"></a>
##### report_name (required)

- Schema name: `Report Name`
- Type: string

Name of the audit report to download.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the audit report download is initiated.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
