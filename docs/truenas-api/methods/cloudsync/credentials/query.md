---
title: cloudsync.credentials.query
kind: method
source_rst: _sources/api_methods_cloudsync.credentials.query.rst.txt
source_html: api_methods_cloudsync.credentials.query.html
required_roles:
  - CLOUD_SYNC_READ
---

# cloudsync.credentials.query

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

###### CloudCredentialQueryResultItem

- Schema name: `CloudCredentialQueryResultItem`
- Type: object
- No Additional Properties
####### id

- Schema name: `Id`
- Type: integer

Unique identifier for the cloud credential.

####### name

- Schema name: `Name`
- Type: string

Human-readable name for the cloud credential.
- Must be at least `1` characters long

####### provider

- Schema name: `Provider`

Cloud provider configuration including type and authentication details.

##### CloudCredentialQueryResultItem

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

- Schema name: `CloudCredentialQueryResultItem`
- Type: object
- No Additional Properties
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the cloud credential.

###### name

- Schema name: `Name`
- Type: string

Human-readable name for the cloud credential.
- Must be at least `1` characters long

###### provider

- Schema name: `Provider`

Cloud provider configuration including type and authentication details.

##### Option 2

- Type: object

##### Option 1

- Type: object

##### Option 2

- Type: object

##### Option 3

- Type: object

##### Option 4

- Type: object

##### Option 5

- Type: object

##### Option 6

- Type: object

##### Option 7

- Type: object

##### Option 8

- Type: object

##### Option 9

- Type: object

##### Option 10

- Type: object

##### Option 11

- Type: object

##### Option 12

- Type: object

##### Option 13

- Type: object

##### Option 14

- Type: object

##### Option 15

- Type: object

##### Option 16

- Type: object

##### Option 17

- Type: object

##### Option 18

- Type: object

##### Option 19

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
