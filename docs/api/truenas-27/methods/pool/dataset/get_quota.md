---
title: pool.dataset.get_quota
kind: method
source_rst: _sources/api_methods_pool.dataset.get_quota.rst.txt
source_html: api_methods_pool.dataset.get_quota.html
required_roles:
  - DATASET_READ
---

# pool.dataset.get_quota

## Summary

Return a list of the specified `quota_type` of quotas on the ZFS dataset `ds`. Support `query-filters` and `query-options`.

Note: SMB client requests to set a quota granting no space will result in an on-disk quota of 1 KiB.

## Required Roles

- `DATASET_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: dataset

<a id="Call_parameters_items_i0"></a>
#### dataset

- Schema name: `dataset`
- Type: string

The dataset path to retrieve quotas for.

#### Parameter 2: quota_type

<a id="Call_parameters_items_i1"></a>
#### quota_type

- Schema name: `quota_type`
- Type: enum (of string)

The type of quotas to retrieve.
##### Must be one of:

- "USER"
- "GROUP"
- "DATASET"
- "PROJECT"

#### Parameter 3: filters

<a id="Call_parameters_items_i2"></a>
#### filters

- Schema name: `filters`
- Type: array
- Default: []

Query filters to limit the results returned.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i2_items"></a>
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

#### Parameter 4: options

<a id="Call_parameters_items_i3"></a>
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

Query options such as sorting and pagination.
- No Additional Properties
<a id="headingCall_parameters_items_i3_extra"></a>
<a id="Call_parameters_items_i3_extra"></a>
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

<a id="headingCall_parameters_items_i3_order_by"></a>
<a id="Call_parameters_items_i3_order_by"></a>
##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i3_order_by_items"></a>
- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

<a id="headingCall_parameters_items_i3_select"></a>
<a id="Call_parameters_items_i3_select"></a>
##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i3_select_items"></a>
<a id="Call_parameters_items_i3_select_items_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i3_select_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i3_select_items_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i3_select_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i3_select_items_anyOf_i1)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i3_select_items_anyOf_i1_items"></a>
- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

<a id="headingCall_parameters_items_i3_count"></a>
<a id="Call_parameters_items_i3_count"></a>
##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

<a id="headingCall_parameters_items_i3_get"></a>
<a id="Call_parameters_items_i3_get"></a>
##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

<a id="headingCall_parameters_items_i3_offset"></a>
<a id="Call_parameters_items_i3_offset"></a>
##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

<a id="headingCall_parameters_items_i3_limit"></a>
<a id="Call_parameters_items_i3_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

<a id="headingCall_parameters_items_i3_force_sql_filters"></a>
<a id="Call_parameters_items_i3_force_sql_filters"></a>
##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`

Array of quota information for the specified quota type.
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items"></a>
<a id="Return_value_anyOf_i0_items_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_anyOf_i0_items_oneOf_i0"></a>
###### [PoolDatasetUserGroupQuota](#tab-pane_Return_value_anyOf_i0_items_oneOf_i0)

- Schema name: `PoolDatasetUserGroupQuota`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_oneOf_i0_used_bytes"></a>
<a id="Return_value_anyOf_i0_items_oneOf_i0_used_bytes"></a>
###### used_bytes

- Schema name: `Used Bytes`
- Type: integer

The number of bytes the user has written to the dataset. A value of zero means unlimited. May not instantly update as space is used.

<a id="headingReturn_value_anyOf_i0_items_oneOf_i0_quota"></a>
<a id="Return_value_anyOf_i0_items_oneOf_i0_quota"></a>
###### quota

- Schema name: `Quota`
- Type: integer

The quota size in bytes. Absent if no quota is set.

<a id="headingReturn_value_anyOf_i0_items_oneOf_i0_quota_type"></a>
<a id="Return_value_anyOf_i0_items_oneOf_i0_quota_type"></a>
###### quota_type

- Schema name: `Quota Type`
- Type: enum (of string)

Type identifier for user or group quotas.
###### Must be one of:

- "USER"
- "GROUP"

