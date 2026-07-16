---
title: zfs.tier.update
kind: method
source_rst: _sources/api_methods_zfs.tier.update.rst.txt
source_html: api_methods_zfs.tier.update.html
required_roles:
  - DATASET_WRITE
---

# zfs.tier.update

## Summary

Update the global ZFS tiering configuration.

Controls whether tiering is enabled, how many rewrite jobs may run concurrently, the filesystem usage threshold at which rewrites are aborted, and the percentage of PERFORMANCE tier space reserved for metadata. Applying the new configuration regenerates the `truenas_zfstierd` daemon configuration and reloads (or restarts, if `max_concurrent_jobs` changed) the daemon.

ZFS tiering requires a license. A JSON-RPC `error` response (code `-32001`, *Method call error*) is returned when the system is not licensed for this feature.

## Required Roles

- `DATASET_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: zfs_tier_update

#### zfs_tier_update

- Schema name: `zfs_tier_update`
- Type: object

ZfsTierUpdateArgs parameters.
- No Additional Properties
##### enabled

- Schema name: `Enabled`
- Type: boolean

Whether the ZFS tier service is enabled.

##### max_concurrent_jobs

- Schema name: `Max Concurrent Jobs`
- Type: integer

Maximum number of rewrite jobs that execute simultaneously. Jobs submitted beyond this limit are held in a QUEUED state until a slot becomes available (1-10).
- Value must be greater or equal to `1` and lesser or equal to `10`

##### max_used_percentage

- Schema name: `Max Used Percentage`
- Type: integer

Abort rewrites when filesystem usage reaches this percentage threshold (70-95).
- Value must be greater or equal to `70` and lesser or equal to `95`

##### special_class_metadata_reserve_pct

- Schema name: `Special Class Metadata Reserve Pct`
- Type: integer

Percentage of PERFORMANCE tier space reserved for metadata. Metadata is always written to the PERFORMANCE tier, but data is only placed there while allocated space stays below `100 - special_class_metadata_reserve_pct` percent of total PERFORMANCE tier capacity. Beyond that threshold data falls back to the REGULAR tier. Corresponds to the ZFS kernel parameter `zfs_special_class_metadata_reserve_pct` (default: 25).
- Value must be greater or equal to `10` and lesser or equal to `30`

### Return value

- Schema name: `ZfsTierEntry`
- Type: object

The updated ZFS tier daemon configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Placeholder identifier. Not used; there is only one configuration instance.

#### enabled (required)

- Schema name: `Enabled`
- Type: boolean

Whether the ZFS tier service is enabled.

#### max_concurrent_jobs (required)

- Schema name: `Max Concurrent Jobs`
- Type: integer

Maximum number of rewrite jobs that execute simultaneously. Jobs submitted beyond this limit are held in a QUEUED state until a slot becomes available (1-10).
- Value must be greater or equal to `1` and lesser or equal to `10`

#### max_used_percentage (required)

- Schema name: `Max Used Percentage`
- Type: integer

Abort rewrites when filesystem usage reaches this percentage threshold (70-95).
- Value must be greater or equal to `70` and lesser or equal to `95`

#### special_class_metadata_reserve_pct (required)

- Schema name: `Special Class Metadata Reserve Pct`
- Type: integer

Percentage of PERFORMANCE tier space reserved for metadata. Metadata is always written to the PERFORMANCE tier, but data is only placed there while allocated space stays below `100 - special_class_metadata_reserve_pct` percent of total PERFORMANCE tier capacity. Beyond that threshold data falls back to the REGULAR tier. Corresponds to the ZFS kernel parameter `zfs_special_class_metadata_reserve_pct` (default: 25).
- Value must be greater or equal to `10` and lesser or equal to `30`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
