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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: dataset

#### dataset

- Schema name: `dataset`
- Type: string

The name of the target ZFS dataset.

#### Parameter 2: quotas

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

##### PoolDatasetSetQuota

- Schema name: `PoolDatasetSetQuota`
- Type: object
- No Additional Properties
###### quota_type (required)

- Schema name: `Quota Type`
- Type: enum (of string)

The type of quota to apply to the dataset. There are three over-arching types of quotas for ZFS datasets: **Dataset quotas and refquotas.** If a `DATASET` quota type is specified in this API call, then the API acts as a wrapper for `pool.dataset.update`. **User and group quotas.** These limit the amount of disk space consumed by files that are owned by the specified users or groups. If the respective "object quota" type is specfied, then the quota limits the number of objects that may be owned by the specified user or group. **Project quotas.** These limit the amount of disk space consumed by files that are owned by the specified project. *Project quotas are not yet implemented.*

###### id (required)

- Schema name: `Id`
- Type: string

The UID, GID, or name to which the quota applies. If `quota_type` is 'DATASET', then `id` must be either `QUOTA` or `REFQUOTA`.

###### quota_value (required)

- Schema name: `Quota Value`

The quota size in bytes. Setting a value of `0` removes the user or group quota.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful quota update.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
