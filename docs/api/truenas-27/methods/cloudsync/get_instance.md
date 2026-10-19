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
- Type: integer

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object
- Default: {}

Query options customize the results returned by a query method. More complete documentation with examples are covered in the "Query methods" section of the TrueNAS API documentation.
- No Additional Properties
<a id="headingCall_parameters_items_i1_extra"></a>
<a id="Call_parameters_items_i1_extra"></a>
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

<a id="headingCall_parameters_items_i1_order_by"></a>
<a id="Call_parameters_items_i1_order_by"></a>
##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_order_by_items"></a>
- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

<a id="headingCall_parameters_items_i1_select"></a>
<a id="Call_parameters_items_i1_select"></a>
##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items"></a>
<a id="Call_parameters_items_i1_select_items_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i1)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items_anyOf_i1_items"></a>
- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

<a id="headingCall_parameters_items_i1_count"></a>
<a id="Call_parameters_items_i1_count"></a>
##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

<a id="headingCall_parameters_items_i1_get"></a>
<a id="Call_parameters_items_i1_get"></a>
##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

<a id="headingCall_parameters_items_i1_offset"></a>
<a id="Call_parameters_items_i1_offset"></a>
##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

<a id="headingCall_parameters_items_i1_force_sql_filters"></a>
<a id="Call_parameters_items_i1_force_sql_filters"></a>
##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `CloudSyncEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this cloud storage configuration.

<a id="headingReturn_value_description"></a>
<a id="Return_value_description"></a>
#### description

- Schema name: `Description`
- Type: string
- Default: ""

The name of the task to display in the UI.

<a id="headingReturn_value_path"></a>
<a id="Return_value_path"></a>
#### path (required)

- Schema name: `Path`
- Type: string

The local path to back up beginning with `/mnt` or `/dev/zvol`.

<a id="headingReturn_value_dataset"></a>
<a id="Return_value_dataset"></a>
#### dataset (required)

- Schema name: `Dataset`

The ZFS dataset containing this path (e.g., 'tank/backup'). This is a read-only field automatically resolved from "path". May be `null` if dataset is unavailable.
<a id="Return_value_dataset_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_dataset_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_dataset_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_dataset_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_dataset_anyOf_i1)

- Type: null

<a id="headingReturn_value_relative_path"></a>
<a id="Return_value_relative_path"></a>
#### relative_path (required)

- Schema name: `Relative Path`

The path relative to the dataset mountpoint (e.g., 'subdir/data'). This is a read-only field automatically resolved from "path". May be `null` if dataset is unavailable.
<a id="Return_value_relative_path_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_relative_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_relative_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_relative_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_relative_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_credentials"></a>
<a id="Return_value_credentials"></a>
#### credentials (required)

- Schema name: `CredentialsEntry`
- Type: object

Cloud credentials to use for each backup.
- No Additional Properties
<a id="headingReturn_value_credentials_id"></a>
<a id="Return_value_credentials_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the cloud credential.

<a id="headingReturn_value_credentials_name"></a>
<a id="Return_value_credentials_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the cloud credential.
- Must be at least `1` characters long

<a id="headingReturn_value_credentials_provider"></a>
<a id="Return_value_credentials_provider"></a>
##### provider (required)

- Schema name: `Provider`

Cloud provider configuration including type and authentication details.
<a id="Return_value_credentials_provider_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_credentials_provider_oneOf_i0"></a>
###### [AzureBlobCredentialsModel](#tab-pane_Return_value_credentials_provider_oneOf_i0)

- Schema name: `AzureBlobCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credentials_provider_oneOf_i0_type"></a>
<a id="Return_value_credentials_provider_oneOf_i0_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Microsoft Azure Blob storage.
- Specific value: `"AZUREBLOB"`

<a id="headingReturn_value_credentials_provider_oneOf_i0_account"></a>
<a id="Return_value_credentials_provider_oneOf_i0_account"></a>
###### account (required)

- Schema name: `Account`
- Type: string

Azure Blob Storage account name for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_credentials_provider_oneOf_i0_key"></a>
<a id="Return_value_credentials_provider_oneOf_i0_key"></a>
###### key (required)

- Schema name: `Key`
- Type: string

Azure Blob Storage access key for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_credentials_provider_oneOf_i0_endpoint"></a>
<a id="Return_value_credentials_provider_oneOf_i0_endpoint"></a>
###### endpoint

- Schema name: `Endpoint`
- Default: ""

Custom Azure Blob Storage endpoint URL. Empty string for default endpoints.
<a id="Return_value_credentials_provider_oneOf_i0_endpoint_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_credentials_provider_oneOf_i0_endpoint_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_credentials_provider_oneOf_i0_endpoint_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_credentials_provider_oneOf_i0_endpoint_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_credentials_provider_oneOf_i0_endpoint_anyOf_i1)

- Type: string
- Type: Format: uri
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="tab-pane_Return_value_credentials_provider_oneOf_i1"></a>
###### [B2CredentialsModel](#tab-pane_Return_value_credentials_provider_oneOf_i1)

- Schema name: `B2CredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credentials_provider_oneOf_i1_type"></a>
<a id="Return_value_credentials_provider_oneOf_i1_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Backblaze B2 storage.
- Specific value: `"B2"`

<a id="headingReturn_value_credentials_provider_oneOf_i1_account"></a>
<a id="Return_value_credentials_provider_oneOf_i1_account"></a>
###### account (required)

