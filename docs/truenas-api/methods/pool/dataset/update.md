---
title: pool.dataset.update
kind: method
source_rst: _sources/api_methods_pool.dataset.update.rst.txt
source_html: api_methods_pool.dataset.update.html
required_roles:
  - DATASET_WRITE
---

# pool.dataset.update

## Summary

Updates a dataset/zvol `id`.

.. examples(websocket)::

Update the `comments` for "tank/myuser".

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "pool.dataset.update, "params": ["tank/myuser", { "comments": "Dataset for myuser, UPDATE #1" }] }

## Required Roles

- `DATASET_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: string

The dataset ID (full path) to update.

#### Parameter 2: data

#### data

- Schema name: `data`
- Type: object

The dataset properties to update.
- No Additional Properties
##### comments

- Schema name: `Comments`
- Type: string

Comments or description for the dataset.

##### sync

- Schema name: `Sync`
- Type: enum (of string)

Synchronous write behavior for the dataset.

##### snapdev

- Schema name: `Snapdev`
- Type: enum (of string)

Controls visibility of volume snapshots under /dev/zvol/.

##### compression

- Schema name: `Compression`
- Type: enum (of string)

Compression algorithm to use for the dataset. Higher numbered variants provide better compression but use more CPU. 'INHERIT' uses the parent dataset's setting.

##### exec

- Schema name: `Exec`
- Type: enum (of string)

Whether files in this dataset can be executed.

##### managedby

- Schema name: `Managedby`
- Type: string

Identifies which service or system manages this dataset.
- Must be at least `1` characters long

##### quota_warning

- Schema name: `Quota Warning`

Percentage of dataset quota at which to issue a warning. 0-100 or 'INHERIT'.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `0` and lesser or equal to `100`

####### Option 2

- Type: const

##### quota_critical

- Schema name: `Quota Critical`

Percentage of dataset quota at which to issue a critical alert. 0-100 or 'INHERIT'.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `0` and lesser or equal to `100`

####### Option 2

- Type: const

##### refquota_warning

- Schema name: `Refquota Warning`

Percentage of reference quota at which to issue a warning. 0-100 or 'INHERIT'.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `0` and lesser or equal to `100`

####### Option 2

- Type: const

##### refquota_critical

- Schema name: `Refquota Critical`

Percentage of reference quota at which to issue a critical alert. 0-100 or 'INHERIT'.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `0` and lesser or equal to `100`

####### Option 2

- Type: const

##### reservation

- Schema name: `Reservation`
- Type: integer

Minimum disk space guaranteed to this dataset and its children in bytes.

##### refreservation

- Schema name: `Refreservation`
- Type: integer

Minimum disk space guaranteed to this dataset itself in bytes.

##### special_small_block_size

- Schema name: `Special Small Block Size`

Size threshold below which blocks are stored on special vdevs.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: const

##### copies

- Schema name: `Copies`

Number of copies of data blocks to maintain for redundancy.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: const

##### snapdir

- Schema name: `Snapdir`
- Type: enum (of string)

Controls visibility of the `.zfs/snapshot` directory. 'DISABLED' hides snapshots, 'VISIBLE' shows them, 'HIDDEN' makes them accessible but not listed.

##### deduplication

- Schema name: `Deduplication`
- Type: enum (of string)

Deduplication setting. 'ON' enables dedup, 'VERIFY' enables with checksum verification, 'OFF' disables.

##### checksum

- Schema name: `Checksum`
- Type: enum (of string)

Checksum algorithm to verify data integrity. Higher security algorithms like SHA256 provide better protection but use more CPU.

##### readonly

- Schema name: `Readonly`
- Type: enum (of string)

Whether the dataset is read-only.

##### user_properties

- Schema name: `User Properties`
- Type: array of object

Custom user-defined properties to set on the dataset.
- No Additional Items

###### Each item of this array must be:

###### PoolDatasetCreateUserProperty

- Schema name: `PoolDatasetCreateUserProperty`
- Type: object
- No Additional Properties
####### key (required)

- Schema name: `Key`
- Type: string

User property key in namespace:property format.
Examples:

```json
"custom:backup_policy"
```
Examples:

```json
"org:created_by"
```

####### value (required)

- Schema name: `Value`
- Type: string

The value to assign to the user property.

##### create_ancestors

- Schema name: `Create Ancestors`
- Type: boolean

Whether to create any missing parent datasets.

##### force_size

- Schema name: `Force Size`
- Type: boolean

Force creation even if the size is not optimal.

##### volsize

- Schema name: `Volsize`
- Type: integer

The volume size in bytes; supposed to be a multiple of the block size.

##### aclmode

- Schema name: `Aclmode`
- Type: enum (of string)

How Access Control Lists are handled when chmod is used.

##### acltype

- Schema name: `Acltype`
- Type: enum (of string)

The type of Access Control List system to use.

##### atime

- Schema name: `Atime`
- Type: enum (of string)

Whether file access times are updated when files are accessed.

##### quota

- Schema name: `Quota`

Maximum disk space this dataset and its children can consume in bytes.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `1073741824`

####### Option 2

- Type: enum (of integer or null)

##### refquota

- Schema name: `Refquota`

Maximum disk space this dataset itself can consume in bytes.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `1073741824`

####### Option 2

- Type: enum (of integer or null)

##### recordsize

- Schema name: `Recordsize`
- Type: string

The suggested block size for files in this filesystem dataset.

##### user_properties_update

- Schema name: `User Properties Update`
- Type: array of object

Array of user property updates to apply to the dataset.
- No Additional Items

###### Each item of this array must be:

###### PoolDatasetUpdateUserProperty

- Schema name: `PoolDatasetUpdateUserProperty`
- Type: object
- No Additional Properties
####### key (required)

- Schema name: `Key`
- Type: string

User property key in namespace:property format.
Examples:

```json
"custom:backup_policy"
```
Examples:

```json
"org:created_by"
```

####### value

- Schema name: `Value`
- Type: string

New value for the user property. Not required if removing the property.

####### remove

- Schema name: `Remove`
- Type: boolean

Whether to remove this user property from the dataset.

### Return value

- Schema name: `PoolDatasetEntry`
- Type: object

The updated dataset information.
#### id

- Schema name: `Id`
- Type: string

The full dataset path including pool name.
Examples:

```json
"tank/dataset/child"
```

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

#### name

- Schema name: `Name`
- Type: string

The dataset name without the pool prefix.

#### pool

- Schema name: `Pool`
- Type: string

The name of the ZFS pool containing this dataset.

#### encrypted

- Schema name: `Encrypted`
- Type: boolean

Whether the dataset is encrypted.

#### encryption_root

- Schema name: `Encryption Root`

The root dataset where encryption is enabled. `null` if the dataset is not encrypted.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### key_loaded

- Schema name: `Key Loaded`

Whether the encryption key is currently loaded for encrypted datasets. `null` for unencrypted datasets.
##### Any of

###### Option 1

- Type: boolean

###### Option 2

- Type: null

#### children

- Schema name: `Children`
- Type: array

Array of child dataset objects nested under this dataset.
- No Additional Items

##### Each item of this array must be:

- Type: object

#### user_properties

- Schema name: `User Properties`
- Type: object

Custom user-defined ZFS properties set on this dataset as key-value pairs.

#### locked

- Schema name: `Locked`
- Type: boolean

Whether an encrypted dataset is currently locked (key not loaded).

#### comments

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS comments property for storing descriptive text about the dataset.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### quota_warning

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS quota warning threshold property as a percentage.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### quota_critical

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS quota critical threshold property as a percentage.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### refquota_warning

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS reference quota warning threshold property as a percentage.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### refquota_critical

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS reference quota critical threshold property as a percentage.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### managedby

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Identifies which service or system manages this dataset.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### deduplication

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS deduplication setting - whether identical data blocks are stored only once.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### aclmode

- Schema name: `PoolDatasetEntryProperty`
- Type: object

How Access Control Lists (ACLs) are handled when chmod is used.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### acltype

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The type of Access Control List system used (NFSV4, POSIX, or OFF).
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### xattr

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Extended attributes storage method (on/off).
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### atime

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Whether file access times are updated when files are accessed.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### casesensitivity

- Schema name: `PoolDatasetEntryProperty`
- Type: object

File name case sensitivity setting (sensitive/insensitive).
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### checksum

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Data integrity checksum algorithm used for this dataset.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### exec

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Whether files in this dataset can be executed.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### sync

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Synchronous write behavior (standard/always/disabled).
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### compression

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Compression algorithm and level applied to data in this dataset.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### compressratio

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The achieved compression ratio as a decimal (e.g., '2.50x').
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### origin

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The snapshot from which this clone was created. Empty for non-clone datasets.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### quota

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Maximum amount of disk space this dataset and its children can consume.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### refquota

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Maximum amount of disk space this dataset itself can consume (excluding children).
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### reservation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Minimum amount of disk space guaranteed to be available to this dataset and its children.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### refreservation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Minimum amount of disk space guaranteed to be available to this dataset itself.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### copies

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Number of copies of data blocks to maintain for redundancy (1-3).
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### snapdir

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Visibility of the .zfs/snapshot directory (visible/hidden).
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### readonly

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Whether the dataset is read-only.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### recordsize

- Schema name: `PoolDatasetEntryProperty`
- Type: object

The suggested block size for files in this filesystem dataset.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### sparse

- Schema name: `PoolDatasetEntryProperty`
- Type: object

For volumes, whether to use sparse (thin) provisioning.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### volsize

- Schema name: `PoolDatasetEntryProperty`
- Type: object

For volumes, the logical size of the volume.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### volblocksize

- Schema name: `PoolDatasetEntryProperty`
- Type: object

For volumes, the block size used by the volume.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### key_format

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Format of the encryption key (hex/raw/passphrase). Only relevant for encrypted datasets.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### encryption_algorithm

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Encryption algorithm used (e.g., AES-256-GCM). Only relevant for encrypted datasets.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### used

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Total amount of disk space consumed by this dataset and all its children.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### usedbychildren

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by child datasets.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### usedbydataset

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by this dataset itself, excluding children and snapshots.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### usedbyrefreservation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by the refreservation of this dataset.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### usedbysnapshots

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space consumed by snapshots of this dataset.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### available

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Amount of disk space available to this dataset and its children.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### special_small_block_size

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Size threshold below which blocks are stored on special vdevs if configured.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### pbkdf2iters

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Number of PBKDF2 iterations used for passphrase-based encryption keys.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### creation

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Timestamp when this dataset was created.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### snapdev

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Controls visibility of volume snapshots under /dev/zvol/<pool>/.
- No Additional Properties
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### source

- Schema name: `Source`

Indicates where the property value originates from.
###### Any of

####### Option 1

- Type: string

####### Option 2

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

##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

#### mountpoint

- Schema name: `Mountpoint`

Filesystem path where this dataset is mounted. Null for unmounted datasets or volumes.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
