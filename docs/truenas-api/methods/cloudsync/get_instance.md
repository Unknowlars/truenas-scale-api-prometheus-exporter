---
title: cloudsync.get_instance
kind: method
source_rst: _sources/api_methods_cloudsync.get_instance.rst.txt
source_html: api_methods_cloudsync.get_instance.html
required_roles:
  - CLOUD_SYNC_READ
---

# cloudsync.get_instance

## Summary

Returns instance matching `id`. If `id` is not found, Validation error is raised.

Please see `query` method documentation for `options`.

## Required Roles

- `CLOUD_SYNC_READ`

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

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object
- Default: {}

Query options customize the results returned by a query method. More complete documentation with examples are covered in the "Query methods" section of the TrueNAS API documentation.
- No Additional Properties
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: array
- No Additional Items

######### Each item of this array must be:

- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

### Return value

- Schema name: `CloudSyncEntry`
- Type: object
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

#### bwlimit

- Schema name: `Bwlimit`
- Type: array of object

Schedule of bandwidth limits.
- No Additional Items

##### Each item of this array must be:

##### CloudSyncBwlimit

- Schema name: `CloudSyncBwlimit`
- Type: object
- No Additional Properties
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

###### bandwidth (required)

- Schema name: `Bandwidth`

Bandwidth limit in bytes per second (upload and download).
####### Any of

######## Option 1

- Type: integer
- Value must be strictly greater than `0`

######## Option 2

- Type: null

#### transfers

- Schema name: `Transfers`
- Default: null

Maximum number of parallel file transfers. `null` for default.
##### Any of

###### Option 1

- Type: integer
- Value must be strictly greater than `0`

###### Option 2

- Type: null

#### direction (required)

- Schema name: `Direction`
- Type: enum (of string)

Direction of the cloud sync operation. `PUSH`: Upload local files to cloud storage `PULL`: Download files from cloud storage to local storage

#### transfer_mode (required)

- Schema name: `Transfer Mode`
- Type: enum (of string)

How files are transferred between local and cloud storage. `SYNC`: Synchronize directories (add new, update changed, remove deleted) `COPY`: Copy files without removing any existing files `MOVE`: Move files (copy then delete from source)

#### encryption

- Schema name: `Encryption`
- Type: boolean
- Default: false

Whether to encrypt files before uploading to cloud storage.

#### filename_encryption

- Schema name: `Filename Encryption`
- Type: boolean
- Default: false

Whether to encrypt filenames in addition to file contents.

#### encryption_password

- Schema name: `Encryption Password`
- Type: string
- Default: ""

Password for client-side encryption. Empty string if encryption is disabled.

#### encryption_salt

- Schema name: `Encryption Salt`
- Type: string
- Default: ""

Salt value for encryption key derivation. Empty string if encryption is disabled.

#### create_empty_src_dirs

- Schema name: `Create Empty Src Dirs`
- Type: boolean
- Default: false

Whether to create empty directories in the destination that exist in the source.

#### follow_symlinks

- Schema name: `Follow Symlinks`
- Type: boolean
- Default: false

Whether to follow symbolic links and sync the files they point to.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
