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

### ADDED

- Schema name: `AuthSessionsAddedEvent`
- Type: object
- No Additional Properties
#### fields (required)

- Schema name: `AuthSessionsEntry`
- Type: object

Event fields.
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the authentication session.

##### current (required)

- Schema name: `Current`
- Type: boolean

Whether this is the current active session.

##### internal (required)

- Schema name: `Internal`
- Type: boolean

Whether this is an internal system session. Pass `[["internal", "=", false]]` as `query-filters` to exclude internal sessions from the list.

##### origin (required)

- Schema name: `Origin`
- Type: string

Origin information for the session (IP address, hostname, etc.).

##### credentials (required)

- Schema name: `Credentials`
- Type: enum (of string)

Authentication method used for this session. `UNIX_SOCKET`: Local Unix domain socket authentication `LOGIN_PASSWORD`: Username and password authentication `LOGIN_TWOFACTOR`: Two-factor authentication login `LOGIN_ONETIME_PASSWORD`: One-time password authentication `API_KEY`: API key authentication `TOKEN`: Token-based authentication `TRUENAS_NODE`: TrueNAS cluster node authentication

##### credentials_data (required)

- Schema name: `Credentials Data`

Detailed credential information specific to the authentication method.
###### Any of

####### BaseCredentialData

- Schema name: `BaseCredentialData`
- Type: object

####### UserCredentialData

- Schema name: `UserCredentialData`
- Type: object
- No Additional Properties
######## username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

######## login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

######## login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

####### APIKeyCredentialData

- Schema name: `APIKeyCredentialData`
- Type: object
- No Additional Properties
######## username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

######## login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

######## login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

######## api_key (required)

- Schema name: `APIKeySessionData`
- Type: object

API key information used for authentication.
- No Additional Properties
######### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the API key.

######### name (required)

- Schema name: `Name`
- Type: string

Human-readable name of the API key.

####### TokenCredentialData

- Schema name: `TokenCredentialData`
- Type: object
- No Additional Properties
######## parent (required)

- Schema name: `TokenParentCredentialsData`
- Type: object

Parent credential information that generated this token.
- No Additional Properties
######### credentials (required)

- Schema name: `Credentials`
- Type: enum (of string)

Type of credentials used to generate this token.

######### credentials_data (required)

- Schema name: `Credentials Data`

Credential data used to authenticate the token request.
########## Any of

########### BaseCredentialData

- Schema name: `BaseCredentialData`
- Type: object

########### UserCredentialData

- Schema name: `UserCredentialData`
- Type: object
- No Additional Properties
############ username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

############ login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

############ login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

########### APIKeyCredentialData

- Schema name: `APIKeyCredentialData`
- Type: object
- No Additional Properties
############ username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

############ login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

############ login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

############ api_key (required)

- Type: object

API key information used for authentication.

########### TokenCredentialData

- Schema name: `TokenCredentialData`
- Type: object
- No Additional Properties
############ parent (required)

- Type: object

Parent credential information that generated this token.

############ login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

############ username (required)

- Schema name: `Username`

Username associated with the token. `null` if not user-specific.
############# Any of

############## Option 1

- Type: string

############## Option 2

- Type: null

########### Option 1

- Type: string

########### Option 2

- Type: null

######## login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

######## username (required)

- Schema name: `Username`

Username associated with the token. `null` if not user-specific.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

####### BaseCredentialData

- Schema name: `BaseCredentialData`
- Type: object

####### UserCredentialData

- Schema name: `UserCredentialData`
- Type: object
- No Additional Properties
######## username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

######## login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

######## login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

####### APIKeyCredentialData

- Schema name: `APIKeyCredentialData`
- Type: object
- No Additional Properties
######## username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

######## login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

######## login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

######## api_key (required)

- Type: object

API key information used for authentication.

####### TokenCredentialData

- Schema name: `TokenCredentialData`
- Type: object
- No Additional Properties
######## parent (required)

- Type: object

Parent credential information that generated this token.

######## login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

######## username (required)

- Schema name: `Username`

Username associated with the token. `null` if not user-specific.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

####### Option 1

- Type: string

####### Option 2

- Type: null

####### Option 1

- Type: string

####### Option 2

- Type: null

##### created_at (required)

- Schema name: `Created At`
- Type: string
- Type: Format: date-time

Timestamp when the session was created.

##### secure_transport (required)

- Schema name: `Secure Transport`
- Type: boolean

Whether the session was established over a secure transport (HTTPS/WSS).

### REMOVED

- Schema name: `AuthSessionsRemovedEvent`
- Type: object
- No Additional Properties
#### fields (required)

- Schema name: `AuthSessionsRemovedEventFields`
- Type: object

Event fields.
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the authentication session.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
