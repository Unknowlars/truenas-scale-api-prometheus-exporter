---
title: s3.accesskey.get_instance
kind: method
source_rst: _sources/api_methods_s3.accesskey.get_instance.rst.txt
source_html: api_methods_s3.accesskey.get_instance.html
required_roles:
  - SHARING_S3_READ
---

# s3.accesskey.get_instance

## Summary

Returns instance matching `id`. If `id` is not found, Validation error is raised.

Please see `query` method documentation for `options`.

## Required Roles

- `SHARING_S3_READ`

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

- Schema name: `S3AccesskeyEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the access key.

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the access key.
- Must be at least `1` characters long
- Must be at most `200` characters long

<a id="headingReturn_value_username"></a>
<a id="Return_value_username"></a>
#### username (required)

- Schema name: `Username`

Account the access key belongs to, or `null` if that account no longer exists.
<a id="Return_value_username_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_username_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_username_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_username_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_username_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_username_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_username_anyOf_i2)

- Type: null

<a id="headingReturn_value_user_identifier"></a>
<a id="Return_value_user_identifier"></a>
#### user_identifier (required)

- Schema name: `User Identifier`

Stored account linkage. A numeric user ID for local accounts or a SID for directory services accounts.
<a id="Return_value_user_identifier_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_user_identifier_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_user_identifier_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_user_identifier_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_user_identifier_anyOf_i1)

- Type: string

<a id="headingReturn_value_local"></a>
<a id="Return_value_local"></a>
#### local (required)

- Schema name: `Local`
- Type: boolean

Whether the access key belongs to a local user account rather than a directory services one.

<a id="headingReturn_value_access_key"></a>
<a id="Return_value_access_key"></a>
#### access_key (required)

- Schema name: `Access Key`
- Type: string

The S3 access key id clients sign requests with.
- Must match regular expression: `^[A-Z0-9]{16,128}$`

<a id="headingReturn_value_secret"></a>
<a id="Return_value_secret"></a>
#### secret (required)

- Schema name: `Secret`

The S3 secret access key. Readable only by administrators holding `SHARING_S3_WRITE`; redacted for everyone else. `null` when the secret was lost to a configuration restore without the secret seed.
<a id="Return_value_secret_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_secret_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_secret_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_secret_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_secret_anyOf_i1)

- Type: null

<a id="headingReturn_value_enabled"></a>
<a id="Return_value_enabled"></a>
#### enabled (required)

- Schema name: `Enabled`
- Type: boolean

Whether the access key may be used. A disabled key is refused by the S3 service.

<a id="headingReturn_value_expires_at"></a>
<a id="Return_value_expires_at"></a>
#### expires_at

- Schema name: `Expires At`
- Default: null

Expiration timestamp for the access key or `null` for no expiration.
<a id="Return_value_expires_at_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_expires_at_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_expires_at_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_Return_value_expires_at_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_expires_at_anyOf_i1)

- Type: null

<a id="headingReturn_value_created_at"></a>
<a id="Return_value_created_at"></a>
#### created_at (required)

- Schema name: `Created At`
- Type: string
- Type: Format: date-time

Timestamp when the access key was created.

<a id="headingReturn_value_last_used_at"></a>
<a id="Return_value_last_used_at"></a>
#### last_used_at

- Schema name: `Last Used At`
- Default: null

Time the S3 service last accepted a request signed with this key, or `null` if the key has never been used. The S3 service reports this at intervals, so a recent request can be absent for a short time. This field is read-only.
<a id="Return_value_last_used_at_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_last_used_at_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_last_used_at_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_Return_value_last_used_at_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_last_used_at_anyOf_i1)

- Type: null

<a id="headingReturn_value_manage_buckets"></a>
<a id="Return_value_manage_buckets"></a>
#### manage_buckets

- Schema name: `Manage Buckets`
- Type: boolean
- Default: false

Whether this access key may create and delete buckets through the S3 protocol. Setting it requires the account that owns the key to hold the `SHARING_S3_WRITE` role, checked when a call turns it on. It scopes the key, not the account: an account may hold several access keys, and leaving this off on one of them affects neither its other keys nor its own access to `sharing.s3.create`.

<a id="headingReturn_value_status"></a>
<a id="Return_value_status"></a>
#### status (required)

- Schema name: `Status`
- Type: enum (of string)

Effective state of the access key. Only `ENABLED` keys are usable. `DISABLED` was set by an administrator, `EXPIRED` passed its expiration, `USER_MISSING` belongs to a directory account that no longer resolves (a deleted local account takes its keys with it), and `SECRET_LOST` lost its secret to a configuration restore without the secret seed and must be rotated.
##### Must be one of:

- "ENABLED"
- "DISABLED"
- "EXPIRED"
- "USER_MISSING"
- "SECRET_LOST"

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
