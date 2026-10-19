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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filters

<a id="Call_parameters_items_i0"></a>
#### filters

- Schema name: `filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i0_items"></a>
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
                "name",
                "=",
                "bob"
            ],
            [
                "name",
                "=",
                "larry"
            ]
        ]
    ]
]
```

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
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
- Value must be greater or equal to `0`

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0` and lesser or equal to `10000`

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

- Schema name: `Result`
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items"></a>
###### CredentialsEntry

- Schema name: `CredentialsEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_id"></a>
<a id="Return_value_anyOf_i0_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the cloud credential.

<a id="headingReturn_value_anyOf_i0_items_name"></a>
<a id="Return_value_anyOf_i0_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the cloud credential.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_provider"></a>
<a id="Return_value_anyOf_i0_items_provider"></a>
###### provider (required)

- Schema name: `Provider`

Cloud provider configuration including type and authentication details.
<a id="Return_value_anyOf_i0_items_provider_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i0"></a>
###### [AzureBlobCredentialsModel](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i0)

- Schema name: `AzureBlobCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i0_type"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i0_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Microsoft Azure Blob storage.
- Specific value: `"AZUREBLOB"`

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i0_account"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i0_account"></a>
###### account (required)

- Schema name: `Account`
- Type: string

Azure Blob Storage account name for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i0_key"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i0_key"></a>
###### key (required)

- Schema name: `Key`
- Type: string

Azure Blob Storage access key for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i0_endpoint"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i0_endpoint"></a>
###### endpoint

- Schema name: `Endpoint`
- Default: ""

Custom Azure Blob Storage endpoint URL. Empty string for default endpoints.
<a id="Return_value_anyOf_i0_items_provider_oneOf_i0_endpoint_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i0_endpoint_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i0_endpoint_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i0_endpoint_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i0_endpoint_anyOf_i1)

- Type: string
- Type: Format: uri
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i1"></a>
###### [B2CredentialsModel](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i1)

- Schema name: `B2CredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i1_type"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i1_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Backblaze B2 storage.
- Specific value: `"B2"`

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i1_account"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i1_account"></a>
###### account (required)

- Schema name: `Account`
- Type: string

Backblaze B2 account ID for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i1_key"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i1_key"></a>
###### key (required)

- Schema name: `Key`
- Type: string

Backblaze B2 application key for authentication.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i2"></a>
###### [BoxCredentialsModel](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i2)

- Schema name: `BoxCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i2_type"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i2_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Box cloud storage.
- Specific value: `"BOX"`

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i2_client_id"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i2_client_id"></a>
###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

Box OAuth application client ID.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i2_client_secret"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i2_client_secret"></a>
###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

Box OAuth application client secret.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i2_token"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i2_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

Box OAuth access token for API authentication.
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i3"></a>
###### [DropboxCredentialsModel](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i3)

- Schema name: `DropboxCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i3_type"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i3_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Dropbox storage.
- Specific value: `"DROPBOX"`

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i3_client_id"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i3_client_id"></a>
###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

Dropbox OAuth application client ID.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i3_client_secret"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i3_client_secret"></a>
###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

Dropbox OAuth application client secret.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i3_token"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i3_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

Dropbox OAuth access token for API authentication.
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i4"></a>
###### [FTPCredentialsModel](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i4)

- Schema name: `FTPCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i4_type"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i4_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for FTP.
- Specific value: `"FTP"`

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i4_host"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i4_host"></a>
###### host (required)

- Schema name: `Host`
- Type: string

FTP server hostname or IP address.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i4_port"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i4_port"></a>
###### port

- Schema name: `Port`
- Type: integer
- Default: "**********"

FTP server port number.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i4_user"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i4_user"></a>
###### user (required)

- Schema name: `User`
- Type: string

FTP username for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i4_pass"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i4_pass"></a>
###### pass (required)

- Schema name: `Pass`
- Type: string

FTP password for authentication.

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i5"></a>
###### [GoogleCloudStorageCredentialsModel](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i5)

- Schema name: `GoogleCloudStorageCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i5_type"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i5_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Google Cloud Storage.
- Specific value: `"GOOGLE_CLOUD_STORAGE"`

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i5_service_account_credentials"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i5_service_account_credentials"></a>
###### service_account_credentials (required)

- Schema name: `Service Account Credentials`
- Type: string

JSON service account credentials for Google Cloud Storage authentication.
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i6"></a>
###### [GoogleDriveCredentialsModel](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i6)

- Schema name: `GoogleDriveCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i6_type"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i6_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Google Drive.
- Specific value: `"GOOGLE_DRIVE"`

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i6_client_id"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i6_client_id"></a>
###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

OAuth client ID for Google Drive API access.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i6_client_secret"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i6_client_secret"></a>
###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

OAuth client secret for Google Drive API access.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i6_token"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i6_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

OAuth access token for Google Drive authentication.
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i6_team_drive"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i6_team_drive"></a>
###### team_drive

- Schema name: `Team Drive`
- Type: string
- Default: ""

Google Drive team drive ID or empty string for personal drive.

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i7"></a>
###### [GooglePhotosCredentialsModel](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i7)

- Schema name: `GooglePhotosCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i7_type"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i7_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Google Photos.
- Specific value: `"GOOGLE_PHOTOS"`

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i7_client_id"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i7_client_id"></a>
###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

