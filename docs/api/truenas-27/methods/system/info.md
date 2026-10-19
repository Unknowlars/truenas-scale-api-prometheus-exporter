---
title: system.info
kind: method
source_rst: _sources/api_methods_system.info.rst.txt
source_html: api_methods_system.info.html
required_roles:
  - READONLY_ADMIN
---

# system.info

## Summary

Returns basic system information.

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

- Schema name: `SystemInfoResult`
- Type: object

SystemInfoResult return fields.
- No Additional Properties
<a id="headingReturn_value_version"></a>
<a id="Return_value_version"></a>
#### version (required)

- Schema name: `Version`
- Type: string

TrueNAS version.

<a id="headingReturn_value_buildtime"></a>
<a id="Return_value_buildtime"></a>
#### buildtime (required)

- Schema name: `Buildtime`
- Type: string
- Type: Format: date-time

TrueNAS build time.

<a id="headingReturn_value_hostname"></a>
<a id="Return_value_hostname"></a>
#### hostname (required)

- Schema name: `Hostname`
- Type: string

System host name.

<a id="headingReturn_value_physmem"></a>
<a id="Return_value_physmem"></a>
#### physmem (required)

- Schema name: `Physmem`
- Type: integer

System physical memory in bytes.

<a id="headingReturn_value_model"></a>
<a id="Return_value_model"></a>
#### model (required)

- Schema name: `Model`
- Type: string

CPU model.

<a id="headingReturn_value_cores"></a>
<a id="Return_value_cores"></a>
#### cores (required)

- Schema name: `Cores`
- Type: integer

Number of CPU cores.

<a id="headingReturn_value_physical_cores"></a>
<a id="Return_value_physical_cores"></a>
#### physical_cores (required)

- Schema name: `Physical Cores`
- Type: integer

Number of physical CPU cores.

<a id="headingReturn_value_loadavg"></a>
<a id="Return_value_loadavg"></a>
#### loadavg (required)

- Schema name: `Loadavg`
- Type: array

System load averages over 1, 5, and 15 minute periods.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_loadavg_items"></a>
- Type: object

<a id="headingReturn_value_uptime"></a>
<a id="Return_value_uptime"></a>
#### uptime (required)

- Schema name: `Uptime`
- Type: string

Human-readable system uptime string.

<a id="headingReturn_value_uptime_seconds"></a>
<a id="Return_value_uptime_seconds"></a>
#### uptime_seconds (required)

- Schema name: `Uptime Seconds`
- Type: number

System uptime in seconds since boot.

<a id="headingReturn_value_system_serial"></a>
<a id="Return_value_system_serial"></a>
#### system_serial (required)

- Schema name: `System Serial`

System hardware serial number. `null` if not available.
<a id="Return_value_system_serial_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_system_serial_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_system_serial_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_system_serial_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_system_serial_anyOf_i1)

- Type: null

<a id="headingReturn_value_system_product"></a>
<a id="Return_value_system_product"></a>
#### system_product (required)

- Schema name: `System Product`

System product name from hardware manufacturer. `null` if not available.
<a id="Return_value_system_product_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_system_product_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_system_product_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_system_product_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_system_product_anyOf_i1)

- Type: null

<a id="headingReturn_value_system_product_version"></a>
<a id="Return_value_system_product_version"></a>
#### system_product_version (required)

- Schema name: `System Product Version`

System product version from hardware manufacturer. `null` if not available.
<a id="Return_value_system_product_version_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_system_product_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_system_product_version_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_system_product_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_system_product_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_license"></a>
<a id="Return_value_license"></a>
#### license (required)

- Schema name: `License`

System license information. `null` if no license is installed.
<a id="Return_value_license_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_license_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_license_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_license_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_license_anyOf_i1)

- Type: null

<a id="headingReturn_value_boottime"></a>
<a id="Return_value_boottime"></a>
#### boottime (required)

- Schema name: `Boottime`
- Type: string
- Type: Format: date-time

System boot time.

<a id="headingReturn_value_datetime"></a>
<a id="Return_value_datetime"></a>
#### datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Current system date and time.

<a id="headingReturn_value_timezone"></a>
<a id="Return_value_timezone"></a>
#### timezone (required)

- Schema name: `Timezone`
- Type: string

System timezone identifier.

<a id="headingReturn_value_system_manufacturer"></a>
<a id="Return_value_system_manufacturer"></a>
#### system_manufacturer (required)

- Schema name: `System Manufacturer`

System manufacturer name from hardware. `null` if not available.
<a id="Return_value_system_manufacturer_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_system_manufacturer_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_system_manufacturer_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_system_manufacturer_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_system_manufacturer_anyOf_i1)

- Type: null

<a id="headingReturn_value_ecc_memory"></a>
<a id="Return_value_ecc_memory"></a>
#### ecc_memory (required)

- Schema name: `Ecc Memory`
- Type: boolean

Whether the system has ECC (Error Correcting Code) memory.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
