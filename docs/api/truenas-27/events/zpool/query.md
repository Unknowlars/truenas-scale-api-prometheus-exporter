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

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `ZPoolQueryAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Database id of the pool.

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `ZPoolEntry`
- Type: object

Event fields.
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id

- Schema name: `Id`
- Default: null

Database id from `storage.volume`. `null` for the boot pool and for any pool not present in the database.
<a id="ADDED_fields_id_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_id_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_id_anyOf_i1)

- Type: null

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of the zpool.

<a id="headingADDED_fields_guid"></a>
<a id="ADDED_fields_guid"></a>
##### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for the pool.

<a id="headingADDED_fields_status"></a>
<a id="ADDED_fields_status"></a>
##### status (required)

- Schema name: `Status`
- Type: string

Current pool status (ONLINE, DEGRADED, FAULTED, OFFLINE, etc.).

<a id="headingADDED_fields_healthy"></a>
<a id="ADDED_fields_healthy"></a>
##### healthy (required)

- Schema name: `Healthy`
- Type: boolean

Whether the pool is in a healthy state.

<a id="headingADDED_fields_warning"></a>
<a id="ADDED_fields_warning"></a>
##### warning (required)

- Schema name: `Warning`
- Type: boolean

Whether the pool has warning conditions.

<a id="headingADDED_fields_status_code"></a>
<a id="ADDED_fields_status_code"></a>
##### status_code (required)

- Schema name: `Status Code`

Detailed status code (e.g., OK, ERRATA, FEAT*DISABLED, LOCKED*SED_DISKS).
<a id="ADDED_fields_status_code_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_status_code_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_status_code_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_status_code_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_status_code_anyOf_i1)

- Type: null

<a id="headingADDED_fields_status_detail"></a>
<a id="ADDED_fields_status_detail"></a>
##### status_detail (required)

- Schema name: `Status Detail`

Human-readable status description.
<a id="ADDED_fields_status_detail_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_status_detail_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_status_detail_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_status_detail_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_status_detail_anyOf_i1)

- Type: null

<a id="headingADDED_fields_is_upgraded"></a>
<a id="ADDED_fields_is_upgraded"></a>
##### is_upgraded

- Schema name: `Is Upgraded`
- Default: null

Whether every ZFS feature flag on the pool is enabled. `null` for OFFLINE pools.
<a id="ADDED_fields_is_upgraded_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_is_upgraded_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_is_upgraded_anyOf_i0)

- Type: boolean

<a id="tab-pane_ADDED_fields_is_upgraded_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_is_upgraded_anyOf_i1)

- Type: null

<a id="headingADDED_fields_all_sed"></a>
<a id="ADDED_fields_all_sed"></a>
##### all_sed

- Schema name: `All Sed`
- Default: null

`true` when every disk backing the pool is a Self-Encrypting Drive, `false` when at least one is not. `null` when the SED status of the pool has not yet been determined or does not apply.
<a id="ADDED_fields_all_sed_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_all_sed_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_all_sed_anyOf_i0)

- Type: boolean

<a id="tab-pane_ADDED_fields_all_sed_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_all_sed_anyOf_i1)

- Type: null

<a id="headingADDED_fields_properties"></a>
<a id="ADDED_fields_properties"></a>
##### properties

- Schema name: `Properties`
- Default: null

Pool properties, keyed by property name.
<a id="ADDED_fields_properties_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_properties_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_properties_anyOf_i0)

- Type: object
<a id="headingADDED_fields_properties_anyOf_i0_additionalProperties"></a>
<a id="ADDED_fields_properties_anyOf_i0_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Schema name: `ZPoolPropertyValue`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_properties_anyOf_i0_additionalProperties_raw"></a>
<a id="ADDED_fields_properties_anyOf_i0_additionalProperties_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw string representation of the property.

<a id="headingADDED_fields_properties_anyOf_i0_additionalProperties_source"></a>
<a id="ADDED_fields_properties_anyOf_i0_additionalProperties_source"></a>
###### source (required)

- Schema name: `Source`

The source from where this property received its value (DEFAULT, LOCAL, NONE, etc.).
<a id="ADDED_fields_properties_anyOf_i0_additionalProperties_source_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_properties_anyOf_i0_additionalProperties_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_properties_anyOf_i0_additionalProperties_source_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_properties_anyOf_i0_additionalProperties_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_properties_anyOf_i0_additionalProperties_source_anyOf_i1)

- Type: null

<a id="headingADDED_fields_properties_anyOf_i0_additionalProperties_value"></a>
<a id="ADDED_fields_properties_anyOf_i0_additionalProperties_value"></a>
###### value (required)

- Schema name: `Value`

The native Python value of the property.
<a id="ADDED_fields_properties_anyOf_i0_additionalProperties_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_properties_anyOf_i0_additionalProperties_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_properties_anyOf_i0_additionalProperties_value_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_properties_anyOf_i0_additionalProperties_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_properties_anyOf_i0_additionalProperties_value_anyOf_i1)

- Type: number

<a id="tab-pane_ADDED_fields_properties_anyOf_i0_additionalProperties_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_ADDED_fields_properties_anyOf_i0_additionalProperties_value_anyOf_i2)

- Type: string

<a id="tab-pane_ADDED_fields_properties_anyOf_i0_additionalProperties_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_ADDED_fields_properties_anyOf_i0_additionalProperties_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_ADDED_fields_properties_anyOf_i0_additionalProperties_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_ADDED_fields_properties_anyOf_i0_additionalProperties_value_anyOf_i4)

- Type: null

<a id="tab-pane_ADDED_fields_properties_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_properties_anyOf_i1)

- Type: null

<a id="headingADDED_fields_topology"></a>
<a id="ADDED_fields_topology"></a>
##### topology

- Default: null

Pool vdev topology.
<a id="ADDED_fields_topology_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_topology_anyOf_i0"></a>
###### [ZPoolTopology](#tab-pane_ADDED_fields_topology_anyOf_i0)

- Schema name: `ZPoolTopology`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_topology_anyOf_i0_data"></a>
<a id="ADDED_fields_topology_anyOf_i0_data"></a>
###### data (required)

- Schema name: `Data`
- Type: array of object

Array of data vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_topology_anyOf_i0_data_items"></a>
###### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_topology_anyOf_i0_data_items_name"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

<a id="headingADDED_fields_topology_anyOf_i0_data_items_vdev_type"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_vdev_type"></a>
###### vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

<a id="headingADDED_fields_topology_anyOf_i0_data_items_guid"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_state"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats"></a>
###### stats (required)

- Schema name: `ZPoolVdevStats`
- Type: object

Vdev I/O statistics.
- No Additional Properties
<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_timestamp"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_timestamp"></a>
###### timestamp

- Schema name: `Timestamp`
- Type: integer
- Default: 0

High-resolution timestamp (nanoseconds).

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_allocated"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_allocated"></a>
###### allocated

- Schema name: `Allocated`
- Type: integer
- Default: 0

Allocated space in bytes.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_space"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_space"></a>
###### space

- Schema name: `Space`
- Type: integer
- Default: 0

Total space in bytes.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_dspace"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_dspace"></a>
###### dspace

- Schema name: `Dspace`
- Type: integer
- Default: 0

Deflated (compressed) space.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_pspace"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_pspace"></a>
###### pspace

- Schema name: `Pspace`
- Type: integer
- Default: 0

Physical space.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_rsize"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_rsize"></a>
###### rsize

- Schema name: `Rsize`
- Type: integer
- Default: 0

Replaceable dev size.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_esize"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_esize"></a>
###### esize

- Schema name: `Esize`
- Type: integer
- Default: 0

Expandable dev size.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_read_errors"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_read_errors"></a>
###### read_errors

- Schema name: `Read Errors`
- Type: integer
- Default: 0

Number of read errors.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_write_errors"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_write_errors"></a>
###### write_errors

- Schema name: `Write Errors`
- Type: integer
- Default: 0

Number of write errors.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_checksum_errors"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_checksum_errors"></a>
###### checksum_errors

- Schema name: `Checksum Errors`
- Type: integer
- Default: 0

Number of checksum errors.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_initialize_errors"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_initialize_errors"></a>
###### initialize_errors

- Schema name: `Initialize Errors`
- Type: integer
- Default: 0

Number of initialize errors.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_dio_verify_errors"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_dio_verify_errors"></a>
###### dio_verify_errors

- Schema name: `Dio Verify Errors`
- Type: integer
- Default: 0

Number of direct I/O verify errors.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_slow_ios"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_slow_ios"></a>
###### slow_ios

- Schema name: `Slow Ios`
- Default: null

Number of slow I/Os.
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_slow_ios_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_data_items_stats_slow_ios_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_topology_anyOf_i0_data_items_stats_slow_ios_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_data_items_stats_slow_ios_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_topology_anyOf_i0_data_items_stats_slow_ios_anyOf_i1)

- Type: null

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_self_healed_bytes"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_self_healed_bytes"></a>
###### self_healed_bytes

- Schema name: `Self Healed Bytes`
- Type: integer
- Default: 0

Self-healed bytes.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_fragmentation"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_fragmentation"></a>
###### fragmentation

- Schema name: `Fragmentation`
- Type: integer
- Default: 0

Fragmentation percentage.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_scan_processed"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_scan_processed"></a>
###### scan_processed

- Schema name: `Scan Processed`
- Type: integer
- Default: 0

Bytes processed by scan.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_scan_removing"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_scan_removing"></a>
###### scan_removing

- Schema name: `Scan Removing`
- Type: integer
- Default: 0

Bytes processed by removal.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_rebuild_processed"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_rebuild_processed"></a>
###### rebuild_processed

- Schema name: `Rebuild Processed`
- Type: integer
- Default: 0

Bytes processed by rebuild.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_noalloc"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_noalloc"></a>
###### noalloc

- Schema name: `Noalloc`
- Type: integer
- Default: 0

Allocations halted.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_ops_read"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_ops_read"></a>
###### ops_read

- Schema name: `Ops Read`
- Type: integer
- Default: 0

Read operations.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_ops_write"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_ops_write"></a>
###### ops_write

- Schema name: `Ops Write`
- Type: integer
- Default: 0

Write operations.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_bytes_read"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_bytes_read"></a>
###### bytes_read

- Schema name: `Bytes Read`
- Type: integer
- Default: 0

Bytes read.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_bytes_write"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_bytes_write"></a>
###### bytes_write

- Schema name: `Bytes Write`
- Type: integer
- Default: 0

Bytes written.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_configured_ashift"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_configured_ashift"></a>
###### configured_ashift

- Schema name: `Configured Ashift`
- Default: null

Configured ashift value.
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_configured_ashift_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_data_items_stats_configured_ashift_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_topology_anyOf_i0_data_items_stats_configured_ashift_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_data_items_stats_configured_ashift_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_topology_anyOf_i0_data_items_stats_configured_ashift_anyOf_i1)

- Type: null

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_logical_ashift"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_logical_ashift"></a>
###### logical_ashift

- Schema name: `Logical Ashift`
- Default: null

Logical ashift value.
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_logical_ashift_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_data_items_stats_logical_ashift_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_topology_anyOf_i0_data_items_stats_logical_ashift_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_data_items_stats_logical_ashift_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_topology_anyOf_i0_data_items_stats_logical_ashift_anyOf_i1)

- Type: null

<a id="headingADDED_fields_topology_anyOf_i0_data_items_stats_physical_ashift"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_physical_ashift"></a>
###### physical_ashift

- Schema name: `Physical Ashift`
- Default: null

Physical ashift value.
<a id="ADDED_fields_topology_anyOf_i0_data_items_stats_physical_ashift_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_data_items_stats_physical_ashift_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_topology_anyOf_i0_data_items_stats_physical_ashift_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_data_items_stats_physical_ashift_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_topology_anyOf_i0_data_items_stats_physical_ashift_anyOf_i1)

- Type: null

<a id="headingADDED_fields_topology_anyOf_i0_data_items_children"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_children"></a>
###### children (required)

- Schema name: `Children`
- Type: array of object

Child vdevs.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_topology_anyOf_i0_data_items_children_items"></a>
###### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_topology_anyOf_i0_data_items_children_items_name"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_children_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

<a id="headingADDED_fields_topology_anyOf_i0_data_items_children_items_vdev_type"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_children_items_vdev_type"></a>
###### vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

<a id="headingADDED_fields_topology_anyOf_i0_data_items_children_items_guid"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_children_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_children_items_state"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_children_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

<a id="headingADDED_fields_topology_anyOf_i0_data_items_children_items_stats"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_children_items_stats"></a>
###### stats (required)

- Type: object

Vdev I/O statistics.

<a id="headingADDED_fields_topology_anyOf_i0_data_items_children_items_children"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_children_items_children"></a>
###### children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_topology_anyOf_i0_data_items_children_items_children_items"></a>
- Type: object

<a id="headingADDED_fields_topology_anyOf_i0_data_items_children_items_top_guid"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_children_items_top_guid"></a>
###### top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
<a id="ADDED_fields_topology_anyOf_i0_data_items_children_items_top_guid_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_data_items_children_items_top_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_topology_anyOf_i0_data_items_children_items_top_guid_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_data_items_children_items_top_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_topology_anyOf_i0_data_items_children_items_top_guid_anyOf_i1)

- Type: null

<a id="headingADDED_fields_topology_anyOf_i0_data_items_children_items_path"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_children_items_path"></a>
###### path

- Schema name: `Path`
- Default: null

Device path stored in the vdev config (e.g. '/dev/disk/by-partuuid/<uuid>'). Unlike `name`, this is preserved for devices that were missing at pool import time. dRAID distributed spares store their synthetic spare name as the config path. `null` for interior vdevs (mirror, raidz, draid) that have no config path.
<a id="ADDED_fields_topology_anyOf_i0_data_items_children_items_path_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_data_items_children_items_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_topology_anyOf_i0_data_items_children_items_path_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_data_items_children_items_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_topology_anyOf_i0_data_items_children_items_path_anyOf_i1)

- Type: null

<a id="headingADDED_fields_topology_anyOf_i0_data_items_top_guid"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_top_guid"></a>
###### top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
<a id="ADDED_fields_topology_anyOf_i0_data_items_top_guid_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_data_items_top_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_topology_anyOf_i0_data_items_top_guid_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_data_items_top_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_topology_anyOf_i0_data_items_top_guid_anyOf_i1)

- Type: null

<a id="headingADDED_fields_topology_anyOf_i0_data_items_path"></a>
<a id="ADDED_fields_topology_anyOf_i0_data_items_path"></a>
###### path

- Schema name: `Path`
- Default: null

Device path stored in the vdev config (e.g. '/dev/disk/by-partuuid/<uuid>'). Unlike `name`, this is preserved for devices that were missing at pool import time. dRAID distributed spares store their synthetic spare name as the config path. `null` for interior vdevs (mirror, raidz, draid) that have no config path.
<a id="ADDED_fields_topology_anyOf_i0_data_items_path_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_data_items_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_topology_anyOf_i0_data_items_path_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_data_items_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_topology_anyOf_i0_data_items_path_anyOf_i1)

- Type: null

<a id="headingADDED_fields_topology_anyOf_i0_log"></a>
<a id="ADDED_fields_topology_anyOf_i0_log"></a>
###### log (required)

- Schema name: `Log`
- Type: array of object

Array of ZFS Intent Log (ZIL) vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_topology_anyOf_i0_log_items"></a>
###### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_topology_anyOf_i0_log_items_name"></a>
<a id="ADDED_fields_topology_anyOf_i0_log_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

<a id="headingADDED_fields_topology_anyOf_i0_log_items_vdev_type"></a>
<a id="ADDED_fields_topology_anyOf_i0_log_items_vdev_type"></a>
###### vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

<a id="headingADDED_fields_topology_anyOf_i0_log_items_guid"></a>
<a id="ADDED_fields_topology_anyOf_i0_log_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

<a id="headingADDED_fields_topology_anyOf_i0_log_items_state"></a>
<a id="ADDED_fields_topology_anyOf_i0_log_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

<a id="headingADDED_fields_topology_anyOf_i0_log_items_stats"></a>
<a id="ADDED_fields_topology_anyOf_i0_log_items_stats"></a>
###### stats (required)

- Type: object

Vdev I/O statistics.

<a id="headingADDED_fields_topology_anyOf_i0_log_items_children"></a>
<a id="ADDED_fields_topology_anyOf_i0_log_items_children"></a>
###### children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_topology_anyOf_i0_log_items_children_items"></a>
- Type: object

<a id="headingADDED_fields_topology_anyOf_i0_log_items_top_guid"></a>
<a id="ADDED_fields_topology_anyOf_i0_log_items_top_guid"></a>
###### top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
<a id="ADDED_fields_topology_anyOf_i0_log_items_top_guid_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_log_items_top_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_topology_anyOf_i0_log_items_top_guid_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_log_items_top_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_topology_anyOf_i0_log_items_top_guid_anyOf_i1)

- Type: null

<a id="headingADDED_fields_topology_anyOf_i0_log_items_path"></a>
<a id="ADDED_fields_topology_anyOf_i0_log_items_path"></a>
###### path

- Schema name: `Path`
- Default: null

Device path stored in the vdev config (e.g. '/dev/disk/by-partuuid/<uuid>'). Unlike `name`, this is preserved for devices that were missing at pool import time. dRAID distributed spares store their synthetic spare name as the config path. `null` for interior vdevs (mirror, raidz, draid) that have no config path.
<a id="ADDED_fields_topology_anyOf_i0_log_items_path_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_log_items_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_topology_anyOf_i0_log_items_path_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_log_items_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_topology_anyOf_i0_log_items_path_anyOf_i1)

- Type: null

<a id="headingADDED_fields_topology_anyOf_i0_cache"></a>
<a id="ADDED_fields_topology_anyOf_i0_cache"></a>
###### cache (required)

- Schema name: `Cache`
- Type: array of object

Array of L2ARC cache vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_topology_anyOf_i0_cache_items"></a>
###### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_topology_anyOf_i0_cache_items_name"></a>
<a id="ADDED_fields_topology_anyOf_i0_cache_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

<a id="headingADDED_fields_topology_anyOf_i0_cache_items_vdev_type"></a>
<a id="ADDED_fields_topology_anyOf_i0_cache_items_vdev_type"></a>
###### vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

<a id="headingADDED_fields_topology_anyOf_i0_cache_items_guid"></a>
<a id="ADDED_fields_topology_anyOf_i0_cache_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

<a id="headingADDED_fields_topology_anyOf_i0_cache_items_state"></a>
<a id="ADDED_fields_topology_anyOf_i0_cache_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

<a id="headingADDED_fields_topology_anyOf_i0_cache_items_stats"></a>
<a id="ADDED_fields_topology_anyOf_i0_cache_items_stats"></a>
###### stats (required)

- Type: object

Vdev I/O statistics.

<a id="headingADDED_fields_topology_anyOf_i0_cache_items_children"></a>
<a id="ADDED_fields_topology_anyOf_i0_cache_items_children"></a>
###### children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_topology_anyOf_i0_cache_items_children_items"></a>
- Type: object

<a id="headingADDED_fields_topology_anyOf_i0_cache_items_top_guid"></a>
<a id="ADDED_fields_topology_anyOf_i0_cache_items_top_guid"></a>
###### top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
<a id="ADDED_fields_topology_anyOf_i0_cache_items_top_guid_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_cache_items_top_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_topology_anyOf_i0_cache_items_top_guid_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_cache_items_top_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_topology_anyOf_i0_cache_items_top_guid_anyOf_i1)

- Type: null

<a id="headingADDED_fields_topology_anyOf_i0_cache_items_path"></a>
<a id="ADDED_fields_topology_anyOf_i0_cache_items_path"></a>
###### path

- Schema name: `Path`
- Default: null

Device path stored in the vdev config (e.g. '/dev/disk/by-partuuid/<uuid>'). Unlike `name`, this is preserved for devices that were missing at pool import time. dRAID distributed spares store their synthetic spare name as the config path. `null` for interior vdevs (mirror, raidz, draid) that have no config path.
<a id="ADDED_fields_topology_anyOf_i0_cache_items_path_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_cache_items_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_topology_anyOf_i0_cache_items_path_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_cache_items_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_topology_anyOf_i0_cache_items_path_anyOf_i1)

- Type: null

<a id="headingADDED_fields_topology_anyOf_i0_spares"></a>
<a id="ADDED_fields_topology_anyOf_i0_spares"></a>
###### spares (required)

- Schema name: `Spares`
- Type: array of object

Array of spare disk configurations.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_topology_anyOf_i0_spares_items"></a>
###### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_topology_anyOf_i0_spares_items_name"></a>
<a id="ADDED_fields_topology_anyOf_i0_spares_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

<a id="headingADDED_fields_topology_anyOf_i0_spares_items_vdev_type"></a>
<a id="ADDED_fields_topology_anyOf_i0_spares_items_vdev_type"></a>
###### vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

<a id="headingADDED_fields_topology_anyOf_i0_spares_items_guid"></a>
<a id="ADDED_fields_topology_anyOf_i0_spares_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

<a id="headingADDED_fields_topology_anyOf_i0_spares_items_state"></a>
<a id="ADDED_fields_topology_anyOf_i0_spares_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

<a id="headingADDED_fields_topology_anyOf_i0_spares_items_stats"></a>
<a id="ADDED_fields_topology_anyOf_i0_spares_items_stats"></a>
###### stats (required)

- Type: object

Vdev I/O statistics.

<a id="headingADDED_fields_topology_anyOf_i0_spares_items_children"></a>
<a id="ADDED_fields_topology_anyOf_i0_spares_items_children"></a>
###### children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_topology_anyOf_i0_spares_items_children_items"></a>
- Type: object

<a id="headingADDED_fields_topology_anyOf_i0_spares_items_top_guid"></a>
<a id="ADDED_fields_topology_anyOf_i0_spares_items_top_guid"></a>
###### top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
<a id="ADDED_fields_topology_anyOf_i0_spares_items_top_guid_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_spares_items_top_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_topology_anyOf_i0_spares_items_top_guid_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_spares_items_top_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_topology_anyOf_i0_spares_items_top_guid_anyOf_i1)

- Type: null

<a id="headingADDED_fields_topology_anyOf_i0_spares_items_path"></a>
<a id="ADDED_fields_topology_anyOf_i0_spares_items_path"></a>
###### path

- Schema name: `Path`
- Default: null

Device path stored in the vdev config (e.g. '/dev/disk/by-partuuid/<uuid>'). Unlike `name`, this is preserved for devices that were missing at pool import time. dRAID distributed spares store their synthetic spare name as the config path. `null` for interior vdevs (mirror, raidz, draid) that have no config path.
<a id="ADDED_fields_topology_anyOf_i0_spares_items_path_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_spares_items_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_topology_anyOf_i0_spares_items_path_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_spares_items_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_topology_anyOf_i0_spares_items_path_anyOf_i1)

- Type: null

<a id="headingADDED_fields_topology_anyOf_i0_special"></a>
<a id="ADDED_fields_topology_anyOf_i0_special"></a>
###### special (required)

- Schema name: `Special`
- Type: array of object

Array of special vdev configurations for metadata.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_topology_anyOf_i0_special_items"></a>
###### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_topology_anyOf_i0_special_items_name"></a>
<a id="ADDED_fields_topology_anyOf_i0_special_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

<a id="headingADDED_fields_topology_anyOf_i0_special_items_vdev_type"></a>
<a id="ADDED_fields_topology_anyOf_i0_special_items_vdev_type"></a>
###### vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

<a id="headingADDED_fields_topology_anyOf_i0_special_items_guid"></a>
<a id="ADDED_fields_topology_anyOf_i0_special_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

<a id="headingADDED_fields_topology_anyOf_i0_special_items_state"></a>
<a id="ADDED_fields_topology_anyOf_i0_special_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

<a id="headingADDED_fields_topology_anyOf_i0_special_items_stats"></a>
<a id="ADDED_fields_topology_anyOf_i0_special_items_stats"></a>
###### stats (required)

- Type: object

Vdev I/O statistics.

<a id="headingADDED_fields_topology_anyOf_i0_special_items_children"></a>
<a id="ADDED_fields_topology_anyOf_i0_special_items_children"></a>
###### children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_topology_anyOf_i0_special_items_children_items"></a>
- Type: object

<a id="headingADDED_fields_topology_anyOf_i0_special_items_top_guid"></a>
<a id="ADDED_fields_topology_anyOf_i0_special_items_top_guid"></a>
###### top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
<a id="ADDED_fields_topology_anyOf_i0_special_items_top_guid_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_special_items_top_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_topology_anyOf_i0_special_items_top_guid_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_special_items_top_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_topology_anyOf_i0_special_items_top_guid_anyOf_i1)

- Type: null

<a id="headingADDED_fields_topology_anyOf_i0_special_items_path"></a>
<a id="ADDED_fields_topology_anyOf_i0_special_items_path"></a>
###### path

- Schema name: `Path`
- Default: null

Device path stored in the vdev config (e.g. '/dev/disk/by-partuuid/<uuid>'). Unlike `name`, this is preserved for devices that were missing at pool import time. dRAID distributed spares store their synthetic spare name as the config path. `null` for interior vdevs (mirror, raidz, draid) that have no config path.
<a id="ADDED_fields_topology_anyOf_i0_special_items_path_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_special_items_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_topology_anyOf_i0_special_items_path_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_special_items_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_topology_anyOf_i0_special_items_path_anyOf_i1)

- Type: null

<a id="headingADDED_fields_topology_anyOf_i0_dedup"></a>
<a id="ADDED_fields_topology_anyOf_i0_dedup"></a>
###### dedup (required)

- Schema name: `Dedup`
- Type: array of object

Array of deduplication table vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_topology_anyOf_i0_dedup_items"></a>
###### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_topology_anyOf_i0_dedup_items_name"></a>
<a id="ADDED_fields_topology_anyOf_i0_dedup_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

<a id="headingADDED_fields_topology_anyOf_i0_dedup_items_vdev_type"></a>
<a id="ADDED_fields_topology_anyOf_i0_dedup_items_vdev_type"></a>
###### vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

<a id="headingADDED_fields_topology_anyOf_i0_dedup_items_guid"></a>
<a id="ADDED_fields_topology_anyOf_i0_dedup_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

<a id="headingADDED_fields_topology_anyOf_i0_dedup_items_state"></a>
<a id="ADDED_fields_topology_anyOf_i0_dedup_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

<a id="headingADDED_fields_topology_anyOf_i0_dedup_items_stats"></a>
<a id="ADDED_fields_topology_anyOf_i0_dedup_items_stats"></a>
###### stats (required)

- Type: object

Vdev I/O statistics.

<a id="headingADDED_fields_topology_anyOf_i0_dedup_items_children"></a>
<a id="ADDED_fields_topology_anyOf_i0_dedup_items_children"></a>
###### children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_topology_anyOf_i0_dedup_items_children_items"></a>
- Type: object

<a id="headingADDED_fields_topology_anyOf_i0_dedup_items_top_guid"></a>
<a id="ADDED_fields_topology_anyOf_i0_dedup_items_top_guid"></a>
###### top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
<a id="ADDED_fields_topology_anyOf_i0_dedup_items_top_guid_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_dedup_items_top_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_topology_anyOf_i0_dedup_items_top_guid_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_dedup_items_top_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_topology_anyOf_i0_dedup_items_top_guid_anyOf_i1)

- Type: null

<a id="headingADDED_fields_topology_anyOf_i0_dedup_items_path"></a>
<a id="ADDED_fields_topology_anyOf_i0_dedup_items_path"></a>
###### path

- Schema name: `Path`
- Default: null

Device path stored in the vdev config (e.g. '/dev/disk/by-partuuid/<uuid>'). Unlike `name`, this is preserved for devices that were missing at pool import time. dRAID distributed spares store their synthetic spare name as the config path. `null` for interior vdevs (mirror, raidz, draid) that have no config path.
<a id="ADDED_fields_topology_anyOf_i0_dedup_items_path_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_dedup_items_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_topology_anyOf_i0_dedup_items_path_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_topology_anyOf_i0_dedup_items_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_topology_anyOf_i0_dedup_items_path_anyOf_i1)

- Type: null

<a id="tab-pane_ADDED_fields_topology_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_topology_anyOf_i1)

- Type: null

<a id="headingADDED_fields_scan"></a>
<a id="ADDED_fields_scan"></a>
##### scan

- Default: null

Most recent scrub or resilver information.
<a id="ADDED_fields_scan_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_scan_anyOf_i0"></a>
###### [ZPoolScan](#tab-pane_ADDED_fields_scan_anyOf_i0)

- Schema name: `ZPoolScan`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_scan_anyOf_i0_function"></a>
<a id="ADDED_fields_scan_anyOf_i0_function"></a>
###### function (required)

- Schema name: `Function`
- Type: enum (of string)

Type of ZFS pool scan.
###### Must be one of:

- "RESILVER"
- "SCRUB"

<a id="headingADDED_fields_scan_anyOf_i0_state"></a>
<a id="ADDED_fields_scan_anyOf_i0_state"></a>
###### state (required)

- Schema name: `State`
- Type: enum (of string)

Current lifecycle state of the scan.
###### Must be one of:

- "SCANNING"
- "FINISHED"
- "CANCELED"

<a id="headingADDED_fields_scan_anyOf_i0_start_time"></a>
<a id="ADDED_fields_scan_anyOf_i0_start_time"></a>
###### start_time (required)

- Schema name: `Start Time`
- Type: integer

Scan start time (unix timestamp).

<a id="headingADDED_fields_scan_anyOf_i0_end_time"></a>
<a id="ADDED_fields_scan_anyOf_i0_end_time"></a>
###### end_time (required)

- Schema name: `End Time`

Scan end time as unix timestamp (`null` while the scan is still running).
<a id="ADDED_fields_scan_anyOf_i0_end_time_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_scan_anyOf_i0_end_time_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_scan_anyOf_i0_end_time_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_scan_anyOf_i0_end_time_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_scan_anyOf_i0_end_time_anyOf_i1)

- Type: null

<a id="headingADDED_fields_scan_anyOf_i0_percentage"></a>
<a id="ADDED_fields_scan_anyOf_i0_percentage"></a>
###### percentage (required)

- Schema name: `Percentage`
- Type: number

Scan progress (between 0 and 100%).

<a id="headingADDED_fields_scan_anyOf_i0_bytes_to_process"></a>
<a id="ADDED_fields_scan_anyOf_i0_bytes_to_process"></a>
###### bytes_to_process (required)

- Schema name: `Bytes To Process`
- Type: integer

Total bytes located by scanner.

<a id="headingADDED_fields_scan_anyOf_i0_bytes_processed"></a>
<a id="ADDED_fields_scan_anyOf_i0_bytes_processed"></a>
###### bytes_processed (required)

- Schema name: `Bytes Processed`
- Type: integer

Total bytes to scan.

<a id="headingADDED_fields_scan_anyOf_i0_bytes_issued"></a>
<a id="ADDED_fields_scan_anyOf_i0_bytes_issued"></a>
###### bytes_issued (required)

- Schema name: `Bytes Issued`
- Type: integer

Issued bytes per scan pass.

<a id="headingADDED_fields_scan_anyOf_i0_pause"></a>
<a id="ADDED_fields_scan_anyOf_i0_pause"></a>
###### pause (required)

- Schema name: `Pause`

Pause time as unix timestamp (`null` if the scan is not paused).
<a id="ADDED_fields_scan_anyOf_i0_pause_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_scan_anyOf_i0_pause_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_scan_anyOf_i0_pause_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_scan_anyOf_i0_pause_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_scan_anyOf_i0_pause_anyOf_i1)

- Type: null

<a id="headingADDED_fields_scan_anyOf_i0_errors"></a>
<a id="ADDED_fields_scan_anyOf_i0_errors"></a>
###### errors (required)

- Schema name: `Errors`
- Type: integer

Number of scan errors.

<a id="headingADDED_fields_scan_anyOf_i0_total_secs_left"></a>
<a id="ADDED_fields_scan_anyOf_i0_total_secs_left"></a>
###### total_secs_left (required)

- Schema name: `Total Secs Left`

Number of seconds left (`null` if the scan is not running).
<a id="ADDED_fields_scan_anyOf_i0_total_secs_left_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_scan_anyOf_i0_total_secs_left_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_scan_anyOf_i0_total_secs_left_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_scan_anyOf_i0_total_secs_left_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_scan_anyOf_i0_total_secs_left_anyOf_i1)

- Type: null

<a id="tab-pane_ADDED_fields_scan_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_scan_anyOf_i1)

- Type: null

<a id="headingADDED_fields_expand"></a>
<a id="ADDED_fields_expand"></a>
##### expand

- Default: null

RAIDZ expansion information.
<a id="ADDED_fields_expand_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_expand_anyOf_i0"></a>
###### [ZPoolExpand](#tab-pane_ADDED_fields_expand_anyOf_i0)

- Schema name: `ZPoolExpand`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_expand_anyOf_i0_state"></a>
<a id="ADDED_fields_expand_anyOf_i0_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Expansion state (e.g., SCANNING, FINISHED).

<a id="headingADDED_fields_expand_anyOf_i0_expanding_vdev"></a>
<a id="ADDED_fields_expand_anyOf_i0_expanding_vdev"></a>
###### expanding_vdev (required)

- Schema name: `Expanding Vdev`
- Type: integer

Index of the vdev being expanded.

<a id="headingADDED_fields_expand_anyOf_i0_start_time"></a>
<a id="ADDED_fields_expand_anyOf_i0_start_time"></a>
###### start_time (required)

- Schema name: `Start Time`
- Type: integer

Expansion start time (unix timestamp).

<a id="headingADDED_fields_expand_anyOf_i0_end_time"></a>
<a id="ADDED_fields_expand_anyOf_i0_end_time"></a>
###### end_time (required)

- Schema name: `End Time`

Expansion end time as unix timestamp (`null` while expanding).
<a id="ADDED_fields_expand_anyOf_i0_end_time_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_expand_anyOf_i0_end_time_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_expand_anyOf_i0_end_time_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_expand_anyOf_i0_end_time_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_expand_anyOf_i0_end_time_anyOf_i1)

- Type: null

<a id="headingADDED_fields_expand_anyOf_i0_bytes_to_reflow"></a>
<a id="ADDED_fields_expand_anyOf_i0_bytes_to_reflow"></a>
###### bytes_to_reflow (required)

- Schema name: `Bytes To Reflow`
- Type: integer

Total bytes that need to be reflowed.

<a id="headingADDED_fields_expand_anyOf_i0_bytes_reflowed"></a>
<a id="ADDED_fields_expand_anyOf_i0_bytes_reflowed"></a>
###### bytes_reflowed (required)

- Schema name: `Bytes Reflowed`
- Type: integer

Total bytes reflowed so far.

<a id="headingADDED_fields_expand_anyOf_i0_waiting_for_resilver"></a>
<a id="ADDED_fields_expand_anyOf_i0_waiting_for_resilver"></a>
###### waiting_for_resilver (required)

- Schema name: `Waiting For Resilver`
- Type: integer

Non-zero if expansion is waiting for a resilver to complete.

<a id="headingADDED_fields_expand_anyOf_i0_total_secs_left"></a>
<a id="ADDED_fields_expand_anyOf_i0_total_secs_left"></a>
###### total_secs_left (required)

- Schema name: `Total Secs Left`

Estimated seconds remaining (`null` if not expanding).
<a id="ADDED_fields_expand_anyOf_i0_total_secs_left_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_expand_anyOf_i0_total_secs_left_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_expand_anyOf_i0_total_secs_left_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_expand_anyOf_i0_total_secs_left_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_expand_anyOf_i0_total_secs_left_anyOf_i1)

- Type: null

<a id="headingADDED_fields_expand_anyOf_i0_percentage"></a>
<a id="ADDED_fields_expand_anyOf_i0_percentage"></a>
###### percentage (required)

- Schema name: `Percentage`
- Type: number

Expansion progress (between 0 and 100%).

<a id="tab-pane_ADDED_fields_expand_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_expand_anyOf_i1)

- Type: null

<a id="headingADDED_fields_features"></a>
<a id="ADDED_fields_features"></a>
##### features

- Schema name: `Features`
- Default: null

Pool feature flags.
<a id="ADDED_fields_features_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_features_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_features_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_features_anyOf_i0_items"></a>
###### ZPoolFeature

- Schema name: `ZPoolFeature`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_features_anyOf_i0_items_name"></a>
<a id="ADDED_fields_features_anyOf_i0_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Feature name.

<a id="headingADDED_fields_features_anyOf_i0_items_guid"></a>
<a id="ADDED_fields_features_anyOf_i0_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: string

Feature GUID.

<a id="headingADDED_fields_features_anyOf_i0_items_description"></a>
<a id="ADDED_fields_features_anyOf_i0_items_description"></a>
###### description (required)

- Schema name: `Description`
- Type: string

Feature description.

<a id="headingADDED_fields_features_anyOf_i0_items_state"></a>
<a id="ADDED_fields_features_anyOf_i0_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Feature state.

<a id="tab-pane_ADDED_fields_features_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_features_anyOf_i1)

- Type: null

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `ZPoolQueryChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Database id of the pool.

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `ZPoolEntry`
- Type: object

