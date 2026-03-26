---
title: snmp.update
kind: method
source_rst: _sources/api_methods_snmp.update.rst.txt
source_html: api_methods_snmp.update.html
required_roles:
  - SYSTEM_GENERAL_WRITE
---

# snmp.update

## Summary

Update SNMP Service Configuration.

--- Rules --- Enabling v3: requires v3_username, v3_authtype and v3_password Disabling v3: By itself will retain the v3 user settings and config in the 'private' config, but remove the entry in the public config to block v3 access by that user. Disabling v3 and clearing the v3_username: This will do the actions described in 'Disabling v3' and take the extra step to remove the user from the 'private' config.

The 'v3_*' settings are valid and enforced only when 'v3' is enabled

## Required Roles

- `SYSTEM_GENERAL_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: snmp_update

#### snmp_update

- Schema name: `snmp_update`
- Type: object

SNMPUpdateArgs parameters.
- No Additional Properties
##### location

- Schema name: `Location`
- Type: string

A comment describing the physical location of the server.

##### contact

- Schema name: `Contact`

Contact information for the system administrator (email or name).
###### Any of

####### Option 1

- Type: string
- Type: Format: email

####### Option 2

- Type: string

##### traps

- Schema name: `Traps`
- Type: boolean

Whether SNMP traps are enabled.

##### v3

- Schema name: `V3`
- Type: boolean

Whether SNMP version 3 is enabled. Enabling version 3 also requires username, authtype and password.

##### community

- Schema name: `Community`
- Type: string

SNMP community string for v1/v2c access. Allows letters and numbers: a-zA-Z0-9 special characters: !$%&()+-_={}[]<>,.? and spaces. Notable excluded characters: # / \ @

##### v3_username

- Schema name: `V3 Username`
- Type: string

Username for SNMP version 3 authentication.
- Must be at most `20` characters long

##### v3_authtype

- Schema name: `V3 Authtype`
- Type: enum (of string)

Authentication type for SNMP version 3 (empty string means no authentication).

##### v3_password

- Schema name: `V3 Password`
- Type: string

Password for SNMP version 3 authentication.

##### v3_privproto

- Schema name: `V3 Privproto`

Privacy protocol for SNMP version 3 encryption. `null` means no encryption. If set, ['AES'|'DES'], a `privpassphrase` must be supplied.
###### Any of

####### Option 1

- Type: enum (of null or string)

####### Option 2

- Type: null

##### v3_privpassphrase

- Schema name: `V3 Privpassphrase`

Privacy passphrase for SNMP version 3 encryption. This field is required when `privproto` is set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### loglevel

- Schema name: `Loglevel`
- Type: integer

Logging level for SNMP daemon (0=emergency to 7=debug).
- Value must be greater or equal to `0` and lesser or equal to `7`

##### options

- Schema name: `Options`
- Type: string

Additional SNMP daemon configuration options. Manual settings should be used with caution as they may render the SNMP service non-functional.

##### zilstat

- Schema name: `Zilstat`
- Type: boolean

Whether to enable ZFS dataset statistics collection for SNMP.

### Return value

- Schema name: `SnmpEntry`
- Type: object

The updated SNMP service configuration.
- No Additional Properties
#### location (required)

- Schema name: `Location`
- Type: string

A comment describing the physical location of the server.

#### contact (required)

- Schema name: `Contact`

Contact information for the system administrator (email or name).
##### Any of

###### Option 1

- Type: string
- Type: Format: email

###### Option 2

- Type: string

#### traps (required)

- Schema name: `Traps`
- Type: boolean

Whether SNMP traps are enabled.

#### v3 (required)

- Schema name: `V3`
- Type: boolean

Whether SNMP version 3 is enabled. Enabling version 3 also requires username, authtype and password.

#### community

- Schema name: `Community`
- Type: string
- Default: "public"

SNMP community string for v1/v2c access. Allows letters and numbers: a-zA-Z0-9 special characters: !$%&()+-_={}[]<>,.? and spaces. Notable excluded characters: # / \ @

#### v3_username (required)

- Schema name: `V3 Username`
- Type: string

Username for SNMP version 3 authentication.
- Must be at most `20` characters long

#### v3_authtype (required)

- Schema name: `V3 Authtype`
- Type: enum (of string)

Authentication type for SNMP version 3 (empty string means no authentication).

#### v3_password (required)

- Schema name: `V3 Password`
- Type: string

Password for SNMP version 3 authentication.

#### v3_privproto (required)

- Schema name: `V3 Privproto`

Privacy protocol for SNMP version 3 encryption. `null` means no encryption. If set, ['AES'|'DES'], a `privpassphrase` must be supplied.
##### Any of

###### Option 1

- Type: enum (of null or string)

###### Option 2

- Type: null

#### v3_privpassphrase

- Schema name: `V3 Privpassphrase`
- Default: null

Privacy passphrase for SNMP version 3 encryption. This field is required when `privproto` is set.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### loglevel (required)

- Schema name: `Loglevel`
- Type: integer

Logging level for SNMP daemon (0=emergency to 7=debug).
- Value must be greater or equal to `0` and lesser or equal to `7`

#### options (required)

- Schema name: `Options`
- Type: string

Additional SNMP daemon configuration options. Manual settings should be used with caution as they may render the SNMP service non-functional.

#### zilstat (required)

- Schema name: `Zilstat`
- Type: boolean

Whether to enable ZFS dataset statistics collection for SNMP.

#### id (required)

- Schema name: `Id`
- Type: integer

Placeholder identifier. Not used as there is only one.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
