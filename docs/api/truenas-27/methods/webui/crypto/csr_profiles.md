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

Return predefined CSR profiles for common certificate types.

Each profile provides recommended defaults for key type, key length or curve, lifetime, digest algorithm, and X.509 extensions (basic constraints, key usage, extended key usage).

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
  "HTTPS RSA Certificate": {
    "cert_extensions": {
      "BasicConstraints": {
        "ca": false,
        "enabled": true,
        "extension_critical": true
      },
      "ExtendedKeyUsage": {
        "enabled": true,
        "extension_critical": true,
        "usages": [
          "SERVER_AUTH",
          "CLIENT_AUTH"
        ]
      },
      "KeyUsage": {
        "digital_signature": true,
        "enabled": true,
        "extension_critical": true,
        "key_agreement": true,
        "key_encipherment": true
      }
    },
    "digest_algorithm": "SHA256",
    "key_length": 2048,
    "key_type": "RSA",
    "lifetime": 397
  },
  "HTTPS ECC Certificate": {
    "cert_extensions": {
      "BasicConstraints": {
        "ca": false,
        "enabled": true,
        "extension_critical": true
      },
      "ExtendedKeyUsage": {
        "enabled": true,
        "extension_critical": true,
        "usages": [
          "SERVER_AUTH",
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
    "key_type": "EC",
    "lifetime": 397
  }
}
```

Predefined certificate profiles for common use cases.
- No Additional Properties
<a id="headingReturn_value_HTTPS_RSA_Certificate"></a>
<a id="Return_value_HTTPS_RSA_Certificate"></a>
#### HTTPS RSA Certificate

- Schema name: `RSACSRExtensions`
- Type: object

Certificate profile configuration for HTTPS RSA certificates.
- No Additional Properties
<a id="headingReturn_value_HTTPS_RSA_Certificate_cert_extensions"></a>
<a id="Return_value_HTTPS_RSA_Certificate_cert_extensions"></a>
##### cert_extensions

- Schema name: `RSACSRExtensionsModel`
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
    "extension_critical": true,
    "usages": [
      "SERVER_AUTH",
      "CLIENT_AUTH"
    ]
  },
  "KeyUsage": {
    "digital_signature": true,
    "enabled": true,
    "extension_critical": true,
    "key_agreement": true,
    "key_encipherment": true
  }
}
```

Certificate extensions configuration for RSA certificates.
- No Additional Properties
<a id="headingReturn_value_HTTPS_RSA_Certificate_cert_extensions_BasicConstraints"></a>
<a id="Return_value_HTTPS_RSA_Certificate_cert_extensions_BasicConstraints"></a>
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
<a id="headingReturn_value_HTTPS_RSA_Certificate_cert_extensions_BasicConstraints_enabled"></a>
<a id="Return_value_HTTPS_RSA_Certificate_cert_extensions_BasicConstraints_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the basic constraints extension is enabled.

<a id="headingReturn_value_HTTPS_RSA_Certificate_cert_extensions_BasicConstraints_ca"></a>
<a id="Return_value_HTTPS_RSA_Certificate_cert_extensions_BasicConstraints_ca"></a>
###### ca

- Schema name: `Ca`
- Type: boolean
- Default: false

Whether this certificate can act as a certificate authority.

<a id="headingReturn_value_HTTPS_RSA_Certificate_cert_extensions_BasicConstraints_extension_critical"></a>
<a id="Return_value_HTTPS_RSA_Certificate_cert_extensions_BasicConstraints_extension_critical"></a>
###### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: true

Whether this extension is marked as critical.

<a id="headingReturn_value_HTTPS_RSA_Certificate_cert_extensions_ExtendedKeyUsage"></a>
<a id="Return_value_HTTPS_RSA_Certificate_cert_extensions_ExtendedKeyUsage"></a>
###### ExtendedKeyUsage

- Schema name: `ExtendedKeyUsageModel`
- Type: object
- Default:
```json
{
  "enabled": true,
  "extension_critical": true,
  "usages": [
    "SERVER_AUTH",
    "CLIENT_AUTH"
  ]
}
```

Extended key usage extension configuration.
- No Additional Properties
<a id="headingReturn_value_HTTPS_RSA_Certificate_cert_extensions_ExtendedKeyUsage_enabled"></a>
<a id="Return_value_HTTPS_RSA_Certificate_cert_extensions_ExtendedKeyUsage_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the extended key usage extension is enabled.

<a id="headingReturn_value_HTTPS_RSA_Certificate_cert_extensions_ExtendedKeyUsage_extension_critical"></a>
<a id="Return_value_HTTPS_RSA_Certificate_cert_extensions_ExtendedKeyUsage_extension_critical"></a>
###### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: true

Whether this extension is marked as critical.

<a id="headingReturn_value_HTTPS_RSA_Certificate_cert_extensions_ExtendedKeyUsage_usages"></a>
<a id="Return_value_HTTPS_RSA_Certificate_cert_extensions_ExtendedKeyUsage_usages"></a>
###### usages

- Schema name: `Usages`
- Type: array of string
- Default: ["SERVER_AUTH", "CLIENT_AUTH"]

Array of extended key usage purposes for the certificate.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_HTTPS_RSA_Certificate_cert_extensions_ExtendedKeyUsage_usages_items"></a>
- Type: string

<a id="headingReturn_value_HTTPS_RSA_Certificate_cert_extensions_KeyUsage"></a>
<a id="Return_value_HTTPS_RSA_Certificate_cert_extensions_KeyUsage"></a>
###### KeyUsage

- Schema name: `RSAKeyUsageModel`
- Type: object
- Default:
```json
{
  "enabled": true,
  "extension_critical": true,
  "digital_signature": true,
  "key_encipherment": true,
  "key_agreement": true
}
```

Key usage extension configuration for RSA certificates.
- No Additional Properties
<a id="headingReturn_value_HTTPS_RSA_Certificate_cert_extensions_KeyUsage_enabled"></a>
<a id="Return_value_HTTPS_RSA_Certificate_cert_extensions_KeyUsage_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the key usage extension is enabled.

<a id="headingReturn_value_HTTPS_RSA_Certificate_cert_extensions_KeyUsage_extension_critical"></a>
<a id="Return_value_HTTPS_RSA_Certificate_cert_extensions_KeyUsage_extension_critical"></a>
###### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: true

Whether this extension is marked as critical.

<a id="headingReturn_value_HTTPS_RSA_Certificate_cert_extensions_KeyUsage_digital_signature"></a>
<a id="Return_value_HTTPS_RSA_Certificate_cert_extensions_KeyUsage_digital_signature"></a>
###### digital_signature

- Schema name: `Digital Signature`
- Type: boolean
- Default: true

Whether the key can be used for digital signatures.

<a id="headingReturn_value_HTTPS_RSA_Certificate_cert_extensions_KeyUsage_key_encipherment"></a>
<a id="Return_value_HTTPS_RSA_Certificate_cert_extensions_KeyUsage_key_encipherment"></a>
###### key_encipherment

- Schema name: `Key Encipherment`
- Type: boolean
- Default: true

Whether the key can be used for key encipherment.

<a id="headingReturn_value_HTTPS_RSA_Certificate_cert_extensions_KeyUsage_key_agreement"></a>
<a id="Return_value_HTTPS_RSA_Certificate_cert_extensions_KeyUsage_key_agreement"></a>
###### key_agreement

- Schema name: `Key Agreement`
- Type: boolean
- Default: true

Whether the key can be used for key agreement.

<a id="headingReturn_value_HTTPS_RSA_Certificate_key_length"></a>
<a id="Return_value_HTTPS_RSA_Certificate_key_length"></a>
##### key_length

- Schema name: `Key Length`
- Type: integer
- Default: 2048

RSA key length in bits.

<a id="headingReturn_value_HTTPS_RSA_Certificate_key_type"></a>
<a id="Return_value_HTTPS_RSA_Certificate_key_type"></a>
##### key_type

- Schema name: `Key Type`
- Type: string
- Default: "RSA"

Type of cryptographic key (RSA).

<a id="headingReturn_value_HTTPS_RSA_Certificate_lifetime"></a>
<a id="Return_value_HTTPS_RSA_Certificate_lifetime"></a>
##### lifetime

- Schema name: `Lifetime`
- Type: integer
- Default: 397

Certificate validity period in days.

<a id="headingReturn_value_HTTPS_RSA_Certificate_digest_algorithm"></a>
<a id="Return_value_HTTPS_RSA_Certificate_digest_algorithm"></a>
##### digest_algorithm

- Schema name: `Digest Algorithm`
- Type: string
- Default: "SHA256"

Hash algorithm for certificate signing.

<a id="headingReturn_value_HTTPS_ECC_Certificate"></a>
<a id="Return_value_HTTPS_ECC_Certificate"></a>
#### HTTPS ECC Certificate

- Schema name: `ECCCSRExtensions`
- Type: object

Certificate profile configuration for HTTPS ECC certificates.
- No Additional Properties
<a id="headingReturn_value_HTTPS_ECC_Certificate_cert_extensions"></a>
<a id="Return_value_HTTPS_ECC_Certificate_cert_extensions"></a>
##### cert_extensions

- Schema name: `ECCCSRExtensionsModel`
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
    "extension_critical": true,
    "usages": [
      "SERVER_AUTH",
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

Certificate extensions configuration for ECC certificates.
- No Additional Properties
<a id="headingReturn_value_HTTPS_ECC_Certificate_cert_extensions_BasicConstraints"></a>
<a id="Return_value_HTTPS_ECC_Certificate_cert_extensions_BasicConstraints"></a>
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
<a id="headingReturn_value_HTTPS_ECC_Certificate_cert_extensions_BasicConstraints_enabled"></a>
<a id="Return_value_HTTPS_ECC_Certificate_cert_extensions_BasicConstraints_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the basic constraints extension is enabled.

<a id="headingReturn_value_HTTPS_ECC_Certificate_cert_extensions_BasicConstraints_ca"></a>
<a id="Return_value_HTTPS_ECC_Certificate_cert_extensions_BasicConstraints_ca"></a>
###### ca

- Schema name: `Ca`
- Type: boolean
- Default: false

Whether this certificate can act as a certificate authority.

<a id="headingReturn_value_HTTPS_ECC_Certificate_cert_extensions_BasicConstraints_extension_critical"></a>
<a id="Return_value_HTTPS_ECC_Certificate_cert_extensions_BasicConstraints_extension_critical"></a>
###### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: true

Whether this extension is marked as critical.

<a id="headingReturn_value_HTTPS_ECC_Certificate_cert_extensions_ExtendedKeyUsage"></a>
<a id="Return_value_HTTPS_ECC_Certificate_cert_extensions_ExtendedKeyUsage"></a>
###### ExtendedKeyUsage

- Schema name: `ExtendedKeyUsageModel`
- Type: object
- Default:
```json
{
  "enabled": true,
  "extension_critical": true,
  "usages": [
    "SERVER_AUTH",
    "CLIENT_AUTH"
  ]
}
```

Extended key usage extension configuration.
- No Additional Properties
<a id="headingReturn_value_HTTPS_ECC_Certificate_cert_extensions_ExtendedKeyUsage_enabled"></a>
<a id="Return_value_HTTPS_ECC_Certificate_cert_extensions_ExtendedKeyUsage_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the extended key usage extension is enabled.

<a id="headingReturn_value_HTTPS_ECC_Certificate_cert_extensions_ExtendedKeyUsage_extension_critical"></a>
<a id="Return_value_HTTPS_ECC_Certificate_cert_extensions_ExtendedKeyUsage_extension_critical"></a>
###### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: true

Whether this extension is marked as critical.

<a id="headingReturn_value_HTTPS_ECC_Certificate_cert_extensions_ExtendedKeyUsage_usages"></a>
<a id="Return_value_HTTPS_ECC_Certificate_cert_extensions_ExtendedKeyUsage_usages"></a>
###### usages

- Schema name: `Usages`
- Type: array of string
- Default: ["SERVER_AUTH", "CLIENT_AUTH"]

Array of extended key usage purposes for the certificate.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_HTTPS_ECC_Certificate_cert_extensions_ExtendedKeyUsage_usages_items"></a>
- Type: string

<a id="headingReturn_value_HTTPS_ECC_Certificate_cert_extensions_KeyUsage"></a>
<a id="Return_value_HTTPS_ECC_Certificate_cert_extensions_KeyUsage"></a>
###### KeyUsage

- Schema name: `ECCKeyUsageModel`
- Type: object
- Default:
```json
{
  "enabled": true,
  "extension_critical": true,
  "digital_signature": true
}
```

Key usage extension configuration for ECC certificates.
- No Additional Properties
<a id="headingReturn_value_HTTPS_ECC_Certificate_cert_extensions_KeyUsage_enabled"></a>
<a id="Return_value_HTTPS_ECC_Certificate_cert_extensions_KeyUsage_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the key usage extension is enabled.

<a id="headingReturn_value_HTTPS_ECC_Certificate_cert_extensions_KeyUsage_extension_critical"></a>
<a id="Return_value_HTTPS_ECC_Certificate_cert_extensions_KeyUsage_extension_critical"></a>
###### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: true

Whether this extension is marked as critical.

<a id="headingReturn_value_HTTPS_ECC_Certificate_cert_extensions_KeyUsage_digital_signature"></a>
<a id="Return_value_HTTPS_ECC_Certificate_cert_extensions_KeyUsage_digital_signature"></a>
###### digital_signature

- Schema name: `Digital Signature`
- Type: boolean
- Default: true

Whether the key can be used for digital signatures.

<a id="headingReturn_value_HTTPS_ECC_Certificate_ec_curve"></a>
<a id="Return_value_HTTPS_ECC_Certificate_ec_curve"></a>
##### ec_curve

- Schema name: `Ec Curve`
- Type: string
- Default: "SECP384R1"

Elliptic curve to use for key generation.

<a id="headingReturn_value_HTTPS_ECC_Certificate_key_type"></a>
<a id="Return_value_HTTPS_ECC_Certificate_key_type"></a>
##### key_type

- Schema name: `Key Type`
- Type: string
- Default: "EC"

Type of cryptographic key (ECC).

<a id="headingReturn_value_HTTPS_ECC_Certificate_lifetime"></a>
<a id="Return_value_HTTPS_ECC_Certificate_lifetime"></a>
##### lifetime

- Schema name: `Lifetime`
- Type: integer
- Default: 397

Certificate validity period in days.

<a id="headingReturn_value_HTTPS_ECC_Certificate_digest_algorithm"></a>
<a id="Return_value_HTTPS_ECC_Certificate_digest_algorithm"></a>
##### digest_algorithm

- Schema name: `Digest Algorithm`
- Type: string
- Default: "SHA256"

Hash algorithm for certificate signing.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
