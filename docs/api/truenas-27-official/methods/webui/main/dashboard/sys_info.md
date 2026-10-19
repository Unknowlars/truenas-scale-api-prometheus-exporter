---
title: webui.main.dashboard.sys_info
kind: method
source_rst: _sources/api_methods_webui.main.dashboard.sys_info.rst.txt
source_html: api_methods_webui.main.dashboard.sys_info.html
required_roles:
  - READONLY_ADMIN
---

# webui.main.dashboard.sys_info

## Summary

This endpoint was designed to be exclusively consumed by the webUI. This is what makes up the System Information card on the main dashboard after a user logs in.

## Required Roles

- `READONLY_ADMIN`

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

- Schema name: `SysInfo`
- Type: object

System information for the web UI main dashboard display.
- No Additional Properties
<a id="headingReturn_value_platform"></a>
<a id="Return_value_platform"></a>
#### platform (required)

- Schema name: `Platform`
- Type: string

Platform type (e.g., 'FREENAS', 'TRUENAS-SCALE').
- Must be at least `1` characters long

<a id="headingReturn_value_version"></a>
<a id="Return_value_version"></a>
#### version (required)

- Schema name: `Version`
- Type: string

Software version string.
- Must be at least `1` characters long

<a id="headingReturn_value_license"></a>
<a id="Return_value_license"></a>
#### license (required)

- Schema name: `License`

License information object. `null` if no license is installed.
<a id="Return_value_license_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_license_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_license_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_license_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_license_anyOf_i1)

- Type: null

<a id="headingReturn_value_system_serial"></a>
<a id="Return_value_system_serial"></a>
#### system_serial (required)

- Schema name: `System Serial`
- Type: string

Hardware serial number of the system.

<a id="headingReturn_value_hostname"></a>
<a id="Return_value_hostname"></a>
#### hostname (required)

- Schema name: `Hostname`
- Type: string

System hostname.
- Must be at least `1` characters long

<a id="headingReturn_value_uptime_seconds"></a>
<a id="Return_value_uptime_seconds"></a>
#### uptime_seconds (required)

- Schema name: `Uptime Seconds`
- Type: number

System uptime in seconds since last boot.

<a id="headingReturn_value_datetime"></a>
<a id="Return_value_datetime"></a>
#### datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Current system date and time.

<a id="headingReturn_value_remote_info"></a>
<a id="Return_value_remote_info"></a>
#### remote_info (required)

Information about the remote system in HA configurations. `null` for standalone systems.
<a id="Return_value_remote_info_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_remote_info_anyOf_i0"></a>
###### [RemoteInfo](#tab-pane_Return_value_remote_info_anyOf_i0)

- Schema name: `RemoteInfo`
- Type: object
- No Additional Properties
<a id="headingReturn_value_remote_info_anyOf_i0_platform"></a>
<a id="Return_value_remote_info_anyOf_i0_platform"></a>
###### platform (required)

- Schema name: `Platform`
- Type: string

Platform type (e.g., 'FREENAS', 'TRUENAS-SCALE').
- Must be at least `1` characters long

<a id="headingReturn_value_remote_info_anyOf_i0_version"></a>
<a id="Return_value_remote_info_anyOf_i0_version"></a>
###### version (required)

- Schema name: `Version`
- Type: string

Software version string.
- Must be at least `1` characters long

<a id="headingReturn_value_remote_info_anyOf_i0_license"></a>
<a id="Return_value_remote_info_anyOf_i0_license"></a>
###### license (required)

- Schema name: `License`

License information object. `null` if no license is installed.
<a id="Return_value_remote_info_anyOf_i0_license_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_remote_info_anyOf_i0_license_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_remote_info_anyOf_i0_license_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_remote_info_anyOf_i0_license_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_remote_info_anyOf_i0_license_anyOf_i1)

- Type: null

<a id="headingReturn_value_remote_info_anyOf_i0_system_serial"></a>
<a id="Return_value_remote_info_anyOf_i0_system_serial"></a>
###### system_serial (required)

- Schema name: `System Serial`
- Type: string

Hardware serial number of the system.

<a id="headingReturn_value_remote_info_anyOf_i0_hostname"></a>
<a id="Return_value_remote_info_anyOf_i0_hostname"></a>
###### hostname (required)

- Schema name: `Hostname`
- Type: string

System hostname.
- Must be at least `1` characters long

<a id="headingReturn_value_remote_info_anyOf_i0_uptime_seconds"></a>
<a id="Return_value_remote_info_anyOf_i0_uptime_seconds"></a>
###### uptime_seconds (required)

- Schema name: `Uptime Seconds`
- Type: number

System uptime in seconds since last boot.

<a id="headingReturn_value_remote_info_anyOf_i0_datetime"></a>
<a id="Return_value_remote_info_anyOf_i0_datetime"></a>
###### datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Current system date and time.

<a id="tab-pane_Return_value_remote_info_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_remote_info_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
