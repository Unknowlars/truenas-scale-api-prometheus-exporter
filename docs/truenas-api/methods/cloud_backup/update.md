---
title: cloud_backup.update
kind: method
source_rst: _sources/api_methods_cloud_backup.update.rst.txt
source_html: api_methods_cloud_backup.update.html
required_roles:
  - CLOUD_BACKUP_WRITE
---

# cloud_backup.update

## Summary

Update the cloud backup entry `id` with `data`.

## Required Roles

- `CLOUD_BACKUP_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the cloud backup task to update.

#### Parameter 2: data

#### data

- Schema name: `data`
- Type: object

Updated configuration data for the cloud backup task.
- No Additional Properties
##### description

- Schema name: `Description`
- Type: string

The name of the task to display in the UI.

##### path

- Schema name: `Path`
- Type: string

The local path to back up beginning with `/mnt` or `/dev/zvol`.

##### credentials

- Schema name: `Credentials`
- Type: integer

ID of the cloud credential to use for each backup.

##### attributes

- Schema name: `CloudTaskAttributes`
- Type: object

Additional information for each backup, e.g. bucket name.
- No Additional Properties
###### bucket

- Schema name: `Bucket`
- Type: string

Name of the cloud storage bucket or container.
- Must be at least `1` characters long

###### folder

- Schema name: `Folder`
- Type: string

Path within the cloud storage bucket to use as the root directory for operations.

###### fast_list

- Schema name: `Fast List`
- Type: boolean

Valid only for some providers. Use fewer transactions in exchange for more RAM. This may also speed up or slow down your transfer. See https://rclone.org/docs/#fast-list for more details.

###### bucket_policy_only

- Schema name: `Bucket Policy Only`
- Type: boolean

Valid only for GOOGLE*CLOUD*STORAGE provider. Access checks should use bucket-level IAM policies. If you want to upload objects to a bucket with Bucket Policy Only set then you will need to set this.

###### chunk_size

- Schema name: `Chunk Size`
- Type: integer

Valid only for DROPBOX provider. Upload chunk size in MiB. Must fit in memory. Note that these chunks are buffered in memory and there might be a maximum of `--transfers` chunks in progress at once. Dropbox Business accounts can have monthly data transfer limits per team per month. By using larger chunk sizes you will decrease the number of data transfer calls used and you'll be able to transfer more data to your Dropbox Business account.

###### acknowledge_abuse

- Schema name: `Acknowledge Abuse`
- Type: boolean

Valid only for GOOGLE_DRIVER provider. Allow files which return cannotDownloadAbusiveFile to be downloaded. If downloading a file returns the error "This file has been identified as malware or spam and cannot be downloaded" with the error code "cannotDownloadAbusiveFile" then enable this flag to indicate you acknowledge the risks of downloading the file and TrueNAS will download it anyway.

###### region

- Schema name: `Region`
- Type: string

Valid only for S3 provider. S3 Region.

###### encryption

- Schema name: `Encryption`
- Type: enum (of null or string)

Valid only for S3 provider. Server-Side Encryption.

###### storage_class

- Schema name: `Storage Class`
- Type: enum (of string)

Valid only for S3 provider. The storage class to use.

##### schedule

- Schema name: `CloudCron`
- Type: object

Cron schedule dictating when the task should run.
- No Additional Properties
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23"

###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31"

###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December)

###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday)

##### pre_script

- Schema name: `Pre Script`
- Type: string

A Bash script to run immediately before every backup.

##### post_script

- Schema name: `Post Script`
- Type: string

A Bash script to run immediately after every backup if it succeeds.

##### snapshot

- Schema name: `Snapshot`
- Type: boolean

Whether to create a temporary snapshot of the dataset before every backup.

##### include

- Schema name: `Include`
- Type: array of string

Paths to pass to `restic backup --include`.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

##### exclude

- Schema name: `Exclude`
- Type: array of string

Paths to pass to `restic backup --exclude`.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

##### args

- Schema name: `Args`
- Type: string

(Slated for removal).

##### enabled

- Schema name: `Enabled`
- Type: boolean

Can enable/disable the task.

##### password

- Schema name: `Password`
- Type: string

Password for the remote repository.
- Must be at least `1` characters long

##### keep_last

- Schema name: `Keep Last`
- Type: integer

How many of the most recent backup snapshots to keep after each backup.
- Value must be strictly greater than `0`

##### transfer_setting

- Schema name: `Transfer Setting`
- Type: enum (of string)

DEFAULT: pack size given by `$RESTIC_PACK_SIZE` (default 16 MiB) read concurrency given by `$RESTIC_READ_CONCURRENCY` (default 2 files) PERFORMANCE: pack size = 29 MiB read concurrency given by `$RESTIC_READ_CONCURRENCY` (default 2 files) FAST_STORAGE: pack size = 58 MiB read concurrency = 100 files

##### cache_path

- Schema name: `Cache Path`

Cache path. If not set, performance may degrade.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### rate_limit

- Schema name: `Rate Limit`

Maximum upload/download rate in KiB/s. Passed to `restic --limit-upload` on `cloud_backup.sync` and `restic --limit-download` on `cloud_backup.restore`. `null` indicates no rate limit will be imposed. Can be overridden on a sync or restore call.
###### Any of

####### Option 1

- Type: integer
- Value must be strictly greater than `0`

####### Option 2

- Type: null

### Return value

- Schema name: `CloudBackupEntry`
- Type: object

The updated cloud backup task.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this cloud storage configuration.

#### description

- Schema name: `Description`
- Type: string
- Default: ""

The name of the task to display in the UI.

#### path (required)

- Schema name: `Path`
- Type: string

The local path to back up beginning with `/mnt` or `/dev/zvol`.

#### credentials (required)

- Schema name: `CloudCredentialEntry`
- Type: object

Cloud credentials to use for each backup.
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the cloud credential.

##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the cloud credential.
- Must be at least `1` characters long

##### provider (required)

- Schema name: `Provider`

Cloud provider configuration including type and authentication details.

#### attributes (required)

- Schema name: `CloudTaskAttributes`
- Type: object

Additional information for each backup, e.g. bucket name.
- No Additional Properties
##### bucket

- Schema name: `Bucket`
- Type: string

Name of the cloud storage bucket or container.
- Must be at least `1` characters long

##### folder

- Schema name: `Folder`
- Type: string

Path within the cloud storage bucket to use as the root directory for operations.

##### fast_list

- Schema name: `Fast List`
- Type: boolean

Valid only for some providers. Use fewer transactions in exchange for more RAM. This may also speed up or slow down your transfer. See https://rclone.org/docs/#fast-list for more details.

##### bucket_policy_only

- Schema name: `Bucket Policy Only`
- Type: boolean

Valid only for GOOGLE*CLOUD*STORAGE provider. Access checks should use bucket-level IAM policies. If you want to upload objects to a bucket with Bucket Policy Only set then you will need to set this.

##### chunk_size

- Schema name: `Chunk Size`
- Type: integer

Valid only for DROPBOX provider. Upload chunk size in MiB. Must fit in memory. Note that these chunks are buffered in memory and there might be a maximum of `--transfers` chunks in progress at once. Dropbox Business accounts can have monthly data transfer limits per team per month. By using larger chunk sizes you will decrease the number of data transfer calls used and you'll be able to transfer more data to your Dropbox Business account.

##### acknowledge_abuse

- Schema name: `Acknowledge Abuse`
- Type: boolean

Valid only for GOOGLE_DRIVER provider. Allow files which return cannotDownloadAbusiveFile to be downloaded. If downloading a file returns the error "This file has been identified as malware or spam and cannot be downloaded" with the error code "cannotDownloadAbusiveFile" then enable this flag to indicate you acknowledge the risks of downloading the file and TrueNAS will download it anyway.

##### region

- Schema name: `Region`
- Type: string

Valid only for S3 provider. S3 Region.

##### encryption

- Schema name: `Encryption`
- Type: enum (of null or string)

Valid only for S3 provider. Server-Side Encryption.

##### storage_class

- Schema name: `Storage Class`
- Type: enum (of string)

Valid only for S3 provider. The storage class to use.

#### schedule

- Schema name: `CloudCron`
- Type: object

Cron schedule dictating when the task should run.
- No Additional Properties
##### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

##### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23"

##### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31"

##### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December)

##### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday)

#### pre_script

- Schema name: `Pre Script`
- Type: string
- Default: ""

A Bash script to run immediately before every backup.

#### post_script

- Schema name: `Post Script`
- Type: string
- Default: ""

A Bash script to run immediately after every backup if it succeeds.

#### snapshot

- Schema name: `Snapshot`
- Type: boolean
- Default: false

Whether to create a temporary snapshot of the dataset before every backup.

#### include

- Schema name: `Include`
- Type: array of string

Paths to pass to `restic backup --include`.
- No Additional Items

##### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

#### exclude

- Schema name: `Exclude`
- Type: array of string

Paths to pass to `restic backup --exclude`.
- No Additional Items

##### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

#### args

- Schema name: `Args`
- Type: string
- Default: ""

(Slated for removal).

#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Can enable/disable the task.

#### job (required)

- Schema name: `Job`

Information regarding the task's job state, e.g. progress.
##### Any of

###### Option 1

- Type: object

###### Option 2

- Type: null

#### locked (required)

- Schema name: `Locked`
- Type: boolean

A locked task cannot run.

#### password (required)

- Schema name: `Password`
- Type: string

Password for the remote repository.
- Must be at least `1` characters long

#### keep_last (required)

- Schema name: `Keep Last`
- Type: integer

How many of the most recent backup snapshots to keep after each backup.
- Value must be strictly greater than `0`

#### transfer_setting

- Schema name: `Transfer Setting`
- Type: enum (of string)
- Default: "DEFAULT"

DEFAULT: pack size given by `$RESTIC_PACK_SIZE` (default 16 MiB) read concurrency given by `$RESTIC_READ_CONCURRENCY` (default 2 files) PERFORMANCE: pack size = 29 MiB read concurrency given by `$RESTIC_READ_CONCURRENCY` (default 2 files) FAST_STORAGE: pack size = 58 MiB read concurrency = 100 files

#### absolute_paths

- Schema name: `Absolute Paths`
- Type: boolean
- Default: false

Preserve absolute paths in each backup (cannot be set when `snapshot=True`).

#### cache_path

- Schema name: `Cache Path`
- Default: null

Cache path. If not set, performance may degrade.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### rate_limit

- Schema name: `Rate Limit`
- Default: null

Maximum upload/download rate in KiB/s. Passed to `restic --limit-upload` on `cloud_backup.sync` and `restic --limit-download` on `cloud_backup.restore`. `null` indicates no rate limit will be imposed. Can be overridden on a sync or restore call.
##### Any of

###### Option 1

- Type: integer
- Value must be strictly greater than `0`

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
