---
title: alertservice.create
kind: method
source_rst: _sources/api_methods_alertservice.create.rst.txt
source_html: api_methods_alertservice.create.html
required_roles:
  - ALERT_WRITE
---

# alertservice.create

## Summary

Create an Alert Service of specified `type`.

If `enabled`, it sends alerts to the configured `type` of Alert Service.

## Required Roles

- `ALERT_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: alert_service_create

<a id="Call_parameters_items_i0"></a>
#### alert_service_create

- Schema name: `alert_service_create`
- Type: object

Alert service configuration data for the new service.
- No Additional Properties
<a id="headingCall_parameters_items_i0_name"></a>
<a id="Call_parameters_items_i0_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the alert service.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_attributes"></a>
<a id="Call_parameters_items_i0_attributes"></a>
##### attributes (required)

- Schema name: `Attributes`

Service-specific configuration attributes (credentials, endpoints, etc.).
<a id="Call_parameters_items_i0_attributes_oneOf"></a>
###### One of

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i0"></a>
###### [AWSSNSServiceModel](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i0)

- Schema name: `AWSSNSServiceModel`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_attributes_oneOf_i0_type"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i0_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for Amazon SNS.
- Specific value: `"AWSSNS"`

<a id="headingCall_parameters_items_i0_attributes_oneOf_i0_region"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i0_region"></a>
###### region (required)

- Schema name: `Region`
- Type: string

AWS region where the SNS topic is located.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_attributes_oneOf_i0_topic_arn"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i0_topic_arn"></a>
###### topic_arn (required)

- Schema name: `Topic Arn`
- Type: string

Amazon Resource Name (ARN) of the SNS topic to publish alerts to.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_attributes_oneOf_i0_aws_access_key_id"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i0_aws_access_key_id"></a>
###### aws_access_key_id (required)

- Schema name: `Aws Access Key Id`
- Type: string

AWS access key ID for authentication.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_attributes_oneOf_i0_aws_secret_access_key"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i0_aws_secret_access_key"></a>
###### aws_secret_access_key (required)

- Schema name: `Aws Secret Access Key`
- Type: string

AWS secret access key for authentication.
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i1"></a>
###### [InfluxDBServiceModel](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i1)

- Schema name: `InfluxDBServiceModel`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_attributes_oneOf_i1_type"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i1_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for InfluxDB.
- Specific value: `"InfluxDB"`

<a id="headingCall_parameters_items_i0_attributes_oneOf_i1_host"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i1_host"></a>
###### host (required)

- Schema name: `Host`
- Type: string

InfluxDB server hostname or IP address.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_attributes_oneOf_i1_username"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i1_username"></a>
###### username (required)

- Schema name: `Username`
- Type: string

Username for InfluxDB authentication.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_attributes_oneOf_i1_password"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i1_password"></a>
###### password (required)

- Schema name: `Password`
- Type: string

Password for InfluxDB authentication.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_attributes_oneOf_i1_database"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i1_database"></a>
###### database (required)

- Schema name: `Database`
- Type: string

InfluxDB database name to store alert data.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_attributes_oneOf_i1_series_name"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i1_series_name"></a>
###### series_name (required)

- Schema name: `Series Name`
- Type: string

Name of the time series to store alert events.
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i2"></a>
###### [MailServiceModel](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i2)

- Schema name: `MailServiceModel`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_attributes_oneOf_i2_type"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i2_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for email notifications.
- Specific value: `"Mail"`

<a id="headingCall_parameters_items_i0_attributes_oneOf_i2_email"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i2_email"></a>
###### email

- Schema name: `Email`
- Type: string
- Default: ""

Email address to send alerts to. Empty string uses system default.

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i3"></a>
###### [MattermostServiceModel](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i3)

- Schema name: `MattermostServiceModel`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_attributes_oneOf_i3_type"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i3_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for Mattermost.
- Specific value: `"Mattermost"`

<a id="headingCall_parameters_items_i0_attributes_oneOf_i3_url"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i3_url"></a>
###### url (required)

- Schema name: `Url`
- Type: string
- Type: Format: uri

Mattermost webhook URL for posting alerts.
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="headingCall_parameters_items_i0_attributes_oneOf_i3_username"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i3_username"></a>
###### username (required)

- Schema name: `Username`
- Type: string

Username to display when posting alerts to Mattermost.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_attributes_oneOf_i3_channel"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i3_channel"></a>
###### channel

- Schema name: `Channel`
- Type: string
- Default: ""

Mattermost channel name to post alerts to. Empty string uses webhook default.

<a id="headingCall_parameters_items_i0_attributes_oneOf_i3_icon_url"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i3_icon_url"></a>
###### icon_url

- Schema name: `Icon Url`
- Default: ""

URL of icon image to display with alert messages. Empty string uses default.
<a id="Call_parameters_items_i0_attributes_oneOf_i3_icon_url_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i3_icon_url_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i3_icon_url_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i3_icon_url_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i3_icon_url_anyOf_i1)

- Type: string
- Type: Format: uri
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i4"></a>
###### [OpsGenieServiceModel](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i4)

- Schema name: `OpsGenieServiceModel`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_attributes_oneOf_i4_type"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i4_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for OpsGenie.
- Specific value: `"OpsGenie"`

<a id="headingCall_parameters_items_i0_attributes_oneOf_i4_api_key"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i4_api_key"></a>
###### api_key (required)

- Schema name: `Api Key`
- Type: string

OpsGenie API key for authentication.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_attributes_oneOf_i4_api_url"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i4_api_url"></a>
###### api_url

- Schema name: `Api Url`
- Default: ""

OpsGenie API URL. Empty string uses default OpsGenie endpoint.
<a id="Call_parameters_items_i0_attributes_oneOf_i4_api_url_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i4_api_url_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i4_api_url_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i4_api_url_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i4_api_url_anyOf_i1)

- Type: string
- Type: Format: uri
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i5"></a>
###### [PagerDutyServiceModel](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i5)

- Schema name: `PagerDutyServiceModel`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_attributes_oneOf_i5_type"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i5_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for PagerDuty.
- Specific value: `"PagerDuty"`

<a id="headingCall_parameters_items_i0_attributes_oneOf_i5_service_key"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i5_service_key"></a>
###### service_key (required)

- Schema name: `Service Key`
- Type: string

PagerDuty service integration key for sending alerts.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_attributes_oneOf_i5_client_name"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i5_client_name"></a>
###### client_name (required)

- Schema name: `Client Name`
- Type: string

Client name to identify the source of alerts in PagerDuty.
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i6"></a>
###### [SlackServiceModel](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i6)

- Schema name: `SlackServiceModel`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_attributes_oneOf_i6_type"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i6_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for Slack.
- Specific value: `"Slack"`

<a id="headingCall_parameters_items_i0_attributes_oneOf_i6_url"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i6_url"></a>
###### url (required)

- Schema name: `Url`
- Type: string
- Type: Format: uri

Slack webhook URL for posting alert messages.
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i7"></a>
###### [SNMPTrapServiceModel](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i7)

- Schema name: `SNMPTrapServiceModel`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_attributes_oneOf_i7_type"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i7_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for SNMP traps.
- Specific value: `"SNMPTrap"`

<a id="headingCall_parameters_items_i0_attributes_oneOf_i7_host"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i7_host"></a>
###### host (required)

- Schema name: `Host`
- Type: string

SNMP trap receiver hostname or IP address.

<a id="headingCall_parameters_items_i0_attributes_oneOf_i7_port"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i7_port"></a>
###### port (required)

- Schema name: `Port`
- Type: integer

TCP port number for SNMP trap receiver.
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="headingCall_parameters_items_i0_attributes_oneOf_i7_v3"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i7_v3"></a>
###### v3 (required)

- Schema name: `V3`
- Type: boolean

Whether to use SNMP v3 instead of v1/v2c.

<a id="headingCall_parameters_items_i0_attributes_oneOf_i7_community"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i7_community"></a>
###### community

- Schema name: `Community`
- Default: null

SNMP community string for v1/v2c authentication or `null` for v3.
<a id="Call_parameters_items_i0_attributes_oneOf_i7_community_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i7_community_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i7_community_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i7_community_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i7_community_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_attributes_oneOf_i7_v3_username"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i7_v3_username"></a>
###### v3_username

- Schema name: `V3 Username`
- Default: null

SNMP v3 username for authentication or `null` for v1/v2c.
<a id="Call_parameters_items_i0_attributes_oneOf_i7_v3_username_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i7_v3_username_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i7_v3_username_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i7_v3_username_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i7_v3_username_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_attributes_oneOf_i7_v3_authkey"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i7_v3_authkey"></a>
###### v3_authkey

- Schema name: `V3 Authkey`
- Default: ""

SNMP v3 authentication key or `null` if not using authentication.
<a id="Call_parameters_items_i0_attributes_oneOf_i7_v3_authkey_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i7_v3_authkey_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i7_v3_authkey_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i7_v3_authkey_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i7_v3_authkey_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_attributes_oneOf_i7_v3_privkey"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i7_v3_privkey"></a>
###### v3_privkey

- Schema name: `V3 Privkey`
- Default: ""

SNMP v3 privacy key for encryption or `null` if not using privacy.
<a id="Call_parameters_items_i0_attributes_oneOf_i7_v3_privkey_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i7_v3_privkey_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i7_v3_privkey_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i7_v3_privkey_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i7_v3_privkey_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_attributes_oneOf_i7_v3_authprotocol"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i7_v3_authprotocol"></a>
###### v3_authprotocol

- Schema name: `V3 Authprotocol`
- Type: enum (of null or string)
- Default: null

SNMP v3 authentication protocol or `null` for no authentication.
###### Must be one of:

- null
- "MD5"
- "SHA"
- "128SHA224"
- "192SHA256"
- "256SHA384"
- "384SHA512"

<a id="headingCall_parameters_items_i0_attributes_oneOf_i7_v3_privprotocol"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i7_v3_privprotocol"></a>
###### v3_privprotocol

- Schema name: `V3 Privprotocol`
- Type: enum (of null or string)
- Default: null

SNMP v3 privacy protocol for encryption or `null` for no privacy.
###### Must be one of:

- null
- "DES"
- "3DESEDE"
- "AESCFB128"
- "AESCFB192"
- "AESCFB256"
- "AESBLUMENTHALCFB192"
- "AESBLUMENTHALCFB256"

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i8"></a>
###### [TelegramServiceModel](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i8)

- Schema name: `TelegramServiceModel`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_attributes_oneOf_i8_type"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i8_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for Telegram.
- Specific value: `"Telegram"`

<a id="headingCall_parameters_items_i0_attributes_oneOf_i8_bot_token"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i8_bot_token"></a>
###### bot_token (required)

- Schema name: `Bot Token`
- Type: string

Telegram bot token for API authentication.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_attributes_oneOf_i8_chat_ids"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i8_chat_ids"></a>
###### chat_ids (required)

- Schema name: `Chat Ids`
- Type: array of integer

List of Telegram chat IDs to send alerts to (minimum 1 required).
- Must contain a minimum of `1` items
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_attributes_oneOf_i8_chat_ids_items"></a>
- Type: integer

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i9"></a>
###### [VictorOpsServiceModel](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i9)

- Schema name: `VictorOpsServiceModel`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_attributes_oneOf_i9_type"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i9_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for VictorOps (now Splunk On-Call).
- Specific value: `"VictorOps"`

<a id="headingCall_parameters_items_i0_attributes_oneOf_i9_api_key"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i9_api_key"></a>
###### api_key (required)

- Schema name: `Api Key`
- Type: string

VictorOps API key for authentication.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_attributes_oneOf_i9_routing_key"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i9_routing_key"></a>
###### routing_key (required)

- Schema name: `Routing Key`
- Type: string

VictorOps routing key to determine alert destination and escalation policy.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_level"></a>
<a id="Call_parameters_items_i0_level"></a>
##### level (required)

- Schema name: `Level`
- Type: enum (of string)

Minimum alert severity level that triggers notifications through this service.
###### Must be one of:

- "INFO"
- "NOTICE"
- "WARNING"
- "ERROR"
- "CRITICAL"
- "ALERT"
- "EMERGENCY"

<a id="headingCall_parameters_items_i0_enabled"></a>
<a id="Call_parameters_items_i0_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the alert service is active and will send notifications.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `AlertServiceEntry`
- Type: object

The created alert service configuration.
- No Additional Properties
<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the alert service.
- Must be at least `1` characters long

<a id="headingReturn_value_attributes"></a>
<a id="Return_value_attributes"></a>
#### attributes (required)

- Schema name: `Attributes`

Service-specific configuration attributes (credentials, endpoints, etc.).
<a id="Return_value_attributes_oneOf"></a>
##### One of

<a id="tab-pane_Return_value_attributes_oneOf_i0"></a>
###### [AWSSNSServiceModel](#tab-pane_Return_value_attributes_oneOf_i0)

- Schema name: `AWSSNSServiceModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_attributes_oneOf_i0_type"></a>
<a id="Return_value_attributes_oneOf_i0_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for Amazon SNS.
- Specific value: `"AWSSNS"`

