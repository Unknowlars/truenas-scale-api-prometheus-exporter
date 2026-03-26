---
title: truecommand.config
kind: method
source_rst: _sources/api_methods_truecommand.config.rst.txt
source_html: api_methods_truecommand.config.html
required_roles:
  - TRUECOMMAND_READ
---

# truecommand.config

## Required Roles

- `TRUECOMMAND_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `TruecommandEntry`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the TrueCommand configuration.

#### api_key (required)

- Schema name: `Api Key`

API key for authenticating with TrueCommand services. `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### status (required)

- Schema name: `Status`
- Type: enum (of string)

Current connection status with TrueCommand service.

#### status_reason (required)

- Schema name: `Status Reason`
- Type: enum (of string)

Explanation of the current TrueCommand connection status.

#### remote_url (required)

- Schema name: `Remote Url`

URL of the connected TrueCommand instance. `null` if not connected.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### remote_ip_address (required)

- Schema name: `Remote Ip Address`

IP address of the connected TrueCommand instance. `null` if not connected.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### enabled (required)

- Schema name: `Enabled`
- Type: boolean

Whether TrueCommand integration is enabled.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