- Schema name: `Account`
- Type: string

Backblaze B2 account ID for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_credentials_provider_oneOf_i1_key"></a>
<a id="Return_value_credentials_provider_oneOf_i1_key"></a>
###### key (required)

- Schema name: `Key`
- Type: string

Backblaze B2 application key for authentication.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_credentials_provider_oneOf_i2"></a>
###### [BoxCredentialsModel](#tab-pane_Return_value_credentials_provider_oneOf_i2)

- Schema name: `BoxCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credentials_provider_oneOf_i2_type"></a>
<a id="Return_value_credentials_provider_oneOf_i2_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Box cloud storage.
- Specific value: `"BOX"`

<a id="headingReturn_value_credentials_provider_oneOf_i2_client_id"></a>
<a id="Return_value_credentials_provider_oneOf_i2_client_id"></a>
###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

Box OAuth application client ID.

<a id="headingReturn_value_credentials_provider_oneOf_i2_client_secret"></a>
<a id="Return_value_credentials_provider_oneOf_i2_client_secret"></a>
###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

Box OAuth application client secret.

<a id="headingReturn_value_credentials_provider_oneOf_i2_token"></a>
<a id="Return_value_credentials_provider_oneOf_i2_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

Box OAuth access token for API authentication.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_credentials_provider_oneOf_i3"></a>
###### [DropboxCredentialsModel](#tab-pane_Return_value_credentials_provider_oneOf_i3)

- Schema name: `DropboxCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credentials_provider_oneOf_i3_type"></a>
<a id="Return_value_credentials_provider_oneOf_i3_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Dropbox storage.
- Specific value: `"DROPBOX"`

<a id="headingReturn_value_credentials_provider_oneOf_i3_client_id"></a>
<a id="Return_value_credentials_provider_oneOf_i3_client_id"></a>
###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

Dropbox OAuth application client ID.

<a id="headingReturn_value_credentials_provider_oneOf_i3_client_secret"></a>
<a id="Return_value_credentials_provider_oneOf_i3_client_secret"></a>
###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

Dropbox OAuth application client secret.

<a id="headingReturn_value_credentials_provider_oneOf_i3_token"></a>
<a id="Return_value_credentials_provider_oneOf_i3_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

Dropbox OAuth access token for API authentication.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_credentials_provider_oneOf_i4"></a>
###### [FTPCredentialsModel](#tab-pane_Return_value_credentials_provider_oneOf_i4)

- Schema name: `FTPCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credentials_provider_oneOf_i4_type"></a>
<a id="Return_value_credentials_provider_oneOf_i4_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for FTP.
- Specific value: `"FTP"`

<a id="headingReturn_value_credentials_provider_oneOf_i4_host"></a>
<a id="Return_value_credentials_provider_oneOf_i4_host"></a>
###### host (required)

- Schema name: `Host`
- Type: string

FTP server hostname or IP address.
- Must be at least `1` characters long

<a id="headingReturn_value_credentials_provider_oneOf_i4_port"></a>
<a id="Return_value_credentials_provider_oneOf_i4_port"></a>
###### port

- Schema name: `Port`
- Type: integer
- Default: 21

FTP server port number.

<a id="headingReturn_value_credentials_provider_oneOf_i4_user"></a>
<a id="Return_value_credentials_provider_oneOf_i4_user"></a>
###### user (required)

- Schema name: `User`
- Type: string

FTP username for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_credentials_provider_oneOf_i4_pass"></a>
<a id="Return_value_credentials_provider_oneOf_i4_pass"></a>
###### pass (required)

- Schema name: `Pass`
- Type: string

FTP password for authentication.

<a id="tab-pane_Return_value_credentials_provider_oneOf_i5"></a>
###### [GoogleCloudStorageCredentialsModel](#tab-pane_Return_value_credentials_provider_oneOf_i5)

- Schema name: `GoogleCloudStorageCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credentials_provider_oneOf_i5_type"></a>
<a id="Return_value_credentials_provider_oneOf_i5_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Google Cloud Storage.
- Specific value: `"GOOGLE_CLOUD_STORAGE"`

<a id="headingReturn_value_credentials_provider_oneOf_i5_service_account_credentials"></a>
<a id="Return_value_credentials_provider_oneOf_i5_service_account_credentials"></a>
###### service_account_credentials (required)

- Schema name: `Service Account Credentials`
- Type: string

JSON service account credentials for Google Cloud Storage authentication.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_credentials_provider_oneOf_i6"></a>
###### [GoogleDriveCredentialsModel](#tab-pane_Return_value_credentials_provider_oneOf_i6)

- Schema name: `GoogleDriveCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credentials_provider_oneOf_i6_type"></a>
<a id="Return_value_credentials_provider_oneOf_i6_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Google Drive.
- Specific value: `"GOOGLE_DRIVE"`

<a id="headingReturn_value_credentials_provider_oneOf_i6_client_id"></a>
<a id="Return_value_credentials_provider_oneOf_i6_client_id"></a>
###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

OAuth client ID for Google Drive API access.

<a id="headingReturn_value_credentials_provider_oneOf_i6_client_secret"></a>
<a id="Return_value_credentials_provider_oneOf_i6_client_secret"></a>
###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

OAuth client secret for Google Drive API access.

<a id="headingReturn_value_credentials_provider_oneOf_i6_token"></a>
<a id="Return_value_credentials_provider_oneOf_i6_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

OAuth access token for Google Drive authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_credentials_provider_oneOf_i6_team_drive"></a>
<a id="Return_value_credentials_provider_oneOf_i6_team_drive"></a>
###### team_drive

- Schema name: `Team Drive`
- Type: string
- Default: ""

Google Drive team drive ID or empty string for personal drive.

<a id="tab-pane_Return_value_credentials_provider_oneOf_i7"></a>
###### [GooglePhotosCredentialsModel](#tab-pane_Return_value_credentials_provider_oneOf_i7)

- Schema name: `GooglePhotosCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credentials_provider_oneOf_i7_type"></a>
<a id="Return_value_credentials_provider_oneOf_i7_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Google Photos.
- Specific value: `"GOOGLE_PHOTOS"`

