---
title: failover.upgrade
kind: method
source_rst: _sources/api_methods_failover.upgrade.rst.txt
source_html: api_methods_failover.upgrade.html
required_roles:
  - FAILOVER_WRITE
---

# failover.upgrade

## Summary

Upgrades both controllers. Files will be downloaded to the Active Controller and then transferred to the Standby Controller. Upgrade process will start concurrently on both nodes. Once both upgrades are applied, the Standby Controller will reboot. This job will wait for that job to complete before finalizing.

This method is a job.

*This job CAN be used with file upload.* See :ref:`uploading-files`.

## Required Roles

- `FAILOVER_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: failover_upgrade

#### failover_upgrade

- Schema name: `failover_upgrade`
- Type: object
- Default:
```json
{
  "train": null,
  "version": null,
  "resume": false,
  "resume_manual": false
}
```

Failover upgrade configuration options.
- No Additional Properties
##### train

- Schema name: `Train`
- Default: null

Update train to use for the upgrade or `null` for default.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### version

- Schema name: `Version`
- Default: null

Specific version to upgrade to or `null` for latest.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### resume

- Schema name: `Resume`
- Type: boolean
- Default: false

Should be set to true if a previous call to this method returned a `CallError` with `errno=EAGAIN` meaning that an upgrade can be performed with a warning and that warning is accepted. In that case, you also have to set `resume_manual` to `true` if a previous call to this method was performed using update file upload.

##### resume_manual

- Schema name: `Resume Manual`
- Type: boolean
- Default: false

Whether to resume a manual upgrade operation.

### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` when the failover upgrade is successfully initiated.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
