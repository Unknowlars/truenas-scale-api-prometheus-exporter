---
title: zpool.query
kind: event
source_rst: _sources/api_events_zpool.query.rst.txt
source_html: api_events_zpool.query.html
required_roles:
  - POOL_READ
---

# zpool.query

## Summary

Sent on zpool changes.

## Required Roles

- `POOL_READ`

## Schema

- Type: object

### ADDED

- Schema name: `ZPoolQueryAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Database id of the pool.

#### fields (required)

- Schema name: `ZPoolEntry`
- Type: object

Event fields.
- No Additional Properties
##### id

- Schema name: `Id`
- Default: null

Database id from `storage.volume`. `null` for the boot pool and for any pool not present in the database.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### name (required)

- Schema name: `Name`
- Type: string

Name of the zpool.

##### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for the pool.

##### status (required)

- Schema name: `Status`
- Type: string

Current pool status (ONLINE, DEGRADED, FAULTED, OFFLINE, etc.).

##### healthy (required)

- Schema name: `Healthy`
- Type: boolean

Whether the pool is in a healthy state.

##### warning (required)

- Schema name: `Warning`
- Type: boolean

Whether the pool has warning conditions.

##### status_code (required)

- Schema name: `Status Code`

Detailed status code (e.g., OK, ERRATA, FEAT*DISABLED, LOCKED*SED_DISKS).
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### status_detail (required)

- Schema name: `Status Detail`

Human-readable status description.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### is_upgraded

- Schema name: `Is Upgraded`
- Default: null

Whether every ZFS feature flag on the pool is enabled. `null` for OFFLINE pools.
###### Any of

####### Option 1

- Type: boolean

####### Option 2

- Type: null

##### all_sed

- Schema name: `All Sed`
- Default: null

`true` when every disk backing the pool is a Self-Encrypting Drive, `false` when at least one is not. `null` when the SED status of the pool has not yet been determined or does not apply.
###### Any of

####### Option 1

- Type: boolean

####### Option 2

- Type: null

##### properties

- Schema name: `Properties`
- Default: null

Pool properties, keyed by property name.
###### Any of

####### Option 1

- Type: object
######## Additional Properties

Each additional property must conform to the following schema
- Schema name: `ZPoolPropertyValue`
- Type: object
- No Additional Properties
######### raw (required)

- Schema name: `Raw`
- Type: string

The raw string representation of the property.

######### source (required)

- Schema name: `Source`

The source from where this property received its value (DEFAULT, LOCAL, NONE, etc.).
########## Any of

########### Option 1

- Type: string

########### Option 2

- Type: null

######### value (required)

- Schema name: `Value`

The native Python value of the property.
########## Any of

########### Option 1

- Type: integer

########### Option 2

- Type: number

########### Option 3

- Type: string

########### Option 4

- Type: boolean

########### Option 5

- Type: null

####### Option 2

- Type: string

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: number

####### Option 2

- Type: string

####### Option 3

- Type: boolean

####### Option 4

- Type: null

####### Option 5

- Type: null

##### topology

- Default: null

Pool vdev topology.
###### Any of

####### ZPoolTopology

- Schema name: `ZPoolTopology`
- Type: object
- No Additional Properties
######## data (required)

- Schema name: `Data`
- Type: array of object

Array of data vdev configurations.
- No Additional Items

######### Each item of this array must be:

######### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
########## name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

########## vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

########## guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

########## state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

########## stats (required)

- Schema name: `ZPoolVdevStats`
- Type: object

Vdev I/O statistics.
- No Additional Properties
########### timestamp

- Schema name: `Timestamp`
- Type: integer
- Default: 0

High-resolution timestamp (nanoseconds).

########### allocated

- Schema name: `Allocated`
- Type: integer
- Default: 0

Allocated space in bytes.

########### space

- Schema name: `Space`
- Type: integer
- Default: 0

Total space in bytes.

########### dspace

- Schema name: `Dspace`
- Type: integer
- Default: 0

Deflated (compressed) space.

########### pspace

- Schema name: `Pspace`
- Type: integer
- Default: 0

Physical space.

########### rsize

- Schema name: `Rsize`
- Type: integer
- Default: 0

Replaceable dev size.

########### esize

- Schema name: `Esize`
- Type: integer
- Default: 0

Expandable dev size.

########### read_errors

- Schema name: `Read Errors`
- Type: integer
- Default: 0

Number of read errors.

########### write_errors

- Schema name: `Write Errors`
- Type: integer
- Default: 0

Number of write errors.

########### checksum_errors

- Schema name: `Checksum Errors`
- Type: integer
- Default: 0

Number of checksum errors.

########### initialize_errors

- Schema name: `Initialize Errors`
- Type: integer
- Default: 0

Number of initialize errors.

########### dio_verify_errors

- Schema name: `Dio Verify Errors`
- Type: integer
- Default: 0

Number of direct I/O verify errors.

########### slow_ios

- Schema name: `Slow Ios`
- Default: null

Number of slow I/Os.
############ Any of

############# Option 1

- Type: integer

############# Option 2

- Type: null

########### self_healed_bytes

- Schema name: `Self Healed Bytes`
- Type: integer
- Default: 0

Self-healed bytes.

########### fragmentation

- Schema name: `Fragmentation`
- Type: integer
- Default: 0

Fragmentation percentage.

########### scan_processed

- Schema name: `Scan Processed`
- Type: integer
- Default: 0

Bytes processed by scan.

########### scan_removing

- Schema name: `Scan Removing`
- Type: integer
- Default: 0

Bytes processed by removal.

########### rebuild_processed

- Schema name: `Rebuild Processed`
- Type: integer
- Default: 0

Bytes processed by rebuild.

########### noalloc

- Schema name: `Noalloc`
- Type: integer
- Default: 0

Allocations halted.

########### ops_read

- Schema name: `Ops Read`
- Type: integer
- Default: 0

Read operations.

########### ops_write

- Schema name: `Ops Write`
- Type: integer
- Default: 0

Write operations.

########### bytes_read

- Schema name: `Bytes Read`
- Type: integer
- Default: 0

Bytes read.

########### bytes_write

- Schema name: `Bytes Write`
- Type: integer
- Default: 0

Bytes written.

########### configured_ashift

- Schema name: `Configured Ashift`
- Default: null

Configured ashift value.
############ Any of

############# Option 1

- Type: integer

############# Option 2

- Type: null

########### logical_ashift

- Schema name: `Logical Ashift`
- Default: null

Logical ashift value.
############ Any of

############# Option 1

- Type: integer

############# Option 2

- Type: null

########### physical_ashift

- Schema name: `Physical Ashift`
- Default: null

Physical ashift value.
############ Any of

############# Option 1

- Type: integer

############# Option 2

- Type: null

########## children (required)

- Schema name: `Children`
- Type: array of object

Child vdevs.
- No Additional Items

########### Each item of this array must be:

########### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
############ name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

############ vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

############ guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

############ state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

############ stats (required)

- Type: object

Vdev I/O statistics.

############ children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

############# Each item of this array must be:

- Type: object

############ top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
############# Any of

############## Option 1

- Type: integer

############## Option 2

- Type: null

########## top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
########### Any of

############ Option 1

- Type: integer

############ Option 2

- Type: null

######## log (required)

- Schema name: `Log`
- Type: array of object

Array of ZFS Intent Log (ZIL) vdev configurations.
- No Additional Items

######### Each item of this array must be:

######### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
########## name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

########## vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

########## guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

########## state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

########## stats (required)

- Type: object

Vdev I/O statistics.

########## children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

########### Each item of this array must be:

- Type: object

########## top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
########### Any of

############ Option 1

- Type: integer

############ Option 2

- Type: null

######## cache (required)

- Schema name: `Cache`
- Type: array of object

Array of L2ARC cache vdev configurations.
- No Additional Items

######### Each item of this array must be:

######### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
########## name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

########## vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

########## guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

########## state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

########## stats (required)

- Type: object

Vdev I/O statistics.

########## children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

########### Each item of this array must be:

- Type: object

########## top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
########### Any of

############ Option 1

- Type: integer

############ Option 2

- Type: null

######## spares (required)

- Schema name: `Spares`
- Type: array of object

Array of spare disk configurations.
- No Additional Items

######### Each item of this array must be:

######### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
########## name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

########## vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

########## guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

########## state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

########## stats (required)

- Type: object

Vdev I/O statistics.

########## children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

########### Each item of this array must be:

- Type: object

########## top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
########### Any of

############ Option 1

- Type: integer

############ Option 2

- Type: null

######## special (required)

- Schema name: `Special`
- Type: array of object

Array of special vdev configurations for metadata.
- No Additional Items

######### Each item of this array must be:

######### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
########## name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

########## vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

########## guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

########## state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

########## stats (required)

- Type: object

Vdev I/O statistics.

########## children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

########### Each item of this array must be:

- Type: object

########## top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
########### Any of

############ Option 1

- Type: integer

############ Option 2

- Type: null

######## dedup (required)

- Schema name: `Dedup`
- Type: array of object

Array of deduplication table vdev configurations.
- No Additional Items

######### Each item of this array must be:

######### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
########## name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

########## vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

########## guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

########## state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

########## stats (required)

- Type: object

Vdev I/O statistics.

########## children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

########### Each item of this array must be:

- Type: object

########## top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
########### Any of

############ Option 1

- Type: integer

############ Option 2

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: null

##### scan

- Default: null

Most recent scrub or resilver information.
###### Any of

####### ZPoolScan

- Schema name: `ZPoolScan`
- Type: object
- No Additional Properties
######## function (required)

- Schema name: `Function`
- Type: enum (of string)

Type of ZFS pool scan.

######## state (required)

- Schema name: `State`
- Type: enum (of string)

Current lifecycle state of the scan.

######## start_time (required)

- Schema name: `Start Time`
- Type: integer

Scan start time (unix timestamp).

######## end_time (required)

- Schema name: `End Time`

Scan end time as unix timestamp (`null` while the scan is still running).
######### Any of

########## Option 1

- Type: integer

########## Option 2

- Type: null

######## percentage (required)

- Schema name: `Percentage`
- Type: number

Scan progress (between 0 and 100%).

######## bytes_to_process (required)

- Schema name: `Bytes To Process`
- Type: integer

Total bytes located by scanner.

######## bytes_processed (required)

- Schema name: `Bytes Processed`
- Type: integer

Total bytes to scan.

######## bytes_issued (required)

- Schema name: `Bytes Issued`
- Type: integer

Issued bytes per scan pass.

######## pause (required)

- Schema name: `Pause`

Pause time as unix timestamp (`null` if the scan is not paused).
######### Any of

########## Option 1

- Type: integer

########## Option 2

- Type: null

######## errors (required)

- Schema name: `Errors`
- Type: integer

Number of scan errors.

######## total_secs_left (required)

- Schema name: `Total Secs Left`

Number of seconds left (`null` if the scan is not running).
######### Any of

########## Option 1

- Type: integer

########## Option 2

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: null

##### expand

- Default: null

RAIDZ expansion information.
###### Any of

####### ZPoolExpand

- Schema name: `ZPoolExpand`
- Type: object
- No Additional Properties
######## state (required)

- Schema name: `State`
- Type: string

Expansion state (e.g., SCANNING, FINISHED).

######## expanding_vdev (required)

- Schema name: `Expanding Vdev`
- Type: integer

Index of the vdev being expanded.

######## start_time (required)

- Schema name: `Start Time`
- Type: integer

Expansion start time (unix timestamp).

######## end_time (required)

- Schema name: `End Time`

Expansion end time as unix timestamp (`null` while expanding).
######### Any of

########## Option 1

- Type: integer

########## Option 2

- Type: null

######## bytes_to_reflow (required)

- Schema name: `Bytes To Reflow`
- Type: integer

Total bytes that need to be reflowed.

######## bytes_reflowed (required)

- Schema name: `Bytes Reflowed`
- Type: integer

Total bytes reflowed so far.

######## waiting_for_resilver (required)

- Schema name: `Waiting For Resilver`
- Type: integer

Non-zero if expansion is waiting for a resilver to complete.

######## total_secs_left (required)

- Schema name: `Total Secs Left`

Estimated seconds remaining (`null` if not expanding).
######### Any of

########## Option 1

- Type: integer

########## Option 2

- Type: null

######## percentage (required)

- Schema name: `Percentage`
- Type: number

Expansion progress (between 0 and 100%).

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: null

##### features

- Schema name: `Features`
- Default: null

Pool feature flags.
###### Any of

####### Option 1

- Type: array of object
- No Additional Items

######## Each item of this array must be:

######## ZPoolFeature

- Schema name: `ZPoolFeature`
- Type: object
- No Additional Properties
######### name (required)

- Schema name: `Name`
- Type: string

Feature name.

######### guid (required)

- Schema name: `Guid`
- Type: string

Feature GUID.

######### description (required)

- Schema name: `Description`
- Type: string

Feature description.

######### state (required)

- Schema name: `State`
- Type: string

Feature state.

####### Option 2

- Type: null

### CHANGED

- Schema name: `ZPoolQueryChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Database id of the pool.

