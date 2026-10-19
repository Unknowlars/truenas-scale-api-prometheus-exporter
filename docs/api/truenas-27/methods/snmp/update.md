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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: snmp_update

<a id="Call_parameters_items_i0"></a>
#### snmp_update

- Schema name: `snmp_update`
- Type: object

SNMPUpdateArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_location"></a>
<a id="Call_parameters_items_i0_location"></a>
##### location

- Schema name: `Location`
- Type: string

A comment describing the physical location of the server.

<a id="headingCall_parameters_items_i0_contact"></a>
<a id="Call_parameters_items_i0_contact"></a>
##### contact

- Schema name: `Contact`

Contact information for the system administrator (email or name).
<a id="Call_parameters_items_i0_contact_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_contact_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_contact_anyOf_i0)

- Type: string
- Type: Format: email

<a id="tab-pane_Call_parameters_items_i0_contact_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_contact_anyOf_i1)

- Type: string
- Must match regular expression: `^[-_a-zA-Z0-9\s]*$`

<a id="headingCall_parameters_items_i0_traps"></a>
<a id="Call_parameters_items_i0_traps"></a>
##### traps

- Schema name: `Traps`
- Type: boolean

Whether SNMP traps are enabled.

<a id="headingCall_parameters_items_i0_v3"></a>
<a id="Call_parameters_items_i0_v3"></a>
##### v3

- Schema name: `V3`
- Type: boolean

Whether SNMP version 3 is enabled. Enabling version 3 also requires username, authtype and password.

<a id="headingCall_parameters_items_i0_community"></a>
<a id="Call_parameters_items_i0_community"></a>
##### community

- Schema name: `Community`
- Type: string

SNMP community string for v1/v2c access. Allows letters and numbers: a-zA-Z0-9 special characters: !$%&()+-_={}[]<>,.? and spaces. Notable excluded characters: # / \ @.
- Must match regular expression: `^[!\$%&()\+\-_={}\[\]<>,\.\?a-zA-Z0-9\s]*$`

<a id="headingCall_parameters_items_i0_v3_username"></a>
<a id="Call_parameters_items_i0_v3_username"></a>
##### v3_username

- Schema name: `V3 Username`
- Type: string

Username for SNMP version 3 authentication.
- Must be at most `20` characters long

<a id="headingCall_parameters_items_i0_v3_authtype"></a>
<a id="Call_parameters_items_i0_v3_authtype"></a>
##### v3_authtype

- Schema name: `V3 Authtype`
- Type: enum (of string)

Authentication type for SNMP version 3 (empty string means no authentication).
###### Must be one of:

- ""
- "MD5"
- "SHA"

<a id="headingCall_parameters_items_i0_v3_password"></a>
<a id="Call_parameters_items_i0_v3_password"></a>
##### v3_password

- Schema name: `V3 Password`
- Type: string

Password for SNMP version 3 authentication.

<a id="headingCall_parameters_items_i0_v3_privproto"></a>
<a id="Call_parameters_items_i0_v3_privproto"></a>
##### v3_privproto

- Schema name: `V3 Privproto`

Privacy protocol for SNMP version 3 encryption. `null` means no encryption. If set, ['AES'|'DES'], a `privpassphrase` must be supplied.
<a id="Call_parameters_items_i0_v3_privproto_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_v3_privproto_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_v3_privproto_anyOf_i0)

- Type: enum (of null or string)
###### Must be one of:

- null
- "AES"
- "DES"

<a id="tab-pane_Call_parameters_items_i0_v3_privproto_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_v3_privproto_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_v3_privpassphrase"></a>
<a id="Call_parameters_items_i0_v3_privpassphrase"></a>
##### v3_privpassphrase

- Schema name: `V3 Privpassphrase`

Privacy passphrase for SNMP version 3 encryption. This field is required when `privproto` is set.
<a id="Call_parameters_items_i0_v3_privpassphrase_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_v3_privpassphrase_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_v3_privpassphrase_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_v3_privpassphrase_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_v3_privpassphrase_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_loglevel"></a>
<a id="Call_parameters_items_i0_loglevel"></a>
##### loglevel

- Schema name: `Loglevel`
- Type: integer

Logging level for SNMP daemon (0=emergency to 7=debug).
- Value must be greater or equal to `0` and lesser or equal to `7`

<a id="headingCall_parameters_items_i0_options"></a>
<a id="Call_parameters_items_i0_options"></a>
##### options

- Schema name: `Options`
- Type: string

Additional SNMP daemon configuration options. Manual settings should be used with caution as they may render the SNMP service non-functional.

<a id="headingCall_parameters_items_i0_zilstat"></a>
<a id="Call_parameters_items_i0_zilstat"></a>
##### zilstat