Event fields.
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id

- Schema name: `Id`
- Default: null

Database id from `storage.volume`. `null` for the boot pool and for any pool not present in the database.
<a id="CHANGED_fields_id_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_id_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_id_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of the zpool.

<a id="headingCHANGED_fields_guid"></a>
<a id="CHANGED_fields_guid"></a>
##### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for the pool.

<a id="headingCHANGED_fields_status"></a>
<a id="CHANGED_fields_status"></a>
##### status (required)

- Schema name: `Status`
- Type: string

Current pool status (ONLINE, DEGRADED, FAULTED, OFFLINE, etc.).

<a id="headingCHANGED_fields_healthy"></a>
<a id="CHANGED_fields_healthy"></a>
##### healthy (required)

- Schema name: `Healthy`
- Type: boolean

Whether the pool is in a healthy state.

<a id="headingCHANGED_fields_warning"></a>
<a id="CHANGED_fields_warning"></a>
##### warning (required)

- Schema name: `Warning`
- Type: boolean

Whether the pool has warning conditions.

<a id="headingCHANGED_fields_status_code"></a>
<a id="CHANGED_fields_status_code"></a>
##### status_code (required)

- Schema name: `Status Code`

Detailed status code (e.g., OK, ERRATA, FEAT*DISABLED, LOCKED*SED_DISKS).
<a id="CHANGED_fields_status_code_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_status_code_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_status_code_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_status_code_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_status_code_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_status_detail"></a>
<a id="CHANGED_fields_status_detail"></a>
##### status_detail (required)

