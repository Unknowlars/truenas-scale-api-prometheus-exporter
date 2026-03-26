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

###### ACMEDNSAuthenticatorQueryResultItem

- Schema name: `ACMEDNSAuthenticatorQueryResultItem`
- Type: object
- No Additional Properties
####### id

- Schema name: `Id`
- Type: integer

Unique identifier for the DNS authenticator.

####### attributes

- Schema name: `Attributes`

Authentication credentials and configuration (masked for security).

####### name

- Schema name: `Name`
- Type: string

Human-readable name for the DNS authenticator.

##### ACMEDNSAuthenticatorQueryResultItem

- Schema name: `CloudFlareSchema`
- Type: object
- No Additional Properties
###### authenticator (required)

- Schema name: `Authenticator`
- Type: const

DNS authenticator type identifier for Cloudflare.

###### cloudflare_email

- Schema name: `Cloudflare Email`
- Default: null

Cloudflare Email.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

###### api_key

- Schema name: `Api Key`
- Default: null

API Key.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

###### api_token

- Schema name: `Api Token`
- Default: null

API Token.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

##### Option 3

- Type: string
- Must be at least `1` characters long

##### CloudFlareSchema

- Type: null

##### DigitalOceanSchema

- Type: string
- Must be at least `1` characters long

##### OVHSchema

- Type: null

##### Route53Schema

- Type: string
- Must be at least `1` characters long

##### ShellSchema

- Type: null

##### Option 1

- Schema name: `DigitalOceanSchema`
- Type: object
- No Additional Properties
###### authenticator (required)

- Schema name: `Authenticator`
- Type: const

DNS authenticator type identifier for DigitalOcean.

###### digitalocean_token (required)

- Schema name: `Digitalocean Token`
- Type: string

DigitalOcean Token.
- Must be at least `1` characters long

##### Option 2

- Schema name: `OVHSchema`
- Type: object
- No Additional Properties
###### authenticator (required)

- Schema name: `Authenticator`
- Type: const

DNS authenticator type identifier for OVH.

###### application_key (required)

- Schema name: `Application Key`
- Type: string

OVH Application Key.
- Must be at least `1` characters long

###### application_secret (required)

- Schema name: `Application Secret`
- Type: string

OVH Application Secret.
- Must be at least `1` characters long

###### consumer_key (required)

- Schema name: `Consumer Key`
- Type: string

OVH Consumer Key.
- Must be at least `1` characters long

###### endpoint (required)

- Schema name: `Endpoint`
- Type: enum (of string)

OVH Endpoint.

##### Option 1

- Schema name: `Route53Schema`
- Type: object
- No Additional Properties
###### authenticator (required)

- Schema name: `Authenticator`
- Type: const

DNS authenticator type identifier for AWS Route 53.

###### access_key_id (required)

- Schema name: `Access Key Id`
- Type: string

AWS Access Key ID.
- Must be at least `1` characters long

###### secret_access_key (required)

- Schema name: `Secret Access Key`
- Type: string

AWS Secret Access Key.
- Must be at least `1` characters long

##### Option 2

- Schema name: `ShellSchema`
- Type: object
- No Additional Properties
###### authenticator (required)

- Schema name: `Authenticator`
- Type: const

DNS authenticator type identifier for custom shell scripts.

###### script (required)

- Schema name: `Script`
- Type: string
- Type: Format: file-path

Authentication Script.

###### user

- Schema name: `User`
- Type: string
- Default: "nobody"

Running user.
- Must be at least `1` characters long

###### timeout

- Schema name: `Timeout`
- Type: integer
- Default: 60

Script Timeout.
- Value must be greater or equal to `5`

###### delay

- Schema name: `Delay`
- Type: integer
- Default: 60

Propagation delay.
- Value must be greater or equal to `10`

##### Option 1

- Schema name: `ACMEDNSAuthenticatorQueryResultItem`
- Type: object
- No Additional Properties
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the DNS authenticator.

###### attributes

- Schema name: `Attributes`

Authentication credentials and configuration (masked for security).

###### name

- Schema name: `Name`
- Type: string

Human-readable name for the DNS authenticator.

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

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../../shared/query_methods.md)
