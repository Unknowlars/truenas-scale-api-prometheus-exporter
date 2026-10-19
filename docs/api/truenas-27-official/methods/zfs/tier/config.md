---
title: zfs.tier.config
kind: method
source_rst: _sources/api_methods_zfs.tier.config.rst.txt
source_html: api_methods_zfs.tier.config.html
required_roles:
  - ZFS_RESOURCE_READ
---

# zfs.tier.config

## Required Roles

- `ZFS_RESOURCE_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `ZfsTierEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Placeholder identifier. Not used; there is only one configuration instance.

<a id="headingReturn_value_enabled"></a>
<a id="Return_value_enabled"></a>
#### enabled (required)

- Schema name: `Enabled`
- Type: boolean

Whether the ZFS tier service is enabled.

<a id="headingReturn_value_max_concurrent_jobs"></a>
<a id="Return_value_max_concurrent_jobs"></a>
#### max_concurrent_jobs (required)

- Schema name: `Max Concurrent Jobs`
- Type: integer

Maximum number of rewrite jobs that execute simultaneously. Jobs submitted beyond this limit are held in a QUEUED state until a slot becomes available (1-10).
- Value must be greater or equal to `1` and lesser or equal to `10`

<a id="headingReturn_value_max_used_percentage"></a>
<a id="Return_value_max_used_percentage"></a>
#### max_used_percentage (required)

- Schema name: `Max Used Percentage`
- Type: integer

Abort rewrites when filesystem usage reaches this percentage threshold (70-95).
- Value must be greater or equal to `70` and lesser or equal to `95`

<a id="headingReturn_value_special_class_metadata_reserve_pct"></a>
<a id="Return_value_special_class_metadata_reserve_pct"></a>
#### special_class_metadata_reserve_pct (required)

- Schema name: `Special Class Metadata Reserve Pct`
- Type: integer

Percentage of PERFORMANCE tier space reserved for metadata. Metadata is always written to the PERFORMANCE tier, but data is only placed there while allocated space stays below `100 - special_class_metadata_reserve_pct` percent of total PERFORMANCE tier capacity. Beyond that threshold data falls back to the REGULAR tier. Corresponds to the ZFS kernel parameter `zfs_special_class_metadata_reserve_pct` (default: 25).
- Value must be greater or equal to `10` and lesser or equal to `30`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
