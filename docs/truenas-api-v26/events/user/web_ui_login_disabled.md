---
title: user.web_ui_login_disabled
kind: event
source_rst: _sources/api_events_user.web_ui_login_disabled.rst.txt
source_html: api_events_user.web_ui_login_disabled.html
required_roles:
  - FULL_ADMIN
---

# user.web_ui_login_disabled

## Summary

Sent when root user login to the Web UI is disabled.

## Required Roles

- `FULL_ADMIN`

## Schema

- Type: object

### ADDED

- Schema name: `UserWebUiLoginDisabledAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: null

Always `null`.

#### fields (required)

- Schema name: `UserWebUiLoginDisabledAddedEventFields`
- Type: object

Event data.
- No Additional Properties
##### usernames (required)

- Schema name: `Usernames`
- Type: array of string

Local administrator accounts that can be used instead.
- No Additional Items

###### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
