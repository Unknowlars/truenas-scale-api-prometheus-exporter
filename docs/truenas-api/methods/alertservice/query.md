---
title: alertservice.query
kind: method
source_rst: _sources/api_methods_alertservice.query.rst.txt
source_html: api_methods_alertservice.query.html
required_roles:
  - ALERT_READ
---

# alertservice.query

## Required Roles

- `ALERT_READ`

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

###### AlertServiceQueryResultItem

- Schema name: `AlertServiceQueryResultItem`
- Type: object
- No Additional Properties
####### name

- Schema name: `Name`
- Type: string

Human-readable name for the alert service.
- Must be at least `1` characters long

####### attributes

- Schema name: `Attributes`

Service-specific configuration attributes (credentials, endpoints, etc.).

####### level

- Schema name: `Level`
- Type: enum (of string)

Minimum alert severity level that triggers notifications through this service.

####### enabled

- Schema name: `Enabled`
- Type: boolean

Whether the alert service is active and will send notifications.

####### id

- Schema name: `Id`
- Type: integer

Unique identifier for the alert service.

####### type__title

- Schema name: `Type Title`
- Type: string

Human-readable title for the alert service type.

##### AlertServiceQueryResultItem

- Schema name: `AWSSNSServiceModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for Amazon SNS.

###### region (required)

- Schema name: `Region`
- Type: string

AWS region where the SNS topic is located.
- Must be at least `1` characters long

###### topic_arn (required)

- Schema name: `Topic Arn`
- Type: string

Amazon Resource Name (ARN) of the SNS topic to publish alerts to.
- Must be at least `1` characters long

###### aws_access_key_id (required)

- Schema name: `Aws Access Key Id`
- Type: string

AWS access key ID for authentication.
- Must be at least `1` characters long

###### aws_secret_access_key (required)

- Schema name: `Aws Secret Access Key`
- Type: string

AWS secret access key for authentication.
- Must be at least `1` characters long

##### Option 3

- Schema name: `InfluxDBServiceModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for InfluxDB.

###### host (required)

- Schema name: `Host`
- Type: string

InfluxDB server hostname or IP address.
- Must be at least `1` characters long

###### username (required)

- Schema name: `Username`
- Type: string

Username for InfluxDB authentication.
- Must be at least `1` characters long

###### password (required)

- Schema name: `Password`
- Type: string

Password for InfluxDB authentication.
- Must be at least `1` characters long

###### database (required)

- Schema name: `Database`
- Type: string

InfluxDB database name to store alert data.
- Must be at least `1` characters long

###### series_name (required)

- Schema name: `Series Name`
- Type: string

Name of the time series to store alert events.
- Must be at least `1` characters long

##### AWSSNSServiceModel

- Schema name: `MailServiceModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for email notifications.

###### email

- Schema name: `Email`
- Type: string
- Default: ""

Email address to send alerts to. Empty string uses system default.

##### InfluxDBServiceModel

- Schema name: `MattermostServiceModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for Mattermost.

###### url (required)

- Schema name: `Url`
- Type: string
- Type: Format: uri

Mattermost webhook URL for posting alerts.
- Must be at least `1` characters long
- Must be at most `2083` characters long

###### username (required)

- Schema name: `Username`
- Type: string

Username to display when posting alerts to Mattermost.
- Must be at least `1` characters long

###### channel

- Schema name: `Channel`
- Type: string
- Default: ""

Mattermost channel name to post alerts to. Empty string uses webhook default.

###### icon_url

- Schema name: `Icon Url`
- Default: ""

URL of icon image to display with alert messages. Empty string uses default.
####### Any of

######## Option 1

- Type: const

######## Option 2

- Type: string
- Type: Format: uri
- Must be at least `1` characters long
- Must be at most `2083` characters long

##### MailServiceModel

- Type: const

##### MattermostServiceModel

- Type: string
- Type: Format: uri
- Must be at least `1` characters long
- Must be at most `2083` characters long

##### OpsGenieServiceModel

- Schema name: `OpsGenieServiceModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for OpsGenie.

###### api_key (required)

- Schema name: `Api Key`
- Type: string

OpsGenie API key for authentication.
- Must be at least `1` characters long

###### api_url

- Schema name: `Api Url`
- Default: ""

OpsGenie API URL. Empty string uses default OpsGenie endpoint.
####### Any of

######## Option 1

- Type: const

######## Option 2

- Type: string
- Type: Format: uri
- Must be at least `1` characters long
- Must be at most `2083` characters long

##### PagerDutyServiceModel

- Type: const

##### SlackServiceModel

- Type: string
- Type: Format: uri
- Must be at least `1` characters long
- Must be at most `2083` characters long

##### SNMPTrapServiceModel

- Schema name: `PagerDutyServiceModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for PagerDuty.