OAuth client ID for Google Photos API access.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i7_client_secret"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i7_client_secret"></a>
###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

OAuth client secret for Google Photos API access.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i7_token"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i7_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

OAuth access token for Google Photos authentication.
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i8"></a>
###### [HTTPCredentialsModel](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i8)

- Schema name: `HTTPCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i8_type"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i8_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for HTTP.
- Specific value: `"HTTP"`

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i8_url"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i8_url"></a>
###### url (required)

- Schema name: `Url`
- Type: string
- Type: Format: uri

HTTP URL for file access.
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i9"></a>
###### [HubicCredentialsModel](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i9)

- Schema name: `HubicCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i9_type"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i9_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Hubic.
- Specific value: `"HUBIC"`

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i9_token"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i9_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

OAuth access token for Hubic authentication.
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i10"></a>
###### [MegaCredentialsModel](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i10)

- Schema name: `MegaCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i10_type"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i10_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for MEGA.
- Specific value: `"MEGA"`

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i10_user"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i10_user"></a>
###### user (required)

- Schema name: `User`
- Type: string

MEGA username for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i10_pass"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i10_pass"></a>
###### pass (required)

- Schema name: `Pass`
- Type: string

MEGA password for authentication.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i11"></a>
###### [OneDriveCredentialsModel](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i11)

- Schema name: `OneDriveCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i11_type"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i11_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for OneDrive.
- Specific value: `"ONEDRIVE"`

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i11_client_id"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i11_client_id"></a>
###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

OAuth client ID for OneDrive API access.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i11_client_secret"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i11_client_secret"></a>
###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

OAuth client secret for OneDrive API access.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i11_token"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i11_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

OAuth access token for OneDrive authentication.
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i11_drive_type"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i11_drive_type"></a>
###### drive_type (required)

- Schema name: `Drive Type`
- Type: enum (of string)

Type of OneDrive to access.
###### Must be one of:

- "PERSONAL"
- "BUSINESS"
- "DOCUMENT_LIBRARY"

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i11_drive_id"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i11_drive_id"></a>
###### drive_id (required)

- Schema name: `Drive Id`
- Type: string

OneDrive drive identifier.

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i12"></a>
###### [PCloudCredentialsModel](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i12)

- Schema name: `PCloudCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i12_type"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i12_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for pCloud.
- Specific value: `"PCLOUD"`

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i12_client_id"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i12_client_id"></a>
###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

OAuth client ID for pCloud API access.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i12_client_secret"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i12_client_secret"></a>
###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

OAuth client secret for pCloud API access.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i12_token"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i12_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

OAuth access token for pCloud authentication.
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i12_hostname"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i12_hostname"></a>
###### hostname

- Schema name: `Hostname`
- Type: string
- Default: ""

pCloud hostname or empty string for default.

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i13"></a>
###### [S3CredentialsModel](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i13)

- Schema name: `S3CredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i13_type"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i13_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for S3-compatible storage.
- Specific value: `"S3"`

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i13_access_key_id"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i13_access_key_id"></a>
###### access_key_id (required)

- Schema name: `Access Key Id`
- Type: string

S3 access key ID for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i13_secret_access_key"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i13_secret_access_key"></a>
###### secret_access_key (required)

- Schema name: `Secret Access Key`
- Type: string

S3 secret access key for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i13_endpoint"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i13_endpoint"></a>
###### endpoint

- Schema name: `Endpoint`
- Default: ""

S3-compatible endpoint URL or empty string for AWS S3.
<a id="Return_value_anyOf_i0_items_provider_oneOf_i13_endpoint_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i13_endpoint_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i13_endpoint_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i13_endpoint_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i13_endpoint_anyOf_i1)

- Type: string
- Type: Format: uri
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i13_region"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i13_region"></a>
###### region

- Schema name: `Region`
- Type: string
- Default: ""

S3 region or empty string for default.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i13_skip_region"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i13_skip_region"></a>
###### skip_region

- Schema name: `Skip Region`
- Type: boolean
- Default: ""

Whether to skip region validation.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i13_signatures_v2"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i13_signatures_v2"></a>
###### signatures_v2

- Schema name: `Signatures V2`
- Type: boolean
- Default: ""

Whether to use AWS Signature Version 2.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i13_max_upload_parts"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i13_max_upload_parts"></a>
###### max_upload_parts

- Schema name: `Max Upload Parts`
- Type: integer
- Default: "**********"

Maximum number of parts for multipart uploads.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i13_provider"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i13_provider"></a>
###### provider

- Schema name: `Provider`
- Type: string
- Default: "Other"

S3 provider. See `cloudsync.credentials.s3_provider_choices` for possible values.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i13_force_path_style"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i13_force_path_style"></a>
###### force_path_style

- Schema name: `Force Path Style`
- Type: boolean
- Default: true

If true use path style access if false use virtual hosted style.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i13_sign_accept_encoding"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i13_sign_accept_encoding"></a>
###### sign_accept_encoding

- Schema name: `Sign Accept Encoding`
- Type: boolean
- Default: true

