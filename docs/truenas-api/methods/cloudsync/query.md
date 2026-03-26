---
title: cloudsync.query
kind: method
source_rst: _sources/api_methods_cloudsync.query.rst.txt
source_html: api_methods_cloudsync.query.html
required_roles:
  - CLOUD_SYNC_READ
---

# cloudsync.query

## Required Roles

- `CLOUD_SYNC_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filters

#### filters

- Schema name: `filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

- Type: object

Examples:

```json
[
    [
        "name",
        "=",
        "bob"
    ]
]
```
Examples:

```json
[
    [
        "OR",
        [
            [
                [
                    "name",
                    "=",
                    "bob"
                ]
            ],
            [
                [
                    "name",
                    "=",
                    "larry"
                ]
            ]
        ]
    ]
]
```

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object
- Default:
```json
{
  "extra": {},
  "order_by": [],
  "select": [],
  "count": false,
  "get": false,
  "offset": 0,
  "limit": 0,
  "force_sql_filters": false
}
```

Query options including pagination, ordering, and additional parameters.
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

- Schema name: `Result`
#### Any of

##### Option 1

- Type: array of object
- No Additional Items

###### Each item of this array must be:

###### CloudSyncQueryResultItem

- Schema name: `CloudSyncQueryResultItem`
- Type: object
- No Additional Properties
####### id

- Schema name: `Id`
- Type: integer

Unique identifier for this cloud storage configuration.

####### description

- Schema name: `Description`
- Type: string

The name of the task to display in the UI.

####### path

- Schema name: `Path`
- Type: string

The local path to back up beginning with `/mnt` or `/dev/zvol`.

####### credentials

- Schema name: `CloudCredentialEntry`
- Type: object

Cloud credentials to use for each backup.
- No Additional Properties
######## id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the cloud credential.

######## name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the cloud credential.
- Must be at least `1` characters long

######## provider (required)

- Schema name: `Provider`

Cloud provider configuration including type and authentication details.

####### attributes

- Schema name: `CloudTaskAttributes`
- Type: object

Additional information for each backup, e.g. bucket name.
- No Additional Properties
######## bucket

- Schema name: `Bucket`
- Type: string

Name of the cloud storage bucket or container.
- Must be at least `1` characters long

######## folder

- Schema name: `Folder`
- Type: string

Path within the cloud storage bucket to use as the root directory for operations.

######## fast_list

- Schema name: `Fast List`
- Type: boolean

Valid only for some providers. Use fewer transactions in exchange for more RAM. This may also speed up or slow down your transfer. See https://rclone.org/docs/#fast-list for more details.

######## bucket_policy_only

- Schema name: `Bucket Policy Only`
- Type: boolean

Valid only for GOOGLE*CLOUD*STORAGE provider. Access checks should use bucket-level IAM policies. If you want to upload objects to a bucket with Bucket Policy Only set then you will need to set this.

######## chunk_size

- Schema name: `Chunk Size`
- Type: integer

Valid only for DROPBOX provider. Upload chunk size in MiB. Must fit in memory. Note that these chunks are buffered in memory and there might be a maximum of `--transfers` chunks in progress at once. Dropbox Business accounts can have monthly data transfer limits per team per month. By using larger chunk sizes you will decrease the number of data transfer calls used and you'll be able to transfer more data to your Dropbox Business account.

######## acknowledge_abuse

- Schema name: `Acknowledge Abuse`
- Type: boolean

Valid only for GOOGLE_DRIVER provider. Allow files which return cannotDownloadAbusiveFile to be downloaded. If downloading a file returns the error "This file has been identified as malware or spam and cannot be downloaded" with the error code "cannotDownloadAbusiveFile" then enable this flag to indicate you acknowledge the risks of downloading the file and TrueNAS will download it anyway.

######## region

- Schema name: `Region`
- Type: string

Valid only for S3 provider. S3 Region.

######## encryption

- Schema name: `Encryption`
- Type: enum (of null or string)

