---
title: pool.dataset.get_instance
kind: method
source_rst: _sources/api_methods_pool.dataset.get_instance.rst.txt
source_html: api_methods_pool.dataset.get_instance.html
required_roles:
  - DATASET_READ
---

# pool.dataset.get_instance

## Summary

Returns instance matching `id`. If `id` is not found, Validation error is raised.

Please see `query` method documentation for `options`.

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

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: string

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

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

- Schema name: `PoolDatasetEntry`
- Type: object
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id

- Schema name: `Id`
- Type: string

The full dataset path including pool name.
Examples:

```json
"tank/dataset/child"
```

<a id="headingReturn_value_type"></a>
<a id="Return_value_type"></a>
#### type

- Schema name: `Type`
- Type: string

The dataset type.
Examples:

```json
"FILESYSTEM"
```
Examples:

```json
"VOLUME"
```

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name

- Schema name: `Name`
- Type: string

The dataset name without the pool prefix.

<a id="headingReturn_value_pool"></a>
<a id="Return_value_pool"></a>
#### pool

- Schema name: `Pool`
- Type: string

The name of the ZFS pool containing this dataset.

<a id="headingReturn_value_encrypted"></a>
<a id="Return_value_encrypted"></a>
#### encrypted

- Schema name: `Encrypted`
- Type: boolean

Whether the dataset is encrypted.

<a id="headingReturn_value_encryption_root"></a>
<a id="Return_value_encryption_root"></a>
#### encryption_root

- Schema name: `Encryption Root`

The root dataset where encryption is enabled. `null` if the dataset is not encrypted.
<a id="Return_value_encryption_root_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_encryption_root_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_encryption_root_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_encryption_root_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_encryption_root_anyOf_i1)

- Type: null

<a id="headingReturn_value_key_loaded"></a>
<a id="Return_value_key_loaded"></a>
#### key_loaded

- Schema name: `Key Loaded`

Whether the encryption key is currently loaded for encrypted datasets. `null` for unencrypted datasets.
<a id="Return_value_key_loaded_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_key_loaded_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_key_loaded_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_key_loaded_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_key_loaded_anyOf_i1)

- Type: null

<a id="headingReturn_value_children"></a>
<a id="Return_value_children"></a>
#### children

- Schema name: `Children`
- Type: array

Array of child dataset objects nested under this dataset.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_children_items"></a>
- Type: object

<a id="headingReturn_value_user_properties"></a>
<a id="Return_value_user_properties"></a>
#### user_properties

- Schema name: `PoolDatasetEntryUserProperties`
- Type: object

