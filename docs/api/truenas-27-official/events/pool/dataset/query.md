---
title: pool.dataset.query
kind: event
source_rst: _sources/api_events_pool.dataset.query.rst.txt
source_html: api_events_pool.dataset.query.html
required_roles:
  - DATASET_READ
---

# pool.dataset.query

## Summary

Sent on pool.dataset changes.

## Required Roles

- `DATASET_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `PoolDatasetAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `PoolDatasetEntry`
- Type: object
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id

- Schema name: `Id`
- Type: string

The full dataset path including pool name.
Examples:

```json
"tank/dataset/child"
```

<a id="headingADDED_fields_type"></a>
<a id="ADDED_fields_type"></a>
##### type

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

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name

- Schema name: `Name`
- Type: string

The dataset name without the pool prefix.

<a id="headingADDED_fields_pool"></a>
<a id="ADDED_fields_pool"></a>
##### pool

- Schema name: `Pool`
- Type: string

The name of the ZFS pool containing this dataset.

<a id="headingADDED_fields_encrypted"></a>
<a id="ADDED_fields_encrypted"></a>
##### encrypted

- Schema name: `Encrypted`
- Type: boolean

Whether the dataset is encrypted.

<a id="headingADDED_fields_encryption_root"></a>
<a id="ADDED_fields_encryption_root"></a>
##### encryption_root

- Schema name: `Encryption Root`

The root dataset where encryption is enabled. `null` if the dataset is not encrypted.
<a id="ADDED_fields_encryption_root_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_encryption_root_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_encryption_root_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_encryption_root_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_encryption_root_anyOf_i1)

- Type: null

<a id="headingADDED_fields_key_loaded"></a>
<a id="ADDED_fields_key_loaded"></a>
##### key_loaded

- Schema name: `Key Loaded`

Whether the encryption key is currently loaded for encrypted datasets. `null` for unencrypted datasets.
<a id="ADDED_fields_key_loaded_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_key_loaded_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_key_loaded_anyOf_i0)

- Type: boolean

<a id="tab-pane_ADDED_fields_key_loaded_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_key_loaded_anyOf_i1)

- Type: null

<a id="headingADDED_fields_children"></a>
<a id="ADDED_fields_children"></a>
##### children

- Schema name: `Children`
- Type: array

Array of child dataset objects nested under this dataset.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_children_items"></a>
- Type: object

<a id="headingADDED_fields_user_properties"></a>
<a id="ADDED_fields_user_properties"></a>
##### user_properties

- Schema name: `PoolDatasetEntryUserProperties`
- Type: object

Custom user-defined ZFS properties set on this dataset as key-value pairs.
<a id="headingADDED_fields_user_properties_comments"></a>
<a id="ADDED_fields_user_properties_comments"></a>
###### comments

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS comments property for storing descriptive text about the dataset.
- No Additional Properties
<a id="headingADDED_fields_user_properties_comments_parsed"></a>
<a id="ADDED_fields_user_properties_comments_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_user_properties_comments_rawvalue"></a>
<a id="ADDED_fields_user_properties_comments_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_user_properties_comments_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_user_properties_comments_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_user_properties_comments_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_user_properties_comments_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_user_properties_comments_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_user_properties_comments_value"></a>
<a id="ADDED_fields_user_properties_comments_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_user_properties_comments_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_user_properties_comments_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_user_properties_comments_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_user_properties_comments_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_user_properties_comments_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_user_properties_comments_source"></a>
<a id="ADDED_fields_user_properties_comments_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_user_properties_comments_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_user_properties_comments_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_user_properties_comments_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_user_properties_comments_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_user_properties_comments_source_anyOf_i1)

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

<a id="headingADDED_fields_user_properties_comments_source_info"></a>
<a id="ADDED_fields_user_properties_comments_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_user_properties_quota_warning"></a>
<a id="ADDED_fields_user_properties_quota_warning"></a>
###### quota_warning

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS quota warning threshold property as a percentage.
- No Additional Properties
<a id="headingADDED_fields_user_properties_quota_warning_parsed"></a>
<a id="ADDED_fields_user_properties_quota_warning_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_user_properties_quota_warning_rawvalue"></a>
<a id="ADDED_fields_user_properties_quota_warning_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_user_properties_quota_warning_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_user_properties_quota_warning_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_user_properties_quota_warning_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_user_properties_quota_warning_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_user_properties_quota_warning_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_user_properties_quota_warning_value"></a>
<a id="ADDED_fields_user_properties_quota_warning_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_user_properties_quota_warning_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_user_properties_quota_warning_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_user_properties_quota_warning_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_user_properties_quota_warning_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_user_properties_quota_warning_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_user_properties_quota_warning_source"></a>
<a id="ADDED_fields_user_properties_quota_warning_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_user_properties_quota_warning_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_user_properties_quota_warning_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_user_properties_quota_warning_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_user_properties_quota_warning_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_user_properties_quota_warning_source_anyOf_i1)

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

<a id="headingADDED_fields_user_properties_quota_warning_source_info"></a>
<a id="ADDED_fields_user_properties_quota_warning_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_user_properties_quota_critical"></a>
<a id="ADDED_fields_user_properties_quota_critical"></a>
###### quota_critical

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS quota critical threshold property as a percentage.
- No Additional Properties
<a id="headingADDED_fields_user_properties_quota_critical_parsed"></a>
<a id="ADDED_fields_user_properties_quota_critical_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_user_properties_quota_critical_rawvalue"></a>
<a id="ADDED_fields_user_properties_quota_critical_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_user_properties_quota_critical_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_user_properties_quota_critical_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_user_properties_quota_critical_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_user_properties_quota_critical_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_user_properties_quota_critical_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_user_properties_quota_critical_value"></a>
<a id="ADDED_fields_user_properties_quota_critical_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_user_properties_quota_critical_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_user_properties_quota_critical_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_user_properties_quota_critical_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_user_properties_quota_critical_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_user_properties_quota_critical_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_user_properties_quota_critical_source"></a>
<a id="ADDED_fields_user_properties_quota_critical_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_user_properties_quota_critical_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_user_properties_quota_critical_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_user_properties_quota_critical_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_user_properties_quota_critical_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_user_properties_quota_critical_source_anyOf_i1)

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

<a id="headingADDED_fields_user_properties_quota_critical_source_info"></a>
<a id="ADDED_fields_user_properties_quota_critical_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_user_properties_refquota_warning"></a>
<a id="ADDED_fields_user_properties_refquota_warning"></a>
###### refquota_warning

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS reference quota warning threshold property as a percentage.
- No Additional Properties
<a id="headingADDED_fields_user_properties_refquota_warning_parsed"></a>
<a id="ADDED_fields_user_properties_refquota_warning_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_user_properties_refquota_warning_rawvalue"></a>
<a id="ADDED_fields_user_properties_refquota_warning_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_user_properties_refquota_warning_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_user_properties_refquota_warning_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_user_properties_refquota_warning_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_user_properties_refquota_warning_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_user_properties_refquota_warning_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_user_properties_refquota_warning_value"></a>
<a id="ADDED_fields_user_properties_refquota_warning_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_user_properties_refquota_warning_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_user_properties_refquota_warning_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_user_properties_refquota_warning_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_user_properties_refquota_warning_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_user_properties_refquota_warning_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_user_properties_refquota_warning_source"></a>
<a id="ADDED_fields_user_properties_refquota_warning_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_user_properties_refquota_warning_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_user_properties_refquota_warning_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_user_properties_refquota_warning_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_user_properties_refquota_warning_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_user_properties_refquota_warning_source_anyOf_i1)

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

<a id="headingADDED_fields_user_properties_refquota_warning_source_info"></a>
<a id="ADDED_fields_user_properties_refquota_warning_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_user_properties_refquota_critical"></a>
<a id="ADDED_fields_user_properties_refquota_critical"></a>
###### refquota_critical

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS reference quota critical threshold property as a percentage.
- No Additional Properties
<a id="headingADDED_fields_user_properties_refquota_critical_parsed"></a>
<a id="ADDED_fields_user_properties_refquota_critical_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_user_properties_refquota_critical_rawvalue"></a>
<a id="ADDED_fields_user_properties_refquota_critical_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_user_properties_refquota_critical_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_user_properties_refquota_critical_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_user_properties_refquota_critical_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_user_properties_refquota_critical_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_user_properties_refquota_critical_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_user_properties_refquota_critical_value"></a>
<a id="ADDED_fields_user_properties_refquota_critical_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_user_properties_refquota_critical_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_user_properties_refquota_critical_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_user_properties_refquota_critical_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_user_properties_refquota_critical_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_user_properties_refquota_critical_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_user_properties_refquota_critical_source"></a>
<a id="ADDED_fields_user_properties_refquota_critical_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_user_properties_refquota_critical_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_user_properties_refquota_critical_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_user_properties_refquota_critical_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_user_properties_refquota_critical_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_user_properties_refquota_critical_source_anyOf_i1)

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

<a id="headingADDED_fields_user_properties_refquota_critical_source_info"></a>
<a id="ADDED_fields_user_properties_refquota_critical_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_user_properties_managedby"></a>
<a id="ADDED_fields_user_properties_managedby"></a>
###### managedby

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Identifies which service or system manages this dataset.
- No Additional Properties
<a id="headingADDED_fields_user_properties_managedby_parsed"></a>
<a id="ADDED_fields_user_properties_managedby_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_user_properties_managedby_rawvalue"></a>
<a id="ADDED_fields_user_properties_managedby_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_user_properties_managedby_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_user_properties_managedby_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_user_properties_managedby_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_user_properties_managedby_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_user_properties_managedby_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_user_properties_managedby_value"></a>
<a id="ADDED_fields_user_properties_managedby_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_user_properties_managedby_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_user_properties_managedby_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_user_properties_managedby_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_user_properties_managedby_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_user_properties_managedby_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_user_properties_managedby_source"></a>
<a id="ADDED_fields_user_properties_managedby_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_user_properties_managedby_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_user_properties_managedby_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_user_properties_managedby_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_user_properties_managedby_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_user_properties_managedby_source_anyOf_i1)

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

<a id="headingADDED_fields_user_properties_managedby_source_info"></a>
<a id="ADDED_fields_user_properties_managedby_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_user_properties_additionalProperties"></a>
<a id="ADDED_fields_user_properties_additionalProperties"></a>
###### Additional Properties

Additional Properties of any type are allowed.
- Type: object

<a id="headingADDED_fields_locked"></a>
<a id="ADDED_fields_locked"></a>
##### locked

- Schema name: `Locked`
- Type: boolean

Whether an encrypted dataset is currently locked (key not loaded).

<a id="headingADDED_fields_tier"></a>
<a id="ADDED_fields_tier"></a>
##### tier

Performance tier. `null` if tiering disabled, if underlying pool does not support tiering, or if deduplication is enabled on the dataset.
<a id="ADDED_fields_tier_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_tier_anyOf_i0"></a>
###### [TierInfo](#tab-pane_ADDED_fields_tier_anyOf_i0)

- Schema name: `TierInfo`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_tier_anyOf_i0_tier_type"></a>
<a id="ADDED_fields_tier_anyOf_i0_tier_type"></a>
###### tier_type (required)

- Schema name: `Tier Type`
- Type: enum (of string)

