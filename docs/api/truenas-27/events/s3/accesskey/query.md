---
title: s3.accesskey.query
kind: event
source_rst: _sources/api_events_s3.accesskey.query.rst.txt
source_html: api_events_s3.accesskey.query.html
required_roles:
  - SHARING_S3_READ
---

# s3.accesskey.query

## Summary

Sent on s3.accesskey changes.

## Required Roles

- `SHARING_S3_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `S3AccesskeyAddedEvent`
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

- Schema name: `S3AccesskeyEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the access key.

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the access key.
- Must be at least `1` characters long
- Must be at most `200` characters long

<a id="headingADDED_fields_username"></a>
<a id="ADDED_fields_username"></a>
##### username (required)

- Schema name: `Username`

Account the access key belongs to, or `null` if that account no longer exists.
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

Stored account linkage. A numeric user ID for local accounts or a SID for directory services accounts.
<a id="ADDED_fields_user_identifier_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_user_identifier_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_user_identifier_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_user_identifier_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_user_identifier_anyOf_i1)

- Type: string

<a id="headingADDED_fields_local"></a>
<a id="ADDED_fields_local"></a>
##### local (required)

- Schema name: `Local`
- Type: boolean

Whether the access key belongs to a local user account rather than a directory services one.

<a id="headingADDED_fields_access_key"></a>
<a id="ADDED_fields_access_key"></a>
##### access_key (required)

- Schema name: `Access Key`
- Type: string

The S3 access key id clients sign requests with.
- Must match regular expression: `^[A-Z0-9]{16,128}$`

<a id="headingADDED_fields_secret"></a>
<a id="ADDED_fields_secret"></a>
##### secret (required)

- Schema name: `Secret`

The S3 secret access key. Readable only by administrators holding `SHARING_S3_WRITE`; redacted for everyone else. `null` when the secret was lost to a configuration restore without the secret seed.
<a id="ADDED_fields_secret_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_secret_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_secret_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_secret_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_secret_anyOf_i1)

- Type: null

<a id="headingADDED_fields_enabled"></a>
<a id="ADDED_fields_enabled"></a>
##### enabled (required)

- Schema name: `Enabled`
- Type: boolean

Whether the access key may be used. A disabled key is refused by the S3 service.

<a id="headingADDED_fields_expires_at"></a>
<a id="ADDED_fields_expires_at"></a>
##### expires_at

- Schema name: `Expires At`
- Default: null

Expiration timestamp for the access key or `null` for no expiration.
<a id="ADDED_fields_expires_at_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_expires_at_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_expires_at_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_ADDED_fields_expires_at_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_expires_at_anyOf_i1)

- Type: null

<a id="headingADDED_fields_created_at"></a>
<a id="ADDED_fields_created_at"></a>
##### created_at (required)

- Schema name: `Created At`
- Type: string
- Type: Format: date-time

Timestamp when the access key was created.

<a id="headingADDED_fields_last_used_at"></a>
<a id="ADDED_fields_last_used_at"></a>
##### last_used_at

- Schema name: `Last Used At`
- Default: null

Time the S3 service last accepted a request signed with this key, or `null` if the key has never been used. The S3 service reports this at intervals, so a recent request can be absent for a short time. This field is read-only.
<a id="ADDED_fields_last_used_at_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_last_used_at_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_last_used_at_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_ADDED_fields_last_used_at_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_last_used_at_anyOf_i1)

- Type: null

<a id="headingADDED_fields_manage_buckets"></a>
<a id="ADDED_fields_manage_buckets"></a>
##### manage_buckets

- Schema name: `Manage Buckets`
- Type: boolean
- Default: false

Whether this access key may create and delete buckets through the S3 protocol. Setting it requires the account that owns the key to hold the `SHARING_S3_WRITE` role, checked when a call turns it on. It scopes the key, not the account: an account may hold several access keys, and leaving this off on one of them affects neither its other keys nor its own access to `sharing.s3.create`.

<a id="headingADDED_fields_status"></a>
<a id="ADDED_fields_status"></a>
##### status (required)

- Schema name: `Status`
- Type: enum (of string)

Effective state of the access key. Only `ENABLED` keys are usable. `DISABLED` was set by an administrator, `EXPIRED` passed its expiration, `USER_MISSING` belongs to a directory account that no longer resolves (a deleted local account takes its keys with it), and `SECRET_LOST` lost its secret to a configuration restore without the secret seed and must be rotated.
###### Must be one of:

