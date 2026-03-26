---
title: kerberos.config
kind: method
source_rst: _sources/api_methods_kerberos.config.rst.txt
source_html: api_methods_kerberos.config.html
required_roles:
  - DIRECTORY_SERVICE_READ
---

# kerberos.config

## Required Roles

- `DIRECTORY_SERVICE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `KerberosEntry`
- Type: object
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
