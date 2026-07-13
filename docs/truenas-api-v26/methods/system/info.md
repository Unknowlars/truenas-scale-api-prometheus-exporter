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

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `SystemInfoResult`
- Type: object

SystemInfoResult return fields.
- No Additional Properties
#### version (required)

- Schema name: `Version`
- Type: string

TrueNAS version.

#### buildtime (required)

- Schema name: `Buildtime`
- Type: string
- Type: Format: date-time

TrueNAS build time.

#### hostname (required)

- Schema name: `Hostname`
- Type: string

System host name.

#### physmem (required)

- Schema name: `Physmem`
- Type: integer

System physical memory in bytes.

#### model (required)

- Schema name: `Model`
- Type: string

CPU model.

#### cores (required)

- Schema name: `Cores`
- Type: integer

Number of CPU cores.

#### physical_cores (required)

- Schema name: `Physical Cores`
- Type: integer

Number of physical CPU cores.

#### loadavg (required)

- Schema name: `Loadavg`
- Type: array

System load averages over 1, 5, and 15 minute periods.
- No Additional Items

##### Each item of this array must be:

- Type: object

#### uptime (required)

- Schema name: `Uptime`
- Type: string

Human-readable system uptime string.

#### uptime_seconds (required)

- Schema name: `Uptime Seconds`
- Type: number

System uptime in seconds since boot.

#### system_serial (required)

- Schema name: `System Serial`

System hardware serial number. `null` if not available.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### system_product (required)

- Schema name: `System Product`

System product name from hardware manufacturer. `null` if not available.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### system_product_version (required)

- Schema name: `System Product Version`

System product version from hardware manufacturer. `null` if not available.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### license (required)

- Schema name: `License`

System license information. `null` if no license is installed.
##### Any of

###### Option 1

- Type: object

###### Option 2

- Type: null

#### boottime (required)

- Schema name: `Boottime`
- Type: string
- Type: Format: date-time

System boot time.

#### datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Current system date and time.

#### timezone (required)

- Schema name: `Timezone`
- Type: string

System timezone identifier.

#### system_manufacturer (required)

- Schema name: `System Manufacturer`

System manufacturer name from hardware. `null` if not available.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### ecc_memory (required)

- Schema name: `Ecc Memory`
- Type: boolean

Whether the system has ECC (Error Correcting Code) memory.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
