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

### ADDED

- Schema name: `PoolDatasetAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

#### fields (required)

- Schema name: `PoolDatasetEntry`
- Type: object
##### id

- Schema name: `Id`
- Type: string

The full dataset path including pool name.
Examples:

```json
"tank/dataset/child"
```

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

##### name

- Schema name: `Name`
- Type: string

The dataset name without the pool prefix.

##### pool

- Schema name: `Pool`
- Type: string

The name of the ZFS pool containing this dataset.

##### encrypted

- Schema name: `Encrypted`
- Type: boolean

Whether the dataset is encrypted.

##### encryption_root

- Schema name: `Encryption Root`

The root dataset where encryption is enabled. `null` if the dataset is not encrypted.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### key_loaded

- Schema name: `Key Loaded`

Whether the encryption key is currently loaded for encrypted datasets. `null` for unencrypted datasets.
###### Any of

####### Option 1

- Type: boolean

####### Option 2

- Type: null

##### children

- Schema name: `Children`
- Type: array

Array of child dataset objects nested under this dataset.
- No Additional Items

###### Each item of this array must be:

- Type: object

##### user_properties

- Schema name: `User Properties`
- Type: object

Custom user-defined ZFS properties set on this dataset as key-value pairs.

##### locked

- Schema name: `Locked`
- Type: boolean

Whether an encrypted dataset is currently locked (key not loaded).

##### comments

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS comments property for storing descriptive text about the dataset.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### quota_warning

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS quota warning threshold property as a percentage.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### quota_critical

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS quota critical threshold property as a percentage.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### refquota_warning

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS reference quota warning threshold property as a percentage.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### refquota_critical

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS reference quota critical threshold property as a percentage.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### managedby

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Identifies which service or system manages this dataset.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### deduplication

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS deduplication setting - whether identical data blocks are stored only once.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### aclmode

- Schema name: `PoolDatasetEntryProperty`
- Type: object

How Access Control Lists (ACLs) are handled when chmod is used.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### acltype

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The type of Access Control List system used (NFSV4, POSIX, or OFF).
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### xattr

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Extended attributes storage method (on/off).
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### atime

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Whether file access times are updated when files are accessed.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### casesensitivity

- Schema name: `PoolDatasetEntryProperty`
- Type: object

File name case sensitivity setting (sensitive/insensitive).
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### checksum

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Data integrity checksum algorithm used for this dataset.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### exec

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Whether files in this dataset can be executed.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### sync

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Synchronous write behavior (standard/always/disabled).
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### compression

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Compression algorithm and level applied to data in this dataset.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### compressratio

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The achieved compression ratio as a decimal (e.g., '2.50x').
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### origin

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The snapshot from which this clone was created. Empty for non-clone datasets.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### quota

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Maximum amount of disk space this dataset and its children can consume.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### refquota

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Maximum amount of disk space this dataset itself can consume (excluding children).
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### reservation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Minimum amount of disk space guaranteed to be available to this dataset and its children.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### refreservation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Minimum amount of disk space guaranteed to be available to this dataset itself.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### copies

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Number of copies of data blocks to maintain for redundancy (1-3).
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### snapdir

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Visibility of the .zfs/snapshot directory (visible/hidden).
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### readonly

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Whether the dataset is read-only.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### recordsize

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The suggested block size for files in this filesystem dataset.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### sparse

- Schema name: `PoolDatasetEntryProperty`
- Type: object

For volumes, whether to use sparse (thin) provisioning.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### volsize

- Schema name: `PoolDatasetEntryProperty`
- Type: object

For volumes, the logical size of the volume.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### volblocksize

- Schema name: `PoolDatasetEntryProperty`
- Type: object

For volumes, the block size used by the volume.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### key_format

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Format of the encryption key (hex/raw/passphrase). Only relevant for encrypted datasets.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### encryption_algorithm

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Encryption algorithm used (e.g., AES-256-GCM). Only relevant for encrypted datasets.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### used

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Total amount of disk space consumed by this dataset and all its children.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### usedbychildren

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by child datasets.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### usedbydataset

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by this dataset itself, excluding children and snapshots.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### usedbyrefreservation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by the refreservation of this dataset.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### usedbysnapshots

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by snapshots of this dataset.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### available

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space available to this dataset and its children.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### special_small_block_size

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Size threshold below which blocks are stored on special vdevs if configured.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### pbkdf2iters

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Number of PBKDF2 iterations used for passphrase-based encryption keys.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### creation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Timestamp when this dataset was created.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### snapdev

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Controls visibility of volume snapshots under /dev/zvol/<pool>/.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### mountpoint

- Schema name: `Mountpoint`

Filesystem path where this dataset is mounted. Null for unmounted datasets or volumes.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### Additional Properties

Additional Properties of any type are allowed.
- Type: object

### CHANGED

- Schema name: `PoolDatasetChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

#### fields (required)

- Schema name: `PoolDatasetEntry`
- Type: object
##### id

