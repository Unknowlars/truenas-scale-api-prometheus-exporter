---
title: support.update
kind: method
source_rst: _sources/api_methods_support.update.rst.txt
source_html: api_methods_support.update.html
required_roles:
  - SUPPORT_WRITE
---

# support.update

## Summary

Update Proactive Support settings.

## Required Roles

- `SUPPORT_WRITE`

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

Updated support configuration data.
- No Additional Properties
##### id

- Schema name: `Id`
- Type: integer

Unique identifier for the support configuration.

##### enabled

- Schema name: `Enabled`

Whether support is enabled. `null` if not available.
###### Any of

####### Option 1

- Type: boolean

####### Option 2

- Type: null

##### name

- Schema name: `Name`
- Type: string

Primary contact name for support.

##### title

- Schema name: `Title`
- Type: string

Primary contact title or role.

##### email

- Schema name: `Email`
- Type: string

Primary contact email address.

##### phone

- Schema name: `Phone`
- Type: string

Primary contact phone number.

##### secondary_name

- Schema name: `Secondary Name`
- Type: string

Secondary contact name for support.

##### secondary_title

- Schema name: `Secondary Title`
- Type: string

Secondary contact title or role.

##### secondary_email

- Schema name: `Secondary Email`
- Type: string

Secondary contact email address.

##### secondary_phone

- Schema name: `Secondary Phone`
- Type: string

Secondary contact phone number.

### Return value

- Schema name: `SupportEntry`
- Type: object

The updated support configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the support configuration.

#### enabled (required)

- Schema name: `Enabled`

Whether support is enabled. `null` if not available.
##### Any of

###### Option 1

- Type: boolean

###### Option 2

- Type: null

#### name (required)

- Schema name: `Name`
- Type: string

Primary contact name for support.

#### title (required)

- Schema name: `Title`
- Type: string

Primary contact title or role.

#### email (required)

- Schema name: `Email`
- Type: string

Primary contact email address.

#### phone (required)

- Schema name: `Phone`
- Type: string

Primary contact phone number.

#### secondary_name (required)

- Schema name: `Secondary Name`
- Type: string

Secondary contact name for support.

#### secondary_title (required)

- Schema name: `Secondary Title`
- Type: string

Secondary contact title or role.

#### secondary_email (required)

- Schema name: `Secondary Email`
- Type: string

Secondary contact email address.

#### secondary_phone (required)

- Schema name: `Secondary Phone`
- Type: string

Secondary contact phone number.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
