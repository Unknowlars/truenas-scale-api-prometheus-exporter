---
title: snmp.config
kind: method
source_rst: _sources/api_methods_snmp.config.rst.txt
source_html: api_methods_snmp.config.html
required_roles:
  - SYSTEM_GENERAL_READ
---

# snmp.config

## Required Roles

- `SYSTEM_GENERAL_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `SnmpEntry`
- Type: object
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
