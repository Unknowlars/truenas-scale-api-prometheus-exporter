---
title: keychaincredential.get_instance
kind: method
source_rst: _sources/api_methods_keychaincredential.get_instance.rst.txt
source_html: api_methods_keychaincredential.get_instance.html
required_roles:
  - KEYCHAIN_CREDENTIAL_READ
---

# keychaincredential.get_instance

## Summary

Returns instance matching `id`. If `id` is not found, Validation error is raised.

Please see `query` method documentation for `options`.

## Required Roles

- `KEYCHAIN_CREDENTIAL_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Query options customize the results returned by a query method. More complete documentation with examples are covered in the "Query methods" section of the TrueNAS API documentation.
- No Additional Properties
<a id="headingCall_parameters_items_i1_extra"></a>
<a id="Call_parameters_items_i1_extra"></a>
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

<a id="headingCall_parameters_items_i1_order_by"></a>
<a id="Call_parameters_items_i1_order_by"></a>
##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_order_by_items"></a>
- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

<a id="headingCall_parameters_items_i1_select"></a>
<a id="Call_parameters_items_i1_select"></a>
##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items"></a>
<a id="Call_parameters_items_i1_select_items_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i1)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items_anyOf_i1_items"></a>
- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

<a id="headingCall_parameters_items_i1_count"></a>
<a id="Call_parameters_items_i1_count"></a>
##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

<a id="headingCall_parameters_items_i1_get"></a>
<a id="Call_parameters_items_i1_get"></a>
##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

<a id="headingCall_parameters_items_i1_offset"></a>
<a id="Call_parameters_items_i1_offset"></a>
##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0`

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0` and lesser or equal to `10000`

<a id="headingCall_parameters_items_i1_force_sql_filters"></a>
<a id="Call_parameters_items_i1_force_sql_filters"></a>
##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `KeychainCredentialEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this keychain credential.

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

Distinguishes this Keychain Credential from others.
- Must be at least `1` characters long

<a id="headingReturn_value_type"></a>
<a id="Return_value_type"></a>
#### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of credential stored in the keychain. `SSH_KEY_PAIR`: SSH public/private key pair `SSH_CREDENTIALS`: SSH connection credentials including host and authentication
##### Must be one of:

- "SSH_KEY_PAIR"
- "SSH_CREDENTIALS"

<a id="headingReturn_value_attributes"></a>
<a id="Return_value_attributes"></a>
#### attributes (required)

- Schema name: `Attributes`

Credential-specific configuration and authentication data.
<a id="Return_value_attributes_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_attributes_anyOf_i0"></a>
###### [SSHKeyPair](#tab-pane_Return_value_attributes_anyOf_i0)

- Schema name: `SSHKeyPair`
- Type: object

At least one of the two keys must be provided on creation.
- No Additional Properties
<a id="headingReturn_value_attributes_anyOf_i0_private_key"></a>
<a id="Return_value_attributes_anyOf_i0_private_key"></a>
###### private_key

- Schema name: `Private Key`
- Default: null

SSH private key in OpenSSH format. `null` if only public key is provided.
<a id="Return_value_attributes_anyOf_i0_private_key_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_attributes_anyOf_i0_private_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_attributes_anyOf_i0_private_key_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_attributes_anyOf_i0_private_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_attributes_anyOf_i0_private_key_anyOf_i1)

- Type: null

<a id="headingReturn_value_attributes_anyOf_i0_public_key"></a>
<a id="Return_value_attributes_anyOf_i0_public_key"></a>
###### public_key

- Schema name: `Public Key`
- Default: null

Can be omitted and automatically derived from the private key.
<a id="Return_value_attributes_anyOf_i0_public_key_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_attributes_anyOf_i0_public_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_attributes_anyOf_i0_public_key_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_attributes_anyOf_i0_public_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_attributes_anyOf_i0_public_key_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_attributes_anyOf_i1"></a>
###### [SSHCredentials](#tab-pane_Return_value_attributes_anyOf_i1)

- Schema name: `SSHCredentials`
- Type: object
- No Additional Properties
<a id="headingReturn_value_attributes_anyOf_i1_host"></a>
<a id="Return_value_attributes_anyOf_i1_host"></a>
###### host (required)

- Schema name: `Host`
- Type: string

SSH server hostname or IP address.

<a id="headingReturn_value_attributes_anyOf_i1_port"></a>
<a id="Return_value_attributes_anyOf_i1_port"></a>
###### port

- Schema name: `Port`
- Type: integer
- Default: 22

SSH server port number.

<a id="headingReturn_value_attributes_anyOf_i1_username"></a>
<a id="Return_value_attributes_anyOf_i1_username"></a>
###### username

- Schema name: `Username`
- Type: string
- Default: "root"

SSH username for authentication.

<a id="headingReturn_value_attributes_anyOf_i1_private_key"></a>
<a id="Return_value_attributes_anyOf_i1_private_key"></a>
###### private_key (required)

- Schema name: `Private Key`
- Type: integer

Keychain Credential ID.

<a id="headingReturn_value_attributes_anyOf_i1_remote_host_key"></a>
<a id="Return_value_attributes_anyOf_i1_remote_host_key"></a>
###### remote_host_key (required)

- Schema name: `Remote Host Key`
- Type: string

Can be discovered with keychaincredential.remote*ssh*host*key*scan.

<a id="headingReturn_value_attributes_anyOf_i1_connect_timeout"></a>
<a id="Return_value_attributes_anyOf_i1_connect_timeout"></a>
###### connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

Connection timeout in seconds for SSH connections.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