#### fields (required)

- Schema name: `ZPoolEntry`
- Type: object

Event fields.
- No Additional Properties
##### id

- Schema name: `Id`
- Default: null

Database id from `storage.volume`. `null` for the boot pool and for any pool not present in the database.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### name (required)

- Schema name: `Name`
- Type: string

Name of the zpool.

##### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for the pool.

##### status (required)

- Schema name: `Status`
- Type: string

Current pool status (ONLINE, DEGRADED, FAULTED, OFFLINE, etc.).

##### healthy (required)

- Schema name: `Healthy`
- Type: boolean

Whether the pool is in a healthy state.

##### warning (required)

- Schema name: `Warning`
- Type: boolean

Whether the pool has warning conditions.

##### status_code (required)

- Schema name: `Status Code`

Detailed status code (e.g., OK, ERRATA, FEAT*DISABLED, LOCKED*SED_DISKS).
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### status_detail (required)

- Schema name: `Status Detail`

Human-readable status description.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### is_upgraded

- Schema name: `Is Upgraded`
- Default: null

Whether every ZFS feature flag on the pool is enabled. `null` for OFFLINE pools.
###### Any of

####### Option 1

- Type: boolean

####### Option 2

- Type: null

##### all_sed

- Schema name: `All Sed`
- Default: null

