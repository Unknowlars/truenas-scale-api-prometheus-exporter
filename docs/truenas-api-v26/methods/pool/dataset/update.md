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

Update the `comments` for "tank/myuser"::

{ "jsonrpc": "2.0", "id": 1, "method": "pool.dataset.update", "params": ["tank/myuser", { "comments": "Dataset for myuser, UPDATE #1" }] }

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

Size threshold below which blocks are stored on special vdevs in bytes.
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

- Type: object

The updated dataset information.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