<a id="headingReturn_value_anyOf_i0_items_oneOf_i0_id"></a>
<a id="Return_value_anyOf_i0_items_oneOf_i0_id"></a>
###### id

- Schema name: `Id`
- Type: integer

The UID or GID to which the quota applies.

<a id="headingReturn_value_anyOf_i0_items_oneOf_i0_name"></a>
<a id="Return_value_anyOf_i0_items_oneOf_i0_name"></a>
###### name

- Schema name: `Name`

The user or group name to which the quota applies. Value is null if the id in the quota cannot be resolved to a user or group. This indicates that the user or group does not exist on the server.
<a id="Return_value_anyOf_i0_items_oneOf_i0_name_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_oneOf_i0_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_oneOf_i0_name_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_oneOf_i0_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_oneOf_i0_name_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_oneOf_i0_obj_used"></a>
<a id="Return_value_anyOf_i0_items_oneOf_i0_obj_used"></a>
###### obj_used

- Schema name: `Obj Used`
- Type: integer

The number of objects currently owned by `id`.

<a id="headingReturn_value_anyOf_i0_items_oneOf_i0_obj_quota"></a>
<a id="Return_value_anyOf_i0_items_oneOf_i0_obj_quota"></a>
###### obj_quota

- Schema name: `Obj Quota`
- Type: integer

The number of objects that may be owned by `id`. A value of zero means unlimited. Absent if no objquota is set.

<a id="tab-pane_Return_value_anyOf_i0_items_oneOf_i1"></a>
###### [PoolDatasetDatasetQuota](#tab-pane_Return_value_anyOf_i0_items_oneOf_i1)

- Schema name: `PoolDatasetDatasetQuota`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_oneOf_i1_used_bytes"></a>
<a id="Return_value_anyOf_i0_items_oneOf_i1_used_bytes"></a>
###### used_bytes

- Schema name: `Used Bytes`
- Type: integer

The number of bytes the user has written to the dataset. A value of zero means unlimited. May not instantly update as space is used.

<a id="headingReturn_value_anyOf_i0_items_oneOf_i1_quota"></a>
<a id="Return_value_anyOf_i0_items_oneOf_i1_quota"></a>
###### quota

- Schema name: `Quota`
- Type: integer

The quota size in bytes. Absent if no quota is set.

<a id="headingReturn_value_anyOf_i0_items_oneOf_i1_quota_type"></a>
<a id="Return_value_anyOf_i0_items_oneOf_i1_quota_type"></a>
###### quota_type

- Schema name: `Quota Type`
- Type: const

Type identifier for dataset quotas.
- Specific value: `"DATASET"`

<a id="headingReturn_value_anyOf_i0_items_oneOf_i1_id"></a>
<a id="Return_value_anyOf_i0_items_oneOf_i1_id"></a>
###### id

- Schema name: `Id`
- Type: string

Name of the dataset.

<a id="headingReturn_value_anyOf_i0_items_oneOf_i1_name"></a>
<a id="Return_value_anyOf_i0_items_oneOf_i1_name"></a>
###### name

- Schema name: `Name`
- Type: string

Name of the dataset.

<a id="headingReturn_value_anyOf_i0_items_oneOf_i1_refquota"></a>
<a id="Return_value_anyOf_i0_items_oneOf_i1_refquota"></a>
###### refquota

- Schema name: `Refquota`
- Type: integer

The dataset's reference quota in bytes.

<a id="tab-pane_Return_value_anyOf_i0_items_oneOf_i2"></a>
###### [PoolDatasetProjectQuota](#tab-pane_Return_value_anyOf_i0_items_oneOf_i2)

- Schema name: `PoolDatasetProjectQuota`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_oneOf_i2_used_bytes"></a>
<a id="Return_value_anyOf_i0_items_oneOf_i2_used_bytes"></a>
###### used_bytes

- Schema name: `Used Bytes`
- Type: integer

The number of bytes the user has written to the dataset. A value of zero means unlimited. May not instantly update as space is used.

