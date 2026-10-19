---
title: kerberos.keytab.query
kind: event
source_rst: _sources/api_events_kerberos.keytab.query.rst.txt
source_html: api_events_kerberos.keytab.query.html
required_roles:
  - DIRECTORY_SERVICE_READ
---

# kerberos.keytab.query

## Summary

Sent on kerberos.keytab changes.

## Required Roles

- `DIRECTORY_SERVICE_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `KerberosKeytabAddedEvent`
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

- Schema name: `KerberosKeytabEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Kerberos keytab entry.

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of the kerberos keytab entry. This is an identifier for the keytab and not the name of the keytab file. Some names are used for internal purposes such as AD*MACHINE*ACCOUNT and IPA*MACHINE*ACCOUNT.
- Must be at least `1` characters long

<a id="headingADDED_fields_file"></a>
<a id="ADDED_fields_file"></a>
##### file (required)

- Schema name: `File`

Base64 encoded kerberos keytab entries to append to the system keytab.
<a id="ADDED_fields_file_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_file_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_file_anyOf_i0)

- Type: string
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="tab-pane_ADDED_fields_file_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_file_anyOf_i1)

- Type: null

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `KerberosKeytabChangedEvent`
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

- Schema name: `KerberosKeytabEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Kerberos keytab entry.

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of the kerberos keytab entry. This is an identifier for the keytab and not the name of the keytab file. Some names are used for internal purposes such as AD*MACHINE*ACCOUNT and IPA*MACHINE*ACCOUNT.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_file"></a>
<a id="CHANGED_fields_file"></a>
##### file (required)

- Schema name: `File`

Base64 encoded kerberos keytab entries to append to the system keytab.
<a id="CHANGED_fields_file_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_file_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_file_anyOf_i0)

- Type: string
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="tab-pane_CHANGED_fields_file_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_file_anyOf_i1)

- Type: null

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `KerberosKeytabRemovedEvent`
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
