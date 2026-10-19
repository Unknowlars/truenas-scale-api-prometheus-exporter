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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `SNMPEntry`
- Type: object
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
- Default: ""

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