Valid only for S3 provider. Server-Side Encryption.

######## storage_class

- Schema name: `Storage Class`
- Type: enum (of string)

Valid only for S3 provider. The storage class to use.

####### schedule

- Schema name: `CloudCron`
- Type: object

Cron schedule dictating when the task should run.
- No Additional Properties
######## minute

- Schema name: `Minute`
- Type: string
- Default: "00"

######## hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23"

######## dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31"

######## month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December)

######## dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday)

####### pre_script

- Schema name: `Pre Script`
- Type: string

A Bash script to run immediately before every backup.

####### post_script

- Schema name: `Post Script`
- Type: string

A Bash script to run immediately after every backup if it succeeds.

####### snapshot

- Schema name: `Snapshot`
- Type: boolean

Whether to create a temporary snapshot of the dataset before every backup.

####### include

- Schema name: `Include`
- Type: array of string

Paths to pass to `restic backup --include`.
- No Additional Items

######## Each item of this array must be:

- Type: string
- Must be at least `1` characters long

####### exclude

- Schema name: `Exclude`
- Type: array of string

Paths to pass to `restic backup --exclude`.
- No Additional Items

######## Each item of this array must be:

- Type: string
- Must be at least `1` characters long

####### args

- Schema name: `Args`
- Type: string

(Slated for removal).

####### enabled

- Schema name: `Enabled`
- Type: boolean

Can enable/disable the task.

####### job

- Schema name: `Job`

Information regarding the task's job state, e.g. progress.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### locked

- Schema name: `Locked`
- Type: boolean

A locked task cannot run.

####### bwlimit

- Schema name: `Bwlimit`
- Type: array of object

Schedule of bandwidth limits.
- No Additional Items

######## Each item of this array must be:

######## CloudSyncBwlimit

- Schema name: `CloudSyncBwlimit`
- Type: object
- No Additional Properties
######### time (required)

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

######### bandwidth (required)

- Schema name: `Bandwidth`

Bandwidth limit in bytes per second (upload and download).
########## Any of

########### Option 1

- Type: integer
- Value must be strictly greater than `0`

########### Option 2

- Type: null

####### transfers

- Schema name: `Transfers`

Maximum number of parallel file transfers. `null` for default.
######## Any of

######### Option 1

- Type: integer
- Value must be strictly greater than `0`

######### Option 2

- Type: null

####### direction

- Schema name: `Direction`
- Type: enum (of string)

Direction of the cloud sync operation. `PUSH`: Upload local files to cloud storage `PULL`: Download files from cloud storage to local storage

####### transfer_mode

- Schema name: `Transfer Mode`
- Type: enum (of string)

How files are transferred between local and cloud storage. `SYNC`: Synchronize directories (add new, update changed, remove deleted) `COPY`: Copy files without removing any existing files `MOVE`: Move files (copy then delete from source)

####### encryption

- Schema name: `Encryption`
- Type: boolean

Whether to encrypt files before uploading to cloud storage.

####### filename_encryption

- Schema name: `Filename Encryption`
- Type: boolean

Whether to encrypt filenames in addition to file contents.

####### encryption_password

- Schema name: `Encryption Password`
- Type: string

Password for client-side encryption. Empty string if encryption is disabled.

####### encryption_salt

- Schema name: `Encryption Salt`
- Type: string

Salt value for encryption key derivation. Empty string if encryption is disabled.

####### create_empty_src_dirs

- Schema name: `Create Empty Src Dirs`
- Type: boolean

Whether to create empty directories in the destination that exist in the source.

####### follow_symlinks

- Schema name: `Follow Symlinks`
- Type: boolean

Whether to follow symbolic links and sync the files they point to.

##### CloudSyncQueryResultItem

