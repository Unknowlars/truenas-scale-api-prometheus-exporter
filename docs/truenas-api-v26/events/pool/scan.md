---
title: pool.scan
kind: event
source_rst: _sources/api_events_pool.scan.rst.txt
source_html: api_events_pool.scan.html
required_roles:
  - POOL_SCRUB_READ
---

# pool.scan

## Summary

Progress of pool resilver/scrub.

## Required Roles

- `POOL_SCRUB_READ`

## Schema

- Type: object

### CHANGED

- Schema name: `PoolScanChangedEvent`
- Type: object
- No Additional Properties
#### name (required)

- Schema name: `Name`
- Type: string

Pool name.

#### scan (required)

- Schema name: `PoolScan`
- Type: object

Scan information.
- No Additional Properties
##### function (required)

- Schema name: `Function`
- Type: enum (of string)

Type of ZFS pool scan.

##### state (required)

- Schema name: `State`
- Type: enum (of string)

Current lifecycle state of the scan.

##### start_time (required)

- Schema name: `Start Time`
- Type: string
- Type: Format: date-time

Scan start time.

##### end_time (required)

- Schema name: `End Time`

Scan end time (`null` while the scan is still running).
###### Any of

####### Option 1

- Type: string
- Type: Format: date-time

####### Option 2

- Type: null

##### percentage (required)

- Schema name: `Percentage`
- Type: number

Scan progress (between 0 and 100%).

##### bytes_to_process (required)

- Schema name: `Bytes To Process`
- Type: integer

Total bytes located by scanner.

##### bytes_processed (required)

- Schema name: `Bytes Processed`
- Type: integer

Total bytes to scan.

##### bytes_issued (required)

- Schema name: `Bytes Issued`
- Type: integer

Issued bytes per scan pass.

##### pause (required)

- Schema name: `Pause`

Pause time of a scrub pass (`null` if the scan is not paused).
###### Any of

####### Option 1

- Type: string
- Type: Format: date-time

####### Option 2

- Type: null

##### errors (required)

- Schema name: `Errors`
- Type: integer

Number of scan errors.

##### total_secs_left (required)

- Schema name: `Total Secs Left`

Number of seconds left (`null` if the scan is not running).
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