<a id="headingReturn_value_anyOf_i0_items_oneOf_i2_quota"></a>
<a id="Return_value_anyOf_i0_items_oneOf_i2_quota"></a>
###### quota

- Schema name: `Quota`
- Type: integer

The quota size in bytes. Absent if no quota is set.

<a id="headingReturn_value_anyOf_i0_items_oneOf_i2_quota_type"></a>
<a id="Return_value_anyOf_i0_items_oneOf_i2_quota_type"></a>
###### quota_type

- Schema name: `Quota Type`
- Type: const

Type identifier for project quotas.
- Specific value: `"PROJECT"`

<a id="headingReturn_value_anyOf_i0_items_oneOf_i2_id"></a>
<a id="Return_value_anyOf_i0_items_oneOf_i2_id"></a>
###### id

- Schema name: `Id`
- Type: integer

The project ID.

<a id="headingReturn_value_anyOf_i0_items_oneOf_i2_obj_used"></a>
<a id="Return_value_anyOf_i0_items_oneOf_i2_obj_used"></a>
###### obj_used

- Schema name: `Obj Used`
- Type: integer

The number of objects currently owned by `id`.

<a id="headingReturn_value_anyOf_i0_items_oneOf_i2_obj_quota"></a>
<a id="Return_value_anyOf_i0_items_oneOf_i2_obj_quota"></a>
###### obj_quota

- Schema name: `Obj Quota`
- Type: integer