Storage performance tier for this share.
###### Must be one of:

- "REGULAR"
- "PERFORMANCE"

<a id="headingADDED_fields_tier_anyOf_i0_tier_job"></a>
<a id="ADDED_fields_tier_anyOf_i0_tier_job"></a>
###### tier_job

- Default: null

Most recent rewrite job for this share's dataset, or `null` if no job history exists.
<a id="ADDED_fields_tier_anyOf_i0_tier_job_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0"></a>
###### [ZfsTierRewriteJobEntry](#tab-pane_ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0)

- Schema name: `ZfsTierRewriteJobEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
<a id="ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
###### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

<a id="headingADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
<a id="ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
###### dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

<a id="headingADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
<a id="ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
###### job_uuid (required)

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

<a id="headingADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
<a id="ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
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

<a id="tab-pane_ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i1)

- Type: null

<a id="tab-pane_ADDED_fields_tier_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_tier_anyOf_i1)

- Type: null

<a id="headingADDED_fields_deduplication"></a>
<a id="ADDED_fields_deduplication"></a>
##### deduplication

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS deduplication setting - whether identical data blocks are stored only once.
- No Additional Properties
<a id="headingADDED_fields_deduplication_parsed"></a>
<a id="ADDED_fields_deduplication_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_deduplication_rawvalue"></a>
<a id="ADDED_fields_deduplication_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_deduplication_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_deduplication_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_deduplication_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_deduplication_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_deduplication_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_deduplication_value"></a>
<a id="ADDED_fields_deduplication_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_deduplication_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_deduplication_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_deduplication_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_deduplication_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_deduplication_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_deduplication_source"></a>
<a id="ADDED_fields_deduplication_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_deduplication_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_deduplication_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_deduplication_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_deduplication_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_deduplication_source_anyOf_i1)

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

<a id="headingADDED_fields_deduplication_source_info"></a>
<a id="ADDED_fields_deduplication_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_aclmode"></a>
<a id="ADDED_fields_aclmode"></a>
##### aclmode

- Schema name: `PoolDatasetEntryProperty`
- Type: object

How Access Control Lists (ACLs) are handled when chmod is used.
- No Additional Properties
<a id="headingADDED_fields_aclmode_parsed"></a>
<a id="ADDED_fields_aclmode_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_aclmode_rawvalue"></a>
<a id="ADDED_fields_aclmode_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_aclmode_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_aclmode_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_aclmode_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_aclmode_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_aclmode_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_aclmode_value"></a>
<a id="ADDED_fields_aclmode_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_aclmode_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_aclmode_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_aclmode_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_aclmode_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_aclmode_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_aclmode_source"></a>
<a id="ADDED_fields_aclmode_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_aclmode_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_aclmode_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_aclmode_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_aclmode_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_aclmode_source_anyOf_i1)

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

<a id="headingADDED_fields_aclmode_source_info"></a>
<a id="ADDED_fields_aclmode_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_acltype"></a>
<a id="ADDED_fields_acltype"></a>
##### acltype

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The type of Access Control List system used (NFSV4, POSIX, or OFF).
- No Additional Properties
<a id="headingADDED_fields_acltype_parsed"></a>
<a id="ADDED_fields_acltype_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_acltype_rawvalue"></a>
<a id="ADDED_fields_acltype_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_acltype_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_acltype_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_acltype_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_acltype_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_acltype_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_acltype_value"></a>
<a id="ADDED_fields_acltype_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_acltype_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_acltype_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_acltype_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_acltype_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_acltype_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_acltype_source"></a>
<a id="ADDED_fields_acltype_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_acltype_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_acltype_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_acltype_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_acltype_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_acltype_source_anyOf_i1)

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

<a id="headingADDED_fields_acltype_source_info"></a>
<a id="ADDED_fields_acltype_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_xattr"></a>
<a id="ADDED_fields_xattr"></a>
##### xattr

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Extended attributes storage method (on/off).
- No Additional Properties
<a id="headingADDED_fields_xattr_parsed"></a>
<a id="ADDED_fields_xattr_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_xattr_rawvalue"></a>
<a id="ADDED_fields_xattr_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_xattr_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_xattr_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_xattr_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_xattr_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_xattr_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_xattr_value"></a>
<a id="ADDED_fields_xattr_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_xattr_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_xattr_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_xattr_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_xattr_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_xattr_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_xattr_source"></a>
<a id="ADDED_fields_xattr_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_xattr_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_xattr_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_xattr_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_xattr_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_xattr_source_anyOf_i1)

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

<a id="headingADDED_fields_xattr_source_info"></a>
<a id="ADDED_fields_xattr_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_atime"></a>
<a id="ADDED_fields_atime"></a>
##### atime

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Whether file access times are updated when files are accessed.
- No Additional Properties
<a id="headingADDED_fields_atime_parsed"></a>
<a id="ADDED_fields_atime_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_atime_rawvalue"></a>
<a id="ADDED_fields_atime_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_atime_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_atime_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_atime_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_atime_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_atime_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_atime_value"></a>
<a id="ADDED_fields_atime_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_atime_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_atime_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_atime_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_atime_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_atime_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_atime_source"></a>
<a id="ADDED_fields_atime_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_atime_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_atime_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_atime_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_atime_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_atime_source_anyOf_i1)

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

<a id="headingADDED_fields_atime_source_info"></a>
<a id="ADDED_fields_atime_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_casesensitivity"></a>
<a id="ADDED_fields_casesensitivity"></a>
##### casesensitivity

- Schema name: `PoolDatasetEntryProperty`
- Type: object

File name case sensitivity setting (sensitive/insensitive).
- No Additional Properties
<a id="headingADDED_fields_casesensitivity_parsed"></a>
<a id="ADDED_fields_casesensitivity_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_casesensitivity_rawvalue"></a>
<a id="ADDED_fields_casesensitivity_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_casesensitivity_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_casesensitivity_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_casesensitivity_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_casesensitivity_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_casesensitivity_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_casesensitivity_value"></a>
<a id="ADDED_fields_casesensitivity_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_casesensitivity_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_casesensitivity_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_casesensitivity_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_casesensitivity_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_casesensitivity_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_casesensitivity_source"></a>
<a id="ADDED_fields_casesensitivity_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_casesensitivity_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_casesensitivity_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_casesensitivity_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_casesensitivity_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_casesensitivity_source_anyOf_i1)

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

<a id="headingADDED_fields_casesensitivity_source_info"></a>
<a id="ADDED_fields_casesensitivity_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_checksum"></a>
<a id="ADDED_fields_checksum"></a>
##### checksum

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Data integrity checksum algorithm used for this dataset.
- No Additional Properties
<a id="headingADDED_fields_checksum_parsed"></a>
<a id="ADDED_fields_checksum_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_checksum_rawvalue"></a>
<a id="ADDED_fields_checksum_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_checksum_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_checksum_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_checksum_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_checksum_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_checksum_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_checksum_value"></a>
<a id="ADDED_fields_checksum_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_checksum_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_checksum_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_checksum_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_checksum_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_checksum_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_checksum_source"></a>
<a id="ADDED_fields_checksum_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_checksum_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_checksum_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_checksum_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_checksum_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_checksum_source_anyOf_i1)

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

<a id="headingADDED_fields_checksum_source_info"></a>
<a id="ADDED_fields_checksum_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_exec"></a>
<a id="ADDED_fields_exec"></a>
##### exec

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Whether files in this dataset can be executed.
- No Additional Properties
<a id="headingADDED_fields_exec_parsed"></a>
<a id="ADDED_fields_exec_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_exec_rawvalue"></a>
<a id="ADDED_fields_exec_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_exec_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_exec_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_exec_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_exec_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_exec_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_exec_value"></a>
<a id="ADDED_fields_exec_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_exec_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_exec_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_exec_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_exec_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_exec_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_exec_source"></a>
<a id="ADDED_fields_exec_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_exec_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_exec_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_exec_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_exec_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_exec_source_anyOf_i1)

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

<a id="headingADDED_fields_exec_source_info"></a>
<a id="ADDED_fields_exec_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_sync"></a>
<a id="ADDED_fields_sync"></a>
##### sync

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Synchronous write behavior (standard/always/disabled).
- No Additional Properties
<a id="headingADDED_fields_sync_parsed"></a>
<a id="ADDED_fields_sync_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_sync_rawvalue"></a>
<a id="ADDED_fields_sync_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_sync_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_sync_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_sync_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_sync_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_sync_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_sync_value"></a>
<a id="ADDED_fields_sync_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_sync_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_sync_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_sync_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_sync_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_sync_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_sync_source"></a>
<a id="ADDED_fields_sync_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_sync_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_sync_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_sync_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_sync_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_sync_source_anyOf_i1)

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

<a id="headingADDED_fields_sync_source_info"></a>
<a id="ADDED_fields_sync_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_compression"></a>
<a id="ADDED_fields_compression"></a>
##### compression

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Compression algorithm and level applied to data in this dataset.
- No Additional Properties
<a id="headingADDED_fields_compression_parsed"></a>
<a id="ADDED_fields_compression_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_compression_rawvalue"></a>
<a id="ADDED_fields_compression_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_compression_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_compression_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_compression_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_compression_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_compression_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_compression_value"></a>
<a id="ADDED_fields_compression_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_compression_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_compression_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_compression_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_compression_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_compression_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_compression_source"></a>
<a id="ADDED_fields_compression_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_compression_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_compression_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_compression_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_compression_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_compression_source_anyOf_i1)

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

<a id="headingADDED_fields_compression_source_info"></a>
<a id="ADDED_fields_compression_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_compressratio"></a>
<a id="ADDED_fields_compressratio"></a>
##### compressratio

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The achieved compression ratio as a decimal (e.g., '2.50x').
- No Additional Properties
<a id="headingADDED_fields_compressratio_parsed"></a>
<a id="ADDED_fields_compressratio_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_compressratio_rawvalue"></a>
<a id="ADDED_fields_compressratio_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_compressratio_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_compressratio_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_compressratio_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_compressratio_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_compressratio_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_compressratio_value"></a>
<a id="ADDED_fields_compressratio_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_compressratio_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_compressratio_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_compressratio_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_compressratio_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_compressratio_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_compressratio_source"></a>
<a id="ADDED_fields_compressratio_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_compressratio_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_compressratio_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_compressratio_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_compressratio_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_compressratio_source_anyOf_i1)

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

<a id="headingADDED_fields_compressratio_source_info"></a>
<a id="ADDED_fields_compressratio_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_origin"></a>
<a id="ADDED_fields_origin"></a>
##### origin

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The snapshot from which this clone was created. Empty for non-clone datasets.
- No Additional Properties
<a id="headingADDED_fields_origin_parsed"></a>
<a id="ADDED_fields_origin_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_origin_rawvalue"></a>
<a id="ADDED_fields_origin_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_origin_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_origin_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_origin_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_origin_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_origin_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_origin_value"></a>
<a id="ADDED_fields_origin_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_origin_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_origin_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_origin_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_origin_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_origin_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_origin_source"></a>
<a id="ADDED_fields_origin_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_origin_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_origin_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_origin_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_origin_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_origin_source_anyOf_i1)

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

<a id="headingADDED_fields_origin_source_info"></a>
<a id="ADDED_fields_origin_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_quota"></a>
<a id="ADDED_fields_quota"></a>
##### quota

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Maximum amount of disk space this dataset and its children can consume.
- No Additional Properties
<a id="headingADDED_fields_quota_parsed"></a>
<a id="ADDED_fields_quota_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_quota_rawvalue"></a>
<a id="ADDED_fields_quota_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_quota_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_quota_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_quota_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_quota_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_quota_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_quota_value"></a>
<a id="ADDED_fields_quota_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_quota_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_quota_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_quota_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_quota_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_quota_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_quota_source"></a>
<a id="ADDED_fields_quota_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_quota_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_quota_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_quota_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_quota_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_quota_source_anyOf_i1)

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

<a id="headingADDED_fields_quota_source_info"></a>
<a id="ADDED_fields_quota_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_refquota"></a>
<a id="ADDED_fields_refquota"></a>
##### refquota

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Maximum amount of disk space this dataset itself can consume (excluding children).
- No Additional Properties
<a id="headingADDED_fields_refquota_parsed"></a>
<a id="ADDED_fields_refquota_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_refquota_rawvalue"></a>
<a id="ADDED_fields_refquota_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_refquota_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_refquota_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_refquota_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_refquota_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_refquota_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_refquota_value"></a>
<a id="ADDED_fields_refquota_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_refquota_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_refquota_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_refquota_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_refquota_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_refquota_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_refquota_source"></a>
<a id="ADDED_fields_refquota_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_refquota_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_refquota_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_refquota_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_refquota_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_refquota_source_anyOf_i1)

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

<a id="headingADDED_fields_refquota_source_info"></a>
<a id="ADDED_fields_refquota_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_reservation"></a>
<a id="ADDED_fields_reservation"></a>
##### reservation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Minimum amount of disk space guaranteed to be available to this dataset and its children.
- No Additional Properties
<a id="headingADDED_fields_reservation_parsed"></a>
<a id="ADDED_fields_reservation_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_reservation_rawvalue"></a>
<a id="ADDED_fields_reservation_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_reservation_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_reservation_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_reservation_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_reservation_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_reservation_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_reservation_value"></a>
<a id="ADDED_fields_reservation_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_reservation_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_reservation_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_reservation_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_reservation_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_reservation_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_reservation_source"></a>
<a id="ADDED_fields_reservation_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_reservation_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_reservation_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_reservation_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_reservation_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_reservation_source_anyOf_i1)

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

<a id="headingADDED_fields_reservation_source_info"></a>
<a id="ADDED_fields_reservation_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_refreservation"></a>
<a id="ADDED_fields_refreservation"></a>
##### refreservation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Minimum amount of disk space guaranteed to be available to this dataset itself.
- No Additional Properties
<a id="headingADDED_fields_refreservation_parsed"></a>
<a id="ADDED_fields_refreservation_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_refreservation_rawvalue"></a>
<a id="ADDED_fields_refreservation_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_refreservation_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_refreservation_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_refreservation_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_refreservation_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_refreservation_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_refreservation_value"></a>
<a id="ADDED_fields_refreservation_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_refreservation_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_refreservation_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_refreservation_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_refreservation_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_refreservation_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_refreservation_source"></a>
<a id="ADDED_fields_refreservation_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_refreservation_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_refreservation_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_refreservation_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_refreservation_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_refreservation_source_anyOf_i1)

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

<a id="headingADDED_fields_refreservation_source_info"></a>
<a id="ADDED_fields_refreservation_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_copies"></a>
<a id="ADDED_fields_copies"></a>
##### copies

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Number of copies of data blocks to maintain for redundancy (1-3).
- No Additional Properties
<a id="headingADDED_fields_copies_parsed"></a>
<a id="ADDED_fields_copies_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_copies_rawvalue"></a>
<a id="ADDED_fields_copies_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_copies_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_copies_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_copies_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_copies_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_copies_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_copies_value"></a>
<a id="ADDED_fields_copies_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_copies_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_copies_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_copies_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_copies_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_copies_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_copies_source"></a>
<a id="ADDED_fields_copies_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_copies_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_copies_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_copies_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_copies_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_copies_source_anyOf_i1)

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

<a id="headingADDED_fields_copies_source_info"></a>
<a id="ADDED_fields_copies_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_snapdir"></a>
<a id="ADDED_fields_snapdir"></a>
##### snapdir

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Visibility of the .zfs/snapshot directory (visible/hidden).
- No Additional Properties
<a id="headingADDED_fields_snapdir_parsed"></a>
<a id="ADDED_fields_snapdir_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_snapdir_rawvalue"></a>
<a id="ADDED_fields_snapdir_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_snapdir_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_snapdir_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_snapdir_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_snapdir_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_snapdir_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_snapdir_value"></a>
<a id="ADDED_fields_snapdir_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_snapdir_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_snapdir_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_snapdir_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_snapdir_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_snapdir_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_snapdir_source"></a>
<a id="ADDED_fields_snapdir_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_snapdir_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_snapdir_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_snapdir_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_snapdir_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_snapdir_source_anyOf_i1)

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

<a id="headingADDED_fields_snapdir_source_info"></a>
<a id="ADDED_fields_snapdir_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_readonly"></a>
<a id="ADDED_fields_readonly"></a>
##### readonly

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Whether the dataset is read-only.
- No Additional Properties
<a id="headingADDED_fields_readonly_parsed"></a>
<a id="ADDED_fields_readonly_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_readonly_rawvalue"></a>
<a id="ADDED_fields_readonly_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_readonly_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_readonly_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_readonly_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_readonly_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_readonly_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_readonly_value"></a>
<a id="ADDED_fields_readonly_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_readonly_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_readonly_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_readonly_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_readonly_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_readonly_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_readonly_source"></a>
<a id="ADDED_fields_readonly_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_readonly_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_readonly_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_readonly_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_readonly_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_readonly_source_anyOf_i1)

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

<a id="headingADDED_fields_readonly_source_info"></a>
<a id="ADDED_fields_readonly_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_recordsize"></a>
<a id="ADDED_fields_recordsize"></a>
##### recordsize

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The suggested block size for files in this filesystem dataset.
- No Additional Properties
<a id="headingADDED_fields_recordsize_parsed"></a>
<a id="ADDED_fields_recordsize_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_recordsize_rawvalue"></a>
<a id="ADDED_fields_recordsize_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_recordsize_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_recordsize_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_recordsize_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_recordsize_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_recordsize_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_recordsize_value"></a>
<a id="ADDED_fields_recordsize_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_recordsize_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_recordsize_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_recordsize_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_recordsize_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_recordsize_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_recordsize_source"></a>
<a id="ADDED_fields_recordsize_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_recordsize_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_recordsize_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_recordsize_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_recordsize_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_recordsize_source_anyOf_i1)

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

<a id="headingADDED_fields_recordsize_source_info"></a>
<a id="ADDED_fields_recordsize_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_sparse"></a>
<a id="ADDED_fields_sparse"></a>
##### sparse

- Schema name: `PoolDatasetEntryProperty`
- Type: object

For volumes, whether to use sparse (thin) provisioning.
- No Additional Properties
<a id="headingADDED_fields_sparse_parsed"></a>
<a id="ADDED_fields_sparse_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_sparse_rawvalue"></a>
<a id="ADDED_fields_sparse_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_sparse_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_sparse_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_sparse_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_sparse_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_sparse_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_sparse_value"></a>
<a id="ADDED_fields_sparse_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_sparse_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_sparse_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_sparse_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_sparse_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_sparse_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_sparse_source"></a>
<a id="ADDED_fields_sparse_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_sparse_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_sparse_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_sparse_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_sparse_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_sparse_source_anyOf_i1)

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

<a id="headingADDED_fields_sparse_source_info"></a>
<a id="ADDED_fields_sparse_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_volsize"></a>
<a id="ADDED_fields_volsize"></a>
##### volsize

- Schema name: `PoolDatasetEntryProperty`
- Type: object

For volumes, the logical size of the volume.
- No Additional Properties
<a id="headingADDED_fields_volsize_parsed"></a>
<a id="ADDED_fields_volsize_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_volsize_rawvalue"></a>
<a id="ADDED_fields_volsize_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_volsize_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_volsize_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_volsize_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_volsize_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_volsize_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_volsize_value"></a>
<a id="ADDED_fields_volsize_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_volsize_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_volsize_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_volsize_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_volsize_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_volsize_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_volsize_source"></a>
<a id="ADDED_fields_volsize_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_volsize_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_volsize_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_volsize_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_volsize_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_volsize_source_anyOf_i1)

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

<a id="headingADDED_fields_volsize_source_info"></a>
<a id="ADDED_fields_volsize_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_volblocksize"></a>
<a id="ADDED_fields_volblocksize"></a>
##### volblocksize

- Schema name: `PoolDatasetEntryProperty`
- Type: object

For volumes, the block size used by the volume.
- No Additional Properties
<a id="headingADDED_fields_volblocksize_parsed"></a>
<a id="ADDED_fields_volblocksize_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_volblocksize_rawvalue"></a>
<a id="ADDED_fields_volblocksize_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_volblocksize_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_volblocksize_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_volblocksize_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_volblocksize_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_volblocksize_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_volblocksize_value"></a>
<a id="ADDED_fields_volblocksize_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_volblocksize_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_volblocksize_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_volblocksize_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_volblocksize_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_volblocksize_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_volblocksize_source"></a>
<a id="ADDED_fields_volblocksize_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_volblocksize_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_volblocksize_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_volblocksize_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_volblocksize_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_volblocksize_source_anyOf_i1)

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

<a id="headingADDED_fields_volblocksize_source_info"></a>
<a id="ADDED_fields_volblocksize_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_key_format"></a>
<a id="ADDED_fields_key_format"></a>
##### key_format

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Format of the encryption key (hex/raw/passphrase). Only relevant for encrypted datasets.
- No Additional Properties
<a id="headingADDED_fields_key_format_parsed"></a>
<a id="ADDED_fields_key_format_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_key_format_rawvalue"></a>
<a id="ADDED_fields_key_format_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_key_format_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_key_format_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_key_format_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_key_format_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_key_format_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_key_format_value"></a>
<a id="ADDED_fields_key_format_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_key_format_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_key_format_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_key_format_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_key_format_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_key_format_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_key_format_source"></a>
<a id="ADDED_fields_key_format_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_key_format_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_key_format_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_key_format_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_key_format_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_key_format_source_anyOf_i1)

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

<a id="headingADDED_fields_key_format_source_info"></a>
<a id="ADDED_fields_key_format_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_encryption_algorithm"></a>
<a id="ADDED_fields_encryption_algorithm"></a>
##### encryption_algorithm

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Encryption algorithm used (e.g., AES-256-GCM). Only relevant for encrypted datasets.
- No Additional Properties
<a id="headingADDED_fields_encryption_algorithm_parsed"></a>
<a id="ADDED_fields_encryption_algorithm_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_encryption_algorithm_rawvalue"></a>
<a id="ADDED_fields_encryption_algorithm_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_encryption_algorithm_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_encryption_algorithm_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_encryption_algorithm_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_encryption_algorithm_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_encryption_algorithm_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_encryption_algorithm_value"></a>
<a id="ADDED_fields_encryption_algorithm_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_encryption_algorithm_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_encryption_algorithm_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_encryption_algorithm_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_encryption_algorithm_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_encryption_algorithm_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_encryption_algorithm_source"></a>
<a id="ADDED_fields_encryption_algorithm_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_encryption_algorithm_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_encryption_algorithm_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_encryption_algorithm_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_encryption_algorithm_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_encryption_algorithm_source_anyOf_i1)

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

<a id="headingADDED_fields_encryption_algorithm_source_info"></a>
<a id="ADDED_fields_encryption_algorithm_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_used"></a>
<a id="ADDED_fields_used"></a>
##### used

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Total amount of disk space consumed by this dataset and all its children.
- No Additional Properties
<a id="headingADDED_fields_used_parsed"></a>
<a id="ADDED_fields_used_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_used_rawvalue"></a>
<a id="ADDED_fields_used_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_used_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_used_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_used_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_used_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_used_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_used_value"></a>
<a id="ADDED_fields_used_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_used_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_used_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_used_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_used_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_used_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_used_source"></a>
<a id="ADDED_fields_used_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_used_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_used_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_used_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_used_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_used_source_anyOf_i1)

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

<a id="headingADDED_fields_used_source_info"></a>
<a id="ADDED_fields_used_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_usedbychildren"></a>
<a id="ADDED_fields_usedbychildren"></a>
##### usedbychildren

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by child datasets.
- No Additional Properties
<a id="headingADDED_fields_usedbychildren_parsed"></a>
<a id="ADDED_fields_usedbychildren_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_usedbychildren_rawvalue"></a>
<a id="ADDED_fields_usedbychildren_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_usedbychildren_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_usedbychildren_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_usedbychildren_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_usedbychildren_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_usedbychildren_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_usedbychildren_value"></a>
<a id="ADDED_fields_usedbychildren_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_usedbychildren_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_usedbychildren_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_usedbychildren_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_usedbychildren_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_usedbychildren_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_usedbychildren_source"></a>
<a id="ADDED_fields_usedbychildren_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_usedbychildren_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_usedbychildren_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_usedbychildren_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_usedbychildren_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_usedbychildren_source_anyOf_i1)

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

<a id="headingADDED_fields_usedbychildren_source_info"></a>
<a id="ADDED_fields_usedbychildren_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_usedbydataset"></a>
<a id="ADDED_fields_usedbydataset"></a>
##### usedbydataset

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by this dataset itself, excluding children and snapshots.
- No Additional Properties
<a id="headingADDED_fields_usedbydataset_parsed"></a>
<a id="ADDED_fields_usedbydataset_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_usedbydataset_rawvalue"></a>
<a id="ADDED_fields_usedbydataset_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_usedbydataset_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_usedbydataset_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_usedbydataset_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_usedbydataset_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_usedbydataset_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_usedbydataset_value"></a>
<a id="ADDED_fields_usedbydataset_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_usedbydataset_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_usedbydataset_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_usedbydataset_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_usedbydataset_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_usedbydataset_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_usedbydataset_source"></a>
<a id="ADDED_fields_usedbydataset_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_usedbydataset_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_usedbydataset_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_usedbydataset_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_usedbydataset_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_usedbydataset_source_anyOf_i1)

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

<a id="headingADDED_fields_usedbydataset_source_info"></a>
<a id="ADDED_fields_usedbydataset_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_usedbyrefreservation"></a>
<a id="ADDED_fields_usedbyrefreservation"></a>
##### usedbyrefreservation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by the refreservation of this dataset.
- No Additional Properties
<a id="headingADDED_fields_usedbyrefreservation_parsed"></a>
<a id="ADDED_fields_usedbyrefreservation_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_usedbyrefreservation_rawvalue"></a>
<a id="ADDED_fields_usedbyrefreservation_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_usedbyrefreservation_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_usedbyrefreservation_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_usedbyrefreservation_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_usedbyrefreservation_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_usedbyrefreservation_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_usedbyrefreservation_value"></a>
<a id="ADDED_fields_usedbyrefreservation_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_usedbyrefreservation_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_usedbyrefreservation_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_usedbyrefreservation_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_usedbyrefreservation_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_usedbyrefreservation_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_usedbyrefreservation_source"></a>
<a id="ADDED_fields_usedbyrefreservation_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_usedbyrefreservation_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_usedbyrefreservation_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_usedbyrefreservation_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_usedbyrefreservation_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_usedbyrefreservation_source_anyOf_i1)

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

<a id="headingADDED_fields_usedbyrefreservation_source_info"></a>
<a id="ADDED_fields_usedbyrefreservation_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_usedbysnapshots"></a>
<a id="ADDED_fields_usedbysnapshots"></a>
##### usedbysnapshots

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by snapshots of this dataset.
- No Additional Properties
<a id="headingADDED_fields_usedbysnapshots_parsed"></a>
<a id="ADDED_fields_usedbysnapshots_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_usedbysnapshots_rawvalue"></a>
<a id="ADDED_fields_usedbysnapshots_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_usedbysnapshots_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_usedbysnapshots_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_usedbysnapshots_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_usedbysnapshots_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_usedbysnapshots_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_usedbysnapshots_value"></a>
<a id="ADDED_fields_usedbysnapshots_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_usedbysnapshots_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_usedbysnapshots_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_usedbysnapshots_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_usedbysnapshots_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_usedbysnapshots_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_usedbysnapshots_source"></a>
<a id="ADDED_fields_usedbysnapshots_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_usedbysnapshots_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_usedbysnapshots_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_usedbysnapshots_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_usedbysnapshots_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_usedbysnapshots_source_anyOf_i1)

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

<a id="headingADDED_fields_usedbysnapshots_source_info"></a>
<a id="ADDED_fields_usedbysnapshots_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_available"></a>
<a id="ADDED_fields_available"></a>
##### available

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space available to this dataset and its children.
- No Additional Properties
<a id="headingADDED_fields_available_parsed"></a>
<a id="ADDED_fields_available_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_available_rawvalue"></a>
<a id="ADDED_fields_available_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_available_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_available_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_available_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_available_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_available_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_available_value"></a>
<a id="ADDED_fields_available_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_available_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_available_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_available_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_available_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_available_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_available_source"></a>
<a id="ADDED_fields_available_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_available_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_available_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_available_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_available_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_available_source_anyOf_i1)

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

<a id="headingADDED_fields_available_source_info"></a>
<a id="ADDED_fields_available_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_special_small_block_size"></a>
<a id="ADDED_fields_special_small_block_size"></a>
##### special_small_block_size

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Size threshold below which blocks are stored on special vdevs if configured.
- No Additional Properties
<a id="headingADDED_fields_special_small_block_size_parsed"></a>
<a id="ADDED_fields_special_small_block_size_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_special_small_block_size_rawvalue"></a>
<a id="ADDED_fields_special_small_block_size_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_special_small_block_size_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_special_small_block_size_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_special_small_block_size_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_special_small_block_size_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_special_small_block_size_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_special_small_block_size_value"></a>
<a id="ADDED_fields_special_small_block_size_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_special_small_block_size_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_special_small_block_size_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_special_small_block_size_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_special_small_block_size_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_special_small_block_size_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_special_small_block_size_source"></a>
<a id="ADDED_fields_special_small_block_size_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_special_small_block_size_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_special_small_block_size_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_special_small_block_size_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_special_small_block_size_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_special_small_block_size_source_anyOf_i1)

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

<a id="headingADDED_fields_special_small_block_size_source_info"></a>
<a id="ADDED_fields_special_small_block_size_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_pbkdf2iters"></a>
<a id="ADDED_fields_pbkdf2iters"></a>
##### pbkdf2iters

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Number of PBKDF2 iterations used for passphrase-based encryption keys.
- No Additional Properties
<a id="headingADDED_fields_pbkdf2iters_parsed"></a>
<a id="ADDED_fields_pbkdf2iters_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_pbkdf2iters_rawvalue"></a>
<a id="ADDED_fields_pbkdf2iters_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_pbkdf2iters_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_pbkdf2iters_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_pbkdf2iters_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_pbkdf2iters_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_pbkdf2iters_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_pbkdf2iters_value"></a>
<a id="ADDED_fields_pbkdf2iters_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_pbkdf2iters_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_pbkdf2iters_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_pbkdf2iters_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_pbkdf2iters_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_pbkdf2iters_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_pbkdf2iters_source"></a>
<a id="ADDED_fields_pbkdf2iters_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_pbkdf2iters_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_pbkdf2iters_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_pbkdf2iters_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_pbkdf2iters_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_pbkdf2iters_source_anyOf_i1)

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

<a id="headingADDED_fields_pbkdf2iters_source_info"></a>
<a id="ADDED_fields_pbkdf2iters_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_creation"></a>
<a id="ADDED_fields_creation"></a>
##### creation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Timestamp when this dataset was created.
- No Additional Properties
<a id="headingADDED_fields_creation_parsed"></a>
<a id="ADDED_fields_creation_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_creation_rawvalue"></a>
<a id="ADDED_fields_creation_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_creation_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_creation_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_creation_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_creation_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_creation_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_creation_value"></a>
<a id="ADDED_fields_creation_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_creation_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_creation_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_creation_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_creation_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_creation_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_creation_source"></a>
<a id="ADDED_fields_creation_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_creation_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_creation_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_creation_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_creation_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_creation_source_anyOf_i1)

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

<a id="headingADDED_fields_creation_source_info"></a>
<a id="ADDED_fields_creation_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_snapdev"></a>
<a id="ADDED_fields_snapdev"></a>
##### snapdev

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Controls visibility of volume snapshots under /dev/zvol/<pool>/.
- No Additional Properties
<a id="headingADDED_fields_snapdev_parsed"></a>
<a id="ADDED_fields_snapdev_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_snapdev_rawvalue"></a>
<a id="ADDED_fields_snapdev_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="ADDED_fields_snapdev_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_snapdev_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_snapdev_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_snapdev_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_snapdev_rawvalue_anyOf_i1)

- Type: null

<a id="headingADDED_fields_snapdev_value"></a>
<a id="ADDED_fields_snapdev_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="ADDED_fields_snapdev_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_snapdev_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_snapdev_value_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_snapdev_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_snapdev_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_snapdev_source"></a>
<a id="ADDED_fields_snapdev_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="ADDED_fields_snapdev_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_snapdev_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_snapdev_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_snapdev_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_snapdev_source_anyOf_i1)

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

<a id="headingADDED_fields_snapdev_source_info"></a>
<a id="ADDED_fields_snapdev_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingADDED_fields_mountpoint"></a>
<a id="ADDED_fields_mountpoint"></a>
##### mountpoint

- Schema name: `Mountpoint`

Filesystem path where this dataset is mounted. Null for unmounted datasets or volumes.
<a id="ADDED_fields_mountpoint_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_mountpoint_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_mountpoint_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_mountpoint_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_mountpoint_anyOf_i1)

- Type: null

<a id="headingADDED_fields_additionalProperties"></a>
<a id="ADDED_fields_additionalProperties"></a>
##### Additional Properties

Additional Properties of any type are allowed.
- Type: object

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `PoolDatasetChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `PoolDatasetEntry`
- Type: object
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id