<a id="headingReturn_value_attributes_oneOf_i0_region"></a>
<a id="Return_value_attributes_oneOf_i0_region"></a>
###### region (required)

- Schema name: `Region`
- Type: string

AWS region where the SNS topic is located.
- Must be at least `1` characters long

<a id="headingReturn_value_attributes_oneOf_i0_topic_arn"></a>
<a id="Return_value_attributes_oneOf_i0_topic_arn"></a>
###### topic_arn (required)

- Schema name: `Topic Arn`
- Type: string

Amazon Resource Name (ARN) of the SNS topic to publish alerts to.
- Must be at least `1` characters long

<a id="headingReturn_value_attributes_oneOf_i0_aws_access_key_id"></a>
<a id="Return_value_attributes_oneOf_i0_aws_access_key_id"></a>
###### aws_access_key_id (required)

- Schema name: `Aws Access Key Id`
- Type: string

AWS access key ID for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_attributes_oneOf_i0_aws_secret_access_key"></a>
<a id="Return_value_attributes_oneOf_i0_aws_secret_access_key"></a>
###### aws_secret_access_key (required)

- Schema name: `Aws Secret Access Key`
- Type: string

AWS secret access key for authentication.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_attributes_oneOf_i1"></a>
###### [InfluxDBServiceModel](#tab-pane_Return_value_attributes_oneOf_i1)

