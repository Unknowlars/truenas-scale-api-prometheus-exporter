---
title: pool.dataset.query
kind: method
source_rst: _sources/api_methods_pool.dataset.query.rst.txt
source_html: api_methods_pool.dataset.query.html
required_roles:
  - DATASET_READ
---

# pool.dataset.query

## Summary

Query Pool Datasets with `query-filters` and `query-options`.

We provide two ways to retrieve datasets. The first is a flat structure (default), where all datasets in the system are returned as separate objects which contain all data there is for their children. This retrieval type is slightly slower because of duplicates in each object. The second type is hierarchical, where only top level datasets are returned in the list. They contain all the children in the `children` key. This retrieval type is slightly faster. These options are controlled by the `query-options.extra.flat` attribute (default true).

In some cases it might be desirable to only retrieve details of a dataset itself and not it's children, in this case `query-options.extra.retrieve_children` should be explicitly specified and set to `false` which will result in children not being retrieved.

In case only some properties are desired to be retrieved for datasets, consumer should specify `query-options.extra.properties` which when `null` ( which is the default ) will retrieve all properties and otherwise a list can be specified like `["type", "used", "available"]` to retrieve selective properties. If no properties are desired, in that case an empty list should be sent. It should be noted that specifying empty list will still retrieve user properties. If user properties are not desired, in that case `query-options.extra.retrieve_user_props` should be set to `false`.

`query-options.extra.snapshots` can be set to retrieve snapshot(s) of dataset in question.

`query-options.extra.snapshots_recursive` can be set to retrieve snapshot(s) recursively of dataset in question. If `query-options.extra.snapshots_recursive` and `query-options.extra.snapshots` are set, snapshot(s) will be retrieved recursively.

`query-options.extra.snapshots_properties` can be specified to list out properties which should be retrieved for snapshot(s) related to each dataset. By default only name of the snapshot would be retrieved, however if `null` is specified all properties of the snapshot would be retrieved in this case.

## Required Roles

