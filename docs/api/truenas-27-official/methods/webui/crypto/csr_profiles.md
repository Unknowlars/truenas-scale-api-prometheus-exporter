---
title: webui.crypto.csr_profiles
kind: method
source_rst: _sources/api_methods_webui.crypto.csr_profiles.rst.txt
source_html: api_methods_webui.crypto.csr_profiles.html
required_roles:
  - CERTIFICATE_READ
---

# webui.crypto.csr_profiles

## Summary

Return predefined CSR profiles for common certificate roles.

There is a profile for each combination of role (a TLS server certificate, or a TLS client certificate used when TrueNAS authenticates itself to a remote service) and key type (RSA or EC). Each one provides recommended defaults for the key parameters, the digest algorithm, and the X.509 extensions (basic constraints, key usage, extended key usage).

The profiles are advisory: they are intended to prefill the CSR form and are not applied by [certificate.create](../../certificate/create.md), which must be passed these values explicitly.

## Required Roles

- `CERTIFICATE_READ`

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

- Schema name: `CSRProfilesModel`
- Type: object
- Default:
```json
{
  "TLS Server (e.g. Web UI, FTPS, Apps) - RSA": {
    "cert_extensions": {
      "BasicConstraints": {
        "ca": false,
        "enabled": true,
        "extension_critical": true
      },
      "ExtendedKeyUsage": {
        "enabled": true,
        "extension_critical": false,
        "usages": [
          "SERVER_AUTH"
        ]
      },
      "KeyUsage": {
        "digital_signature": true,
        "enabled": true,
        "extension_critical": true,
        "key_encipherment": true
      }
    },
    "digest_algorithm": "SHA256",
    "key_length": 2048,
    "key_type": "RSA"
  },
  "TLS Server (e.g. Web UI, FTPS, Apps) - EC": {
    "cert_extensions": {
      "BasicConstraints": {
        "ca": false,
        "enabled": true,
        "extension_critical": true
      },
      "ExtendedKeyUsage": {
        "enabled": true,
        "extension_critical": false,
        "usages": [
          "SERVER_AUTH"
        ]
      },
      "KeyUsage": {
        "digital_signature": true,
        "enabled": true,
        "extension_critical": true
      }
    },
    "digest_algorithm": "SHA256",
    "ec_curve": "SECP384R1",
    "key_type": "EC"
  },
  "TLS Client (e.g. Syslog, LDAP, KMIP) - RSA": {
    "cert_extensions": {
      "BasicConstraints": {
        "ca": false,
        "enabled": true,
        "extension_critical": true
      },
      "ExtendedKeyUsage": {
        "enabled": true,
        "extension_critical": false,
        "usages": [
          "CLIENT_AUTH"
        ]
      },
      "KeyUsage": {
        "digital_signature": true,
        "enabled": true,
        "extension_critical": true
      }
    },
    "digest_algorithm": "SHA256",
    "key_length": 2048,
    "key_type": "RSA"
  },
  "TLS Client (e.g. Syslog, LDAP, KMIP) - EC": {
    "cert_extensions": {
      "BasicConstraints": {
        "ca": false,
        "enabled": true,
        "extension_critical": true
      },
      "ExtendedKeyUsage": {
        "enabled": true,
        "extension_critical": false,
        "usages": [
          "CLIENT_AUTH"
        ]
      },
      "KeyUsage": {
        "digital_signature": true,
        "enabled": true,
        "extension_critical": true
      }
    },
    "digest_algorithm": "SHA256",
    "ec_curve": "SECP384R1",
    "key_type": "EC"
  }
}
```

Predefined certificate profiles for common use cases.
- No Additional Properties
<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA"></a>
#### TLS Server (e.g. Web UI, FTPS, Apps) - RSA

- Schema name: `TLSServerRSAProfile`
- Type: object

RSA certificate for services where TrueNAS accepts incoming TLS connections, such as the web UI, FTPS, and apps. Requests TLS Web Server Authentication only, which every public and ACME CA accepts.
- No Additional Properties
<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions"></a>
##### cert_extensions

- Schema name: `ServerRSACSRExtensionsModel`
- Type: object
- Default:
```json
{
  "BasicConstraints": {
    "ca": false,
    "enabled": true,
    "extension_critical": true
  },
  "ExtendedKeyUsage": {
    "enabled": true,
    "extension_critical": false,
    "usages": [
      "SERVER_AUTH"
    ]
  },
  "KeyUsage": {
    "digital_signature": true,
    "enabled": true,
    "extension_critical": true,
    "key_encipherment": true
  }
}
```

Certificate extensions configuration for RSA certificates.
- No Additional Properties
<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_BasicConstraints"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_BasicConstraints"></a>
###### BasicConstraints