<a id="headingReturn_value_credentials_provider_oneOf_i7_client_id"></a>
<a id="Return_value_credentials_provider_oneOf_i7_client_id"></a>
###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

OAuth client ID for Google Photos API access.

<a id="headingReturn_value_credentials_provider_oneOf_i7_client_secret"></a>
<a id="Return_value_credentials_provider_oneOf_i7_client_secret"></a>
###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

OAuth client secret for Google Photos API access.

<a id="headingReturn_value_credentials_provider_oneOf_i7_token"></a>
<a id="Return_value_credentials_provider_oneOf_i7_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

OAuth access token for Google Photos authentication.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_credentials_provider_oneOf_i8"></a>
###### [HTTPCredentialsModel](#tab-pane_Return_value_credentials_provider_oneOf_i8)

- Schema name: `HTTPCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credentials_provider_oneOf_i8_type"></a>
<a id="Return_value_credentials_provider_oneOf_i8_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for HTTP.
- Specific value: `"HTTP"`

<a id="headingReturn_value_credentials_provider_oneOf_i8_url"></a>
<a id="Return_value_credentials_provider_oneOf_i8_url"></a>
###### url (required)

- Schema name: `Url`
- Type: string
- Type: Format: uri

HTTP URL for file access.
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="tab-pane_Return_value_credentials_provider_oneOf_i9"></a>
###### [HubicCredentialsModel](#tab-pane_Return_value_credentials_provider_oneOf_i9)

- Schema name: `HubicCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credentials_provider_oneOf_i9_type"></a>
<a id="Return_value_credentials_provider_oneOf_i9_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Hubic.
- Specific value: `"HUBIC"`

<a id="headingReturn_value_credentials_provider_oneOf_i9_token"></a>
<a id="Return_value_credentials_provider_oneOf_i9_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

OAuth access token for Hubic authentication.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_credentials_provider_oneOf_i10"></a>
###### [MegaCredentialsModel](#tab-pane_Return_value_credentials_provider_oneOf_i10)

- Schema name: `MegaCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credentials_provider_oneOf_i10_type"></a>
<a id="Return_value_credentials_provider_oneOf_i10_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for MEGA.
- Specific value: `"MEGA"`

<a id="headingReturn_value_credentials_provider_oneOf_i10_user"></a>
<a id="Return_value_credentials_provider_oneOf_i10_user"></a>
###### user (required)

- Schema name: `User`
- Type: string

MEGA username for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_credentials_provider_oneOf_i10_pass"></a>
<a id="Return_value_credentials_provider_oneOf_i10_pass"></a>
###### pass (required)

- Schema name: `Pass`
- Type: string

MEGA password for authentication.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_credentials_provider_oneOf_i11"></a>
###### [OneDriveCredentialsModel](#tab-pane_Return_value_credentials_provider_oneOf_i11)

- Schema name: `OneDriveCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credentials_provider_oneOf_i11_type"></a>
<a id="Return_value_credentials_provider_oneOf_i11_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for OneDrive.
- Specific value: `"ONEDRIVE"`

<a id="headingReturn_value_credentials_provider_oneOf_i11_client_id"></a>
<a id="Return_value_credentials_provider_oneOf_i11_client_id"></a>
###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

OAuth client ID for OneDrive API access.

<a id="headingReturn_value_credentials_provider_oneOf_i11_client_secret"></a>
<a id="Return_value_credentials_provider_oneOf_i11_client_secret"></a>
###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

OAuth client secret for OneDrive API access.

<a id="headingReturn_value_credentials_provider_oneOf_i11_token"></a>
<a id="Return_value_credentials_provider_oneOf_i11_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

OAuth access token for OneDrive authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_credentials_provider_oneOf_i11_drive_type"></a>
<a id="Return_value_credentials_provider_oneOf_i11_drive_type"></a>
###### drive_type (required)

- Schema name: `Drive Type`
- Type: enum (of string)

Type of OneDrive to access.
###### Must be one of:

- "PERSONAL"
- "BUSINESS"
- "DOCUMENT_LIBRARY"

<a id="headingReturn_value_credentials_provider_oneOf_i11_drive_id"></a>
<a id="Return_value_credentials_provider_oneOf_i11_drive_id"></a>
###### drive_id (required)

- Schema name: `Drive Id`
- Type: string

OneDrive drive identifier.

<a id="tab-pane_Return_value_credentials_provider_oneOf_i12"></a>
###### [PCloudCredentialsModel](#tab-pane_Return_value_credentials_provider_oneOf_i12)