Set this to `false` if your S3 server is behind a proxy that modified HTTP headers and you are experiencing `SignatureDoesNotMatch` error.

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i14"></a>
###### [SFTPCredentialsModel](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i14)

- Schema name: `SFTPCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i14_type"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i14_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for SFTP.
- Specific value: `"SFTP"`

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i14_host"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i14_host"></a>
###### host (required)

- Schema name: `Host`
- Type: string

SFTP server hostname or IP address.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i14_port"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i14_port"></a>
###### port

- Schema name: `Port`
- Type: integer
- Default: "**********"

SFTP server port number.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i14_user"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i14_user"></a>
###### user (required)

- Schema name: `User`
- Type: string

SFTP username for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i14_pass"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i14_pass"></a>
###### pass

- Schema name: `Pass`
- Default: ""

SFTP password for authentication or `null` for key-based auth.
<a id="Return_value_anyOf_i0_items_provider_oneOf_i14_pass_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i14_pass_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i14_pass_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i14_pass_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i14_pass_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i14_private_key"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i14_private_key"></a>
###### private_key

- Schema name: `Private Key`
- Default: ""

SSH private key ID for authentication or `null` for password auth.
<a id="Return_value_anyOf_i0_items_provider_oneOf_i14_private_key_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i14_private_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i14_private_key_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i14_private_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i14_private_key_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i15"></a>
###### [StorjIxCredentialsModel](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i15)

- Schema name: `StorjIxCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i15_type"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i15_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Storj decentralized storage.
- Specific value: `"STORJ_IX"`

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i15_access_key_id"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i15_access_key_id"></a>
###### access_key_id (required)

- Schema name: `Access Key Id`
- Type: string

Storj S3-compatible access key ID for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i15_secret_access_key"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i15_secret_access_key"></a>
###### secret_access_key (required)

- Schema name: `Secret Access Key`
- Type: string

Storj S3-compatible secret access key for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i15_endpoint"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i15_endpoint"></a>
###### endpoint

- Schema name: `Endpoint`
- Type: string
- Default: "https://gateway.storjshare.io/"

Storj gateway endpoint URL for S3-compatible access.

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i16"></a>
###### [SwiftCredentialsModel](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i16)

- Schema name: `SwiftCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i16_type"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i16_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for OpenStack Swift storage.
- Specific value: `"OPENSTACK_SWIFT"`

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i16_user"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i16_user"></a>
###### user (required)

- Schema name: `User`
- Type: string

Swift username for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i16_key"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i16_key"></a>
###### key (required)

- Schema name: `Key`
- Type: string

Swift password or API key for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i16_auth"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i16_auth"></a>
###### auth (required)

- Schema name: `Auth`
- Type: string

Swift authentication URL endpoint.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i16_user_id"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i16_user_id"></a>
###### user_id

- Schema name: `User Id`
- Type: string
- Default: ""

Swift user ID for authentication.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i16_domain"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i16_domain"></a>
###### domain

- Schema name: `Domain`
- Type: string
- Default: ""

Swift domain name for authentication.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i16_tenant"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i16_tenant"></a>
###### tenant

- Schema name: `Tenant`
- Type: string
- Default: ""

Swift tenant name for multi-tenancy.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i16_tenant_id"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i16_tenant_id"></a>
###### tenant_id

- Schema name: `Tenant Id`
- Type: string
- Default: ""

Swift tenant ID for multi-tenancy.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i16_tenant_domain"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i16_tenant_domain"></a>
###### tenant_domain

- Schema name: `Tenant Domain`
- Type: string
- Default: ""

Swift tenant domain name.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i16_region"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i16_region"></a>
###### region

- Schema name: `Region`
- Type: string
- Default: ""

Swift region name for geographic distribution.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i16_storage_url"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i16_storage_url"></a>
###### storage_url

- Schema name: `Storage Url`
- Type: string
- Default: ""

Swift storage URL endpoint.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i16_auth_token"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i16_auth_token"></a>
###### auth_token

- Schema name: `Auth Token`
- Type: string
- Default: ""

Swift authentication token for pre-authenticated access.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i16_application_credential_id"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i16_application_credential_id"></a>
###### application_credential_id

- Schema name: `Application Credential Id`
- Type: string
- Default: ""

Swift application credential ID for authentication.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i16_application_credential_name"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i16_application_credential_name"></a>
###### application_credential_name

- Schema name: `Application Credential Name`
- Type: string
- Default: ""

Swift application credential name for authentication.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i16_application_credential_secret"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i16_application_credential_secret"></a>
###### application_credential_secret

- Schema name: `Application Credential Secret`
- Type: string
- Default: ""

Swift application credential secret for authentication.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i16_auth_version"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i16_auth_version"></a>
###### auth_version (required)

- Schema name: `Auth Version`

Swift authentication API version. `0`: Legacy auth `1`: TempAuth `2`: Keystone v2.0 `3`: Keystone v3 `null`: Auto-detect
<a id="Return_value_anyOf_i0_items_provider_oneOf_i16_auth_version_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i16_auth_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i16_auth_version_anyOf_i0)

- Type: enum (of integer)
###### Must be one of:

- 0
- 1
- 2
- 3

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i16_auth_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i16_auth_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i16_endpoint_type"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i16_endpoint_type"></a>
###### endpoint_type (required)

- Schema name: `Endpoint Type`

Swift endpoint type to use. `public`: Public endpoint (default) `internal`: Internal network endpoint `admin`: Administrative endpoint `null`: Use default
<a id="Return_value_anyOf_i0_items_provider_oneOf_i16_endpoint_type_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i16_endpoint_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i16_endpoint_type_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "public"
- "internal"
- "admin"

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i16_endpoint_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i16_endpoint_type_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i17"></a>
###### [WebDavCredentialsModel](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i17)

- Schema name: `WebDavCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i17_type"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i17_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for WebDAV servers.
- Specific value: `"WEBDAV"`

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i17_url"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i17_url"></a>
###### url (required)

