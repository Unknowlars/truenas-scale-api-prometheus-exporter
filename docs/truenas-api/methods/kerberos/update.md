---
title: kerberos.update
kind: method
source_rst: _sources/api_methods_kerberos.update.rst.txt
source_html: api_methods_kerberos.update.html
required_roles:
  - DIRECTORY_SERVICE_WRITE
---

# kerberos.update

## Summary

`appdefaults_aux` add parameters to "appdefaults" section of the krb5.conf file.

`libdefaults_aux` add parameters to "libdefaults" section of the krb5.conf file.

## Required Roles

- `DIRECTORY_SERVICE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: kerberos_update

#### kerberos_update

- Schema name: `kerberos_update`
- Type: object

KerberosUpdateArgs parameters.
- No Additional Properties
##### appdefaults_aux

- Schema name: `Appdefaults Aux`
- Type: string

Advanced field for manually setting additional parameters inside the appdefaults section of the krb5.conf file. These are generally not required as the required krb5.conf settings are automatically detected and set for the environment. See manpage for MIT krb5.conf.

##### libdefaults_aux

- Schema name: `Libdefaults Aux`
- Type: string

Advanced field for manually setting additional parameters inside the libdefaults section of the krb5.conf file. These are generally not required as the required krb5.conf settings are automatically detected and set for the environment. See manpage for MIT krb5.conf.

### Return value

- Schema name: `KerberosEntry`
- Type: object

The updated Kerberos configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Kerberos configuration.

#### appdefaults_aux (required)

- Schema name: `Appdefaults Aux`
- Type: string

Advanced field for manually setting additional parameters inside the appdefaults section of the krb5.conf file. These are generally not required as the required krb5.conf settings are automatically detected and set for the environment. See manpage for MIT krb5.conf.

#### libdefaults_aux (required)

- Schema name: `Libdefaults Aux`
- Type: string

Advanced field for manually setting additional parameters inside the libdefaults section of the krb5.conf file. These are generally not required as the required krb5.conf settings are automatically detected and set for the environment. See manpage for MIT krb5.conf.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