Custom user-defined ZFS properties set on this dataset as key-value pairs.
<a id="headingReturn_value_user_properties_comments"></a>
<a id="Return_value_user_properties_comments"></a>
##### comments

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS comments property for storing descriptive text about the dataset.
- No Additional Properties
<a id="headingReturn_value_user_properties_comments_parsed"></a>
<a id="Return_value_user_properties_comments_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_user_properties_comments_rawvalue"></a>
<a id="Return_value_user_properties_comments_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_user_properties_comments_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_user_properties_comments_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_user_properties_comments_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_user_properties_comments_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_user_properties_comments_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_user_properties_comments_value"></a>
<a id="Return_value_user_properties_comments_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_user_properties_comments_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_user_properties_comments_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_user_properties_comments_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_user_properties_comments_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_user_properties_comments_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_user_properties_comments_source"></a>
<a id="Return_value_user_properties_comments_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_user_properties_comments_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_user_properties_comments_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_user_properties_comments_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_user_properties_comments_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_user_properties_comments_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_user_properties_comments_source_info"></a>
<a id="Return_value_user_properties_comments_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_user_properties_quota_warning"></a>
<a id="Return_value_user_properties_quota_warning"></a>
##### quota_warning

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS quota warning threshold property as a percentage.
- No Additional Properties
<a id="headingReturn_value_user_properties_quota_warning_parsed"></a>
<a id="Return_value_user_properties_quota_warning_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_user_properties_quota_warning_rawvalue"></a>
<a id="Return_value_user_properties_quota_warning_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_user_properties_quota_warning_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_user_properties_quota_warning_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_user_properties_quota_warning_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_user_properties_quota_warning_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_user_properties_quota_warning_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_user_properties_quota_warning_value"></a>
<a id="Return_value_user_properties_quota_warning_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_user_properties_quota_warning_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_user_properties_quota_warning_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_user_properties_quota_warning_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_user_properties_quota_warning_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_user_properties_quota_warning_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_user_properties_quota_warning_source"></a>
<a id="Return_value_user_properties_quota_warning_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_user_properties_quota_warning_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_user_properties_quota_warning_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_user_properties_quota_warning_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_user_properties_quota_warning_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_user_properties_quota_warning_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_user_properties_quota_warning_source_info"></a>
<a id="Return_value_user_properties_quota_warning_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_user_properties_quota_critical"></a>
<a id="Return_value_user_properties_quota_critical"></a>
##### quota_critical

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS quota critical threshold property as a percentage.
- No Additional Properties
<a id="headingReturn_value_user_properties_quota_critical_parsed"></a>
<a id="Return_value_user_properties_quota_critical_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_user_properties_quota_critical_rawvalue"></a>
<a id="Return_value_user_properties_quota_critical_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_user_properties_quota_critical_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_user_properties_quota_critical_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_user_properties_quota_critical_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_user_properties_quota_critical_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_user_properties_quota_critical_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_user_properties_quota_critical_value"></a>
<a id="Return_value_user_properties_quota_critical_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_user_properties_quota_critical_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_user_properties_quota_critical_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_user_properties_quota_critical_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_user_properties_quota_critical_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_user_properties_quota_critical_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_user_properties_quota_critical_source"></a>
<a id="Return_value_user_properties_quota_critical_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_user_properties_quota_critical_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_user_properties_quota_critical_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_user_properties_quota_critical_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_user_properties_quota_critical_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_user_properties_quota_critical_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_user_properties_quota_critical_source_info"></a>
<a id="Return_value_user_properties_quota_critical_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_user_properties_refquota_warning"></a>
<a id="Return_value_user_properties_refquota_warning"></a>
##### refquota_warning

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS reference quota warning threshold property as a percentage.
- No Additional Properties
<a id="headingReturn_value_user_properties_refquota_warning_parsed"></a>
<a id="Return_value_user_properties_refquota_warning_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_user_properties_refquota_warning_rawvalue"></a>
<a id="Return_value_user_properties_refquota_warning_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_user_properties_refquota_warning_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_user_properties_refquota_warning_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_user_properties_refquota_warning_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_user_properties_refquota_warning_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_user_properties_refquota_warning_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_user_properties_refquota_warning_value"></a>
<a id="Return_value_user_properties_refquota_warning_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_user_properties_refquota_warning_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_user_properties_refquota_warning_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_user_properties_refquota_warning_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_user_properties_refquota_warning_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_user_properties_refquota_warning_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_user_properties_refquota_warning_source"></a>
<a id="Return_value_user_properties_refquota_warning_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_user_properties_refquota_warning_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_user_properties_refquota_warning_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_user_properties_refquota_warning_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_user_properties_refquota_warning_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_user_properties_refquota_warning_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_user_properties_refquota_warning_source_info"></a>
<a id="Return_value_user_properties_refquota_warning_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_user_properties_refquota_critical"></a>
<a id="Return_value_user_properties_refquota_critical"></a>
##### refquota_critical

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS reference quota critical threshold property as a percentage.
- No Additional Properties
<a id="headingReturn_value_user_properties_refquota_critical_parsed"></a>
<a id="Return_value_user_properties_refquota_critical_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_user_properties_refquota_critical_rawvalue"></a>
<a id="Return_value_user_properties_refquota_critical_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_user_properties_refquota_critical_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_user_properties_refquota_critical_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_user_properties_refquota_critical_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_user_properties_refquota_critical_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_user_properties_refquota_critical_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_user_properties_refquota_critical_value"></a>
<a id="Return_value_user_properties_refquota_critical_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_user_properties_refquota_critical_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_user_properties_refquota_critical_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_user_properties_refquota_critical_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_user_properties_refquota_critical_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_user_properties_refquota_critical_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_user_properties_refquota_critical_source"></a>
<a id="Return_value_user_properties_refquota_critical_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_user_properties_refquota_critical_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_user_properties_refquota_critical_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_user_properties_refquota_critical_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_user_properties_refquota_critical_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_user_properties_refquota_critical_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_user_properties_refquota_critical_source_info"></a>
<a id="Return_value_user_properties_refquota_critical_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_user_properties_managedby"></a>
<a id="Return_value_user_properties_managedby"></a>
##### managedby

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Identifies which service or system manages this dataset.
- No Additional Properties
<a id="headingReturn_value_user_properties_managedby_parsed"></a>
<a id="Return_value_user_properties_managedby_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_user_properties_managedby_rawvalue"></a>
<a id="Return_value_user_properties_managedby_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_user_properties_managedby_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_user_properties_managedby_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_user_properties_managedby_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_user_properties_managedby_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_user_properties_managedby_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_user_properties_managedby_value"></a>
<a id="Return_value_user_properties_managedby_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_user_properties_managedby_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_user_properties_managedby_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_user_properties_managedby_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_user_properties_managedby_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_user_properties_managedby_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_user_properties_managedby_source"></a>
<a id="Return_value_user_properties_managedby_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_user_properties_managedby_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_user_properties_managedby_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_user_properties_managedby_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_user_properties_managedby_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_user_properties_managedby_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_user_properties_managedby_source_info"></a>
<a id="Return_value_user_properties_managedby_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_user_properties_additionalProperties"></a>
<a id="Return_value_user_properties_additionalProperties"></a>
##### Additional Properties

Additional Properties of any type are allowed.
- Type: object

<a id="headingReturn_value_locked"></a>
<a id="Return_value_locked"></a>
#### locked

- Schema name: `Locked`
- Type: boolean

Whether an encrypted dataset is currently locked (key not loaded).

<a id="headingReturn_value_tier"></a>
<a id="Return_value_tier"></a>
#### tier

Performance tier. `null` if tiering disabled, if underlying pool does not support tiering, or if deduplication is enabled on the dataset.
<a id="Return_value_tier_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_tier_anyOf_i0"></a>
###### [TierInfo](#tab-pane_Return_value_tier_anyOf_i0)

