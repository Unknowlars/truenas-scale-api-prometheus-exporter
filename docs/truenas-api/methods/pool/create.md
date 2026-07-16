---
title: pool.create
kind: method
source_rst: _sources/api_methods_pool.create.rst.txt
source_html: api_methods_pool.create.html
required_roles:
  - POOL_WRITE
---

# pool.create

## Summary

Create a new ZFS Pool.

.. examples(websocket)::

Create a pool named "tank", raidz1 with 3 disks, 1 cache disk, 1 ZIL/log disk and 1 hot spare disk.

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "pool.create", "params": [{ "name": "tank", "topology": { "data": [ {"type": "RAIDZ1", "disks": ["da1", "da2", "da3"]} ], "cache": [ {"type": "STRIPE", "disks": ["da4"]} ], "log": [ {"type": "RAIDZ1", "disks": ["da5"]} ], "spares": ["da6"] } }] }

This method is a job.

## Required Roles

- `POOL_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`
- Type: object

Configuration for creating a new storage pool.
- No Additional Properties
##### name (required)

- Schema name: `Name`
- Type: string

Name for the new storage pool.
- Must be at least `1` characters long
- Must be at most `50` characters long

##### encryption

- Schema name: `Encryption`
- Type: boolean
- Default: false

If set, create a ZFS encrypted root dataset for this pool.

##### dedup_table_quota

- Schema name: `Dedup Table Quota`
- Type: enum (of null or string)
- Default: "AUTO"

How to manage the deduplication table quota allocation.

##### dedup_table_quota_value

- Schema name: `Dedup Table Quota Value`
- Default: null

Custom quota value in bytes when `dedup_table_quota` is set to CUSTOM.
###### Any of

####### Option 1

- Type: integer
- Value must be strictly greater than `0`

####### Option 2

- Type: null

##### deduplication

- Schema name: `Deduplication`
- Type: enum (of null or string)
- Default: null

Make sure no block of data is duplicated in the pool. If set to `VERIFY` and two blocks have similar signatures, byte-to-byte comparison is performed to ensure that the blcoks are identical. This should be used in special circumstances as it carries a significant overhead.

##### checksum

- Schema name: `Checksum`
- Type: enum (of null or string)
- Default: null

Checksum algorithm to use for data integrity verification.

##### encryption_options

- Schema name: `PoolCreateEncryptionOptions`
- Type: object

Specify configuration for encryption of root dataset.
- No Additional Properties
###### generate_key

- Schema name: `Generate Key`
- Type: boolean
- Default: false

Automatically generate the key to be used for dataset encryption.

###### pbkdf2iters

- Schema name: `Pbkdf2Iters`
- Type: integer
- Default: 350000

Number of PBKDF2 iterations for key derivation from passphrase. Higher iterations improve security against brute force attacks but increase unlock time. Default 350,000 balances security and performance.
- Value must be greater or equal to `100000`

###### algorithm

- Schema name: `Algorithm`
- Type: enum (of string)
- Default: "AES-256-GCM"

Encryption algorithm to use for dataset encryption.

###### passphrase

- Schema name: `Passphrase`
- Default: null

Must be specified if encryption for root dataset is desired with a passphrase as a key.
####### Any of

######## Option 1

- Type: string
- Must be at least `8` characters long

######## Option 2

- Type: null

###### key

- Schema name: `Key`
- Default: null

A hex-encoded key specified as an alternative to using `passphrase`.
####### Any of

######## Option 1

- Type: string
- Must be at least `64` characters long
- Must be at most `64` characters long

######## Option 2

- Type: null

##### topology (required)

- Schema name: `PoolCreateTopology`
- Type: object

Physical layout and configuration of vdevs in the pool.
- No Additional Properties
Examples:

```json
{
    "cache": [
        {
            "disks": [
                "da4"
            ],
            "type": "STRIPE"
        }
    ],
    "data": [
        {
            "disks": [
                "da1",
                "da2",
                "da3"
            ],
            "type": "RAIDZ1"
        }
    ],
    "log": [
        {
            "disks": [
                "da5"
            ],
            "type": "STRIPE"
        }
    ],
    "spares": [
        "da6"
    ]
}
```
###### data (required)

