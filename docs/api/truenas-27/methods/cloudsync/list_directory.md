---
title: cloudsync.list_directory
kind: method
source_rst: _sources/api_methods_cloudsync.list_directory.rst.txt
source_html: api_methods_cloudsync.list_directory.html
required_roles:
  - CLOUD_SYNC_WRITE
---

# cloudsync.list_directory

## Summary

List contents of a remote bucket / directory.

If remote supports buckets, path is constructed by two keys "bucket"/"folder" in `attributes`. If remote does not support buckets, path is constructed using "folder" key only in `attributes`. "folder" is directory name and "bucket" is bucket name for remote.

Path examples:

S3 Service `bucketname/directory/name`

Dropbox Service `directory/name`

`credentials` is a valid id of a Cloud Sync Credential which will be used to connect to the provider.

## Required Roles

- `CLOUD_SYNC_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: cloud_sync_ls

<a id="Call_parameters_items_i0"></a>
#### cloud_sync_ls

- Schema name: `cloud_sync_ls`
- Type: object

CloudSyncListDirectoryArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_credentials"></a>
<a id="Call_parameters_items_i0_credentials"></a>
##### credentials (required)

- Schema name: `Credentials`
- Type: integer

ID of the cloud credential to use for directory listing.

<a id="headingCall_parameters_items_i0_encryption"></a>
<a id="Call_parameters_items_i0_encryption"></a>
##### encryption

- Schema name: `Encryption`
- Type: boolean
- Default: false

Whether files are encrypted in cloud storage.

<a id="headingCall_parameters_items_i0_filename_encryption"></a>
<a id="Call_parameters_items_i0_filename_encryption"></a>
##### filename_encryption

- Schema name: `Filename Encryption`
- Type: boolean
- Default: false

Whether filenames are encrypted in cloud storage.

<a id="headingCall_parameters_items_i0_encryption_password"></a>
<a id="Call_parameters_items_i0_encryption_password"></a>
##### encryption_password

- Schema name: `Encryption Password`
- Type: string
- Default: ""

Password for decrypting files and filenames.

<a id="headingCall_parameters_items_i0_encryption_salt"></a>
<a id="Call_parameters_items_i0_encryption_salt"></a>
##### encryption_salt

- Schema name: `Encryption Salt`
- Type: string
- Default: ""

Salt value for encryption key derivation.

<a id="headingCall_parameters_items_i0_attributes"></a>
<a id="Call_parameters_items_i0_attributes"></a>
##### attributes (required)

- Schema name: `CloudTaskAttributes`
- Type: object

Cloud provider-specific attributes for the listing operation.
- No Additional Properties
<a id="headingCall_parameters_items_i0_attributes_bucket"></a>
<a id="Call_parameters_items_i0_attributes_bucket"></a>
###### bucket

- Schema name: `Bucket`
- Type: string

Name of the cloud storage bucket or container.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_attributes_folder"></a>
<a id="Call_parameters_items_i0_attributes_folder"></a>
###### folder

- Schema name: `Folder`
- Type: string

Path within the cloud storage bucket to use as the root directory for operations.

<a id="headingCall_parameters_items_i0_attributes_fast_list"></a>
<a id="Call_parameters_items_i0_attributes_fast_list"></a>
###### fast_list

- Schema name: `Fast List`
- Type: boolean

Valid only for some providers. Use fewer transactions in exchange for more RAM. This may also speed up or slow down your transfer. See https://rclone.org/docs/#fast-list for more details.

<a id="headingCall_parameters_items_i0_attributes_bucket_policy_only"></a>
<a id="Call_parameters_items_i0_attributes_bucket_policy_only"></a>
###### bucket_policy_only

- Schema name: `Bucket Policy Only`
- Type: boolean

Valid only for GOOGLE*CLOUD*STORAGE provider. Access checks should use bucket-level IAM policies. If you want to upload objects to a bucket with Bucket Policy Only set then you will need to set this.

<a id="headingCall_parameters_items_i0_attributes_chunk_size"></a>
<a id="Call_parameters_items_i0_attributes_chunk_size"></a>
###### chunk_size

- Schema name: `Chunk Size`
- Type: integer

Valid only for DROPBOX provider. Upload chunk size in MiB. Must fit in memory. Note that these chunks are buffered in memory and there might be a maximum of `--transfers` chunks in progress at once. Dropbox Business accounts can have monthly data transfer limits per team per month. By using larger chunk sizes you will decrease the number of data transfer calls used and you'll be able to transfer more data to your Dropbox Business account.

<a id="headingCall_parameters_items_i0_attributes_acknowledge_abuse"></a>
<a id="Call_parameters_items_i0_attributes_acknowledge_abuse"></a>
###### acknowledge_abuse

- Schema name: `Acknowledge Abuse`
- Type: boolean

Valid only for GOOGLE_DRIVER provider. Allow files which return cannotDownloadAbusiveFile to be downloaded. If downloading a file returns the error "This file has been identified as malware or spam and cannot be downloaded" with the error code "cannotDownloadAbusiveFile" then enable this flag to indicate you acknowledge the risks of downloading the file and TrueNAS will download it anyway.

<a id="headingCall_parameters_items_i0_attributes_region"></a>
<a id="Call_parameters_items_i0_attributes_region"></a>
###### region

- Schema name: `Region`
- Type: string

Valid only for S3 provider. S3 Region.

<a id="headingCall_parameters_items_i0_attributes_encryption"></a>
<a id="Call_parameters_items_i0_attributes_encryption"></a>
###### encryption

- Schema name: `Encryption`
- Type: enum (of null or string)

Valid only for S3 provider. Server-Side Encryption.
###### Must be one of:

- null
- "AES256"

<a id="headingCall_parameters_items_i0_attributes_storage_class"></a>
<a id="Call_parameters_items_i0_attributes_storage_class"></a>
###### storage_class

- Schema name: `Storage Class`
- Type: enum (of string)

Valid only for S3 provider. The storage class to use.
###### Must be one of:

- ""
- "STANDARD"
- "REDUCED_REDUNDANCY"
- "STANDARD_IA"
- "ONEZONE_IA"
- "INTELLIGENT_TIERING"
- "GLACIER"
- "GLACIER_IR"
- "DEEP_ARCHIVE"

<a id="headingCall_parameters_items_i0_args"></a>
<a id="Call_parameters_items_i0_args"></a>
##### args

- Schema name: `Args`
- Type: string
- Default: ""

Additional arguments for the directory listing command.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of object

Array of file and directory information objects.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