- Schema name: `Id`
- Type: string

The full dataset path including pool name.
Examples:

```json
"tank/dataset/child"
```

<a id="headingCHANGED_fields_type"></a>
<a id="CHANGED_fields_type"></a>
##### type

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

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name

- Schema name: `Name`
- Type: string

The dataset name without the pool prefix.

<a id="headingCHANGED_fields_pool"></a>
<a id="CHANGED_fields_pool"></a>
##### pool

- Schema name: `Pool`
- Type: string

The name of the ZFS pool containing this dataset.

<a id="headingCHANGED_fields_encrypted"></a>
<a id="CHANGED_fields_encrypted"></a>
##### encrypted

- Schema name: `Encrypted`
- Type: boolean

Whether the dataset is encrypted.

<a id="headingCHANGED_fields_encryption_root"></a>
<a id="CHANGED_fields_encryption_root"></a>
##### encryption_root

- Schema name: `Encryption Root`

The root dataset where encryption is enabled. `null` if the dataset is not encrypted.
<a id="CHANGED_fields_encryption_root_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_encryption_root_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_encryption_root_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_encryption_root_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_encryption_root_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_key_loaded"></a>
<a id="CHANGED_fields_key_loaded"></a>
##### key_loaded

- Schema name: `Key Loaded`

