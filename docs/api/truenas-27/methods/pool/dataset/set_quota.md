---
title: pool.dataset.set_quota
kind: method
source_rst: _sources/api_methods_pool.dataset.set_quota.rst.txt
source_html: api_methods_pool.dataset.set_quota.html
required_roles:
  - DATASET_WRITE
---

# pool.dataset.set_quota

## Summary

Allow users to set multiple quotas simultaneously by submitting a list of quotas.

## Required Roles

- `DATASET_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: dataset

<a id="Call_parameters_items_i0"></a>
#### dataset

- Schema name: `dataset`
- Type: string

The name of the target ZFS dataset.

#### Parameter 2: quotas

<a id="Call_parameters_items_i1"></a>
#### quotas

- Schema name: `quotas`
- Type: array of object
- Default:
```json
[
  {
    "quota_type": "USER",
    "id": "0",
    "quota_value": 0
  }
]
```

Specify an array of quota entries to apply to dataset. The array may contain all supported quota types.
- Must contain a maximum of `100` items
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i1_items"></a>
##### PoolDatasetSetQuota

- Schema name: `PoolDatasetSetQuota`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i1_items_quota_type"></a>
<a id="Call_parameters_items_i1_items_quota_type"></a>
###### quota_type (required)

- Schema name: `Quota Type`
- Type: enum (of string)

The type of quota to apply to the dataset. There are three over-arching types of quotas for ZFS datasets: **Dataset quotas and refquotas.** If a `DATASET` quota type is specified in this API call, then the API acts as a wrapper for `pool.dataset.update`. **User and group quotas.** These limit the amount of disk space consumed by files that are owned by the specified users or groups. If the respective "object quota" type is specfied, then the quota limits the number of objects that may be owned by the specified user or group. **Project quotas.** These limit the amount of disk space consumed by files that are owned by the specified project. *Project quotas are not yet implemented.*
###### Must be one of:

- "DATASET"
- "USER"
- "USEROBJ"
- "GROUP"
- "GROUPOBJ"

<a id="headingCall_parameters_items_i1_items_id"></a>
<a id="Call_parameters_items_i1_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: string

The UID, GID, or name to which the quota applies. If `quota_type` is 'DATASET', then `id` must be either `QUOTA` or `REFQUOTA`.

<a id="headingCall_parameters_items_i1_items_quota_value"></a>
<a id="Call_parameters_items_i1_items_quota_value"></a>
###### quota_value (required)

- Schema name: `Quota Value`

The quota size in bytes. Setting a value of `0` removes the user or group quota.
<a id="Call_parameters_items_i1_items_quota_value_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_items_quota_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_items_quota_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i1_items_quota_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_items_quota_value_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful quota update.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