- Schema name: `Data`
- Type: array

All vdevs must be of the same `type`.
- Must contain a minimum of `1` items
- No Additional Items

####### Each item of this array must be:

###### special

- Schema name: `Special`
- Type: array of object
- Default: []

Array of special vdev configurations for metadata storage.
- No Additional Items

####### Each item of this array must be:

####### PoolCreateTopologySpecialVdev

- Schema name: `PoolCreateTopologySpecialVdev`
- Type: object
- No Additional Properties
######## type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of special vdev configuration for metadata storage.

######## disks (required)

- Schema name: `Disks`
- Type: array of string

Array of disk names to use in this special vdev.
- No Additional Items

######### Each item of this array must be:

- Type: string

###### dedup

- Schema name: `Dedup`
- Type: array of object
- Default: []

Array of deduplication table vdev configurations.
- No Additional Items

####### Each item of this array must be:

####### PoolCreateTopologyDedupVdev

- Schema name: `PoolCreateTopologyDedupVdev`
- Type: object
- No Additional Properties
######## type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of deduplication table vdev configuration.

######## disks (required)

- Schema name: `Disks`
- Type: array of string

Array of disk names to use in this dedup vdev.
- No Additional Items

######### Each item of this array must be:

- Type: string

###### cache

- Schema name: `Cache`
- Type: array of object
- Default: []

Array of L2ARC cache vdev configurations.
- No Additional Items

####### Each item of this array must be:

####### PoolCreateTopologyCacheVdev

- Schema name: `PoolCreateTopologyCacheVdev`
- Type: object
- No Additional Properties
######## type (required)

- Schema name: `Type`
- Type: const

Type of L2ARC cache vdev configuration (always stripe).

######## disks (required)

- Schema name: `Disks`
- Type: array of string

Array of disk names to use in this cache vdev.
- No Additional Items

######### Each item of this array must be:

- Type: string

###### log

- Schema name: `Log`
- Type: array of object
- Default: []

Array of ZFS Intent Log (ZIL) vdev configurations.
- No Additional Items

####### Each item of this array must be:

####### PoolCreateTopologyLogVdev

- Schema name: `PoolCreateTopologyLogVdev`
- Type: object
- No Additional Properties
######## type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of ZFS Intent Log (ZIL) vdev configuration.

######## disks (required)

- Schema name: `Disks`
- Type: array of string

Array of disk names to use in this log vdev.
- No Additional Items

######### Each item of this array must be:

- Type: string

###### spares

- Schema name: `Spares`
- Type: array of string
- Default: []

Array of spare disk names for the pool.
- No Additional Items

####### Each item of this array must be:

- Type: string

##### allow_duplicate_serials

- Schema name: `Allow Duplicate Serials`
- Type: boolean
- Default: false

Whether to allow disks with duplicate serial numbers in the pool.

### Return value

- Schema name: `PoolEntry`
- Type: object

Information about the newly created pool.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this storage pool.

#### name (required)

- Schema name: `Name`
- Type: string

Name of the storage pool.

#### guid (required)

- Schema name: `Guid`
- Type: string

Globally unique identifier (GUID) for this pool.

#### status (required)

- Schema name: `Status`
- Type: string

Current status of the pool.
Examples:

```json
"ONLINE"
```
Examples:

```json
"DEGRADED"
```
Examples:

```json
"FAULTED"
```

#### path (required)

- Schema name: `Path`
- Type: string

Filesystem path where the pool is mounted.

#### scan (required)

- Schema name: `Scan`

Information about any active scrub or resilver operation. `null` if no operation is running.
##### Any of

###### Option 1

- Type: object
Examples:

```json
{
    "bytes_issued": null,
    "bytes_processed": null,
    "bytes_to_process": null,
    "end_time": null,
    "errors": null,
    "function": null,
    "pause": null,
    "percentage": null,
    "start_time": null,
    "state": null,
    "total_secs_left": null
}
```