Whether the encryption key is currently loaded for encrypted datasets. `null` for unencrypted datasets.
<a id="CHANGED_fields_key_loaded_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_key_loaded_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_key_loaded_anyOf_i0)

- Type: boolean

<a id="tab-pane_CHANGED_fields_key_loaded_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_key_loaded_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_children"></a>
<a id="CHANGED_fields_children"></a>
##### children

- Schema name: `Children`
- Type: array

Array of child dataset objects nested under this dataset.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_children_items"></a>
- Type: object

<a id="headingCHANGED_fields_user_properties"></a>
<a id="CHANGED_fields_user_properties"></a>
##### user_properties

- Schema name: `PoolDatasetEntryUserProperties`
- Type: object

Custom user-defined ZFS properties set on this dataset as key-value pairs.
<a id="headingCHANGED_fields_user_properties_comments"></a>
<a id="CHANGED_fields_user_properties_comments"></a>
###### comments

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS comments property for storing descriptive text about the dataset.
- No Additional Properties
<a id="headingCHANGED_fields_user_properties_comments_parsed"></a>
<a id="CHANGED_fields_user_properties_comments_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_user_properties_comments_rawvalue"></a>
<a id="CHANGED_fields_user_properties_comments_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_user_properties_comments_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_user_properties_comments_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_user_properties_comments_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_user_properties_comments_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_user_properties_comments_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_user_properties_comments_value"></a>
<a id="CHANGED_fields_user_properties_comments_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_user_properties_comments_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_user_properties_comments_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_user_properties_comments_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_user_properties_comments_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_user_properties_comments_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_user_properties_comments_source"></a>
<a id="CHANGED_fields_user_properties_comments_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_user_properties_comments_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_user_properties_comments_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_user_properties_comments_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_user_properties_comments_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_user_properties_comments_source_anyOf_i1)

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

