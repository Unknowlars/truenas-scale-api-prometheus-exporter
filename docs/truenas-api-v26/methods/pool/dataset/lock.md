---
title: pool.dataset.lock
kind: method
source_rst: _sources/api_methods_pool.dataset.lock.rst.txt
source_html: api_methods_pool.dataset.lock.html
required_roles:
  - DATASET_WRITE
---

# pool.dataset.lock

## Summary

Locks `id` dataset. It will unmount the dataset and its children before locking.

After the dataset has been unmounted, system will set immutable flag on the dataset's mountpoint where the dataset was mounted before it was locked making sure that the path cannot be modified. Once the dataset is unlocked, it will not be affected by this change and consumers can continue consuming it.

This method is a job.

## Required Roles

- `DATASET_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: string

The dataset ID (full path) to lock.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

Options for locking the dataset, such as force unmount settings.
- No Additional Properties
##### force_umount

- Schema name: `Force Umount`
- Type: boolean
- Default: false

Force unmounting of the dataset before locking.

### Return value

- Schema name: `Result`
- Type: const

Dataset is locked.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
