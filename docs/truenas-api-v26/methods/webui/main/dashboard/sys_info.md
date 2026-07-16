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

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `SysInfo`
- Type: object

System information for the web UI main dashboard display.
- No Additional Properties
#### platform (required)

- Schema name: `Platform`
- Type: string

Platform type (e.g., 'FREENAS', 'TRUENAS-SCALE').
- Must be at least `1` characters long

#### version (required)

- Schema name: `Version`
- Type: string

Software version string.
- Must be at least `1` characters long

#### license (required)

- Schema name: `License`

License information object. `null` if no license is installed.
##### Any of

###### Option 1

- Type: object

###### Option 2

- Type: null

#### system_serial (required)

- Schema name: `System Serial`
- Type: string

Hardware serial number of the system.

#### hostname (required)

- Schema name: `Hostname`
- Type: string

System hostname.
- Must be at least `1` characters long

#### uptime_seconds (required)

- Schema name: `Uptime Seconds`
- Type: number

System uptime in seconds since last boot.

#### datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Current system date and time.

#### remote_info (required)

Information about the remote system in HA configurations. `null` for standalone systems.
##### Any of

###### RemoteInfo

- Schema name: `RemoteInfo`
- Type: object
- No Additional Properties
####### platform (required)

- Schema name: `Platform`
- Type: string

Platform type (e.g., 'FREENAS', 'TRUENAS-SCALE').
- Must be at least `1` characters long

####### version (required)

- Schema name: `Version`
- Type: string

Software version string.
- Must be at least `1` characters long

####### license (required)

- Schema name: `License`

License information object. `null` if no license is installed.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### system_serial (required)

- Schema name: `System Serial`
- Type: string

Hardware serial number of the system.

####### hostname (required)

- Schema name: `Hostname`
- Type: string

System hostname.
- Must be at least `1` characters long

####### uptime_seconds (required)

- Schema name: `Uptime Seconds`
- Type: number

System uptime in seconds since last boot.

####### datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Current system date and time.

###### Option 2

- Type: object

###### Option 1

- Type: null

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
