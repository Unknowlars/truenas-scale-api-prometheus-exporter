---
title: iscsi.portal.query
kind: method
source_rst: _sources/api_methods_iscsi.portal.query.rst.txt
source_html: api_methods_iscsi.portal.query.html
required_roles:
  - SHARING_ISCSI_PORTAL_READ
---

# iscsi.portal.query

## Required Roles

- `SHARING_ISCSI_PORTAL_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filters

<a id="Call_parameters_items_i0"></a>
#### filters

- Schema name: `filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i0_items"></a>
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

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object
- Default:
```json
{
  "extra": {},
  "order_by": [],
  "select": [],
  "count": false,
  "get": false,
  "offset": 0,
  "limit": 0,
  "force_sql_filters": false
}
```

Query options including pagination, ordering, and additional parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i1_extra"></a>
<a id="Call_parameters_items_i1_extra"></a>
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

<a id="headingCall_parameters_items_i1_order_by"></a>
<a id="Call_parameters_items_i1_order_by"></a>
##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_order_by_items"></a>
- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

<a id="headingCall_parameters_items_i1_select"></a>
<a id="Call_parameters_items_i1_select"></a>
##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items"></a>
<a id="Call_parameters_items_i1_select_items_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i1)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items_anyOf_i1_items"></a>
- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

<a id="headingCall_parameters_items_i1_count"></a>
<a id="Call_parameters_items_i1_count"></a>
##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

<a id="headingCall_parameters_items_i1_get"></a>
<a id="Call_parameters_items_i1_get"></a>
##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

<a id="headingCall_parameters_items_i1_offset"></a>
<a id="Call_parameters_items_i1_offset"></a>
##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0`

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0` and lesser or equal to `10000`

<a id="headingCall_parameters_items_i1_force_sql_filters"></a>
<a id="Call_parameters_items_i1_force_sql_filters"></a>
##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items"></a>
###### ISCSIPortalEntry

- Schema name: `ISCSIPortalEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_id"></a>
<a id="Return_value_anyOf_i0_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI portal.

<a id="headingReturn_value_anyOf_i0_items_listen"></a>
<a id="Return_value_anyOf_i0_items_listen"></a>
###### listen (required)

- Schema name: `Listen`
- Type: array of object

Array of IP address and port combinations for the portal to listen on.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_listen_items"></a>
###### IscsiPortalIPInfo

- Schema name: `IscsiPortalIPInfo`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_listen_items_ip"></a>
<a id="Return_value_anyOf_i0_items_listen_items_ip"></a>
###### ip (required)

- Schema name: `Ip`
- Type: string

IP address for the iSCSI portal to listen on.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_listen_items_port"></a>
<a id="Return_value_anyOf_i0_items_listen_items_port"></a>
###### port (required)

- Schema name: `Port`
- Type: integer

TCP port number for the iSCSI portal.

<a id="headingReturn_value_anyOf_i0_items_tag"></a>
<a id="Return_value_anyOf_i0_items_tag"></a>
###### tag (required)

- Schema name: `Tag`
- Type: integer

Numeric tag used to associate this portal with iSCSI targets.

<a id="headingReturn_value_anyOf_i0_items_comment"></a>
<a id="Return_value_anyOf_i0_items_comment"></a>
###### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the portal.

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [ISCSIPortalEntry](#tab-pane_Return_value_anyOf_i1)

- Schema name: `ISCSIPortalEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_id"></a>
<a id="Return_value_anyOf_i1_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI portal.

<a id="headingReturn_value_anyOf_i1_listen"></a>
<a id="Return_value_anyOf_i1_listen"></a>
###### listen (required)

- Schema name: `Listen`
- Type: array

Array of IP address and port combinations for the portal to listen on.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_listen_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i1_tag"></a>
<a id="Return_value_anyOf_i1_tag"></a>
###### tag (required)

- Schema name: `Tag`
- Type: integer

Numeric tag used to associate this portal with iSCSI targets.

<a id="headingReturn_value_anyOf_i1_comment"></a>
<a id="Return_value_anyOf_i1_comment"></a>
###### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the portal.

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items"></a>
###### ISCSIPortalQueryResultItem

- Schema name: `ISCSIPortalQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_id"></a>
<a id="Return_value_anyOf_i2_items_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI portal.

<a id="headingReturn_value_anyOf_i2_items_listen"></a>
<a id="Return_value_anyOf_i2_items_listen"></a>
###### listen

- Schema name: `Listen`
- Type: array of object

Array of IP address and port combinations for the portal to listen on.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_listen_items"></a>
###### IscsiPortalIPInfo

- Schema name: `IscsiPortalIPInfo`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_listen_items_ip"></a>
<a id="Return_value_anyOf_i2_items_listen_items_ip"></a>
###### ip (required)

- Schema name: `Ip`
- Type: string

IP address for the iSCSI portal to listen on.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_listen_items_port"></a>
<a id="Return_value_anyOf_i2_items_listen_items_port"></a>
###### port (required)

- Schema name: `Port`
- Type: integer

TCP port number for the iSCSI portal.

<a id="headingReturn_value_anyOf_i2_items_tag"></a>
<a id="Return_value_anyOf_i2_items_tag"></a>
###### tag

- Schema name: `Tag`
- Type: integer

Numeric tag used to associate this portal with iSCSI targets.

<a id="headingReturn_value_anyOf_i2_items_comment"></a>
<a id="Return_value_anyOf_i2_items_comment"></a>
###### comment

- Schema name: `Comment`
- Type: string

Optional comment describing the portal.

<a id="tab-pane_Return_value_anyOf_i3"></a>
##### [ISCSIPortalQueryResultItem](#tab-pane_Return_value_anyOf_i3)

- Schema name: `ISCSIPortalQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i3_id"></a>
<a id="Return_value_anyOf_i3_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI portal.

<a id="headingReturn_value_anyOf_i3_listen"></a>
<a id="Return_value_anyOf_i3_listen"></a>
###### listen

- Schema name: `Listen`
- Type: array

Array of IP address and port combinations for the portal to listen on.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i3_listen_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i3_tag"></a>
<a id="Return_value_anyOf_i3_tag"></a>
###### tag

- Schema name: `Tag`
- Type: integer

Numeric tag used to associate this portal with iSCSI targets.

<a id="headingReturn_value_anyOf_i3_comment"></a>
<a id="Return_value_anyOf_i3_comment"></a>
###### comment

- Schema name: `Comment`
- Type: string

Optional comment describing the portal.

<a id="tab-pane_Return_value_anyOf_i4"></a>
##### [Option 5](#tab-pane_Return_value_anyOf_i4)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
