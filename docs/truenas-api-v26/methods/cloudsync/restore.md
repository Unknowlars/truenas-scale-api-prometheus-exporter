---
title: cloudsync.restore
kind: method
source_rst: _sources/api_methods_cloudsync.restore.rst.txt
source_html: api_methods_cloudsync.restore.html
required_roles:
  - CLOUD_SYNC_WRITE
---

# cloudsync.restore

## Summary

Create the opposite of cloud sync task `id` (PULL if it was PUSH and vice versa).

## Required Roles

- `CLOUD_SYNC_WRITE`

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

ID of the cloud sync task to restore from.

#### Parameter 2: opts

#### opts

- Schema name: `opts`
- Type: object

Restore operation configuration options.
- No Additional Properties
##### description

- Schema name: `Description`
- Type: string
- Default: ""

Description for the restore operation.

##### transfer_mode (required)

- Schema name: `Transfer Mode`
- Type: enum (of string)

Transfer mode for the restore operation.

##### path (required)

- Schema name: `Path`
- Type: string

Local path where files will be restored.
- Must be at least `1` characters long

### Return value

- Schema name: `CloudSyncEntry`
- Type: object

The created restore task configuration.
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

#### dataset (required)

- Schema name: `Dataset`

The ZFS dataset containing this path (e.g., 'tank/backup'). This is a read-only field automatically resolved from "path". May be `null` if dataset is unavailable.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### relative_path (required)

- Schema name: `Relative Path`

The path relative to the dataset mountpoint (e.g., 'subdir/data'). This is a read-only field automatically resolved from "path". May be `null` if dataset is unavailable.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### credentials (required)

- Schema name: `CredentialsEntry`
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

- Type: object

Additional information for each backup, e.g. bucket name.

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

"00" - "23".

##### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

##### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

##### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

#### pre_script

- Schema name: `Pre Script`
- Type: string
- Default: ""

A Bash script to run immediately before every backup.
- Must be at most `2147483647` characters long

#### post_script

- Schema name: `Post Script`
- Type: string
- Default: ""

A Bash script to run immediately after every backup if it succeeds.
- Must be at most `2147483647` characters long

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
- Must be at most `2147483647` characters long

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