- Schema name: `Url`
- Type: string
- Type: Format: uri

WebDAV server URL endpoint.
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i17_vendor"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i17_vendor"></a>
###### vendor (required)

- Schema name: `Vendor`
- Type: enum (of string)

WebDAV server vendor type for compatibility optimizations. `NEXTCLOUD`: Nextcloud server `OWNCLOUD`: ownCloud server `SHAREPOINT`: Microsoft SharePoint `OTHER`: Generic WebDAV server
###### Must be one of:

- "NEXTCLOUD"
- "OWNCLOUD"
- "SHAREPOINT"
- "OTHER"

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i17_user"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i17_user"></a>
###### user (required)

- Schema name: `User`
- Type: string

WebDAV username for authentication.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i17_pass"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i17_pass"></a>
###### pass (required)

- Schema name: `Pass`
- Type: string

WebDAV password for authentication.

<a id="tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i18"></a>
###### [YandexCredentialsModel](#tab-pane_Return_value_anyOf_i0_items_provider_oneOf_i18)

- Schema name: `YandexCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i18_type"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i18_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Yandex Disk storage.
- Specific value: `"YANDEX"`

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i18_client_id"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i18_client_id"></a>
###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

Yandex OAuth application client ID.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i18_client_secret"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i18_client_secret"></a>
###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

Yandex OAuth application client secret.

<a id="headingReturn_value_anyOf_i0_items_provider_oneOf_i18_token"></a>
<a id="Return_value_anyOf_i0_items_provider_oneOf_i18_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

Yandex OAuth access token for API authentication.
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [CredentialsEntry](#tab-pane_Return_value_anyOf_i1)

- Schema name: `CredentialsEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_id"></a>
<a id="Return_value_anyOf_i1_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the cloud credential.

<a id="headingReturn_value_anyOf_i1_name"></a>
<a id="Return_value_anyOf_i1_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the cloud credential.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_provider"></a>
<a id="Return_value_anyOf_i1_provider"></a>
###### provider (required)

- Schema name: `Provider`

Cloud provider configuration including type and authentication details.
<a id="Return_value_anyOf_i1_provider_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_anyOf_i1_provider_oneOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_provider_oneOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_provider_oneOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_provider_oneOf_i1)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_provider_oneOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_anyOf_i1_provider_oneOf_i2)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_provider_oneOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_anyOf_i1_provider_oneOf_i3)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_provider_oneOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_anyOf_i1_provider_oneOf_i4)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_provider_oneOf_i5"></a>
###### [Option 6](#tab-pane_Return_value_anyOf_i1_provider_oneOf_i5)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_provider_oneOf_i6"></a>
###### [Option 7](#tab-pane_Return_value_anyOf_i1_provider_oneOf_i6)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_provider_oneOf_i7"></a>
###### [Option 8](#tab-pane_Return_value_anyOf_i1_provider_oneOf_i7)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_provider_oneOf_i8"></a>
###### [Option 9](#tab-pane_Return_value_anyOf_i1_provider_oneOf_i8)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_provider_oneOf_i9"></a>
###### [Option 10](#tab-pane_Return_value_anyOf_i1_provider_oneOf_i9)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_provider_oneOf_i10"></a>
###### [Option 11](#tab-pane_Return_value_anyOf_i1_provider_oneOf_i10)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_provider_oneOf_i11"></a>
###### [Option 12](#tab-pane_Return_value_anyOf_i1_provider_oneOf_i11)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_provider_oneOf_i12"></a>
###### [Option 13](#tab-pane_Return_value_anyOf_i1_provider_oneOf_i12)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_provider_oneOf_i13"></a>
###### [Option 14](#tab-pane_Return_value_anyOf_i1_provider_oneOf_i13)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_provider_oneOf_i14"></a>
###### [Option 15](#tab-pane_Return_value_anyOf_i1_provider_oneOf_i14)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_provider_oneOf_i15"></a>
###### [Option 16](#tab-pane_Return_value_anyOf_i1_provider_oneOf_i15)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_provider_oneOf_i16"></a>
###### [Option 17](#tab-pane_Return_value_anyOf_i1_provider_oneOf_i16)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_provider_oneOf_i17"></a>
###### [Option 18](#tab-pane_Return_value_anyOf_i1_provider_oneOf_i17)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_provider_oneOf_i18"></a>
###### [Option 19](#tab-pane_Return_value_anyOf_i1_provider_oneOf_i18)

