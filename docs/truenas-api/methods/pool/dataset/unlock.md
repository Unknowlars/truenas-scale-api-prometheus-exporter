---
title: pool.dataset.unlock
kind: method
source_rst: _sources/api_methods_pool.dataset.unlock.rst.txt
source_html: api_methods_pool.dataset.unlock.html
required_roles:
  - DATASET_WRITE
---

# pool.dataset.unlock

## Summary

Unlock dataset `id` (and its children if `unlock_options.recursive` is `true`).

If `id` dataset is not encrypted an exception will be raised. There is one exception: when `id` is a root dataset and `unlock_options.recursive` is specified, encryption validation will not be performed for `id`. This allow unlocking encrypted children for the entire pool `id`.

There are two ways to supply the key(s)/passphrase(s) for unlocking a dataset:

1. Upload a json file which contains encrypted dataset keys (it will be read from the input pipe if `unlock_options.key_file` is `true`). The format is the one that is used for exporting encrypted dataset keys (`pool.export_keys`).

2. Specify a key or a passphrase for each unlocked dataset using `unlock_options.datasets`.

This method is a job.

*This job CAN be used with file upload.* See :ref:`uploading-files`.

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

The dataset ID (full path) to unlock.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

Options for unlocking including force settings, recursion, and dataset-specific keys.
- No Additional Properties
##### force

- Schema name: `Force`
- Type: boolean
- Default: false

In some cases it's possible that the provided key/passphrase is valid but the path where the dataset is supposed to be mounted after being unlocked already exists and is not empty. In this case, unlock operation would fail. This can be overridden by setting `datasets.X.force` boolean flag or by setting `force` flag. When any of these flags are set, system will rename the existing directory/file path where the dataset should be mounted resulting in successful unlock of the dataset.

##### key_file

- Schema name: `Key File`
- Type: boolean
- Default: false

Whether to use a key file instead of a passphrase for unlocking encrypted datasets.

##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively unlock child datasets.

##### toggle_attachments

- Schema name: `Toggle Attachments`
- Type: boolean
- Default: true

Whether attachments should be put in action after unlocking the dataset(s). Toggling attachments can theoretically lead to service interruption when daemons configurations are reloaded (this should not happen, and if this happens it should be considered a bug). As TrueNAS does not have a state for resources that should be unlocked but are still locked, disabling this option will put the system into an inconsistent state so it should really never be disabled.

##### datasets

- Schema name: `Datasets`
- Type: array of object
- Default: []

List of specific datasets with their individual unlock options.
- No Additional Items

###### Each item of this array must be:

###### PoolDatasetUnlockOptionsDataset

- Schema name: `PoolDatasetUnlockOptionsDataset`
- Type: object
- No Additional Properties
####### force

- Schema name: `Force`
- Type: boolean
- Default: false

Force unlock even if the mount path already exists and is not empty.

####### name (required)

- Schema name: `Name`
- Type: string

The dataset name to unlock.
- Must be at least `1` characters long

####### key

- Schema name: `Key`
- Type: string

Raw hex-encoded encryption key for this dataset.
- Must be at least `64` characters long
- Must be at most `64` characters long

####### passphrase

- Schema name: `Passphrase`
- Type: string

Passphrase for this dataset if using passphrase-based encryption.
- Must be at least `1` characters long

####### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Apply the key or passphrase to all encrypted children.

### Return value

- Schema name: `PoolDatasetUnlock`
- Type: object

Results of the unlock operation including successful and failed datasets.
- No Additional Properties
#### unlocked (required)

- Schema name: `Unlocked`
- Type: array of string

Array of dataset names that were successfully unlocked.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### failed (required)

- Schema name: `Failed`
- Type: object

Object containing datasets that failed to unlock and their respective error messages.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
