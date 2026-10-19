---
title: auth.sessions
kind: event
source_rst: _sources/api_events_auth.sessions.rst.txt
source_html: api_events_auth.sessions.html
required_roles:
  - FULL_ADMIN
---

# auth.sessions

## Summary

Notification of new and removed sessions.

## Required Roles

- `FULL_ADMIN`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `AuthSessionsAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `AuthSessionsEntry`
- Type: object

Event fields.
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the authentication session.

<a id="headingADDED_fields_current"></a>
<a id="ADDED_fields_current"></a>
##### current (required)

- Schema name: `Current`
- Type: boolean

Whether this is the current active session.

<a id="headingADDED_fields_internal"></a>
<a id="ADDED_fields_internal"></a>
##### internal (required)

- Schema name: `Internal`
- Type: boolean

Whether this is an internal system session.

<a id="headingADDED_fields_origin"></a>
<a id="ADDED_fields_origin"></a>
##### origin (required)

- Schema name: `Origin`
- Type: string

Origin information for the session (IP address, hostname, etc.).

<a id="headingADDED_fields_credentials"></a>
<a id="ADDED_fields_credentials"></a>
##### credentials (required)

- Schema name: `Credentials`
- Type: enum (of string)

Authentication method used for this session. `UNIX_SOCKET`: Local Unix domain socket authentication `LOGIN_PASSWORD`: Username and password authentication `LOGIN_TWOFACTOR`: Two-factor authentication login `LOGIN_ONETIME_PASSWORD`: One-time password authentication `API_KEY`: API key authentication `TOKEN`: Token-based authentication `TRUENAS_NODE`: TrueNAS cluster node authentication
###### Must be one of:

- "UNIX_SOCKET"
- "LOGIN_PASSWORD"
- "LOGIN_TWOFACTOR"
- "LOGIN_ONETIME_PASSWORD"
- "API_KEY"
- "TOKEN"
- "TRUENAS_NODE"

<a id="headingADDED_fields_credentials_data"></a>
<a id="ADDED_fields_credentials_data"></a>
##### credentials_data (required)

- Schema name: `Credentials Data`

Detailed credential information specific to the authentication method.
<a id="ADDED_fields_credentials_data_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_credentials_data_anyOf_i0"></a>
###### [BaseCredentialData](#tab-pane_ADDED_fields_credentials_data_anyOf_i0)

- Schema name: `BaseCredentialData`
- Type: object

<a id="tab-pane_ADDED_fields_credentials_data_anyOf_i1"></a>
###### [UserCredentialData](#tab-pane_ADDED_fields_credentials_data_anyOf_i1)

- Schema name: `UserCredentialData`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_credentials_data_anyOf_i1_username"></a>
<a id="ADDED_fields_credentials_data_anyOf_i1_username"></a>
###### username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

<a id="headingADDED_fields_credentials_data_anyOf_i1_login_id"></a>
<a id="ADDED_fields_credentials_data_anyOf_i1_login_id"></a>
###### login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

<a id="headingADDED_fields_credentials_data_anyOf_i1_login_at"></a>
<a id="ADDED_fields_credentials_data_anyOf_i1_login_at"></a>
###### login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

<a id="tab-pane_ADDED_fields_credentials_data_anyOf_i2"></a>
###### [APIKeyCredentialData](#tab-pane_ADDED_fields_credentials_data_anyOf_i2)

- Schema name: `APIKeyCredentialData`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_credentials_data_anyOf_i2_username"></a>
<a id="ADDED_fields_credentials_data_anyOf_i2_username"></a>
###### username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

<a id="headingADDED_fields_credentials_data_anyOf_i2_login_id"></a>
<a id="ADDED_fields_credentials_data_anyOf_i2_login_id"></a>
###### login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

<a id="headingADDED_fields_credentials_data_anyOf_i2_login_at"></a>
<a id="ADDED_fields_credentials_data_anyOf_i2_login_at"></a>
###### login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

<a id="headingADDED_fields_credentials_data_anyOf_i2_api_key"></a>
<a id="ADDED_fields_credentials_data_anyOf_i2_api_key"></a>
###### api_key (required)

- Schema name: `APIKeySessionData`
- Type: object

API key information used for authentication.
- No Additional Properties
<a id="headingADDED_fields_credentials_data_anyOf_i2_api_key_id"></a>
<a id="ADDED_fields_credentials_data_anyOf_i2_api_key_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the API key.

<a id="headingADDED_fields_credentials_data_anyOf_i2_api_key_name"></a>
<a id="ADDED_fields_credentials_data_anyOf_i2_api_key_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Human-readable name of the API key.

<a id="tab-pane_ADDED_fields_credentials_data_anyOf_i3"></a>
###### [TokenCredentialData](#tab-pane_ADDED_fields_credentials_data_anyOf_i3)

- Schema name: `TokenCredentialData`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_credentials_data_anyOf_i3_parent"></a>
<a id="ADDED_fields_credentials_data_anyOf_i3_parent"></a>
###### parent (required)

- Schema name: `TokenParentCredentialsData`
- Type: object

Parent credential information that generated this token.
- No Additional Properties
<a id="headingADDED_fields_credentials_data_anyOf_i3_parent_credentials"></a>
<a id="ADDED_fields_credentials_data_anyOf_i3_parent_credentials"></a>
###### credentials (required)

- Schema name: `Credentials`
- Type: enum (of string)

Type of credentials used to generate this token.
###### Must be one of:

- "UNIX_SOCKET"
- "LOGIN_PASSWORD"
- "LOGIN_TWOFACTOR"
- "API_KEY"
- "TOKEN"
- "TRUENAS_NODE"

<a id="headingADDED_fields_credentials_data_anyOf_i3_parent_credentials_data"></a>
<a id="ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data"></a>
###### credentials_data (required)

- Schema name: `Credentials Data`

Credential data used to authenticate the token request.
<a id="ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i0"></a>
###### [BaseCredentialData](#tab-pane_ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i0)

- Schema name: `BaseCredentialData`
- Type: object

<a id="tab-pane_ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i1"></a>
###### [UserCredentialData](#tab-pane_ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i1)

- Schema name: `UserCredentialData`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i1_username"></a>
<a id="ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i1_username"></a>
###### username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

<a id="headingADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i1_login_id"></a>
<a id="ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i1_login_id"></a>
###### login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

<a id="headingADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i1_login_at"></a>
<a id="ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i1_login_at"></a>
###### login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

<a id="tab-pane_ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i2"></a>
###### [APIKeyCredentialData](#tab-pane_ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i2)

- Schema name: `APIKeyCredentialData`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i2_username"></a>
<a id="ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i2_username"></a>
###### username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

<a id="headingADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i2_login_id"></a>
<a id="ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i2_login_id"></a>
###### login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

<a id="headingADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i2_login_at"></a>
<a id="ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i2_login_at"></a>
###### login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

<a id="headingADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i2_api_key"></a>
<a id="ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i2_api_key"></a>
###### api_key (required)

- Type: object

API key information used for authentication.

<a id="tab-pane_ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3"></a>
###### [TokenCredentialData](#tab-pane_ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3)

- Schema name: `TokenCredentialData`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3_parent"></a>
<a id="ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3_parent"></a>
###### parent (required)

- Type: object

Parent credential information that generated this token.

<a id="headingADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3_login_id"></a>
<a id="ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3_login_id"></a>
###### login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

<a id="headingADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3_username"></a>
<a id="ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3_username"></a>
###### username (required)

- Schema name: `Username`

Username associated with the token. `null` if not user-specific.
<a id="ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3_username_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3_username_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3_username_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3_username_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3_username_anyOf_i1)

- Type: null

<a id="headingADDED_fields_credentials_data_anyOf_i3_login_id"></a>
<a id="ADDED_fields_credentials_data_anyOf_i3_login_id"></a>
###### login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

<a id="headingADDED_fields_credentials_data_anyOf_i3_username"></a>
<a id="ADDED_fields_credentials_data_anyOf_i3_username"></a>
###### username (required)

- Schema name: `Username`

Username associated with the token. `null` if not user-specific.
<a id="ADDED_fields_credentials_data_anyOf_i3_username_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_credentials_data_anyOf_i3_username_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_credentials_data_anyOf_i3_username_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_credentials_data_anyOf_i3_username_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_credentials_data_anyOf_i3_username_anyOf_i1)

- Type: null

<a id="headingADDED_fields_created_at"></a>
<a id="ADDED_fields_created_at"></a>
##### created_at (required)

- Schema name: `Created At`
- Type: string
- Type: Format: date-time

Timestamp when the session was created.

<a id="headingADDED_fields_secure_transport"></a>
<a id="ADDED_fields_secure_transport"></a>
##### secure_transport (required)

- Schema name: `Secure Transport`
- Type: boolean

Whether the session was established over a secure transport (HTTPS/WSS).

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `AuthSessionsRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_fields"></a>
<a id="REMOVED_fields"></a>
#### fields (required)

- Schema name: `AuthSessionsRemovedEventFields`
- Type: object

Event fields.
- No Additional Properties
<a id="headingREMOVED_fields_id"></a>
<a id="REMOVED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the authentication session.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
