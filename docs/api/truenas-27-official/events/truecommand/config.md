---
title: truecommand.config
kind: event
source_rst: _sources/api_events_truecommand.config.rst.txt
source_html: api_events_truecommand.config.html
required_roles:
  - READONLY_ADMIN
---

# truecommand.config

## Summary

Sent on TrueCommand configuration changes.

## Required Roles

- `READONLY_ADMIN`

## Schema

- Type: object

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `TruecommandConfigChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `TruecommandConfigChangedEventFields`
- Type: object

Event fields.
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the TrueCommand configuration.

<a id="headingCHANGED_fields_status"></a>
<a id="CHANGED_fields_status"></a>
##### status (required)

- Schema name: `Status`
- Type: enum (of string)

Current connection status with TrueCommand service.
###### Must be one of:

- "CONNECTED"
- "CONNECTING"
- "DISABLED"
- "FAILED"

<a id="headingCHANGED_fields_status_reason"></a>
<a id="CHANGED_fields_status_reason"></a>
##### status_reason (required)

- Schema name: `Status Reason`
- Type: enum (of string)

Explanation of the current TrueCommand connection status.
###### Must be one of:

- "Truecommand service is connected."
- "Pending Confirmation From iX Portal for Truecommand API Key."
- "Truecommand service is disabled."
- "Truecommand API Key Disabled by iX Portal."
- "Waiting for connection from Truecommand."
- "Truecommand service is disabled on standby controller"

<a id="headingCHANGED_fields_remote_url"></a>
<a id="CHANGED_fields_remote_url"></a>
##### remote_url (required)

- Schema name: `Remote Url`

URL of the connected TrueCommand instance. `null` if not connected.
<a id="CHANGED_fields_remote_url_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_remote_url_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_remote_url_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_remote_url_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_remote_url_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_remote_ip_address"></a>
<a id="CHANGED_fields_remote_ip_address"></a>
##### remote_ip_address (required)

- Schema name: `Remote Ip Address`

IP address of the connected TrueCommand instance. `null` if not connected.
<a id="CHANGED_fields_remote_ip_address_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_remote_ip_address_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_remote_ip_address_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_remote_ip_address_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_remote_ip_address_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_enabled"></a>
<a id="CHANGED_fields_enabled"></a>
##### enabled (required)

- Schema name: `Enabled`
- Type: boolean

Whether TrueCommand integration is enabled.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
