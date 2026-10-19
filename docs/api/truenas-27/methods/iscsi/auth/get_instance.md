---
title: iscsi.auth.get_instance
kind: method
source_rst: _sources/api_methods_iscsi.auth.get_instance.rst.txt
source_html: api_methods_iscsi.auth.get_instance.html
required_roles:
  - SHARING_ISCSI_AUTH_READ
---

# iscsi.auth.get_instance

## Summary

Returns instance matching `id`. If `id` is not found, Validation error is raised.

Please see `query` method documentation for `options`.

## Required Roles

- `SHARING_ISCSI_AUTH_READ`

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

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object
- Default: {}

Query options customize the results returned by a query method. More complete documentation with examples are covered in the "Query methods" section of the TrueNAS API documentation.
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

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

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

- Schema name: `iSCSITargetAuthCredentialEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI authentication credential.

<a id="headingReturn_value_tag"></a>
<a id="Return_value_tag"></a>
#### tag (required)

- Schema name: `Tag`
- Type: integer

Numeric tag used to associate this credential with iSCSI targets.

<a id="headingReturn_value_user"></a>
<a id="Return_value_user"></a>
#### user (required)

- Schema name: `User`
- Type: string

Username for iSCSI CHAP authentication.

<a id="headingReturn_value_secret"></a>
<a id="Return_value_secret"></a>
#### secret (required)

- Schema name: `Secret`
- Type: string

Password/secret for iSCSI CHAP authentication.

<a id="headingReturn_value_peeruser"></a>
<a id="Return_value_peeruser"></a>
#### peeruser

- Schema name: `Peeruser`
- Type: string
- Default: ""

Username for mutual CHAP authentication or empty string if not configured.

<a id="headingReturn_value_peersecret"></a>
<a id="Return_value_peersecret"></a>
#### peersecret

- Schema name: `Peersecret`
- Type: string
- Default: ""

Password/secret for mutual CHAP authentication or empty string if not configured.

<a id="headingReturn_value_discovery_auth"></a>
<a id="Return_value_discovery_auth"></a>
#### discovery_auth

- Schema name: `Discovery Auth`
- Type: enum (of string)
- Default: "NONE"

Authentication method for target discovery. If "CHAP_MUTUAL" is selected for target discovery, it is only permitted for a single entry systemwide.
##### Must be one of:

- "NONE"
- "CHAP"
- "CHAP_MUTUAL"

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
