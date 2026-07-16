---
title: api_key.update
kind: method
source_rst: _sources/api_methods_api_key.update.rst.txt
source_html: api_methods_api_key.update.html
required_roles:
  - API_KEY_WRITE | READONLY_ADMIN
---

# api_key.update

## Summary

Update API Key `id`.

Specify `reset: true` to reset this API Key.

## Required Roles

- `API_KEY_WRITE | READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the API key to update.

#### Parameter 2: api_key_update

#### api_key_update

- Schema name: `api_key_update`
- Type: object

Updated API key configuration data.
- No Additional Properties
##### name

- Schema name: `Name`
- Type: string

Human-readable name for the API key.
- Must be at least `1` characters long
- Must be at most `200` characters long

##### expires_at

- Schema name: `Expires At`

Expiration timestamp for the API key or `null` for no expiration.
###### Any of

####### Option 1

- Type: string
- Type: Format: date-time

####### Option 2

- Type: null

##### reset

- Schema name: `Reset`
- Type: boolean

Whether to regenerate a new API key value for this entry.

### Return value

- Schema name: `Result`

The updated API key (includes key value if reset was performed).
#### Any of

##### ApiKeyEntryWithKey

- Schema name: `ApiKeyEntryWithKey`
- Type: object
- No Additional Properties
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the API key.

###### name

- Schema name: `Name`
- Type: string
- Default: "nobody"

Human-readable name for the API key.
- Must be at least `1` characters long
- Must be at most `200` characters long

###### username (required)

- Schema name: `Username`

Username associated with the API key or `null` for system keys.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: string
- Must be at least `1` characters long

######## Option 3

- Type: null

###### user_identifier (required)

- Schema name: `User Identifier`

User ID (numeric) or SID (string) that owns this API key.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: string

###### keyhash (required)

- Schema name: `Keyhash`
- Type: string

Hashed representation of the API key (masked for security).

###### created_at (required)

- Schema name: `Created At`
- Type: string
- Type: Format: date-time

Timestamp when the API key was created.

###### expires_at

- Schema name: `Expires At`
- Default: null

Expiration timestamp for the API key or `null` for no expiration.
####### Any of

######## Option 1

- Type: string
- Type: Format: date-time

######## Option 2

- Type: null

###### local (required)

- Schema name: `Local`
- Type: boolean

Whether this API key is for local system use only.

###### revoked (required)

- Schema name: `Revoked`
- Type: boolean

Whether the API key has been revoked and is no longer valid.

###### revoked_reason (required)

- Schema name: `Revoked Reason`

Reason for API key revocation or `null` if not revoked.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### key (required)

- Schema name: `Key`
- Type: string

The actual API key value (only returned on creation).

##### ApiKeyEntry

- Type: string

##### Option 1

- Type: string
- Must be at least `1` characters long

##### Option 2

- Type: null

##### Option 3

- Type: integer

##### Option 1

- Type: string

##### Option 2

- Type: string
- Type: Format: date-time

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Schema name: `ApiKeyEntry`
- Type: object
- No Additional Properties
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the API key.

###### name

- Schema name: `Name`
- Type: string
- Default: "nobody"

Human-readable name for the API key.
- Must be at least `1` characters long
- Must be at most `200` characters long

###### username (required)

- Schema name: `Username`

Username associated with the API key or `null` for system keys.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: string
- Must be at least `1` characters long

######## Option 3

- Type: null

###### user_identifier (required)

- Schema name: `User Identifier`

User ID (numeric) or SID (string) that owns this API key.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: string

###### keyhash (required)

- Schema name: `Keyhash`
- Type: string

Hashed representation of the API key (masked for security).

###### created_at (required)

- Schema name: `Created At`
- Type: string
- Type: Format: date-time

Timestamp when the API key was created.

###### expires_at

- Schema name: `Expires At`
- Default: null

Expiration timestamp for the API key or `null` for no expiration.
####### Any of

######## Option 1

- Type: string
- Type: Format: date-time

######## Option 2

- Type: null

###### local (required)

- Schema name: `Local`
- Type: boolean

Whether this API key is for local system use only.

###### revoked (required)

- Schema name: `Revoked`
- Type: boolean

Whether the API key has been revoked and is no longer valid.

###### revoked_reason (required)

- Schema name: `Revoked Reason`

Reason for API key revocation or `null` if not revoked.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: string
- Must be at least `1` characters long

##### Option 3

- Type: null

##### Option 1

- Type: integer

##### Option 2

- Type: string

##### Option 1

- Type: string
- Type: Format: date-time

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