`true` when every disk backing the pool is a Self-Encrypting Drive, `false` when at least one is not. `null` when the SED status of the pool has not yet been determined or does not apply.
###### Any of

####### Option 1

- Type: boolean

####### Option 2

- Type: null

##### properties

- Schema name: `Properties`
- Default: null

Pool properties, keyed by property name.
###### Any of

####### Option 1

- Type: object
######## Additional Properties

Each additional property must conform to the following schema
- Schema name: `ZPoolPropertyValue`
- Type: object
- No Additional Properties
######### raw (required)

- Schema name: `Raw`
- Type: string

The raw string representation of the property.

######### source (required)

- Schema name: `Source`

The source from where this property received its value (DEFAULT, LOCAL, NONE, etc.).
########## Any of

########### Option 1

- Type: string

########### Option 2

- Type: null

######### value (required)

- Schema name: `Value`

The native Python value of the property.
########## Any of

########### Option 1

- Type: integer

########### Option 2

- Type: number

########### Option 3

- Type: string

########### Option 4

- Type: boolean

########### Option 5

- Type: null

####### Option 2

- Type: string

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: number

####### Option 2

- Type: string

####### Option 3

- Type: boolean

####### Option 4

- Type: null

####### Option 5

- Type: null

##### topology

- Default: null