- Schema name: `Status Detail`

Human-readable status description.
<a id="CHANGED_fields_status_detail_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_status_detail_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_status_detail_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_status_detail_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_status_detail_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_is_upgraded"></a>
<a id="CHANGED_fields_is_upgraded"></a>
##### is_upgraded

- Schema name: `Is Upgraded`
- Default: null

Whether every ZFS feature flag on the pool is enabled. `null` for OFFLINE pools.
<a id="CHANGED_fields_is_upgraded_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_is_upgraded_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_is_upgraded_anyOf_i0)

- Type: boolean

<a id="tab-pane_CHANGED_fields_is_upgraded_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_is_upgraded_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_all_sed"></a>
<a id="CHANGED_fields_all_sed"></a>
##### all_sed

- Schema name: `All Sed`
- Default: null

`true` when every disk backing the pool is a Self-Encrypting Drive, `false` when at least one is not. `null` when the SED status of the pool has not yet been determined or does not apply.
<a id="CHANGED_fields_all_sed_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_all_sed_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_all_sed_anyOf_i0)

- Type: boolean

<a id="tab-pane_CHANGED_fields_all_sed_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_all_sed_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_properties"></a>
<a id="CHANGED_fields_properties"></a>
##### properties

- Schema name: `Properties`
- Default: null