- Schema name: `PCloudCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credentials_provider_oneOf_i12_type"></a>
<a id="Return_value_credentials_provider_oneOf_i12_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for pCloud.
- Specific value: `"PCLOUD"`

<a id="headingReturn_value_credentials_provider_oneOf_i12_client_id"></a>
<a id="Return_value_credentials_provider_oneOf_i12_client_id"></a>
###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

OAuth client ID for pCloud API access.

<a id="headingReturn_value_credentials_provider_oneOf_i12_client_secret"></a>
<a id="Return_value_credentials_provider_oneOf_i12_client_secret"></a>
###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

OAuth client secret for pCloud API access.

<a id="headingReturn_value_credentials_provider_oneOf_i12_token"></a>
<a id="Return_value_credentials_provider_oneOf_i12_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

OAuth access token for pCloud authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_credentials_provider_oneOf_i12_hostname"></a>
<a id="Return_value_credentials_provider_oneOf_i12_hostname"></a>
###### hostname

- Schema name: `Hostname`
- Type: string
- Default: ""

pCloud hostname or empty string for default.

<a id="tab-pane_Return_value_credentials_provider_oneOf_i13"></a>
###### [S3CredentialsModel](#tab-pane_Return_value_credentials_provider_oneOf_i13)

- Schema name: `S3CredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credentials_provider_oneOf_i13_type"></a>
<a id="Return_value_credentials_provider_oneOf_i13_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for S3-compatible storage.
- Specific value: `"S3"`

<a id="headingReturn_value_credentials_provider_oneOf_i13_access_key_id"></a>
<a id="Return_value_credentials_provider_oneOf_i13_access_key_id"></a>
###### access_key_id (required)

- Schema name: `Access Key Id`
- Type: string

S3 access key ID for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_credentials_provider_oneOf_i13_secret_access_key"></a>
<a id="Return_value_credentials_provider_oneOf_i13_secret_access_key"></a>
###### secret_access_key (required)

- Schema name: `Secret Access Key`
- Type: string

S3 secret access key for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_credentials_provider_oneOf_i13_endpoint"></a>
<a id="Return_value_credentials_provider_oneOf_i13_endpoint"></a>
###### endpoint

- Schema name: `Endpoint`
- Default: ""

S3-compatible endpoint URL or empty string for AWS S3.
<a id="Return_value_credentials_provider_oneOf_i13_endpoint_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_credentials_provider_oneOf_i13_endpoint_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_credentials_provider_oneOf_i13_endpoint_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_credentials_provider_oneOf_i13_endpoint_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_credentials_provider_oneOf_i13_endpoint_anyOf_i1)

- Type: string
- Type: Format: uri
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="headingReturn_value_credentials_provider_oneOf_i13_region"></a>
<a id="Return_value_credentials_provider_oneOf_i13_region"></a>
###### region

- Schema name: `Region`
- Type: string
- Default: ""

S3 region or empty string for default.

<a id="headingReturn_value_credentials_provider_oneOf_i13_skip_region"></a>
<a id="Return_value_credentials_provider_oneOf_i13_skip_region"></a>
###### skip_region

- Schema name: `Skip Region`
- Type: boolean
- Default: false

Whether to skip region validation.

<a id="headingReturn_value_credentials_provider_oneOf_i13_signatures_v2"></a>
<a id="Return_value_credentials_provider_oneOf_i13_signatures_v2"></a>
###### signatures_v2

- Schema name: `Signatures V2`
- Type: boolean
- Default: false

Whether to use AWS Signature Version 2.

<a id="headingReturn_value_credentials_provider_oneOf_i13_max_upload_parts"></a>
<a id="Return_value_credentials_provider_oneOf_i13_max_upload_parts"></a>
###### max_upload_parts

- Schema name: `Max Upload Parts`
- Type: integer
- Default: 10000

Maximum number of parts for multipart uploads.

<a id="headingReturn_value_credentials_provider_oneOf_i13_provider"></a>
<a id="Return_value_credentials_provider_oneOf_i13_provider"></a>
###### provider

- Schema name: `Provider`
- Type: string
- Default: "Other"

S3 provider. See `cloudsync.credentials.s3_provider_choices` for possible values.

<a id="headingReturn_value_credentials_provider_oneOf_i13_force_path_style"></a>
<a id="Return_value_credentials_provider_oneOf_i13_force_path_style"></a>
###### force_path_style

- Schema name: `Force Path Style`
- Type: boolean
- Default: true

If true use path style access if false use virtual hosted style.

<a id="headingReturn_value_credentials_provider_oneOf_i13_sign_accept_encoding"></a>
<a id="Return_value_credentials_provider_oneOf_i13_sign_accept_encoding"></a>
###### sign_accept_encoding

- Schema name: `Sign Accept Encoding`
- Type: boolean
- Default: true

Set this to `false` if your S3 server is behind a proxy that modified HTTP headers and you are experiencing `SignatureDoesNotMatch` error.

<a id="tab-pane_Return_value_credentials_provider_oneOf_i14"></a>
###### [SFTPCredentialsModel](#tab-pane_Return_value_credentials_provider_oneOf_i14)