- Schema name: `InfluxDBServiceModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_attributes_oneOf_i1_type"></a>
<a id="Return_value_attributes_oneOf_i1_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for InfluxDB.
- Specific value: `"InfluxDB"`

<a id="headingReturn_value_attributes_oneOf_i1_host"></a>
<a id="Return_value_attributes_oneOf_i1_host"></a>
###### host (required)

- Schema name: `Host`
- Type: string

InfluxDB server hostname or IP address.
- Must be at least `1` characters long

<a id="headingReturn_value_attributes_oneOf_i1_username"></a>
<a id="Return_value_attributes_oneOf_i1_username"></a>
###### username (required)

- Schema name: `Username`
- Type: string

Username for InfluxDB authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_attributes_oneOf_i1_password"></a>
<a id="Return_value_attributes_oneOf_i1_password"></a>
###### password (required)

- Schema name: `Password`
- Type: string

Password for InfluxDB authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_attributes_oneOf_i1_database"></a>
<a id="Return_value_attributes_oneOf_i1_database"></a>
###### database (required)

- Schema name: `Database`
- Type: string

InfluxDB database name to store alert data.
- Must be at least `1` characters long

<a id="headingReturn_value_attributes_oneOf_i1_series_name"></a>
<a id="Return_value_attributes_oneOf_i1_series_name"></a>
###### series_name (required)

- Schema name: `Series Name`
- Type: string

Name of the time series to store alert events.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_attributes_oneOf_i2"></a>
###### [MailServiceModel](#tab-pane_Return_value_attributes_oneOf_i2)

- Schema name: `MailServiceModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_attributes_oneOf_i2_type"></a>
<a id="Return_value_attributes_oneOf_i2_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for email notifications.
- Specific value: `"Mail"`

