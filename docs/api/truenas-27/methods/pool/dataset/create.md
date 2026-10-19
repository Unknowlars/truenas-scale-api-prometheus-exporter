---
title: pool.dataset.create
kind: method
source_rst: _sources/api_methods_pool.dataset.create.rst.txt
source_html: api_methods_pool.dataset.create.html
required_roles:
  - DATASET_WRITE
---

# pool.dataset.create

## Summary

Creates a dataset/zvol.

.. examples(websocket)::

Create a dataset within tank pool.

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "pool.dataset.create, "params": [{ "name": "tank/myuser", "comments": "Dataset for myuser" }] }

## Required Roles

- `DATASET_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

<a id="Call_parameters_items_i0"></a>
#### data

- Schema name: `data`

Configuration data for creating a new ZFS dataset.
<a id="Call_parameters_items_i0_oneOf"></a>
##### One of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0"></a>
###### [PoolDatasetCreateFilesystem](#tab-pane_Call_parameters_items_i0_oneOf_i0)

- Schema name: `PoolDatasetCreateFilesystem`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_oneOf_i0_name"></a>
<a id="Call_parameters_items_i0_oneOf_i0_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

The name of the dataset to create.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_oneOf_i0_comments"></a>
<a id="Call_parameters_items_i0_oneOf_i0_comments"></a>
###### comments

- Schema name: `Comments`
- Type: string
- Default: "INHERIT"

Comments or description for the dataset.

<a id="headingCall_parameters_items_i0_oneOf_i0_sync"></a>
<a id="Call_parameters_items_i0_oneOf_i0_sync"></a>
###### sync

- Schema name: `Sync`
- Type: enum (of string)
- Default: "INHERIT"

Synchronous write behavior for the dataset.
###### Must be one of:

- "STANDARD"
- "ALWAYS"
- "DISABLED"
- "INHERIT"

<a id="headingCall_parameters_items_i0_oneOf_i0_snapdev"></a>
<a id="Call_parameters_items_i0_oneOf_i0_snapdev"></a>
###### snapdev

- Schema name: `Snapdev`
- Type: enum (of string)

Controls visibility of volume snapshots under /dev/zvol/.
###### Must be one of:

- "HIDDEN"
- "VISIBLE"
- "INHERIT"

<a id="headingCall_parameters_items_i0_oneOf_i0_compression"></a>
<a id="Call_parameters_items_i0_oneOf_i0_compression"></a>
###### compression

- Schema name: `Compression`
- Type: enum (of string)
- Default: "INHERIT"

Compression algorithm to use for the dataset. Higher numbered variants provide better compression but use more CPU. 'INHERIT' uses the parent dataset's setting.
###### Must be one of:

- "ON"
- "OFF"
- "LZ4"
- "GZIP"
- "GZIP-1"
- "GZIP-9"
- "ZSTD"
- "ZSTD-FAST"
- "ZLE"
- "LZJB"
- "ZSTD-1"
- "ZSTD-2"
- "ZSTD-3"
- "ZSTD-4"
- "ZSTD-5"
- "ZSTD-6"
- "ZSTD-7"
- "ZSTD-8"
- "ZSTD-9"
- "ZSTD-10"
- "ZSTD-11"
- "ZSTD-12"
- "ZSTD-13"
- "ZSTD-14"
- "ZSTD-15"
- "ZSTD-16"
- "ZSTD-17"
- "ZSTD-18"
- "ZSTD-19"
- "ZSTD-FAST-1"
- "ZSTD-FAST-2"
- "ZSTD-FAST-3"
- "ZSTD-FAST-4"
- "ZSTD-FAST-5"
- "ZSTD-FAST-6"
- "ZSTD-FAST-7"
- "ZSTD-FAST-8"
- "ZSTD-FAST-9"
- "ZSTD-FAST-10"
- "ZSTD-FAST-20"
- "ZSTD-FAST-30"
- "ZSTD-FAST-40"
- "ZSTD-FAST-50"
- "ZSTD-FAST-60"
- "ZSTD-FAST-70"
- "ZSTD-FAST-80"
- "ZSTD-FAST-90"
- "ZSTD-FAST-100"
- "ZSTD-FAST-500"
- "ZSTD-FAST-1000"
- "INHERIT"

<a id="headingCall_parameters_items_i0_oneOf_i0_exec"></a>
<a id="Call_parameters_items_i0_oneOf_i0_exec"></a>
###### exec

- Schema name: `Exec`
- Type: enum (of string)
- Default: "INHERIT"

Whether files in this dataset can be executed.
###### Must be one of:

- "ON"
- "OFF"
- "INHERIT"

<a id="headingCall_parameters_items_i0_oneOf_i0_managedby"></a>
<a id="Call_parameters_items_i0_oneOf_i0_managedby"></a>
###### managedby

- Schema name: `Managedby`
- Type: string
- Default: "INHERIT"

Identifies which service or system manages this dataset.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_oneOf_i0_quota_warning"></a>
<a id="Call_parameters_items_i0_oneOf_i0_quota_warning"></a>
###### quota_warning

- Schema name: `Quota Warning`
- Default: "INHERIT"

Percentage of dataset quota at which to issue a warning. 0-100 or 'INHERIT'.
<a id="Call_parameters_items_i0_oneOf_i0_quota_warning_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0_quota_warning_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_oneOf_i0_quota_warning_anyOf_i0)

- Type: integer
- Value must be greater or equal to `0` and lesser or equal to `100`

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0_quota_warning_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_oneOf_i0_quota_warning_anyOf_i1)

- Type: const
- Specific value: `"INHERIT"`

<a id="headingCall_parameters_items_i0_oneOf_i0_quota_critical"></a>
<a id="Call_parameters_items_i0_oneOf_i0_quota_critical"></a>
###### quota_critical

- Schema name: `Quota Critical`
- Default: "INHERIT"

Percentage of dataset quota at which to issue a critical alert. 0-100 or 'INHERIT'.
<a id="Call_parameters_items_i0_oneOf_i0_quota_critical_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0_quota_critical_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_oneOf_i0_quota_critical_anyOf_i0)

- Type: integer
- Value must be greater or equal to `0` and lesser or equal to `100`

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0_quota_critical_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_oneOf_i0_quota_critical_anyOf_i1)

- Type: const
- Specific value: `"INHERIT"`

<a id="headingCall_parameters_items_i0_oneOf_i0_refquota_warning"></a>
<a id="Call_parameters_items_i0_oneOf_i0_refquota_warning"></a>
###### refquota_warning

- Schema name: `Refquota Warning`
- Default: "INHERIT"

Percentage of reference quota at which to issue a warning. 0-100 or 'INHERIT'.
<a id="Call_parameters_items_i0_oneOf_i0_refquota_warning_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0_refquota_warning_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_oneOf_i0_refquota_warning_anyOf_i0)

- Type: integer
- Value must be greater or equal to `0` and lesser or equal to `100`

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0_refquota_warning_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_oneOf_i0_refquota_warning_anyOf_i1)

- Type: const
- Specific value: `"INHERIT"`

<a id="headingCall_parameters_items_i0_oneOf_i0_refquota_critical"></a>
<a id="Call_parameters_items_i0_oneOf_i0_refquota_critical"></a>
###### refquota_critical

- Schema name: `Refquota Critical`
- Default: "INHERIT"

Percentage of reference quota at which to issue a critical alert. 0-100 or 'INHERIT'.
<a id="Call_parameters_items_i0_oneOf_i0_refquota_critical_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0_refquota_critical_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_oneOf_i0_refquota_critical_anyOf_i0)

- Type: integer
- Value must be greater or equal to `0` and lesser or equal to `100`

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0_refquota_critical_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_oneOf_i0_refquota_critical_anyOf_i1)

- Type: const
- Specific value: `"INHERIT"`

<a id="headingCall_parameters_items_i0_oneOf_i0_reservation"></a>
<a id="Call_parameters_items_i0_oneOf_i0_reservation"></a>
###### reservation

- Schema name: `Reservation`
- Type: integer

Minimum disk space guaranteed to this dataset and its children in bytes.

<a id="headingCall_parameters_items_i0_oneOf_i0_refreservation"></a>
<a id="Call_parameters_items_i0_oneOf_i0_refreservation"></a>
###### refreservation

- Schema name: `Refreservation`
- Type: integer

Minimum disk space guaranteed to this dataset itself in bytes.

<a id="headingCall_parameters_items_i0_oneOf_i0_special_small_block_size"></a>
<a id="Call_parameters_items_i0_oneOf_i0_special_small_block_size"></a>
###### special_small_block_size

- Schema name: `Special Small Block Size`

Size threshold below which blocks are stored on special vdevs in bytes.
<a id="Call_parameters_items_i0_oneOf_i0_special_small_block_size_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0_special_small_block_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_oneOf_i0_special_small_block_size_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0_special_small_block_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_oneOf_i0_special_small_block_size_anyOf_i1)

- Type: const
- Specific value: `"INHERIT"`

<a id="headingCall_parameters_items_i0_oneOf_i0_copies"></a>
<a id="Call_parameters_items_i0_oneOf_i0_copies"></a>
###### copies

- Schema name: `Copies`
- Default: "INHERIT"

Number of copies of data blocks to maintain for redundancy.
<a id="Call_parameters_items_i0_oneOf_i0_copies_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0_copies_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_oneOf_i0_copies_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0_copies_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_oneOf_i0_copies_anyOf_i1)

- Type: const
- Specific value: `"INHERIT"`

<a id="headingCall_parameters_items_i0_oneOf_i0_snapdir"></a>
<a id="Call_parameters_items_i0_oneOf_i0_snapdir"></a>
###### snapdir

- Schema name: `Snapdir`
- Type: enum (of string)
- Default: "INHERIT"

Controls visibility of the `.zfs/snapshot` directory. 'DISABLED' hides snapshots, 'VISIBLE' shows them, 'HIDDEN' makes them accessible but not listed.
###### Must be one of:

- "DISABLED"
- "VISIBLE"
- "HIDDEN"
- "INHERIT"

<a id="headingCall_parameters_items_i0_oneOf_i0_deduplication"></a>
<a id="Call_parameters_items_i0_oneOf_i0_deduplication"></a>
###### deduplication

- Schema name: `Deduplication`
- Type: enum (of string)
- Default: "INHERIT"

Deduplication setting. 'ON' enables dedup, 'VERIFY' enables with checksum verification, 'OFF' disables. While ZFS tiering is enabled, cannot be enabled on a dataset in the PERFORMANCE tier (data on the SPECIAL vdev) or on one with a PERFORMANCE-tier descendant that would inherit the setting.
###### Must be one of:

- "ON"
- "VERIFY"
- "OFF"
- "INHERIT"

<a id="headingCall_parameters_items_i0_oneOf_i0_checksum"></a>
<a id="Call_parameters_items_i0_oneOf_i0_checksum"></a>
###### checksum

- Schema name: `Checksum`
- Type: enum (of string)
- Default: "INHERIT"

Checksum algorithm to verify data integrity. Higher security algorithms like SHA256 provide better protection but use more CPU.
###### Must be one of:

- "ON"
- "OFF"
- "FLETCHER2"
- "FLETCHER4"
- "SHA256"
- "SHA512"
- "SKEIN"
- "EDONR"
- "BLAKE3"
- "INHERIT"

<a id="headingCall_parameters_items_i0_oneOf_i0_readonly"></a>
<a id="Call_parameters_items_i0_oneOf_i0_readonly"></a>
###### readonly

- Schema name: `Readonly`
- Type: enum (of string)
- Default: "INHERIT"

Whether the dataset is read-only.
###### Must be one of:

- "ON"
- "OFF"
- "INHERIT"

<a id="headingCall_parameters_items_i0_oneOf_i0_share_type"></a>
<a id="Call_parameters_items_i0_oneOf_i0_share_type"></a>
###### share_type

- Schema name: `Share Type`
- Type: enum (of string)
- Default: "GENERIC"

Optimization type for the dataset based on its intended use.
###### Must be one of:

- "GENERIC"
- "MULTIPROTOCOL"
- "NFS"
- "SMB"
- "APPS"

<a id="headingCall_parameters_items_i0_oneOf_i0_encryption_options"></a>
<a id="Call_parameters_items_i0_oneOf_i0_encryption_options"></a>
###### encryption_options

- Schema name: `PoolCreateEncryptionOptions`
- Type: object

Configuration for encryption of dataset for `name` pool.
- No Additional Properties
<a id="headingCall_parameters_items_i0_oneOf_i0_encryption_options_generate_key"></a>
<a id="Call_parameters_items_i0_oneOf_i0_encryption_options_generate_key"></a>
###### generate_key

- Schema name: `Generate Key`
- Type: boolean
- Default: false

Automatically generate the key to be used for dataset encryption.

<a id="headingCall_parameters_items_i0_oneOf_i0_encryption_options_pbkdf2iters"></a>
<a id="Call_parameters_items_i0_oneOf_i0_encryption_options_pbkdf2iters"></a>
###### pbkdf2iters

- Schema name: `Pbkdf2Iters`
- Type: integer
- Default: 1300000

Number of PBKDF2 iterations for key derivation from passphrase. Higher iterations improve security against brute force attacks but increase unlock time.
- Value must be greater or equal to `1300000`

<a id="headingCall_parameters_items_i0_oneOf_i0_encryption_options_passphrase"></a>
<a id="Call_parameters_items_i0_oneOf_i0_encryption_options_passphrase"></a>
###### passphrase

- Schema name: `Passphrase`
- Default: null

Must be specified if encryption for root dataset is desired with a passphrase as a key.
<a id="Call_parameters_items_i0_oneOf_i0_encryption_options_passphrase_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0_encryption_options_passphrase_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_oneOf_i0_encryption_options_passphrase_anyOf_i0)

- Type: string
- Must be at least `8` characters long

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0_encryption_options_passphrase_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_oneOf_i0_encryption_options_passphrase_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_oneOf_i0_encryption_options_key"></a>
<a id="Call_parameters_items_i0_oneOf_i0_encryption_options_key"></a>
###### key

- Schema name: `Key`
- Default: null

A hex-encoded key specified as an alternative to using `passphrase`.
<a id="Call_parameters_items_i0_oneOf_i0_encryption_options_key_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0_encryption_options_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_oneOf_i0_encryption_options_key_anyOf_i0)

- Type: string
- Must be at least `64` characters long
- Must be at most `64` characters long

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0_encryption_options_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_oneOf_i0_encryption_options_key_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_oneOf_i0_encryption"></a>
<a id="Call_parameters_items_i0_oneOf_i0_encryption"></a>
###### encryption

- Schema name: `Encryption`
- Type: boolean
- Default: false

Create a ZFS encrypted root dataset for `name` pool. There is 1 case where ZFS encryption is not allowed for a dataset: 1) If the parent dataset is encrypted with a passphrase and `name` is being created with a key for encrypting the dataset.

<a id="headingCall_parameters_items_i0_oneOf_i0_inherit_encryption"></a>
<a id="Call_parameters_items_i0_oneOf_i0_inherit_encryption"></a>
###### inherit_encryption

- Schema name: `Inherit Encryption`
- Type: boolean
- Default: true

Whether to inherit encryption settings from the parent dataset.

<a id="headingCall_parameters_items_i0_oneOf_i0_user_properties"></a>
<a id="Call_parameters_items_i0_oneOf_i0_user_properties"></a>
###### user_properties

- Schema name: `User Properties`
- Type: array of object
- Default: []

Custom user-defined properties to set on the dataset.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_oneOf_i0_user_properties_items"></a>
###### PoolDatasetCreateUserProperty

- Schema name: `PoolDatasetCreateUserProperty`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_oneOf_i0_user_properties_items_key"></a>
<a id="Call_parameters_items_i0_oneOf_i0_user_properties_items_key"></a>
###### key (required)

- Schema name: `Key`
- Type: string

User property key in namespace:property format.
- Must match regular expression: `.*:.*`
Examples:

```json
"custom:backup_policy"
```
Examples:

```json
"org:created_by"
```

<a id="headingCall_parameters_items_i0_oneOf_i0_user_properties_items_value"></a>
<a id="Call_parameters_items_i0_oneOf_i0_user_properties_items_value"></a>
###### value (required)

- Schema name: `Value`
- Type: string

The value to assign to the user property.

<a id="headingCall_parameters_items_i0_oneOf_i0_create_ancestors"></a>
<a id="Call_parameters_items_i0_oneOf_i0_create_ancestors"></a>
###### create_ancestors

- Schema name: `Create Ancestors`
- Type: boolean
- Default: false

Whether to create any missing parent datasets.

<a id="headingCall_parameters_items_i0_oneOf_i0_type"></a>
<a id="Call_parameters_items_i0_oneOf_i0_type"></a>
###### type

- Schema name: `Type`
- Type: const
- Default: "FILESYSTEM"

Type of dataset to create - filesystem.
- Specific value: `"FILESYSTEM"`

<a id="headingCall_parameters_items_i0_oneOf_i0_aclmode"></a>
<a id="Call_parameters_items_i0_oneOf_i0_aclmode"></a>
###### aclmode

- Schema name: `Aclmode`
- Type: enum (of string)

How Access Control Lists are handled when chmod is used.
###### Must be one of:

- "PASSTHROUGH"
- "RESTRICTED"
- "DISCARD"
- "INHERIT"

<a id="headingCall_parameters_items_i0_oneOf_i0_acltype"></a>
<a id="Call_parameters_items_i0_oneOf_i0_acltype"></a>
###### acltype

- Schema name: `Acltype`
- Type: enum (of string)

The type of Access Control List system to use.
###### Must be one of:

- "OFF"
- "NFSV4"
- "POSIX"
- "INHERIT"

<a id="headingCall_parameters_items_i0_oneOf_i0_atime"></a>
<a id="Call_parameters_items_i0_oneOf_i0_atime"></a>
###### atime

- Schema name: `Atime`
- Type: enum (of string)

Whether file access times are updated when files are accessed.
###### Must be one of:

- "ON"
- "OFF"
- "INHERIT"

<a id="headingCall_parameters_items_i0_oneOf_i0_casesensitivity"></a>
<a id="Call_parameters_items_i0_oneOf_i0_casesensitivity"></a>
###### casesensitivity

- Schema name: `Casesensitivity`
- Type: enum (of string)

File name case sensitivity setting.
###### Must be one of:

- "SENSITIVE"
- "INSENSITIVE"
- "INHERIT"

<a id="headingCall_parameters_items_i0_oneOf_i0_quota"></a>
<a id="Call_parameters_items_i0_oneOf_i0_quota"></a>
###### quota

- Schema name: `Quota`

Maximum disk space this dataset and its children can consume in bytes.
<a id="Call_parameters_items_i0_oneOf_i0_quota_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0_quota_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_oneOf_i0_quota_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1073741824`

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0_quota_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_oneOf_i0_quota_anyOf_i1)

