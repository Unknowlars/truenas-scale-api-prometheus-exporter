---
title: directoryservices.config
kind: method
source_rst: _sources/api_methods_directoryservices.config.rst.txt
source_html: api_methods_directoryservices.config.html
required_roles:
  - DIRECTORY_SERVICE_READ
---

# directoryservices.config

## Required Roles

- `DIRECTORY_SERVICE_READ`

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

- Schema name: `DirectoryServicesEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the directory services configuration.

<a id="headingReturn_value_service_type"></a>
<a id="Return_value_service_type"></a>
#### service_type (required)

- Schema name: `Service Type`

The pre-existing directory service type to which to bind TrueNAS. Select ACTIVEDIRECTORY to join an Active Directory domain. Select IPA to join a FreeIPA domain. Select LDAP to bind to one or more OpenLDAP-compatible servers.
<a id="Return_value_service_type_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_service_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_service_type_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "ACTIVEDIRECTORY"
- "IPA"
- "LDAP"

<a id="tab-pane_Return_value_service_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_service_type_anyOf_i1)

- Type: null

<a id="headingReturn_value_credential"></a>
<a id="Return_value_credential"></a>
#### credential (required)

- Schema name: `Credential`

Credential used to bind to the specified directory service. Kerberos credentials are required for Active Directory or IPA domains. Generic LDAP environments support various authentication methods. Available methods depend on the remote LDAP server configuration. If Kerberos credentials are selected for LDAP, GSSAPI binds replace plain LDAP binds. Use Kerberos or mutual TLS authentication when possible for better security. The following credential types are supported based on `service_type`: `ACTIVEDIRECTORY` service_type: `KERBEROS_USER` and `KERBEROS_PRINCIPAL`. `LDAP` service_type: `LDAP_PLAIN`, `LDAP_ANONYMOUS`, `LDAP_MTLS`, `KERBEROS_USER`, and `KERBEROS_PRINCIPAL`. NOTE: prior configuration of kerberos realm is required in order to use kerberos credentials with the `LDAP` `service_type`. `IPA` service_type: `KERBEROS_USER` and `KERBEROS_PRINCIPAL`. NOTE: `KERBEROS_USER` should be used when initially joining an IPA domain.
<a id="Return_value_credential_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_credential_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_credential_anyOf_i0)

<a id="Return_value_credential_anyOf_i0_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_credential_anyOf_i0_oneOf_i0"></a>
###### [CredKRBUser](#tab-pane_Return_value_credential_anyOf_i0_oneOf_i0)

- Schema name: `CredKRBUser`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credential_anyOf_i0_oneOf_i0_credential_type"></a>
<a id="Return_value_credential_anyOf_i0_oneOf_i0_credential_type"></a>
###### credential_type (required)

- Schema name: `Credential Type`
- Type: const

Credential type identifier for Kerberos user authentication.
- Specific value: `"KERBEROS_USER"`

<a id="headingReturn_value_credential_anyOf_i0_oneOf_i0_username"></a>
<a id="Return_value_credential_anyOf_i0_oneOf_i0_username"></a>
###### username (required)

- Schema name: `Username`
- Type: string

Username of the account to use to create a kerberos ticket for authentication to directory services. This account must exist on the domain controller.
- Must be at least `1` characters long

<a id="headingReturn_value_credential_anyOf_i0_oneOf_i0_password"></a>
<a id="Return_value_credential_anyOf_i0_oneOf_i0_password"></a>
###### password (required)

- Schema name: `Password`
- Type: string

The password for the user account that will obtain the kerberos ticket.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_credential_anyOf_i0_oneOf_i1"></a>
###### [CredKRBPrincipal](#tab-pane_Return_value_credential_anyOf_i0_oneOf_i1)

- Schema name: `CredKRBPrincipal`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credential_anyOf_i0_oneOf_i1_credential_type"></a>
<a id="Return_value_credential_anyOf_i0_oneOf_i1_credential_type"></a>
###### credential_type (required)

- Schema name: `Credential Type`
- Type: const

Credential type identifier for Kerberos principal authentication.
- Specific value: `"KERBEROS_PRINCIPAL"`

<a id="headingReturn_value_credential_anyOf_i0_oneOf_i1_principal"></a>
<a id="Return_value_credential_anyOf_i0_oneOf_i1_principal"></a>
###### principal (required)

- Schema name: `Principal`
- Type: string

A kerberos principal is a unique identity to which Kerberos can assign tickets. The specified kerberos principal must have an entry within a keytab on the TrueNAS server.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_credential_anyOf_i0_oneOf_i2"></a>
###### [CredLDAPPlain](#tab-pane_Return_value_credential_anyOf_i0_oneOf_i2)

- Schema name: `CredLDAPPlain`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credential_anyOf_i0_oneOf_i2_credential_type"></a>
<a id="Return_value_credential_anyOf_i0_oneOf_i2_credential_type"></a>
###### credential_type (required)

- Schema name: `Credential Type`
- Type: const

Credential type identifier for LDAP plain text authentication.
- Specific value: `"LDAP_PLAIN"`

<a id="headingReturn_value_credential_anyOf_i0_oneOf_i2_binddn"></a>
<a id="Return_value_credential_anyOf_i0_oneOf_i2_binddn"></a>
###### binddn (required)

- Schema name: `Binddn`
- Type: string

Distinguished name to use for LDAP authentication.

<a id="headingReturn_value_credential_anyOf_i0_oneOf_i2_bindpw"></a>
<a id="Return_value_credential_anyOf_i0_oneOf_i2_bindpw"></a>
###### bindpw (required)

- Schema name: `Bindpw`
- Type: string

Password for the bind DN used for LDAP authentication.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_credential_anyOf_i0_oneOf_i3"></a>
###### [CredLDAPAnonymous](#tab-pane_Return_value_credential_anyOf_i0_oneOf_i3)

- Schema name: `CredLDAPAnonymous`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credential_anyOf_i0_oneOf_i3_credential_type"></a>
<a id="Return_value_credential_anyOf_i0_oneOf_i3_credential_type"></a>
###### credential_type (required)

- Schema name: `Credential Type`
- Type: const

Anonymous LDAP authentication with no credentials required.
- Specific value: `"LDAP_ANONYMOUS"`

<a id="tab-pane_Return_value_credential_anyOf_i0_oneOf_i4"></a>
###### [CredLDAPMTLS](#tab-pane_Return_value_credential_anyOf_i0_oneOf_i4)

- Schema name: `CredLDAPMTLS`
- Type: object
- No Additional Properties
<a id="headingReturn_value_credential_anyOf_i0_oneOf_i4_credential_type"></a>
<a id="Return_value_credential_anyOf_i0_oneOf_i4_credential_type"></a>
###### credential_type (required)

- Schema name: `Credential Type`
- Type: const

Credential type identifier for LDAP mutual TLS authentication.
- Specific value: `"LDAP_MTLS"`

<a id="headingReturn_value_credential_anyOf_i0_oneOf_i4_client_certificate"></a>
<a id="Return_value_credential_anyOf_i0_oneOf_i4_client_certificate"></a>
###### client_certificate (required)

- Schema name: `Client Certificate`
- Type: string

The client certificate name used for mutual TLS authentication to the remote LDAP server.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_credential_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_credential_anyOf_i1)

- Type: null

Examples:

```json
{
    "binddn": "uid=truenasserver,ou=Users,dc=ldap01,dc=internal",
    "bindpw": "Canary",
    "credential_type": "LDAP_PLAIN"
}
```
Examples:

```json
{
    "credential_type": "LDAP_ANONYMOUS"
}
```
Examples:

```json
{
    "client_certificate": "ldap01_client_cert",
    "credential_type": "LDAP_MTLS"
}
```
Examples:

```json
{
    "credential_type": "KERBEROS_USER",
    "password": "Canary",
    "username": "truenas_user"
}
```
Examples:

```json
{
    "credential_type": "KERBEROS_PRINCIPAL",
    "principal": "truenas@LDAP01.INTERNAL"
}
```

<a id="headingReturn_value_enable"></a>
<a id="Return_value_enable"></a>
#### enable (required)

- Schema name: `Enable`
- Type: boolean

Enable the directory service. If TrueNAS has never joined the specified domain (IPA or Active Directory), setting this to True causes TrueNAS to attempt to join the domain. NOTE: The domain join process for Active Directory and IPA will make changes to the domain such as creating a new computer account for the TrueNAS server and creating DNS records for TrueNAS.

<a id="headingReturn_value_enable_account_cache"></a>
<a id="Return_value_enable_account_cache"></a>
#### enable_account_cache

- Schema name: `Enable Account Cache`
- Type: boolean
- Default: true

Enable backend caching for user and group lists. If enabled, then directory services users and groups will be presented as choices in the UI dropdowns and in API responses for user and group queries. This setting also controls whether users and groups appear in getent results. Disable this setting to reduce load on the directory server when necessary.

<a id="headingReturn_value_enable_dns_updates"></a>
<a id="Return_value_enable_dns_updates"></a>
#### enable_dns_updates

- Schema name: `Enable Dns Updates`
- Type: boolean
- Default: true

Enable automatic DNS updates for the TrueNAS server in the domain via nsupdate and gssapi / TSIG.

<a id="headingReturn_value_timeout"></a>
<a id="Return_value_timeout"></a>
#### timeout

- Schema name: `Timeout`
- Type: integer
- Default: 10

The timeout value for DNS queries that are performed as part of the join process and NETWORK_TIMEOUT for LDAP requests.
- Value must be greater or equal to `5` and lesser or equal to `60`

<a id="headingReturn_value_kerberos_realm"></a>
<a id="Return_value_kerberos_realm"></a>
#### kerberos_realm

- Schema name: `Kerberos Realm`
- Default: null

Name of kerberos realm used for authentication to the directory service. If set to null, then Kerberos is not used for binding to the directory service. When joining an Active Directory or IPA domain for the first time, the realm is detected and configured automatically if not specified.
<a id="Return_value_kerberos_realm_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_kerberos_realm_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_kerberos_realm_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_kerberos_realm_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_kerberos_realm_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration"></a>
<a id="Return_value_configuration"></a>
#### configuration

- Schema name: `Configuration`
- Default: null

The service_type specific configuration for the directory sevices plugin.
<a id="Return_value_configuration_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0)

<a id="Return_value_configuration_anyOf_i0_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0"></a>
###### [ActiveDirectoryConfig](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0)

- Schema name: `ActiveDirectoryConfig`
- Type: object
- No Additional Properties
<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_hostname"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_hostname"></a>
###### hostname (required)

- Schema name: `Hostname`
- Type: string

Hostname of TrueNAS server to register in Active Directory. Example: "truenasnyc".
- Must be at least `1` characters long

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_domain"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_domain"></a>
###### domain (required)

- Schema name: `Domain`
- Type: string

The full DNS domain name of the Active Directory domain. This must not be a domain controller. Example: "mydomain.internal".
- Must be at least `1` characters long

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap"></a>
###### idmap

- Schema name: `PrimaryDomainIdmap`
- Type: object
- Default:
```json
{
  "builtin": {
    "name": null,
    "range_high": 100000000,
    "range_low": 90000001
  },
  "idmap_domain": {
    "idmap_backend": "RID",
    "name": null,
    "range_high": 200000000,
    "range_low": 100000001,
    "sssd_compat": false
  }
}
```

Configuration for mapping Active Directory accounts to accounts on the TrueNAS server. The exact settings may vary based on other servers and Linux clients in the domain. Defaults are suitable for new deployments without existing support for unix-like operating systems.
- No Additional Properties
Examples:

```json
{
    "builtin": {
        "range_high": 100000000,
        "range_low": 90000001
    },
    "idmap_domain": {
        "idmap_backend": "RID",
        "name": "MYDOMAIN",
        "range_high": 200000000,
        "range_low": 100000001
    }
}
```
<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_builtin"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_builtin"></a>
###### builtin

- Schema name: `BuiltinDomainTdb`
- Type: object
- Default:
```json
{
  "name": null,
  "range_low": 90000001,
  "range_high": 100000000
}
```

UID and GID range configuration for automatically generated accounts linked to well-known and BUILTIN accounts on Windows servers.
- No Additional Properties
<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_builtin_name"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_builtin_name"></a>
###### name

- Schema name: `Name`
- Default: null

Short name for the domain. This should match the NetBIOS domain name for Active Directory domains. It may be null if the domain is configured as the base idmap for Active Directory.
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_builtin_name_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_builtin_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_builtin_name_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_builtin_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_builtin_name_anyOf_i1)

- Type: null

Examples:

```json
"IXDOM"
```

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_builtin_range_low"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_builtin_range_low"></a>
###### range_low

- Schema name: `Range Low`
- Type: integer
- Default: 90000001

The lowest UID or GID that the idmap backend can assign.
- Value must be greater or equal to `1000` and lesser or equal to `2147000000`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_builtin_range_high"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_builtin_range_high"></a>
###### range_high

- Schema name: `Range High`
- Type: integer
- Default: 100000000

The highest UID or GID that the idmap backend can assign.
- Value must be greater or equal to `1000` and lesser or equal to `2147000000`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain"></a>
###### idmap_domain

- Schema name: `Idmap Domain`
- Default:
```json
{
  "name": null,
  "range_low": 100000001,
  "range_high": 200000000,
  "idmap_backend": "RID",
  "sssd_compat": false
}
```

This configuration defines how domain accounts joined to TrueNAS are mapped to Unix UIDs and GIDs on the TrueNAS server. Most TrueNAS deployments use the RID backend, which algorithmically assigns UIDs and GIDs based on the Active Directory account SID. Another common option is the AD backend, which reads predefined Active Directory LDAP schema attributes that assign explicit UID and GID numbers to accounts.
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i0"></a>
###### [AD_Idmap](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i0)

- Schema name: `AD_Idmap`
- Type: object

The AD backend reads UID and GID mappings from an Active Directory server that uses pre-existing RFC2307 / SFU schema extensions. The administrator must add mappings for users and groups in Active Directory before use. NOTE: these schema extensions are not present by default in Active Directory.
- No Additional Properties
<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i0_name"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i0_name"></a>
###### name

- Schema name: `Name`
- Default: null

Short name for the domain. This should match the NetBIOS domain name for Active Directory domains. It may be null if the domain is configured as the base idmap for Active Directory.
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i0_name_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i0_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i0_name_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i0_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i0_name_anyOf_i1)

- Type: null

Examples:

```json
"IXDOM"
```

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i0_range_low"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i0_range_low"></a>
###### range_low

- Schema name: `Range Low`
- Type: integer
- Default: 100000001

The lowest UID or GID that the idmap backend can assign.
- Value must be greater or equal to `1000` and lesser or equal to `2147000000`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i0_range_high"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i0_range_high"></a>
###### range_high

- Schema name: `Range High`
- Type: integer
- Default: 200000000

The highest UID or GID that the idmap backend can assign.
- Value must be greater or equal to `1000` and lesser or equal to `2147000000`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i0_idmap_backend"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i0_idmap_backend"></a>
###### idmap_backend (required)

- Schema name: `Idmap Backend`
- Type: const

Idmap backend type identifier for Active Directory RFC2307 schema integration.
- Specific value: `"AD"`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i0_schema_mode"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i0_schema_mode"></a>
###### schema_mode (required)

- Schema name: `Schema Mode`
- Type: enum (of string)

The schema mode the idmap backend uses to query Active Directory for user and group information. The RFC2307 schema applies to Windows Server 2003 R2 and newer. The Services for Unix (SFU) schema applies to versions before Windows Server 2003 R2.
###### Must be one of:

- "RFC2307"
- "SFU"
- "SFU20"

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i0_unix_primary_group"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i0_unix_primary_group"></a>
###### unix_primary_group

- Schema name: `Unix Primary Group`
- Type: boolean
- Default: false

Defines if the user's primary group is fetched from SFU attributes or the Active Directory primary group. If True, the TrueNAS server uses the `gidNumber` LDAP attribute. If False, it uses the `primaryGroupID` LDAP attribute.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i0_unix_nss_info"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i0_unix_nss_info"></a>
###### unix_nss_info

- Schema name: `Unix Nss Info`
- Type: boolean
- Default: false

If True, the login shell and home directory are retrieved from LDAP attributes. If False, or if the Active Directory LDAP entry lacks SFU attributes, the home directory defaults to `/var/empty`.

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1"></a>
###### [LDAP_Idmap](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1)

- Schema name: `LDAP_Idmap`
- Type: object

The LDAP backend reads and writes UID / GID mapping tables from an external LDAP server.
- No Additional Properties
<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_name"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_name"></a>
###### name

- Schema name: `Name`
- Default: null

Short name for the domain. This should match the NetBIOS domain name for Active Directory domains. It may be null if the domain is configured as the base idmap for Active Directory.
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_name_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_name_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_name_anyOf_i1)

- Type: null

Examples:

```json
"IXDOM"
```

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_range_low"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_range_low"></a>
###### range_low

- Schema name: `Range Low`
- Type: integer
- Default: 100000001

The lowest UID or GID that the idmap backend can assign.
- Value must be greater or equal to `1000` and lesser or equal to `2147000000`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_range_high"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_range_high"></a>
###### range_high

- Schema name: `Range High`
- Type: integer
- Default: 200000000

The highest UID or GID that the idmap backend can assign.
- Value must be greater or equal to `1000` and lesser or equal to `2147000000`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_idmap_backend"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_idmap_backend"></a>
###### idmap_backend (required)

- Schema name: `Idmap Backend`
- Type: const

Idmap backend type identifier for external LDAP server mapping.
- Specific value: `"LDAP"`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_ldap_base_dn"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_ldap_base_dn"></a>
###### ldap_base_dn (required)

- Schema name: `Ldap Base Dn`
- Type: string

Directory base suffix to use for mapping UIDs and GIDs to SIDs.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_ldap_user_dn"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_ldap_user_dn"></a>
###### ldap_user_dn (required)

- Schema name: `Ldap User Dn`
- Type: string

Defines the user DN to be used for authentication to the LDAP server.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_ldap_user_dn_password"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_ldap_user_dn_password"></a>
###### ldap_user_dn_password (required)

- Schema name: `Ldap User Dn Password`
- Type: string

Secret to use for authenticating the user specified by `ldap_user_dn`.
- Must be at least `1` characters long

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_ldap_url"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_ldap_url"></a>
###### ldap_url (required)

- Schema name: `Ldap Url`
- Type: string

LDAP server to use for the idmap entries.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_readonly"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_readonly"></a>
###### readonly

- Schema name: `Readonly`
- Type: boolean
- Default: true

If readonly is set to True then TrueNAS will not attempt to write new idmap entries.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_validate_certificates"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i1_validate_certificates"></a>
###### validate_certificates

- Schema name: `Validate Certificates`
- Type: boolean
- Default: true

If False, TrueNAS does not validate certificates from the remote LDAP server. It is better to use valid certificates or import them into the TrueNAS server's trusted certificate store.

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2"></a>
###### [RFC2307_Idmap](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2)

- Schema name: `RFC2307_Idmap`
- Type: object

The RFC2307 backend reads ID mappings from RFC2307 attributes on a standalone LDAP server. This backend is read-only. Use the `AD` idmap backend if the server is an Active Directory domain controller.
- No Additional Properties
<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_name"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_name"></a>
###### name

- Schema name: `Name`
- Default: null

Short name for the domain. This should match the NetBIOS domain name for Active Directory domains. It may be null if the domain is configured as the base idmap for Active Directory.
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_name_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_name_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_name_anyOf_i1)

- Type: null

Examples:

```json
"IXDOM"
```

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_range_low"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_range_low"></a>
###### range_low

- Schema name: `Range Low`
- Type: integer
- Default: 100000001

The lowest UID or GID that the idmap backend can assign.
- Value must be greater or equal to `1000` and lesser or equal to `2147000000`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_range_high"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_range_high"></a>
###### range_high

- Schema name: `Range High`
- Type: integer
- Default: 200000000

The highest UID or GID that the idmap backend can assign.
- Value must be greater or equal to `1000` and lesser or equal to `2147000000`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_idmap_backend"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_idmap_backend"></a>
###### idmap_backend (required)

- Schema name: `Idmap Backend`
- Type: const

Idmap backend type identifier for RFC2307 LDAP attribute mapping.
- Specific value: `"RFC2307"`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_ldap_url"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_ldap_url"></a>
###### ldap_url (required)

- Schema name: `Ldap Url`
- Type: string

The LDAP URL used to access the LDAP server.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_ldap_user_dn"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_ldap_user_dn"></a>
###### ldap_user_dn (required)

- Schema name: `Ldap User Dn`
- Type: string

Defines the DN used to authenticate to the LDAP server.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_ldap_user_dn_password"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_ldap_user_dn_password"></a>
###### ldap_user_dn_password (required)

- Schema name: `Ldap User Dn Password`
- Type: string

The password used to authenticate the account specified in ldap*user*dn.
- Must be at least `1` characters long

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_bind_path_user"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_bind_path_user"></a>
###### bind_path_user (required)

- Schema name: `Bind Path User`
- Type: string

The search base that contains user objects in the LDAP server.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_bind_path_group"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_bind_path_group"></a>
###### bind_path_group (required)

- Schema name: `Bind Path Group`
- Type: string

The search base that contains group objects in the LDAP server.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_user_cn"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_user_cn"></a>
###### user_cn

- Schema name: `User Cn`
- Type: boolean
- Default: false

If set, query the CN attribute instead of the UID attribute for the user name in LDAP.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_ldap_realm"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_ldap_realm"></a>
###### ldap_realm

- Schema name: `Ldap Realm`
- Type: boolean
- Default: false

Append @realm to the CN for groups. Also append it to users if user_cn is specified.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_validate_certificates"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i2_validate_certificates"></a>
###### validate_certificates

- Schema name: `Validate Certificates`
- Type: boolean
- Default: true

If False, TrueNAS does not validate certificates from the remote LDAP server. It is better to use valid certificates or import them into the TrueNAS server's trusted certificate store.

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i3"></a>
###### [RID_Idmap](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i3)

- Schema name: `RID_Idmap`
- Type: object

The RID backend uses an algorithm to map UIDs and GIDs to SIDs. It determines the UID or GID by adding the RID value from the Windows Account SID to the base value in range_low. RID values in an Active Directory domain can be large, especially as the domain ages. Administrators should configure a range large enough to cover the current RID values assigned by the RID master. One way to do this is to check the RID of a recently created account in Active Directory. For example, if the RID is 500000, the range must include at least 500000 Unix IDs (for example, 1000000 to 2000000).
- No Additional Properties
<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i3_name"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i3_name"></a>
###### name

- Schema name: `Name`
- Default: null

Short name for the domain. This should match the NetBIOS domain name for Active Directory domains. It may be null if the domain is configured as the base idmap for Active Directory.
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i3_name_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i3_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i3_name_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i3_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i3_name_anyOf_i1)

- Type: null

Examples:

```json
"IXDOM"
```

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i3_range_low"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i3_range_low"></a>
###### range_low

- Schema name: `Range Low`
- Type: integer
- Default: 100000001

The lowest UID or GID that the idmap backend can assign.
- Value must be greater or equal to `1000` and lesser or equal to `2147000000`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i3_range_high"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i3_range_high"></a>
###### range_high

- Schema name: `Range High`
- Type: integer
- Default: 200000000

The highest UID or GID that the idmap backend can assign.
- Value must be greater or equal to `1000` and lesser or equal to `2147000000`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i3_idmap_backend"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i3_idmap_backend"></a>
###### idmap_backend (required)

- Schema name: `Idmap Backend`
- Type: const

Idmap backend type identifier for RID-based algorithmic mapping.
- Specific value: `"RID"`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i3_sssd_compat"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_idmap_idmap_domain_oneOf_i3_sssd_compat"></a>
###### sssd_compat

- Schema name: `Sssd Compat`
- Type: boolean
- Default: false

Generate an idmap low range using the algorithm from SSSD. This works if the domain uses only a single SSSD idmap slice, and is sufficient if the domain uses only a single SSSD idmap slice.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_site"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_site"></a>
###### site

- Schema name: `Site`
- Default: null

The Active Directory site where the TrueNAS server is located. TrueNAS detects this automatically during the domain join process.
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_site_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_site_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_site_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_site_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_site_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_computer_account_ou"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_computer_account_ou"></a>
###### computer_account_ou

- Schema name: `Computer Account Ou`
- Default: null

Use this setting to override the default organizational unit (OU) in which the TrueNAS computer account is created during the domain join. Use it to set a custom location for TrueNAS computer accounts.
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_computer_account_ou_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_computer_account_ou_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_computer_account_ou_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_computer_account_ou_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_computer_account_ou_anyOf_i1)

- Type: null

Examples:

```json
"TRUENAS_SERVERS/NYC"
```

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_use_default_domain"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_use_default_domain"></a>
###### use_default_domain

- Schema name: `Use Default Domain`
- Type: boolean
- Default: false

Controls if the system removes the domain prefix from Active Directory user and group names. If enabled, users appear as "administrator" instead of "EXAMPLE\administrator". In most cases, disable this (default) to avoid name conflicts between Active Directory and local accounts.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_enable_trusted_domains"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_enable_trusted_domains"></a>
###### enable_trusted_domains

- Schema name: `Enable Trusted Domains`
- Type: boolean
- Default: false

Enable support for trusted domains. If True, then separate trusted domain configuration must be set for all trusted domains.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains"></a>
###### trusted_domains

- Schema name: `Trusted Domains`
- Type: array
- Default: []

Configuration for trusted domains.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i0"></a>
###### [AD_Idmap](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i0)

- Schema name: `AD_Idmap`
- Type: object

The AD backend reads UID and GID mappings from an Active Directory server that uses pre-existing RFC2307 / SFU schema extensions. The administrator must add mappings for users and groups in Active Directory before use. NOTE: these schema extensions are not present by default in Active Directory.
- No Additional Properties
<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i0_name"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i0_name"></a>
###### name

- Schema name: `Name`
- Default: null

Short name for the domain. This should match the NetBIOS domain name for Active Directory domains. It may be null if the domain is configured as the base idmap for Active Directory.
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i0_name_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i0_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i0_name_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i0_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i0_name_anyOf_i1)

- Type: null

Examples:

```json
"IXDOM"
```

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i0_range_low"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i0_range_low"></a>
###### range_low

- Schema name: `Range Low`
- Type: integer
- Default: 100000001

The lowest UID or GID that the idmap backend can assign.
- Value must be greater or equal to `1000` and lesser or equal to `2147000000`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i0_range_high"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i0_range_high"></a>
###### range_high

- Schema name: `Range High`
- Type: integer
- Default: 200000000

The highest UID or GID that the idmap backend can assign.
- Value must be greater or equal to `1000` and lesser or equal to `2147000000`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i0_idmap_backend"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i0_idmap_backend"></a>
###### idmap_backend (required)

- Schema name: `Idmap Backend`
- Type: const

Idmap backend type identifier for Active Directory RFC2307 schema integration.
- Specific value: `"AD"`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i0_schema_mode"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i0_schema_mode"></a>
###### schema_mode (required)

- Schema name: `Schema Mode`
- Type: enum (of string)

The schema mode the idmap backend uses to query Active Directory for user and group information. The RFC2307 schema applies to Windows Server 2003 R2 and newer. The Services for Unix (SFU) schema applies to versions before Windows Server 2003 R2.
###### Must be one of:

- "RFC2307"
- "SFU"
- "SFU20"

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i0_unix_primary_group"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i0_unix_primary_group"></a>
###### unix_primary_group

- Schema name: `Unix Primary Group`
- Type: boolean
- Default: false

Defines if the user's primary group is fetched from SFU attributes or the Active Directory primary group. If True, the TrueNAS server uses the `gidNumber` LDAP attribute. If False, it uses the `primaryGroupID` LDAP attribute.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i0_unix_nss_info"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i0_unix_nss_info"></a>
###### unix_nss_info

- Schema name: `Unix Nss Info`
- Type: boolean
- Default: false

If True, the login shell and home directory are retrieved from LDAP attributes. If False, or if the Active Directory LDAP entry lacks SFU attributes, the home directory defaults to `/var/empty`.

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1"></a>
###### [LDAP_Idmap](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1)

- Schema name: `LDAP_Idmap`
- Type: object

The LDAP backend reads and writes UID / GID mapping tables from an external LDAP server.
- No Additional Properties
<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_name"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_name"></a>
###### name

- Schema name: `Name`
- Default: null

Short name for the domain. This should match the NetBIOS domain name for Active Directory domains. It may be null if the domain is configured as the base idmap for Active Directory.
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_name_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_name_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_name_anyOf_i1)

- Type: null

Examples:

```json
"IXDOM"
```

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_range_low"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_range_low"></a>
###### range_low

- Schema name: `Range Low`
- Type: integer
- Default: 100000001

The lowest UID or GID that the idmap backend can assign.
- Value must be greater or equal to `1000` and lesser or equal to `2147000000`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_range_high"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_range_high"></a>
###### range_high

- Schema name: `Range High`
- Type: integer
- Default: 200000000

The highest UID or GID that the idmap backend can assign.
- Value must be greater or equal to `1000` and lesser or equal to `2147000000`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_idmap_backend"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_idmap_backend"></a>
###### idmap_backend (required)

- Schema name: `Idmap Backend`
- Type: const

Idmap backend type identifier for external LDAP server mapping.
- Specific value: `"LDAP"`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_ldap_base_dn"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_ldap_base_dn"></a>
###### ldap_base_dn (required)

- Schema name: `Ldap Base Dn`
- Type: string

Directory base suffix to use for mapping UIDs and GIDs to SIDs.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_ldap_user_dn"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_ldap_user_dn"></a>
###### ldap_user_dn (required)

- Schema name: `Ldap User Dn`
- Type: string

Defines the user DN to be used for authentication to the LDAP server.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_ldap_user_dn_password"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_ldap_user_dn_password"></a>
###### ldap_user_dn_password (required)

- Schema name: `Ldap User Dn Password`
- Type: string

Secret to use for authenticating the user specified by `ldap_user_dn`.
- Must be at least `1` characters long

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_ldap_url"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_ldap_url"></a>
###### ldap_url (required)

- Schema name: `Ldap Url`
- Type: string

LDAP server to use for the idmap entries.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_readonly"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_readonly"></a>
###### readonly

- Schema name: `Readonly`
- Type: boolean
- Default: true

If readonly is set to True then TrueNAS will not attempt to write new idmap entries.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_validate_certificates"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i1_validate_certificates"></a>
###### validate_certificates

- Schema name: `Validate Certificates`
- Type: boolean
- Default: true

If False, TrueNAS does not validate certificates from the remote LDAP server. It is better to use valid certificates or import them into the TrueNAS server's trusted certificate store.

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2"></a>
###### [RFC2307_Idmap](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2)

- Schema name: `RFC2307_Idmap`
- Type: object

The RFC2307 backend reads ID mappings from RFC2307 attributes on a standalone LDAP server. This backend is read-only. Use the `AD` idmap backend if the server is an Active Directory domain controller.
- No Additional Properties
<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_name"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_name"></a>
###### name

- Schema name: `Name`
- Default: null

Short name for the domain. This should match the NetBIOS domain name for Active Directory domains. It may be null if the domain is configured as the base idmap for Active Directory.
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_name_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_name_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_name_anyOf_i1)

- Type: null

Examples:

```json
"IXDOM"
```

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_range_low"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_range_low"></a>
###### range_low

- Schema name: `Range Low`
- Type: integer
- Default: 100000001

The lowest UID or GID that the idmap backend can assign.
- Value must be greater or equal to `1000` and lesser or equal to `2147000000`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_range_high"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_range_high"></a>
###### range_high

- Schema name: `Range High`
- Type: integer
- Default: 200000000

The highest UID or GID that the idmap backend can assign.
- Value must be greater or equal to `1000` and lesser or equal to `2147000000`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_idmap_backend"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_idmap_backend"></a>
###### idmap_backend (required)

- Schema name: `Idmap Backend`
- Type: const

Idmap backend type identifier for RFC2307 LDAP attribute mapping.
- Specific value: `"RFC2307"`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_ldap_url"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_ldap_url"></a>
###### ldap_url (required)

- Schema name: `Ldap Url`
- Type: string

The LDAP URL used to access the LDAP server.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_ldap_user_dn"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_ldap_user_dn"></a>
###### ldap_user_dn (required)

- Schema name: `Ldap User Dn`
- Type: string

Defines the DN used to authenticate to the LDAP server.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_ldap_user_dn_password"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_ldap_user_dn_password"></a>
###### ldap_user_dn_password (required)

- Schema name: `Ldap User Dn Password`
- Type: string

The password used to authenticate the account specified in ldap*user*dn.
- Must be at least `1` characters long

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_bind_path_user"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_bind_path_user"></a>
###### bind_path_user (required)

- Schema name: `Bind Path User`
- Type: string

The search base that contains user objects in the LDAP server.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_bind_path_group"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_bind_path_group"></a>
###### bind_path_group (required)

- Schema name: `Bind Path Group`
- Type: string

The search base that contains group objects in the LDAP server.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_user_cn"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_user_cn"></a>
###### user_cn

- Schema name: `User Cn`
- Type: boolean
- Default: false

If set, query the CN attribute instead of the UID attribute for the user name in LDAP.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_ldap_realm"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_ldap_realm"></a>
###### ldap_realm

- Schema name: `Ldap Realm`
- Type: boolean
- Default: false

Append @realm to the CN for groups. Also append it to users if user_cn is specified.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_validate_certificates"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i2_validate_certificates"></a>
###### validate_certificates

- Schema name: `Validate Certificates`
- Type: boolean
- Default: true

If False, TrueNAS does not validate certificates from the remote LDAP server. It is better to use valid certificates or import them into the TrueNAS server's trusted certificate store.

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i3"></a>
###### [RID_Idmap](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i3)

- Schema name: `RID_Idmap`
- Type: object

The RID backend uses an algorithm to map UIDs and GIDs to SIDs. It determines the UID or GID by adding the RID value from the Windows Account SID to the base value in range_low. RID values in an Active Directory domain can be large, especially as the domain ages. Administrators should configure a range large enough to cover the current RID values assigned by the RID master. One way to do this is to check the RID of a recently created account in Active Directory. For example, if the RID is 500000, the range must include at least 500000 Unix IDs (for example, 1000000 to 2000000).
- No Additional Properties
<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i3_name"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i3_name"></a>
###### name

- Schema name: `Name`
- Default: null

Short name for the domain. This should match the NetBIOS domain name for Active Directory domains. It may be null if the domain is configured as the base idmap for Active Directory.
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i3_name_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i3_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i3_name_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i3_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i3_name_anyOf_i1)

- Type: null

Examples:

```json
"IXDOM"
```

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i3_range_low"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i3_range_low"></a>
###### range_low

- Schema name: `Range Low`
- Type: integer
- Default: 100000001

The lowest UID or GID that the idmap backend can assign.
- Value must be greater or equal to `1000` and lesser or equal to `2147000000`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i3_range_high"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i3_range_high"></a>
###### range_high

- Schema name: `Range High`
- Type: integer
- Default: 200000000

The highest UID or GID that the idmap backend can assign.
- Value must be greater or equal to `1000` and lesser or equal to `2147000000`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i3_idmap_backend"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i3_idmap_backend"></a>
###### idmap_backend (required)

- Schema name: `Idmap Backend`
- Type: const

Idmap backend type identifier for RID-based algorithmic mapping.
- Specific value: `"RID"`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i3_sssd_compat"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i0_trusted_domains_items_oneOf_i3_sssd_compat"></a>
###### sssd_compat

- Schema name: `Sssd Compat`
- Type: boolean
- Default: false

Generate an idmap low range using the algorithm from SSSD. This works if the domain uses only a single SSSD idmap slice, and is sufficient if the domain uses only a single SSSD idmap slice.

Examples:

```json
{
    "idmap_backend": "RID",
    "name": "BROOK",
    "range_high": 300000000,
    "range_low": 200000001
}
```
Examples:

```json
{
    "idmap_backend": "RID",
    "name": "DARVO",
    "range_high": 400000000,
    "range_low": 300000001
}
```

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i1"></a>
###### [IPAConfig](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i1)

- Schema name: `IPAConfig`
- Type: object
- No Additional Properties
<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i1_target_server"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i1_target_server"></a>
###### target_server (required)

- Schema name: `Target Server`
- Type: string

The name of the IPA server that TrueNAS uses to build URLs when it joins or leaves the IPA domain. Example: "ipa.example.internal".
- Must be at least `1` characters long

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i1_hostname"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i1_hostname"></a>
###### hostname (required)

- Schema name: `Hostname`
- Type: string

Hostname of TrueNAS server to register in IPA during the join process. Example: "truenasnyc".
- Must be at least `1` characters long

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i1_domain"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i1_domain"></a>
###### domain (required)

- Schema name: `Domain`
- Type: string

The domain of the IPA server. Example "ipa.internal".
- Must be at least `1` characters long

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i1_basedn"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i1_basedn"></a>
###### basedn (required)

- Schema name: `Basedn`
- Type: string

The base DN to use when performing LDAP operations. Example: "dc=example,dc=internal".

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i1_smb_domain"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain"></a>
###### smb_domain

- Default: null

Settings for the IPA SMB domain. TrueNAS detects these settings during IPA join. Some IPA domains may not include SMB schema configuration.
<a id="Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0"></a>
###### [IPA_SMBDomain](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0)

- Schema name: `IPA_SMBDomain`
- Type: object

This is a special idmap backend used when TrueNAS joins an IPA domain. The remote IPA server provides the configuration information during the domain join process.
- No Additional Properties
<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_name"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_name"></a>
###### name

- Schema name: `Name`
- Default: null

Short name for the domain. This should match the NetBIOS domain name for Active Directory domains. It may be null if the domain is configured as the base idmap for Active Directory.
<a id="Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_name_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_name_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_name_anyOf_i1)

- Type: null

Examples:

```json
"IXDOM"
```

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_range_low"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_range_low"></a>
###### range_low

- Schema name: `Range Low`
- Type: integer
- Default: 100000001

The lowest UID or GID that the idmap backend can assign.
- Value must be greater or equal to `1000` and lesser or equal to `2147000000`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_range_high"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_range_high"></a>
###### range_high

- Schema name: `Range High`
- Type: integer
- Default: 200000000

The highest UID or GID that the idmap backend can assign.
- Value must be greater or equal to `1000` and lesser or equal to `2147000000`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_idmap_backend"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_idmap_backend"></a>
###### idmap_backend (required)

- Schema name: `Idmap Backend`
- Type: const

Idmap backend type identifier for System Security Services Daemon integration.
- Specific value: `"SSS"`

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_domain_name"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_domain_name"></a>
###### domain_name

- Schema name: `Domain Name`
- Default: null

Name of the SMB domain as defined in the IPA configuration for the IPA domain to which TrueNAS is joined.
<a id="Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_domain_name_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_domain_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_domain_name_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_domain_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_domain_name_anyOf_i1)

- Type: null

Examples:

```json
"IXDOM.INTERNAL"
```

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_domain_sid"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_domain_sid"></a>
###### domain_sid

- Schema name: `Domain Sid`
- Default: null

The domain SID for the IPA domain to which TrueNAS is joined.
<a id="Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_domain_sid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_domain_sid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_domain_sid_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_domain_sid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i0_domain_sid_anyOf_i1)

- Type: null

Examples:

```json
"S-1-5-21-3696504179-2855309571-923743039"
```

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i1_smb_domain_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i1_validate_certificates"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i1_validate_certificates"></a>
###### validate_certificates

- Schema name: `Validate Certificates`
- Type: boolean
- Default: true

If `False`, TrueNAS does not validate certificates from the remote LDAP server. It is better to use valid certificates or import them into the TrueNAS server's trusted certificate store.

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2"></a>
###### [LDAPConfig](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2)

- Schema name: `LDAPConfig`
- Type: object
- No Additional Properties
<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_server_urls"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_server_urls"></a>
###### server_urls (required)

- Schema name: `Server Urls`
- Type: array of string

List of LDAP server URIs used for LDAP binds. Each URI must begin with ldap:// or ldaps:// and may use either a DNS name or an IP address. Example: `['ldaps://myldap.domain.internal']`.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_configuration_anyOf_i0_oneOf_i2_server_urls_items"></a>
- Type: string

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_basedn"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_basedn"></a>
###### basedn (required)

- Schema name: `Basedn`
- Type: string

The base DN to use when performing LDAP operations. Example: `"dc=domain,dc=internal"`.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_starttls"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_starttls"></a>
###### starttls

- Schema name: `Starttls`
- Type: boolean
- Default: false

Establish TLS by transmitting a StartTLS request to the server.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_validate_certificates"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_validate_certificates"></a>
###### validate_certificates

- Schema name: `Validate Certificates`
- Type: boolean
- Default: true

If `False`, TrueNAS does not validate certificates from the remote LDAP server. It is better to use valid certificates or import them into the TrueNAS server's trusted certificate store.

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_schema"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_schema"></a>
###### schema

- Schema name: `Schema`
- Type: enum (of string)
- Default: "RFC2307"

The type of LDAP attribute schema that the remote LDAP server uses.
###### Must be one of:

- "RFC2307"
- "RFC2307BIS"

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_search_bases"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_search_bases"></a>
###### search_bases

- Schema name: `LDAPSearchBases`
- Type: object
- Default:
```json
{
  "base_user": null,
  "base_group": null,
  "base_netgroup": null
}
```

Alternative LDAP search base settings. These settings define where to find user, group, and netgroup entries. If unspecified (the default), TrueNAS uses the `basedn` to find users. groups, and netgroups. Use these settings only if the LDAP server uses a non-standard LDAP schema or if you want to limit the accounts available on TrueNAS.
- No Additional Properties
<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_search_bases_base_user"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_search_bases_base_user"></a>
###### base_user

- Schema name: `Base User`
- Default: null

Optional base DN to limit LDAP user searches. If null (default) then the `base_dn` is used.
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_search_bases_base_user_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_search_bases_base_user_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_search_bases_base_user_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_search_bases_base_user_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_search_bases_base_user_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_search_bases_base_group"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_search_bases_base_group"></a>
###### base_group

- Schema name: `Base Group`
- Default: null

Optional base DN to limit LDAP group searches. If null (default) then the `base_dn` is used.
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_search_bases_base_group_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_search_bases_base_group_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_search_bases_base_group_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_search_bases_base_group_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_search_bases_base_group_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_search_bases_base_netgroup"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_search_bases_base_netgroup"></a>
###### base_netgroup

- Schema name: `Base Netgroup`
- Default: null

Optional base DN to limit LDAP netgroup searches. If null (default) then the `base_dn` is used.
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_search_bases_base_netgroup_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_search_bases_base_netgroup_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_search_bases_base_netgroup_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_search_bases_base_netgroup_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_search_bases_base_netgroup_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps"></a>
###### attribute_maps

- Schema name: `LDAPAttributeMaps`
- Type: object
- Default:
```json
{
  "passwd": {
    "user_gecos": null,
    "user_gid": null,
    "user_home_directory": null,
    "user_name": null,
    "user_object_class": null,
    "user_shell": null,
    "user_uid": null
  },
  "shadow": {
    "shadow_expire": null,
    "shadow_inactive": null,
    "shadow_last_change": null,
    "shadow_max": null,
    "shadow_min": null,
    "shadow_warning": null
  },
  "group": {
    "group_gid": null,
    "group_member": null,
    "group_object_class": null
  },
  "netgroup": {
    "netgroup_member": null,
    "netgroup_object_class": null,
    "netgroup_triple": null
  }
}
```

Optional LDAP attribute mapping for LDAP servers that do not follow RFC2307 or RFC2307BIS. Use this only if the LDAP server is non-standard.
- No Additional Properties
<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd"></a>
###### passwd

- Schema name: `LDAPMapPasswd`
- Type: object
- Default:
```json
{
  "user_object_class": null,
  "user_name": null,
  "user_uid": null,
  "user_gid": null,
  "user_gecos": null,
  "user_home_directory": null,
  "user_shell": null
}
```

LDAP attribute mappings for passwd/user entries.
- No Additional Properties
<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_object_class"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_object_class"></a>
###### user_object_class

- Schema name: `User Object Class`
- Default: null

The user entry object class in LDAP.
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_object_class_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_object_class_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_object_class_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_object_class_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_object_class_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_name"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_name"></a>
###### user_name

- Schema name: `User Name`
- Default: null

The LDAP attribute for the user's login name.
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_name_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_name_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_name_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_uid"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_uid"></a>
###### user_uid

- Schema name: `User Uid`
- Default: null

The LDAP attribute for the user's id.
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_uid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_uid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_uid_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_uid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_uid_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_gid"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_gid"></a>
###### user_gid

- Schema name: `User Gid`
- Default: null

The LDAP attribute for the user's primary group id.
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_gid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_gid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_gid_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_gid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_gid_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_gecos"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_gecos"></a>
###### user_gecos

- Schema name: `User Gecos`
- Default: null

The LDAP attribute for the user's gecos field.
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_gecos_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_gecos_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_gecos_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_gecos_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_gecos_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_home_directory"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_home_directory"></a>
###### user_home_directory

- Schema name: `User Home Directory`
- Default: null

The LDAP attribute for the user's home directory.
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_home_directory_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_home_directory_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_home_directory_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_home_directory_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_home_directory_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_shell"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_shell"></a>
###### user_shell

- Schema name: `User Shell`
- Default: null

The LDAP attribute for the path to the user's default shell.
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_shell_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_shell_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_shell_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_shell_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_passwd_user_shell_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow"></a>
###### shadow

- Schema name: `LDAPMapShadow`
- Type: object
- Default:
```json
{
  "shadow_last_change": null,
  "shadow_min": null,
  "shadow_max": null,
  "shadow_warning": null,
  "shadow_inactive": null,
  "shadow_expire": null
}
```

LDAP attribute mappings for shadow password entries.
- No Additional Properties
<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_last_change"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_last_change"></a>
###### shadow_last_change

- Schema name: `Shadow Last Change`
- Default: null

This parameter contains the name of an LDAP attribute for its shadow(5) counterpart (date of the last password change).
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_last_change_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_last_change_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_last_change_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_last_change_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_last_change_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_min"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_min"></a>
###### shadow_min

- Schema name: `Shadow Min`
- Default: null

This parameter contains the name of an LDAP attribute for its shadow(5) counterpart (minimum password age).
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_min_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_min_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_min_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_min_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_min_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_max"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_max"></a>
###### shadow_max

- Schema name: `Shadow Max`
- Default: null

This parameter contains the name of an LDAP attribute for its shadow(5) counterpart (maximum password age).
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_max_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_max_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_max_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_max_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_max_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_warning"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_warning"></a>
###### shadow_warning

- Schema name: `Shadow Warning`
- Default: null

This parameter contains the name of an LDAP attribute for its shadow(5) counterpart (password warning period).
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_warning_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_warning_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_warning_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_warning_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_warning_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_inactive"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_inactive"></a>
###### shadow_inactive

- Schema name: `Shadow Inactive`
- Default: null

This parameter contains the name of an LDAP attribute for its shadow(5) counterpart (password inactivity period).
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_inactive_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_inactive_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_inactive_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_inactive_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_inactive_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_expire"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_expire"></a>
###### shadow_expire

- Schema name: `Shadow Expire`
- Default: null

This parameter contains the name of an LDAP attribute for its shadow(5) counterpart (account expiration date).
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_expire_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_expire_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_expire_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_expire_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_shadow_shadow_expire_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group"></a>
###### group

- Schema name: `LDAPMapGroup`
- Type: object
- Default:
```json
{
  "group_object_class": null,
  "group_gid": null,
  "group_member": null
}
```

LDAP attribute mappings for group entries.
- No Additional Properties
<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group_group_object_class"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group_group_object_class"></a>
###### group_object_class

- Schema name: `Group Object Class`
- Default: null

The LDAP object class for group entries.
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group_group_object_class_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group_group_object_class_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group_group_object_class_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group_group_object_class_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group_group_object_class_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group_group_gid"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group_group_gid"></a>
###### group_gid

- Schema name: `Group Gid`
- Default: null

The LDAP attribute for the group's id.
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group_group_gid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group_group_gid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group_group_gid_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group_group_gid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group_group_gid_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group_group_member"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group_group_member"></a>
###### group_member

- Schema name: `Group Member`
- Default: null

The LDAP attribute for the names of the group's members.
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group_group_member_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group_group_member_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group_group_member_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group_group_member_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_group_group_member_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup"></a>
###### netgroup

- Schema name: `LDAPMapNetgroup`
- Type: object
- Default:
```json
{
  "netgroup_object_class": null,
  "netgroup_member": null,
  "netgroup_triple": null
}
```

LDAP attribute mappings for netgroup entries.
- No Additional Properties
<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup_netgroup_object_class"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup_netgroup_object_class"></a>
###### netgroup_object_class

- Schema name: `Netgroup Object Class`
- Default: null

The LDAP object class for netgroup entries.
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup_netgroup_object_class_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup_netgroup_object_class_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup_netgroup_object_class_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup_netgroup_object_class_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup_netgroup_object_class_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup_netgroup_member"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup_netgroup_member"></a>
###### netgroup_member

- Schema name: `Netgroup Member`
- Default: null

The LDAP attribute for the netgroup's members.
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup_netgroup_member_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup_netgroup_member_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup_netgroup_member_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup_netgroup_member_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup_netgroup_member_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup_netgroup_triple"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup_netgroup_triple"></a>
###### netgroup_triple

- Schema name: `Netgroup Triple`
- Default: null

The LDAP attribute for netgroup triples (host, user, domain).
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup_netgroup_triple_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup_netgroup_triple_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup_netgroup_triple_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup_netgroup_triple_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_attribute_maps_netgroup_netgroup_triple_anyOf_i1)

- Type: null

<a id="headingReturn_value_configuration_anyOf_i0_oneOf_i2_auxiliary_parameters"></a>
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_auxiliary_parameters"></a>
###### auxiliary_parameters

- Schema name: `Auxiliary Parameters`
- Default: null

Additional paramaters to add to the SSSD configuration. WARNING: TrueNAS does not check the validity of these parameters. Incorrect values can cause production outages when they are applied or after an operating system upgrade.
<a id="Return_value_configuration_anyOf_i0_oneOf_i2_auxiliary_parameters_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_auxiliary_parameters_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_auxiliary_parameters_anyOf_i0)

- Type: string
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_auxiliary_parameters_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i0_oneOf_i2_auxiliary_parameters_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_configuration_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_configuration_anyOf_i1)

- Type: null

Examples:

```json
{
    "computer_account_ou": "TRUENAS_SERVERS",
    "domain": "ACME.INTERNAL",
    "hostname": "TRUENASZ356"
}
```
Examples:

```json
{
    "basedn": "dc=ipadom,dc=internal",
    "domain": "ipadom.internal",
    "hostname": "TRUENASZ345",
    "target_server": "ipasrv5.ipadom.internal"
}
```
Examples:

```json
{
    "basedn": "dc=ipadom,dc=internal",
    "server_urls": [
        "ldap.ipadom.internal"
    ]
}
```

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