Pool properties, keyed by property name.
<a id="CHANGED_fields_properties_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_properties_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_properties_anyOf_i0)

- Type: object
<a id="headingCHANGED_fields_properties_anyOf_i0_additionalProperties"></a>
<a id="CHANGED_fields_properties_anyOf_i0_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Schema name: `ZPoolPropertyValue`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_properties_anyOf_i0_additionalProperties_raw"></a>
<a id="CHANGED_fields_properties_anyOf_i0_additionalProperties_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw string representation of the property.

<a id="headingCHANGED_fields_properties_anyOf_i0_additionalProperties_source"></a>
<a id="CHANGED_fields_properties_anyOf_i0_additionalProperties_source"></a>
###### source (required)

- Schema name: `Source`

The source from where this property received its value (DEFAULT, LOCAL, NONE, etc.).
<a id="CHANGED_fields_properties_anyOf_i0_additionalProperties_source_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_properties_anyOf_i0_additionalProperties_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_properties_anyOf_i0_additionalProperties_source_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_properties_anyOf_i0_additionalProperties_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_properties_anyOf_i0_additionalProperties_source_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_properties_anyOf_i0_additionalProperties_value"></a>
<a id="CHANGED_fields_properties_anyOf_i0_additionalProperties_value"></a>
###### value (required)