- Type: enum (of integer or null)
###### Must be one of:

- 0
- null

<a id="headingCall_parameters_items_i0_oneOf_i0_refquota"></a>
<a id="Call_parameters_items_i0_oneOf_i0_refquota"></a>
###### refquota

- Schema name: `Refquota`

Maximum disk space this dataset itself can consume in bytes.
<a id="Call_parameters_items_i0_oneOf_i0_refquota_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0_refquota_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_oneOf_i0_refquota_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1073741824`

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0_refquota_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_oneOf_i0_refquota_anyOf_i1)

- Type: enum (of integer or null)
###### Must be one of:

- 0
- null

<a id="headingCall_parameters_items_i0_oneOf_i0_recordsize"></a>
<a id="Call_parameters_items_i0_oneOf_i0_recordsize"></a>
###### recordsize

- Schema name: `Recordsize`
- Type: string

The suggested block size for files in this filesystem dataset.

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1"></a>
###### [PoolDatasetCreateVolume](#tab-pane_Call_parameters_items_i0_oneOf_i1)

- Schema name: `PoolDatasetCreateVolume`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_oneOf_i1_name"></a>
<a id="Call_parameters_items_i0_oneOf_i1_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

The name of the dataset to create.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_oneOf_i1_comments"></a>
<a id="Call_parameters_items_i0_oneOf_i1_comments"></a>
###### comments