- Schema name: `AzureBlobCredentialsModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Microsoft Azure Blob storage.

###### account (required)

- Schema name: `Account`
- Type: string

Azure Blob Storage account name for authentication.
- Must be at least `1` characters long

###### key (required)

- Schema name: `Key`
- Type: string

Azure Blob Storage access key for authentication.
- Must be at least `1` characters long

###### endpoint

- Schema name: `Endpoint`
- Default: ""

Custom Azure Blob Storage endpoint URL. Empty string for default endpoints.
####### Any of

######## Option 1

- Type: const

######## Option 2

- Type: string
- Type: Format: uri
- Must be at least `1` characters long
- Must be at most `2083` characters long

##### Option 3

- Type: const

##### AzureBlobCredentialsModel

- Type: string
- Type: Format: uri
- Must be at least `1` characters long
- Must be at most `2083` characters long

##### B2CredentialsModel

- Schema name: `B2CredentialsModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Backblaze B2 storage.

###### account (required)

- Schema name: `Account`
- Type: string

Backblaze B2 account ID for authentication.
- Must be at least `1` characters long

###### key (required)

- Schema name: `Key`
- Type: string

Backblaze B2 application key for authentication.
- Must be at least `1` characters long

##### BoxCredentialsModel

- Schema name: `BoxCredentialsModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Box cloud storage.

###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

Box OAuth application client ID.

###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

Box OAuth application client secret.

###### token (required)

- Schema name: `Token`
- Type: string

Box OAuth access token for API authentication.
- Must be at least `1` characters long

##### DropboxCredentialsModel

- Schema name: `DropboxCredentialsModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Dropbox storage.

###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

Dropbox OAuth application client ID.

###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

Dropbox OAuth application client secret.

###### token (required)

- Schema name: `Token`
- Type: string

Dropbox OAuth access token for API authentication.
- Must be at least `1` characters long

##### FTPCredentialsModel

- Schema name: `FTPCredentialsModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for FTP.

###### host (required)

- Schema name: `Host`
- Type: string

FTP server hostname or IP address.
- Must be at least `1` characters long

###### port

- Schema name: `Port`
- Type: integer
- Default: 21

FTP server port number.

###### user (required)

- Schema name: `User`
- Type: string

FTP username for authentication.
- Must be at least `1` characters long

###### pass (required)

- Schema name: `Pass`
- Type: string

FTP password for authentication.

##### GoogleCloudStorageCredentialsModel

- Schema name: `GoogleCloudStorageCredentialsModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Google Cloud Storage.

###### service_account_credentials (required)

- Schema name: `Service Account Credentials`
- Type: string

JSON service account credentials for Google Cloud Storage authentication.
- Must be at least `1` characters long

##### GoogleDriveCredentialsModel

- Schema name: `GoogleDriveCredentialsModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Google Drive.

###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

OAuth client ID for Google Drive API access.

###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

OAuth client secret for Google Drive API access.

###### token (required)

- Schema name: `Token`
- Type: string

OAuth access token for Google Drive authentication.
- Must be at least `1` characters long

###### team_drive

- Schema name: `Team Drive`
- Type: string
- Default: ""

Google Drive team drive ID or empty string for personal drive.

##### GooglePhotosCredentialsModel

- Schema name: `GooglePhotosCredentialsModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Google Photos.

###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

OAuth client ID for Google Photos API access.

###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

OAuth client secret for Google Photos API access.

###### token (required)

- Schema name: `Token`
- Type: string

OAuth access token for Google Photos authentication.
- Must be at least `1` characters long

##### HTTPCredentialsModel

- Schema name: `HTTPCredentialsModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for HTTP.

###### url (required)

- Schema name: `Url`
- Type: string
- Type: Format: uri

HTTP URL for file access.
- Must be at least `1` characters long
- Must be at most `2083` characters long

##### HubicCredentialsModel

- Schema name: `HubicCredentialsModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Hubic.

###### token (required)

- Schema name: `Token`
- Type: string

OAuth access token for Hubic authentication.
- Must be at least `1` characters long

##### MegaCredentialsModel