Pool vdev topology.
###### Any of

####### ZPoolTopology

- Schema name: `ZPoolTopology`
- Type: object
- No Additional Properties
######## data (required)

- Schema name: `Data`
- Type: array of object

Array of data vdev configurations.
- No Additional Items

######### Each item of this array must be:

######### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
########## name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

########## vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

########## guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

########## state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

########## stats (required)

- Schema name: `ZPoolVdevStats`
- Type: object

Vdev I/O statistics.
- No Additional Properties
########### timestamp

- Schema name: `Timestamp`
- Type: integer
- Default: 0

High-resolution timestamp (nanoseconds).

########### allocated

- Schema name: `Allocated`
- Type: integer
- Default: 0

Allocated space in bytes.

########### space

- Schema name: `Space`
- Type: integer
- Default: 0

Total space in bytes.

########### dspace

- Schema name: `Dspace`
- Type: integer
- Default: 0

Deflated (compressed) space.

########### pspace

- Schema name: `Pspace`
- Type: integer
- Default: 0

Physical space.

########### rsize

- Schema name: `Rsize`
- Type: integer
- Default: 0

Replaceable dev size.

########### esize

- Schema name: `Esize`
- Type: integer
- Default: 0

Expandable dev size.

########### read_errors

- Schema name: `Read Errors`
- Type: integer
- Default: 0

Number of read errors.

########### write_errors

- Schema name: `Write Errors`
- Type: integer
- Default: 0

Number of write errors.

########### checksum_errors

- Schema name: `Checksum Errors`
- Type: integer
- Default: 0

