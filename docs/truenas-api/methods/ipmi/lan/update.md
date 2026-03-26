---
title: ipmi.lan.update
kind: method
source_rst: _sources/api_methods_ipmi.lan.update.rst.txt
source_html: api_methods_ipmi.lan.update.html
required_roles:
  - IPMI_WRITE
---

# ipmi.lan.update

## Summary

Update IPMI channel configuration

## Required Roles

- `IPMI_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: channel

#### channel

- Schema name: `channel`
- Type: integer

IPMI LAN channel number to update.

#### Parameter 2: data

#### data

- Schema name: `data`

IPMI LAN configuration data (DHCP or static IP).

### Return value

- Schema name: `Result`
- Type: integer

Returns the channel number that was updated.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