- Schema name: `Zilstat`
- Type: boolean

Whether to enable ZFS dataset statistics collection for SNMP.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `SNMPEntry`
- Type: object

The updated SNMP service configuration.
- No Additional Properties
<a id="headingReturn_value_location"></a>
<a id="Return_value_location"></a>
#### location (required)

- Schema name: `Location`
- Type: string

A comment describing the physical location of the server.

<a id="headingReturn_value_contact"></a>
<a id="Return_value_contact"></a>
#### contact (required)

- Schema name: `Contact`

Contact information for the system administrator (email or name).
<a id="Return_value_contact_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_contact_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_contact_anyOf_i0)

- Type: string
- Type: Format: email

<a id="tab-pane_Return_value_contact_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_contact_anyOf_i1)

- Type: string
- Must match regular expression: `^[-_a-zA-Z0-9\s]*$`

<a id="headingReturn_value_traps"></a>
<a id="Return_value_traps"></a>
#### traps (required)

- Schema name: `Traps`
- Type: boolean

Whether SNMP traps are enabled.

<a id="headingReturn_value_v3"></a>
<a id="Return_value_v3"></a>
#### v3 (required)

- Schema name: `V3`
- Type: boolean

Whether SNMP version 3 is enabled. Enabling version 3 also requires username, authtype and password.

<a id="headingReturn_value_community"></a>
<a id="Return_value_community"></a>
#### community

- Schema name: `Community`
- Type: string
- Default: "public"

SNMP community string for v1/v2c access. Allows letters and numbers: a-zA-Z0-9 special characters: !$%&()+-_={}[]<>,.? and spaces. Notable excluded characters: # / \ @.
- Must match regular expression: `^[!\$%&()\+\-_={}\[\]<>,\.\?a-zA-Z0-9\s]*$`

<a id="headingReturn_value_v3_username"></a>
<a id="Return_value_v3_username"></a>
#### v3_username (required)

- Schema name: `V3 Username`
- Type: string

Username for SNMP version 3 authentication.
- Must be at most `20` characters long

<a id="headingReturn_value_v3_authtype"></a>
<a id="Return_value_v3_authtype"></a>
#### v3_authtype (required)

- Schema name: `V3 Authtype`
- Type: enum (of string)

Authentication type for SNMP version 3 (empty string means no authentication).
##### Must be one of:

- ""
- "MD5"
- "SHA"

<a id="headingReturn_value_v3_password"></a>
<a id="Return_value_v3_password"></a>
#### v3_password (required)

- Schema name: `V3 Password`
- Type: string

Password for SNMP version 3 authentication.

<a id="headingReturn_value_v3_privproto"></a>
<a id="Return_value_v3_privproto"></a>
#### v3_privproto (required)

- Schema name: `V3 Privproto`

Privacy protocol for SNMP version 3 encryption. `null` means no encryption. If set, ['AES'|'DES'], a `privpassphrase` must be supplied.
<a id="Return_value_v3_privproto_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_v3_privproto_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_v3_privproto_anyOf_i0)

- Type: enum (of null or string)
###### Must be one of:

- null
- "AES"
- "DES"

<a id="tab-pane_Return_value_v3_privproto_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_v3_privproto_anyOf_i1)

- Type: null

<a id="headingReturn_value_v3_privpassphrase"></a>
<a id="Return_value_v3_privpassphrase"></a>
#### v3_privpassphrase

- Schema name: `V3 Privpassphrase`
- Default: null

Privacy passphrase for SNMP version 3 encryption. This field is required when `privproto` is set.
<a id="Return_value_v3_privpassphrase_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_v3_privpassphrase_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_v3_privpassphrase_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_v3_privpassphrase_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_v3_privpassphrase_anyOf_i1)

- Type: null

<a id="headingReturn_value_loglevel"></a>
<a id="Return_value_loglevel"></a>
#### loglevel (required)

- Schema name: `Loglevel`
- Type: integer

Logging level for SNMP daemon (0=emergency to 7=debug).
- Value must be greater or equal to `0` and lesser or equal to `7`

<a id="headingReturn_value_options"></a>
<a id="Return_value_options"></a>
#### options (required)

- Schema name: `Options`
- Type: string

Additional SNMP daemon configuration options. Manual settings should be used with caution as they may render the SNMP service non-functional.

<a id="headingReturn_value_zilstat"></a>
<a id="Return_value_zilstat"></a>
#### zilstat (required)

- Schema name: `Zilstat`
- Type: boolean

Whether to enable ZFS dataset statistics collection for SNMP.

<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Placeholder identifier. Not used as there is only one.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
