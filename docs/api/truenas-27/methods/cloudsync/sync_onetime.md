---
title: cloudsync.sync_onetime
kind: method
source_rst: _sources/api_methods_cloudsync.sync_onetime.rst.txt
source_html: api_methods_cloudsync.sync_onetime.html
required_roles:
  - CLOUD_SYNC_WRITE
---

# cloudsync.sync_onetime

## Summary

Run cloud sync task without creating it.

This method is a job.

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

#### Parameter 1: cloud_sync_sync_onetime

<a id="Call_parameters_items_i0"></a>
#### cloud_sync_sync_onetime

- Schema name: `cloud_sync_sync_onetime`
- Type: object

Cloud sync task configuration for one-time execution.
- No Additional Properties
<a id="headingCall_parameters_items_i0_description"></a>
<a id="Call_parameters_items_i0_description"></a>
##### description

- Schema name: `Description`
- Type: string
- Default: ""

The name of the task to display in the UI.

<a id="headingCall_parameters_items_i0_path"></a>
<a id="Call_parameters_items_i0_path"></a>
##### path (required)

- Schema name: `Path`
- Type: string

The local path to back up beginning with `/mnt` or `/dev/zvol`.

<a id="headingCall_parameters_items_i0_credentials"></a>
<a id="Call_parameters_items_i0_credentials"></a>
##### credentials (required)

- Schema name: `Credentials`
- Type: integer

ID of the cloud credential.

<a id="headingCall_parameters_items_i0_attributes"></a>
<a id="Call_parameters_items_i0_attributes"></a>
##### attributes (required)

- Schema name: `CloudTaskAttributes`
- Type: object

Additional information for each backup, e.g. bucket name.
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

<a id="headingCall_parameters_items_i0_schedule"></a>
<a id="Call_parameters_items_i0_schedule"></a>
##### schedule

- Schema name: `CloudCron`
- Type: object

Cron schedule dictating when the task should run.
- No Additional Properties
<a id="headingCall_parameters_items_i0_schedule_minute"></a>
<a id="Call_parameters_items_i0_schedule_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

<a id="headingCall_parameters_items_i0_schedule_hour"></a>
<a id="Call_parameters_items_i0_schedule_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingCall_parameters_items_i0_schedule_dom"></a>
<a id="Call_parameters_items_i0_schedule_dom"></a>
###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingCall_parameters_items_i0_schedule_month"></a>
<a id="Call_parameters_items_i0_schedule_month"></a>
###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingCall_parameters_items_i0_schedule_dow"></a>
<a id="Call_parameters_items_i0_schedule_dow"></a>
###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingCall_parameters_items_i0_pre_script"></a>
<a id="Call_parameters_items_i0_pre_script"></a>
##### pre_script

- Schema name: `Pre Script`
- Type: string
- Default: ""

A Bash script to run immediately before every backup.

<a id="headingCall_parameters_items_i0_post_script"></a>
<a id="Call_parameters_items_i0_post_script"></a>
##### post_script

- Schema name: `Post Script`
- Type: string
- Default: ""

A Bash script to run immediately after every backup if it succeeds.

<a id="headingCall_parameters_items_i0_snapshot"></a>
<a id="Call_parameters_items_i0_snapshot"></a>
##### snapshot

- Schema name: `Snapshot`
- Type: boolean
- Default: false

Whether to create a temporary snapshot of the dataset before every backup.

<a id="headingCall_parameters_items_i0_include"></a>
<a id="Call_parameters_items_i0_include"></a>
##### include

- Schema name: `Include`
- Type: array of string

Paths to pass to `restic backup --include`.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_include_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_exclude"></a>
<a id="Call_parameters_items_i0_exclude"></a>
##### exclude

- Schema name: `Exclude`
- Type: array of string

Paths to pass to `restic backup --exclude`.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_exclude_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_args"></a>
<a id="Call_parameters_items_i0_args"></a>
##### args

- Schema name: `Args`
- Type: string
- Default: ""

(Slated for removal).

<a id="headingCall_parameters_items_i0_enabled"></a>
<a id="Call_parameters_items_i0_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Can enable/disable the task.

<a id="headingCall_parameters_items_i0_bwlimit"></a>
<a id="Call_parameters_items_i0_bwlimit"></a>
##### bwlimit

- Schema name: `Bwlimit`
- Type: array of object

Schedule of bandwidth limits.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_bwlimit_items"></a>
###### CloudSyncBwlimit

- Schema name: `CloudSyncBwlimit`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_bwlimit_items_time"></a>
<a id="Call_parameters_items_i0_bwlimit_items_time"></a>
###### time (required)