- Schema name: `Id`
- Type: string

The full dataset path including pool name.
Examples:

```json
"tank/dataset/child"
```

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

##### name

- Schema name: `Name`
- Type: string

The dataset name without the pool prefix.

##### pool

- Schema name: `Pool`
- Type: string

The name of the ZFS pool containing this dataset.

##### encrypted

- Schema name: `Encrypted`
- Type: boolean

Whether the dataset is encrypted.

##### encryption_root

- Schema name: `Encryption Root`

The root dataset where encryption is enabled. `null` if the dataset is not encrypted.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### key_loaded

- Schema name: `Key Loaded`

Whether the encryption key is currently loaded for encrypted datasets. `null` for unencrypted datasets.
###### Any of

####### Option 1

- Type: boolean

####### Option 2

- Type: null

##### children

- Schema name: `Children`
- Type: array

Array of child dataset objects nested under this dataset.
- No Additional Items

###### Each item of this array must be:

- Type: object

##### user_properties

- Schema name: `User Properties`
- Type: object

Custom user-defined ZFS properties set on this dataset as key-value pairs.

##### locked

- Schema name: `Locked`
- Type: boolean

Whether an encrypted dataset is currently locked (key not loaded).

##### comments

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS comments property for storing descriptive text about the dataset.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### quota_warning

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS quota warning threshold property as a percentage.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### quota_critical

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS quota critical threshold property as a percentage.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### refquota_warning

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS reference quota warning threshold property as a percentage.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### refquota_critical

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS reference quota critical threshold property as a percentage.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### managedby

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Identifies which service or system manages this dataset.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### deduplication

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS deduplication setting - whether identical data blocks are stored only once.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### aclmode

- Schema name: `PoolDatasetEntryProperty`
- Type: object

How Access Control Lists (ACLs) are handled when chmod is used.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### acltype

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The type of Access Control List system used (NFSV4, POSIX, or OFF).
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### xattr

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Extended attributes storage method (on/off).
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### atime

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Whether file access times are updated when files are accessed.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### casesensitivity

- Schema name: `PoolDatasetEntryProperty`
- Type: object

File name case sensitivity setting (sensitive/insensitive).
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### checksum

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Data integrity checksum algorithm used for this dataset.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### exec

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Whether files in this dataset can be executed.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### sync

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Synchronous write behavior (standard/always/disabled).
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### compression

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Compression algorithm and level applied to data in this dataset.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### compressratio

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The achieved compression ratio as a decimal (e.g., '2.50x').
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### origin

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The snapshot from which this clone was created. Empty for non-clone datasets.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### quota

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Maximum amount of disk space this dataset and its children can consume.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### refquota

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Maximum amount of disk space this dataset itself can consume (excluding children).
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### reservation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Minimum amount of disk space guaranteed to be available to this dataset and its children.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### refreservation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Minimum amount of disk space guaranteed to be available to this dataset itself.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### copies

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Number of copies of data blocks to maintain for redundancy (1-3).
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### snapdir

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Visibility of the .zfs/snapshot directory (visible/hidden).
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### readonly

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Whether the dataset is read-only.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### recordsize

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The suggested block size for files in this filesystem dataset.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### sparse

- Schema name: `PoolDatasetEntryProperty`
- Type: object

For volumes, whether to use sparse (thin) provisioning.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### volsize

- Schema name: `PoolDatasetEntryProperty`
- Type: object

For volumes, the logical size of the volume.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### volblocksize

- Schema name: `PoolDatasetEntryProperty`
- Type: object

For volumes, the block size used by the volume.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### key_format

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Format of the encryption key (hex/raw/passphrase). Only relevant for encrypted datasets.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### encryption_algorithm

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Encryption algorithm used (e.g., AES-256-GCM). Only relevant for encrypted datasets.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### used

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Total amount of disk space consumed by this dataset and all its children.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### usedbychildren

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by child datasets.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### usedbydataset

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by this dataset itself, excluding children and snapshots.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### usedbyrefreservation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by the refreservation of this dataset.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### usedbysnapshots

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by snapshots of this dataset.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### available

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space available to this dataset and its children.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### special_small_block_size

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Size threshold below which blocks are stored on special vdevs if configured.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### pbkdf2iters

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Number of PBKDF2 iterations used for passphrase-based encryption keys.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### creation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Timestamp when this dataset was created.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### snapdev

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Controls visibility of volume snapshots under /dev/zvol/<pool>/.
- No Additional Properties
###### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

###### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### source

- Schema name: `Source`

Indicates where the property value originates from.
####### Any of

######## Option 1

- Type: string

######## Option 2

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

###### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

##### mountpoint

- Schema name: `Mountpoint`

Filesystem path where this dataset is mounted. Null for unmounted datasets or volumes.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### Additional Properties

Additional Properties of any type are allowed.
- Type: object

### REMOVED

- Schema name: `PoolDatasetRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
