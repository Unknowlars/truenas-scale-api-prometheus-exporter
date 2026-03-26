---
title: reporting.exporters.exporter_schemas
kind: method
source_rst: _sources/api_methods_reporting.exporters.exporter_schemas.rst.txt
source_html: api_methods_reporting.exporters.exporter_schemas.html
required_roles:
  - REPORTING_READ
---

# reporting.exporters.exporter_schemas

## Summary

Get the schemas for all the reporting export types we support with their respective attributes required for successfully exporting reporting metrics to them.

## Required Roles

- `REPORTING_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: array of object

Array of available exporter schema definitions.
- No Additional Items

#### Each item of this array must be:

#### ReportingExporterSchema

- Schema name: `ReportingExporterSchema`
- Type: object
- No Additional Properties
##### key (required)

- Schema name: `Key`
- Type: string

Unique key identifying the exporter type.

##### schema (required)

- Schema name: `Schema`
- Type: array of object

Array of attribute definitions for this exporter type.
- No Additional Items

###### Each item of this array must be:

###### ReportingExporterAttributeSchema

- Schema name: `ReportingExporterAttributeSchema`
- Type: object
####### _name_ (required)

- Schema name: `Name`
- Type: string

Internal name of the exporter attribute.

####### title (required)

- Schema name: `Title`
- Type: string

Human-readable title for the attribute.

####### _required_ (required)

- Schema name: `Required`
- Type: boolean

Whether this attribute is required for the exporter configuration.

####### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