- Schema name: `MegaCredentialsModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for MEGA.

###### user (required)

- Schema name: `User`
- Type: string

MEGA username for authentication.
- Must be at least `1` characters long

###### pass (required)

- Schema name: `Pass`
- Type: string

MEGA password for authentication.
- Must be at least `1` characters long

##### OneDriveCredentialsModel

- Schema name: `OneDriveCredentialsModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for OneDrive.

###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

OAuth client ID for OneDrive API access.

###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

OAuth client secret for OneDrive API access.

###### token (required)

- Schema name: `Token`
- Type: string

OAuth access token for OneDrive authentication.
- Must be at least `1` characters long

###### drive_type (required)

- Schema name: `Drive Type`
- Type: enum (of string)

Type of OneDrive to access.

###### drive_id (required)

- Schema name: `Drive Id`
- Type: string

OneDrive drive identifier.

##### PCloudCredentialsModel

- Schema name: `PCloudCredentialsModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for pCloud.

###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

OAuth client ID for pCloud API access.

###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

OAuth client secret for pCloud API access.

###### token (required)

- Schema name: `Token`
- Type: string

OAuth access token for pCloud authentication.
- Must be at least `1` characters long

###### hostname

- Schema name: `Hostname`
- Type: string
- Default: ""

pCloud hostname or empty string for default.

##### S3CredentialsModel

- Schema name: `S3CredentialsModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for S3-compatible storage.

###### access_key_id (required)

- Schema name: `Access Key Id`
- Type: string

S3 access key ID for authentication.
- Must be at least `1` characters long

###### secret_access_key (required)

- Schema name: `Secret Access Key`
- Type: string

S3 secret access key for authentication.
- Must be at least `1` characters long

###### endpoint

- Schema name: `Endpoint`
- Default: ""

S3-compatible endpoint URL or empty string for AWS S3.
####### Any of

######## Option 1

- Type: const

######## Option 2

- Type: string
- Type: Format: uri
- Must be at least `1` characters long
- Must be at most `2083` characters long

###### region

- Schema name: `Region`
- Type: string
- Default: ""

S3 region or empty string for default.

###### skip_region

- Schema name: `Skip Region`
- Type: boolean
- Default: false

Whether to skip region validation.

###### signatures_v2

- Schema name: `Signatures V2`
- Type: boolean
- Default: false

Whether to use AWS Signature Version 2.

###### max_upload_parts

- Schema name: `Max Upload Parts`
- Type: integer
- Default: 10000

Maximum number of parts for multipart uploads.

##### SFTPCredentialsModel

- Type: const

##### StorjIxCredentialsModel

- Type: string
- Type: Format: uri
- Must be at least `1` characters long
- Must be at most `2083` characters long

##### SwiftCredentialsModel

- Schema name: `SFTPCredentialsModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for SFTP.

###### host (required)

- Schema name: `Host`
- Type: string

SFTP server hostname or IP address.
- Must be at least `1` characters long

###### port

- Schema name: `Port`
- Type: integer
- Default: 22

SFTP server port number.

###### user (required)

- Schema name: `User`
- Type: string

SFTP username for authentication.
- Must be at least `1` characters long

###### pass

- Schema name: `Pass`
- Default: null

SFTP password for authentication or `null` for key-based auth.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### private_key

- Schema name: `Private Key`
- Default: null

SSH private key ID for authentication or `null` for password auth.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

##### WebDavCredentialsModel

- Type: string

##### YandexCredentialsModel

- Type: null

##### Option 1

- Type: integer

##### Option 2

- Type: null

##### Option 1

- Schema name: `StorjIxCredentialsModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Storj decentralized storage.

###### access_key_id (required)

- Schema name: `Access Key Id`
- Type: string

Storj S3-compatible access key ID for authentication.
- Must be at least `1` characters long

###### secret_access_key (required)

- Schema name: `Secret Access Key`
- Type: string