<a id="headingReturn_value_attributes_oneOf_i2_email"></a>
<a id="Return_value_attributes_oneOf_i2_email"></a>
###### email

- Schema name: `Email`
- Type: string
- Default: ""

Email address to send alerts to. Empty string uses system default.

<a id="tab-pane_Return_value_attributes_oneOf_i3"></a>
###### [MattermostServiceModel](#tab-pane_Return_value_attributes_oneOf_i3)

- Schema name: `MattermostServiceModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_attributes_oneOf_i3_type"></a>
<a id="Return_value_attributes_oneOf_i3_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for Mattermost.
- Specific value: `"Mattermost"`

<a id="headingReturn_value_attributes_oneOf_i3_url"></a>
<a id="Return_value_attributes_oneOf_i3_url"></a>
###### url (required)

- Schema name: `Url`
- Type: string
- Type: Format: uri

Mattermost webhook URL for posting alerts.
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="headingReturn_value_attributes_oneOf_i3_username"></a>
<a id="Return_value_attributes_oneOf_i3_username"></a>
###### username (required)

- Schema name: `Username`
- Type: string

Username to display when posting alerts to Mattermost.
- Must be at least `1` characters long

<a id="headingReturn_value_attributes_oneOf_i3_channel"></a>
<a id="Return_value_attributes_oneOf_i3_channel"></a>
###### channel

- Schema name: `Channel`
- Type: string
- Default: ""

Mattermost channel name to post alerts to. Empty string uses webhook default.

<a id="headingReturn_value_attributes_oneOf_i3_icon_url"></a>
<a id="Return_value_attributes_oneOf_i3_icon_url"></a>
###### icon_url

- Schema name: `Icon Url`
- Default: ""

URL of icon image to display with alert messages. Empty string uses default.
<a id="Return_value_attributes_oneOf_i3_icon_url_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_attributes_oneOf_i3_icon_url_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_attributes_oneOf_i3_icon_url_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_attributes_oneOf_i3_icon_url_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_attributes_oneOf_i3_icon_url_anyOf_i1)

- Type: string
- Type: Format: uri
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="tab-pane_Return_value_attributes_oneOf_i4"></a>
###### [OpsGenieServiceModel](#tab-pane_Return_value_attributes_oneOf_i4)

- Schema name: `OpsGenieServiceModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_attributes_oneOf_i4_type"></a>
<a id="Return_value_attributes_oneOf_i4_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for OpsGenie.
- Specific value: `"OpsGenie"`