- Schema name: `Time`
- Type: string

Time at which the bandwidth limit takes effect in 24-hour format.
Examples:

```json
"00:00"
```
Examples:

```json
"06:30"
```
Examples:

```json
"18:00"
```
Examples:

```json
"23:00"
```

<a id="headingCall_parameters_items_i0_bwlimit_items_bandwidth"></a>
<a id="Call_parameters_items_i0_bwlimit_items_bandwidth"></a>
###### bandwidth (required)

- Schema name: `Bandwidth`

Bandwidth limit in bytes per second (upload and download).
<a id="Call_parameters_items_i0_bwlimit_items_bandwidth_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_bwlimit_items_bandwidth_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_bwlimit_items_bandwidth_anyOf_i0)

- Type: integer
- Value must be strictly greater than `0`

<a id="tab-pane_Call_parameters_items_i0_bwlimit_items_bandwidth_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_bwlimit_items_bandwidth_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_transfers"></a>
<a id="Call_parameters_items_i0_transfers"></a>
##### transfers

- Schema name: `Transfers`
- Default: null

Maximum number of parallel file transfers. `null` for default.
<a id="Call_parameters_items_i0_transfers_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_transfers_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_transfers_anyOf_i0)

- Type: integer
- Value must be strictly greater than `0`

<a id="tab-pane_Call_parameters_items_i0_transfers_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_transfers_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_direction"></a>
<a id="Call_parameters_items_i0_direction"></a>
##### direction (required)

- Schema name: `Direction`
- Type: enum (of string)

Direction of the cloud sync operation. `PUSH`: Upload local files to cloud storage `PULL`: Download files from cloud storage to local storage
###### Must be one of:

- "PUSH"
- "PULL"

<a id="headingCall_parameters_items_i0_transfer_mode"></a>
<a id="Call_parameters_items_i0_transfer_mode"></a>
##### transfer_mode (required)

- Schema name: `Transfer Mode`
- Type: enum (of string)

How files are transferred between local and cloud storage. `SYNC`: Synchronize directories (add new, update changed, remove deleted) `COPY`: Copy files without removing any existing files `MOVE`: Move files (copy then delete from source)
###### Must be one of:

- "SYNC"
- "COPY"
- "MOVE"

<a id="headingCall_parameters_items_i0_encryption"></a>
<a id="Call_parameters_items_i0_encryption"></a>
##### encryption

- Schema name: `Encryption`
- Type: boolean
- Default: false

Whether to encrypt files before uploading to cloud storage.

<a id="headingCall_parameters_items_i0_filename_encryption"></a>
<a id="Call_parameters_items_i0_filename_encryption"></a>
##### filename_encryption

- Schema name: `Filename Encryption`
- Type: boolean
- Default: false

Whether to encrypt filenames in addition to file contents.

<a id="headingCall_parameters_items_i0_encryption_password"></a>
<a id="Call_parameters_items_i0_encryption_password"></a>
##### encryption_password

- Schema name: `Encryption Password`
- Type: string
- Default: ""

Password for client-side encryption. Empty string if encryption is disabled.

<a id="headingCall_parameters_items_i0_encryption_salt"></a>
<a id="Call_parameters_items_i0_encryption_salt"></a>
##### encryption_salt

- Schema name: `Encryption Salt`
- Type: string
- Default: ""

Salt value for encryption key derivation. Empty string if encryption is disabled.

<a id="headingCall_parameters_items_i0_create_empty_src_dirs"></a>
<a id="Call_parameters_items_i0_create_empty_src_dirs"></a>
##### create_empty_src_dirs

- Schema name: `Create Empty Src Dirs`
- Type: boolean
- Default: false

Whether to create empty directories in the destination that exist in the source.

<a id="headingCall_parameters_items_i0_follow_symlinks"></a>
<a id="Call_parameters_items_i0_follow_symlinks"></a>
##### follow_symlinks

- Schema name: `Follow Symlinks`
- Type: boolean
- Default: false

Whether to follow symbolic links and sync the files they point to.

#### Parameter 2: cloud_sync_sync_onetime_options

<a id="Call_parameters_items_i1"></a>
#### cloud_sync_sync_onetime_options

- Schema name: `cloud_sync_sync_onetime_options`
- Type: object

Options for the one-time sync operation.
- No Additional Properties
<a id="headingCall_parameters_items_i1_dry_run"></a>
<a id="Call_parameters_items_i1_dry_run"></a>
##### dry_run

- Schema name: `Dry Run`
- Type: boolean
- Default: false

Whether to perform a dry run without making actual changes.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the one-time sync operation is successfully started.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