Storj S3-compatible secret access key for authentication.
- Must be at least `1` characters long

###### endpoint

- Schema name: `Endpoint`
- Type: string
- Type: Format: uri
- Default: "https://gateway.storjshare.io/"

Storj gateway endpoint URL for S3-compatible access.
- Must be at least `1` characters long
- Must be at most `2083` characters long

##### Option 2

- Schema name: `SwiftCredentialsModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for OpenStack Swift storage.

###### user (required)

- Schema name: `User`
- Type: string

Swift username for authentication.
- Must be at least `1` characters long

###### key (required)

- Schema name: `Key`
- Type: string

Swift password or API key for authentication.
- Must be at least `1` characters long

###### auth (required)

- Schema name: `Auth`
- Type: string

Swift authentication URL endpoint.
- Must be at least `1` characters long

###### user_id

- Schema name: `User Id`
- Type: string
- Default: ""

Swift user ID for authentication.

###### domain

- Schema name: `Domain`
- Type: string
- Default: ""

Swift domain name for authentication.

###### tenant

- Schema name: `Tenant`
- Type: string
- Default: ""

Swift tenant name for multi-tenancy.

###### tenant_id

- Schema name: `Tenant Id`
- Type: string
- Default: ""

Swift tenant ID for multi-tenancy.

###### tenant_domain

- Schema name: `Tenant Domain`
- Type: string
- Default: ""

Swift tenant domain name.

###### region

- Schema name: `Region`
- Type: string
- Default: ""

Swift region name for geographic distribution.

###### storage_url

- Schema name: `Storage Url`
- Type: string
- Default: ""

Swift storage URL endpoint.

###### auth_token

- Schema name: `Auth Token`
- Type: string
- Default: ""

Swift authentication token for pre-authenticated access.

###### application_credential_id

- Schema name: `Application Credential Id`
- Type: string
- Default: ""

Swift application credential ID for authentication.

###### application_credential_name

- Schema name: `Application Credential Name`
- Type: string
- Default: ""

Swift application credential name for authentication.

###### application_credential_secret

- Schema name: `Application Credential Secret`
- Type: string
- Default: ""

Swift application credential secret for authentication.

###### auth_version (required)

- Schema name: `Auth Version`

Swift authentication API version. `0`: Legacy auth `1`: TempAuth `2`: Keystone v2.0 `3`: Keystone v3 `null`: Auto-detect
####### Any of

######## Option 1

- Type: enum (of integer)

######## Option 2

- Type: null

###### endpoint_type (required)

- Schema name: `Endpoint Type`

Swift endpoint type to use. `public`: Public endpoint (default) `internal`: Internal network endpoint `admin`: Administrative endpoint `null`: Use default
####### Any of

######## Option 1

- Type: enum (of string)

######## Option 2

- Type: null

##### Option 1

- Type: enum (of integer)

##### Option 2

- Type: null

##### Option 1

- Type: enum (of string)

##### Option 2

- Type: null

##### Option 1

- Schema name: `WebDavCredentialsModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for WebDAV servers.

###### url (required)

- Schema name: `Url`
- Type: string
- Type: Format: uri

WebDAV server URL endpoint.
- Must be at least `1` characters long
- Must be at most `2083` characters long

###### vendor (required)

- Schema name: `Vendor`
- Type: enum (of string)

WebDAV server vendor type for compatibility optimizations. `NEXTCLOUD`: Nextcloud server `OWNCLOUD`: ownCloud server `SHAREPOINT`: Microsoft SharePoint `OTHER`: Generic WebDAV server

###### user (required)

- Schema name: `User`
- Type: string

WebDAV username for authentication.

###### pass (required)

- Schema name: `Pass`
- Type: string

WebDAV password for authentication.

##### Option 2