- Schema name: `SFTPCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credentials_provider_oneOf_i14_type"></a>
<a id="Return_value_credentials_provider_oneOf_i14_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for SFTP.
- Specific value: `"SFTP"`

<a id="headingReturn_value_credentials_provider_oneOf_i14_host"></a>
<a id="Return_value_credentials_provider_oneOf_i14_host"></a>
###### host (required)

- Schema name: `Host`
- Type: string

SFTP server hostname or IP address.
- Must be at least `1` characters long

<a id="headingReturn_value_credentials_provider_oneOf_i14_port"></a>
<a id="Return_value_credentials_provider_oneOf_i14_port"></a>
###### port

- Schema name: `Port`
- Type: integer
- Default: 22

SFTP server port number.

<a id="headingReturn_value_credentials_provider_oneOf_i14_user"></a>
<a id="Return_value_credentials_provider_oneOf_i14_user"></a>
###### user (required)

- Schema name: `User`
- Type: string

SFTP username for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_credentials_provider_oneOf_i14_pass"></a>
<a id="Return_value_credentials_provider_oneOf_i14_pass"></a>
###### pass

- Schema name: `Pass`
- Default: null

SFTP password for authentication or `null` for key-based auth.
<a id="Return_value_credentials_provider_oneOf_i14_pass_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_credentials_provider_oneOf_i14_pass_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_credentials_provider_oneOf_i14_pass_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_credentials_provider_oneOf_i14_pass_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_credentials_provider_oneOf_i14_pass_anyOf_i1)

- Type: null

<a id="headingReturn_value_credentials_provider_oneOf_i14_private_key"></a>
<a id="Return_value_credentials_provider_oneOf_i14_private_key"></a>
###### private_key

- Schema name: `Private Key`
- Default: null

SSH private key ID for authentication or `null` for password auth.
<a id="Return_value_credentials_provider_oneOf_i14_private_key_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_credentials_provider_oneOf_i14_private_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_credentials_provider_oneOf_i14_private_key_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_credentials_provider_oneOf_i14_private_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_credentials_provider_oneOf_i14_private_key_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_credentials_provider_oneOf_i15"></a>
###### [StorjIxCredentialsModel](#tab-pane_Return_value_credentials_provider_oneOf_i15)

- Schema name: `StorjIxCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credentials_provider_oneOf_i15_type"></a>
<a id="Return_value_credentials_provider_oneOf_i15_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Storj decentralized storage.
- Specific value: `"STORJ_IX"`

<a id="headingReturn_value_credentials_provider_oneOf_i15_access_key_id"></a>
<a id="Return_value_credentials_provider_oneOf_i15_access_key_id"></a>
###### access_key_id (required)

- Schema name: `Access Key Id`
- Type: string

Storj S3-compatible access key ID for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_credentials_provider_oneOf_i15_secret_access_key"></a>
<a id="Return_value_credentials_provider_oneOf_i15_secret_access_key"></a>
###### secret_access_key (required)

- Schema name: `Secret Access Key`
- Type: string

Storj S3-compatible secret access key for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_credentials_provider_oneOf_i15_endpoint"></a>
<a id="Return_value_credentials_provider_oneOf_i15_endpoint"></a>
###### endpoint

- Schema name: `Endpoint`
- Type: string
- Type: Format: uri
- Default: "https://gateway.storjshare.io/"

Storj gateway endpoint URL for S3-compatible access.
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="tab-pane_Return_value_credentials_provider_oneOf_i16"></a>
###### [SwiftCredentialsModel](#tab-pane_Return_value_credentials_provider_oneOf_i16)

