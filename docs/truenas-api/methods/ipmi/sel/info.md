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

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`

SEL information or raw dictionary if parsing fails.
#### Any of

##### IPMISELInfo

- Schema name: `IPMISELInfo`
- Type: object
- No Additional Properties
###### sel_version (required)

- Schema name: `Sel Version`
- Type: string

Version of the SEL (System Event Log) implementation.

###### number_of_log_entries (required)

- Schema name: `Number Of Log Entries`
- Type: string

Total number of entries currently in the SEL.

###### free_space_remaining (required)

- Schema name: `Free Space Remaining`
- Type: string

Amount of free space remaining in the SEL storage.

###### recent_erase_timestamp (required)

- Schema name: `Recent Erase Timestamp`
- Type: string

Timestamp of the most recent SEL erase operation.

###### get_sel_allocation_information_command (required)

- Schema name: `Get Sel Allocation Information Command`
- Type: string

Support status for the get SEL allocation information command.

###### reserve_sel_command (required)

- Schema name: `Reserve Sel Command`
- Type: string

Support status for the reserve SEL command.

###### partial_add_sel_entry_command (required)

- Schema name: `Partial Add Sel Entry Command`
- Type: string

Support status for the partial add SEL entry command.

###### delete_sel_command (required)

- Schema name: `Delete Sel Command`
- Type: string

Support status for the delete SEL command.

###### events_dropped_due_to_lack_of_space (required)

- Schema name: `Events Dropped Due To Lack Of Space`
- Type: string

Number of events that were dropped due to insufficient SEL space.

###### number_of_possible_allocation_units (required)

- Schema name: `Number Of Possible Allocation Units`
- Type: string

Total number of allocation units that can be used for SEL storage.

###### allocation_unit_size (required)

- Schema name: `Allocation Unit Size`
- Type: string

Size of each allocation unit in bytes.

###### number_of_free_allocation_units (required)

- Schema name: `Number Of Free Allocation Units`
- Type: string

Number of allocation units currently available for use.

###### largest_free_block (required)

- Schema name: `Largest Free Block`
- Type: string

Size of the largest contiguous free block in allocation units.

###### maximum_record_size (required)

- Schema name: `Maximum Record Size`
- Type: string

Maximum size of a single SEL record in bytes.

##### Option 2

- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
