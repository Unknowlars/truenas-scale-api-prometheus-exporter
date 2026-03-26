---
title: system.general.update
kind: method
source_rst: _sources/api_methods_system.general.update.rst.txt
source_html: api_methods_system.general.update.html
required_roles:
  - SYSTEM_GENERAL_WRITE
---

# system.general.update

## Summary

Update System General Service Configuration.

UI configuration is not applied automatically. Call `system.general.ui_restart` to apply new UI settings (all HTTP connections will be aborted) or specify `ui_restart_delay` (in seconds) to automatically apply them after some small amount of time necessary you might need to receive the response for your settings update request.

If incorrect UI configuration is applied, you might loss API connectivity and won't be able to fix the settings. To avoid that, specify `rollback_timeout` (in seconds). It will automatically roll back UI configuration to the previously working settings after `rollback_timeout` passes unless you call `system.general.checkin` in case the new settings were correct and no rollback is necessary.

## Required Roles

- `SYSTEM_GENERAL_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: general_settings

#### general_settings

- Schema name: `general_settings`
- Type: object

SystemGeneralUpdateArgs parameters.
- No Additional Properties
##### ui_certificate

- Schema name: `Ui Certificate`

Used to enable HTTPS access to the system. If `ui_certificate` is not configured on boot, it is automatically created by the system.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### ui_httpsport

- Schema name: `Ui Httpsport`
- Type: integer

HTTPS port for the web UI.
- Value must be greater or equal to `1` and lesser or equal to `65535`

##### ui_httpsredirect

- Schema name: `Ui Httpsredirect`
- Type: boolean

When set, makes sure that all HTTP requests are converted to HTTPS requests to better enhance security.

##### ui_httpsprotocols

- Schema name: `Ui Httpsprotocols`
- Type: array of enum (of string)

Array of TLS protocol versions enabled for HTTPS connections.
- All items must be unique
- No Additional Items

###### Each item of this array must be:

- Type: enum (of string)

##### ui_port

- Schema name: `Ui Port`
- Type: integer

HTTP port for the web UI.
- Value must be greater or equal to `1` and lesser or equal to `65535`

##### ui_address

- Schema name: `Ui Address`
- Type: array of string

A list of valid IPv4 addresses which the system will listen on.
- Must contain a minimum of `1` items
- No Additional Items

###### Each item of this array must be:

- Type: string

##### ui_v6address

- Schema name: `Ui V6Address`
- Type: array of string

A list of valid IPv6 addresses which the system will listen on.
- Must contain a minimum of `1` items
- No Additional Items

###### Each item of this array must be:

- Type: string

##### ui_allowlist

- Schema name: `Ui Allowlist`
- Type: array of string

A list of IP addresses and networks that are allow to use API and UI. If this list is empty, then all IP addresses are allowed to use API and UI.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### ui_consolemsg

- Schema name: `Ui Consolemsg`
- Type: boolean

Whether to show console messages on the web UI.

##### ui_x_frame_options

- Schema name: `Ui X Frame Options`
- Type: enum (of string)

X-Frame-Options header policy for web UI security.

##### kbdmap

- Schema name: `Kbdmap`
- Type: string

System keyboard layout mapping.

##### timezone

- Schema name: `Timezone`
- Type: string

System timezone identifier.
- Must be at least `1` characters long

##### usage_collection

- Schema name: `Usage Collection`

Whether usage data collection is enabled. `null` if not set.
###### Any of

####### Option 1

- Type: boolean

####### Option 2

- Type: null

##### ds_auth

- Schema name: `Ds Auth`
- Type: boolean

Controls whether configured Directory Service users that are granted with Privileges are allowed to log in to the Web UI or use TrueNAS API.

##### ui_restart_delay

- Schema name: `Ui Restart Delay`

Delay in seconds before restarting the UI after configuration changes. `null` to use default.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### rollback_timeout

- Schema name: `Rollback Timeout`

Timeout in seconds for automatic rollback of UI changes. `null` for no timeout.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

### Return value

- Schema name: `SystemGeneralEntry`
- Type: object

The updated system general configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the system general configuration.

#### ui_certificate (required)

- Schema name: `Ui Certificate`

Used to enable HTTPS access to the system. If `ui_certificate` is not configured on boot, it is automatically created by the system.
##### Any of

###### Option 1

- Type: object

###### Option 2

- Type: null

#### ui_httpsport (required)

- Schema name: `Ui Httpsport`
- Type: integer

HTTPS port for the web UI.
- Value must be greater or equal to `1` and lesser or equal to `65535`

#### ui_httpsredirect (required)

- Schema name: `Ui Httpsredirect`
- Type: boolean

When set, makes sure that all HTTP requests are converted to HTTPS requests to better enhance security.

#### ui_httpsprotocols (required)

- Schema name: `Ui Httpsprotocols`
- Type: array of enum (of string)

Array of TLS protocol versions enabled for HTTPS connections.
- All items must be unique
- No Additional Items

##### Each item of this array must be:

- Type: enum (of string)

#### ui_port (required)

- Schema name: `Ui Port`
- Type: integer

HTTP port for the web UI.
- Value must be greater or equal to `1` and lesser or equal to `65535`

#### ui_address (required)

- Schema name: `Ui Address`
- Type: array of string

A list of valid IPv4 addresses which the system will listen on.
- Must contain a minimum of `1` items
- No Additional Items

##### Each item of this array must be:

- Type: string

#### ui_v6address (required)

- Schema name: `Ui V6Address`
- Type: array of string

A list of valid IPv6 addresses which the system will listen on.
- Must contain a minimum of `1` items
- No Additional Items

##### Each item of this array must be:

- Type: string

#### ui_allowlist (required)

- Schema name: `Ui Allowlist`
- Type: array of string

A list of IP addresses and networks that are allow to use API and UI. If this list is empty, then all IP addresses are allowed to use API and UI.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### ui_consolemsg (required)

- Schema name: `Ui Consolemsg`
- Type: boolean

Whether to show console messages on the web UI.

#### ui_x_frame_options (required)

- Schema name: `Ui X Frame Options`
- Type: enum (of string)

X-Frame-Options header policy for web UI security.

#### kbdmap (required)

- Schema name: `Kbdmap`
- Type: string

System keyboard layout mapping.

#### timezone (required)

- Schema name: `Timezone`
- Type: string

System timezone identifier.
- Must be at least `1` characters long

#### usage_collection (required)

- Schema name: `Usage Collection`

Whether usage data collection is enabled. `null` if not set.
##### Any of

###### Option 1

- Type: boolean

###### Option 2

- Type: null

#### wizardshown (required)

- Schema name: `Wizardshown`
- Type: boolean

Whether the initial setup wizard has been shown.

#### usage_collection_is_set (required)

- Schema name: `Usage Collection Is Set`
- Type: boolean

Whether the usage collection preference has been explicitly set.

#### ds_auth (required)

- Schema name: `Ds Auth`
- Type: boolean

Controls whether configured Directory Service users that are granted with Privileges are allowed to log in to the Web UI or use TrueNAS API.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