- "ENABLED"
- "DISABLED"
- "EXPIRED"
- "USER_MISSING"
- "SECRET_LOST"

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `S3AccesskeyChangedEvent`
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

- Schema name: `S3AccesskeyEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the access key.

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the access key.
- Must be at least `1` characters long
- Must be at most `200` characters long

<a id="headingCHANGED_fields_username"></a>
<a id="CHANGED_fields_username"></a>
##### username (required)

- Schema name: `Username`

Account the access key belongs to, or `null` if that account no longer exists.
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

Stored account linkage. A numeric user ID for local accounts or a SID for directory services accounts.
<a id="CHANGED_fields_user_identifier_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_user_identifier_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_user_identifier_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_user_identifier_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_user_identifier_anyOf_i1)

- Type: string

<a id="headingCHANGED_fields_local"></a>
<a id="CHANGED_fields_local"></a>
##### local (required)

- Schema name: `Local`
- Type: boolean

Whether the access key belongs to a local user account rather than a directory services one.

<a id="headingCHANGED_fields_access_key"></a>
<a id="CHANGED_fields_access_key"></a>
##### access_key (required)

- Schema name: `Access Key`
- Type: string

The S3 access key id clients sign requests with.
- Must match regular expression: `^[A-Z0-9]{16,128}$`

<a id="headingCHANGED_fields_secret"></a>
<a id="CHANGED_fields_secret"></a>
##### secret (required)

- Schema name: `Secret`

The S3 secret access key. Readable only by administrators holding `SHARING_S3_WRITE`; redacted for everyone else. `null` when the secret was lost to a configuration restore without the secret seed.
<a id="CHANGED_fields_secret_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_secret_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_secret_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_secret_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_secret_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_enabled"></a>
<a id="CHANGED_fields_enabled"></a>
##### enabled (required)

- Schema name: `Enabled`
- Type: boolean

Whether the access key may be used. A disabled key is refused by the S3 service.

<a id="headingCHANGED_fields_expires_at"></a>
<a id="CHANGED_fields_expires_at"></a>
##### expires_at

- Schema name: `Expires At`
- Default: null

Expiration timestamp for the access key or `null` for no expiration.
<a id="CHANGED_fields_expires_at_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_expires_at_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_expires_at_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_CHANGED_fields_expires_at_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_expires_at_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_created_at"></a>
<a id="CHANGED_fields_created_at"></a>
##### created_at (required)

- Schema name: `Created At`
- Type: string
- Type: Format: date-time

Timestamp when the access key was created.

<a id="headingCHANGED_fields_last_used_at"></a>
<a id="CHANGED_fields_last_used_at"></a>
##### last_used_at

- Schema name: `Last Used At`
- Default: null

Time the S3 service last accepted a request signed with this key, or `null` if the key has never been used. The S3 service reports this at intervals, so a recent request can be absent for a short time. This field is read-only.
<a id="CHANGED_fields_last_used_at_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_last_used_at_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_last_used_at_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_CHANGED_fields_last_used_at_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_last_used_at_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_manage_buckets"></a>
<a id="CHANGED_fields_manage_buckets"></a>
##### manage_buckets

- Schema name: `Manage Buckets`
- Type: boolean
- Default: false

Whether this access key may create and delete buckets through the S3 protocol. Setting it requires the account that owns the key to hold the `SHARING_S3_WRITE` role, checked when a call turns it on. It scopes the key, not the account: an account may hold several access keys, and leaving this off on one of them affects neither its other keys nor its own access to `sharing.s3.create`.

<a id="headingCHANGED_fields_status"></a>
<a id="CHANGED_fields_status"></a>
##### status (required)

- Schema name: `Status`
- Type: enum (of string)

Effective state of the access key. Only `ENABLED` keys are usable. `DISABLED` was set by an administrator, `EXPIRED` passed its expiration, `USER_MISSING` belongs to a directory account that no longer resolves (a deleted local account takes its keys with it), and `SECRET_LOST` lost its secret to a configuration restore without the secret seed and must be rotated.
###### Must be one of:

- "ENABLED"
- "DISABLED"
- "EXPIRED"
- "USER_MISSING"
- "SECRET_LOST"

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `S3AccesskeyRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
