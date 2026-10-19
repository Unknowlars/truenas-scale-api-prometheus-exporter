---
title: disk.temperatures
kind: method
source_rst: _sources/api_methods_disk.temperatures.rst.txt
source_html: api_methods_disk.temperatures.html
required_roles:
  - REPORTING_READ
---

# disk.temperatures

## Summary

Returns disk temperatures for disks in degrees celsius.

.. note::

Disk temperatures are not retrieved more than once every 5 minutes.

## Required Roles

- `REPORTING_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: name

<a id="Call_parameters_items_i0"></a>
#### name

- Schema name: `name`
- Type: array of string

List of names of disks to retrieve temperature information. Name should be in the form of "sda", "nvme0n1", etc.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i0_items"></a>
- Type: string

#### Parameter 2: include_thresholds

<a id="Call_parameters_items_i1"></a>
#### include_thresholds

- Schema name: `include_thresholds`
- Type: boolean
- Default: false

Include the temperature thresholds as reported by the disk (i.e. the critical temp).

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: object

Object mapping disk names to their current temperature information.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
