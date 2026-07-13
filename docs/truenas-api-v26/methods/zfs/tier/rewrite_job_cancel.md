---
title: zfs.tier.rewrite_job_cancel
kind: method
source_rst: _sources/api_methods_zfs.tier.rewrite_job_cancel.rst.txt
source_html: api_methods_zfs.tier.rewrite_job_cancel.html
required_roles:
  - DATASET_WRITE
---

# zfs.tier.rewrite_job_cancel

## Summary

Cancel a running or queued rewrite job.

## Required Roles

- `DATASET_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: zfs_tier_rewrite_job_cancel

#### zfs_tier_rewrite_job_cancel

- Schema name: `zfs_tier_rewrite_job_cancel`
- Type: object

ZfsTierRewriteJobCancelArgs parameters.
- No Additional Properties
##### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job to cancel, in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the job has been successfully cancelled.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
