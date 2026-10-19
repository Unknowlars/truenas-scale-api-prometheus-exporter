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

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `PoolScanChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_name"></a>
<a id="CHANGED_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

Pool name.

<a id="headingCHANGED_scan"></a>
<a id="CHANGED_scan"></a>
#### scan (required)

- Schema name: `PoolScan`
- Type: object

Scan information.
- No Additional Properties
<a id="headingCHANGED_scan_function"></a>
<a id="CHANGED_scan_function"></a>
##### function (required)

- Schema name: `Function`
- Type: enum (of string)

Type of ZFS pool scan.
###### Must be one of:

- "RESILVER"
- "SCRUB"

<a id="headingCHANGED_scan_state"></a>
<a id="CHANGED_scan_state"></a>
##### state (required)

- Schema name: `State`
- Type: enum (of string)

Current lifecycle state of the scan.
###### Must be one of:

- "SCANNING"
- "FINISHED"
- "CANCELED"

<a id="headingCHANGED_scan_start_time"></a>
<a id="CHANGED_scan_start_time"></a>
##### start_time (required)

- Schema name: `Start Time`
- Type: string
- Type: Format: date-time

Scan start time.

<a id="headingCHANGED_scan_end_time"></a>
<a id="CHANGED_scan_end_time"></a>
##### end_time (required)

- Schema name: `End Time`

Scan end time (`null` while the scan is still running).
<a id="CHANGED_scan_end_time_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_scan_end_time_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_scan_end_time_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_CHANGED_scan_end_time_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_scan_end_time_anyOf_i1)

- Type: null

<a id="headingCHANGED_scan_percentage"></a>
<a id="CHANGED_scan_percentage"></a>
##### percentage (required)

- Schema name: `Percentage`
- Type: number

Scan progress (between 0 and 100%).

<a id="headingCHANGED_scan_bytes_to_process"></a>
<a id="CHANGED_scan_bytes_to_process"></a>
##### bytes_to_process (required)

- Schema name: `Bytes To Process`
- Type: integer

Total bytes located by scanner.

<a id="headingCHANGED_scan_bytes_processed"></a>
<a id="CHANGED_scan_bytes_processed"></a>
##### bytes_processed (required)

- Schema name: `Bytes Processed`
- Type: integer

Total bytes to scan.

<a id="headingCHANGED_scan_bytes_issued"></a>
<a id="CHANGED_scan_bytes_issued"></a>
##### bytes_issued (required)

- Schema name: `Bytes Issued`
- Type: integer

Issued bytes per scan pass.

<a id="headingCHANGED_scan_pause"></a>
<a id="CHANGED_scan_pause"></a>
##### pause (required)

- Schema name: `Pause`

Pause time of a scrub pass (`null` if the scan is not paused).
<a id="CHANGED_scan_pause_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_scan_pause_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_scan_pause_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_CHANGED_scan_pause_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_scan_pause_anyOf_i1)

- Type: null

<a id="headingCHANGED_scan_errors"></a>
<a id="CHANGED_scan_errors"></a>
##### errors (required)

- Schema name: `Errors`
- Type: integer

Number of scan errors.

<a id="headingCHANGED_scan_total_secs_left"></a>
<a id="CHANGED_scan_total_secs_left"></a>
##### total_secs_left (required)

- Schema name: `Total Secs Left`

Number of seconds left (`null` if the scan is not running).
<a id="CHANGED_scan_total_secs_left_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_scan_total_secs_left_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_scan_total_secs_left_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_scan_total_secs_left_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_scan_total_secs_left_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