- Type: object

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items"></a>
###### CredentialsQueryResultItem

- Schema name: `CredentialsQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_id"></a>
<a id="Return_value_anyOf_i2_items_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the cloud credential.

<a id="headingReturn_value_anyOf_i2_items_name"></a>
<a id="Return_value_anyOf_i2_items_name"></a>
###### name

- Schema name: `Name`
- Type: string

Human-readable name for the cloud credential.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_provider"></a>
<a id="Return_value_anyOf_i2_items_provider"></a>
###### provider

- Schema name: `Provider`

Cloud provider configuration including type and authentication details.
<a id="Return_value_anyOf_i2_items_provider_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i0"></a>
###### [AzureBlobCredentialsModel](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i0)

- Schema name: `AzureBlobCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i0_type"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i0_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Microsoft Azure Blob storage.
- Specific value: `"AZUREBLOB"`

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i0_account"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i0_account"></a>
###### account (required)

- Schema name: `Account`
- Type: string

Azure Blob Storage account name for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i0_key"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i0_key"></a>
###### key (required)

- Schema name: `Key`
- Type: string

Azure Blob Storage access key for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i0_endpoint"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i0_endpoint"></a>
###### endpoint

- Schema name: `Endpoint`
- Default: ""

Custom Azure Blob Storage endpoint URL. Empty string for default endpoints.
<a id="Return_value_anyOf_i2_items_provider_oneOf_i0_endpoint_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i0_endpoint_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i0_endpoint_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i0_endpoint_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i0_endpoint_anyOf_i1)

- Type: string
- Type: Format: uri
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i1"></a>
###### [B2CredentialsModel](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i1)

- Schema name: `B2CredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i1_type"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i1_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Backblaze B2 storage.
- Specific value: `"B2"`

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i1_account"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i1_account"></a>
###### account (required)

- Schema name: `Account`
- Type: string

Backblaze B2 account ID for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i1_key"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i1_key"></a>
###### key (required)

- Schema name: `Key`
- Type: string

Backblaze B2 application key for authentication.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i2"></a>
###### [BoxCredentialsModel](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i2)

- Schema name: `BoxCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i2_type"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i2_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Box cloud storage.
- Specific value: `"BOX"`

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i2_client_id"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i2_client_id"></a>
###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

Box OAuth application client ID.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i2_client_secret"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i2_client_secret"></a>
###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

Box OAuth application client secret.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i2_token"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i2_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

Box OAuth access token for API authentication.
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i3"></a>
###### [DropboxCredentialsModel](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i3)

- Schema name: `DropboxCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i3_type"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i3_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Dropbox storage.
- Specific value: `"DROPBOX"`

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i3_client_id"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i3_client_id"></a>
###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

Dropbox OAuth application client ID.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i3_client_secret"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i3_client_secret"></a>
###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

Dropbox OAuth application client secret.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i3_token"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i3_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

Dropbox OAuth access token for API authentication.
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i4"></a>
###### [FTPCredentialsModel](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i4)

- Schema name: `FTPCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i4_type"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i4_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for FTP.
- Specific value: `"FTP"`

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i4_host"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i4_host"></a>
###### host (required)

- Schema name: `Host`
- Type: string

FTP server hostname or IP address.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i4_port"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i4_port"></a>
###### port

- Schema name: `Port`
- Type: integer
- Default: "**********"

FTP server port number.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i4_user"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i4_user"></a>
###### user (required)

- Schema name: `User`
- Type: string

FTP username for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i4_pass"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i4_pass"></a>
###### pass (required)

- Schema name: `Pass`
- Type: string

FTP password for authentication.

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i5"></a>
###### [GoogleCloudStorageCredentialsModel](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i5)

- Schema name: `GoogleCloudStorageCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i5_type"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i5_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Google Cloud Storage.
- Specific value: `"GOOGLE_CLOUD_STORAGE"`

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i5_service_account_credentials"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i5_service_account_credentials"></a>
###### service_account_credentials (required)

- Schema name: `Service Account Credentials`
- Type: string

JSON service account credentials for Google Cloud Storage authentication.
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i6"></a>
###### [GoogleDriveCredentialsModel](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i6)

- Schema name: `GoogleDriveCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i6_type"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i6_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Google Drive.
- Specific value: `"GOOGLE_DRIVE"`

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i6_client_id"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i6_client_id"></a>
###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

OAuth client ID for Google Drive API access.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i6_client_secret"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i6_client_secret"></a>
###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

OAuth client secret for Google Drive API access.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i6_token"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i6_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

OAuth access token for Google Drive authentication.
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i6_team_drive"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i6_team_drive"></a>
###### team_drive

- Schema name: `Team Drive`
- Type: string
- Default: ""

Google Drive team drive ID or empty string for personal drive.

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i7"></a>
###### [GooglePhotosCredentialsModel](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i7)

- Schema name: `GooglePhotosCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i7_type"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i7_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Google Photos.
- Specific value: `"GOOGLE_PHOTOS"`

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i7_client_id"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i7_client_id"></a>
###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

OAuth client ID for Google Photos API access.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i7_client_secret"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i7_client_secret"></a>
###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

OAuth client secret for Google Photos API access.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i7_token"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i7_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

OAuth access token for Google Photos authentication.
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i8"></a>
###### [HTTPCredentialsModel](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i8)

- Schema name: `HTTPCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i8_type"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i8_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for HTTP.
- Specific value: `"HTTP"`

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i8_url"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i8_url"></a>
###### url (required)

