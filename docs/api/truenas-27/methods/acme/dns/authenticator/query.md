---
title: acme.dns.authenticator.query
kind: method
source_rst: _sources/api_methods_acme.dns.authenticator.query.rst.txt
source_html: api_methods_acme.dns.authenticator.query.html
required_roles:
  - NETWORK_INTERFACE_READ
---

# acme.dns.authenticator.query

## Required Roles

- `NETWORK_INTERFACE_READ`

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

- Schema name: `Result`
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items"></a>
###### DNSAuthenticatorQueryResultItem

- Schema name: `DNSAuthenticatorQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_id"></a>
<a id="Return_value_anyOf_i0_items_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the DNS authenticator.

<a id="headingReturn_value_anyOf_i0_items_attributes"></a>
<a id="Return_value_anyOf_i0_items_attributes"></a>
###### attributes

- Schema name: `Attributes`

Authentication credentials and configuration (masked for security).
<a id="Return_value_anyOf_i0_items_attributes_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i0"></a>
###### [CloudFlareSchema](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i0)

- Schema name: `CloudFlareSchema`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i0_authenticator"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i0_authenticator"></a>
###### authenticator (required)

- Schema name: `Authenticator`
- Type: const

DNS authenticator type identifier for Cloudflare.
- Specific value: `"cloudflare"`

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i0_cloudflare_email"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i0_cloudflare_email"></a>
###### cloudflare_email

- Schema name: `Cloudflare Email`
- Default: null

Cloudflare Email.
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i0_cloudflare_email_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i0_cloudflare_email_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i0_cloudflare_email_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i0_cloudflare_email_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i0_cloudflare_email_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i0_api_key"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i0_api_key"></a>
###### api_key

- Schema name: `Api Key`
- Default: null

API Key.
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i0_api_key_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i0_api_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i0_api_key_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i0_api_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i0_api_key_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i0_api_token"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i0_api_token"></a>
###### api_token

- Schema name: `Api Token`
- Default: null

API Token.
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i0_api_token_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i0_api_token_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i0_api_token_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i0_api_token_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i0_api_token_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i1"></a>
###### [DigitalOceanSchema](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i1)

- Schema name: `DigitalOceanSchema`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i1_authenticator"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i1_authenticator"></a>
###### authenticator (required)

- Schema name: `Authenticator`
- Type: const

DNS authenticator type identifier for DigitalOcean.
- Specific value: `"digitalocean"`

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i1_digitalocean_token"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i1_digitalocean_token"></a>
###### digitalocean_token (required)

- Schema name: `Digitalocean Token`
- Type: string

DigitalOcean Token.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i2"></a>
###### [OVHSchema](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i2)

- Schema name: `OVHSchema`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i2_authenticator"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i2_authenticator"></a>
###### authenticator (required)

- Schema name: `Authenticator`
- Type: const

DNS authenticator type identifier for OVH.
- Specific value: `"OVH"`

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i2_application_key"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i2_application_key"></a>
###### application_key (required)

- Schema name: `Application Key`
- Type: string

OVH Application Key.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i2_application_secret"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i2_application_secret"></a>
###### application_secret (required)

- Schema name: `Application Secret`
- Type: string

OVH Application Secret.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i2_consumer_key"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i2_consumer_key"></a>
###### consumer_key (required)

- Schema name: `Consumer Key`
- Type: string

OVH Consumer Key.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i2_endpoint"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i2_endpoint"></a>
###### endpoint (required)

- Schema name: `Endpoint`
- Type: enum (of string)

OVH Endpoint.
###### Must be one of:

- "ovh-eu"
- "ovh-ca"
- "ovh-us"
- "kimsufi-eu"
- "kimsufi-ca"
- "soyoustart-eu"
- "soyoustart-ca"

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i3"></a>
###### [Route53Schema](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i3)

- Schema name: `Route53Schema`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i3_authenticator"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i3_authenticator"></a>
###### authenticator (required)

- Schema name: `Authenticator`
- Type: const

DNS authenticator type identifier for AWS Route 53.
- Specific value: `"route53"`

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i3_access_key_id"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i3_access_key_id"></a>
###### access_key_id (required)

- Schema name: `Access Key Id`
- Type: string

AWS Access Key ID.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i3_secret_access_key"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i3_secret_access_key"></a>
###### secret_access_key (required)

- Schema name: `Secret Access Key`
- Type: string

AWS Secret Access Key.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i4"></a>
###### [ShellSchema](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i4)

- Schema name: `ShellSchema`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i4_authenticator"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i4_authenticator"></a>
###### authenticator (required)

- Schema name: `Authenticator`
- Type: const

DNS authenticator type identifier for custom shell scripts.
- Specific value: `"shell"`

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i4_script"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i4_script"></a>
###### script (required)

- Schema name: `Script`
- Type: string
- Type: Format: file-path

Authentication Script.

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i4_user"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i4_user"></a>
###### user

- Schema name: `User`
- Type: string
- Default: "nobody"

Running user.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i4_timeout"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i4_timeout"></a>
###### timeout

- Schema name: `Timeout`
- Type: integer
- Default: 60

Script Timeout.
- Value must be greater or equal to `5`

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i4_delay"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i4_delay"></a>
###### delay

- Schema name: `Delay`
- Type: integer
- Default: 60

Propagation delay.
- Value must be greater or equal to `10`

<a id="headingReturn_value_anyOf_i0_items_name"></a>
<a id="Return_value_anyOf_i0_items_name"></a>
###### name

- Schema name: `Name`
- Type: string

Human-readable name for the DNS authenticator.

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [DNSAuthenticatorQueryResultItem](#tab-pane_Return_value_anyOf_i1)

- Schema name: `DNSAuthenticatorQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_id"></a>
<a id="Return_value_anyOf_i1_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the DNS authenticator.

<a id="headingReturn_value_anyOf_i1_attributes"></a>
<a id="Return_value_anyOf_i1_attributes"></a>
###### attributes

- Schema name: `Attributes`

Authentication credentials and configuration (masked for security).
<a id="Return_value_anyOf_i1_attributes_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_anyOf_i1_attributes_oneOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_attributes_oneOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_attributes_oneOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_attributes_oneOf_i1)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_attributes_oneOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_anyOf_i1_attributes_oneOf_i2)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_attributes_oneOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_anyOf_i1_attributes_oneOf_i3)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_attributes_oneOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_anyOf_i1_attributes_oneOf_i4)

- Type: object

<a id="headingReturn_value_anyOf_i1_name"></a>
<a id="Return_value_anyOf_i1_name"></a>
###### name

- Schema name: `Name`
- Type: string

Human-readable name for the DNS authenticator.

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../../shared/query_methods.md)
