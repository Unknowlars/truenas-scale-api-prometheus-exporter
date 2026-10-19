---
title: tn_connect.config
kind: method
source_rst: _sources/api_methods_tn_connect.config.rst.txt
source_html: api_methods_tn_connect.config.html
required_roles:
  - TRUENAS_CONNECT_READ
---

# tn_connect.config

## Required Roles

- `TRUENAS_CONNECT_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `TrueNASConnectEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the TrueNAS Connect configuration.

<a id="headingReturn_value_enabled"></a>
<a id="Return_value_enabled"></a>
#### enabled (required)

- Schema name: `Enabled`
- Type: boolean

Whether TrueNAS Connect service is enabled.

<a id="headingReturn_value_registration_details"></a>
<a id="Return_value_registration_details"></a>
#### registration_details (required)

- Schema name: `Registration Details`
- Type: object

Object containing registration information and credentials for TrueNAS Connect.

<a id="headingReturn_value_status"></a>
<a id="Return_value_status"></a>
#### status (required)

- Schema name: `Status`
- Type: string

Current operational status of the TrueNAS Connect service.
- Must be at least `1` characters long

<a id="headingReturn_value_status_reason"></a>
<a id="Return_value_status_reason"></a>
#### status_reason (required)

- Schema name: `Status Reason`
- Type: string

Detailed explanation of the current status, including any error conditions.
- Must be at least `1` characters long

<a id="headingReturn_value_certificate"></a>
<a id="Return_value_certificate"></a>
#### certificate (required)

- Schema name: `Certificate`

ID of the SSL certificate used for TrueNAS Connect communications. `null` if using default.
<a id="Return_value_certificate_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_certificate_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_certificate_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_certificate_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_certificate_anyOf_i1)

- Type: null

<a id="headingReturn_value_account_service_base_url"></a>
<a id="Return_value_account_service_base_url"></a>
#### account_service_base_url (required)

- Schema name: `Account Service Base Url`
- Type: string

Base URL for the TrueNAS Connect account service API.

<a id="headingReturn_value_leca_service_base_url"></a>
<a id="Return_value_leca_service_base_url"></a>
#### leca_service_base_url (required)

- Schema name: `Leca Service Base Url`
- Type: string

Base URL for the Let's Encrypt Certificate Authority service used by TrueNAS Connect.

<a id="headingReturn_value_tnc_base_url"></a>
<a id="Return_value_tnc_base_url"></a>
#### tnc_base_url (required)

- Schema name: `Tnc Base Url`
- Type: string

Base URL for the TrueNAS Connect service.

<a id="headingReturn_value_heartbeat_url"></a>
<a id="Return_value_heartbeat_url"></a>
#### heartbeat_url (required)

- Schema name: `Heartbeat Url`
- Type: string

URL endpoint for sending heartbeat signals to maintain connection status.

<a id="headingReturn_value_tier"></a>
<a id="Return_value_tier"></a>
#### tier (required)

- Schema name: `Tier`

TrueNAS Connect tier.
<a id="Return_value_tier_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_tier_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_tier_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "FOUNDATION"
- "PLUS"
- "BUSINESS"

<a id="tab-pane_Return_value_tier_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_tier_anyOf_i1)

- Type: null

<a id="headingReturn_value_last_heartbeat_failure_datetime"></a>
<a id="Return_value_last_heartbeat_failure_datetime"></a>
#### last_heartbeat_failure_datetime (required)

- Schema name: `Last Heartbeat Failure Datetime`

Datetime of when the current heartbeat failure streak began. Null if heartbeat is not currently failing.
<a id="Return_value_last_heartbeat_failure_datetime_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_last_heartbeat_failure_datetime_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_last_heartbeat_failure_datetime_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_last_heartbeat_failure_datetime_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_last_heartbeat_failure_datetime_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