- Schema name: `Comments`
- Type: string
- Default: "INHERIT"

Comments or description for the dataset.

<a id="headingCall_parameters_items_i0_oneOf_i1_sync"></a>
<a id="Call_parameters_items_i0_oneOf_i1_sync"></a>
###### sync

- Schema name: `Sync`
- Type: enum (of string)
- Default: "INHERIT"

Synchronous write behavior for the dataset.
###### Must be one of:

- "STANDARD"
- "ALWAYS"
- "DISABLED"
- "INHERIT"

<a id="headingCall_parameters_items_i0_oneOf_i1_snapdev"></a>
<a id="Call_parameters_items_i0_oneOf_i1_snapdev"></a>
###### snapdev

- Schema name: `Snapdev`
- Type: enum (of string)

Controls visibility of volume snapshots under /dev/zvol/.
###### Must be one of:

- "HIDDEN"
- "VISIBLE"
- "INHERIT"

<a id="headingCall_parameters_items_i0_oneOf_i1_compression"></a>
<a id="Call_parameters_items_i0_oneOf_i1_compression"></a>
###### compression

- Schema name: `Compression`
- Type: enum (of string)
- Default: "INHERIT"

Compression algorithm to use for the dataset. Higher numbered variants provide better compression but use more CPU. 'INHERIT' uses the parent dataset's setting.
###### Must be one of:

- "ON"
- "OFF"
- "LZ4"
- "GZIP"
- "GZIP-1"
- "GZIP-9"
- "ZSTD"
- "ZSTD-FAST"
- "ZLE"
- "LZJB"
- "ZSTD-1"
- "ZSTD-2"
- "ZSTD-3"
- "ZSTD-4"
- "ZSTD-5"
- "ZSTD-6"
- "ZSTD-7"
- "ZSTD-8"
- "ZSTD-9"
- "ZSTD-10"
- "ZSTD-11"
- "ZSTD-12"
- "ZSTD-13"
- "ZSTD-14"
- "ZSTD-15"
- "ZSTD-16"
- "ZSTD-17"
- "ZSTD-18"
- "ZSTD-19"
- "ZSTD-FAST-1"
- "ZSTD-FAST-2"
- "ZSTD-FAST-3"
- "ZSTD-FAST-4"
- "ZSTD-FAST-5"
- "ZSTD-FAST-6"
- "ZSTD-FAST-7"
- "ZSTD-FAST-8"
- "ZSTD-FAST-9"
- "ZSTD-FAST-10"
- "ZSTD-FAST-20"
- "ZSTD-FAST-30"
- "ZSTD-FAST-40"
- "ZSTD-FAST-50"
- "ZSTD-FAST-60"
- "ZSTD-FAST-70"
- "ZSTD-FAST-80"
- "ZSTD-FAST-90"
- "ZSTD-FAST-100"
- "ZSTD-FAST-500"
- "ZSTD-FAST-1000"
- "INHERIT"

