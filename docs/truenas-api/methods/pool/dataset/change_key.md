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

Change encryption properties for `id` encrypted dataset.

Changing dataset encryption to use passphrase instead of a key is not allowed if:

1) It has encrypted roots as children which are encrypted with a key 2) If it is a root dataset where the system dataset is located

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

The dataset ID (full path) to change the encryption key for.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

Configuration options for changing the encryption key.
- No Additional Properties
##### generate_key

- Schema name: `Generate Key`
- Type: boolean
- Default: false

Generate a new random encryption key instead of using a provided key or passphrase.

##### key_file

- Schema name: `Key File`
- Type: boolean
- Default: false

Whether the provided key is from a key file rather than entered directly.

##### pbkdf2iters

- Schema name: `Pbkdf2Iters`
- Type: integer
- Default: 350000

Number of PBKDF2 iterations for passphrase-based keys. Higher values improve security against brute force attacks but increase unlock time. Default 350,000 balances security and performance.
- Value must be greater or equal to `100000`

##### passphrase

- Schema name: `Passphrase`
- Default: null

Passphrase to use for encryption key derivation.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### key

- Schema name: `Key`
- Default: null

Raw hex-encoded encryption key.
###### Any of

####### Option 1

- Type: string
- Must be at least `64` characters long
- Must be at most `64` characters long

####### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful key change.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