- Schema name: `Value`

The native Python value of the property.
<a id="CHANGED_fields_properties_anyOf_i0_additionalProperties_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_properties_anyOf_i0_additionalProperties_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_properties_anyOf_i0_additionalProperties_value_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_properties_anyOf_i0_additionalProperties_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_properties_anyOf_i0_additionalProperties_value_anyOf_i1)

- Type: number

<a id="tab-pane_CHANGED_fields_properties_anyOf_i0_additionalProperties_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_CHANGED_fields_properties_anyOf_i0_additionalProperties_value_anyOf_i2)

- Type: string

<a id="tab-pane_CHANGED_fields_properties_anyOf_i0_additionalProperties_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_CHANGED_fields_properties_anyOf_i0_additionalProperties_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_CHANGED_fields_properties_anyOf_i0_additionalProperties_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_CHANGED_fields_properties_anyOf_i0_additionalProperties_value_anyOf_i4)

- Type: null

<a id="tab-pane_CHANGED_fields_properties_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_properties_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_topology"></a>
<a id="CHANGED_fields_topology"></a>
##### topology

- Default: null

Pool vdev topology.
<a id="CHANGED_fields_topology_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0"></a>
###### [ZPoolTopology](#tab-pane_CHANGED_fields_topology_anyOf_i0)

- Schema name: `ZPoolTopology`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_topology_anyOf_i0_data"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data"></a>
###### data (required)

- Schema name: `Data`
- Type: array of object

Array of data vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_topology_anyOf_i0_data_items"></a>
###### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_name"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_vdev_type"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_vdev_type"></a>
###### vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_guid"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_state"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats"></a>
###### stats (required)

- Schema name: `ZPoolVdevStats`
- Type: object

Vdev I/O statistics.
- No Additional Properties
<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_timestamp"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_timestamp"></a>
###### timestamp

- Schema name: `Timestamp`
- Type: integer
- Default: 0

High-resolution timestamp (nanoseconds).

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_allocated"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_allocated"></a>
###### allocated

- Schema name: `Allocated`
- Type: integer
- Default: 0

Allocated space in bytes.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_space"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_space"></a>
###### space

- Schema name: `Space`
- Type: integer
- Default: 0

Total space in bytes.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_dspace"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_dspace"></a>
###### dspace

- Schema name: `Dspace`
- Type: integer
- Default: 0

Deflated (compressed) space.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_pspace"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_pspace"></a>
###### pspace

- Schema name: `Pspace`
- Type: integer
- Default: 0

Physical space.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_rsize"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_rsize"></a>
###### rsize

- Schema name: `Rsize`
- Type: integer
- Default: 0

Replaceable dev size.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_esize"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_esize"></a>
###### esize

- Schema name: `Esize`
- Type: integer
- Default: 0

Expandable dev size.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_read_errors"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_read_errors"></a>
###### read_errors

- Schema name: `Read Errors`
- Type: integer
- Default: 0

Number of read errors.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_write_errors"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_write_errors"></a>
###### write_errors

- Schema name: `Write Errors`
- Type: integer
- Default: 0

Number of write errors.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_checksum_errors"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_checksum_errors"></a>
###### checksum_errors

- Schema name: `Checksum Errors`
- Type: integer
- Default: 0

Number of checksum errors.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_initialize_errors"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_initialize_errors"></a>
###### initialize_errors

- Schema name: `Initialize Errors`
- Type: integer
- Default: 0

Number of initialize errors.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_dio_verify_errors"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_dio_verify_errors"></a>
###### dio_verify_errors

- Schema name: `Dio Verify Errors`
- Type: integer
- Default: 0

Number of direct I/O verify errors.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_slow_ios"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_slow_ios"></a>
###### slow_ios

- Schema name: `Slow Ios`
- Default: null