- Schema name: `SwiftCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credentials_provider_oneOf_i16_type"></a>
<a id="Return_value_credentials_provider_oneOf_i16_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for OpenStack Swift storage.
- Specific value: `"OPENSTACK_SWIFT"`

<a id="headingReturn_value_credentials_provider_oneOf_i16_user"></a>
<a id="Return_value_credentials_provider_oneOf_i16_user"></a>
###### user (required)

- Schema name: `User`
- Type: string

Swift username for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_credentials_provider_oneOf_i16_key"></a>
<a id="Return_value_credentials_provider_oneOf_i16_key"></a>
###### key (required)

- Schema name: `Key`
- Type: string

Swift password or API key for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_credentials_provider_oneOf_i16_auth"></a>
<a id="Return_value_credentials_provider_oneOf_i16_auth"></a>
###### auth (required)

- Schema name: `Auth`
- Type: string

Swift authentication URL endpoint.
- Must be at least `1` characters long

<a id="headingReturn_value_credentials_provider_oneOf_i16_user_id"></a>
<a id="Return_value_credentials_provider_oneOf_i16_user_id"></a>
###### user_id

- Schema name: `User Id`
- Type: string
- Default: ""

Swift user ID for authentication.

<a id="headingReturn_value_credentials_provider_oneOf_i16_domain"></a>
<a id="Return_value_credentials_provider_oneOf_i16_domain"></a>
###### domain

- Schema name: `Domain`
- Type: string
- Default: ""

Swift domain name for authentication.

<a id="headingReturn_value_credentials_provider_oneOf_i16_tenant"></a>
<a id="Return_value_credentials_provider_oneOf_i16_tenant"></a>
###### tenant

- Schema name: `Tenant`
- Type: string
- Default: ""

Swift tenant name for multi-tenancy.

<a id="headingReturn_value_credentials_provider_oneOf_i16_tenant_id"></a>
<a id="Return_value_credentials_provider_oneOf_i16_tenant_id"></a>
###### tenant_id

- Schema name: `Tenant Id`
- Type: string
- Default: ""

Swift tenant ID for multi-tenancy.

<a id="headingReturn_value_credentials_provider_oneOf_i16_tenant_domain"></a>
<a id="Return_value_credentials_provider_oneOf_i16_tenant_domain"></a>
###### tenant_domain

- Schema name: `Tenant Domain`
- Type: string
- Default: ""

Swift tenant domain name.

<a id="headingReturn_value_credentials_provider_oneOf_i16_region"></a>
<a id="Return_value_credentials_provider_oneOf_i16_region"></a>
###### region

- Schema name: `Region`
- Type: string
- Default: ""

Swift region name for geographic distribution.

<a id="headingReturn_value_credentials_provider_oneOf_i16_storage_url"></a>
<a id="Return_value_credentials_provider_oneOf_i16_storage_url"></a>
###### storage_url

- Schema name: `Storage Url`
- Type: string
- Default: ""

Swift storage URL endpoint.

<a id="headingReturn_value_credentials_provider_oneOf_i16_auth_token"></a>
<a id="Return_value_credentials_provider_oneOf_i16_auth_token"></a>
###### auth_token

- Schema name: `Auth Token`
- Type: string
- Default: ""

Swift authentication token for pre-authenticated access.

<a id="headingReturn_value_credentials_provider_oneOf_i16_application_credential_id"></a>
<a id="Return_value_credentials_provider_oneOf_i16_application_credential_id"></a>
###### application_credential_id

- Schema name: `Application Credential Id`
- Type: string
- Default: ""

Swift application credential ID for authentication.

<a id="headingReturn_value_credentials_provider_oneOf_i16_application_credential_name"></a>
<a id="Return_value_credentials_provider_oneOf_i16_application_credential_name"></a>
###### application_credential_name

- Schema name: `Application Credential Name`
- Type: string
- Default: ""

Swift application credential name for authentication.

<a id="headingReturn_value_credentials_provider_oneOf_i16_application_credential_secret"></a>
<a id="Return_value_credentials_provider_oneOf_i16_application_credential_secret"></a>
###### application_credential_secret

- Schema name: `Application Credential Secret`
- Type: string
- Default: ""

Swift application credential secret for authentication.

<a id="headingReturn_value_credentials_provider_oneOf_i16_auth_version"></a>
<a id="Return_value_credentials_provider_oneOf_i16_auth_version"></a>
###### auth_version (required)

- Schema name: `Auth Version`

Swift authentication API version. `0`: Legacy auth `1`: TempAuth `2`: Keystone v2.0 `3`: Keystone v3 `null`: Auto-detect
<a id="Return_value_credentials_provider_oneOf_i16_auth_version_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_credentials_provider_oneOf_i16_auth_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_credentials_provider_oneOf_i16_auth_version_anyOf_i0)

- Type: enum (of integer)
###### Must be one of:

- 0
- 1
- 2
- 3

<a id="tab-pane_Return_value_credentials_provider_oneOf_i16_auth_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_credentials_provider_oneOf_i16_auth_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_credentials_provider_oneOf_i16_endpoint_type"></a>
<a id="Return_value_credentials_provider_oneOf_i16_endpoint_type"></a>
###### endpoint_type (required)

- Schema name: `Endpoint Type`

Swift endpoint type to use. `public`: Public endpoint (default) `internal`: Internal network endpoint `admin`: Administrative endpoint `null`: Use default
<a id="Return_value_credentials_provider_oneOf_i16_endpoint_type_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_credentials_provider_oneOf_i16_endpoint_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_credentials_provider_oneOf_i16_endpoint_type_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "public"
- "internal"
- "admin"

<a id="tab-pane_Return_value_credentials_provider_oneOf_i16_endpoint_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_credentials_provider_oneOf_i16_endpoint_type_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_credentials_provider_oneOf_i17"></a>
###### [WebDavCredentialsModel](#tab-pane_Return_value_credentials_provider_oneOf_i17)

- Schema name: `WebDavCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credentials_provider_oneOf_i17_type"></a>
<a id="Return_value_credentials_provider_oneOf_i17_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for WebDAV servers.
- Specific value: `"WEBDAV"`

<a id="headingReturn_value_credentials_provider_oneOf_i17_url"></a>
<a id="Return_value_credentials_provider_oneOf_i17_url"></a>
###### url (required)

- Schema name: `Url`
- Type: string
- Type: Format: uri

WebDAV server URL endpoint.
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="headingReturn_value_credentials_provider_oneOf_i17_vendor"></a>
<a id="Return_value_credentials_provider_oneOf_i17_vendor"></a>
###### vendor (required)

- Schema name: `Vendor`
- Type: enum (of string)

WebDAV server vendor type for compatibility optimizations. `NEXTCLOUD`: Nextcloud server `OWNCLOUD`: ownCloud server `SHAREPOINT`: Microsoft SharePoint `OTHER`: Generic WebDAV server
###### Must be one of:

- "NEXTCLOUD"
- "OWNCLOUD"
- "SHAREPOINT"
- "OTHER"

<a id="headingReturn_value_credentials_provider_oneOf_i17_user"></a>
<a id="Return_value_credentials_provider_oneOf_i17_user"></a>
###### user (required)

- Schema name: `User`
- Type: string

WebDAV username for authentication.

<a id="headingReturn_value_credentials_provider_oneOf_i17_pass"></a>
<a id="Return_value_credentials_provider_oneOf_i17_pass"></a>
###### pass (required)

- Schema name: `Pass`
- Type: string

WebDAV password for authentication.

