---
title: api_key.query
kind: event
source_rst: _sources/api_events_api_key.query.rst.txt
source_html: api_events_api_key.query.html
required_roles:
  - API_KEY_READ
---

# api_key.query

## Summary

Sent on api_key changes.

## Required Roles

- `API_KEY_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `ApiKeyAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `ApiKeyEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the API key.

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the API key.
- Must be at least `1` characters long
- Must be at most `200` characters long

<a id="headingADDED_fields_username"></a>
<a id="ADDED_fields_username"></a>
##### username (required)

- Schema name: `Username`

Username associated with the API key or `null` for system keys.
<a id="ADDED_fields_username_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_username_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_username_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_username_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_username_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_username_anyOf_i2"></a>
###### [Option 3](#tab-pane_ADDED_fields_username_anyOf_i2)

- Type: null

<a id="headingADDED_fields_user_identifier"></a>
<a id="ADDED_fields_user_identifier"></a>
##### user_identifier (required)

- Schema name: `User Identifier`

User ID (numeric) or SID (string) that owns this API key.
<a id="ADDED_fields_user_identifier_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_user_identifier_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_user_identifier_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_user_identifier_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_user_identifier_anyOf_i1)

- Type: string

<a id="headingADDED_fields_iterations"></a>
<a id="ADDED_fields_iterations"></a>
##### iterations (required)

- Schema name: `Iterations`
- Type: integer

Number of iterations of PBKDF2-SHA512.

<a id="headingADDED_fields_salt"></a>
<a id="ADDED_fields_salt"></a>
##### salt (required)

- Schema name: `Salt`
- Type: string

Base64 encoded salt for API key.

<a id="headingADDED_fields_stored_key"></a>
<a id="ADDED_fields_stored_key"></a>
##### stored_key (required)

- Schema name: `Stored Key`
- Type: string

SCRAM StoredKey for API key.

<a id="headingADDED_fields_server_key"></a>
<a id="ADDED_fields_server_key"></a>
##### server_key (required)

- Schema name: `Server Key`
- Type: string

SCRAM ServerKey for API key.

<a id="headingADDED_fields_created_at"></a>
<a id="ADDED_fields_created_at"></a>
##### created_at (required)

- Schema name: `Created At`
- Type: string
- Type: Format: date-time

Timestamp when the API key was created.

<a id="headingADDED_fields_expires_at"></a>
<a id="ADDED_fields_expires_at"></a>
##### expires_at

- Schema name: `Expires At`
- Default: null

Expiration timestamp for the API key or `null` for no expiration.
<a id="ADDED_fields_expires_at_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_expires_at_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_expires_at_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_ADDED_fields_expires_at_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_expires_at_anyOf_i1)

- Type: null

<a id="headingADDED_fields_local"></a>
<a id="ADDED_fields_local"></a>
##### local (required)

- Schema name: `Local`
- Type: boolean

Whether the API key belongs to a local user account rather than a directory services one.

<a id="headingADDED_fields_revoked"></a>
<a id="ADDED_fields_revoked"></a>
##### revoked (required)

- Schema name: `Revoked`
- Type: boolean

Whether the API key has been revoked and is no longer valid.

<a id="headingADDED_fields_revoked_reason"></a>
<a id="ADDED_fields_revoked_reason"></a>
##### revoked_reason (required)

- Schema name: `Revoked Reason`

Reason for API key revocation or `null` if not revoked.
<a id="ADDED_fields_revoked_reason_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_revoked_reason_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_revoked_reason_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_revoked_reason_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_revoked_reason_anyOf_i1)

- Type: null

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `ApiKeyChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `ApiKeyEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the API key.

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the API key.
- Must be at least `1` characters long
- Must be at most `200` characters long

<a id="headingCHANGED_fields_username"></a>
<a id="CHANGED_fields_username"></a>
##### username (required)

- Schema name: `Username`

Username associated with the API key or `null` for system keys.
<a id="CHANGED_fields_username_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_username_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_username_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_username_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_username_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_username_anyOf_i2"></a>
###### [Option 3](#tab-pane_CHANGED_fields_username_anyOf_i2)

- Type: null

<a id="headingCHANGED_fields_user_identifier"></a>
<a id="CHANGED_fields_user_identifier"></a>
##### user_identifier (required)

- Schema name: `User Identifier`

User ID (numeric) or SID (string) that owns this API key.
<a id="CHANGED_fields_user_identifier_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_user_identifier_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_user_identifier_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_user_identifier_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_user_identifier_anyOf_i1)

- Type: string

<a id="headingCHANGED_fields_iterations"></a>
<a id="CHANGED_fields_iterations"></a>
##### iterations (required)

- Schema name: `Iterations`
- Type: integer

Number of iterations of PBKDF2-SHA512.

<a id="headingCHANGED_fields_salt"></a>
<a id="CHANGED_fields_salt"></a>
##### salt (required)

- Schema name: `Salt`
- Type: string

Base64 encoded salt for API key.

<a id="headingCHANGED_fields_stored_key"></a>
<a id="CHANGED_fields_stored_key"></a>
##### stored_key (required)

- Schema name: `Stored Key`
- Type: string

SCRAM StoredKey for API key.

<a id="headingCHANGED_fields_server_key"></a>
<a id="CHANGED_fields_server_key"></a>
##### server_key (required)

- Schema name: `Server Key`
- Type: string

SCRAM ServerKey for API key.

<a id="headingCHANGED_fields_created_at"></a>
<a id="CHANGED_fields_created_at"></a>
##### created_at (required)

- Schema name: `Created At`
- Type: string
- Type: Format: date-time

Timestamp when the API key was created.

<a id="headingCHANGED_fields_expires_at"></a>
<a id="CHANGED_fields_expires_at"></a>
##### expires_at

- Schema name: `Expires At`
- Default: null

Expiration timestamp for the API key or `null` for no expiration.
<a id="CHANGED_fields_expires_at_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_expires_at_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_expires_at_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_CHANGED_fields_expires_at_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_expires_at_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_local"></a>
<a id="CHANGED_fields_local"></a>
##### local (required)

- Schema name: `Local`
- Type: boolean

Whether the API key belongs to a local user account rather than a directory services one.

<a id="headingCHANGED_fields_revoked"></a>
<a id="CHANGED_fields_revoked"></a>
##### revoked (required)

- Schema name: `Revoked`
- Type: boolean

Whether the API key has been revoked and is no longer valid.

<a id="headingCHANGED_fields_revoked_reason"></a>
<a id="CHANGED_fields_revoked_reason"></a>
##### revoked_reason (required)

- Schema name: `Revoked Reason`

Reason for API key revocation or `null` if not revoked.
<a id="CHANGED_fields_revoked_reason_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_revoked_reason_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_revoked_reason_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_revoked_reason_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_revoked_reason_anyOf_i1)

- Type: null

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `ApiKeyRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