Number of slow I/Os.
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_slow_ios_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_stats_slow_ios_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_stats_slow_ios_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_stats_slow_ios_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_stats_slow_ios_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_self_healed_bytes"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_self_healed_bytes"></a>
###### self_healed_bytes

- Schema name: `Self Healed Bytes`
- Type: integer
- Default: 0

Self-healed bytes.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_fragmentation"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_fragmentation"></a>
###### fragmentation

- Schema name: `Fragmentation`
- Type: integer
- Default: 0

Fragmentation percentage.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_scan_processed"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_scan_processed"></a>
###### scan_processed

- Schema name: `Scan Processed`
- Type: integer
- Default: 0

Bytes processed by scan.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_scan_removing"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_scan_removing"></a>
###### scan_removing

- Schema name: `Scan Removing`
- Type: integer
- Default: 0

Bytes processed by removal.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_rebuild_processed"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_rebuild_processed"></a>
###### rebuild_processed

- Schema name: `Rebuild Processed`
- Type: integer
- Default: 0

Bytes processed by rebuild.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_noalloc"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_noalloc"></a>
###### noalloc

- Schema name: `Noalloc`
- Type: integer
- Default: 0

Allocations halted.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_ops_read"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_ops_read"></a>
###### ops_read

- Schema name: `Ops Read`
- Type: integer
- Default: 0

Read operations.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_ops_write"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_ops_write"></a>
###### ops_write

- Schema name: `Ops Write`
- Type: integer
- Default: 0

Write operations.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_bytes_read"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_bytes_read"></a>
###### bytes_read

- Schema name: `Bytes Read`
- Type: integer
- Default: 0

Bytes read.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_bytes_write"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_bytes_write"></a>
###### bytes_write

- Schema name: `Bytes Write`
- Type: integer
- Default: 0

Bytes written.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_configured_ashift"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_configured_ashift"></a>
###### configured_ashift

- Schema name: `Configured Ashift`
- Default: null

Configured ashift value.
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_configured_ashift_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_stats_configured_ashift_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_stats_configured_ashift_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_stats_configured_ashift_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_stats_configured_ashift_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_logical_ashift"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_logical_ashift"></a>
###### logical_ashift

- Schema name: `Logical Ashift`
- Default: null

Logical ashift value.
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_logical_ashift_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_stats_logical_ashift_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_stats_logical_ashift_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_stats_logical_ashift_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_stats_logical_ashift_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_stats_physical_ashift"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_physical_ashift"></a>
###### physical_ashift

- Schema name: `Physical Ashift`
- Default: null

Physical ashift value.
<a id="CHANGED_fields_topology_anyOf_i0_data_items_stats_physical_ashift_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_stats_physical_ashift_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_stats_physical_ashift_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_stats_physical_ashift_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_stats_physical_ashift_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_children"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_children"></a>
###### children (required)

- Schema name: `Children`
- Type: array of object

Child vdevs.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_topology_anyOf_i0_data_items_children_items"></a>
###### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_children_items_name"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_children_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_children_items_vdev_type"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_children_items_vdev_type"></a>
###### vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_children_items_guid"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_children_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_children_items_state"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_children_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_children_items_stats"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_children_items_stats"></a>
###### stats (required)

- Type: object

Vdev I/O statistics.

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_children_items_children"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_children_items_children"></a>
###### children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_topology_anyOf_i0_data_items_children_items_children_items"></a>
- Type: object

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_children_items_top_guid"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_children_items_top_guid"></a>
###### top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
<a id="CHANGED_fields_topology_anyOf_i0_data_items_children_items_top_guid_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_children_items_top_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_children_items_top_guid_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_children_items_top_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_children_items_top_guid_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_children_items_path"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_children_items_path"></a>
###### path

- Schema name: `Path`
- Default: null

Device path stored in the vdev config (e.g. '/dev/disk/by-partuuid/<uuid>'). Unlike `name`, this is preserved for devices that were missing at pool import time. dRAID distributed spares store their synthetic spare name as the config path. `null` for interior vdevs (mirror, raidz, draid) that have no config path.
<a id="CHANGED_fields_topology_anyOf_i0_data_items_children_items_path_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_children_items_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_children_items_path_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_children_items_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_children_items_path_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_top_guid"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_top_guid"></a>
###### top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
<a id="CHANGED_fields_topology_anyOf_i0_data_items_top_guid_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_top_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_top_guid_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_top_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_top_guid_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_topology_anyOf_i0_data_items_path"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data_items_path"></a>
###### path

- Schema name: `Path`
- Default: null

Device path stored in the vdev config (e.g. '/dev/disk/by-partuuid/<uuid>'). Unlike `name`, this is preserved for devices that were missing at pool import time. dRAID distributed spares store their synthetic spare name as the config path. `null` for interior vdevs (mirror, raidz, draid) that have no config path.
<a id="CHANGED_fields_topology_anyOf_i0_data_items_path_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_path_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_topology_anyOf_i0_data_items_path_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_topology_anyOf_i0_log"></a>
<a id="CHANGED_fields_topology_anyOf_i0_log"></a>
###### log (required)

- Schema name: `Log`
- Type: array of object

Array of ZFS Intent Log (ZIL) vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_topology_anyOf_i0_log_items"></a>
###### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_topology_anyOf_i0_log_items_name"></a>
<a id="CHANGED_fields_topology_anyOf_i0_log_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

<a id="headingCHANGED_fields_topology_anyOf_i0_log_items_vdev_type"></a>
<a id="CHANGED_fields_topology_anyOf_i0_log_items_vdev_type"></a>
###### vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

<a id="headingCHANGED_fields_topology_anyOf_i0_log_items_guid"></a>
<a id="CHANGED_fields_topology_anyOf_i0_log_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

<a id="headingCHANGED_fields_topology_anyOf_i0_log_items_state"></a>
<a id="CHANGED_fields_topology_anyOf_i0_log_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

<a id="headingCHANGED_fields_topology_anyOf_i0_log_items_stats"></a>
<a id="CHANGED_fields_topology_anyOf_i0_log_items_stats"></a>
###### stats (required)

- Type: object

Vdev I/O statistics.

<a id="headingCHANGED_fields_topology_anyOf_i0_log_items_children"></a>
<a id="CHANGED_fields_topology_anyOf_i0_log_items_children"></a>
###### children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_topology_anyOf_i0_log_items_children_items"></a>
- Type: object

<a id="headingCHANGED_fields_topology_anyOf_i0_log_items_top_guid"></a>
<a id="CHANGED_fields_topology_anyOf_i0_log_items_top_guid"></a>
###### top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
<a id="CHANGED_fields_topology_anyOf_i0_log_items_top_guid_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_log_items_top_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_topology_anyOf_i0_log_items_top_guid_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_log_items_top_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_topology_anyOf_i0_log_items_top_guid_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_topology_anyOf_i0_log_items_path"></a>
<a id="CHANGED_fields_topology_anyOf_i0_log_items_path"></a>
###### path

- Schema name: `Path`
- Default: null

Device path stored in the vdev config (e.g. '/dev/disk/by-partuuid/<uuid>'). Unlike `name`, this is preserved for devices that were missing at pool import time. dRAID distributed spares store their synthetic spare name as the config path. `null` for interior vdevs (mirror, raidz, draid) that have no config path.
<a id="CHANGED_fields_topology_anyOf_i0_log_items_path_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_log_items_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_topology_anyOf_i0_log_items_path_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_log_items_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_topology_anyOf_i0_log_items_path_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_topology_anyOf_i0_cache"></a>
<a id="CHANGED_fields_topology_anyOf_i0_cache"></a>
###### cache (required)

- Schema name: `Cache`
- Type: array of object

Array of L2ARC cache vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_topology_anyOf_i0_cache_items"></a>
###### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_topology_anyOf_i0_cache_items_name"></a>
<a id="CHANGED_fields_topology_anyOf_i0_cache_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

<a id="headingCHANGED_fields_topology_anyOf_i0_cache_items_vdev_type"></a>
<a id="CHANGED_fields_topology_anyOf_i0_cache_items_vdev_type"></a>
###### vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

<a id="headingCHANGED_fields_topology_anyOf_i0_cache_items_guid"></a>
<a id="CHANGED_fields_topology_anyOf_i0_cache_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

<a id="headingCHANGED_fields_topology_anyOf_i0_cache_items_state"></a>
<a id="CHANGED_fields_topology_anyOf_i0_cache_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

<a id="headingCHANGED_fields_topology_anyOf_i0_cache_items_stats"></a>
<a id="CHANGED_fields_topology_anyOf_i0_cache_items_stats"></a>
###### stats (required)

- Type: object

Vdev I/O statistics.

<a id="headingCHANGED_fields_topology_anyOf_i0_cache_items_children"></a>
<a id="CHANGED_fields_topology_anyOf_i0_cache_items_children"></a>
###### children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_topology_anyOf_i0_cache_items_children_items"></a>
- Type: object