- Schema name: `Url`
- Type: string
- Type: Format: uri

HTTP URL for file access.
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i9"></a>
###### [HubicCredentialsModel](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i9)

- Schema name: `HubicCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i9_type"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i9_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Hubic.
- Specific value: `"HUBIC"`

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i9_token"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i9_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

OAuth access token for Hubic authentication.
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i10"></a>
###### [MegaCredentialsModel](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i10)

- Schema name: `MegaCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i10_type"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i10_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for MEGA.
- Specific value: `"MEGA"`

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i10_user"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i10_user"></a>
###### user (required)

- Schema name: `User`
- Type: string

MEGA username for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i10_pass"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i10_pass"></a>
###### pass (required)

- Schema name: `Pass`
- Type: string

MEGA password for authentication.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i11"></a>
###### [OneDriveCredentialsModel](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i11)

- Schema name: `OneDriveCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i11_type"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i11_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for OneDrive.
- Specific value: `"ONEDRIVE"`

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i11_client_id"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i11_client_id"></a>
###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

OAuth client ID for OneDrive API access.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i11_client_secret"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i11_client_secret"></a>
###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

OAuth client secret for OneDrive API access.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i11_token"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i11_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

OAuth access token for OneDrive authentication.
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i11_drive_type"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i11_drive_type"></a>
###### drive_type (required)

- Schema name: `Drive Type`
- Type: enum (of string)

Type of OneDrive to access.
###### Must be one of:

- "PERSONAL"
- "BUSINESS"
- "DOCUMENT_LIBRARY"

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i11_drive_id"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i11_drive_id"></a>
###### drive_id (required)

- Schema name: `Drive Id`
- Type: string

OneDrive drive identifier.

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i12"></a>
###### [PCloudCredentialsModel](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i12)

- Schema name: `PCloudCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i12_type"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i12_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for pCloud.
- Specific value: `"PCLOUD"`

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i12_client_id"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i12_client_id"></a>
###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

OAuth client ID for pCloud API access.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i12_client_secret"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i12_client_secret"></a>
###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

OAuth client secret for pCloud API access.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i12_token"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i12_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

OAuth access token for pCloud authentication.
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i12_hostname"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i12_hostname"></a>
###### hostname

- Schema name: `Hostname`
- Type: string
- Default: ""

pCloud hostname or empty string for default.

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i13"></a>
###### [S3CredentialsModel](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i13)

- Schema name: `S3CredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i13_type"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i13_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for S3-compatible storage.
- Specific value: `"S3"`

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i13_access_key_id"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i13_access_key_id"></a>
###### access_key_id (required)

- Schema name: `Access Key Id`
- Type: string

S3 access key ID for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i13_secret_access_key"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i13_secret_access_key"></a>
###### secret_access_key (required)

- Schema name: `Secret Access Key`
- Type: string

S3 secret access key for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i13_endpoint"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i13_endpoint"></a>
###### endpoint

- Schema name: `Endpoint`
- Default: ""

S3-compatible endpoint URL or empty string for AWS S3.
<a id="Return_value_anyOf_i2_items_provider_oneOf_i13_endpoint_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i13_endpoint_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i13_endpoint_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i13_endpoint_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i13_endpoint_anyOf_i1)

- Type: string
- Type: Format: uri
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i13_region"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i13_region"></a>
###### region

- Schema name: `Region`
- Type: string
- Default: ""

S3 region or empty string for default.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i13_skip_region"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i13_skip_region"></a>
###### skip_region

- Schema name: `Skip Region`
- Type: boolean
- Default: ""

Whether to skip region validation.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i13_signatures_v2"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i13_signatures_v2"></a>
###### signatures_v2

- Schema name: `Signatures V2`
- Type: boolean
- Default: ""

Whether to use AWS Signature Version 2.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i13_max_upload_parts"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i13_max_upload_parts"></a>
###### max_upload_parts

- Schema name: `Max Upload Parts`
- Type: integer
- Default: "**********"

Maximum number of parts for multipart uploads.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i13_provider"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i13_provider"></a>
###### provider

- Schema name: `Provider`
- Type: string
- Default: "Other"

S3 provider. See `cloudsync.credentials.s3_provider_choices` for possible values.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i13_force_path_style"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i13_force_path_style"></a>
###### force_path_style

- Schema name: `Force Path Style`
- Type: boolean
- Default: true

If true use path style access if false use virtual hosted style.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i13_sign_accept_encoding"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i13_sign_accept_encoding"></a>
###### sign_accept_encoding

- Schema name: `Sign Accept Encoding`
- Type: boolean
- Default: true

Set this to `false` if your S3 server is behind a proxy that modified HTTP headers and you are experiencing `SignatureDoesNotMatch` error.

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i14"></a>
###### [SFTPCredentialsModel](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i14)

- Schema name: `SFTPCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i14_type"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i14_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for SFTP.
- Specific value: `"SFTP"`

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i14_host"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i14_host"></a>
###### host (required)