Number of checksum errors.

########### initialize_errors

- Schema name: `Initialize Errors`
- Type: integer
- Default: 0

Number of initialize errors.

########### dio_verify_errors

- Schema name: `Dio Verify Errors`
- Type: integer
- Default: 0

Number of direct I/O verify errors.

########### slow_ios

- Schema name: `Slow Ios`
- Default: null

Number of slow I/Os.
############ Any of

############# Option 1

- Type: integer

############# Option 2

- Type: null

########### self_healed_bytes

- Schema name: `Self Healed Bytes`
- Type: integer
- Default: 0

Self-healed bytes.

########### fragmentation

- Schema name: `Fragmentation`
- Type: integer
- Default: 0

Fragmentation percentage.

########### scan_processed

- Schema name: `Scan Processed`
- Type: integer
- Default: 0

Bytes processed by scan.

########### scan_removing

- Schema name: `Scan Removing`
- Type: integer
- Default: 0

Bytes processed by removal.

########### rebuild_processed

- Schema name: `Rebuild Processed`
- Type: integer
- Default: 0

Bytes processed by rebuild.

########### noalloc

- Schema name: `Noalloc`
- Type: integer
- Default: 0

Allocations halted.

########### ops_read

- Schema name: `Ops Read`
- Type: integer
- Default: 0

Read operations.

########### ops_write

- Schema name: `Ops Write`
- Type: integer
- Default: 0

Write operations.

########### bytes_read

- Schema name: `Bytes Read`
- Type: integer
- Default: 0

Bytes read.

########### bytes_write

- Schema name: `Bytes Write`
- Type: integer
- Default: 0

Bytes written.

########### configured_ashift

- Schema name: `Configured Ashift`
- Default: null

Configured ashift value.
############ Any of

############# Option 1

- Type: integer

############# Option 2

- Type: null

########### logical_ashift

- Schema name: `Logical Ashift`
- Default: null

Logical ashift value.
############ Any of

############# Option 1

- Type: integer

############# Option 2

- Type: null

########### physical_ashift

- Schema name: `Physical Ashift`
- Default: null

Physical ashift value.
############ Any of

############# Option 1

- Type: integer

############# Option 2

- Type: null

########## children (required)

- Schema name: `Children`
- Type: array of object

Child vdevs.
- No Additional Items

########### Each item of this array must be:

########### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
############ name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

############ vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

############ guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

############ state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

############ stats (required)

- Type: object

Vdev I/O statistics.

############ children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

############# Each item of this array must be:

- Type: object

############ top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
############# Any of

############## Option 1

- Type: integer

############## Option 2

- Type: null

########## top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
########### Any of

############ Option 1

- Type: integer

############ Option 2

- Type: null

######## log (required)

- Schema name: `Log`
- Type: array of object

Array of ZFS Intent Log (ZIL) vdev configurations.
- No Additional Items

######### Each item of this array must be:

######### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
########## name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

########## vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

########## guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

########## state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

########## stats (required)

- Type: object

Vdev I/O statistics.

########## children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

########### Each item of this array must be:

- Type: object

########## top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
########### Any of

############ Option 1

- Type: integer

############ Option 2

- Type: null

######## cache (required)

- Schema name: `Cache`
- Type: array of object

Array of L2ARC cache vdev configurations.
- No Additional Items

######### Each item of this array must be:

######### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
########## name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

########## vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

########## guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

########## state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

########## stats (required)

- Type: object

Vdev I/O statistics.

########## children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

########### Each item of this array must be:

- Type: object

########## top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
########### Any of

############ Option 1

- Type: integer

############ Option 2

- Type: null

######## spares (required)

- Schema name: `Spares`
- Type: array of object

Array of spare disk configurations.
- No Additional Items

######### Each item of this array must be:

######### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
########## name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

########## vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

########## guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

########## state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

########## stats (required)

- Type: object

Vdev I/O statistics.

########## children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

########### Each item of this array must be:

- Type: object

########## top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
########### Any of

############ Option 1

- Type: integer

############ Option 2

- Type: null

######## special (required)

- Schema name: `Special`
- Type: array of object

Array of special vdev configurations for metadata.
- No Additional Items

######### Each item of this array must be:

######### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
########## name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

########## vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

########## guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

########## state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

########## stats (required)

- Type: object

Vdev I/O statistics.

########## children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

########### Each item of this array must be:

- Type: object

