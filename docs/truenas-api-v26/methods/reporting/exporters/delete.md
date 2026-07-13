---
title: reporting.exporters.delete
kind: method
source_rst: _sources/api_methods_reporting.exporters.delete.rst.txt
source_html: api_methods_reporting.exporters.delete.html
required_roles:
  - REPORTING_WRITE
---

# reporting.exporters.delete

## Summary

Delete Reporting Exporter of `id`.

## Required Roles

- `REPORTING_WRITE`

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

ID of the reporting exporter to delete.

### Return value

- Schema name: `Result`
- Type: boolean

Whether the reporting exporter was successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
