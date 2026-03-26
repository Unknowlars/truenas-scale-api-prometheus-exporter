---
title: update.profile_choices
kind: method
source_rst: _sources/api_methods_update.profile_choices.rst.txt
source_html: api_methods_update.profile_choices.html
required_roles:
  - READONLY_ADMIN | SYSTEM_UPDATE_READ
---

# update.profile_choices

## Summary

`profile` choices for configuration update.

## Required Roles

- `READONLY_ADMIN | SYSTEM_UPDATE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Object of available update profiles with their configuration details.
#### Additional Properties

Each additional property must conform to the following schema
- Schema name: `UpdateProfileChoice`
- Type: object
- No Additional Properties
##### name (required)

- Schema name: `Name`
- Type: string

Profile name.

##### footnote (required)

- Schema name: `Footnote`
- Type: string

Profile footnote.

##### description (required)

- Schema name: `Description`
- Type: string

Profile description.

##### available (required)

- Schema name: `Available`
- Type: boolean

Whether profile is available for selection.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
