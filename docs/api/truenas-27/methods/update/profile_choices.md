---
title: update.profile_choices
kind: method
source_rst: _sources/api_methods_update.profile_choices.rst.txt
source_html: api_methods_update.profile_choices.html
required_roles:
  - READONLY_ADMIN
  - SYSTEM_UPDATE_READ
---

# update.profile_choices

## Summary

`profile` choices for configuration update.

## Required Roles

- `READONLY_ADMIN`
- `SYSTEM_UPDATE_READ`

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

Object of available update profiles with their configuration details.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Schema name: `UpdateProfileChoice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_additionalProperties_name"></a>
<a id="Return_value_additionalProperties_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Profile name.

<a id="headingReturn_value_additionalProperties_footnote"></a>
<a id="Return_value_additionalProperties_footnote"></a>
##### footnote (required)

- Schema name: `Footnote`
- Type: string

Profile footnote.

<a id="headingReturn_value_additionalProperties_description"></a>
<a id="Return_value_additionalProperties_description"></a>
##### description (required)

- Schema name: `Description`
- Type: string

Profile description.

<a id="headingReturn_value_additionalProperties_available"></a>
<a id="Return_value_additionalProperties_available"></a>
##### available (required)

- Schema name: `Available`
- Type: boolean

Whether profile is available for selection.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
