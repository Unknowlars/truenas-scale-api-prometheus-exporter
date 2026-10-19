---
title: zpool.query
kind: method
source_rst: _sources/api_methods_zpool.query.rst.txt
source_html: api_methods_zpool.query.html
required_roles:
  - POOL_READ
---

# zpool.query

## Summary

Query ZFS pools with flexible options for properties, topology, scan, and features.

Returns information about both imported and non-imported pools. By default, only minimal data is returned (name, guid, status, health); additional sections like topology, scan, properties, etc. must be opted into via their respective flags. Pools that exist in the database but are not currently imported are returned with an OFFLINE status.

The boot pool can be queried by explicitly passing its name in `pool_names`. It is excluded from results when `pool_names` is null (query-all mode).

Examples::

# Query all pools (minimal info: name, guid, status, health) {}

# Query specific pools with properties { "pool_names": ["tank", "boot-pool"], "properties": ["size", "capacity"] }

# Query with full topology and scan information { "pool_names": ["tank"], "topology": true, "scan": true }

# Query everything { "topology": true, "scan": true, "expand": true, "features": true, "properties": ["size", "capacity", "health"] }

## Required Roles

- `POOL_READ`

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
- Type: object
- Default:
```json
{
  "pool_names": null,
  "properties": null,
  "topology": false,
  "scan": false,
  "expand": false,
  "features": false
}
```

Query parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_pool_names"></a>
<a id="Call_parameters_items_i0_pool_names"></a>
##### pool_names

- Schema name: `Pool Names`
- Default: null

Pool names to query. None queries all imported pools.
<a id="Call_parameters_items_i0_pool_names_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_pool_names_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_pool_names_anyOf_i0)

- Type: array of string
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_pool_names_anyOf_i0_items"></a>
- Type: string

<a id="tab-pane_Call_parameters_items_i0_pool_names_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_pool_names_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_properties"></a>
<a id="Call_parameters_items_i0_properties"></a>
##### properties

- Schema name: `Properties`
- Default: null

Property names to retrieve. None returns no properties.
<a id="Call_parameters_items_i0_properties_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_properties_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_properties_anyOf_i0)

- Type: array of string
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_properties_anyOf_i0_items"></a>
- Type: string

<a id="tab-pane_Call_parameters_items_i0_properties_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_properties_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_topology"></a>
<a id="Call_parameters_items_i0_topology"></a>
##### topology

- Schema name: `Topology`
- Type: boolean
- Default: false

Include vdev topology.

<a id="headingCall_parameters_items_i0_scan"></a>
<a id="Call_parameters_items_i0_scan"></a>
##### scan

- Schema name: `Scan`
- Type: boolean
- Default: false

Include scan/scrub information.

<a id="headingCall_parameters_items_i0_expand"></a>
<a id="Call_parameters_items_i0_expand"></a>
##### expand

- Schema name: `Expand`
- Type: boolean
- Default: false

Include expansion information.

<a id="headingCall_parameters_items_i0_features"></a>
<a id="Call_parameters_items_i0_features"></a>
##### features

- Schema name: `Features`
- Type: boolean
- Default: false

Include feature flags.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of object
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### ZPoolEntry

