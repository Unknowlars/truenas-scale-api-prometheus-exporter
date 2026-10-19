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
<a id="headingCall_parameters_items_i0_services"></a>
<a id="Call_parameters_items_i0_services"></a>
##### services

- Schema name: `Services`
- Type: array of enum (of string)
- Default: ["MIDDLEWARE"]

Array of services to include in the audit query.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_services_items"></a>
- Type: enum (of string)
###### Must be one of:

- "MIDDLEWARE"
- "SMB"
- "SUDO"
- "SYSTEM"

<a id="headingCall_parameters_items_i0_query-filters"></a>
<a id="Call_parameters_items_i0_query-filters"></a>
##### query-filters

- Schema name: `Query-Filters`
- Type: array
- Default: []

Array of filters to apply to the audit query results.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_query-filters_items"></a>
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

<a id="headingCall_parameters_items_i0_query-options"></a>
<a id="Call_parameters_items_i0_query-options"></a>
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
<a id="headingCall_parameters_items_i0_query-options_order_by"></a>
<a id="Call_parameters_items_i0_query-options_order_by"></a>
###### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_query-options_order_by_items"></a>
- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

<a id="headingCall_parameters_items_i0_query-options_select"></a>
<a id="Call_parameters_items_i0_query-options_select"></a>
###### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_query-options_select_items"></a>
<a id="Call_parameters_items_i0_query-options_select_items_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_query-options_select_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_query-options_select_items_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_query-options_select_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_query-options_select_items_anyOf_i1)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_query-options_select_items_anyOf_i1_items"></a>
- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

<a id="headingCall_parameters_items_i0_query-options_offset"></a>
<a id="Call_parameters_items_i0_query-options_offset"></a>
###### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0`

<a id="headingCall_parameters_items_i0_query-options_limit"></a>
<a id="Call_parameters_items_i0_query-options_limit"></a>
###### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0` and lesser or equal to `10000`

<a id="headingCall_parameters_items_i0_query-options_force_sql_filters"></a>
<a id="Call_parameters_items_i0_query-options_force_sql_filters"></a>
###### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

<a id="headingCall_parameters_items_i0_remote_controller"></a>
<a id="Call_parameters_items_i0_remote_controller"></a>
##### remote_controller

- Schema name: `Remote Controller`
- Type: boolean
- Default: false

HA systems may direct the query to the 'remote' controller by including 'remote_controller=True'. The default is the 'current' controller.

<a id="headingCall_parameters_items_i0_export_format"></a>
<a id="Call_parameters_items_i0_export_format"></a>
##### export_format

- Schema name: `Export Format`
- Type: enum (of string)
- Default: "JSON"

Format for exporting audit data.
###### Must be one of:

- "CSV"
- "JSON"
- "YAML"

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: string

Path to the exported audit data file.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