- `DATASET_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filters

#### filters

- Schema name: `filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

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
                [
                    "name",
                    "=",
                    "bob"
                ]
            ],
            [
                [
                    "name",
                    "=",
                    "larry"
                ]
            ]
        ]
    ]
]
```

#### Parameter 2: options

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
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: array
- No Additional Items

######### Each item of this array must be:

- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

### Return value

- Schema name: `Result`
#### Any of

##### Option 1

- Type: array of object
- No Additional Items

###### Each item of this array must be:

###### PoolDatasetQueryResultItem

- Schema name: `PoolDatasetQueryResultItem`
- Type: object
####### id

- Schema name: `Id`
- Type: string

The full dataset path including pool name.
Examples:

```json
"tank/dataset/child"
```

####### type

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

####### name

- Schema name: `Name`
- Type: string

The dataset name without the pool prefix.

####### pool

- Schema name: `Pool`
- Type: string

The name of the ZFS pool containing this dataset.

####### encrypted

- Schema name: `Encrypted`
- Type: boolean

Whether the dataset is encrypted.

####### encryption_root

- Schema name: `Encryption Root`

The root dataset where encryption is enabled. `null` if the dataset is not encrypted.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### key_loaded

- Schema name: `Key Loaded`

Whether the encryption key is currently loaded for encrypted datasets. `null` for unencrypted datasets.
######## Any of

######### Option 1

- Type: boolean

######### Option 2

- Type: null

####### children

- Schema name: `Children`
- Type: array

Array of child dataset objects nested under this dataset.
- No Additional Items

######## Each item of this array must be:

- Type: object

####### user_properties

- Schema name: `User Properties`
- Type: object

Custom user-defined ZFS properties set on this dataset as key-value pairs.

####### locked

- Schema name: `Locked`
- Type: boolean

Whether an encrypted dataset is currently locked (key not loaded).

####### comments

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS comments property for storing descriptive text about the dataset.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### quota_warning

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS quota warning threshold property as a percentage.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### quota_critical

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS quota critical threshold property as a percentage.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### refquota_warning

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS reference quota warning threshold property as a percentage.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### refquota_critical

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS reference quota critical threshold property as a percentage.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### managedby

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Identifies which service or system manages this dataset.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### deduplication

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS deduplication setting - whether identical data blocks are stored only once.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### aclmode

- Schema name: `PoolDatasetEntryProperty`
- Type: object

How Access Control Lists (ACLs) are handled when chmod is used.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### acltype

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The type of Access Control List system used (NFSV4, POSIX, or OFF).
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### xattr

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Extended attributes storage method (on/off).
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### atime

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Whether file access times are updated when files are accessed.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### casesensitivity

- Schema name: `PoolDatasetEntryProperty`
- Type: object

File name case sensitivity setting (sensitive/insensitive).
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### checksum

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Data integrity checksum algorithm used for this dataset.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### exec

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Whether files in this dataset can be executed.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### sync

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Synchronous write behavior (standard/always/disabled).
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### compression

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Compression algorithm and level applied to data in this dataset.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### compressratio

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The achieved compression ratio as a decimal (e.g., '2.50x').
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### origin

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The snapshot from which this clone was created. Empty for non-clone datasets.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### quota

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Maximum amount of disk space this dataset and its children can consume.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### refquota

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Maximum amount of disk space this dataset itself can consume (excluding children).
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### reservation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Minimum amount of disk space guaranteed to be available to this dataset and its children.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### refreservation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Minimum amount of disk space guaranteed to be available to this dataset itself.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### copies

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Number of copies of data blocks to maintain for redundancy (1-3).
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### snapdir

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Visibility of the .zfs/snapshot directory (visible/hidden).
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### readonly

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Whether the dataset is read-only.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### recordsize

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The suggested block size for files in this filesystem dataset.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### sparse

- Schema name: `PoolDatasetEntryProperty`
- Type: object

For volumes, whether to use sparse (thin) provisioning.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### volsize

- Schema name: `PoolDatasetEntryProperty`
- Type: object

For volumes, the logical size of the volume.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### volblocksize

- Schema name: `PoolDatasetEntryProperty`
- Type: object

For volumes, the block size used by the volume.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### key_format

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Format of the encryption key (hex/raw/passphrase). Only relevant for encrypted datasets.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### encryption_algorithm

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Encryption algorithm used (e.g., AES-256-GCM). Only relevant for encrypted datasets.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### used

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Total amount of disk space consumed by this dataset and all its children.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### usedbychildren

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by child datasets.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### usedbydataset

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by this dataset itself, excluding children and snapshots.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### usedbyrefreservation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by the refreservation of this dataset.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### usedbysnapshots

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by snapshots of this dataset.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### available

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space available to this dataset and its children.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### special_small_block_size

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Size threshold below which blocks are stored on special vdevs if configured.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### pbkdf2iters

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Number of PBKDF2 iterations used for passphrase-based encryption keys.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### creation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Timestamp when this dataset was created.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### snapdev

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Controls visibility of volume snapshots under /dev/zvol/<pool>/.
- No Additional Properties
######## parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

######## rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## source

- Schema name: `Source`

Indicates where the property value originates from.
######### Any of

########## Option 1

- Type: string

########## Option 2

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

######## source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

####### mountpoint

- Schema name: `Mountpoint`

Filesystem path where this dataset is mounted. Null for unmounted datasets or volumes.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### Additional Properties

Additional Properties of any type are allowed.
- Type: object

##### PoolDatasetQueryResultItem

- Type: string

##### Option 3

- Type: null

##### Option 1

- Type: boolean

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Schema name: `PoolDatasetQueryResultItem`
- Type: object
###### id

- Schema name: `Id`
- Type: string

The full dataset path including pool name.
Examples:

```json
"tank/dataset/child"
```

###### type

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

###### name

- Schema name: `Name`
- Type: string

The dataset name without the pool prefix.

###### pool

- Schema name: `Pool`
- Type: string

The name of the ZFS pool containing this dataset.

###### encrypted

- Schema name: `Encrypted`
- Type: boolean

Whether the dataset is encrypted.

###### encryption_root

- Schema name: `Encryption Root`

The root dataset where encryption is enabled. `null` if the dataset is not encrypted.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### key_loaded

- Schema name: `Key Loaded`

Whether the encryption key is currently loaded for encrypted datasets. `null` for unencrypted datasets.
####### Any of

######## Option 1

- Type: boolean

######## Option 2

- Type: null

###### children

- Schema name: `Children`
- Type: array

Array of child dataset objects nested under this dataset.
- No Additional Items

####### Each item of this array must be:

- Type: object

###### user_properties

- Schema name: `User Properties`
- Type: object

Custom user-defined ZFS properties set on this dataset as key-value pairs.

###### locked

- Schema name: `Locked`
- Type: boolean

Whether an encrypted dataset is currently locked (key not loaded).

###### comments

- Type: object

ZFS comments property for storing descriptive text about the dataset.

###### quota_warning

- Type: object

ZFS quota warning threshold property as a percentage.

###### quota_critical

- Type: object

ZFS quota critical threshold property as a percentage.

###### refquota_warning

- Type: object

ZFS reference quota warning threshold property as a percentage.

###### refquota_critical

- Type: object

ZFS reference quota critical threshold property as a percentage.

###### managedby

- Type: object

Identifies which service or system manages this dataset.

###### deduplication

- Type: object

ZFS deduplication setting - whether identical data blocks are stored only once.

###### aclmode

- Type: object

How Access Control Lists (ACLs) are handled when chmod is used.

###### acltype

- Type: object

The type of Access Control List system used (NFSV4, POSIX, or OFF).

###### xattr

- Type: object

Extended attributes storage method (on/off).

###### atime

- Type: object

Whether file access times are updated when files are accessed.

###### casesensitivity

- Type: object

File name case sensitivity setting (sensitive/insensitive).

###### checksum

- Type: object

Data integrity checksum algorithm used for this dataset.

###### exec

- Type: object

Whether files in this dataset can be executed.

###### sync

- Type: object

Synchronous write behavior (standard/always/disabled).

###### compression

- Type: object

Compression algorithm and level applied to data in this dataset.

###### compressratio

- Type: object

The achieved compression ratio as a decimal (e.g., '2.50x').

###### origin

- Type: object

The snapshot from which this clone was created. Empty for non-clone datasets.

###### quota

- Type: object

Maximum amount of disk space this dataset and its children can consume.

###### refquota

- Type: object

Maximum amount of disk space this dataset itself can consume (excluding children).

###### reservation

- Type: object

Minimum amount of disk space guaranteed to be available to this dataset and its children.

###### refreservation

- Type: object

Minimum amount of disk space guaranteed to be available to this dataset itself.

###### copies

- Type: object

Number of copies of data blocks to maintain for redundancy (1-3).

###### snapdir

- Type: object

Visibility of the .zfs/snapshot directory (visible/hidden).

###### readonly

- Type: object

Whether the dataset is read-only.

###### recordsize

- Type: object

The suggested block size for files in this filesystem dataset.

###### sparse

- Type: object

For volumes, whether to use sparse (thin) provisioning.

###### volsize

- Type: object

For volumes, the logical size of the volume.

###### volblocksize

- Type: object

For volumes, the block size used by the volume.

###### key_format

- Type: object

Format of the encryption key (hex/raw/passphrase). Only relevant for encrypted datasets.

###### encryption_algorithm

- Type: object

Encryption algorithm used (e.g., AES-256-GCM). Only relevant for encrypted datasets.

###### used

- Type: object

Total amount of disk space consumed by this dataset and all its children.

###### usedbychildren

- Type: object

Amount of disk space consumed by child datasets.

###### usedbydataset

- Type: object

Amount of disk space consumed by this dataset itself, excluding children and snapshots.

###### usedbyrefreservation

- Type: object

Amount of disk space consumed by the refreservation of this dataset.

###### usedbysnapshots

- Type: object

Amount of disk space consumed by snapshots of this dataset.

###### available

- Type: object

Amount of disk space available to this dataset and its children.

###### special_small_block_size

- Type: object

Size threshold below which blocks are stored on special vdevs if configured.

###### pbkdf2iters

- Type: object

Number of PBKDF2 iterations used for passphrase-based encryption keys.

###### creation

- Type: object

Timestamp when this dataset was created.

###### snapdev

- Type: object

Controls visibility of volume snapshots under /dev/zvol/<pool>/.

###### mountpoint

- Schema name: `Mountpoint`

Filesystem path where this dataset is mounted. Null for unmounted datasets or volumes.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### Additional Properties

Additional Properties of any type are allowed.
- Type: object

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: boolean

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