<a id="headingCHANGED_fields_topology_anyOf_i0_cache_items_top_guid"></a>
<a id="CHANGED_fields_topology_anyOf_i0_cache_items_top_guid"></a>
###### top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
<a id="CHANGED_fields_topology_anyOf_i0_cache_items_top_guid_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_cache_items_top_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_topology_anyOf_i0_cache_items_top_guid_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_cache_items_top_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_topology_anyOf_i0_cache_items_top_guid_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_topology_anyOf_i0_cache_items_path"></a>
<a id="CHANGED_fields_topology_anyOf_i0_cache_items_path"></a>
###### path

- Schema name: `Path`
- Default: null

Device path stored in the vdev config (e.g. '/dev/disk/by-partuuid/<uuid>'). Unlike `name`, this is preserved for devices that were missing at pool import time. dRAID distributed spares store their synthetic spare name as the config path. `null` for interior vdevs (mirror, raidz, draid) that have no config path.
<a id="CHANGED_fields_topology_anyOf_i0_cache_items_path_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_cache_items_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_topology_anyOf_i0_cache_items_path_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_cache_items_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_topology_anyOf_i0_cache_items_path_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_topology_anyOf_i0_spares"></a>
<a id="CHANGED_fields_topology_anyOf_i0_spares"></a>
###### spares (required)

- Schema name: `Spares`
- Type: array of object

Array of spare disk configurations.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_topology_anyOf_i0_spares_items"></a>
###### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_topology_anyOf_i0_spares_items_name"></a>
<a id="CHANGED_fields_topology_anyOf_i0_spares_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

<a id="headingCHANGED_fields_topology_anyOf_i0_spares_items_vdev_type"></a>
<a id="CHANGED_fields_topology_anyOf_i0_spares_items_vdev_type"></a>
###### vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

<a id="headingCHANGED_fields_topology_anyOf_i0_spares_items_guid"></a>
<a id="CHANGED_fields_topology_anyOf_i0_spares_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

<a id="headingCHANGED_fields_topology_anyOf_i0_spares_items_state"></a>
<a id="CHANGED_fields_topology_anyOf_i0_spares_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

<a id="headingCHANGED_fields_topology_anyOf_i0_spares_items_stats"></a>
<a id="CHANGED_fields_topology_anyOf_i0_spares_items_stats"></a>
###### stats (required)

- Type: object

Vdev I/O statistics.

<a id="headingCHANGED_fields_topology_anyOf_i0_spares_items_children"></a>
<a id="CHANGED_fields_topology_anyOf_i0_spares_items_children"></a>
###### children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_topology_anyOf_i0_spares_items_children_items"></a>
- Type: object

<a id="headingCHANGED_fields_topology_anyOf_i0_spares_items_top_guid"></a>
<a id="CHANGED_fields_topology_anyOf_i0_spares_items_top_guid"></a>
###### top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
<a id="CHANGED_fields_topology_anyOf_i0_spares_items_top_guid_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_spares_items_top_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_topology_anyOf_i0_spares_items_top_guid_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_spares_items_top_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_topology_anyOf_i0_spares_items_top_guid_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_topology_anyOf_i0_spares_items_path"></a>
<a id="CHANGED_fields_topology_anyOf_i0_spares_items_path"></a>
###### path

- Schema name: `Path`
- Default: null

Device path stored in the vdev config (e.g. '/dev/disk/by-partuuid/<uuid>'). Unlike `name`, this is preserved for devices that were missing at pool import time. dRAID distributed spares store their synthetic spare name as the config path. `null` for interior vdevs (mirror, raidz, draid) that have no config path.
<a id="CHANGED_fields_topology_anyOf_i0_spares_items_path_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_spares_items_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_topology_anyOf_i0_spares_items_path_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_spares_items_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_topology_anyOf_i0_spares_items_path_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_topology_anyOf_i0_special"></a>
<a id="CHANGED_fields_topology_anyOf_i0_special"></a>
###### special (required)

- Schema name: `Special`
- Type: array of object

Array of special vdev configurations for metadata.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_topology_anyOf_i0_special_items"></a>
###### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_topology_anyOf_i0_special_items_name"></a>
<a id="CHANGED_fields_topology_anyOf_i0_special_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

<a id="headingCHANGED_fields_topology_anyOf_i0_special_items_vdev_type"></a>
<a id="CHANGED_fields_topology_anyOf_i0_special_items_vdev_type"></a>
###### vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

<a id="headingCHANGED_fields_topology_anyOf_i0_special_items_guid"></a>
<a id="CHANGED_fields_topology_anyOf_i0_special_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

<a id="headingCHANGED_fields_topology_anyOf_i0_special_items_state"></a>
<a id="CHANGED_fields_topology_anyOf_i0_special_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

<a id="headingCHANGED_fields_topology_anyOf_i0_special_items_stats"></a>
<a id="CHANGED_fields_topology_anyOf_i0_special_items_stats"></a>
###### stats (required)

- Type: object

Vdev I/O statistics.

<a id="headingCHANGED_fields_topology_anyOf_i0_special_items_children"></a>
<a id="CHANGED_fields_topology_anyOf_i0_special_items_children"></a>
###### children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_topology_anyOf_i0_special_items_children_items"></a>
- Type: object

<a id="headingCHANGED_fields_topology_anyOf_i0_special_items_top_guid"></a>
<a id="CHANGED_fields_topology_anyOf_i0_special_items_top_guid"></a>
###### top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
<a id="CHANGED_fields_topology_anyOf_i0_special_items_top_guid_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_special_items_top_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_topology_anyOf_i0_special_items_top_guid_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_special_items_top_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_topology_anyOf_i0_special_items_top_guid_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_topology_anyOf_i0_special_items_path"></a>
<a id="CHANGED_fields_topology_anyOf_i0_special_items_path"></a>
###### path

- Schema name: `Path`
- Default: null

Device path stored in the vdev config (e.g. '/dev/disk/by-partuuid/<uuid>'). Unlike `name`, this is preserved for devices that were missing at pool import time. dRAID distributed spares store their synthetic spare name as the config path. `null` for interior vdevs (mirror, raidz, draid) that have no config path.
<a id="CHANGED_fields_topology_anyOf_i0_special_items_path_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_special_items_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_topology_anyOf_i0_special_items_path_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_special_items_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_topology_anyOf_i0_special_items_path_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_topology_anyOf_i0_dedup"></a>
<a id="CHANGED_fields_topology_anyOf_i0_dedup"></a>
###### dedup (required)

- Schema name: `Dedup`
- Type: array of object

Array of deduplication table vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_topology_anyOf_i0_dedup_items"></a>
###### ZPoolVdev

- Schema name: `ZPoolVdev`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_topology_anyOf_i0_dedup_items_name"></a>
<a id="CHANGED_fields_topology_anyOf_i0_dedup_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Vdev name (e.g., 'mirror-0', '/dev/sda1').

<a id="headingCHANGED_fields_topology_anyOf_i0_dedup_items_vdev_type"></a>
<a id="CHANGED_fields_topology_anyOf_i0_dedup_items_vdev_type"></a>
###### vdev_type (required)

- Schema name: `Vdev Type`
- Type: string

Vdev type (e.g., 'mirror', 'raidz1', 'disk').

<a id="headingCHANGED_fields_topology_anyOf_i0_dedup_items_guid"></a>
<a id="CHANGED_fields_topology_anyOf_i0_dedup_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for this vdev.

<a id="headingCHANGED_fields_topology_anyOf_i0_dedup_items_state"></a>
<a id="CHANGED_fields_topology_anyOf_i0_dedup_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Current state (ONLINE, DEGRADED, FAULTED, OFFLINE, UNAVAIL, etc.).

<a id="headingCHANGED_fields_topology_anyOf_i0_dedup_items_stats"></a>
<a id="CHANGED_fields_topology_anyOf_i0_dedup_items_stats"></a>
###### stats (required)

- Type: object

Vdev I/O statistics.

<a id="headingCHANGED_fields_topology_anyOf_i0_dedup_items_children"></a>
<a id="CHANGED_fields_topology_anyOf_i0_dedup_items_children"></a>
###### children (required)

- Schema name: `Children`
- Type: array

Child vdevs.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_topology_anyOf_i0_dedup_items_children_items"></a>
- Type: object

<a id="headingCHANGED_fields_topology_anyOf_i0_dedup_items_top_guid"></a>
<a id="CHANGED_fields_topology_anyOf_i0_dedup_items_top_guid"></a>
###### top_guid

- Schema name: `Top Guid`
- Default: null

GUID of the top-level vdev this belongs to.
<a id="CHANGED_fields_topology_anyOf_i0_dedup_items_top_guid_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_dedup_items_top_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_topology_anyOf_i0_dedup_items_top_guid_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_dedup_items_top_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_topology_anyOf_i0_dedup_items_top_guid_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_topology_anyOf_i0_dedup_items_path"></a>
<a id="CHANGED_fields_topology_anyOf_i0_dedup_items_path"></a>
###### path

- Schema name: `Path`
- Default: null

Device path stored in the vdev config (e.g. '/dev/disk/by-partuuid/<uuid>'). Unlike `name`, this is preserved for devices that were missing at pool import time. dRAID distributed spares store their synthetic spare name as the config path. `null` for interior vdevs (mirror, raidz, draid) that have no config path.
<a id="CHANGED_fields_topology_anyOf_i0_dedup_items_path_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_dedup_items_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_topology_anyOf_i0_dedup_items_path_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0_dedup_items_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_topology_anyOf_i0_dedup_items_path_anyOf_i1)