- Schema name: `BasicConstraintsModel`
- Type: object
- Default:
```json
{
  "enabled": true,
  "ca": false,
  "extension_critical": true
}
```

Basic constraints extension configuration.
- No Additional Properties
<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_BasicConstraints_enabled"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_BasicConstraints_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the basic constraints extension is enabled.

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_BasicConstraints_ca"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_BasicConstraints_ca"></a>
###### ca

- Schema name: `Ca`
- Type: boolean
- Default: false

Whether this certificate can act as a certificate authority.

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_BasicConstraints_extension_critical"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_BasicConstraints_extension_critical"></a>
###### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: true

Whether this extension is marked as critical.

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_ExtendedKeyUsage"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_ExtendedKeyUsage"></a>
###### ExtendedKeyUsage

- Schema name: `ServerAuthExtendedKeyUsageModel`
- Type: object
- Default:
```json
{
  "enabled": true,
  "extension_critical": false,
  "usages": [
    "SERVER_AUTH"
  ]
}
```

Extended key usage extension configuration.
- No Additional Properties
<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_ExtendedKeyUsage_enabled"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_ExtendedKeyUsage_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the extended key usage extension is enabled.

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_ExtendedKeyUsage_extension_critical"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_ExtendedKeyUsage_extension_critical"></a>
###### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: false

Whether this extension is marked as critical.

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_ExtendedKeyUsage_usages"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_ExtendedKeyUsage_usages"></a>
###### usages

- Schema name: `Usages`
- Type: array of string

Array of extended key usage purposes for the certificate.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_ExtendedKeyUsage_usages_items"></a>
- Type: string

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_KeyUsage"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_KeyUsage"></a>
###### KeyUsage

- Schema name: `ServerRSAKeyUsageModel`
- Type: object
- Default:
```json
{
  "enabled": true,
  "extension_critical": true,
  "digital_signature": true,
  "key_encipherment": true
}
```

Key usage extension configuration for RSA certificates.
- No Additional Properties
<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_KeyUsage_enabled"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_KeyUsage_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the key usage extension is enabled.

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_KeyUsage_extension_critical"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_KeyUsage_extension_critical"></a>
###### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: true

Whether this extension is marked as critical.

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_KeyUsage_digital_signature"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_KeyUsage_digital_signature"></a>
###### digital_signature

- Schema name: `Digital Signature`
- Type: boolean
- Default: true

Whether the key can be used for digital signatures.

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_KeyUsage_key_encipherment"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_cert_extensions_KeyUsage_key_encipherment"></a>
###### key_encipherment

- Schema name: `Key Encipherment`
- Type: boolean
- Default: true

Whether the key can be used for key encipherment.

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_key_length"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_key_length"></a>
##### key_length

- Schema name: `Key Length`
- Type: integer
- Default: 2048

RSA key length in bits.

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_key_type"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_key_type"></a>
##### key_type

- Schema name: `Key Type`
- Type: string
- Default: "RSA"

Type of cryptographic key (RSA).

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_digest_algorithm"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_RSA_digest_algorithm"></a>
##### digest_algorithm

- Schema name: `Digest Algorithm`
- Type: string
- Default: "SHA256"

Hash algorithm for certificate signing.

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC"></a>
#### TLS Server (e.g. Web UI, FTPS, Apps) - EC

- Schema name: `TLSServerECProfile`
- Type: object

Elliptic curve certificate for services where TrueNAS accepts incoming TLS connections, such as the web UI, FTPS, and apps. Requests TLS Web Server Authentication only, which every public and ACME CA accepts.
- No Additional Properties
<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions"></a>
##### cert_extensions

- Schema name: `ServerECCSRExtensionsModel`
- Type: object
- Default:
```json
{
  "BasicConstraints": {
    "ca": false,
    "enabled": true,
    "extension_critical": true
  },
  "ExtendedKeyUsage": {
    "enabled": true,
    "extension_critical": false,
    "usages": [
      "SERVER_AUTH"
    ]
  },
  "KeyUsage": {
    "digital_signature": true,
    "enabled": true,
    "extension_critical": true
  }
}
```

Certificate extensions configuration for EC certificates.
- No Additional Properties
<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_BasicConstraints"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_BasicConstraints"></a>
###### BasicConstraints

- Schema name: `BasicConstraintsModel`
- Type: object
- Default:
```json
{
  "enabled": true,
  "ca": false,
  "extension_critical": true
}
```

Basic constraints extension configuration.
- No Additional Properties
<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_BasicConstraints_enabled"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_BasicConstraints_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the basic constraints extension is enabled.

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_BasicConstraints_ca"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_BasicConstraints_ca"></a>
###### ca

- Schema name: `Ca`
- Type: boolean
- Default: false

