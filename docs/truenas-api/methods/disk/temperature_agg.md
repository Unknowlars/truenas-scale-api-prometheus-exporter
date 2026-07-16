---
title: disk.temperature_agg
kind: method
source_rst: _sources/api_methods_disk.temperature_agg.rst.txt
source_html: api_methods_disk.temperature_agg.html
required_roles:
  - REPORTING_READ
---

# disk.temperature_agg

## Summary

Returns min/max/avg temperature for `names` disks for the last `days` days

## Required Roles

- `REPORTING_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: names

#### names

- Schema name: `names`
- Type: array of string

Array of disk names to retrieve temperature aggregates for.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### Parameter 2: days

#### days

- Schema name: `days`
- Type: integer
- Default: 7

Number of days to aggregate temperature data over.

### Return value

- Schema name: `Result`
- Type: object

Object mapping disk names to their aggregated temperature statistics.
#### Additional Properties

Each additional property must conform to the following schema
- Schema name: `DiskTemperatureAggEntry`
- Type: object
- No Additional Properties
##### min (required)

- Schema name: `Min`

Minimum temperature recorded during the time period or `null`.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: number

####### Option 3

- Type: null

##### max (required)

- Schema name: `Max`

Maximum temperature recorded during the time period or `null`.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: number

####### Option 3

- Type: null

##### avg (required)

- Schema name: `Avg`

Average temperature during the time period or `null`.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: number

####### Option 3

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
