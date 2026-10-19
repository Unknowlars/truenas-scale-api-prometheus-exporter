---
title: system.general.config
kind: method
source_rst: _sources/api_methods_system.general.config.rst.txt
source_html: api_methods_system.general.config.html
required_roles:
  - SYSTEM_GENERAL_READ
---

# system.general.config

## Required Roles

- `SYSTEM_GENERAL_READ`

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

- Schema name: `SystemGeneralEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the system general configuration.

<a id="headingReturn_value_ui_certificate"></a>
<a id="Return_value_ui_certificate"></a>
#### ui_certificate (required)

- Schema name: `Ui Certificate`

Used to enable HTTPS access to the system. If `ui_certificate` is not configured on boot, it is automatically created by the system.
<a id="Return_value_ui_certificate_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_ui_certificate_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_ui_certificate_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_ui_certificate_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_ui_certificate_anyOf_i1)

- Type: null

<a id="headingReturn_value_ui_httpsport"></a>
<a id="Return_value_ui_httpsport"></a>
#### ui_httpsport (required)

- Schema name: `Ui Httpsport`
- Type: integer

HTTPS port for the web UI.
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="headingReturn_value_ui_httpsredirect"></a>
<a id="Return_value_ui_httpsredirect"></a>
#### ui_httpsredirect (required)

- Schema name: `Ui Httpsredirect`
- Type: boolean

When set, makes sure that all HTTP requests are converted to HTTPS requests to better enhance security.

<a id="headingReturn_value_ui_httpsprotocols"></a>
<a id="Return_value_ui_httpsprotocols"></a>
#### ui_httpsprotocols (required)

- Schema name: `Ui Httpsprotocols`
- Type: array of enum (of string)

Array of TLS protocol versions enabled for HTTPS connections.
- All items must be unique
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_ui_httpsprotocols_items"></a>
- Type: enum (of string)
###### Must be one of:

- "TLSv1"
- "TLSv1.1"
- "TLSv1.2"
- "TLSv1.3"

<a id="headingReturn_value_ui_port"></a>
<a id="Return_value_ui_port"></a>
#### ui_port (required)

- Schema name: `Ui Port`
- Type: integer

HTTP port for the web UI.
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="headingReturn_value_ui_address"></a>
<a id="Return_value_ui_address"></a>
#### ui_address (required)

- Schema name: `Ui Address`
- Type: array of string

A list of valid IPv4 addresses which the system will listen on.
- Must contain a minimum of `1` items
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_ui_address_items"></a>
- Type: string

<a id="headingReturn_value_ui_v6address"></a>
<a id="Return_value_ui_v6address"></a>
#### ui_v6address (required)

- Schema name: `Ui V6Address`
- Type: array of string

A list of valid IPv6 addresses which the system will listen on.
- Must contain a minimum of `1` items
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_ui_v6address_items"></a>
- Type: string

<a id="headingReturn_value_ui_allowlist"></a>
<a id="Return_value_ui_allowlist"></a>
#### ui_allowlist (required)

- Schema name: `Ui Allowlist`
- Type: array of string

A list of IP addresses and networks that are allow to use API and UI. If this list is empty, then all IP addresses are allowed to use API and UI.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_ui_allowlist_items"></a>
- Type: string

<a id="headingReturn_value_ui_consolemsg"></a>
<a id="Return_value_ui_consolemsg"></a>
#### ui_consolemsg (required)

- Schema name: `Ui Consolemsg`
- Type: boolean

Whether to show console messages on the web UI.

<a id="headingReturn_value_ui_x_frame_options"></a>
<a id="Return_value_ui_x_frame_options"></a>
#### ui_x_frame_options (required)

- Schema name: `Ui X Frame Options`
- Type: enum (of string)

X-Frame-Options header policy for web UI security.
##### Must be one of:

- "SAMEORIGIN"
- "DENY"
- "ALLOW_ALL"

<a id="headingReturn_value_kbdmap"></a>
<a id="Return_value_kbdmap"></a>
#### kbdmap (required)

- Schema name: `Kbdmap`
- Type: string

System keyboard layout mapping.

<a id="headingReturn_value_timezone"></a>
<a id="Return_value_timezone"></a>
#### timezone (required)

- Schema name: `Timezone`
- Type: string

System timezone identifier.
- Must be at least `1` characters long

<a id="headingReturn_value_usage_collection"></a>
<a id="Return_value_usage_collection"></a>
#### usage_collection (required)

- Schema name: `Usage Collection`

Whether usage data collection is enabled. `null` if not set.
<a id="Return_value_usage_collection_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_usage_collection_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_usage_collection_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_usage_collection_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_usage_collection_anyOf_i1)

- Type: null

<a id="headingReturn_value_wizardshown"></a>
<a id="Return_value_wizardshown"></a>
#### wizardshown (required)

- Schema name: `Wizardshown`
- Type: boolean

Whether the initial setup wizard has been shown.

<a id="headingReturn_value_usage_collection_is_set"></a>
<a id="Return_value_usage_collection_is_set"></a>
#### usage_collection_is_set (required)

- Schema name: `Usage Collection Is Set`
- Type: boolean

Whether the usage collection preference has been explicitly set.

<a id="headingReturn_value_ds_auth"></a>
<a id="Return_value_ds_auth"></a>
#### ds_auth (required)

- Schema name: `Ds Auth`
- Type: boolean

Controls whether configured Directory Service users that are granted with Privileges are allowed to log in to the Web UI or use TrueNAS API.

<a id="headingReturn_value_ui_certificate_name"></a>
<a id="Return_value_ui_certificate_name"></a>
#### ui_certificate_name (required)

- Schema name: `Ui Certificate Name`

Name of the certificate used for HTTPS access. `null` if no certificate is configured.
<a id="Return_value_ui_certificate_name_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_ui_certificate_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_ui_certificate_name_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_ui_certificate_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_ui_certificate_name_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
