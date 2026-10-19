---
title: system.general.country_choices
kind: method
source_rst: _sources/api_methods_system.general.country_choices.rst.txt
source_html: api_methods_system.general.country_choices.html
required_roles:
  - READONLY_ADMIN
  - SYSTEM_GENERAL_READ
---

# system.general.country_choices

## Summary

Return a dictionary whose keys represent the ISO 3166-1 alpha 2 country code and values represent the English short name (used in ISO 3166/MA)

## Required Roles

- `READONLY_ADMIN`
- `SYSTEM_GENERAL_READ`

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
- Type: object

Object of country codes and their names.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