########## top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
########### Any of

############ Option 1

- Type: integer

############ Option 2

- Type: null

######## dedup (required)

- Schema name: `Dedup`
- Type: array of object

Array of deduplication table vdev configurations.
- No Additional Items

######### Each item of this array must be:

######### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
########## name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

########## vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

########## guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

########## state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

########## stats (required)

- Type: object

Vdev I/O statistics.

########## children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

########### Each item of this array must be:

- Type: object

########## top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
########### Any of

############ Option 1

- Type: integer

############ Option 2

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: null

##### scan

- Default: null

Most recent scrub or resilver information.
###### Any of

####### ZPoolScan

- Schema name: `ZPoolScan`
- Type: object
- No Additional Properties
######## function (required)

- Schema name: `Function`
- Type: enum (of string)

Type of ZFS pool scan.

######## state (required)

- Schema name: `State`
- Type: enum (of string)

Current lifecycle state of the scan.

######## start_time (required)

- Schema name: `Start Time`
- Type: integer

Scan start time (unix timestamp).

######## end_time (required)

- Schema name: `End Time`

Scan end time as unix timestamp (`null` while the scan is still running).
######### Any of

########## Option 1

- Type: integer

########## Option 2

- Type: null

######## percentage (required)

- Schema name: `Percentage`
- Type: number

Scan progress (between 0 and 100%).

######## bytes_to_process (required)

- Schema name: `Bytes To Process`
- Type: integer

Total bytes located by scanner.

######## bytes_processed (required)

- Schema name: `Bytes Processed`
- Type: integer

Total bytes to scan.

######## bytes_issued (required)

- Schema name: `Bytes Issued`
- Type: integer

Issued bytes per scan pass.

######## pause (required)

- Schema name: `Pause`

Pause time as unix timestamp (`null` if the scan is not paused).
######### Any of

########## Option 1

- Type: integer

########## Option 2

- Type: null

######## errors (required)

- Schema name: `Errors`
- Type: integer

Number of scan errors.

######## total_secs_left (required)

- Schema name: `Total Secs Left`

Number of seconds left (`null` if the scan is not running).
######### Any of

########## Option 1

- Type: integer

########## Option 2

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: null

##### expand

- Default: null

RAIDZ expansion information.
###### Any of

####### ZPoolExpand

- Schema name: `ZPoolExpand`
- Type: object
- No Additional Properties
######## state (required)

- Schema name: `State`
- Type: string

Expansion state (e.g., SCANNING, FINISHED).

######## expanding_vdev (required)

- Schema name: `Expanding Vdev`
- Type: integer

Index of the vdev being expanded.

######## start_time (required)

- Schema name: `Start Time`
- Type: integer

Expansion start time (unix timestamp).

######## end_time (required)

- Schema name: `End Time`

Expansion end time as unix timestamp (`null` while expanding).
######### Any of

########## Option 1

- Type: integer

########## Option 2

- Type: null

######## bytes_to_reflow (required)

- Schema name: `Bytes To Reflow`
- Type: integer

Total bytes that need to be reflowed.

######## bytes_reflowed (required)

- Schema name: `Bytes Reflowed`
- Type: integer

Total bytes reflowed so far.

######## waiting_for_resilver (required)

- Schema name: `Waiting For Resilver`
- Type: integer

Non-zero if expansion is waiting for a resilver to complete.

######## total_secs_left (required)

- Schema name: `Total Secs Left`

Estimated seconds remaining (`null` if not expanding).
######### Any of

########## Option 1

- Type: integer

########## Option 2

- Type: null

######## percentage (required)

- Schema name: `Percentage`
- Type: number

Expansion progress (between 0 and 100%).

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: null

##### features

- Schema name: `Features`
- Default: null

Pool feature flags.
###### Any of

####### Option 1

- Type: array of object
- No Additional Items

######## Each item of this array must be:

######## ZPoolFeature

- Schema name: `ZPoolFeature`
- Type: object
- No Additional Properties
######### name (required)

- Schema name: `Name`
- Type: string

Feature name.

######### guid (required)

- Schema name: `Guid`
- Type: string

Feature GUID.

######### description (required)

- Schema name: `Description`
- Type: string

Feature description.

######### state (required)

- Schema name: `State`
- Type: string

Feature state.

####### Option 2

- Type: null

### REMOVED

- Schema name: `ZPoolQueryRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Database id of the pool.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
