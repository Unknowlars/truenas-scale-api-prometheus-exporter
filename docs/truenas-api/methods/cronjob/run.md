---
title: cronjob.run
kind: method
source_rst: _sources/api_methods_cronjob.run.rst.txt
source_html: api_methods_cronjob.run.html
required_roles:
  - SYSTEM_CRON_WRITE
---

# cronjob.run

## Summary

Job to run cronjob task of `id`.

This method is a job.

## Required Roles

- `SYSTEM_CRON_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the cron job to run immediately.

#### Parameter 2: skip_disabled

#### skip_disabled

- Schema name: `skip_disabled`
- Type: boolean
- Default: false

Whether to skip execution if the cron job is disabled.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the cron job is successfully started.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