- Schema name: `Host`
- Type: string

SFTP server hostname or IP address.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i14_port"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i14_port"></a>
###### port

- Schema name: `Port`
- Type: integer
- Default: "**********"

SFTP server port number.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i14_user"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i14_user"></a>
###### user (required)

- Schema name: `User`
- Type: string

SFTP username for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i14_pass"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i14_pass"></a>
###### pass

- Schema name: `Pass`
- Default: ""

SFTP password for authentication or `null` for key-based auth.
<a id="Return_value_anyOf_i2_items_provider_oneOf_i14_pass_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i14_pass_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i14_pass_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i14_pass_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i14_pass_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i14_private_key"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i14_private_key"></a>
###### private_key

- Schema name: `Private Key`
- Default: ""

SSH private key ID for authentication or `null` for password auth.
<a id="Return_value_anyOf_i2_items_provider_oneOf_i14_private_key_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i14_private_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i14_private_key_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i14_private_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i14_private_key_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i15"></a>
###### [StorjIxCredentialsModel](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i15)

- Schema name: `StorjIxCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i15_type"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i15_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Storj decentralized storage.
- Specific value: `"STORJ_IX"`

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i15_access_key_id"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i15_access_key_id"></a>
###### access_key_id (required)

- Schema name: `Access Key Id`
- Type: string

Storj S3-compatible access key ID for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i15_secret_access_key"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i15_secret_access_key"></a>
###### secret_access_key (required)

- Schema name: `Secret Access Key`
- Type: string

Storj S3-compatible secret access key for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i15_endpoint"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i15_endpoint"></a>
###### endpoint

- Schema name: `Endpoint`
- Type: string
- Default: "https://gateway.storjshare.io/"

Storj gateway endpoint URL for S3-compatible access.

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i16"></a>
###### [SwiftCredentialsModel](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i16)

- Schema name: `SwiftCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i16_type"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i16_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for OpenStack Swift storage.
- Specific value: `"OPENSTACK_SWIFT"`

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i16_user"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i16_user"></a>
###### user (required)

- Schema name: `User`
- Type: string

Swift username for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i16_key"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i16_key"></a>
###### key (required)

- Schema name: `Key`
- Type: string

Swift password or API key for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i16_auth"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i16_auth"></a>
###### auth (required)

- Schema name: `Auth`
- Type: string

Swift authentication URL endpoint.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i16_user_id"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i16_user_id"></a>
###### user_id

- Schema name: `User Id`
- Type: string
- Default: ""

Swift user ID for authentication.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i16_domain"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i16_domain"></a>
###### domain

- Schema name: `Domain`
- Type: string
- Default: ""

Swift domain name for authentication.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i16_tenant"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i16_tenant"></a>
###### tenant

- Schema name: `Tenant`
- Type: string
- Default: ""

Swift tenant name for multi-tenancy.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i16_tenant_id"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i16_tenant_id"></a>
###### tenant_id

- Schema name: `Tenant Id`
- Type: string
- Default: ""

Swift tenant ID for multi-tenancy.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i16_tenant_domain"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i16_tenant_domain"></a>
###### tenant_domain

- Schema name: `Tenant Domain`
- Type: string
- Default: ""

Swift tenant domain name.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i16_region"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i16_region"></a>
###### region

- Schema name: `Region`
- Type: string
- Default: ""

Swift region name for geographic distribution.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i16_storage_url"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i16_storage_url"></a>
###### storage_url

- Schema name: `Storage Url`
- Type: string
- Default: ""

Swift storage URL endpoint.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i16_auth_token"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i16_auth_token"></a>
###### auth_token

- Schema name: `Auth Token`
- Type: string
- Default: ""

Swift authentication token for pre-authenticated access.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i16_application_credential_id"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i16_application_credential_id"></a>
###### application_credential_id

- Schema name: `Application Credential Id`
- Type: string
- Default: ""

Swift application credential ID for authentication.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i16_application_credential_name"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i16_application_credential_name"></a>
###### application_credential_name

- Schema name: `Application Credential Name`
- Type: string
- Default: ""

Swift application credential name for authentication.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i16_application_credential_secret"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i16_application_credential_secret"></a>
###### application_credential_secret

- Schema name: `Application Credential Secret`
- Type: string
- Default: ""

Swift application credential secret for authentication.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i16_auth_version"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i16_auth_version"></a>
###### auth_version (required)

- Schema name: `Auth Version`

Swift authentication API version. `0`: Legacy auth `1`: TempAuth `2`: Keystone v2.0 `3`: Keystone v3 `null`: Auto-detect
<a id="Return_value_anyOf_i2_items_provider_oneOf_i16_auth_version_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i16_auth_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i16_auth_version_anyOf_i0)

- Type: enum (of integer)
###### Must be one of:

- 0
- 1
- 2
- 3

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i16_auth_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i16_auth_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i16_endpoint_type"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i16_endpoint_type"></a>
###### endpoint_type (required)

- Schema name: `Endpoint Type`

