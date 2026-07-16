---
title: audit.export
kind: method
source_rst: _sources/api_methods_audit.export.rst.txt
source_html: api_methods_audit.export.html
required_roles:
  - SYSTEM_AUDIT_READ
---

# audit.export

## Summary

Generate an audit report based on the specified `query-filters` and `query-options` for the specified `services` in the specified `export_format`.

Supported export_formats are CSV, JSON, and YAML. The endpoint returns a local filesystem path where the resulting audit report is located.

This method is a job.

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
- Default:
```json
{
  "services": [
    "MIDDLEWARE"
  ],
  "query-filters": [],
  "query-options": {
    "force_sql_filters": false,
    "limit": 0,
    "offset": 0,
    "order_by": [],
    "select": []
  },
  "remote_controller": false,
  "export_format": "JSON"
}
```

Audit export configuration specifying services, filters, and format.
- No Additional Properties
##### services

- Schema name: `Services`
- Type: array of enum (of string)
- Default: ["MIDDLEWARE"]

Array of services to include in the audit query.
- No Additional Items

###### Each item of this array must be:

- Type: enum (of string)

##### query-filters

- Schema name: `Query-Filters`
- Type: array
- Default: []

Array of filters to apply to the audit query results.
- No Additional Items

###### Each item of this array must be:

- Type: object

Examples:

```json
[
    [
        "name",
        "=",
        "bob"
    ]
]
```
Examples:

```json
[
    [
        "OR",
        [
            [
                "name",
                "=",
                "bob"
            ],
            [
                "name",
                "=",
                "larry"
            ]
        ]
    ]
]
```

##### query-options

- Schema name: `AuditExportQueryOptions`
- Type: object
- Default:
```json
{
  "order_by": [],
  "select": [],
  "offset": 0,
  "limit": 0,
  "force_sql_filters": false
}
```
- No Additional Properties
###### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

####### Each item of this array must be:

- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

###### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

####### Each item of this array must be:

######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: array
- No Additional Items

########## Each item of this array must be:

- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

###### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0`

###### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0` and lesser or equal to `10000`

###### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

##### remote_controller

- Schema name: `Remote Controller`
- Type: boolean
- Default: false

HA systems may direct the query to the 'remote' controller by including 'remote_controller=True'. The default is the 'current' controller.

##### export_format

- Schema name: `Export Format`
- Type: enum (of string)
- Default: "JSON"

Format for exporting audit data.

### Return value

- Schema name: `Result`
- Type: string

Path to the exported audit data file.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