- Schema name: `TierInfo`
- Type: object
- No Additional Properties
<a id="headingReturn_value_tier_anyOf_i0_tier_type"></a>
<a id="Return_value_tier_anyOf_i0_tier_type"></a>
###### tier_type (required)

- Schema name: `Tier Type`
- Type: enum (of string)

Storage performance tier for this share.
###### Must be one of:

- "REGULAR"
- "PERFORMANCE"

<a id="headingReturn_value_tier_anyOf_i0_tier_job"></a>
<a id="Return_value_tier_anyOf_i0_tier_job"></a>
###### tier_job

- Default: null

Most recent rewrite job for this share's dataset, or `null` if no job history exists.
<a id="Return_value_tier_anyOf_i0_tier_job_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_tier_anyOf_i0_tier_job_anyOf_i0"></a>
###### [ZfsTierRewriteJobEntry](#tab-pane_Return_value_tier_anyOf_i0_tier_job_anyOf_i0)

- Schema name: `ZfsTierRewriteJobEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
<a id="Return_value_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
###### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

<a id="headingReturn_value_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
<a id="Return_value_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
###### dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

<a id="headingReturn_value_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
<a id="Return_value_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
###### job_uuid (required)

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

<a id="headingReturn_value_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
<a id="Return_value_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
###### status (required)

- Schema name: `Status`
- Type: enum (of string)

Current lifecycle state of the job. `COMPLETE` - All files in the dataset have been processed. `RUNNING` - Job is actively processing files. `QUEUED` - Job is waiting for a free execution slot (see `max_concurrent_jobs`). `CANCELLED` - Job was stopped via `zfs_tier_job.cancel`. Not resumable. `STOPPED` - Job was RUNNING but its process is no longer active (e.g. daemon restart). This state is computed on read and is never written to persistent storage. `ERROR` - Job halted due to an unrecoverable error. Use `zfs_tier_job.recover` to retry failed files.
###### Must be one of:

- "COMPLETE"
- "RUNNING"
- "QUEUED"
- "CANCELLED"
- "STOPPED"
- "ERROR"

<a id="tab-pane_Return_value_tier_anyOf_i0_tier_job_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_tier_anyOf_i0_tier_job_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_tier_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_tier_anyOf_i1)

- Type: null

<a id="headingReturn_value_deduplication"></a>
<a id="Return_value_deduplication"></a>
#### deduplication

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS deduplication setting - whether identical data blocks are stored only once.
- No Additional Properties
<a id="headingReturn_value_deduplication_parsed"></a>
<a id="Return_value_deduplication_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_deduplication_rawvalue"></a>
<a id="Return_value_deduplication_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_deduplication_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_deduplication_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_deduplication_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_deduplication_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_deduplication_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_deduplication_value"></a>
<a id="Return_value_deduplication_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_deduplication_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_deduplication_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_deduplication_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_deduplication_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_deduplication_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_deduplication_source"></a>
<a id="Return_value_deduplication_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_deduplication_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_deduplication_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_deduplication_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_deduplication_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_deduplication_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_deduplication_source_info"></a>
<a id="Return_value_deduplication_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_aclmode"></a>
<a id="Return_value_aclmode"></a>
#### aclmode

- Schema name: `PoolDatasetEntryProperty`
- Type: object

How Access Control Lists (ACLs) are handled when chmod is used.
- No Additional Properties
<a id="headingReturn_value_aclmode_parsed"></a>
<a id="Return_value_aclmode_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_aclmode_rawvalue"></a>
<a id="Return_value_aclmode_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_aclmode_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_aclmode_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_aclmode_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_aclmode_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_aclmode_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_aclmode_value"></a>
<a id="Return_value_aclmode_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_aclmode_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_aclmode_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_aclmode_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_aclmode_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_aclmode_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_aclmode_source"></a>
<a id="Return_value_aclmode_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_aclmode_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_aclmode_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_aclmode_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_aclmode_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_aclmode_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_aclmode_source_info"></a>
<a id="Return_value_aclmode_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_acltype"></a>
<a id="Return_value_acltype"></a>
#### acltype

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The type of Access Control List system used (NFSV4, POSIX, or OFF).
- No Additional Properties
<a id="headingReturn_value_acltype_parsed"></a>
<a id="Return_value_acltype_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_acltype_rawvalue"></a>
<a id="Return_value_acltype_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_acltype_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_acltype_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_acltype_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_acltype_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_acltype_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_acltype_value"></a>
<a id="Return_value_acltype_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_acltype_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_acltype_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_acltype_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_acltype_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_acltype_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_acltype_source"></a>
<a id="Return_value_acltype_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_acltype_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_acltype_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_acltype_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_acltype_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_acltype_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_acltype_source_info"></a>
<a id="Return_value_acltype_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_xattr"></a>
<a id="Return_value_xattr"></a>
#### xattr

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Extended attributes storage method (on/off).
- No Additional Properties
<a id="headingReturn_value_xattr_parsed"></a>
<a id="Return_value_xattr_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_xattr_rawvalue"></a>
<a id="Return_value_xattr_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_xattr_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_xattr_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_xattr_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_xattr_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_xattr_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_xattr_value"></a>
<a id="Return_value_xattr_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_xattr_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_xattr_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_xattr_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_xattr_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_xattr_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_xattr_source"></a>
<a id="Return_value_xattr_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_xattr_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_xattr_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_xattr_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_xattr_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_xattr_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_xattr_source_info"></a>
<a id="Return_value_xattr_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_atime"></a>
<a id="Return_value_atime"></a>
#### atime

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Whether file access times are updated when files are accessed.
- No Additional Properties
<a id="headingReturn_value_atime_parsed"></a>
<a id="Return_value_atime_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_atime_rawvalue"></a>
<a id="Return_value_atime_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_atime_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_atime_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_atime_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_atime_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_atime_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_atime_value"></a>
<a id="Return_value_atime_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_atime_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_atime_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_atime_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_atime_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_atime_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_atime_source"></a>
<a id="Return_value_atime_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_atime_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_atime_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_atime_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_atime_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_atime_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_atime_source_info"></a>
<a id="Return_value_atime_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_casesensitivity"></a>
<a id="Return_value_casesensitivity"></a>
#### casesensitivity

- Schema name: `PoolDatasetEntryProperty`
- Type: object

File name case sensitivity setting (sensitive/insensitive).
- No Additional Properties
<a id="headingReturn_value_casesensitivity_parsed"></a>
<a id="Return_value_casesensitivity_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_casesensitivity_rawvalue"></a>
<a id="Return_value_casesensitivity_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_casesensitivity_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_casesensitivity_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_casesensitivity_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_casesensitivity_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_casesensitivity_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_casesensitivity_value"></a>
<a id="Return_value_casesensitivity_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_casesensitivity_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_casesensitivity_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_casesensitivity_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_casesensitivity_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_casesensitivity_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_casesensitivity_source"></a>
<a id="Return_value_casesensitivity_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_casesensitivity_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_casesensitivity_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_casesensitivity_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_casesensitivity_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_casesensitivity_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_casesensitivity_source_info"></a>
<a id="Return_value_casesensitivity_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_checksum"></a>
<a id="Return_value_checksum"></a>
#### checksum

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Data integrity checksum algorithm used for this dataset.
- No Additional Properties
<a id="headingReturn_value_checksum_parsed"></a>
<a id="Return_value_checksum_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_checksum_rawvalue"></a>
<a id="Return_value_checksum_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_checksum_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_checksum_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_checksum_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_checksum_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_checksum_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_checksum_value"></a>
<a id="Return_value_checksum_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_checksum_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_checksum_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_checksum_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_checksum_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_checksum_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_checksum_source"></a>
<a id="Return_value_checksum_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_checksum_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_checksum_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_checksum_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_checksum_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_checksum_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_checksum_source_info"></a>
<a id="Return_value_checksum_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_exec"></a>
<a id="Return_value_exec"></a>
#### exec

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Whether files in this dataset can be executed.
- No Additional Properties
<a id="headingReturn_value_exec_parsed"></a>
<a id="Return_value_exec_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_exec_rawvalue"></a>
<a id="Return_value_exec_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_exec_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_exec_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_exec_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_exec_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_exec_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_exec_value"></a>
<a id="Return_value_exec_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_exec_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_exec_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_exec_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_exec_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_exec_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_exec_source"></a>
<a id="Return_value_exec_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_exec_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_exec_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_exec_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_exec_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_exec_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_exec_source_info"></a>
<a id="Return_value_exec_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_sync"></a>
<a id="Return_value_sync"></a>
#### sync

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Synchronous write behavior (standard/always/disabled).
- No Additional Properties
<a id="headingReturn_value_sync_parsed"></a>
<a id="Return_value_sync_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_sync_rawvalue"></a>
<a id="Return_value_sync_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_sync_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_sync_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_sync_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_sync_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_sync_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_sync_value"></a>
<a id="Return_value_sync_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_sync_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_sync_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_sync_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_sync_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_sync_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_sync_source"></a>
<a id="Return_value_sync_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_sync_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_sync_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_sync_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_sync_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_sync_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_sync_source_info"></a>
<a id="Return_value_sync_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_compression"></a>
<a id="Return_value_compression"></a>
#### compression

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Compression algorithm and level applied to data in this dataset.
- No Additional Properties
<a id="headingReturn_value_compression_parsed"></a>
<a id="Return_value_compression_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_compression_rawvalue"></a>
<a id="Return_value_compression_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_compression_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_compression_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_compression_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_compression_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_compression_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_compression_value"></a>
<a id="Return_value_compression_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_compression_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_compression_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_compression_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_compression_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_compression_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_compression_source"></a>
<a id="Return_value_compression_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_compression_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_compression_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_compression_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_compression_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_compression_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_compression_source_info"></a>
<a id="Return_value_compression_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_compressratio"></a>
<a id="Return_value_compressratio"></a>
#### compressratio

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The achieved compression ratio as a decimal (e.g., '2.50x').
- No Additional Properties
<a id="headingReturn_value_compressratio_parsed"></a>
<a id="Return_value_compressratio_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_compressratio_rawvalue"></a>
<a id="Return_value_compressratio_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_compressratio_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_compressratio_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_compressratio_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_compressratio_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_compressratio_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_compressratio_value"></a>
<a id="Return_value_compressratio_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_compressratio_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_compressratio_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_compressratio_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_compressratio_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_compressratio_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_compressratio_source"></a>
<a id="Return_value_compressratio_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_compressratio_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_compressratio_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_compressratio_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_compressratio_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_compressratio_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_compressratio_source_info"></a>
<a id="Return_value_compressratio_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_origin"></a>
<a id="Return_value_origin"></a>
#### origin

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The snapshot from which this clone was created. Empty for non-clone datasets.
- No Additional Properties
<a id="headingReturn_value_origin_parsed"></a>
<a id="Return_value_origin_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_origin_rawvalue"></a>
<a id="Return_value_origin_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_origin_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_origin_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_origin_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_origin_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_origin_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_origin_value"></a>
<a id="Return_value_origin_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_origin_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_origin_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_origin_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_origin_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_origin_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_origin_source"></a>
<a id="Return_value_origin_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_origin_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_origin_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_origin_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_origin_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_origin_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_origin_source_info"></a>
<a id="Return_value_origin_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_quota"></a>
<a id="Return_value_quota"></a>
#### quota

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Maximum amount of disk space this dataset and its children can consume.
- No Additional Properties
<a id="headingReturn_value_quota_parsed"></a>
<a id="Return_value_quota_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_quota_rawvalue"></a>
<a id="Return_value_quota_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_quota_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_quota_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_quota_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_quota_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_quota_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_quota_value"></a>
<a id="Return_value_quota_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_quota_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_quota_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_quota_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_quota_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_quota_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_quota_source"></a>
<a id="Return_value_quota_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_quota_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_quota_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_quota_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_quota_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_quota_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_quota_source_info"></a>
<a id="Return_value_quota_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_refquota"></a>
<a id="Return_value_refquota"></a>
#### refquota

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Maximum amount of disk space this dataset itself can consume (excluding children).
- No Additional Properties
<a id="headingReturn_value_refquota_parsed"></a>
<a id="Return_value_refquota_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_refquota_rawvalue"></a>
<a id="Return_value_refquota_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_refquota_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_refquota_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_refquota_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_refquota_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_refquota_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_refquota_value"></a>
<a id="Return_value_refquota_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_refquota_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_refquota_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_refquota_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_refquota_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_refquota_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_refquota_source"></a>
<a id="Return_value_refquota_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_refquota_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_refquota_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_refquota_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_refquota_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_refquota_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_refquota_source_info"></a>
<a id="Return_value_refquota_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_reservation"></a>
<a id="Return_value_reservation"></a>
#### reservation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Minimum amount of disk space guaranteed to be available to this dataset and its children.
- No Additional Properties
<a id="headingReturn_value_reservation_parsed"></a>
<a id="Return_value_reservation_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_reservation_rawvalue"></a>
<a id="Return_value_reservation_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_reservation_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_reservation_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_reservation_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_reservation_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_reservation_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_reservation_value"></a>
<a id="Return_value_reservation_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_reservation_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_reservation_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_reservation_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_reservation_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_reservation_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_reservation_source"></a>
<a id="Return_value_reservation_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_reservation_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_reservation_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_reservation_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_reservation_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_reservation_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_reservation_source_info"></a>
<a id="Return_value_reservation_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_refreservation"></a>
<a id="Return_value_refreservation"></a>
#### refreservation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Minimum amount of disk space guaranteed to be available to this dataset itself.
- No Additional Properties
<a id="headingReturn_value_refreservation_parsed"></a>
<a id="Return_value_refreservation_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_refreservation_rawvalue"></a>
<a id="Return_value_refreservation_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_refreservation_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_refreservation_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_refreservation_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_refreservation_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_refreservation_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_refreservation_value"></a>
<a id="Return_value_refreservation_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_refreservation_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_refreservation_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_refreservation_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_refreservation_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_refreservation_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_refreservation_source"></a>
<a id="Return_value_refreservation_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_refreservation_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_refreservation_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_refreservation_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_refreservation_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_refreservation_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_refreservation_source_info"></a>
<a id="Return_value_refreservation_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_copies"></a>
<a id="Return_value_copies"></a>
#### copies

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Number of copies of data blocks to maintain for redundancy (1-3).
- No Additional Properties
<a id="headingReturn_value_copies_parsed"></a>
<a id="Return_value_copies_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_copies_rawvalue"></a>
<a id="Return_value_copies_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_copies_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_copies_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_copies_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_copies_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_copies_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_copies_value"></a>
<a id="Return_value_copies_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_copies_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_copies_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_copies_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_copies_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_copies_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_copies_source"></a>
<a id="Return_value_copies_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_copies_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_copies_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_copies_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_copies_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_copies_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_copies_source_info"></a>
<a id="Return_value_copies_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_snapdir"></a>
<a id="Return_value_snapdir"></a>
#### snapdir

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Visibility of the .zfs/snapshot directory (visible/hidden).
- No Additional Properties
<a id="headingReturn_value_snapdir_parsed"></a>
<a id="Return_value_snapdir_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_snapdir_rawvalue"></a>
<a id="Return_value_snapdir_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_snapdir_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_snapdir_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_snapdir_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_snapdir_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_snapdir_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_snapdir_value"></a>
<a id="Return_value_snapdir_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_snapdir_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_snapdir_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_snapdir_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_snapdir_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_snapdir_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_snapdir_source"></a>
<a id="Return_value_snapdir_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_snapdir_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_snapdir_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_snapdir_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_snapdir_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_snapdir_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_snapdir_source_info"></a>
<a id="Return_value_snapdir_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_readonly"></a>
<a id="Return_value_readonly"></a>
#### readonly

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Whether the dataset is read-only.
- No Additional Properties
<a id="headingReturn_value_readonly_parsed"></a>
<a id="Return_value_readonly_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_readonly_rawvalue"></a>
<a id="Return_value_readonly_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_readonly_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_readonly_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_readonly_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_readonly_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_readonly_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_readonly_value"></a>
<a id="Return_value_readonly_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_readonly_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_readonly_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_readonly_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_readonly_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_readonly_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_readonly_source"></a>
<a id="Return_value_readonly_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_readonly_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_readonly_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_readonly_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_readonly_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_readonly_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_readonly_source_info"></a>
<a id="Return_value_readonly_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_recordsize"></a>
<a id="Return_value_recordsize"></a>
#### recordsize

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The suggested block size for files in this filesystem dataset.
- No Additional Properties
<a id="headingReturn_value_recordsize_parsed"></a>
<a id="Return_value_recordsize_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_recordsize_rawvalue"></a>
<a id="Return_value_recordsize_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_recordsize_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_recordsize_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_recordsize_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_recordsize_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_recordsize_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_recordsize_value"></a>
<a id="Return_value_recordsize_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_recordsize_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_recordsize_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_recordsize_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_recordsize_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_recordsize_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_recordsize_source"></a>
<a id="Return_value_recordsize_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_recordsize_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_recordsize_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_recordsize_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_recordsize_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_recordsize_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_recordsize_source_info"></a>
<a id="Return_value_recordsize_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_sparse"></a>
<a id="Return_value_sparse"></a>
#### sparse

- Schema name: `PoolDatasetEntryProperty`
- Type: object

For volumes, whether to use sparse (thin) provisioning.
- No Additional Properties
<a id="headingReturn_value_sparse_parsed"></a>
<a id="Return_value_sparse_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_sparse_rawvalue"></a>
<a id="Return_value_sparse_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_sparse_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_sparse_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_sparse_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_sparse_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_sparse_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_sparse_value"></a>
<a id="Return_value_sparse_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_sparse_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_sparse_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_sparse_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_sparse_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_sparse_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_sparse_source"></a>
<a id="Return_value_sparse_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_sparse_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_sparse_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_sparse_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_sparse_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_sparse_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_sparse_source_info"></a>
<a id="Return_value_sparse_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_volsize"></a>
<a id="Return_value_volsize"></a>
#### volsize

- Schema name: `PoolDatasetEntryProperty`
- Type: object

For volumes, the logical size of the volume.
- No Additional Properties
<a id="headingReturn_value_volsize_parsed"></a>
<a id="Return_value_volsize_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_volsize_rawvalue"></a>
<a id="Return_value_volsize_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_volsize_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_volsize_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_volsize_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_volsize_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_volsize_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_volsize_value"></a>
<a id="Return_value_volsize_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_volsize_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_volsize_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_volsize_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_volsize_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_volsize_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_volsize_source"></a>
<a id="Return_value_volsize_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_volsize_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_volsize_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_volsize_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_volsize_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_volsize_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_volsize_source_info"></a>
<a id="Return_value_volsize_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_volblocksize"></a>
<a id="Return_value_volblocksize"></a>
#### volblocksize

- Schema name: `PoolDatasetEntryProperty`
- Type: object

For volumes, the block size used by the volume.
- No Additional Properties
<a id="headingReturn_value_volblocksize_parsed"></a>
<a id="Return_value_volblocksize_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_volblocksize_rawvalue"></a>
<a id="Return_value_volblocksize_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_volblocksize_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_volblocksize_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_volblocksize_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_volblocksize_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_volblocksize_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_volblocksize_value"></a>
<a id="Return_value_volblocksize_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_volblocksize_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_volblocksize_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_volblocksize_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_volblocksize_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_volblocksize_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_volblocksize_source"></a>
<a id="Return_value_volblocksize_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_volblocksize_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_volblocksize_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_volblocksize_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_volblocksize_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_volblocksize_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_volblocksize_source_info"></a>
<a id="Return_value_volblocksize_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_key_format"></a>
<a id="Return_value_key_format"></a>
#### key_format

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Format of the encryption key (hex/raw/passphrase). Only relevant for encrypted datasets.
- No Additional Properties
<a id="headingReturn_value_key_format_parsed"></a>
<a id="Return_value_key_format_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_key_format_rawvalue"></a>
<a id="Return_value_key_format_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_key_format_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_key_format_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_key_format_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_key_format_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_key_format_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_key_format_value"></a>
<a id="Return_value_key_format_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_key_format_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_key_format_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_key_format_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_key_format_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_key_format_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_key_format_source"></a>
<a id="Return_value_key_format_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_key_format_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_key_format_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_key_format_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_key_format_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_key_format_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_key_format_source_info"></a>
<a id="Return_value_key_format_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_encryption_algorithm"></a>
<a id="Return_value_encryption_algorithm"></a>
#### encryption_algorithm

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Encryption algorithm used (e.g., AES-256-GCM). Only relevant for encrypted datasets.
- No Additional Properties
<a id="headingReturn_value_encryption_algorithm_parsed"></a>
<a id="Return_value_encryption_algorithm_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_encryption_algorithm_rawvalue"></a>
<a id="Return_value_encryption_algorithm_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_encryption_algorithm_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_encryption_algorithm_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_encryption_algorithm_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_encryption_algorithm_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_encryption_algorithm_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_encryption_algorithm_value"></a>
<a id="Return_value_encryption_algorithm_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_encryption_algorithm_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_encryption_algorithm_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_encryption_algorithm_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_encryption_algorithm_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_encryption_algorithm_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_encryption_algorithm_source"></a>
<a id="Return_value_encryption_algorithm_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_encryption_algorithm_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_encryption_algorithm_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_encryption_algorithm_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_encryption_algorithm_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_encryption_algorithm_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_encryption_algorithm_source_info"></a>
<a id="Return_value_encryption_algorithm_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_used"></a>
<a id="Return_value_used"></a>
#### used

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Total amount of disk space consumed by this dataset and all its children.
- No Additional Properties
<a id="headingReturn_value_used_parsed"></a>
<a id="Return_value_used_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_used_rawvalue"></a>
<a id="Return_value_used_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_used_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_used_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_used_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_used_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_used_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_used_value"></a>
<a id="Return_value_used_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_used_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_used_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_used_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_used_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_used_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_used_source"></a>
<a id="Return_value_used_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_used_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_used_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_used_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_used_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_used_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_used_source_info"></a>
<a id="Return_value_used_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_usedbychildren"></a>
<a id="Return_value_usedbychildren"></a>
#### usedbychildren

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by child datasets.
- No Additional Properties
<a id="headingReturn_value_usedbychildren_parsed"></a>
<a id="Return_value_usedbychildren_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_usedbychildren_rawvalue"></a>
<a id="Return_value_usedbychildren_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_usedbychildren_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_usedbychildren_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_usedbychildren_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_usedbychildren_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_usedbychildren_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_usedbychildren_value"></a>
<a id="Return_value_usedbychildren_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_usedbychildren_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_usedbychildren_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_usedbychildren_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_usedbychildren_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_usedbychildren_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_usedbychildren_source"></a>
<a id="Return_value_usedbychildren_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_usedbychildren_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_usedbychildren_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_usedbychildren_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_usedbychildren_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_usedbychildren_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_usedbychildren_source_info"></a>
<a id="Return_value_usedbychildren_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_usedbydataset"></a>
<a id="Return_value_usedbydataset"></a>
#### usedbydataset

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by this dataset itself, excluding children and snapshots.
- No Additional Properties
<a id="headingReturn_value_usedbydataset_parsed"></a>
<a id="Return_value_usedbydataset_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_usedbydataset_rawvalue"></a>
<a id="Return_value_usedbydataset_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_usedbydataset_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_usedbydataset_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_usedbydataset_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_usedbydataset_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_usedbydataset_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_usedbydataset_value"></a>
<a id="Return_value_usedbydataset_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_usedbydataset_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_usedbydataset_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_usedbydataset_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_usedbydataset_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_usedbydataset_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_usedbydataset_source"></a>
<a id="Return_value_usedbydataset_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_usedbydataset_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_usedbydataset_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_usedbydataset_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_usedbydataset_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_usedbydataset_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_usedbydataset_source_info"></a>
<a id="Return_value_usedbydataset_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_usedbyrefreservation"></a>
<a id="Return_value_usedbyrefreservation"></a>
#### usedbyrefreservation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by the refreservation of this dataset.
- No Additional Properties
<a id="headingReturn_value_usedbyrefreservation_parsed"></a>
<a id="Return_value_usedbyrefreservation_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_usedbyrefreservation_rawvalue"></a>
<a id="Return_value_usedbyrefreservation_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_usedbyrefreservation_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_usedbyrefreservation_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_usedbyrefreservation_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_usedbyrefreservation_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_usedbyrefreservation_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_usedbyrefreservation_value"></a>
<a id="Return_value_usedbyrefreservation_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_usedbyrefreservation_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_usedbyrefreservation_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_usedbyrefreservation_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_usedbyrefreservation_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_usedbyrefreservation_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_usedbyrefreservation_source"></a>
<a id="Return_value_usedbyrefreservation_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_usedbyrefreservation_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_usedbyrefreservation_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_usedbyrefreservation_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_usedbyrefreservation_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_usedbyrefreservation_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_usedbyrefreservation_source_info"></a>
<a id="Return_value_usedbyrefreservation_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_usedbysnapshots"></a>
<a id="Return_value_usedbysnapshots"></a>
#### usedbysnapshots

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by snapshots of this dataset.
- No Additional Properties
<a id="headingReturn_value_usedbysnapshots_parsed"></a>
<a id="Return_value_usedbysnapshots_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_usedbysnapshots_rawvalue"></a>
<a id="Return_value_usedbysnapshots_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_usedbysnapshots_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_usedbysnapshots_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_usedbysnapshots_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_usedbysnapshots_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_usedbysnapshots_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_usedbysnapshots_value"></a>
<a id="Return_value_usedbysnapshots_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_usedbysnapshots_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_usedbysnapshots_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_usedbysnapshots_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_usedbysnapshots_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_usedbysnapshots_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_usedbysnapshots_source"></a>
<a id="Return_value_usedbysnapshots_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_usedbysnapshots_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_usedbysnapshots_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_usedbysnapshots_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_usedbysnapshots_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_usedbysnapshots_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_usedbysnapshots_source_info"></a>
<a id="Return_value_usedbysnapshots_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_available"></a>
<a id="Return_value_available"></a>
#### available

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space available to this dataset and its children.
- No Additional Properties
<a id="headingReturn_value_available_parsed"></a>
<a id="Return_value_available_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_available_rawvalue"></a>
<a id="Return_value_available_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_available_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_available_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_available_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_available_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_available_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_available_value"></a>
<a id="Return_value_available_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_available_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_available_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_available_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_available_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_available_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_available_source"></a>
<a id="Return_value_available_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_available_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_available_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_available_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_available_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_available_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_available_source_info"></a>
<a id="Return_value_available_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_special_small_block_size"></a>
<a id="Return_value_special_small_block_size"></a>
#### special_small_block_size

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Size threshold below which blocks are stored on special vdevs if configured.
- No Additional Properties
<a id="headingReturn_value_special_small_block_size_parsed"></a>
<a id="Return_value_special_small_block_size_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_special_small_block_size_rawvalue"></a>
<a id="Return_value_special_small_block_size_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_special_small_block_size_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_special_small_block_size_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_special_small_block_size_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_special_small_block_size_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_special_small_block_size_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_special_small_block_size_value"></a>
<a id="Return_value_special_small_block_size_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_special_small_block_size_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_special_small_block_size_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_special_small_block_size_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_special_small_block_size_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_special_small_block_size_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_special_small_block_size_source"></a>
<a id="Return_value_special_small_block_size_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_special_small_block_size_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_special_small_block_size_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_special_small_block_size_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_special_small_block_size_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_special_small_block_size_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_special_small_block_size_source_info"></a>
<a id="Return_value_special_small_block_size_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_pbkdf2iters"></a>
<a id="Return_value_pbkdf2iters"></a>
#### pbkdf2iters

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Number of PBKDF2 iterations used for passphrase-based encryption keys.
- No Additional Properties
<a id="headingReturn_value_pbkdf2iters_parsed"></a>
<a id="Return_value_pbkdf2iters_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_pbkdf2iters_rawvalue"></a>
<a id="Return_value_pbkdf2iters_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_pbkdf2iters_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_pbkdf2iters_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_pbkdf2iters_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_pbkdf2iters_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_pbkdf2iters_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_pbkdf2iters_value"></a>
<a id="Return_value_pbkdf2iters_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_pbkdf2iters_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_pbkdf2iters_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_pbkdf2iters_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_pbkdf2iters_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_pbkdf2iters_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_pbkdf2iters_source"></a>
<a id="Return_value_pbkdf2iters_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_pbkdf2iters_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_pbkdf2iters_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_pbkdf2iters_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_pbkdf2iters_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_pbkdf2iters_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_pbkdf2iters_source_info"></a>
<a id="Return_value_pbkdf2iters_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_creation"></a>
<a id="Return_value_creation"></a>
#### creation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Timestamp when this dataset was created.
- No Additional Properties
<a id="headingReturn_value_creation_parsed"></a>
<a id="Return_value_creation_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_creation_rawvalue"></a>
<a id="Return_value_creation_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_creation_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_creation_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_creation_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_creation_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_creation_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_creation_value"></a>
<a id="Return_value_creation_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_creation_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_creation_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_creation_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_creation_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_creation_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_creation_source"></a>
<a id="Return_value_creation_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_creation_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_creation_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_creation_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_creation_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_creation_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_creation_source_info"></a>
<a id="Return_value_creation_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_snapdev"></a>
<a id="Return_value_snapdev"></a>
#### snapdev

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Controls visibility of volume snapshots under /dev/zvol/<pool>/.
- No Additional Properties
<a id="headingReturn_value_snapdev_parsed"></a>
<a id="Return_value_snapdev_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_snapdev_rawvalue"></a>
<a id="Return_value_snapdev_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_snapdev_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_snapdev_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_snapdev_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_snapdev_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_snapdev_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_snapdev_value"></a>
<a id="Return_value_snapdev_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_snapdev_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_snapdev_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_snapdev_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_snapdev_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_snapdev_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_snapdev_source"></a>
<a id="Return_value_snapdev_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_snapdev_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_snapdev_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_snapdev_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_snapdev_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_snapdev_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_snapdev_source_info"></a>
<a id="Return_value_snapdev_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_mountpoint"></a>
<a id="Return_value_mountpoint"></a>
#### mountpoint

- Schema name: `Mountpoint`

Filesystem path where this dataset is mounted. Null for unmounted datasets or volumes.
<a id="Return_value_mountpoint_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_mountpoint_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_mountpoint_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_mountpoint_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_mountpoint_anyOf_i1)

- Type: null

<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
