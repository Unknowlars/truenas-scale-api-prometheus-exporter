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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: credential

<a id="Call_parameters_items_i0"></a>
#### credential

- Schema name: `credential`
- Type: object

DirectoryServicesLeaveArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_credential"></a>
<a id="Call_parameters_items_i0_credential"></a>
##### credential (required)

- Schema name: `CredKRBUser`
- Type: object

Kerberos user credentials with administrative privileges to leave the domain.
- No Additional Properties
<a id="headingCall_parameters_items_i0_credential_credential_type"></a>
<a id="Call_parameters_items_i0_credential_credential_type"></a>
###### credential_type (required)

- Schema name: `Credential Type`
- Type: const

Credential type identifier for Kerberos user authentication.
- Specific value: `"KERBEROS_USER"`

<a id="headingCall_parameters_items_i0_credential_username"></a>
<a id="Call_parameters_items_i0_credential_username"></a>
###### username (required)

- Schema name: `Username`
- Type: string

Username of the account to use to create a kerberos ticket for authentication to directory services. This account must exist on the domain controller.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_credential_password"></a>
<a id="Call_parameters_items_i0_credential_password"></a>
###### password (required)

- Schema name: `Password`
- Type: string

The password for the user account that will obtain the kerberos ticket.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