<a id="tab-pane_Return_value_credentials_provider_oneOf_i18"></a>
###### [YandexCredentialsModel](#tab-pane_Return_value_credentials_provider_oneOf_i18)

- Schema name: `YandexCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credentials_provider_oneOf_i18_type"></a>
<a id="Return_value_credentials_provider_oneOf_i18_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Yandex Disk storage.
- Specific value: `"YANDEX"`

<a id="headingReturn_value_credentials_provider_oneOf_i18_client_id"></a>
<a id="Return_value_credentials_provider_oneOf_i18_client_id"></a>
###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

Yandex OAuth application client ID.

<a id="headingReturn_value_credentials_provider_oneOf_i18_client_secret"></a>
<a id="Return_value_credentials_provider_oneOf_i18_client_secret"></a>
###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

Yandex OAuth application client secret.

<a id="headingReturn_value_credentials_provider_oneOf_i18_token"></a>
<a id="Return_value_credentials_provider_oneOf_i18_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

Yandex OAuth access token for API authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_attributes"></a>
<a id="Return_value_attributes"></a>
#### attributes (required)

- Schema name: `CloudTaskAttributes`
- Type: object

Additional information for each backup, e.g. bucket name.
- No Additional Properties
<a id="headingReturn_value_attributes_bucket"></a>
<a id="Return_value_attributes_bucket"></a>
##### bucket

- Schema name: `Bucket`
- Type: string

Name of the cloud storage bucket or container.
- Must be at least `1` characters long

<a id="headingReturn_value_attributes_folder"></a>
<a id="Return_value_attributes_folder"></a>
##### folder

- Schema name: `Folder`
- Type: string

Path within the cloud storage bucket to use as the root directory for operations.

<a id="headingReturn_value_attributes_fast_list"></a>
<a id="Return_value_attributes_fast_list"></a>
##### fast_list

- Schema name: `Fast List`
- Type: boolean

Valid only for some providers. Use fewer transactions in exchange for more RAM. This may also speed up or slow down your transfer. See https://rclone.org/docs/#fast-list for more details.

<a id="headingReturn_value_attributes_bucket_policy_only"></a>
<a id="Return_value_attributes_bucket_policy_only"></a>
##### bucket_policy_only

- Schema name: `Bucket Policy Only`
- Type: boolean

Valid only for GOOGLE*CLOUD*STORAGE provider. Access checks should use bucket-level IAM policies. If you want to upload objects to a bucket with Bucket Policy Only set then you will need to set this.

<a id="headingReturn_value_attributes_chunk_size"></a>
<a id="Return_value_attributes_chunk_size"></a>
##### chunk_size

- Schema name: `Chunk Size`
- Type: integer

Valid only for DROPBOX provider. Upload chunk size in MiB. Must fit in memory. Note that these chunks are buffered in memory and there might be a maximum of `--transfers` chunks in progress at once. Dropbox Business accounts can have monthly data transfer limits per team per month. By using larger chunk sizes you will decrease the number of data transfer calls used and you'll be able to transfer more data to your Dropbox Business account.

<a id="headingReturn_value_attributes_acknowledge_abuse"></a>
<a id="Return_value_attributes_acknowledge_abuse"></a>
##### acknowledge_abuse

- Schema name: `Acknowledge Abuse`
- Type: boolean

Valid only for GOOGLE_DRIVER provider. Allow files which return cannotDownloadAbusiveFile to be downloaded. If downloading a file returns the error "This file has been identified as malware or spam and cannot be downloaded" with the error code "cannotDownloadAbusiveFile" then enable this flag to indicate you acknowledge the risks of downloading the file and TrueNAS will download it anyway.

<a id="headingReturn_value_attributes_region"></a>
<a id="Return_value_attributes_region"></a>
##### region

- Schema name: `Region`
- Type: string

Valid only for S3 provider. S3 Region.

<a id="headingReturn_value_attributes_encryption"></a>
<a id="Return_value_attributes_encryption"></a>
##### encryption

- Schema name: `Encryption`
- Type: enum (of null or string)

Valid only for S3 provider. Server-Side Encryption.
###### Must be one of:

- null
- "AES256"

<a id="headingReturn_value_attributes_storage_class"></a>
<a id="Return_value_attributes_storage_class"></a>
##### storage_class

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

<a id="headingReturn_value_schedule"></a>
<a id="Return_value_schedule"></a>
#### schedule

- Schema name: `CloudCron`
- Type: object

Cron schedule dictating when the task should run.
- No Additional Properties
<a id="headingReturn_value_schedule_minute"></a>
<a id="Return_value_schedule_minute"></a>
##### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

<a id="headingReturn_value_schedule_hour"></a>
<a id="Return_value_schedule_hour"></a>
##### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingReturn_value_schedule_dom"></a>
<a id="Return_value_schedule_dom"></a>
##### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingReturn_value_schedule_month"></a>
<a id="Return_value_schedule_month"></a>
##### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingReturn_value_schedule_dow"></a>
<a id="Return_value_schedule_dow"></a>
##### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingReturn_value_pre_script"></a>
<a id="Return_value_pre_script"></a>
#### pre_script

- Schema name: `Pre Script`
- Type: string
- Default: ""

A Bash script to run immediately before every backup.

<a id="headingReturn_value_post_script"></a>
<a id="Return_value_post_script"></a>
#### post_script

- Schema name: `Post Script`
- Type: string
- Default: ""

A Bash script to run immediately after every backup if it succeeds.

<a id="headingReturn_value_snapshot"></a>
<a id="Return_value_snapshot"></a>
#### snapshot

- Schema name: `Snapshot`
- Type: boolean
- Default: false

Whether to create a temporary snapshot of the dataset before every backup.

<a id="headingReturn_value_include"></a>
<a id="Return_value_include"></a>
#### include

- Schema name: `Include`
- Type: array of string

Paths to pass to `restic backup --include`.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_include_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_exclude"></a>
<a id="Return_value_exclude"></a>
#### exclude

- Schema name: `Exclude`
- Type: array of string

Paths to pass to `restic backup --exclude`.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_exclude_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_args"></a>
<a id="Return_value_args"></a>
#### args

- Schema name: `Args`
- Type: string
- Default: ""

(Slated for removal).

<a id="headingReturn_value_enabled"></a>
<a id="Return_value_enabled"></a>
#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Can enable/disable the task.

<a id="headingReturn_value_job"></a>
<a id="Return_value_job"></a>
#### job (required)

- Schema name: `Job`

Information regarding the task's job state, e.g. progress.
<a id="Return_value_job_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_job_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_job_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_job_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_job_anyOf_i1)

- Type: null

<a id="headingReturn_value_locked"></a>
<a id="Return_value_locked"></a>
#### locked (required)

- Schema name: `Locked`
- Type: boolean

A locked task cannot run.

<a id="headingReturn_value_bwlimit"></a>
<a id="Return_value_bwlimit"></a>
#### bwlimit

- Schema name: `Bwlimit`
- Type: array of object

Schedule of bandwidth limits.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_bwlimit_items"></a>
##### CloudSyncBwlimit

- Schema name: `CloudSyncBwlimit`
- Type: object
- No Additional Properties
<a id="headingReturn_value_bwlimit_items_time"></a>
<a id="Return_value_bwlimit_items_time"></a>
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

<a id="headingReturn_value_bwlimit_items_bandwidth"></a>
<a id="Return_value_bwlimit_items_bandwidth"></a>
###### bandwidth (required)

- Schema name: `Bandwidth`

Bandwidth limit in bytes per second (upload and download).
<a id="Return_value_bwlimit_items_bandwidth_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_bwlimit_items_bandwidth_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_bwlimit_items_bandwidth_anyOf_i0)

- Type: integer
- Value must be strictly greater than `0`

<a id="tab-pane_Return_value_bwlimit_items_bandwidth_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_bwlimit_items_bandwidth_anyOf_i1)

- Type: null

<a id="headingReturn_value_transfers"></a>
<a id="Return_value_transfers"></a>
#### transfers

- Schema name: `Transfers`
- Default: null

Maximum number of parallel file transfers. `null` for default.
<a id="Return_value_transfers_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_transfers_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_transfers_anyOf_i0)

- Type: integer
- Value must be strictly greater than `0`

<a id="tab-pane_Return_value_transfers_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_transfers_anyOf_i1)

- Type: null

<a id="headingReturn_value_direction"></a>
<a id="Return_value_direction"></a>
#### direction (required)

- Schema name: `Direction`
- Type: enum (of string)

Direction of the cloud sync operation. `PUSH`: Upload local files to cloud storage `PULL`: Download files from cloud storage to local storage
##### Must be one of:

- "PUSH"
- "PULL"

<a id="headingReturn_value_transfer_mode"></a>
<a id="Return_value_transfer_mode"></a>
#### transfer_mode (required)

- Schema name: `Transfer Mode`
- Type: enum (of string)

How files are transferred between local and cloud storage. `SYNC`: Synchronize directories (add new, update changed, remove deleted) `COPY`: Copy files without removing any existing files `MOVE`: Move files (copy then delete from source)
##### Must be one of:

- "SYNC"
- "COPY"
- "MOVE"

<a id="headingReturn_value_encryption"></a>
<a id="Return_value_encryption"></a>
#### encryption

- Schema name: `Encryption`
- Type: boolean
- Default: false

Whether to encrypt files before uploading to cloud storage.

<a id="headingReturn_value_filename_encryption"></a>
<a id="Return_value_filename_encryption"></a>
#### filename_encryption

- Schema name: `Filename Encryption`
- Type: boolean
- Default: false

Whether to encrypt filenames in addition to file contents.

<a id="headingReturn_value_encryption_password"></a>
<a id="Return_value_encryption_password"></a>
#### encryption_password

- Schema name: `Encryption Password`
- Type: string
- Default: ""

Password for client-side encryption. Empty string if encryption is disabled.

<a id="headingReturn_value_encryption_salt"></a>
<a id="Return_value_encryption_salt"></a>
#### encryption_salt

- Schema name: `Encryption Salt`
- Type: string
- Default: ""

Salt value for encryption key derivation. Empty string if encryption is disabled.

<a id="headingReturn_value_create_empty_src_dirs"></a>
<a id="Return_value_create_empty_src_dirs"></a>
#### create_empty_src_dirs

- Schema name: `Create Empty Src Dirs`
- Type: boolean
- Default: false

Whether to create empty directories in the destination that exist in the source.

<a id="headingReturn_value_follow_symlinks"></a>
<a id="Return_value_follow_symlinks"></a>
#### follow_symlinks

- Schema name: `Follow Symlinks`
- Type: boolean
- Default: false

Whether to follow symbolic links and sync the files they point to.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