###### Option 2

- Type: null

#### expand (required)

- Schema name: `Expand`

Information about any active pool expansion operation. `null` if no expansion is running.
##### Any of

###### Option 1

- Type: object
Examples:

```json
{
    "bytes_reflowed": 978944,
    "bytes_to_reflow": 835584,
    "end_time": null,
    "expanding_vdev": 0,
    "percentage": 85.35564853556485,
    "start_time": null,
    "state": "FINISHED",
    "total_secs_left": null,
    "waiting_for_resilver": 0
}
```

###### Option 2

- Type: null

#### is_upgraded

- Schema name: `Is Upgraded`
- Type: boolean
- Default: false

Whether this pool has been upgraded to the latest feature flags.

#### healthy (required)

- Schema name: `Healthy`
- Type: boolean

Whether the pool is in a healthy state with no errors or warnings.

#### warning (required)

- Schema name: `Warning`
- Type: boolean

Whether the pool has warning conditions that require attention.

#### status_code (required)

- Schema name: `Status Code`

Detailed status code for the pool condition. `null` if not applicable.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### status_detail (required)

- Schema name: `Status Detail`

Human-readable description of the pool status. `null` if not available.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### size (required)

- Schema name: `Size`

Total size of the pool in bytes. `null` if not available.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### allocated (required)

- Schema name: `Allocated`

Amount of space currently allocated in the pool in bytes. `null` if not available.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### free (required)

- Schema name: `Free`

Amount of free space available in the pool in bytes. `null` if not available.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### freeing (required)

- Schema name: `Freeing`

Amount of space being freed (in bytes) by ongoing operations. `null` if not available.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### dedup_table_size (required)

- Schema name: `Dedup Table Size`

Size of the deduplication table in bytes. `null` if deduplication is not enabled.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### dedup_table_quota (required)

- Schema name: `Dedup Table Quota`

Quota limit for the deduplication table. `null` if no quota is set.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### fragmentation (required)

- Schema name: `Fragmentation`

Percentage of pool fragmentation as a string. `null` if not available.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### size_str (required)

- Schema name: `Size Str`

Human-readable string representation of the pool size. `null` if not available.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### allocated_str (required)

- Schema name: `Allocated Str`

Human-readable string representation of allocated space. `null` if not available.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### free_str (required)

- Schema name: `Free Str`

Human-readable string representation of free space. `null` if not available.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### freeing_str (required)

- Schema name: `Freeing Str`

Human-readable string representation of space being freed. `null` if not available.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### autotrim (required)

- Schema name: `Autotrim`
- Type: object

Auto-trim configuration for the pool indicating whether automatic TRIM operations are enabled.
Examples:

```json
{
    "parsed": "off",
    "rawvalue": "off",
    "source": "DEFAULT",
    "value": "off"
}
```

#### topology (required)

Physical topology and structure of the pool including vdevs. `null` if not available.
##### Any of

###### PoolTopology

- Schema name: `PoolTopology`
- Type: object
- No Additional Properties
####### data (required)

- Schema name: `Data`
- Type: array

Array of data vdev configurations in the pool.
- No Additional Items

######## Each item of this array must be:

- Type: object

####### log (required)

- Schema name: `Log`
- Type: array

Array of ZFS Intent Log (ZIL) vdev configurations.
- No Additional Items

######## Each item of this array must be:

- Type: object

####### cache (required)

- Schema name: `Cache`
- Type: array

Array of L2ARC cache vdev configurations.
- No Additional Items

######## Each item of this array must be:

- Type: object

####### spare (required)

- Schema name: `Spare`
- Type: array

Array of spare disk configurations.
- No Additional Items

######## Each item of this array must be:

- Type: object

####### special (required)

- Schema name: `Special`
- Type: array

Array of special vdev configurations for metadata.
- No Additional Items

######## Each item of this array must be:

- Type: object

####### dedup (required)

- Schema name: `Dedup`
- Type: array

Array of deduplication table vdev configurations.
- No Additional Items

######## Each item of this array must be:

- Type: object

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
