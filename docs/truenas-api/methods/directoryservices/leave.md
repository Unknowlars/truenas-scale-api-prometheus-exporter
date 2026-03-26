---
title: directoryservices.leave
kind: method
source_rst: _sources/api_methods_directoryservices.leave.rst.txt
source_html: api_methods_directoryservices.leave.html
required_roles:
  - DIRECTORY_SERVICE_WRITE
---

# directoryservices.leave

## Summary

Leave an Active Directory or IPA domain. Calling this endpoint when the directory services status is `HEALTHY` will cause TrueNAS to remove its account from the domain and then reset the local directory services configuration on TrueNAS.

This method is a job.

## Required Roles

- `DIRECTORY_SERVICE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: credential

#### credential

- Schema name: `credential`
- Type: object

DirectoryServicesLeaveArgs parameters.
- No Additional Properties
##### credential (required)

- Schema name: `CredKRBUser`
- Type: object

Kerberos user credentials with administrative privileges to leave the domain.
- No Additional Properties
###### credential_type (required)

- Schema name: `Credential Type`
- Type: const

Credential type identifier for Kerberos user authentication.

###### username (required)

- Schema name: `Username`
- Type: string

Username of the account to use to create a kerberos ticket for authentication to directory services. This account must exist on the domain controller.
- Must be at least `1` characters long

###### password (required)

- Schema name: `Password`
- Type: string

The password for the user account that will obtain the kerberos ticket.
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