Swift endpoint type to use. `public`: Public endpoint (default) `internal`: Internal network endpoint `admin`: Administrative endpoint `null`: Use default
<a id="Return_value_anyOf_i2_items_provider_oneOf_i16_endpoint_type_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i16_endpoint_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i16_endpoint_type_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "public"
- "internal"
- "admin"

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i16_endpoint_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i16_endpoint_type_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i17"></a>
###### [WebDavCredentialsModel](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i17)

- Schema name: `WebDavCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i17_type"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i17_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for WebDAV servers.
- Specific value: `"WEBDAV"`

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i17_url"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i17_url"></a>
###### url (required)

- Schema name: `Url`
- Type: string
- Type: Format: uri

WebDAV server URL endpoint.
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i17_vendor"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i17_vendor"></a>
###### vendor (required)

- Schema name: `Vendor`
- Type: enum (of string)

WebDAV server vendor type for compatibility optimizations. `NEXTCLOUD`: Nextcloud server `OWNCLOUD`: ownCloud server `SHAREPOINT`: Microsoft SharePoint `OTHER`: Generic WebDAV server
###### Must be one of:

- "NEXTCLOUD"
- "OWNCLOUD"
- "SHAREPOINT"
- "OTHER"

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i17_user"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i17_user"></a>
###### user (required)

- Schema name: `User`
- Type: string

WebDAV username for authentication.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i17_pass"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i17_pass"></a>
###### pass (required)

- Schema name: `Pass`
- Type: string

WebDAV password for authentication.

<a id="tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i18"></a>
###### [YandexCredentialsModel](#tab-pane_Return_value_anyOf_i2_items_provider_oneOf_i18)

- Schema name: `YandexCredentialsModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i18_type"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i18_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Cloud provider type identifier for Yandex Disk storage.
- Specific value: `"YANDEX"`

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i18_client_id"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i18_client_id"></a>
###### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

Yandex OAuth application client ID.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i18_client_secret"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i18_client_secret"></a>
###### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

Yandex OAuth application client secret.

<a id="headingReturn_value_anyOf_i2_items_provider_oneOf_i18_token"></a>
<a id="Return_value_anyOf_i2_items_provider_oneOf_i18_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

Yandex OAuth access token for API authentication.
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i3"></a>
##### [CredentialsQueryResultItem](#tab-pane_Return_value_anyOf_i3)

- Schema name: `CredentialsQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i3_id"></a>
<a id="Return_value_anyOf_i3_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the cloud credential.

<a id="headingReturn_value_anyOf_i3_name"></a>
<a id="Return_value_anyOf_i3_name"></a>
###### name

- Schema name: `Name`
- Type: string

Human-readable name for the cloud credential.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i3_provider"></a>
<a id="Return_value_anyOf_i3_provider"></a>
###### provider

- Schema name: `Provider`

Cloud provider configuration including type and authentication details.
<a id="Return_value_anyOf_i3_provider_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_anyOf_i3_provider_oneOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_provider_oneOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_provider_oneOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_provider_oneOf_i1)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_provider_oneOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_anyOf_i3_provider_oneOf_i2)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_provider_oneOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_anyOf_i3_provider_oneOf_i3)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_provider_oneOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_anyOf_i3_provider_oneOf_i4)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_provider_oneOf_i5"></a>
###### [Option 6](#tab-pane_Return_value_anyOf_i3_provider_oneOf_i5)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_provider_oneOf_i6"></a>
###### [Option 7](#tab-pane_Return_value_anyOf_i3_provider_oneOf_i6)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_provider_oneOf_i7"></a>
###### [Option 8](#tab-pane_Return_value_anyOf_i3_provider_oneOf_i7)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_provider_oneOf_i8"></a>
###### [Option 9](#tab-pane_Return_value_anyOf_i3_provider_oneOf_i8)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_provider_oneOf_i9"></a>
###### [Option 10](#tab-pane_Return_value_anyOf_i3_provider_oneOf_i9)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_provider_oneOf_i10"></a>
###### [Option 11](#tab-pane_Return_value_anyOf_i3_provider_oneOf_i10)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_provider_oneOf_i11"></a>
###### [Option 12](#tab-pane_Return_value_anyOf_i3_provider_oneOf_i11)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_provider_oneOf_i12"></a>
###### [Option 13](#tab-pane_Return_value_anyOf_i3_provider_oneOf_i12)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_provider_oneOf_i13"></a>
###### [Option 14](#tab-pane_Return_value_anyOf_i3_provider_oneOf_i13)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_provider_oneOf_i14"></a>
###### [Option 15](#tab-pane_Return_value_anyOf_i3_provider_oneOf_i14)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_provider_oneOf_i15"></a>
###### [Option 16](#tab-pane_Return_value_anyOf_i3_provider_oneOf_i15)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_provider_oneOf_i16"></a>
###### [Option 17](#tab-pane_Return_value_anyOf_i3_provider_oneOf_i16)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_provider_oneOf_i17"></a>
###### [Option 18](#tab-pane_Return_value_anyOf_i3_provider_oneOf_i17)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_provider_oneOf_i18"></a>
###### [Option 19](#tab-pane_Return_value_anyOf_i3_provider_oneOf_i18)

- Type: object

<a id="tab-pane_Return_value_anyOf_i4"></a>
##### [Option 5](#tab-pane_Return_value_anyOf_i4)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