- Schema name: `YandexCredentialsModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Yandex Disk storage.

###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

Yandex OAuth application client ID.

###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

Yandex OAuth application client secret.

###### token (required)

- Schema name: `Token`
- Type: string

Yandex OAuth access token for API authentication.
- Must be at least `1` characters long

##### Option 1

- Type: object

##### Option 2

- Type: null

##### Option 1

- Type: integer
- Value must be strictly greater than `0`

##### Option 2

- Type: null

##### Option 1

- Type: integer
- Value must be strictly greater than `0`

##### Option 2

- Type: null

##### Option 1

- Schema name: `CloudSyncQueryResultItem`
- Type: object
- No Additional Properties
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for this cloud storage configuration.

###### description

- Schema name: `Description`
- Type: string

The name of the task to display in the UI.

###### path

- Schema name: `Path`
- Type: string

The local path to back up beginning with `/mnt` or `/dev/zvol`.

###### credentials

- Type: object

Cloud credentials to use for each backup.

###### attributes

- Type: object

Additional information for each backup, e.g. bucket name.

###### schedule

- Type: object

Cron schedule dictating when the task should run.

###### pre_script

- Schema name: `Pre Script`
- Type: string

A Bash script to run immediately before every backup.

###### post_script

- Schema name: `Post Script`
- Type: string

A Bash script to run immediately after every backup if it succeeds.

###### snapshot

- Schema name: `Snapshot`
- Type: boolean

Whether to create a temporary snapshot of the dataset before every backup.

###### include

- Schema name: `Include`
- Type: array of string

Paths to pass to `restic backup --include`.
- No Additional Items

####### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

###### exclude

- Schema name: `Exclude`
- Type: array of string

Paths to pass to `restic backup --exclude`.
- No Additional Items

####### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

###### args

- Schema name: `Args`
- Type: string

(Slated for removal).

###### enabled

- Schema name: `Enabled`
- Type: boolean

Can enable/disable the task.

###### job

- Schema name: `Job`

Information regarding the task's job state, e.g. progress.
####### Any of

######## Option 1

- Type: object

######## Option 2

- Type: null

###### locked

- Schema name: `Locked`
- Type: boolean

A locked task cannot run.

###### bwlimit

- Schema name: `Bwlimit`
- Type: array

Schedule of bandwidth limits.
- No Additional Items

####### Each item of this array must be:

- Type: object

###### transfers

- Schema name: `Transfers`

Maximum number of parallel file transfers. `null` for default.
####### Any of

######## Option 1

- Type: integer
- Value must be strictly greater than `0`

######## Option 2

- Type: null

###### direction

- Schema name: `Direction`
- Type: enum (of string)

Direction of the cloud sync operation. `PUSH`: Upload local files to cloud storage `PULL`: Download files from cloud storage to local storage

###### transfer_mode

- Schema name: `Transfer Mode`
- Type: enum (of string)

How files are transferred between local and cloud storage. `SYNC`: Synchronize directories (add new, update changed, remove deleted) `COPY`: Copy files without removing any existing files `MOVE`: Move files (copy then delete from source)

###### encryption

- Schema name: `Encryption`
- Type: boolean

Whether to encrypt files before uploading to cloud storage.

###### filename_encryption

- Schema name: `Filename Encryption`
- Type: boolean

Whether to encrypt filenames in addition to file contents.

###### encryption_password

- Schema name: `Encryption Password`
- Type: string

Password for client-side encryption. Empty string if encryption is disabled.

###### encryption_salt

- Schema name: `Encryption Salt`
- Type: string

Salt value for encryption key derivation. Empty string if encryption is disabled.

###### create_empty_src_dirs

- Schema name: `Create Empty Src Dirs`
- Type: boolean

Whether to create empty directories in the destination that exist in the source.

###### follow_symlinks

- Schema name: `Follow Symlinks`
- Type: boolean

Whether to follow symbolic links and sync the files they point to.

##### Option 2

- Type: object

##### Option 1

- Type: null

##### Option 2

- Type: integer
- Value must be strictly greater than `0`

##### Option 1

- Type: null

##### Option 2

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
