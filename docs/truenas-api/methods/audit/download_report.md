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

*This job MUST be used with* :doc:`core.download <api_methods_core.download>`.

## Required Roles

- `SYSTEM_AUDIT_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`
- Type: object

AuditDownloadReportArgs parameters.
- No Additional Properties
##### report_name (required)

- Schema name: `Report Name`
- Type: string

Name of the audit report to download.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the audit report download is initiated.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
