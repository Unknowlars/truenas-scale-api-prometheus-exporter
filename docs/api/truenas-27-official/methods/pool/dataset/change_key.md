---
title: pool.dataset.change_key
kind: method
source_rst: _sources/api_methods_pool.dataset.change_key.rst.txt
source_html: api_methods_pool.dataset.change_key.html
required_roles:
  - DATASET_WRITE
---

# pool.dataset.change_key

## Summary

Change encryption properties for the `id` encrypted dataset.

Changing dataset encryption to use a passphrase instead of a key is not allowed if:

1. It has encrypted roots as children that are encrypted with a key. 2. It is a root dataset where the system dataset is located.

This method is a job.

*This job CAN be used with file upload.* See [uploading-files](../../../shared/jobs.md#uploading-files).

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

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: string

The dataset ID (full path) to change the encryption key for.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Configuration options for changing the encryption key.
- No Additional Properties
<a id="headingCall_parameters_items_i1_generate_key"></a>
<a id="Call_parameters_items_i1_generate_key"></a>
##### generate_key

- Schema name: `Generate Key`
- Type: boolean
- Default: false

Generate a new random encryption key instead of using a provided key or passphrase.

<a id="headingCall_parameters_items_i1_key_file"></a>
<a id="Call_parameters_items_i1_key_file"></a>
##### key_file

- Schema name: `Key File`
- Type: boolean
- Default: false

Whether the provided key is from a key file rather than entered directly.

<a id="headingCall_parameters_items_i1_pbkdf2iters"></a>
<a id="Call_parameters_items_i1_pbkdf2iters"></a>
##### pbkdf2iters

- Schema name: `Pbkdf2Iters`
- Type: integer
- Default: 1300000

Number of PBKDF2 iterations for passphrase-based keys. Higher values improve security against brute force attacks but increase unlock time.
- Value must be greater or equal to `1300000`

<a id="headingCall_parameters_items_i1_passphrase"></a>
<a id="Call_parameters_items_i1_passphrase"></a>
##### passphrase

- Schema name: `Passphrase`
- Default: ""

Passphrase to use for encryption key derivation.
<a id="Call_parameters_items_i1_passphrase_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_passphrase_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_passphrase_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i1_passphrase_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_passphrase_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_key"></a>
<a id="Call_parameters_items_i1_key"></a>
##### key

- Schema name: `Key`
- Default: ""

Raw hex-encoded encryption key.
<a id="Call_parameters_items_i1_key_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_key_anyOf_i0)

- Type: string
- Must be at least `64` characters long
- Must be at most `64` characters long

<a id="tab-pane_Call_parameters_items_i1_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_key_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful key change.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
