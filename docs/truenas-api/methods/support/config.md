---
title: support.config
kind: method
source_rst: _sources/api_methods_support.config.rst.txt
source_html: api_methods_support.config.html
required_roles:
  - SUPPORT_READ
---

# support.config

## Required Roles

- `SUPPORT_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `SupportEntry`
- Type: object
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
