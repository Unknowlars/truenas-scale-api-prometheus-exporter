---
title: ipmi.sel.info
kind: method
source_rst: _sources/api_methods_ipmi.sel.info.rst.txt
source_html: api_methods_ipmi.sel.info.html
required_roles:
  - IPMI_READ
---

# ipmi.sel.info

## Summary

Query General information about the IPMI System Event Log

This method is a job.

## Required Roles

- `IPMI_READ`

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

- Schema name: `Result`

SEL information or raw dictionary if parsing fails.
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [IPMISELInfo](#tab-pane_Return_value_anyOf_i0)

- Schema name: `IPMISELInfo`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_sel_version"></a>
<a id="Return_value_anyOf_i0_sel_version"></a>
###### sel_version (required)

- Schema name: `Sel Version`
- Type: string

Version of the SEL (System Event Log) implementation.

<a id="headingReturn_value_anyOf_i0_number_of_log_entries"></a>
<a id="Return_value_anyOf_i0_number_of_log_entries"></a>
###### number_of_log_entries (required)

- Schema name: `Number Of Log Entries`
- Type: string

Total number of entries currently in the SEL.

<a id="headingReturn_value_anyOf_i0_free_space_remaining"></a>
<a id="Return_value_anyOf_i0_free_space_remaining"></a>
###### free_space_remaining (required)

- Schema name: `Free Space Remaining`
- Type: string

Amount of free space remaining in the SEL storage.

<a id="headingReturn_value_anyOf_i0_recent_erase_timestamp"></a>
<a id="Return_value_anyOf_i0_recent_erase_timestamp"></a>
###### recent_erase_timestamp (required)

- Schema name: `Recent Erase Timestamp`
- Type: string

Timestamp of the most recent SEL erase operation.

<a id="headingReturn_value_anyOf_i0_get_sel_allocation_information_command"></a>
<a id="Return_value_anyOf_i0_get_sel_allocation_information_command"></a>
###### get_sel_allocation_information_command (required)

- Schema name: `Get Sel Allocation Information Command`
- Type: string

Support status for the get SEL allocation information command.

<a id="headingReturn_value_anyOf_i0_reserve_sel_command"></a>
<a id="Return_value_anyOf_i0_reserve_sel_command"></a>
###### reserve_sel_command (required)

- Schema name: `Reserve Sel Command`
- Type: string

Support status for the reserve SEL command.

<a id="headingReturn_value_anyOf_i0_partial_add_sel_entry_command"></a>
<a id="Return_value_anyOf_i0_partial_add_sel_entry_command"></a>
###### partial_add_sel_entry_command (required)

- Schema name: `Partial Add Sel Entry Command`
- Type: string

Support status for the partial add SEL entry command.

<a id="headingReturn_value_anyOf_i0_delete_sel_command"></a>
<a id="Return_value_anyOf_i0_delete_sel_command"></a>
###### delete_sel_command (required)

- Schema name: `Delete Sel Command`
- Type: string

Support status for the delete SEL command.

<a id="headingReturn_value_anyOf_i0_events_dropped_due_to_lack_of_space"></a>
<a id="Return_value_anyOf_i0_events_dropped_due_to_lack_of_space"></a>
###### events_dropped_due_to_lack_of_space (required)

- Schema name: `Events Dropped Due To Lack Of Space`
- Type: string

Number of events that were dropped due to insufficient SEL space.

<a id="headingReturn_value_anyOf_i0_number_of_possible_allocation_units"></a>
<a id="Return_value_anyOf_i0_number_of_possible_allocation_units"></a>
###### number_of_possible_allocation_units (required)

- Schema name: `Number Of Possible Allocation Units`
- Type: string

Total number of allocation units that can be used for SEL storage.

<a id="headingReturn_value_anyOf_i0_allocation_unit_size"></a>
<a id="Return_value_anyOf_i0_allocation_unit_size"></a>
###### allocation_unit_size (required)

- Schema name: `Allocation Unit Size`
- Type: string

Size of each allocation unit in bytes.

<a id="headingReturn_value_anyOf_i0_number_of_free_allocation_units"></a>
<a id="Return_value_anyOf_i0_number_of_free_allocation_units"></a>
###### number_of_free_allocation_units (required)

- Schema name: `Number Of Free Allocation Units`
- Type: string

Number of allocation units currently available for use.

<a id="headingReturn_value_anyOf_i0_largest_free_block"></a>
<a id="Return_value_anyOf_i0_largest_free_block"></a>
###### largest_free_block (required)

- Schema name: `Largest Free Block`
- Type: string

Size of the largest contiguous free block in allocation units.

<a id="headingReturn_value_anyOf_i0_maximum_record_size"></a>
<a id="Return_value_anyOf_i0_maximum_record_size"></a>
###### maximum_record_size (required)

- Schema name: `Maximum Record Size`
- Type: string

Maximum size of a single SEL record in bytes.

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [Option 2](#tab-pane_Return_value_anyOf_i1)

- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
