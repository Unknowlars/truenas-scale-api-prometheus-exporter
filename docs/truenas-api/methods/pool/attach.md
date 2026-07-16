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

Locking behavior: - If another attach operation is already using the same disk, this call will fail immediately with EBUSY rather than queueing. - If another attach operation is running on the same pool (but with a different disk), this call will queue and wait for the previous operation to complete. - Operations on different pools with different disks can run concurrently.

This method is a job.

## Required Roles

- `POOL_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: oid

#### oid

- Schema name: `oid`
- Type: integer

ID of the pool to attach a disk to.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

Configuration for the disk attachment operation.
- No Additional Properties
##### target_vdev (required)

- Schema name: `Target Vdev`
- Type: string

The GUID of the vdev where the disk needs to be attached. In the case of a STRIPED vdev, this is the STRIPED disk GUID which will be converted into a mirror. If `target_vdev` is already a mirror, it will be converted into an n-way mirror.

##### new_disk (required)

- Schema name: `New Disk`
- Type: string

Name of the new disk to attach.

##### allow_duplicate_serials

- Schema name: `Allow Duplicate Serials`
- Type: boolean
- Default: false

Whether to allow attaching disks with duplicate serial numbers.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful disk attachment.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