- Schema name: `ZPoolEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_id"></a>
<a id="Return_value_items_id"></a>
##### id

- Schema name: `Id`
- Default: null

Database id from `storage.volume`. `null` for the boot pool and for any pool not present in the database.
<a id="Return_value_items_id_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_id_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_id_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_name"></a>
<a id="Return_value_items_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of the zpool.

<a id="headingReturn_value_items_guid"></a>
<a id="Return_value_items_guid"></a>
##### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for the pool.

<a id="headingReturn_value_items_status"></a>
<a id="Return_value_items_status"></a>
##### status (required)

- Schema name: `Status`
- Type: string

Current pool status (ONLINE, DEGRADED, FAULTED, OFFLINE, etc.).

<a id="headingReturn_value_items_healthy"></a>
<a id="Return_value_items_healthy"></a>
##### healthy (required)

- Schema name: `Healthy`
- Type: boolean

Whether the pool is in a healthy state.

<a id="headingReturn_value_items_warning"></a>
<a id="Return_value_items_warning"></a>
##### warning (required)

- Schema name: `Warning`
- Type: boolean

Whether the pool has warning conditions.

<a id="headingReturn_value_items_status_code"></a>
<a id="Return_value_items_status_code"></a>
##### status_code (required)

- Schema name: `Status Code`

Detailed status code (e.g., OK, ERRATA, FEAT*DISABLED, LOCKED*SED_DISKS).
<a id="Return_value_items_status_code_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_status_code_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_status_code_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_status_code_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_status_code_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_status_detail"></a>
<a id="Return_value_items_status_detail"></a>
##### status_detail (required)

- Schema name: `Status Detail`

Human-readable status description.
<a id="Return_value_items_status_detail_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_status_detail_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_status_detail_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_status_detail_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_status_detail_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_is_upgraded"></a>
<a id="Return_value_items_is_upgraded"></a>
##### is_upgraded

- Schema name: `Is Upgraded`
- Default: null

Whether every ZFS feature flag on the pool is enabled. `null` for OFFLINE pools.
<a id="Return_value_items_is_upgraded_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_is_upgraded_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_is_upgraded_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_items_is_upgraded_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_is_upgraded_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_all_sed"></a>
<a id="Return_value_items_all_sed"></a>
##### all_sed

- Schema name: `All Sed`
- Default: null

`true` when every disk backing the pool is a Self-Encrypting Drive, `false` when at least one is not. `null` when the SED status of the pool has not yet been determined or does not apply.
<a id="Return_value_items_all_sed_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_all_sed_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_all_sed_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_items_all_sed_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_all_sed_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties"></a>
<a id="Return_value_items_properties"></a>
##### properties

- Schema name: `Properties`
- Default: null

Pool properties, keyed by property name.
<a id="Return_value_items_properties_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0)

- Type: object
<a id="headingReturn_value_items_properties_anyOf_i0_additionalProperties"></a>
<a id="Return_value_items_properties_anyOf_i0_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Schema name: `ZPoolPropertyValue`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_additionalProperties_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_additionalProperties_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw string representation of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_additionalProperties_source"></a>
<a id="Return_value_items_properties_anyOf_i0_additionalProperties_source"></a>
###### source (required)

- Schema name: `Source`

The source from where this property received its value (DEFAULT, LOCAL, NONE, etc.).
<a id="Return_value_items_properties_anyOf_i0_additionalProperties_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_additionalProperties_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_additionalProperties_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_additionalProperties_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_additionalProperties_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_additionalProperties_value"></a>
<a id="Return_value_items_properties_anyOf_i0_additionalProperties_value"></a>
###### value (required)

- Schema name: `Value`

The native Python value of the property.
<a id="Return_value_items_properties_anyOf_i0_additionalProperties_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_additionalProperties_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_additionalProperties_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_additionalProperties_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_additionalProperties_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_additionalProperties_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_additionalProperties_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_additionalProperties_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_additionalProperties_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_additionalProperties_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_additionalProperties_value_anyOf_i4)

- Type: null

<a id="tab-pane_Return_value_items_properties_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_topology"></a>
<a id="Return_value_items_topology"></a>
##### topology

- Default: null

Pool vdev topology.
<a id="Return_value_items_topology_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_topology_anyOf_i0"></a>
###### [ZPoolTopology](#tab-pane_Return_value_items_topology_anyOf_i0)

- Schema name: `ZPoolTopology`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_topology_anyOf_i0_data"></a>
<a id="Return_value_items_topology_anyOf_i0_data"></a>
###### data (required)

- Schema name: `Data`
- Type: array of object

Array of data vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_topology_anyOf_i0_data_items"></a>
###### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_topology_anyOf_i0_data_items_name"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_vdev_type"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_vdev_type"></a>
###### vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_guid"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_state"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats"></a>
###### stats (required)

- Schema name: `ZPoolVdevStats`
- Type: object

Vdev I/O statistics.
- No Additional Properties
<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_timestamp"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_timestamp"></a>
###### timestamp

- Schema name: `Timestamp`
- Type: integer
- Default: 0

High-resolution timestamp (nanoseconds).

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_allocated"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_allocated"></a>
###### allocated

- Schema name: `Allocated`
- Type: integer
- Default: 0

Allocated space in bytes.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_space"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_space"></a>
###### space

- Schema name: `Space`
- Type: integer
- Default: 0

Total space in bytes.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_dspace"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_dspace"></a>
###### dspace

- Schema name: `Dspace`
- Type: integer
- Default: 0

Deflated (compressed) space.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_pspace"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_pspace"></a>
###### pspace

- Schema name: `Pspace`
- Type: integer
- Default: 0

Physical space.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_rsize"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_rsize"></a>
###### rsize

- Schema name: `Rsize`
- Type: integer
- Default: 0

Replaceable dev size.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_esize"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_esize"></a>
###### esize

- Schema name: `Esize`
- Type: integer
- Default: 0

Expandable dev size.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_read_errors"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_read_errors"></a>
###### read_errors

- Schema name: `Read Errors`
- Type: integer
- Default: 0

Number of read errors.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_write_errors"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_write_errors"></a>
###### write_errors

- Schema name: `Write Errors`
- Type: integer
- Default: 0

Number of write errors.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_checksum_errors"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_checksum_errors"></a>
###### checksum_errors

- Schema name: `Checksum Errors`
- Type: integer
- Default: 0

Number of checksum errors.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_initialize_errors"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_initialize_errors"></a>
###### initialize_errors

- Schema name: `Initialize Errors`
- Type: integer
- Default: 0

Number of initialize errors.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_dio_verify_errors"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_dio_verify_errors"></a>
###### dio_verify_errors

- Schema name: `Dio Verify Errors`
- Type: integer
- Default: 0

Number of direct I/O verify errors.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_slow_ios"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_slow_ios"></a>
###### slow_ios

- Schema name: `Slow Ios`
- Default: null

Number of slow I/Os.
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_slow_ios_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_topology_anyOf_i0_data_items_stats_slow_ios_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_topology_anyOf_i0_data_items_stats_slow_ios_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_topology_anyOf_i0_data_items_stats_slow_ios_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_topology_anyOf_i0_data_items_stats_slow_ios_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_self_healed_bytes"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_self_healed_bytes"></a>
###### self_healed_bytes

- Schema name: `Self Healed Bytes`
- Type: integer
- Default: 0

Self-healed bytes.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_fragmentation"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_fragmentation"></a>
###### fragmentation

- Schema name: `Fragmentation`
- Type: integer
- Default: 0

Fragmentation percentage.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_scan_processed"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_scan_processed"></a>
###### scan_processed

- Schema name: `Scan Processed`
- Type: integer
- Default: 0

Bytes processed by scan.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_scan_removing"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_scan_removing"></a>
###### scan_removing

- Schema name: `Scan Removing`
- Type: integer
- Default: 0

Bytes processed by removal.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_rebuild_processed"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_rebuild_processed"></a>
###### rebuild_processed

- Schema name: `Rebuild Processed`
- Type: integer
- Default: 0

Bytes processed by rebuild.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_noalloc"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_noalloc"></a>
###### noalloc

- Schema name: `Noalloc`
- Type: integer
- Default: 0

Allocations halted.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_ops_read"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_ops_read"></a>
###### ops_read

- Schema name: `Ops Read`
- Type: integer
- Default: 0

Read operations.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_ops_write"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_ops_write"></a>
###### ops_write

- Schema name: `Ops Write`
- Type: integer
- Default: 0

Write operations.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_bytes_read"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_bytes_read"></a>
###### bytes_read

- Schema name: `Bytes Read`
- Type: integer
- Default: 0

Bytes read.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_bytes_write"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_bytes_write"></a>
###### bytes_write

- Schema name: `Bytes Write`
- Type: integer
- Default: 0

Bytes written.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_configured_ashift"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_configured_ashift"></a>
###### configured_ashift

- Schema name: `Configured Ashift`
- Default: null

Configured ashift value.
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_configured_ashift_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_topology_anyOf_i0_data_items_stats_configured_ashift_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_topology_anyOf_i0_data_items_stats_configured_ashift_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_topology_anyOf_i0_data_items_stats_configured_ashift_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_topology_anyOf_i0_data_items_stats_configured_ashift_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_logical_ashift"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_logical_ashift"></a>
###### logical_ashift

- Schema name: `Logical Ashift`
- Default: null

Logical ashift value.
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_logical_ashift_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_topology_anyOf_i0_data_items_stats_logical_ashift_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_topology_anyOf_i0_data_items_stats_logical_ashift_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_topology_anyOf_i0_data_items_stats_logical_ashift_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_topology_anyOf_i0_data_items_stats_logical_ashift_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_stats_physical_ashift"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_physical_ashift"></a>
###### physical_ashift

- Schema name: `Physical Ashift`
- Default: null

Physical ashift value.
<a id="Return_value_items_topology_anyOf_i0_data_items_stats_physical_ashift_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_topology_anyOf_i0_data_items_stats_physical_ashift_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_topology_anyOf_i0_data_items_stats_physical_ashift_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_topology_anyOf_i0_data_items_stats_physical_ashift_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_topology_anyOf_i0_data_items_stats_physical_ashift_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_children"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_children"></a>
###### children (required)

- Schema name: `Children`
- Type: array of object

Child vdevs.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_topology_anyOf_i0_data_items_children_items"></a>
###### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_topology_anyOf_i0_data_items_children_items_name"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_children_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_children_items_vdev_type"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_children_items_vdev_type"></a>
###### vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_children_items_guid"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_children_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_children_items_state"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_children_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_children_items_stats"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_children_items_stats"></a>
###### stats (required)

- Type: object

Vdev I/O statistics.

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_children_items_children"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_children_items_children"></a>
###### children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_topology_anyOf_i0_data_items_children_items_children_items"></a>
- Type: object

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_children_items_top_guid"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_children_items_top_guid"></a>
###### top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
<a id="Return_value_items_topology_anyOf_i0_data_items_children_items_top_guid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_topology_anyOf_i0_data_items_children_items_top_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_topology_anyOf_i0_data_items_children_items_top_guid_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_topology_anyOf_i0_data_items_children_items_top_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_topology_anyOf_i0_data_items_children_items_top_guid_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_children_items_path"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_children_items_path"></a>
###### path

- Schema name: `Path`
- Default: null

Device path stored in the vdev config (e.g. '/dev/disk/by-partuuid/<uuid>'). Unlike `name`, this is preserved for devices that were missing at pool import time. dRAID distributed spares store their synthetic spare name as the config path. `null` for interior vdevs (mirror, raidz, draid) that have no config path.
<a id="Return_value_items_topology_anyOf_i0_data_items_children_items_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_topology_anyOf_i0_data_items_children_items_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_topology_anyOf_i0_data_items_children_items_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_topology_anyOf_i0_data_items_children_items_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_topology_anyOf_i0_data_items_children_items_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_top_guid"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_top_guid"></a>
###### top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
<a id="Return_value_items_topology_anyOf_i0_data_items_top_guid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_topology_anyOf_i0_data_items_top_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_topology_anyOf_i0_data_items_top_guid_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_topology_anyOf_i0_data_items_top_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_topology_anyOf_i0_data_items_top_guid_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_topology_anyOf_i0_data_items_path"></a>
<a id="Return_value_items_topology_anyOf_i0_data_items_path"></a>
###### path

- Schema name: `Path`
- Default: null

Device path stored in the vdev config (e.g. '/dev/disk/by-partuuid/<uuid>'). Unlike `name`, this is preserved for devices that were missing at pool import time. dRAID distributed spares store their synthetic spare name as the config path. `null` for interior vdevs (mirror, raidz, draid) that have no config path.
<a id="Return_value_items_topology_anyOf_i0_data_items_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_topology_anyOf_i0_data_items_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_topology_anyOf_i0_data_items_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_topology_anyOf_i0_data_items_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_topology_anyOf_i0_data_items_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_topology_anyOf_i0_log"></a>
<a id="Return_value_items_topology_anyOf_i0_log"></a>
###### log (required)

- Schema name: `Log`
- Type: array of object

Array of ZFS Intent Log (ZIL) vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_topology_anyOf_i0_log_items"></a>
###### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_topology_anyOf_i0_log_items_name"></a>
<a id="Return_value_items_topology_anyOf_i0_log_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

<a id="headingReturn_value_items_topology_anyOf_i0_log_items_vdev_type"></a>
<a id="Return_value_items_topology_anyOf_i0_log_items_vdev_type"></a>
###### vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

<a id="headingReturn_value_items_topology_anyOf_i0_log_items_guid"></a>
<a id="Return_value_items_topology_anyOf_i0_log_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

<a id="headingReturn_value_items_topology_anyOf_i0_log_items_state"></a>
<a id="Return_value_items_topology_anyOf_i0_log_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

<a id="headingReturn_value_items_topology_anyOf_i0_log_items_stats"></a>
<a id="Return_value_items_topology_anyOf_i0_log_items_stats"></a>
###### stats (required)

- Type: object

Vdev I/O statistics.

<a id="headingReturn_value_items_topology_anyOf_i0_log_items_children"></a>
<a id="Return_value_items_topology_anyOf_i0_log_items_children"></a>
###### children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_topology_anyOf_i0_log_items_children_items"></a>
- Type: object

<a id="headingReturn_value_items_topology_anyOf_i0_log_items_top_guid"></a>
<a id="Return_value_items_topology_anyOf_i0_log_items_top_guid"></a>
###### top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
<a id="Return_value_items_topology_anyOf_i0_log_items_top_guid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_topology_anyOf_i0_log_items_top_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_topology_anyOf_i0_log_items_top_guid_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_topology_anyOf_i0_log_items_top_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_topology_anyOf_i0_log_items_top_guid_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_topology_anyOf_i0_log_items_path"></a>
<a id="Return_value_items_topology_anyOf_i0_log_items_path"></a>
###### path

- Schema name: `Path`
- Default: null

Device path stored in the vdev config (e.g. '/dev/disk/by-partuuid/<uuid>'). Unlike `name`, this is preserved for devices that were missing at pool import time. dRAID distributed spares store their synthetic spare name as the config path. `null` for interior vdevs (mirror, raidz, draid) that have no config path.
<a id="Return_value_items_topology_anyOf_i0_log_items_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_topology_anyOf_i0_log_items_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_topology_anyOf_i0_log_items_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_topology_anyOf_i0_log_items_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_topology_anyOf_i0_log_items_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_topology_anyOf_i0_cache"></a>
<a id="Return_value_items_topology_anyOf_i0_cache"></a>
###### cache (required)

- Schema name: `Cache`
- Type: array of object

Array of L2ARC cache vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_topology_anyOf_i0_cache_items"></a>
###### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_topology_anyOf_i0_cache_items_name"></a>
<a id="Return_value_items_topology_anyOf_i0_cache_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

<a id="headingReturn_value_items_topology_anyOf_i0_cache_items_vdev_type"></a>
<a id="Return_value_items_topology_anyOf_i0_cache_items_vdev_type"></a>
###### vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

<a id="headingReturn_value_items_topology_anyOf_i0_cache_items_guid"></a>
<a id="Return_value_items_topology_anyOf_i0_cache_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

<a id="headingReturn_value_items_topology_anyOf_i0_cache_items_state"></a>
<a id="Return_value_items_topology_anyOf_i0_cache_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

<a id="headingReturn_value_items_topology_anyOf_i0_cache_items_stats"></a>
<a id="Return_value_items_topology_anyOf_i0_cache_items_stats"></a>
###### stats (required)

- Type: object

Vdev I/O statistics.

<a id="headingReturn_value_items_topology_anyOf_i0_cache_items_children"></a>
<a id="Return_value_items_topology_anyOf_i0_cache_items_children"></a>
###### children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_topology_anyOf_i0_cache_items_children_items"></a>
- Type: object

<a id="headingReturn_value_items_topology_anyOf_i0_cache_items_top_guid"></a>
<a id="Return_value_items_topology_anyOf_i0_cache_items_top_guid"></a>
###### top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
<a id="Return_value_items_topology_anyOf_i0_cache_items_top_guid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_topology_anyOf_i0_cache_items_top_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_topology_anyOf_i0_cache_items_top_guid_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_topology_anyOf_i0_cache_items_top_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_topology_anyOf_i0_cache_items_top_guid_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_topology_anyOf_i0_cache_items_path"></a>
<a id="Return_value_items_topology_anyOf_i0_cache_items_path"></a>
###### path

- Schema name: `Path`
- Default: null

Device path stored in the vdev config (e.g. '/dev/disk/by-partuuid/<uuid>'). Unlike `name`, this is preserved for devices that were missing at pool import time. dRAID distributed spares store their synthetic spare name as the config path. `null` for interior vdevs (mirror, raidz, draid) that have no config path.
<a id="Return_value_items_topology_anyOf_i0_cache_items_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_topology_anyOf_i0_cache_items_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_topology_anyOf_i0_cache_items_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_topology_anyOf_i0_cache_items_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_topology_anyOf_i0_cache_items_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_topology_anyOf_i0_spares"></a>
<a id="Return_value_items_topology_anyOf_i0_spares"></a>
###### spares (required)

- Schema name: `Spares`
- Type: array of object

Array of spare disk configurations.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_topology_anyOf_i0_spares_items"></a>
###### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_topology_anyOf_i0_spares_items_name"></a>
<a id="Return_value_items_topology_anyOf_i0_spares_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

<a id="headingReturn_value_items_topology_anyOf_i0_spares_items_vdev_type"></a>
<a id="Return_value_items_topology_anyOf_i0_spares_items_vdev_type"></a>
###### vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

<a id="headingReturn_value_items_topology_anyOf_i0_spares_items_guid"></a>
<a id="Return_value_items_topology_anyOf_i0_spares_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

<a id="headingReturn_value_items_topology_anyOf_i0_spares_items_state"></a>
<a id="Return_value_items_topology_anyOf_i0_spares_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

<a id="headingReturn_value_items_topology_anyOf_i0_spares_items_stats"></a>
<a id="Return_value_items_topology_anyOf_i0_spares_items_stats"></a>
###### stats (required)

- Type: object

Vdev I/O statistics.

<a id="headingReturn_value_items_topology_anyOf_i0_spares_items_children"></a>
<a id="Return_value_items_topology_anyOf_i0_spares_items_children"></a>
###### children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_topology_anyOf_i0_spares_items_children_items"></a>
- Type: object

<a id="headingReturn_value_items_topology_anyOf_i0_spares_items_top_guid"></a>
<a id="Return_value_items_topology_anyOf_i0_spares_items_top_guid"></a>
###### top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
<a id="Return_value_items_topology_anyOf_i0_spares_items_top_guid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_topology_anyOf_i0_spares_items_top_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_topology_anyOf_i0_spares_items_top_guid_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_topology_anyOf_i0_spares_items_top_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_topology_anyOf_i0_spares_items_top_guid_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_topology_anyOf_i0_spares_items_path"></a>
<a id="Return_value_items_topology_anyOf_i0_spares_items_path"></a>
###### path

- Schema name: `Path`
- Default: null

Device path stored in the vdev config (e.g. '/dev/disk/by-partuuid/<uuid>'). Unlike `name`, this is preserved for devices that were missing at pool import time. dRAID distributed spares store their synthetic spare name as the config path. `null` for interior vdevs (mirror, raidz, draid) that have no config path.
<a id="Return_value_items_topology_anyOf_i0_spares_items_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_topology_anyOf_i0_spares_items_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_topology_anyOf_i0_spares_items_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_topology_anyOf_i0_spares_items_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_topology_anyOf_i0_spares_items_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_topology_anyOf_i0_special"></a>
<a id="Return_value_items_topology_anyOf_i0_special"></a>
###### special (required)

- Schema name: `Special`
- Type: array of object

Array of special vdev configurations for metadata.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_topology_anyOf_i0_special_items"></a>
###### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_topology_anyOf_i0_special_items_name"></a>
<a id="Return_value_items_topology_anyOf_i0_special_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

<a id="headingReturn_value_items_topology_anyOf_i0_special_items_vdev_type"></a>
<a id="Return_value_items_topology_anyOf_i0_special_items_vdev_type"></a>
###### vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

<a id="headingReturn_value_items_topology_anyOf_i0_special_items_guid"></a>
<a id="Return_value_items_topology_anyOf_i0_special_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

<a id="headingReturn_value_items_topology_anyOf_i0_special_items_state"></a>
<a id="Return_value_items_topology_anyOf_i0_special_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

<a id="headingReturn_value_items_topology_anyOf_i0_special_items_stats"></a>
<a id="Return_value_items_topology_anyOf_i0_special_items_stats"></a>
###### stats (required)

- Type: object

Vdev I/O statistics.

<a id="headingReturn_value_items_topology_anyOf_i0_special_items_children"></a>
<a id="Return_value_items_topology_anyOf_i0_special_items_children"></a>
###### children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_topology_anyOf_i0_special_items_children_items"></a>
- Type: object

<a id="headingReturn_value_items_topology_anyOf_i0_special_items_top_guid"></a>
<a id="Return_value_items_topology_anyOf_i0_special_items_top_guid"></a>
###### top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
<a id="Return_value_items_topology_anyOf_i0_special_items_top_guid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_topology_anyOf_i0_special_items_top_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_topology_anyOf_i0_special_items_top_guid_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_topology_anyOf_i0_special_items_top_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_topology_anyOf_i0_special_items_top_guid_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_topology_anyOf_i0_special_items_path"></a>
<a id="Return_value_items_topology_anyOf_i0_special_items_path"></a>
###### path

- Schema name: `Path`
- Default: null

Device path stored in the vdev config (e.g. '/dev/disk/by-partuuid/<uuid>'). Unlike `name`, this is preserved for devices that were missing at pool import time. dRAID distributed spares store their synthetic spare name as the config path. `null` for interior vdevs (mirror, raidz, draid) that have no config path.
<a id="Return_value_items_topology_anyOf_i0_special_items_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_topology_anyOf_i0_special_items_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_topology_anyOf_i0_special_items_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_topology_anyOf_i0_special_items_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_topology_anyOf_i0_special_items_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_topology_anyOf_i0_dedup"></a>
<a id="Return_value_items_topology_anyOf_i0_dedup"></a>
###### dedup (required)

- Schema name: `Dedup`
- Type: array of object

Array of deduplication table vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_topology_anyOf_i0_dedup_items"></a>
###### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_topology_anyOf_i0_dedup_items_name"></a>
<a id="Return_value_items_topology_anyOf_i0_dedup_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

<a id="headingReturn_value_items_topology_anyOf_i0_dedup_items_vdev_type"></a>
<a id="Return_value_items_topology_anyOf_i0_dedup_items_vdev_type"></a>
###### vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

<a id="headingReturn_value_items_topology_anyOf_i0_dedup_items_guid"></a>
<a id="Return_value_items_topology_anyOf_i0_dedup_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

<a id="headingReturn_value_items_topology_anyOf_i0_dedup_items_state"></a>
<a id="Return_value_items_topology_anyOf_i0_dedup_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

<a id="headingReturn_value_items_topology_anyOf_i0_dedup_items_stats"></a>
<a id="Return_value_items_topology_anyOf_i0_dedup_items_stats"></a>
###### stats (required)

- Type: object

Vdev I/O statistics.

<a id="headingReturn_value_items_topology_anyOf_i0_dedup_items_children"></a>
<a id="Return_value_items_topology_anyOf_i0_dedup_items_children"></a>
###### children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_topology_anyOf_i0_dedup_items_children_items"></a>
- Type: object

<a id="headingReturn_value_items_topology_anyOf_i0_dedup_items_top_guid"></a>
<a id="Return_value_items_topology_anyOf_i0_dedup_items_top_guid"></a>
###### top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
<a id="Return_value_items_topology_anyOf_i0_dedup_items_top_guid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_topology_anyOf_i0_dedup_items_top_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_topology_anyOf_i0_dedup_items_top_guid_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_topology_anyOf_i0_dedup_items_top_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_topology_anyOf_i0_dedup_items_top_guid_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_topology_anyOf_i0_dedup_items_path"></a>
<a id="Return_value_items_topology_anyOf_i0_dedup_items_path"></a>
###### path

- Schema name: `Path`
- Default: null

Device path stored in the vdev config (e.g. '/dev/disk/by-partuuid/<uuid>'). Unlike `name`, this is preserved for devices that were missing at pool import time. dRAID distributed spares store their synthetic spare name as the config path. `null` for interior vdevs (mirror, raidz, draid) that have no config path.
<a id="Return_value_items_topology_anyOf_i0_dedup_items_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_topology_anyOf_i0_dedup_items_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_topology_anyOf_i0_dedup_items_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_topology_anyOf_i0_dedup_items_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_topology_anyOf_i0_dedup_items_path_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_items_topology_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_topology_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_scan"></a>
<a id="Return_value_items_scan"></a>
##### scan

- Default: null

Most recent scrub or resilver information.
<a id="Return_value_items_scan_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_scan_anyOf_i0"></a>
###### [ZPoolScan](#tab-pane_Return_value_items_scan_anyOf_i0)

- Schema name: `ZPoolScan`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_scan_anyOf_i0_function"></a>
<a id="Return_value_items_scan_anyOf_i0_function"></a>
###### function (required)

- Schema name: `Function`
- Type: enum (of string)

Type of ZFS pool scan.
###### Must be one of:

- "RESILVER"
- "SCRUB"

<a id="headingReturn_value_items_scan_anyOf_i0_state"></a>
<a id="Return_value_items_scan_anyOf_i0_state"></a>
###### state (required)

- Schema name: `State`
- Type: enum (of string)

Current lifecycle state of the scan.
###### Must be one of:

- "SCANNING"
- "FINISHED"
- "CANCELED"

<a id="headingReturn_value_items_scan_anyOf_i0_start_time"></a>
<a id="Return_value_items_scan_anyOf_i0_start_time"></a>
###### start_time (required)

- Schema name: `Start Time`
- Type: integer

Scan start time (unix timestamp).

<a id="headingReturn_value_items_scan_anyOf_i0_end_time"></a>
<a id="Return_value_items_scan_anyOf_i0_end_time"></a>
###### end_time (required)

- Schema name: `End Time`

Scan end time as unix timestamp (`null` while the scan is still running).
<a id="Return_value_items_scan_anyOf_i0_end_time_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_scan_anyOf_i0_end_time_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_scan_anyOf_i0_end_time_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_scan_anyOf_i0_end_time_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_scan_anyOf_i0_end_time_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_scan_anyOf_i0_percentage"></a>
<a id="Return_value_items_scan_anyOf_i0_percentage"></a>
###### percentage (required)

- Schema name: `Percentage`
- Type: number

Scan progress (between 0 and 100%).

<a id="headingReturn_value_items_scan_anyOf_i0_bytes_to_process"></a>
<a id="Return_value_items_scan_anyOf_i0_bytes_to_process"></a>
###### bytes_to_process (required)

- Schema name: `Bytes To Process`
- Type: integer

Total bytes located by scanner.

<a id="headingReturn_value_items_scan_anyOf_i0_bytes_processed"></a>
<a id="Return_value_items_scan_anyOf_i0_bytes_processed"></a>
###### bytes_processed (required)

- Schema name: `Bytes Processed`
- Type: integer

Total bytes to scan.

<a id="headingReturn_value_items_scan_anyOf_i0_bytes_issued"></a>
<a id="Return_value_items_scan_anyOf_i0_bytes_issued"></a>
###### bytes_issued (required)

- Schema name: `Bytes Issued`
- Type: integer

Issued bytes per scan pass.

<a id="headingReturn_value_items_scan_anyOf_i0_pause"></a>
<a id="Return_value_items_scan_anyOf_i0_pause"></a>
###### pause (required)

- Schema name: `Pause`

Pause time as unix timestamp (`null` if the scan is not paused).
<a id="Return_value_items_scan_anyOf_i0_pause_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_scan_anyOf_i0_pause_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_scan_anyOf_i0_pause_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_scan_anyOf_i0_pause_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_scan_anyOf_i0_pause_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_scan_anyOf_i0_errors"></a>
<a id="Return_value_items_scan_anyOf_i0_errors"></a>
###### errors (required)

- Schema name: `Errors`
- Type: integer

Number of scan errors.

<a id="headingReturn_value_items_scan_anyOf_i0_total_secs_left"></a>
<a id="Return_value_items_scan_anyOf_i0_total_secs_left"></a>
###### total_secs_left (required)

- Schema name: `Total Secs Left`

Number of seconds left (`null` if the scan is not running).
<a id="Return_value_items_scan_anyOf_i0_total_secs_left_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_scan_anyOf_i0_total_secs_left_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_scan_anyOf_i0_total_secs_left_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_scan_anyOf_i0_total_secs_left_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_scan_anyOf_i0_total_secs_left_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_items_scan_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_scan_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_expand"></a>
<a id="Return_value_items_expand"></a>
##### expand

- Default: null

RAIDZ expansion information.
<a id="Return_value_items_expand_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_expand_anyOf_i0"></a>
###### [ZPoolExpand](#tab-pane_Return_value_items_expand_anyOf_i0)

- Schema name: `ZPoolExpand`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_expand_anyOf_i0_state"></a>
<a id="Return_value_items_expand_anyOf_i0_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Expansion state (e.g., SCANNING, FINISHED).

<a id="headingReturn_value_items_expand_anyOf_i0_expanding_vdev"></a>
<a id="Return_value_items_expand_anyOf_i0_expanding_vdev"></a>
###### expanding_vdev (required)

- Schema name: `Expanding Vdev`
- Type: integer

Index of the vdev being expanded.

<a id="headingReturn_value_items_expand_anyOf_i0_start_time"></a>
<a id="Return_value_items_expand_anyOf_i0_start_time"></a>
###### start_time (required)

- Schema name: `Start Time`
- Type: integer

Expansion start time (unix timestamp).

<a id="headingReturn_value_items_expand_anyOf_i0_end_time"></a>
<a id="Return_value_items_expand_anyOf_i0_end_time"></a>
###### end_time (required)

- Schema name: `End Time`

Expansion end time as unix timestamp (`null` while expanding).
<a id="Return_value_items_expand_anyOf_i0_end_time_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_expand_anyOf_i0_end_time_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_expand_anyOf_i0_end_time_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_expand_anyOf_i0_end_time_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_expand_anyOf_i0_end_time_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_expand_anyOf_i0_bytes_to_reflow"></a>
<a id="Return_value_items_expand_anyOf_i0_bytes_to_reflow"></a>
###### bytes_to_reflow (required)

- Schema name: `Bytes To Reflow`
- Type: integer

Total bytes that need to be reflowed.

<a id="headingReturn_value_items_expand_anyOf_i0_bytes_reflowed"></a>
<a id="Return_value_items_expand_anyOf_i0_bytes_reflowed"></a>
###### bytes_reflowed (required)

- Schema name: `Bytes Reflowed`
- Type: integer

Total bytes reflowed so far.

<a id="headingReturn_value_items_expand_anyOf_i0_waiting_for_resilver"></a>
<a id="Return_value_items_expand_anyOf_i0_waiting_for_resilver"></a>
###### waiting_for_resilver (required)

- Schema name: `Waiting For Resilver`
- Type: integer

Non-zero if expansion is waiting for a resilver to complete.

<a id="headingReturn_value_items_expand_anyOf_i0_total_secs_left"></a>
<a id="Return_value_items_expand_anyOf_i0_total_secs_left"></a>
###### total_secs_left (required)

- Schema name: `Total Secs Left`

Estimated seconds remaining (`null` if not expanding).
<a id="Return_value_items_expand_anyOf_i0_total_secs_left_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_expand_anyOf_i0_total_secs_left_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_expand_anyOf_i0_total_secs_left_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_expand_anyOf_i0_total_secs_left_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_expand_anyOf_i0_total_secs_left_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_expand_anyOf_i0_percentage"></a>
<a id="Return_value_items_expand_anyOf_i0_percentage"></a>
###### percentage (required)

- Schema name: `Percentage`
- Type: number

Expansion progress (between 0 and 100%).

<a id="tab-pane_Return_value_items_expand_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_expand_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_features"></a>
<a id="Return_value_items_features"></a>
##### features

- Schema name: `Features`
- Default: null

Pool feature flags.
<a id="Return_value_items_features_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_features_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_features_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_features_anyOf_i0_items"></a>
###### ZPoolFeature

- Schema name: `ZPoolFeature`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_features_anyOf_i0_items_name"></a>
<a id="Return_value_items_features_anyOf_i0_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Feature name.

<a id="headingReturn_value_items_features_anyOf_i0_items_guid"></a>
<a id="Return_value_items_features_anyOf_i0_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: string

Feature GUID.

<a id="headingReturn_value_items_features_anyOf_i0_items_description"></a>
<a id="Return_value_items_features_anyOf_i0_items_description"></a>
###### description (required)

- Schema name: `Description`
- Type: string

Feature description.

<a id="headingReturn_value_items_features_anyOf_i0_items_state"></a>
<a id="Return_value_items_features_anyOf_i0_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Feature state.

<a id="tab-pane_Return_value_items_features_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_features_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