Whether this certificate can act as a certificate authority.

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_BasicConstraints_extension_critical"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_BasicConstraints_extension_critical"></a>
###### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: true

Whether this extension is marked as critical.

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_ExtendedKeyUsage"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_ExtendedKeyUsage"></a>
###### ExtendedKeyUsage

- Schema name: `ServerAuthExtendedKeyUsageModel`
- Type: object
- Default:
```json
{
  "enabled": true,
  "extension_critical": false,
  "usages": [
    "SERVER_AUTH"
  ]
}
```

Extended key usage extension configuration.
- No Additional Properties
<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_ExtendedKeyUsage_enabled"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_ExtendedKeyUsage_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the extended key usage extension is enabled.

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_ExtendedKeyUsage_extension_critical"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_ExtendedKeyUsage_extension_critical"></a>
###### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: false

Whether this extension is marked as critical.

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_ExtendedKeyUsage_usages"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_ExtendedKeyUsage_usages"></a>
###### usages

- Schema name: `Usages`
- Type: array of string

Array of extended key usage purposes for the certificate.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_ExtendedKeyUsage_usages_items"></a>
- Type: string

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_KeyUsage"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_KeyUsage"></a>
###### KeyUsage

- Schema name: `SigningKeyUsageModel`
- Type: object
- Default:
```json
{
  "enabled": true,
  "extension_critical": true,
  "digital_signature": true
}
```

Key usage extension configuration for EC certificates.
- No Additional Properties
<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_KeyUsage_enabled"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_KeyUsage_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the key usage extension is enabled.

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_KeyUsage_extension_critical"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_KeyUsage_extension_critical"></a>
###### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: true

Whether this extension is marked as critical.

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_KeyUsage_digital_signature"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_cert_extensions_KeyUsage_digital_signature"></a>
###### digital_signature

- Schema name: `Digital Signature`
- Type: boolean
- Default: true

Whether the key can be used for digital signatures.

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_ec_curve"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_ec_curve"></a>
##### ec_curve

- Schema name: `Ec Curve`
- Type: string
- Default: "SECP384R1"

Elliptic curve to use for key generation.

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_key_type"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_key_type"></a>
##### key_type

- Schema name: `Key Type`
- Type: string
- Default: "EC"

Type of cryptographic key (EC).

<a id="headingReturn_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_digest_algorithm"></a>
<a id="Return_value_TLS_Server_(eg_Web_UI,_FTPS,_Apps)_-_EC_digest_algorithm"></a>
##### digest_algorithm

- Schema name: `Digest Algorithm`
- Type: string
- Default: "SHA256"

Hash algorithm for certificate signing.

<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA"></a>
#### TLS Client (e.g. Syslog, LDAP, KMIP) - RSA

- Schema name: `TLSClientRSAProfile`
- Type: object

RSA certificate for services where TrueNAS connects out and must authenticate itself, such as remote syslog over TLS, LDAP mutual TLS, and KMIP. Requests TLS Web Client Authentication and is intended for a private CA.
- No Additional Properties
<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions"></a>
##### cert_extensions

- Schema name: `ClientCSRExtensionsModel`
- Type: object
- Default:
```json
{
  "BasicConstraints": {
    "ca": false,
    "enabled": true,
    "extension_critical": true
  },
  "ExtendedKeyUsage": {
    "enabled": true,
    "extension_critical": false,
    "usages": [
      "CLIENT_AUTH"
    ]
  },
  "KeyUsage": {
    "digital_signature": true,
    "enabled": true,
    "extension_critical": true
  }
}
```

Certificate extensions configuration for RSA certificates.
- No Additional Properties
<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_BasicConstraints"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_BasicConstraints"></a>
###### BasicConstraints

- Schema name: `BasicConstraintsModel`
- Type: object
- Default:
```json
{
  "enabled": true,
  "ca": false,
  "extension_critical": true
}
```

Basic constraints extension configuration.
- No Additional Properties
<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_BasicConstraints_enabled"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_BasicConstraints_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the basic constraints extension is enabled.

<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_BasicConstraints_ca"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_BasicConstraints_ca"></a>
###### ca

- Schema name: `Ca`
- Type: boolean
- Default: false

Whether this certificate can act as a certificate authority.

<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_BasicConstraints_extension_critical"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_BasicConstraints_extension_critical"></a>
###### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: true

Whether this extension is marked as critical.

<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_ExtendedKeyUsage"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_ExtendedKeyUsage"></a>
###### ExtendedKeyUsage

- Schema name: `ClientAuthExtendedKeyUsageModel`
- Type: object
- Default:
```json
{
  "enabled": true,
  "extension_critical": false,
  "usages": [
    "CLIENT_AUTH"
  ]
}
```