<a id="headingReturn_value_attributes_oneOf_i4_api_key"></a>
<a id="Return_value_attributes_oneOf_i4_api_key"></a>
###### api_key (required)

- Schema name: `Api Key`
- Type: string

OpsGenie API key for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_attributes_oneOf_i4_api_url"></a>
<a id="Return_value_attributes_oneOf_i4_api_url"></a>
###### api_url

- Schema name: `Api Url`
- Default: ""

OpsGenie API URL. Empty string uses default OpsGenie endpoint.
<a id="Return_value_attributes_oneOf_i4_api_url_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_attributes_oneOf_i4_api_url_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_attributes_oneOf_i4_api_url_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_attributes_oneOf_i4_api_url_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_attributes_oneOf_i4_api_url_anyOf_i1)

- Type: string
- Type: Format: uri
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="tab-pane_Return_value_attributes_oneOf_i5"></a>
###### [PagerDutyServiceModel](#tab-pane_Return_value_attributes_oneOf_i5)

- Schema name: `PagerDutyServiceModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_attributes_oneOf_i5_type"></a>
<a id="Return_value_attributes_oneOf_i5_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for PagerDuty.
- Specific value: `"PagerDuty"`

<a id="headingReturn_value_attributes_oneOf_i5_service_key"></a>
<a id="Return_value_attributes_oneOf_i5_service_key"></a>
###### service_key (required)

- Schema name: `Service Key`
- Type: string

PagerDuty service integration key for sending alerts.
- Must be at least `1` characters long

<a id="headingReturn_value_attributes_oneOf_i5_client_name"></a>
<a id="Return_value_attributes_oneOf_i5_client_name"></a>
###### client_name (required)

- Schema name: `Client Name`
- Type: string

Client name to identify the source of alerts in PagerDuty.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_attributes_oneOf_i6"></a>
###### [SlackServiceModel](#tab-pane_Return_value_attributes_oneOf_i6)

- Schema name: `SlackServiceModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_attributes_oneOf_i6_type"></a>
<a id="Return_value_attributes_oneOf_i6_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for Slack.
- Specific value: `"Slack"`