<a id="headingCall_parameters_items_i0_oneOf_i1_exec"></a>
<a id="Call_parameters_items_i0_oneOf_i1_exec"></a>
###### exec

- Schema name: `Exec`
- Type: enum (of string)
- Default: "INHERIT"

Whether files in this dataset can be executed.
###### Must be one of:

- "ON"
- "OFF"
- "INHERIT"

<a id="headingCall_parameters_items_i0_oneOf_i1_managedby"></a>
<a id="Call_parameters_items_i0_oneOf_i1_managedby"></a>
###### managedby

- Schema name: `Managedby`
- Type: string
- Default: "INHERIT"

Identifies which service or system manages this dataset.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_oneOf_i1_quota_warning"></a>
<a id="Call_parameters_items_i0_oneOf_i1_quota_warning"></a>
###### quota_warning

- Schema name: `Quota Warning`
- Default: "INHERIT"

Percentage of dataset quota at which to issue a warning. 0-100 or 'INHERIT'.
<a id="Call_parameters_items_i0_oneOf_i1_quota_warning_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_quota_warning_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_oneOf_i1_quota_warning_anyOf_i0)

- Type: integer
- Value must be greater or equal to `0` and lesser or equal to `100`

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_quota_warning_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_oneOf_i1_quota_warning_anyOf_i1)

- Type: const
- Specific value: `"INHERIT"`

<a id="headingCall_parameters_items_i0_oneOf_i1_quota_critical"></a>
<a id="Call_parameters_items_i0_oneOf_i1_quota_critical"></a>
###### quota_critical

- Schema name: `Quota Critical`
- Default: "INHERIT"

Percentage of dataset quota at which to issue a critical alert. 0-100 or 'INHERIT'.
<a id="Call_parameters_items_i0_oneOf_i1_quota_critical_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_quota_critical_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_oneOf_i1_quota_critical_anyOf_i0)

- Type: integer
- Value must be greater or equal to `0` and lesser or equal to `100`

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_quota_critical_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_oneOf_i1_quota_critical_anyOf_i1)

- Type: const
- Specific value: `"INHERIT"`

<a id="headingCall_parameters_items_i0_oneOf_i1_refquota_warning"></a>
<a id="Call_parameters_items_i0_oneOf_i1_refquota_warning"></a>
###### refquota_warning

- Schema name: `Refquota Warning`
- Default: "INHERIT"

Percentage of reference quota at which to issue a warning. 0-100 or 'INHERIT'.
<a id="Call_parameters_items_i0_oneOf_i1_refquota_warning_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_refquota_warning_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_oneOf_i1_refquota_warning_anyOf_i0)

- Type: integer
- Value must be greater or equal to `0` and lesser or equal to `100`

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_refquota_warning_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_oneOf_i1_refquota_warning_anyOf_i1)

- Type: const
- Specific value: `"INHERIT"`

<a id="headingCall_parameters_items_i0_oneOf_i1_refquota_critical"></a>
<a id="Call_parameters_items_i0_oneOf_i1_refquota_critical"></a>
###### refquota_critical

- Schema name: `Refquota Critical`
- Default: "INHERIT"

Percentage of reference quota at which to issue a critical alert. 0-100 or 'INHERIT'.
<a id="Call_parameters_items_i0_oneOf_i1_refquota_critical_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_refquota_critical_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_oneOf_i1_refquota_critical_anyOf_i0)

- Type: integer
- Value must be greater or equal to `0` and lesser or equal to `100`

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_refquota_critical_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_oneOf_i1_refquota_critical_anyOf_i1)

- Type: const
- Specific value: `"INHERIT"`

<a id="headingCall_parameters_items_i0_oneOf_i1_reservation"></a>
<a id="Call_parameters_items_i0_oneOf_i1_reservation"></a>
###### reservation

- Schema name: `Reservation`
- Type: integer

Minimum disk space guaranteed to this dataset and its children in bytes.

<a id="headingCall_parameters_items_i0_oneOf_i1_refreservation"></a>
<a id="Call_parameters_items_i0_oneOf_i1_refreservation"></a>
###### refreservation

- Schema name: `Refreservation`
- Type: integer

Minimum disk space guaranteed to this dataset itself in bytes.