Extended key usage extension configuration.
- No Additional Properties
<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_ExtendedKeyUsage_enabled"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_ExtendedKeyUsage_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the extended key usage extension is enabled.

<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_ExtendedKeyUsage_extension_critical"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_ExtendedKeyUsage_extension_critical"></a>
###### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: false

Whether this extension is marked as critical.

<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_ExtendedKeyUsage_usages"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_ExtendedKeyUsage_usages"></a>
###### usages

- Schema name: `Usages`
- Type: array of string

Array of extended key usage purposes for the certificate.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_ExtendedKeyUsage_usages_items"></a>
- Type: string

<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_KeyUsage"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_KeyUsage"></a>
###### KeyUsage

- Schema name: `SigningKeyUsageModel`
- Type: object
- Default:
```json
{
  "enabled": true,
  "extension_critical": true,
  "digital_signature": true
}
```

Key usage extension configuration for client certificates.
- No Additional Properties
<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_KeyUsage_enabled"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_KeyUsage_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the key usage extension is enabled.

<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_KeyUsage_extension_critical"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_KeyUsage_extension_critical"></a>
###### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: true

Whether this extension is marked as critical.

<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_KeyUsage_digital_signature"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_cert_extensions_KeyUsage_digital_signature"></a>
###### digital_signature

- Schema name: `Digital Signature`
- Type: boolean
- Default: true

Whether the key can be used for digital signatures.

<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_key_length"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_key_length"></a>
##### key_length

- Schema name: `Key Length`
- Type: integer
- Default: 2048

RSA key length in bits.

<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_key_type"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_key_type"></a>
##### key_type

- Schema name: `Key Type`
- Type: string
- Default: "RSA"

Type of cryptographic key (RSA).

<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_digest_algorithm"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_RSA_digest_algorithm"></a>
##### digest_algorithm

- Schema name: `Digest Algorithm`
- Type: string
- Default: "SHA256"

Hash algorithm for certificate signing.

<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_EC"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_EC"></a>
#### TLS Client (e.g. Syslog, LDAP, KMIP) - EC

- Schema name: `TLSClientECProfile`
- Type: object

Elliptic curve certificate for services where TrueNAS connects out and must authenticate itself, such as remote syslog over TLS, LDAP mutual TLS, and KMIP. Requests TLS Web Client Authentication and is intended for a private CA.
- No Additional Properties
<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_EC_cert_extensions"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_EC_cert_extensions"></a>
##### cert_extensions

- Schema name: `ClientCSRExtensionsModel`
- Type: object
- Default:
```json
{
  "BasicConstraints": {
    "ca": false,
    "enabled": true,
    "extension_critical": true
  },
  "ExtendedKeyUsage": {
    "enabled": true,
    "extension_critical": false,
    "usages": [
      "CLIENT_AUTH"
    ]
  },
  "KeyUsage": {
    "digital_signature": true,
    "enabled": true,
    "extension_critical": true
  }
}
```

Certificate extensions configuration for EC certificates.
- No Additional Properties
<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_EC_cert_extensions_BasicConstraints"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_EC_cert_extensions_BasicConstraints"></a>
###### BasicConstraints

- Type: object
- Default:
```json
{
  "enabled": true,
  "ca": false,
  "extension_critical": true
}
```

Basic constraints extension configuration.

<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_EC_cert_extensions_ExtendedKeyUsage"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_EC_cert_extensions_ExtendedKeyUsage"></a>
###### ExtendedKeyUsage

- Type: object
- Default:
```json
{
  "enabled": true,
  "extension_critical": false,
  "usages": [
    "CLIENT_AUTH"
  ]
}
```

Extended key usage extension configuration.

<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_EC_cert_extensions_KeyUsage"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_EC_cert_extensions_KeyUsage"></a>
###### KeyUsage

- Type: object
- Default:
```json
{
  "enabled": true,
  "extension_critical": true,
  "digital_signature": true
}
```

Key usage extension configuration for client certificates.

<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_EC_ec_curve"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_EC_ec_curve"></a>
##### ec_curve

- Schema name: `Ec Curve`
- Type: string
- Default: "SECP384R1"

Elliptic curve to use for key generation.

<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_EC_key_type"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_EC_key_type"></a>
##### key_type

- Schema name: `Key Type`
- Type: string
- Default: "EC"

Type of cryptographic key (EC).

<a id="headingReturn_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_EC_digest_algorithm"></a>
<a id="Return_value_TLS_Client_(eg_Syslog,_LDAP,_KMIP)_-_EC_digest_algorithm"></a>
##### digest_algorithm

- Schema name: `Digest Algorithm`
- Type: string
- Default: "SHA256"

Hash algorithm for certificate signing.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