<a id="headingReturn_value_attributes_oneOf_i6_url"></a>
<a id="Return_value_attributes_oneOf_i6_url"></a>
###### url (required)

- Schema name: `Url`
- Type: string
- Type: Format: uri

Slack webhook URL for posting alert messages.
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="tab-pane_Return_value_attributes_oneOf_i7"></a>
###### [SNMPTrapServiceModel](#tab-pane_Return_value_attributes_oneOf_i7)

- Schema name: `SNMPTrapServiceModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_attributes_oneOf_i7_type"></a>
<a id="Return_value_attributes_oneOf_i7_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for SNMP traps.
- Specific value: `"SNMPTrap"`

<a id="headingReturn_value_attributes_oneOf_i7_host"></a>
<a id="Return_value_attributes_oneOf_i7_host"></a>
###### host (required)

- Schema name: `Host`
- Type: string

SNMP trap receiver hostname or IP address.

<a id="headingReturn_value_attributes_oneOf_i7_port"></a>
<a id="Return_value_attributes_oneOf_i7_port"></a>
###### port (required)

- Schema name: `Port`
- Type: integer

TCP port number for SNMP trap receiver.
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="headingReturn_value_attributes_oneOf_i7_v3"></a>
<a id="Return_value_attributes_oneOf_i7_v3"></a>
###### v3 (required)

- Schema name: `V3`
- Type: boolean

Whether to use SNMP v3 instead of v1/v2c.

<a id="headingReturn_value_attributes_oneOf_i7_community"></a>
<a id="Return_value_attributes_oneOf_i7_community"></a>
###### community

- Schema name: `Community`
- Default: null

SNMP community string for v1/v2c authentication or `null` for v3.
<a id="Return_value_attributes_oneOf_i7_community_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_attributes_oneOf_i7_community_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_attributes_oneOf_i7_community_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_attributes_oneOf_i7_community_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_attributes_oneOf_i7_community_anyOf_i1)

- Type: null

<a id="headingReturn_value_attributes_oneOf_i7_v3_username"></a>
<a id="Return_value_attributes_oneOf_i7_v3_username"></a>
###### v3_username

- Schema name: `V3 Username`
- Default: null

SNMP v3 username for authentication or `null` for v1/v2c.
<a id="Return_value_attributes_oneOf_i7_v3_username_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_attributes_oneOf_i7_v3_username_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_attributes_oneOf_i7_v3_username_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_attributes_oneOf_i7_v3_username_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_attributes_oneOf_i7_v3_username_anyOf_i1)

- Type: null

<a id="headingReturn_value_attributes_oneOf_i7_v3_authkey"></a>
<a id="Return_value_attributes_oneOf_i7_v3_authkey"></a>
###### v3_authkey

- Schema name: `V3 Authkey`
- Default: ""

SNMP v3 authentication key or `null` if not using authentication.
<a id="Return_value_attributes_oneOf_i7_v3_authkey_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_attributes_oneOf_i7_v3_authkey_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_attributes_oneOf_i7_v3_authkey_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_attributes_oneOf_i7_v3_authkey_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_attributes_oneOf_i7_v3_authkey_anyOf_i1)

- Type: null

<a id="headingReturn_value_attributes_oneOf_i7_v3_privkey"></a>
<a id="Return_value_attributes_oneOf_i7_v3_privkey"></a>
###### v3_privkey

- Schema name: `V3 Privkey`
- Default: ""

SNMP v3 privacy key for encryption or `null` if not using privacy.
<a id="Return_value_attributes_oneOf_i7_v3_privkey_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_attributes_oneOf_i7_v3_privkey_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_attributes_oneOf_i7_v3_privkey_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_attributes_oneOf_i7_v3_privkey_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_attributes_oneOf_i7_v3_privkey_anyOf_i1)

- Type: null

<a id="headingReturn_value_attributes_oneOf_i7_v3_authprotocol"></a>
<a id="Return_value_attributes_oneOf_i7_v3_authprotocol"></a>
###### v3_authprotocol

- Schema name: `V3 Authprotocol`
- Type: enum (of null or string)
- Default: null

SNMP v3 authentication protocol or `null` for no authentication.
###### Must be one of:

- null
- "MD5"
- "SHA"
- "128SHA224"
- "192SHA256"
- "256SHA384"
- "384SHA512"

<a id="headingReturn_value_attributes_oneOf_i7_v3_privprotocol"></a>
<a id="Return_value_attributes_oneOf_i7_v3_privprotocol"></a>
###### v3_privprotocol

- Schema name: `V3 Privprotocol`
- Type: enum (of null or string)
- Default: null

SNMP v3 privacy protocol for encryption or `null` for no privacy.
###### Must be one of:

- null
- "DES"
- "3DESEDE"
- "AESCFB128"
- "AESCFB192"
- "AESCFB256"
- "AESBLUMENTHALCFB192"
- "AESBLUMENTHALCFB256"

<a id="tab-pane_Return_value_attributes_oneOf_i8"></a>
###### [TelegramServiceModel](#tab-pane_Return_value_attributes_oneOf_i8)

- Schema name: `TelegramServiceModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_attributes_oneOf_i8_type"></a>
<a id="Return_value_attributes_oneOf_i8_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for Telegram.
- Specific value: `"Telegram"`