- Type: null

<a id="tab-pane_CHANGED_fields_topology_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_topology_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_scan"></a>
<a id="CHANGED_fields_scan"></a>
##### scan

- Default: null

Most recent scrub or resilver information.
<a id="CHANGED_fields_scan_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_scan_anyOf_i0"></a>
###### [ZPoolScan](#tab-pane_CHANGED_fields_scan_anyOf_i0)

- Schema name: `ZPoolScan`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_scan_anyOf_i0_function"></a>
<a id="CHANGED_fields_scan_anyOf_i0_function"></a>
###### function (required)

- Schema name: `Function`
- Type: enum (of string)

Type of ZFS pool scan.
###### Must be one of:

- "RESILVER"
- "SCRUB"

<a id="headingCHANGED_fields_scan_anyOf_i0_state"></a>
<a id="CHANGED_fields_scan_anyOf_i0_state"></a>
###### state (required)

- Schema name: `State`
- Type: enum (of string)

Current lifecycle state of the scan.
###### Must be one of:

- "SCANNING"
- "FINISHED"
- "CANCELED"

<a id="headingCHANGED_fields_scan_anyOf_i0_start_time"></a>
<a id="CHANGED_fields_scan_anyOf_i0_start_time"></a>
###### start_time (required)

- Schema name: `Start Time`
- Type: integer

Scan start time (unix timestamp).

<a id="headingCHANGED_fields_scan_anyOf_i0_end_time"></a>
<a id="CHANGED_fields_scan_anyOf_i0_end_time"></a>
###### end_time (required)

- Schema name: `End Time`

Scan end time as unix timestamp (`null` while the scan is still running).
<a id="CHANGED_fields_scan_anyOf_i0_end_time_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_scan_anyOf_i0_end_time_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_scan_anyOf_i0_end_time_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_scan_anyOf_i0_end_time_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_scan_anyOf_i0_end_time_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_scan_anyOf_i0_percentage"></a>
<a id="CHANGED_fields_scan_anyOf_i0_percentage"></a>
###### percentage (required)

- Schema name: `Percentage`
- Type: number

Scan progress (between 0 and 100%).

<a id="headingCHANGED_fields_scan_anyOf_i0_bytes_to_process"></a>
<a id="CHANGED_fields_scan_anyOf_i0_bytes_to_process"></a>
###### bytes_to_process (required)

- Schema name: `Bytes To Process`
- Type: integer

Total bytes located by scanner.

<a id="headingCHANGED_fields_scan_anyOf_i0_bytes_processed"></a>
<a id="CHANGED_fields_scan_anyOf_i0_bytes_processed"></a>
###### bytes_processed (required)

- Schema name: `Bytes Processed`
- Type: integer

Total bytes to scan.

<a id="headingCHANGED_fields_scan_anyOf_i0_bytes_issued"></a>
<a id="CHANGED_fields_scan_anyOf_i0_bytes_issued"></a>
###### bytes_issued (required)

- Schema name: `Bytes Issued`
- Type: integer

Issued bytes per scan pass.

<a id="headingCHANGED_fields_scan_anyOf_i0_pause"></a>
<a id="CHANGED_fields_scan_anyOf_i0_pause"></a>
###### pause (required)

- Schema name: `Pause`

Pause time as unix timestamp (`null` if the scan is not paused).
<a id="CHANGED_fields_scan_anyOf_i0_pause_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_scan_anyOf_i0_pause_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_scan_anyOf_i0_pause_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_scan_anyOf_i0_pause_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_scan_anyOf_i0_pause_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_scan_anyOf_i0_errors"></a>
<a id="CHANGED_fields_scan_anyOf_i0_errors"></a>
###### errors (required)

- Schema name: `Errors`
- Type: integer

Number of scan errors.

<a id="headingCHANGED_fields_scan_anyOf_i0_total_secs_left"></a>
<a id="CHANGED_fields_scan_anyOf_i0_total_secs_left"></a>
###### total_secs_left (required)

- Schema name: `Total Secs Left`

Number of seconds left (`null` if the scan is not running).
<a id="CHANGED_fields_scan_anyOf_i0_total_secs_left_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_scan_anyOf_i0_total_secs_left_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_scan_anyOf_i0_total_secs_left_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_scan_anyOf_i0_total_secs_left_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_scan_anyOf_i0_total_secs_left_anyOf_i1)

- Type: null

<a id="tab-pane_CHANGED_fields_scan_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_scan_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_expand"></a>
<a id="CHANGED_fields_expand"></a>
##### expand

- Default: null

RAIDZ expansion information.
<a id="CHANGED_fields_expand_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_expand_anyOf_i0"></a>
###### [ZPoolExpand](#tab-pane_CHANGED_fields_expand_anyOf_i0)

- Schema name: `ZPoolExpand`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_expand_anyOf_i0_state"></a>
<a id="CHANGED_fields_expand_anyOf_i0_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Expansion state (e.g., SCANNING, FINISHED).

<a id="headingCHANGED_fields_expand_anyOf_i0_expanding_vdev"></a>
<a id="CHANGED_fields_expand_anyOf_i0_expanding_vdev"></a>
###### expanding_vdev (required)

- Schema name: `Expanding Vdev`
- Type: integer

Index of the vdev being expanded.

<a id="headingCHANGED_fields_expand_anyOf_i0_start_time"></a>
<a id="CHANGED_fields_expand_anyOf_i0_start_time"></a>
###### start_time (required)

- Schema name: `Start Time`
- Type: integer

Expansion start time (unix timestamp).

<a id="headingCHANGED_fields_expand_anyOf_i0_end_time"></a>
<a id="CHANGED_fields_expand_anyOf_i0_end_time"></a>
###### end_time (required)

- Schema name: `End Time`

Expansion end time as unix timestamp (`null` while expanding).
<a id="CHANGED_fields_expand_anyOf_i0_end_time_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_expand_anyOf_i0_end_time_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_expand_anyOf_i0_end_time_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_expand_anyOf_i0_end_time_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_expand_anyOf_i0_end_time_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_expand_anyOf_i0_bytes_to_reflow"></a>
<a id="CHANGED_fields_expand_anyOf_i0_bytes_to_reflow"></a>
###### bytes_to_reflow (required)

- Schema name: `Bytes To Reflow`
- Type: integer

Total bytes that need to be reflowed.

<a id="headingCHANGED_fields_expand_anyOf_i0_bytes_reflowed"></a>
<a id="CHANGED_fields_expand_anyOf_i0_bytes_reflowed"></a>
###### bytes_reflowed (required)

- Schema name: `Bytes Reflowed`
- Type: integer

Total bytes reflowed so far.

<a id="headingCHANGED_fields_expand_anyOf_i0_waiting_for_resilver"></a>
<a id="CHANGED_fields_expand_anyOf_i0_waiting_for_resilver"></a>
###### waiting_for_resilver (required)

- Schema name: `Waiting For Resilver`
- Type: integer

Non-zero if expansion is waiting for a resilver to complete.

<a id="headingCHANGED_fields_expand_anyOf_i0_total_secs_left"></a>
<a id="CHANGED_fields_expand_anyOf_i0_total_secs_left"></a>
###### total_secs_left (required)

- Schema name: `Total Secs Left`

Estimated seconds remaining (`null` if not expanding).
<a id="CHANGED_fields_expand_anyOf_i0_total_secs_left_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_expand_anyOf_i0_total_secs_left_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_expand_anyOf_i0_total_secs_left_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_expand_anyOf_i0_total_secs_left_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_expand_anyOf_i0_total_secs_left_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_expand_anyOf_i0_percentage"></a>
<a id="CHANGED_fields_expand_anyOf_i0_percentage"></a>
###### percentage (required)

- Schema name: `Percentage`
- Type: number

Expansion progress (between 0 and 100%).

<a id="tab-pane_CHANGED_fields_expand_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_expand_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_features"></a>
<a id="CHANGED_fields_features"></a>
##### features

- Schema name: `Features`
- Default: null

Pool feature flags.
<a id="CHANGED_fields_features_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_features_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_features_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_features_anyOf_i0_items"></a>
###### ZPoolFeature

- Schema name: `ZPoolFeature`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_features_anyOf_i0_items_name"></a>
<a id="CHANGED_fields_features_anyOf_i0_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Feature name.

<a id="headingCHANGED_fields_features_anyOf_i0_items_guid"></a>
<a id="CHANGED_fields_features_anyOf_i0_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: string

Feature GUID.

<a id="headingCHANGED_fields_features_anyOf_i0_items_description"></a>
<a id="CHANGED_fields_features_anyOf_i0_items_description"></a>
###### description (required)

- Schema name: `Description`
- Type: string

Feature description.

<a id="headingCHANGED_fields_features_anyOf_i0_items_state"></a>
<a id="CHANGED_fields_features_anyOf_i0_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Feature state.

<a id="tab-pane_CHANGED_fields_features_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_features_anyOf_i1)

- Type: null

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `ZPoolQueryRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Database id of the pool.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