<a id="headingCall_parameters_items_i0_oneOf_i1_special_small_block_size"></a>
<a id="Call_parameters_items_i0_oneOf_i1_special_small_block_size"></a>
###### special_small_block_size

- Schema name: `Special Small Block Size`

Size threshold below which blocks are stored on special vdevs in bytes.
<a id="Call_parameters_items_i0_oneOf_i1_special_small_block_size_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_special_small_block_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_oneOf_i1_special_small_block_size_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_special_small_block_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_oneOf_i1_special_small_block_size_anyOf_i1)

- Type: const
- Specific value: `"INHERIT"`

<a id="headingCall_parameters_items_i0_oneOf_i1_copies"></a>
<a id="Call_parameters_items_i0_oneOf_i1_copies"></a>
###### copies

- Schema name: `Copies`
- Default: "INHERIT"

Number of copies of data blocks to maintain for redundancy.
<a id="Call_parameters_items_i0_oneOf_i1_copies_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_copies_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_oneOf_i1_copies_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_copies_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_oneOf_i1_copies_anyOf_i1)

- Type: const
- Specific value: `"INHERIT"`

<a id="headingCall_parameters_items_i0_oneOf_i1_snapdir"></a>
<a id="Call_parameters_items_i0_oneOf_i1_snapdir"></a>
###### snapdir

- Schema name: `Snapdir`
- Type: enum (of string)
- Default: "INHERIT"

Controls visibility of the `.zfs/snapshot` directory. 'DISABLED' hides snapshots, 'VISIBLE' shows them, 'HIDDEN' makes them accessible but not listed.
###### Must be one of:

- "DISABLED"
- "VISIBLE"
- "HIDDEN"
- "INHERIT"

<a id="headingCall_parameters_items_i0_oneOf_i1_deduplication"></a>
<a id="Call_parameters_items_i0_oneOf_i1_deduplication"></a>
###### deduplication

- Schema name: `Deduplication`
- Type: enum (of string)
- Default: "INHERIT"

Deduplication setting. 'ON' enables dedup, 'VERIFY' enables with checksum verification, 'OFF' disables. While ZFS tiering is enabled, cannot be enabled on a dataset in the PERFORMANCE tier (data on the SPECIAL vdev) or on one with a PERFORMANCE-tier descendant that would inherit the setting.
###### Must be one of:

- "ON"
- "VERIFY"
- "OFF"
- "INHERIT"

<a id="headingCall_parameters_items_i0_oneOf_i1_checksum"></a>
<a id="Call_parameters_items_i0_oneOf_i1_checksum"></a>
###### checksum

- Schema name: `Checksum`
- Type: enum (of string)
- Default: "INHERIT"

Checksum algorithm to verify data integrity. Higher security algorithms like SHA256 provide better protection but use more CPU.
###### Must be one of:

- "ON"
- "OFF"
- "FLETCHER2"
- "FLETCHER4"
- "SHA256"
- "SHA512"
- "SKEIN"
- "EDONR"
- "BLAKE3"
- "INHERIT"

<a id="headingCall_parameters_items_i0_oneOf_i1_readonly"></a>
<a id="Call_parameters_items_i0_oneOf_i1_readonly"></a>
###### readonly

- Schema name: `Readonly`
- Type: enum (of string)
- Default: "INHERIT"

Whether the dataset is read-only.
###### Must be one of:

- "ON"
- "OFF"
- "INHERIT"

<a id="headingCall_parameters_items_i0_oneOf_i1_share_type"></a>
<a id="Call_parameters_items_i0_oneOf_i1_share_type"></a>
###### share_type

- Schema name: `Share Type`
- Type: enum (of string)
- Default: "GENERIC"

Optimization type for the dataset based on its intended use.
###### Must be one of:

- "GENERIC"
- "MULTIPROTOCOL"
- "NFS"
- "SMB"
- "APPS"

<a id="headingCall_parameters_items_i0_oneOf_i1_encryption_options"></a>
<a id="Call_parameters_items_i0_oneOf_i1_encryption_options"></a>
###### encryption_options

- Schema name: `PoolCreateEncryptionOptions`
- Type: object

Configuration for encryption of dataset for `name` pool.
- No Additional Properties
<a id="headingCall_parameters_items_i0_oneOf_i1_encryption_options_generate_key"></a>
<a id="Call_parameters_items_i0_oneOf_i1_encryption_options_generate_key"></a>
###### generate_key

- Schema name: `Generate Key`
- Type: boolean
- Default: false

Automatically generate the key to be used for dataset encryption.

<a id="headingCall_parameters_items_i0_oneOf_i1_encryption_options_pbkdf2iters"></a>
<a id="Call_parameters_items_i0_oneOf_i1_encryption_options_pbkdf2iters"></a>
###### pbkdf2iters

- Schema name: `Pbkdf2Iters`
- Type: integer
- Default: 1300000

Number of PBKDF2 iterations for key derivation from passphrase. Higher iterations improve security against brute force attacks but increase unlock time.
- Value must be greater or equal to `1300000`

<a id="headingCall_parameters_items_i0_oneOf_i1_encryption_options_passphrase"></a>
<a id="Call_parameters_items_i0_oneOf_i1_encryption_options_passphrase"></a>
###### passphrase

- Schema name: `Passphrase`
- Default: null

Must be specified if encryption for root dataset is desired with a passphrase as a key.
<a id="Call_parameters_items_i0_oneOf_i1_encryption_options_passphrase_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_encryption_options_passphrase_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_oneOf_i1_encryption_options_passphrase_anyOf_i0)