<a id="headingReturn_value_attributes_oneOf_i8_bot_token"></a>
<a id="Return_value_attributes_oneOf_i8_bot_token"></a>
###### bot_token (required)

- Schema name: `Bot Token`
- Type: string

Telegram bot token for API authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_attributes_oneOf_i8_chat_ids"></a>
<a id="Return_value_attributes_oneOf_i8_chat_ids"></a>
###### chat_ids (required)

- Schema name: `Chat Ids`
- Type: array of integer

List of Telegram chat IDs to send alerts to (minimum 1 required).
- Must contain a minimum of `1` items
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_attributes_oneOf_i8_chat_ids_items"></a>
- Type: integer

<a id="tab-pane_Return_value_attributes_oneOf_i9"></a>
###### [VictorOpsServiceModel](#tab-pane_Return_value_attributes_oneOf_i9)

- Schema name: `VictorOpsServiceModel`
- Type: object
- No Additional Properties
<a id="headingReturn_value_attributes_oneOf_i9_type"></a>
<a id="Return_value_attributes_oneOf_i9_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Alert service type identifier for VictorOps (now Splunk On-Call).
- Specific value: `"VictorOps"`

<a id="headingReturn_value_attributes_oneOf_i9_api_key"></a>
<a id="Return_value_attributes_oneOf_i9_api_key"></a>
###### api_key (required)

- Schema name: `Api Key`
- Type: string

VictorOps API key for authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_attributes_oneOf_i9_routing_key"></a>
<a id="Return_value_attributes_oneOf_i9_routing_key"></a>
###### routing_key (required)

- Schema name: `Routing Key`
- Type: string

VictorOps routing key to determine alert destination and escalation policy.
- Must be at least `1` characters long

<a id="headingReturn_value_level"></a>
<a id="Return_value_level"></a>
#### level (required)

- Schema name: `Level`
- Type: enum (of string)

Minimum alert severity level that triggers notifications through this service.
##### Must be one of:

- "INFO"
- "NOTICE"
- "WARNING"
- "ERROR"
- "CRITICAL"
- "ALERT"
- "EMERGENCY"

<a id="headingReturn_value_enabled"></a>
<a id="Return_value_enabled"></a>
#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the alert service is active and will send notifications.

<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the alert service.

<a id="headingReturn_value_type__title"></a>
<a id="Return_value_type__title"></a>
#### type__title (required)

- Schema name: `Type Title`
- Type: string

Human-readable title for the alert service type.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