###### service_key (required)

- Schema name: `Service Key`
- Type: string

PagerDuty service integration key for sending alerts.
- Must be at least `1` characters long

###### client_name (required)

- Schema name: `Client Name`
- Type: string

Client name to identify the source of alerts in PagerDuty.
- Must be at least `1` characters long

##### TelegramServiceModel

- Schema name: `SlackServiceModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for Slack.

###### url (required)

- Schema name: `Url`
- Type: string
- Type: Format: uri

Slack webhook URL for posting alert messages.
- Must be at least `1` characters long
- Must be at most `2083` characters long

##### VictorOpsServiceModel

- Schema name: `SNMPTrapServiceModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for SNMP traps.

###### host (required)

- Schema name: `Host`
- Type: string

SNMP trap receiver hostname or IP address.

###### port (required)

- Schema name: `Port`
- Type: integer

TCP port number for SNMP trap receiver.
- Value must be greater or equal to `1` and lesser or equal to `65535`

###### v3 (required)

- Schema name: `V3`
- Type: boolean

Whether to use SNMP v3 instead of v1/v2c.

###### community

- Schema name: `Community`
- Default: null

SNMP community string for v1/v2c authentication or `null` for v3.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

###### v3_username

- Schema name: `V3 Username`
- Default: null

SNMP v3 username for authentication or `null` for v1/v2c.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

###### v3_authkey

- Schema name: `V3 Authkey`
- Default: null

SNMP v3 authentication key or `null` if not using authentication.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

###### v3_privkey

- Schema name: `V3 Privkey`
- Default: null

SNMP v3 privacy key for encryption or `null` if not using privacy.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

###### v3_authprotocol

- Schema name: `V3 Authprotocol`
- Type: enum (of null or string)
- Default: null

SNMP v3 authentication protocol or `null` for no authentication.

###### v3_privprotocol

- Schema name: `V3 Privprotocol`
- Type: enum (of null or string)
- Default: null

SNMP v3 privacy protocol for encryption or `null` for no privacy.

##### Option 1

- Type: string
- Must be at least `1` characters long

##### Option 2

- Type: null

##### Option 1

- Type: string
- Must be at least `1` characters long

##### Option 2

- Type: null

##### Option 1

- Type: string
- Must be at least `1` characters long

##### Option 2

- Type: null

##### Option 1

- Type: string
- Must be at least `1` characters long

##### Option 2

- Type: null

##### Option 1

- Schema name: `TelegramServiceModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for Telegram.

###### bot_token (required)

- Schema name: `Bot Token`
- Type: string

Telegram bot token for API authentication.
- Must be at least `1` characters long

###### chat_ids (required)

- Schema name: `Chat Ids`
- Type: array of integer

List of Telegram chat IDs to send alerts to (minimum 1 required).
- Must contain a minimum of `1` items
- No Additional Items

####### Each item of this array must be:

- Type: integer

##### Option 2

- Schema name: `VictorOpsServiceModel`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for VictorOps (now Splunk On-Call).

###### api_key (required)

- Schema name: `Api Key`
- Type: string

VictorOps API key for authentication.
- Must be at least `1` characters long

###### routing_key (required)

- Schema name: `Routing Key`
- Type: string

VictorOps routing key to determine alert destination and escalation policy.
- Must be at least `1` characters long

##### Option 1

- Schema name: `AlertServiceQueryResultItem`
- Type: object
- No Additional Properties
###### name

- Schema name: `Name`
- Type: string

Human-readable name for the alert service.
- Must be at least `1` characters long

###### attributes

- Schema name: `Attributes`

Service-specific configuration attributes (credentials, endpoints, etc.).

###### level

- Schema name: `Level`
- Type: enum (of string)

Minimum alert severity level that triggers notifications through this service.

###### enabled

- Schema name: `Enabled`
- Type: boolean

Whether the alert service is active and will send notifications.

###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the alert service.

###### type__title

- Schema name: `Type Title`
- Type: string

Human-readable title for the alert service type.

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

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