The number of objects that may be owned by `id`. A value of zero means unlimited. Absent if no objquota is set.

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [Option 2](#tab-pane_Return_value_anyOf_i1)

<a id="Return_value_anyOf_i1_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_anyOf_i1_oneOf_i0"></a>
###### [PoolDatasetUserGroupQuota](#tab-pane_Return_value_anyOf_i1_oneOf_i0)

- Schema name: `PoolDatasetUserGroupQuota`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_oneOf_i0_used_bytes"></a>
<a id="Return_value_anyOf_i1_oneOf_i0_used_bytes"></a>
###### used_bytes

- Schema name: `Used Bytes`
- Type: integer

The number of bytes the user has written to the dataset. A value of zero means unlimited. May not instantly update as space is used.

<a id="headingReturn_value_anyOf_i1_oneOf_i0_quota"></a>
<a id="Return_value_anyOf_i1_oneOf_i0_quota"></a>
###### quota

- Schema name: `Quota`
- Type: integer

The quota size in bytes. Absent if no quota is set.

<a id="headingReturn_value_anyOf_i1_oneOf_i0_quota_type"></a>
<a id="Return_value_anyOf_i1_oneOf_i0_quota_type"></a>
###### quota_type

- Schema name: `Quota Type`
- Type: enum (of string)

Type identifier for user or group quotas.
###### Must be one of:

- "USER"
- "GROUP"

<a id="headingReturn_value_anyOf_i1_oneOf_i0_id"></a>
<a id="Return_value_anyOf_i1_oneOf_i0_id"></a>
###### id

- Schema name: `Id`
- Type: integer

The UID or GID to which the quota applies.

<a id="headingReturn_value_anyOf_i1_oneOf_i0_name"></a>
<a id="Return_value_anyOf_i1_oneOf_i0_name"></a>
###### name

- Schema name: `Name`

The user or group name to which the quota applies. Value is null if the id in the quota cannot be resolved to a user or group. This indicates that the user or group does not exist on the server.
<a id="Return_value_anyOf_i1_oneOf_i0_name_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_oneOf_i0_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_oneOf_i0_name_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_oneOf_i0_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_oneOf_i0_name_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_oneOf_i0_obj_used"></a>
<a id="Return_value_anyOf_i1_oneOf_i0_obj_used"></a>
###### obj_used

- Schema name: `Obj Used`
- Type: integer

The number of objects currently owned by `id`.

<a id="headingReturn_value_anyOf_i1_oneOf_i0_obj_quota"></a>
<a id="Return_value_anyOf_i1_oneOf_i0_obj_quota"></a>
###### obj_quota

- Schema name: `Obj Quota`
- Type: integer

The number of objects that may be owned by `id`. A value of zero means unlimited. Absent if no objquota is set.

<a id="tab-pane_Return_value_anyOf_i1_oneOf_i1"></a>
###### [PoolDatasetDatasetQuota](#tab-pane_Return_value_anyOf_i1_oneOf_i1)

- Schema name: `PoolDatasetDatasetQuota`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_oneOf_i1_used_bytes"></a>
<a id="Return_value_anyOf_i1_oneOf_i1_used_bytes"></a>
###### used_bytes

- Schema name: `Used Bytes`
- Type: integer

The number of bytes the user has written to the dataset. A value of zero means unlimited. May not instantly update as space is used.

<a id="headingReturn_value_anyOf_i1_oneOf_i1_quota"></a>
<a id="Return_value_anyOf_i1_oneOf_i1_quota"></a>
###### quota

- Schema name: `Quota`
- Type: integer

The quota size in bytes. Absent if no quota is set.

<a id="headingReturn_value_anyOf_i1_oneOf_i1_quota_type"></a>
<a id="Return_value_anyOf_i1_oneOf_i1_quota_type"></a>
###### quota_type

- Schema name: `Quota Type`
- Type: const

Type identifier for dataset quotas.
- Specific value: `"DATASET"`

<a id="headingReturn_value_anyOf_i1_oneOf_i1_id"></a>
<a id="Return_value_anyOf_i1_oneOf_i1_id"></a>
###### id

- Schema name: `Id`
- Type: string

Name of the dataset.

<a id="headingReturn_value_anyOf_i1_oneOf_i1_name"></a>
<a id="Return_value_anyOf_i1_oneOf_i1_name"></a>
###### name

- Schema name: `Name`
- Type: string

Name of the dataset.

<a id="headingReturn_value_anyOf_i1_oneOf_i1_refquota"></a>
<a id="Return_value_anyOf_i1_oneOf_i1_refquota"></a>
###### refquota

- Schema name: `Refquota`
- Type: integer

The dataset's reference quota in bytes.

<a id="tab-pane_Return_value_anyOf_i1_oneOf_i2"></a>
###### [PoolDatasetProjectQuota](#tab-pane_Return_value_anyOf_i1_oneOf_i2)

- Schema name: `PoolDatasetProjectQuota`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_oneOf_i2_used_bytes"></a>
<a id="Return_value_anyOf_i1_oneOf_i2_used_bytes"></a>
###### used_bytes

- Schema name: `Used Bytes`
- Type: integer

The number of bytes the user has written to the dataset. A value of zero means unlimited. May not instantly update as space is used.

<a id="headingReturn_value_anyOf_i1_oneOf_i2_quota"></a>
<a id="Return_value_anyOf_i1_oneOf_i2_quota"></a>
###### quota

- Schema name: `Quota`
- Type: integer

The quota size in bytes. Absent if no quota is set.

<a id="headingReturn_value_anyOf_i1_oneOf_i2_quota_type"></a>
<a id="Return_value_anyOf_i1_oneOf_i2_quota_type"></a>
###### quota_type

- Schema name: `Quota Type`
- Type: const

Type identifier for project quotas.
- Specific value: `"PROJECT"`

<a id="headingReturn_value_anyOf_i1_oneOf_i2_id"></a>
<a id="Return_value_anyOf_i1_oneOf_i2_id"></a>
###### id

- Schema name: `Id`
- Type: integer

The project ID.

<a id="headingReturn_value_anyOf_i1_oneOf_i2_obj_used"></a>
<a id="Return_value_anyOf_i1_oneOf_i2_obj_used"></a>
###### obj_used

- Schema name: `Obj Used`
- Type: integer

The number of objects currently owned by `id`.

<a id="headingReturn_value_anyOf_i1_oneOf_i2_obj_quota"></a>
<a id="Return_value_anyOf_i1_oneOf_i2_obj_quota"></a>
###### obj_quota

- Schema name: `Obj Quota`
- Type: integer

The number of objects that may be owned by `id`. A value of zero means unlimited. Absent if no objquota is set.

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
