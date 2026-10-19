---
title: pool.dataset.encryption_summary
kind: method
source_rst: _sources/api_methods_pool.dataset.encryption_summary.rst.txt
source_html: api_methods_pool.dataset.encryption_summary.html
required_roles:
  - DATASET_READ
---

# pool.dataset.encryption_summary

## Summary

Retrieve summary of all encrypted roots under `id`.

Keys/passphrase can be supplied to check if the keys are valid.

Example output::

[ { "name": "vol", "key_format": "PASSPHRASE", "key_present_in_database": false, "valid_key": true, "locked": true, "unlock_error": null, "unlock_successful": true }, { "name": "vol/c1/d1", "key_format": "PASSPHRASE", "key_present_in_database": false, "valid_key": false, "locked": true, "unlock_error": "Provided key is invalid", "unlock_successful": false }, { "name": "vol/c", "key_format": "PASSPHRASE", "key_present_in_database": false, "valid_key": false, "locked": true, "unlock_error": "Key not provided", "unlock_successful": false }, { "name": "vol/c/d2", "key_format": "PASSPHRASE", "key_present_in_database": false, "valid_key": false, "locked": true, "unlock_error": "Child cannot be unlocked when parent "vol/c" is locked and key is invalid", "unlock_successful": false } ]

This method is a job.

*This job CAN be used with file upload.* See [uploading-files](../../../shared/jobs.md#uploading-files).

## Required Roles

- `DATASET_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: string

The dataset ID (full path) to generate an encryption summary for.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Options for generating the encryption summary including force settings and datasets.
- No Additional Properties
<a id="headingCall_parameters_items_i1_key_file"></a>
<a id="Call_parameters_items_i1_key_file"></a>
##### key_file

- Schema name: `Key File`
- Type: boolean
- Default: false

Whether keys are provided via key files rather than directly.

<a id="headingCall_parameters_items_i1_force"></a>
<a id="Call_parameters_items_i1_force"></a>
##### force

- Schema name: `Force`
- Type: boolean
- Default: false

Force unlock operations even if mount paths already exist.

<a id="headingCall_parameters_items_i1_datasets"></a>
<a id="Call_parameters_items_i1_datasets"></a>
##### datasets

- Schema name: `Datasets`
- Type: array of object
- Default: []

Array of dataset-specific unlock options and credentials.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_datasets_items"></a>
###### PoolDatasetEncryptionSummaryOptionsDataset

- Schema name: `PoolDatasetEncryptionSummaryOptionsDataset`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i1_datasets_items_force"></a>
<a id="Call_parameters_items_i1_datasets_items_force"></a>
###### force

- Schema name: `Force`
- Type: boolean
- Default: false

Force unlock even if the mount path already exists and is not empty.

<a id="headingCall_parameters_items_i1_datasets_items_name"></a>
<a id="Call_parameters_items_i1_datasets_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

The dataset name to unlock.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i1_datasets_items_key"></a>
<a id="Call_parameters_items_i1_datasets_items_key"></a>
###### key

- Schema name: `Key`
- Type: string

Raw hex-encoded encryption key for this dataset.
- Must be at least `64` characters long
- Must be at most `64` characters long

<a id="headingCall_parameters_items_i1_datasets_items_passphrase"></a>
<a id="Call_parameters_items_i1_datasets_items_passphrase"></a>
###### passphrase

- Schema name: `Passphrase`
- Type: string

Passphrase for this dataset if using passphrase-based encryption.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of object

Array of encryption status information for datasets that would be affected by an unlock operation.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### PoolDatasetEncryptionSummary

- Schema name: `PoolDatasetEncryptionSummary`
- Type: object

There are 2 keys which show if a recursive unlock operation is done for `id`, which dataset will be unlocked and if not why it won't be unlocked. The keys namely are `unlock_successful` and `unlock_error`. The former is a boolean value showing if unlock would succeed/fail. The latter is description why it failed if it failed. In some cases it's possible that the provided key/passphrase is valid but the path where the dataset is supposed to be mounted after being unlocked already exists and is not empty. In this case, unlock operation would fail and `unlock_error` will reflect this error appropriately. This can be overridden by setting `options.datasets.X.force` boolean flag or by setting `options.force` flag. In practice, when the dataset is going to be unlocked and these flags have been provided to `pool.dataset.unlock`, system will rename the directory/file path where the dataset should be mounted resulting in successful unlock of the dataset. If a dataset is already unlocked, it will show up as true for "unlock*successful" regardless of what key user provided as the unlock keys in the output are to reflect what a real unlock operation would behave. If user is interested in seeing if a provided key is valid or not, then the key to look out for in the output is "valid*key" which based on what system has in database or if a user provided one, validates the key and sets a boolean value for the dataset.
- No Additional Properties
<a id="headingReturn_value_items_name"></a>
<a id="Return_value_items_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

The dataset name.

<a id="headingReturn_value_items_key_format"></a>
<a id="Return_value_items_key_format"></a>
##### key_format (required)

- Schema name: `Key Format`
- Type: string

The format of the encryption key (hex, raw, or passphrase).

<a id="headingReturn_value_items_key_present_in_database"></a>
<a id="Return_value_items_key_present_in_database"></a>
##### key_present_in_database (required)

- Schema name: `Key Present In Database`
- Type: boolean

Whether an encryption key for this dataset exists in the system database.

<a id="headingReturn_value_items_valid_key"></a>
<a id="Return_value_items_valid_key"></a>
##### valid_key (required)

- Schema name: `Valid Key`
- Type: boolean

Whether the provided key is valid for this dataset.

<a id="headingReturn_value_items_locked"></a>
<a id="Return_value_items_locked"></a>
##### locked (required)

- Schema name: `Locked`
- Type: boolean

Whether the dataset is currently locked.

<a id="headingReturn_value_items_unlock_error"></a>
<a id="Return_value_items_unlock_error"></a>
##### unlock_error (required)

- Schema name: `Unlock Error`

Error message if unlock would fail, or `null` if unlock would succeed.
<a id="Return_value_items_unlock_error_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_unlock_error_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_unlock_error_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_unlock_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_unlock_error_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_unlock_successful"></a>
<a id="Return_value_items_unlock_successful"></a>
##### unlock_successful (required)

- Schema name: `Unlock Successful`
- Type: boolean

Whether an unlock operation would be successful.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
