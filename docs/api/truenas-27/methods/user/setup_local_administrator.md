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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: username

<a id="Call_parameters_items_i0"></a>
#### username

- Schema name: `username`
- Type: enum (of string)

Administrator username to configure.
##### Must be one of:

- "root"
- "truenas_admin"

#### Parameter 2: password

<a id="Call_parameters_items_i1"></a>
#### password

- Schema name: `password`
- Type: string

Password for the administrator account.

#### Parameter 3: options

<a id="Call_parameters_items_i2"></a>
#### options

- Schema name: `options`
- Type: object

Additional options for cloud or specialized administrator setup.
- No Additional Properties
<a id="headingCall_parameters_items_i2_ec2"></a>
<a id="Call_parameters_items_i2_ec2"></a>
##### ec2

- Default: null

Cloud platform-specific options for administrator setup. `null` for standard setup.
<a id="Call_parameters_items_i2_ec2_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i2_ec2_anyOf_i0"></a>
###### [UserSetupLocalAdministratorEC2Options](#tab-pane_Call_parameters_items_i2_ec2_anyOf_i0)

- Schema name: `UserSetupLocalAdministratorEC2Options`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i2_ec2_anyOf_i0_instance_id"></a>
<a id="Call_parameters_items_i2_ec2_anyOf_i0_instance_id"></a>
###### instance_id (required)

- Schema name: `Instance Id`
- Type: string

EC2 instance identifier for cloud-specific administrator setup.
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i2_ec2_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i2_ec2_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful administrator account setup.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