- Type: string
- Must be at least `8` characters long

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_encryption_options_passphrase_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_oneOf_i1_encryption_options_passphrase_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_oneOf_i1_encryption_options_key"></a>
<a id="Call_parameters_items_i0_oneOf_i1_encryption_options_key"></a>
###### key

- Schema name: `Key`
- Default: null

A hex-encoded key specified as an alternative to using `passphrase`.
<a id="Call_parameters_items_i0_oneOf_i1_encryption_options_key_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_encryption_options_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_oneOf_i1_encryption_options_key_anyOf_i0)

- Type: string
- Must be at least `64` characters long
- Must be at most `64` characters long

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_encryption_options_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_oneOf_i1_encryption_options_key_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_oneOf_i1_encryption"></a>
<a id="Call_parameters_items_i0_oneOf_i1_encryption"></a>
###### encryption

- Schema name: `Encryption`
- Type: boolean
- Default: false

Create a ZFS encrypted root dataset for `name` pool. There is 1 case where ZFS encryption is not allowed for a dataset: 1) If the parent dataset is encrypted with a passphrase and `name` is being created with a key for encrypting the dataset.

<a id="headingCall_parameters_items_i0_oneOf_i1_inherit_encryption"></a>
<a id="Call_parameters_items_i0_oneOf_i1_inherit_encryption"></a>
###### inherit_encryption

- Schema name: `Inherit Encryption`
- Type: boolean
- Default: true

Whether to inherit encryption settings from the parent dataset.

<a id="headingCall_parameters_items_i0_oneOf_i1_user_properties"></a>
<a id="Call_parameters_items_i0_oneOf_i1_user_properties"></a>
###### user_properties

- Schema name: `User Properties`
- Type: array of object
- Default: []

Custom user-defined properties to set on the dataset.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_oneOf_i1_user_properties_items"></a>
###### PoolDatasetCreateUserProperty

- Schema name: `PoolDatasetCreateUserProperty`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_oneOf_i1_user_properties_items_key"></a>
<a id="Call_parameters_items_i0_oneOf_i1_user_properties_items_key"></a>
###### key (required)

- Schema name: `Key`
- Type: string

User property key in namespace:property format.
- Must match regular expression: `.*:.*`
Examples:

```json
"custom:backup_policy"
```
Examples:

```json
"org:created_by"
```

<a id="headingCall_parameters_items_i0_oneOf_i1_user_properties_items_value"></a>
<a id="Call_parameters_items_i0_oneOf_i1_user_properties_items_value"></a>
###### value (required)

- Schema name: `Value`
- Type: string

The value to assign to the user property.

<a id="headingCall_parameters_items_i0_oneOf_i1_create_ancestors"></a>
<a id="Call_parameters_items_i0_oneOf_i1_create_ancestors"></a>
###### create_ancestors

- Schema name: `Create Ancestors`
- Type: boolean
- Default: false

Whether to create any missing parent datasets.

<a id="headingCall_parameters_items_i0_oneOf_i1_type"></a>
<a id="Call_parameters_items_i0_oneOf_i1_type"></a>
###### type

- Schema name: `Type`
- Type: const
- Default: "VOLUME"

Type of dataset to create - volume (zvol).
- Specific value: `"VOLUME"`

<a id="headingCall_parameters_items_i0_oneOf_i1_force_size"></a>
<a id="Call_parameters_items_i0_oneOf_i1_force_size"></a>
###### force_size

- Schema name: `Force Size`
- Type: boolean

Force creation even if the size is not optimal.

<a id="headingCall_parameters_items_i0_oneOf_i1_sparse"></a>
<a id="Call_parameters_items_i0_oneOf_i1_sparse"></a>
###### sparse

- Schema name: `Sparse`
- Type: boolean

Whether to use sparse (thin) provisioning for the volume.

<a id="headingCall_parameters_items_i0_oneOf_i1_volsize"></a>
<a id="Call_parameters_items_i0_oneOf_i1_volsize"></a>
###### volsize (required)

- Schema name: `Volsize`
- Type: integer

The volume size in bytes; supposed to be a multiple of the block size.

<a id="headingCall_parameters_items_i0_oneOf_i1_volblocksize"></a>
<a id="Call_parameters_items_i0_oneOf_i1_volblocksize"></a>
###### volblocksize

- Schema name: `Volblocksize`
- Type: enum (of string)

Defaults to `128K` if the parent pool is a DRAID pool or `16K` otherwise.
###### Must be one of:

- "512"
- "512B"
- "1K"
- "2K"
- "4K"
- "8K"
- "16K"
- "32K"
- "64K"
- "128K"

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `PoolDatasetEntry`
- Type: object

The newly created dataset information.
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

- Schema name: `User Properties`
- Type: object

Custom user-defined ZFS properties set on this dataset as key-value pairs.

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

