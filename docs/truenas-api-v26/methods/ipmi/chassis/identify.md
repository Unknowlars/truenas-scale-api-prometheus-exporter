---
title: ipmi.chassis.identify
kind: method
source_rst: _sources/api_methods_ipmi.chassis.identify.rst.txt
source_html: api_methods_ipmi.chassis.identify.html
required_roles:
  - IPMI_WRITE
---

# ipmi.chassis.identify

## Summary

Toggle the chassis identify light on or off.

On an HA system, set `apply_remote` to `true` to apply the change to the remote controller instead of the local one.

## Required Roles

- `IPMI_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`
- Type: object

Request parameters for IPMI chassis identify operation.
- No Additional Properties
##### verb

- Schema name: `Verb`
- Type: enum (of string)
- Default: "ON"

Action to perform on the chassis identify LED.

##### apply_remote

- Schema name: `Apply Remote`
- Type: boolean
- Default: false

If on an HA system, and this field is set to True, the settings will be sent to the remote controller.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the chassis identify operation completes successfully.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
