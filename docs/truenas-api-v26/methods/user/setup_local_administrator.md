---
title: user.setup_local_administrator
kind: method
source_rst: _sources/api_methods_user.setup_local_administrator.rst.txt
source_html: api_methods_user.setup_local_administrator.html
required_roles:
  []
---

# user.setup_local_administrator

## Summary

Set up local administrator (this method does not require authentication if local administrator is not already set up).

## Required Roles

- None documented.

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: username

#### username

- Schema name: `username`
- Type: enum (of string)

Administrator username to configure.

#### Parameter 2: password

#### password

- Schema name: `password`
- Type: string

Password for the administrator account.

#### Parameter 3: options

#### options

- Schema name: `options`
- Type: object

Additional options for cloud or specialized administrator setup.
- No Additional Properties
##### ec2

- Default: null

Cloud platform-specific options for administrator setup. `null` for standard setup.
###### Any of

####### UserSetupLocalAdministratorEC2Options

- Schema name: `UserSetupLocalAdministratorEC2Options`
- Type: object
- No Additional Properties
######## instance_id (required)

- Schema name: `Instance Id`
- Type: string

EC2 instance identifier for cloud-specific administrator setup.
- Must be at least `1` characters long

####### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful administrator account setup.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
