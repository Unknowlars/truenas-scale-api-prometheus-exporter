---
title: api_key.my_keys
kind: method
source_rst: _sources/api_methods_api_key.my_keys.rst.txt
source_html: api_methods_api_key.my_keys.html
required_roles:
  - API_KEY_READ
  - READONLY_ADMIN
---

# api_key.my_keys

## Summary

Get the existing API keys for the currently authenticated user.

## Required Roles

- `API_KEY_READ`
- `READONLY_ADMIN`

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
- Type: array of object

Array of API keys owned by the current authenticated user.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### ApiKeyEntry

- Schema name: `ApiKeyEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_id"></a>
<a id="Return_value_items_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the API key.

<a id="headingReturn_value_items_name"></a>
<a id="Return_value_items_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the API key.
- Must be at least `1` characters long
- Must be at most `200` characters long

<a id="headingReturn_value_items_username"></a>
<a id="Return_value_items_username"></a>
##### username (required)

- Schema name: `Username`

Username associated with the API key or `null` for system keys.
<a id="Return_value_items_username_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_username_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_username_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_username_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_username_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_items_username_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_username_anyOf_i2)

- Type: null

<a id="headingReturn_value_items_user_identifier"></a>
<a id="Return_value_items_user_identifier"></a>
##### user_identifier (required)

- Schema name: `User Identifier`

User ID (numeric) or SID (string) that owns this API key.
<a id="Return_value_items_user_identifier_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_user_identifier_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_user_identifier_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_user_identifier_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_user_identifier_anyOf_i1)

- Type: string

<a id="headingReturn_value_items_iterations"></a>
<a id="Return_value_items_iterations"></a>
##### iterations (required)

- Schema name: `Iterations`
- Type: integer

Number of iterations of PBKDF2-SHA512.

<a id="headingReturn_value_items_salt"></a>
<a id="Return_value_items_salt"></a>
##### salt (required)

- Schema name: `Salt`
- Type: string

Base64 encoded salt for API key.

<a id="headingReturn_value_items_stored_key"></a>
<a id="Return_value_items_stored_key"></a>
##### stored_key (required)

- Schema name: `Stored Key`
- Type: string

SCRAM StoredKey for API key.

<a id="headingReturn_value_items_server_key"></a>
<a id="Return_value_items_server_key"></a>
##### server_key (required)

- Schema name: `Server Key`
- Type: string

SCRAM ServerKey for API key.

<a id="headingReturn_value_items_created_at"></a>
<a id="Return_value_items_created_at"></a>
##### created_at (required)

- Schema name: `Created At`
- Type: string
- Type: Format: date-time

Timestamp when the API key was created.

<a id="headingReturn_value_items_expires_at"></a>
<a id="Return_value_items_expires_at"></a>
##### expires_at

- Schema name: `Expires At`
- Default: null

Expiration timestamp for the API key or `null` for no expiration.
<a id="Return_value_items_expires_at_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_expires_at_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_expires_at_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_Return_value_items_expires_at_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_expires_at_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_local"></a>
<a id="Return_value_items_local"></a>
##### local (required)

- Schema name: `Local`
- Type: boolean

Whether the API key belongs to a local user account rather than a directory services one.

<a id="headingReturn_value_items_revoked"></a>
<a id="Return_value_items_revoked"></a>
##### revoked (required)

- Schema name: `Revoked`
- Type: boolean

Whether the API key has been revoked and is no longer valid.

<a id="headingReturn_value_items_revoked_reason"></a>
<a id="Return_value_items_revoked_reason"></a>
##### revoked_reason (required)

- Schema name: `Revoked Reason`

Reason for API key revocation or `null` if not revoked.
<a id="Return_value_items_revoked_reason_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_revoked_reason_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_revoked_reason_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_revoked_reason_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_revoked_reason_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
