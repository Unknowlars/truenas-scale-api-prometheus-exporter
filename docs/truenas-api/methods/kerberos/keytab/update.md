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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the Kerberos keytab entry to update.

#### Parameter 2: data

#### data

- Schema name: `data`
- Type: object

Updated Kerberos keytab configuration data.
- No Additional Properties
##### name

- Schema name: `Name`
- Type: string

Name of the kerberos keytab entry. This is an identifier for the keytab and not the name of the keytab file. Some names are used for internal purposes such as AD*MACHINE*ACCOUNT and IPA*MACHINE*ACCOUNT.
- Must be at least `1` characters long

##### file

- Schema name: `File`

Base64 encoded kerberos keytab entries to append to the system keytab.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

### Return value

- Schema name: `KerberosKeytabEntry`
- Type: object

The updated Kerberos keytab entry.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Kerberos keytab entry.

#### name (required)

- Schema name: `Name`
- Type: string

Name of the kerberos keytab entry. This is an identifier for the keytab and not the name of the keytab file. Some names are used for internal purposes such as AD*MACHINE*ACCOUNT and IPA*MACHINE*ACCOUNT.
- Must be at least `1` characters long

#### file (required)

- Schema name: `File`

Base64 encoded kerberos keytab entries to append to the system keytab.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