<a id="headingReturn_value_comments"></a>
<a id="Return_value_comments"></a>
#### comments

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS comments property for storing descriptive text about the dataset.
- No Additional Properties
<a id="headingReturn_value_comments_parsed"></a>
<a id="Return_value_comments_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_comments_rawvalue"></a>
<a id="Return_value_comments_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_comments_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_comments_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_comments_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_comments_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_comments_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_comments_value"></a>
<a id="Return_value_comments_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_comments_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_comments_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_comments_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_comments_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_comments_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_comments_source"></a>
<a id="Return_value_comments_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_comments_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_comments_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_comments_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_comments_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_comments_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_comments_source_info"></a>
<a id="Return_value_comments_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_quota_warning"></a>
<a id="Return_value_quota_warning"></a>
#### quota_warning

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS quota warning threshold property as a percentage.
- No Additional Properties
<a id="headingReturn_value_quota_warning_parsed"></a>
<a id="Return_value_quota_warning_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_quota_warning_rawvalue"></a>
<a id="Return_value_quota_warning_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_quota_warning_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_quota_warning_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_quota_warning_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_quota_warning_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_quota_warning_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_quota_warning_value"></a>
<a id="Return_value_quota_warning_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_quota_warning_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_quota_warning_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_quota_warning_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_quota_warning_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_quota_warning_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_quota_warning_source"></a>
<a id="Return_value_quota_warning_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_quota_warning_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_quota_warning_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_quota_warning_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_quota_warning_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_quota_warning_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_quota_warning_source_info"></a>
<a id="Return_value_quota_warning_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_quota_critical"></a>
<a id="Return_value_quota_critical"></a>
#### quota_critical

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS quota critical threshold property as a percentage.
- No Additional Properties
<a id="headingReturn_value_quota_critical_parsed"></a>
<a id="Return_value_quota_critical_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_quota_critical_rawvalue"></a>
<a id="Return_value_quota_critical_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_quota_critical_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_quota_critical_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_quota_critical_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_quota_critical_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_quota_critical_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_quota_critical_value"></a>
<a id="Return_value_quota_critical_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_quota_critical_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_quota_critical_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_quota_critical_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_quota_critical_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_quota_critical_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_quota_critical_source"></a>
<a id="Return_value_quota_critical_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_quota_critical_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_quota_critical_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_quota_critical_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_quota_critical_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_quota_critical_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_quota_critical_source_info"></a>
<a id="Return_value_quota_critical_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_refquota_warning"></a>
<a id="Return_value_refquota_warning"></a>
#### refquota_warning

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS reference quota warning threshold property as a percentage.
- No Additional Properties
<a id="headingReturn_value_refquota_warning_parsed"></a>
<a id="Return_value_refquota_warning_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_refquota_warning_rawvalue"></a>
<a id="Return_value_refquota_warning_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_refquota_warning_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_refquota_warning_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_refquota_warning_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_refquota_warning_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_refquota_warning_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_refquota_warning_value"></a>
<a id="Return_value_refquota_warning_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_refquota_warning_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_refquota_warning_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_refquota_warning_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_refquota_warning_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_refquota_warning_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_refquota_warning_source"></a>
<a id="Return_value_refquota_warning_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_refquota_warning_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_refquota_warning_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_refquota_warning_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_refquota_warning_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_refquota_warning_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_refquota_warning_source_info"></a>
<a id="Return_value_refquota_warning_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_refquota_critical"></a>
<a id="Return_value_refquota_critical"></a>
#### refquota_critical

- Schema name: `PoolDatasetEntryProperty`
- Type: object

ZFS reference quota critical threshold property as a percentage.
- No Additional Properties
<a id="headingReturn_value_refquota_critical_parsed"></a>
<a id="Return_value_refquota_critical_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_refquota_critical_rawvalue"></a>
<a id="Return_value_refquota_critical_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_refquota_critical_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_refquota_critical_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_refquota_critical_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_refquota_critical_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_refquota_critical_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_refquota_critical_value"></a>
<a id="Return_value_refquota_critical_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_refquota_critical_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_refquota_critical_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_refquota_critical_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_refquota_critical_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_refquota_critical_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_refquota_critical_source"></a>
<a id="Return_value_refquota_critical_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_refquota_critical_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_refquota_critical_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_refquota_critical_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_refquota_critical_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_refquota_critical_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_refquota_critical_source_info"></a>
<a id="Return_value_refquota_critical_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

<a id="headingReturn_value_managedby"></a>
<a id="Return_value_managedby"></a>
#### managedby

- Schema name: `PoolDatasetEntryProperty`
- Type: object

Identifies which service or system manages this dataset.
- No Additional Properties
<a id="headingReturn_value_managedby_parsed"></a>
<a id="Return_value_managedby_parsed"></a>
##### parsed

- Schema name: `Parsed`
- Type: object

The ZFS property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_managedby_rawvalue"></a>
<a id="Return_value_managedby_rawvalue"></a>
##### rawvalue

- Schema name: `Rawvalue`

The raw string value of the ZFS property as stored in the pool. Can be null if not set.
<a id="Return_value_managedby_rawvalue_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_managedby_rawvalue_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_managedby_rawvalue_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_managedby_rawvalue_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_managedby_rawvalue_anyOf_i1)

- Type: null

<a id="headingReturn_value_managedby_value"></a>
<a id="Return_value_managedby_value"></a>
##### value

- Schema name: `Value`

The current effective value of the ZFS property as a string. Can be null if inherited or not set.
<a id="Return_value_managedby_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_managedby_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_managedby_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_managedby_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_managedby_value_anyOf_i1)

- Type: null

<a id="headingReturn_value_managedby_source"></a>
<a id="Return_value_managedby_source"></a>
##### source

- Schema name: `Source`

Indicates where the property value originates from.
<a id="Return_value_managedby_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_managedby_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_managedby_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_managedby_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_managedby_source_anyOf_i1)

- Type: null

Examples:

```json
"LOCAL"
```
Examples:

```json
"INHERITED"
```
Examples:

```json
"DEFAULT"
```

<a id="headingReturn_value_managedby_source_info"></a>
<a id="Return_value_managedby_source_info"></a>
##### source_info

- Schema name: `Source Info`
- Type: object

Additional metadata about the property source, such as the parent dataset for inherited values.

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
