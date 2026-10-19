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

*This job CAN be used with file upload.* See [uploading-files](../../shared/jobs.md#uploading-files).

## Required Roles

- `FAILOVER_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: failover_upgrade

<a id="Call_parameters_items_i0"></a>
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
<a id="headingCall_parameters_items_i0_train"></a>
<a id="Call_parameters_items_i0_train"></a>
##### train

- Schema name: `Train`
- Default: null

Update train to use for the upgrade or `null` for default.
<a id="Call_parameters_items_i0_train_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_train_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_train_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_train_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_train_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_version"></a>
<a id="Call_parameters_items_i0_version"></a>
##### version

- Schema name: `Version`
- Default: null

Specific version to upgrade to or `null` for latest.
<a id="Call_parameters_items_i0_version_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_version_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_version_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_resume"></a>
<a id="Call_parameters_items_i0_resume"></a>
##### resume

- Schema name: `Resume`
- Type: boolean
- Default: false

Should be set to true if a previous call to this method returned a `CallError` with `errno=EAGAIN` meaning that an upgrade can be performed with a warning and that warning is accepted. In that case, you also have to set `resume_manual` to `true` if a previous call to this method was performed using update file upload.

<a id="headingCall_parameters_items_i0_resume_manual"></a>
<a id="Call_parameters_items_i0_resume_manual"></a>
##### resume_manual

- Schema name: `Resume Manual`
- Type: boolean
- Default: false

Whether to resume a manual upgrade operation.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` when the failover upgrade is successfully initiated.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
