---
title: kerberos.keytab.update
kind: method
source_rst: _sources/api_methods_kerberos.keytab.update.rst.txt
source_html: api_methods_kerberos.keytab.update.html
required_roles:
  - DIRECTORY_SERVICE_WRITE
---

# kerberos.keytab.update

## Summary

Update kerberos keytab by id.

## Required Roles

- `DIRECTORY_SERVICE_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the Kerberos keytab entry to update.

#### Parameter 2: data

<a id="Call_parameters_items_i1"></a>
#### data

- Schema name: `data`
- Type: object

Updated Kerberos keytab configuration data.
- No Additional Properties
<a id="headingCall_parameters_items_i1_name"></a>
<a id="Call_parameters_items_i1_name"></a>
##### name

- Schema name: `Name`
- Type: string

Name of the kerberos keytab entry. This is an identifier for the keytab and not the name of the keytab file. Some names are used for internal purposes such as AD*MACHINE*ACCOUNT and IPA*MACHINE*ACCOUNT.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i1_file"></a>
<a id="Call_parameters_items_i1_file"></a>
##### file

- Schema name: `File`

Base64 encoded kerberos keytab entries to append to the system keytab.
<a id="Call_parameters_items_i1_file_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_file_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_file_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i1_file_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_file_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `KerberosKeytabEntry`
- Type: object

The updated Kerberos keytab entry.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Kerberos keytab entry.

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

Name of the kerberos keytab entry. This is an identifier for the keytab and not the name of the keytab file. Some names are used for internal purposes such as AD*MACHINE*ACCOUNT and IPA*MACHINE*ACCOUNT.
- Must be at least `1` characters long

<a id="headingReturn_value_file"></a>
<a id="Return_value_file"></a>
#### file (required)

- Schema name: `File`

Base64 encoded kerberos keytab entries to append to the system keytab.
<a id="Return_value_file_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_file_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_file_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_file_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_file_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
