---
title: pool.attach
kind: method
source_rst: _sources/api_methods_pool.attach.rst.txt
source_html: api_methods_pool.attach.html
required_roles:
  - POOL_WRITE
---

# pool.attach

## Summary

Attach a disk to an existing vdev in a pool, converting a striped vdev to a mirror or extending an existing mirror to an n-way mirror.

This operation will format the new disk, attach it to the target vdev, and wait for resilvering to complete if the target is a RAIDZ vdev undergoing expansion.

Locking behavior:

- If another attach operation is already using the same disk, this call will fail immediately with EBUSY rather than queueing. - If another attach operation is running on the same pool (but with a different disk), this call will queue and wait for the previous operation to complete. - Operations on different pools with different disks can run concurrently.

This method is a job.

## Required Roles

- `POOL_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: oid

<a id="Call_parameters_items_i0"></a>
#### oid

- Schema name: `oid`
- Type: integer

ID of the pool to attach a disk to.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Configuration for the disk attachment operation.
- No Additional Properties
<a id="headingCall_parameters_items_i1_target_vdev"></a>
<a id="Call_parameters_items_i1_target_vdev"></a>
##### target_vdev (required)

- Schema name: `Target Vdev`
- Type: string

GUID or device name of the target vdev to attach to.

<a id="headingCall_parameters_items_i1_new_disk"></a>
<a id="Call_parameters_items_i1_new_disk"></a>
##### new_disk (required)

- Schema name: `New Disk`
- Type: string

Name of the new disk to attach.

<a id="headingCall_parameters_items_i1_allow_duplicate_serials"></a>
<a id="Call_parameters_items_i1_allow_duplicate_serials"></a>
##### allow_duplicate_serials

- Schema name: `Allow Duplicate Serials`
- Type: boolean
- Default: false

Whether to allow attaching disks with duplicate serial numbers.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful disk attachment.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