<a id="headingCHANGED_fields_user_properties_comments_source_info"></a>
<a id="CHANGED_fields_user_properties_comments_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_user_properties_quota_warning"></a>
<a id="CHANGED_fields_user_properties_quota_warning"></a>
###### quota_warning

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS quota warning threshold property as a percentage.
- No Additional Properties
<a id="headingCHANGED_fields_user_properties_quota_warning_parsed"></a>
<a id="CHANGED_fields_user_properties_quota_warning_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_user_properties_quota_warning_rawvalue"></a>
<a id="CHANGED_fields_user_properties_quota_warning_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_user_properties_quota_warning_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_user_properties_quota_warning_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_user_properties_quota_warning_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_user_properties_quota_warning_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_user_properties_quota_warning_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_user_properties_quota_warning_value"></a>
<a id="CHANGED_fields_user_properties_quota_warning_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_user_properties_quota_warning_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_user_properties_quota_warning_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_user_properties_quota_warning_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_user_properties_quota_warning_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_user_properties_quota_warning_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_user_properties_quota_warning_source"></a>
<a id="CHANGED_fields_user_properties_quota_warning_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_user_properties_quota_warning_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_user_properties_quota_warning_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_user_properties_quota_warning_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_user_properties_quota_warning_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_user_properties_quota_warning_source_anyOf_i1)

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

<a id="headingCHANGED_fields_user_properties_quota_warning_source_info"></a>
<a id="CHANGED_fields_user_properties_quota_warning_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_user_properties_quota_critical"></a>
<a id="CHANGED_fields_user_properties_quota_critical"></a>
###### quota_critical

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS quota critical threshold property as a percentage.
- No Additional Properties
<a id="headingCHANGED_fields_user_properties_quota_critical_parsed"></a>
<a id="CHANGED_fields_user_properties_quota_critical_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_user_properties_quota_critical_rawvalue"></a>
<a id="CHANGED_fields_user_properties_quota_critical_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_user_properties_quota_critical_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_user_properties_quota_critical_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_user_properties_quota_critical_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_user_properties_quota_critical_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_user_properties_quota_critical_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_user_properties_quota_critical_value"></a>
<a id="CHANGED_fields_user_properties_quota_critical_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_user_properties_quota_critical_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_user_properties_quota_critical_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_user_properties_quota_critical_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_user_properties_quota_critical_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_user_properties_quota_critical_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_user_properties_quota_critical_source"></a>
<a id="CHANGED_fields_user_properties_quota_critical_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_user_properties_quota_critical_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_user_properties_quota_critical_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_user_properties_quota_critical_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_user_properties_quota_critical_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_user_properties_quota_critical_source_anyOf_i1)

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

<a id="headingCHANGED_fields_user_properties_quota_critical_source_info"></a>
<a id="CHANGED_fields_user_properties_quota_critical_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_user_properties_refquota_warning"></a>
<a id="CHANGED_fields_user_properties_refquota_warning"></a>
###### refquota_warning

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS reference quota warning threshold property as a percentage.
- No Additional Properties
<a id="headingCHANGED_fields_user_properties_refquota_warning_parsed"></a>
<a id="CHANGED_fields_user_properties_refquota_warning_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_user_properties_refquota_warning_rawvalue"></a>
<a id="CHANGED_fields_user_properties_refquota_warning_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_user_properties_refquota_warning_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_user_properties_refquota_warning_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_user_properties_refquota_warning_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_user_properties_refquota_warning_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_user_properties_refquota_warning_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_user_properties_refquota_warning_value"></a>
<a id="CHANGED_fields_user_properties_refquota_warning_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_user_properties_refquota_warning_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_user_properties_refquota_warning_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_user_properties_refquota_warning_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_user_properties_refquota_warning_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_user_properties_refquota_warning_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_user_properties_refquota_warning_source"></a>
<a id="CHANGED_fields_user_properties_refquota_warning_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_user_properties_refquota_warning_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_user_properties_refquota_warning_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_user_properties_refquota_warning_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_user_properties_refquota_warning_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_user_properties_refquota_warning_source_anyOf_i1)

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

<a id="headingCHANGED_fields_user_properties_refquota_warning_source_info"></a>
<a id="CHANGED_fields_user_properties_refquota_warning_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_user_properties_refquota_critical"></a>
<a id="CHANGED_fields_user_properties_refquota_critical"></a>
###### refquota_critical

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS reference quota critical threshold property as a percentage.
- No Additional Properties
<a id="headingCHANGED_fields_user_properties_refquota_critical_parsed"></a>
<a id="CHANGED_fields_user_properties_refquota_critical_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_user_properties_refquota_critical_rawvalue"></a>
<a id="CHANGED_fields_user_properties_refquota_critical_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_user_properties_refquota_critical_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_user_properties_refquota_critical_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_user_properties_refquota_critical_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_user_properties_refquota_critical_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_user_properties_refquota_critical_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_user_properties_refquota_critical_value"></a>
<a id="CHANGED_fields_user_properties_refquota_critical_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_user_properties_refquota_critical_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_user_properties_refquota_critical_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_user_properties_refquota_critical_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_user_properties_refquota_critical_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_user_properties_refquota_critical_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_user_properties_refquota_critical_source"></a>
<a id="CHANGED_fields_user_properties_refquota_critical_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_user_properties_refquota_critical_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_user_properties_refquota_critical_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_user_properties_refquota_critical_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_user_properties_refquota_critical_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_user_properties_refquota_critical_source_anyOf_i1)

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

<a id="headingCHANGED_fields_user_properties_refquota_critical_source_info"></a>
<a id="CHANGED_fields_user_properties_refquota_critical_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_user_properties_managedby"></a>
<a id="CHANGED_fields_user_properties_managedby"></a>
###### managedby

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Identifies which service or system manages this dataset.
- No Additional Properties
<a id="headingCHANGED_fields_user_properties_managedby_parsed"></a>
<a id="CHANGED_fields_user_properties_managedby_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_user_properties_managedby_rawvalue"></a>
<a id="CHANGED_fields_user_properties_managedby_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_user_properties_managedby_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_user_properties_managedby_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_user_properties_managedby_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_user_properties_managedby_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_user_properties_managedby_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_user_properties_managedby_value"></a>
<a id="CHANGED_fields_user_properties_managedby_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_user_properties_managedby_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_user_properties_managedby_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_user_properties_managedby_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_user_properties_managedby_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_user_properties_managedby_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_user_properties_managedby_source"></a>
<a id="CHANGED_fields_user_properties_managedby_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_user_properties_managedby_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_user_properties_managedby_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_user_properties_managedby_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_user_properties_managedby_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_user_properties_managedby_source_anyOf_i1)

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

<a id="headingCHANGED_fields_user_properties_managedby_source_info"></a>
<a id="CHANGED_fields_user_properties_managedby_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_user_properties_additionalProperties"></a>
<a id="CHANGED_fields_user_properties_additionalProperties"></a>
###### Additional Properties

Additional Properties of any type are allowed.
- Type: object

<a id="headingCHANGED_fields_locked"></a>
<a id="CHANGED_fields_locked"></a>
##### locked

- Schema name: `Locked`
- Type: boolean

Whether an encrypted dataset is currently locked (key not loaded).

<a id="headingCHANGED_fields_tier"></a>
<a id="CHANGED_fields_tier"></a>
##### tier

Performance tier. `null` if tiering disabled, if underlying pool does not support tiering, or if deduplication is enabled on the dataset.
<a id="CHANGED_fields_tier_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_tier_anyOf_i0"></a>
###### [TierInfo](#tab-pane_CHANGED_fields_tier_anyOf_i0)

- Schema name: `TierInfo`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_tier_anyOf_i0_tier_type"></a>
<a id="CHANGED_fields_tier_anyOf_i0_tier_type"></a>
###### tier_type (required)

- Schema name: `Tier Type`
- Type: enum (of string)

Storage performance tier for this share.
###### Must be one of:

- "REGULAR"
- "PERFORMANCE"

<a id="headingCHANGED_fields_tier_anyOf_i0_tier_job"></a>
<a id="CHANGED_fields_tier_anyOf_i0_tier_job"></a>
###### tier_job

- Default: null

Most recent rewrite job for this share's dataset, or `null` if no job history exists.
<a id="CHANGED_fields_tier_anyOf_i0_tier_job_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0"></a>
###### [ZfsTierRewriteJobEntry](#tab-pane_CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0)

- Schema name: `ZfsTierRewriteJobEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
<a id="CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
###### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
<a id="CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
###### dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
<a id="CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
###### job_uuid (required)

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
<a id="CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
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

<a id="tab-pane_CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i1)

- Type: null

<a id="tab-pane_CHANGED_fields_tier_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_tier_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_deduplication"></a>
<a id="CHANGED_fields_deduplication"></a>
##### deduplication

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS deduplication setting - whether identical data blocks are stored only once.
- No Additional Properties
<a id="headingCHANGED_fields_deduplication_parsed"></a>
<a id="CHANGED_fields_deduplication_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_deduplication_rawvalue"></a>
<a id="CHANGED_fields_deduplication_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_deduplication_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_deduplication_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_deduplication_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_deduplication_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_deduplication_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_deduplication_value"></a>
<a id="CHANGED_fields_deduplication_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_deduplication_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_deduplication_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_deduplication_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_deduplication_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_deduplication_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_deduplication_source"></a>
<a id="CHANGED_fields_deduplication_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_deduplication_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_deduplication_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_deduplication_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_deduplication_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_deduplication_source_anyOf_i1)

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

<a id="headingCHANGED_fields_deduplication_source_info"></a>
<a id="CHANGED_fields_deduplication_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_aclmode"></a>
<a id="CHANGED_fields_aclmode"></a>
##### aclmode

- Schema name: `PoolDatasetEntryProperty`
- Type: object

How Access Control Lists (ACLs) are handled when chmod is used.
- No Additional Properties
<a id="headingCHANGED_fields_aclmode_parsed"></a>
<a id="CHANGED_fields_aclmode_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_aclmode_rawvalue"></a>
<a id="CHANGED_fields_aclmode_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_aclmode_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_aclmode_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_aclmode_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_aclmode_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_aclmode_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_aclmode_value"></a>
<a id="CHANGED_fields_aclmode_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_aclmode_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_aclmode_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_aclmode_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_aclmode_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_aclmode_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_aclmode_source"></a>
<a id="CHANGED_fields_aclmode_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_aclmode_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_aclmode_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_aclmode_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_aclmode_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_aclmode_source_anyOf_i1)

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

<a id="headingCHANGED_fields_aclmode_source_info"></a>
<a id="CHANGED_fields_aclmode_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_acltype"></a>
<a id="CHANGED_fields_acltype"></a>
##### acltype

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The type of Access Control List system used (NFSV4, POSIX, or OFF).
- No Additional Properties
<a id="headingCHANGED_fields_acltype_parsed"></a>
<a id="CHANGED_fields_acltype_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_acltype_rawvalue"></a>
<a id="CHANGED_fields_acltype_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_acltype_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_acltype_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_acltype_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_acltype_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_acltype_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_acltype_value"></a>
<a id="CHANGED_fields_acltype_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_acltype_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_acltype_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_acltype_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_acltype_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_acltype_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_acltype_source"></a>
<a id="CHANGED_fields_acltype_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_acltype_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_acltype_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_acltype_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_acltype_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_acltype_source_anyOf_i1)

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

<a id="headingCHANGED_fields_acltype_source_info"></a>
<a id="CHANGED_fields_acltype_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_xattr"></a>
<a id="CHANGED_fields_xattr"></a>
##### xattr

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Extended attributes storage method (on/off).
- No Additional Properties
<a id="headingCHANGED_fields_xattr_parsed"></a>
<a id="CHANGED_fields_xattr_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_xattr_rawvalue"></a>
<a id="CHANGED_fields_xattr_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_xattr_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_xattr_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_xattr_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_xattr_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_xattr_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_xattr_value"></a>
<a id="CHANGED_fields_xattr_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_xattr_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_xattr_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_xattr_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_xattr_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_xattr_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_xattr_source"></a>
<a id="CHANGED_fields_xattr_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_xattr_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_xattr_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_xattr_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_xattr_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_xattr_source_anyOf_i1)

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

<a id="headingCHANGED_fields_xattr_source_info"></a>
<a id="CHANGED_fields_xattr_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_atime"></a>
<a id="CHANGED_fields_atime"></a>
##### atime

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Whether file access times are updated when files are accessed.
- No Additional Properties
<a id="headingCHANGED_fields_atime_parsed"></a>
<a id="CHANGED_fields_atime_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_atime_rawvalue"></a>
<a id="CHANGED_fields_atime_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_atime_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_atime_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_atime_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_atime_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_atime_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_atime_value"></a>
<a id="CHANGED_fields_atime_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_atime_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_atime_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_atime_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_atime_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_atime_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_atime_source"></a>
<a id="CHANGED_fields_atime_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_atime_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_atime_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_atime_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_atime_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_atime_source_anyOf_i1)

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

<a id="headingCHANGED_fields_atime_source_info"></a>
<a id="CHANGED_fields_atime_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_casesensitivity"></a>
<a id="CHANGED_fields_casesensitivity"></a>
##### casesensitivity

- Schema name: `PoolDatasetEntryProperty`
- Type: object

File name case sensitivity setting (sensitive/insensitive).
- No Additional Properties
<a id="headingCHANGED_fields_casesensitivity_parsed"></a>
<a id="CHANGED_fields_casesensitivity_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_casesensitivity_rawvalue"></a>
<a id="CHANGED_fields_casesensitivity_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_casesensitivity_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_casesensitivity_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_casesensitivity_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_casesensitivity_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_casesensitivity_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_casesensitivity_value"></a>
<a id="CHANGED_fields_casesensitivity_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_casesensitivity_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_casesensitivity_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_casesensitivity_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_casesensitivity_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_casesensitivity_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_casesensitivity_source"></a>
<a id="CHANGED_fields_casesensitivity_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_casesensitivity_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_casesensitivity_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_casesensitivity_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_casesensitivity_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_casesensitivity_source_anyOf_i1)

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

<a id="headingCHANGED_fields_casesensitivity_source_info"></a>
<a id="CHANGED_fields_casesensitivity_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_checksum"></a>
<a id="CHANGED_fields_checksum"></a>
##### checksum

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Data integrity checksum algorithm used for this dataset.
- No Additional Properties
<a id="headingCHANGED_fields_checksum_parsed"></a>
<a id="CHANGED_fields_checksum_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_checksum_rawvalue"></a>
<a id="CHANGED_fields_checksum_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_checksum_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_checksum_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_checksum_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_checksum_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_checksum_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_checksum_value"></a>
<a id="CHANGED_fields_checksum_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_checksum_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_checksum_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_checksum_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_checksum_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_checksum_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_checksum_source"></a>
<a id="CHANGED_fields_checksum_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_checksum_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_checksum_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_checksum_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_checksum_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_checksum_source_anyOf_i1)

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

<a id="headingCHANGED_fields_checksum_source_info"></a>
<a id="CHANGED_fields_checksum_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_exec"></a>
<a id="CHANGED_fields_exec"></a>
##### exec

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Whether files in this dataset can be executed.
- No Additional Properties
<a id="headingCHANGED_fields_exec_parsed"></a>
<a id="CHANGED_fields_exec_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_exec_rawvalue"></a>
<a id="CHANGED_fields_exec_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_exec_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_exec_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_exec_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_exec_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_exec_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_exec_value"></a>
<a id="CHANGED_fields_exec_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_exec_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_exec_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_exec_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_exec_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_exec_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_exec_source"></a>
<a id="CHANGED_fields_exec_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_exec_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_exec_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_exec_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_exec_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_exec_source_anyOf_i1)

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

<a id="headingCHANGED_fields_exec_source_info"></a>
<a id="CHANGED_fields_exec_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_sync"></a>
<a id="CHANGED_fields_sync"></a>
##### sync

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Synchronous write behavior (standard/always/disabled).
- No Additional Properties
<a id="headingCHANGED_fields_sync_parsed"></a>
<a id="CHANGED_fields_sync_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_sync_rawvalue"></a>
<a id="CHANGED_fields_sync_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_sync_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_sync_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_sync_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_sync_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_sync_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_sync_value"></a>
<a id="CHANGED_fields_sync_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_sync_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_sync_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_sync_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_sync_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_sync_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_sync_source"></a>
<a id="CHANGED_fields_sync_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_sync_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_sync_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_sync_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_sync_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_sync_source_anyOf_i1)

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

<a id="headingCHANGED_fields_sync_source_info"></a>
<a id="CHANGED_fields_sync_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_compression"></a>
<a id="CHANGED_fields_compression"></a>
##### compression

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Compression algorithm and level applied to data in this dataset.
- No Additional Properties
<a id="headingCHANGED_fields_compression_parsed"></a>
<a id="CHANGED_fields_compression_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_compression_rawvalue"></a>
<a id="CHANGED_fields_compression_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_compression_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_compression_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_compression_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_compression_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_compression_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_compression_value"></a>
<a id="CHANGED_fields_compression_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_compression_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_compression_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_compression_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_compression_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_compression_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_compression_source"></a>
<a id="CHANGED_fields_compression_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_compression_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_compression_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_compression_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_compression_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_compression_source_anyOf_i1)

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

<a id="headingCHANGED_fields_compression_source_info"></a>
<a id="CHANGED_fields_compression_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_compressratio"></a>
<a id="CHANGED_fields_compressratio"></a>
##### compressratio

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The achieved compression ratio as a decimal (e.g., '2.50x').
- No Additional Properties
<a id="headingCHANGED_fields_compressratio_parsed"></a>
<a id="CHANGED_fields_compressratio_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_compressratio_rawvalue"></a>
<a id="CHANGED_fields_compressratio_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_compressratio_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_compressratio_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_compressratio_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_compressratio_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_compressratio_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_compressratio_value"></a>
<a id="CHANGED_fields_compressratio_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_compressratio_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_compressratio_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_compressratio_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_compressratio_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_compressratio_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_compressratio_source"></a>
<a id="CHANGED_fields_compressratio_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_compressratio_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_compressratio_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_compressratio_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_compressratio_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_compressratio_source_anyOf_i1)

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

<a id="headingCHANGED_fields_compressratio_source_info"></a>
<a id="CHANGED_fields_compressratio_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_origin"></a>
<a id="CHANGED_fields_origin"></a>
##### origin

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The snapshot from which this clone was created. Empty for non-clone datasets.
- No Additional Properties
<a id="headingCHANGED_fields_origin_parsed"></a>
<a id="CHANGED_fields_origin_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_origin_rawvalue"></a>
<a id="CHANGED_fields_origin_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_origin_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_origin_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_origin_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_origin_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_origin_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_origin_value"></a>
<a id="CHANGED_fields_origin_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_origin_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_origin_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_origin_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_origin_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_origin_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_origin_source"></a>
<a id="CHANGED_fields_origin_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_origin_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_origin_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_origin_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_origin_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_origin_source_anyOf_i1)

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

<a id="headingCHANGED_fields_origin_source_info"></a>
<a id="CHANGED_fields_origin_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_quota"></a>
<a id="CHANGED_fields_quota"></a>
##### quota

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Maximum amount of disk space this dataset and its children can consume.
- No Additional Properties
<a id="headingCHANGED_fields_quota_parsed"></a>
<a id="CHANGED_fields_quota_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_quota_rawvalue"></a>
<a id="CHANGED_fields_quota_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_quota_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_quota_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_quota_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_quota_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_quota_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_quota_value"></a>
<a id="CHANGED_fields_quota_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_quota_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_quota_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_quota_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_quota_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_quota_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_quota_source"></a>
<a id="CHANGED_fields_quota_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_quota_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_quota_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_quota_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_quota_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_quota_source_anyOf_i1)

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

<a id="headingCHANGED_fields_quota_source_info"></a>
<a id="CHANGED_fields_quota_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_refquota"></a>
<a id="CHANGED_fields_refquota"></a>
##### refquota

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Maximum amount of disk space this dataset itself can consume (excluding children).
- No Additional Properties
<a id="headingCHANGED_fields_refquota_parsed"></a>
<a id="CHANGED_fields_refquota_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_refquota_rawvalue"></a>
<a id="CHANGED_fields_refquota_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_refquota_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_refquota_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_refquota_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_refquota_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_refquota_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_refquota_value"></a>
<a id="CHANGED_fields_refquota_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_refquota_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_refquota_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_refquota_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_refquota_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_refquota_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_refquota_source"></a>
<a id="CHANGED_fields_refquota_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_refquota_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_refquota_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_refquota_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_refquota_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_refquota_source_anyOf_i1)

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

<a id="headingCHANGED_fields_refquota_source_info"></a>
<a id="CHANGED_fields_refquota_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_reservation"></a>
<a id="CHANGED_fields_reservation"></a>
##### reservation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Minimum amount of disk space guaranteed to be available to this dataset and its children.
- No Additional Properties
<a id="headingCHANGED_fields_reservation_parsed"></a>
<a id="CHANGED_fields_reservation_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_reservation_rawvalue"></a>
<a id="CHANGED_fields_reservation_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_reservation_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_reservation_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_reservation_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_reservation_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_reservation_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_reservation_value"></a>
<a id="CHANGED_fields_reservation_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_reservation_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_reservation_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_reservation_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_reservation_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_reservation_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_reservation_source"></a>
<a id="CHANGED_fields_reservation_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_reservation_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_reservation_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_reservation_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_reservation_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_reservation_source_anyOf_i1)

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

<a id="headingCHANGED_fields_reservation_source_info"></a>
<a id="CHANGED_fields_reservation_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_refreservation"></a>
<a id="CHANGED_fields_refreservation"></a>
##### refreservation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Minimum amount of disk space guaranteed to be available to this dataset itself.
- No Additional Properties
<a id="headingCHANGED_fields_refreservation_parsed"></a>
<a id="CHANGED_fields_refreservation_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_refreservation_rawvalue"></a>
<a id="CHANGED_fields_refreservation_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_refreservation_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_refreservation_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_refreservation_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_refreservation_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_refreservation_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_refreservation_value"></a>
<a id="CHANGED_fields_refreservation_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_refreservation_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_refreservation_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_refreservation_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_refreservation_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_refreservation_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_refreservation_source"></a>
<a id="CHANGED_fields_refreservation_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_refreservation_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_refreservation_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_refreservation_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_refreservation_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_refreservation_source_anyOf_i1)

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

<a id="headingCHANGED_fields_refreservation_source_info"></a>
<a id="CHANGED_fields_refreservation_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_copies"></a>
<a id="CHANGED_fields_copies"></a>
##### copies

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Number of copies of data blocks to maintain for redundancy (1-3).
- No Additional Properties
<a id="headingCHANGED_fields_copies_parsed"></a>
<a id="CHANGED_fields_copies_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_copies_rawvalue"></a>
<a id="CHANGED_fields_copies_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_copies_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_copies_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_copies_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_copies_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_copies_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_copies_value"></a>
<a id="CHANGED_fields_copies_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_copies_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_copies_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_copies_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_copies_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_copies_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_copies_source"></a>
<a id="CHANGED_fields_copies_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_copies_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_copies_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_copies_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_copies_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_copies_source_anyOf_i1)

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

<a id="headingCHANGED_fields_copies_source_info"></a>
<a id="CHANGED_fields_copies_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_snapdir"></a>
<a id="CHANGED_fields_snapdir"></a>
##### snapdir

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Visibility of the .zfs/snapshot directory (visible/hidden).
- No Additional Properties
<a id="headingCHANGED_fields_snapdir_parsed"></a>
<a id="CHANGED_fields_snapdir_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_snapdir_rawvalue"></a>
<a id="CHANGED_fields_snapdir_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_snapdir_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_snapdir_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_snapdir_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_snapdir_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_snapdir_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_snapdir_value"></a>
<a id="CHANGED_fields_snapdir_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_snapdir_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_snapdir_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_snapdir_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_snapdir_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_snapdir_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_snapdir_source"></a>
<a id="CHANGED_fields_snapdir_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_snapdir_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_snapdir_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_snapdir_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_snapdir_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_snapdir_source_anyOf_i1)

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

<a id="headingCHANGED_fields_snapdir_source_info"></a>
<a id="CHANGED_fields_snapdir_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_readonly"></a>
<a id="CHANGED_fields_readonly"></a>
##### readonly

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Whether the dataset is read-only.
- No Additional Properties
<a id="headingCHANGED_fields_readonly_parsed"></a>
<a id="CHANGED_fields_readonly_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_readonly_rawvalue"></a>
<a id="CHANGED_fields_readonly_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_readonly_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_readonly_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_readonly_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_readonly_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_readonly_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_readonly_value"></a>
<a id="CHANGED_fields_readonly_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_readonly_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_readonly_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_readonly_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_readonly_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_readonly_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_readonly_source"></a>
<a id="CHANGED_fields_readonly_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_readonly_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_readonly_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_readonly_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_readonly_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_readonly_source_anyOf_i1)

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

<a id="headingCHANGED_fields_readonly_source_info"></a>
<a id="CHANGED_fields_readonly_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_recordsize"></a>
<a id="CHANGED_fields_recordsize"></a>
##### recordsize

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The suggested block size for files in this filesystem dataset.
- No Additional Properties
<a id="headingCHANGED_fields_recordsize_parsed"></a>
<a id="CHANGED_fields_recordsize_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_recordsize_rawvalue"></a>
<a id="CHANGED_fields_recordsize_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_recordsize_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_recordsize_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_recordsize_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_recordsize_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_recordsize_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_recordsize_value"></a>
<a id="CHANGED_fields_recordsize_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_recordsize_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_recordsize_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_recordsize_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_recordsize_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_recordsize_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_recordsize_source"></a>
<a id="CHANGED_fields_recordsize_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_recordsize_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_recordsize_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_recordsize_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_recordsize_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_recordsize_source_anyOf_i1)

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

<a id="headingCHANGED_fields_recordsize_source_info"></a>
<a id="CHANGED_fields_recordsize_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_sparse"></a>
<a id="CHANGED_fields_sparse"></a>
##### sparse

- Schema name: `PoolDatasetEntryProperty`
- Type: object

For volumes, whether to use sparse (thin) provisioning.
- No Additional Properties
<a id="headingCHANGED_fields_sparse_parsed"></a>
<a id="CHANGED_fields_sparse_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_sparse_rawvalue"></a>
<a id="CHANGED_fields_sparse_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_sparse_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_sparse_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_sparse_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_sparse_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_sparse_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_sparse_value"></a>
<a id="CHANGED_fields_sparse_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_sparse_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_sparse_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_sparse_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_sparse_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_sparse_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_sparse_source"></a>
<a id="CHANGED_fields_sparse_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_sparse_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_sparse_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_sparse_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_sparse_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_sparse_source_anyOf_i1)

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

<a id="headingCHANGED_fields_sparse_source_info"></a>
<a id="CHANGED_fields_sparse_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_volsize"></a>
<a id="CHANGED_fields_volsize"></a>
##### volsize

- Schema name: `PoolDatasetEntryProperty`
- Type: object

For volumes, the logical size of the volume.
- No Additional Properties
<a id="headingCHANGED_fields_volsize_parsed"></a>
<a id="CHANGED_fields_volsize_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_volsize_rawvalue"></a>
<a id="CHANGED_fields_volsize_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_volsize_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_volsize_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_volsize_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_volsize_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_volsize_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_volsize_value"></a>
<a id="CHANGED_fields_volsize_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_volsize_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_volsize_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_volsize_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_volsize_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_volsize_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_volsize_source"></a>
<a id="CHANGED_fields_volsize_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_volsize_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_volsize_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_volsize_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_volsize_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_volsize_source_anyOf_i1)

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

<a id="headingCHANGED_fields_volsize_source_info"></a>
<a id="CHANGED_fields_volsize_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_volblocksize"></a>
<a id="CHANGED_fields_volblocksize"></a>
##### volblocksize

- Schema name: `PoolDatasetEntryProperty`
- Type: object

For volumes, the block size used by the volume.
- No Additional Properties
<a id="headingCHANGED_fields_volblocksize_parsed"></a>
<a id="CHANGED_fields_volblocksize_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_volblocksize_rawvalue"></a>
<a id="CHANGED_fields_volblocksize_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_volblocksize_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_volblocksize_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_volblocksize_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_volblocksize_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_volblocksize_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_volblocksize_value"></a>
<a id="CHANGED_fields_volblocksize_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_volblocksize_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_volblocksize_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_volblocksize_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_volblocksize_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_volblocksize_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_volblocksize_source"></a>
<a id="CHANGED_fields_volblocksize_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_volblocksize_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_volblocksize_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_volblocksize_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_volblocksize_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_volblocksize_source_anyOf_i1)

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

<a id="headingCHANGED_fields_volblocksize_source_info"></a>
<a id="CHANGED_fields_volblocksize_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_key_format"></a>
<a id="CHANGED_fields_key_format"></a>
##### key_format

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Format of the encryption key (hex/raw/passphrase). Only relevant for encrypted datasets.
- No Additional Properties
<a id="headingCHANGED_fields_key_format_parsed"></a>
<a id="CHANGED_fields_key_format_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_key_format_rawvalue"></a>
<a id="CHANGED_fields_key_format_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_key_format_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_key_format_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_key_format_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_key_format_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_key_format_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_key_format_value"></a>
<a id="CHANGED_fields_key_format_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_key_format_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_key_format_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_key_format_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_key_format_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_key_format_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_key_format_source"></a>
<a id="CHANGED_fields_key_format_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_key_format_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_key_format_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_key_format_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_key_format_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_key_format_source_anyOf_i1)

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

<a id="headingCHANGED_fields_key_format_source_info"></a>
<a id="CHANGED_fields_key_format_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_encryption_algorithm"></a>
<a id="CHANGED_fields_encryption_algorithm"></a>
##### encryption_algorithm

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Encryption algorithm used (e.g., AES-256-GCM). Only relevant for encrypted datasets.
- No Additional Properties
<a id="headingCHANGED_fields_encryption_algorithm_parsed"></a>
<a id="CHANGED_fields_encryption_algorithm_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_encryption_algorithm_rawvalue"></a>
<a id="CHANGED_fields_encryption_algorithm_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_encryption_algorithm_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_encryption_algorithm_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_encryption_algorithm_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_encryption_algorithm_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_encryption_algorithm_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_encryption_algorithm_value"></a>
<a id="CHANGED_fields_encryption_algorithm_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_encryption_algorithm_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_encryption_algorithm_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_encryption_algorithm_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_encryption_algorithm_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_encryption_algorithm_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_encryption_algorithm_source"></a>
<a id="CHANGED_fields_encryption_algorithm_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_encryption_algorithm_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_encryption_algorithm_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_encryption_algorithm_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_encryption_algorithm_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_encryption_algorithm_source_anyOf_i1)

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

<a id="headingCHANGED_fields_encryption_algorithm_source_info"></a>
<a id="CHANGED_fields_encryption_algorithm_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_used"></a>
<a id="CHANGED_fields_used"></a>
##### used

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Total amount of disk space consumed by this dataset and all its children.
- No Additional Properties
<a id="headingCHANGED_fields_used_parsed"></a>
<a id="CHANGED_fields_used_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_used_rawvalue"></a>
<a id="CHANGED_fields_used_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_used_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_used_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_used_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_used_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_used_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_used_value"></a>
<a id="CHANGED_fields_used_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_used_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_used_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_used_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_used_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_used_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_used_source"></a>
<a id="CHANGED_fields_used_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_used_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_used_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_used_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_used_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_used_source_anyOf_i1)

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

<a id="headingCHANGED_fields_used_source_info"></a>
<a id="CHANGED_fields_used_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_usedbychildren"></a>
<a id="CHANGED_fields_usedbychildren"></a>
##### usedbychildren

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by child datasets.
- No Additional Properties
<a id="headingCHANGED_fields_usedbychildren_parsed"></a>
<a id="CHANGED_fields_usedbychildren_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_usedbychildren_rawvalue"></a>
<a id="CHANGED_fields_usedbychildren_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_usedbychildren_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_usedbychildren_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_usedbychildren_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_usedbychildren_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_usedbychildren_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_usedbychildren_value"></a>
<a id="CHANGED_fields_usedbychildren_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_usedbychildren_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_usedbychildren_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_usedbychildren_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_usedbychildren_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_usedbychildren_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_usedbychildren_source"></a>
<a id="CHANGED_fields_usedbychildren_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_usedbychildren_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_usedbychildren_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_usedbychildren_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_usedbychildren_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_usedbychildren_source_anyOf_i1)

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

<a id="headingCHANGED_fields_usedbychildren_source_info"></a>
<a id="CHANGED_fields_usedbychildren_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_usedbydataset"></a>
<a id="CHANGED_fields_usedbydataset"></a>
##### usedbydataset

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by this dataset itself, excluding children and snapshots.
- No Additional Properties
<a id="headingCHANGED_fields_usedbydataset_parsed"></a>
<a id="CHANGED_fields_usedbydataset_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_usedbydataset_rawvalue"></a>
<a id="CHANGED_fields_usedbydataset_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_usedbydataset_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_usedbydataset_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_usedbydataset_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_usedbydataset_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_usedbydataset_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_usedbydataset_value"></a>
<a id="CHANGED_fields_usedbydataset_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_usedbydataset_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_usedbydataset_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_usedbydataset_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_usedbydataset_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_usedbydataset_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_usedbydataset_source"></a>
<a id="CHANGED_fields_usedbydataset_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_usedbydataset_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_usedbydataset_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_usedbydataset_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_usedbydataset_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_usedbydataset_source_anyOf_i1)

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

<a id="headingCHANGED_fields_usedbydataset_source_info"></a>
<a id="CHANGED_fields_usedbydataset_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_usedbyrefreservation"></a>
<a id="CHANGED_fields_usedbyrefreservation"></a>
##### usedbyrefreservation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by the refreservation of this dataset.
- No Additional Properties
<a id="headingCHANGED_fields_usedbyrefreservation_parsed"></a>
<a id="CHANGED_fields_usedbyrefreservation_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_usedbyrefreservation_rawvalue"></a>
<a id="CHANGED_fields_usedbyrefreservation_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_usedbyrefreservation_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_usedbyrefreservation_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_usedbyrefreservation_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_usedbyrefreservation_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_usedbyrefreservation_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_usedbyrefreservation_value"></a>
<a id="CHANGED_fields_usedbyrefreservation_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_usedbyrefreservation_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_usedbyrefreservation_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_usedbyrefreservation_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_usedbyrefreservation_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_usedbyrefreservation_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_usedbyrefreservation_source"></a>
<a id="CHANGED_fields_usedbyrefreservation_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_usedbyrefreservation_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_usedbyrefreservation_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_usedbyrefreservation_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_usedbyrefreservation_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_usedbyrefreservation_source_anyOf_i1)

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

<a id="headingCHANGED_fields_usedbyrefreservation_source_info"></a>
<a id="CHANGED_fields_usedbyrefreservation_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_usedbysnapshots"></a>
<a id="CHANGED_fields_usedbysnapshots"></a>
##### usedbysnapshots

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by snapshots of this dataset.
- No Additional Properties
<a id="headingCHANGED_fields_usedbysnapshots_parsed"></a>
<a id="CHANGED_fields_usedbysnapshots_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_usedbysnapshots_rawvalue"></a>
<a id="CHANGED_fields_usedbysnapshots_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_usedbysnapshots_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_usedbysnapshots_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_usedbysnapshots_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_usedbysnapshots_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_usedbysnapshots_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_usedbysnapshots_value"></a>
<a id="CHANGED_fields_usedbysnapshots_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_usedbysnapshots_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_usedbysnapshots_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_usedbysnapshots_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_usedbysnapshots_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_usedbysnapshots_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_usedbysnapshots_source"></a>
<a id="CHANGED_fields_usedbysnapshots_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_usedbysnapshots_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_usedbysnapshots_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_usedbysnapshots_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_usedbysnapshots_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_usedbysnapshots_source_anyOf_i1)

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

<a id="headingCHANGED_fields_usedbysnapshots_source_info"></a>
<a id="CHANGED_fields_usedbysnapshots_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_available"></a>
<a id="CHANGED_fields_available"></a>
##### available

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space available to this dataset and its children.
- No Additional Properties
<a id="headingCHANGED_fields_available_parsed"></a>
<a id="CHANGED_fields_available_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_available_rawvalue"></a>
<a id="CHANGED_fields_available_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_available_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_available_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_available_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_available_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_available_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_available_value"></a>
<a id="CHANGED_fields_available_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_available_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_available_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_available_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_available_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_available_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_available_source"></a>
<a id="CHANGED_fields_available_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_available_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_available_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_available_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_available_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_available_source_anyOf_i1)

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

<a id="headingCHANGED_fields_available_source_info"></a>
<a id="CHANGED_fields_available_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_special_small_block_size"></a>
<a id="CHANGED_fields_special_small_block_size"></a>
##### special_small_block_size

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Size threshold below which blocks are stored on special vdevs if configured.
- No Additional Properties
<a id="headingCHANGED_fields_special_small_block_size_parsed"></a>
<a id="CHANGED_fields_special_small_block_size_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_special_small_block_size_rawvalue"></a>
<a id="CHANGED_fields_special_small_block_size_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_special_small_block_size_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_special_small_block_size_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_special_small_block_size_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_special_small_block_size_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_special_small_block_size_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_special_small_block_size_value"></a>
<a id="CHANGED_fields_special_small_block_size_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_special_small_block_size_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_special_small_block_size_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_special_small_block_size_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_special_small_block_size_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_special_small_block_size_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_special_small_block_size_source"></a>
<a id="CHANGED_fields_special_small_block_size_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_special_small_block_size_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_special_small_block_size_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_special_small_block_size_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_special_small_block_size_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_special_small_block_size_source_anyOf_i1)

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

<a id="headingCHANGED_fields_special_small_block_size_source_info"></a>
<a id="CHANGED_fields_special_small_block_size_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_pbkdf2iters"></a>
<a id="CHANGED_fields_pbkdf2iters"></a>
##### pbkdf2iters

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Number of PBKDF2 iterations used for passphrase-based encryption keys.
- No Additional Properties
<a id="headingCHANGED_fields_pbkdf2iters_parsed"></a>
<a id="CHANGED_fields_pbkdf2iters_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_pbkdf2iters_rawvalue"></a>
<a id="CHANGED_fields_pbkdf2iters_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_pbkdf2iters_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_pbkdf2iters_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_pbkdf2iters_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_pbkdf2iters_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_pbkdf2iters_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_pbkdf2iters_value"></a>
<a id="CHANGED_fields_pbkdf2iters_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_pbkdf2iters_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_pbkdf2iters_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_pbkdf2iters_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_pbkdf2iters_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_pbkdf2iters_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_pbkdf2iters_source"></a>
<a id="CHANGED_fields_pbkdf2iters_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_pbkdf2iters_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_pbkdf2iters_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_pbkdf2iters_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_pbkdf2iters_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_pbkdf2iters_source_anyOf_i1)

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

<a id="headingCHANGED_fields_pbkdf2iters_source_info"></a>
<a id="CHANGED_fields_pbkdf2iters_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_creation"></a>
<a id="CHANGED_fields_creation"></a>
##### creation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Timestamp when this dataset was created.
- No Additional Properties
<a id="headingCHANGED_fields_creation_parsed"></a>
<a id="CHANGED_fields_creation_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_creation_rawvalue"></a>
<a id="CHANGED_fields_creation_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_creation_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_creation_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_creation_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_creation_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_creation_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_creation_value"></a>
<a id="CHANGED_fields_creation_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_creation_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_creation_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_creation_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_creation_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_creation_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_creation_source"></a>
<a id="CHANGED_fields_creation_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_creation_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_creation_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_creation_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_creation_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_creation_source_anyOf_i1)

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

<a id="headingCHANGED_fields_creation_source_info"></a>
<a id="CHANGED_fields_creation_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_snapdev"></a>
<a id="CHANGED_fields_snapdev"></a>
##### snapdev

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Controls visibility of volume snapshots under /dev/zvol/<pool>/.
- No Additional Properties
<a id="headingCHANGED_fields_snapdev_parsed"></a>
<a id="CHANGED_fields_snapdev_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_snapdev_rawvalue"></a>
<a id="CHANGED_fields_snapdev_rawvalue"></a>
###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="CHANGED_fields_snapdev_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_snapdev_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_snapdev_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_snapdev_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_snapdev_rawvalue_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_snapdev_value"></a>
<a id="CHANGED_fields_snapdev_value"></a>
###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="CHANGED_fields_snapdev_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_snapdev_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_snapdev_value_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_snapdev_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_snapdev_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_snapdev_source"></a>
<a id="CHANGED_fields_snapdev_source"></a>
###### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="CHANGED_fields_snapdev_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_snapdev_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_snapdev_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_snapdev_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_snapdev_source_anyOf_i1)

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

<a id="headingCHANGED_fields_snapdev_source_info"></a>
<a id="CHANGED_fields_snapdev_source_info"></a>
###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingCHANGED_fields_mountpoint"></a>
<a id="CHANGED_fields_mountpoint"></a>
##### mountpoint

- Schema name: `Mountpoint`

Filesystem path where this dataset is mounted. Null for unmounted datasets or volumes.
<a id="CHANGED_fields_mountpoint_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_mountpoint_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_mountpoint_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_mountpoint_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_mountpoint_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_additionalProperties"></a>
<a id="CHANGED_fields_additionalProperties"></a>
##### Additional Properties

Additional Properties of any type are allowed.
- Type: object

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `PoolDatasetRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
