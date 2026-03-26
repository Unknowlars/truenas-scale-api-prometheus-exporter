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

### ADDED

- Schema name: `KerberosKeytabAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `KerberosKeytabEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Kerberos keytab entry.

##### name (required)

- Schema name: `Name`
- Type: string

Name of the kerberos keytab entry. This is an identifier for the keytab and not the name of the keytab file. Some names are used for internal purposes such as AD*MACHINE*ACCOUNT and IPA*MACHINE*ACCOUNT.
- Must be at least `1` characters long

##### file (required)

- Schema name: `File`

Base64 encoded kerberos keytab entries to append to the system keytab.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

### CHANGED

- Schema name: `KerberosKeytabChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `KerberosKeytabEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Kerberos keytab entry.

##### name (required)

- Schema name: `Name`
- Type: string

Name of the kerberos keytab entry. This is an identifier for the keytab and not the name of the keytab file. Some names are used for internal purposes such as AD*MACHINE*ACCOUNT and IPA*MACHINE*ACCOUNT.
- Must be at least `1` characters long

##### file (required)

- Schema name: `File`

Base64 encoded kerberos keytab entries to append to the system keytab.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

### REMOVED

- Schema name: `KerberosKeytabRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
