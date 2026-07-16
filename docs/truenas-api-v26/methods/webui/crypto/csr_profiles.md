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

### Call parameters

- Type: array
- No Additional Items

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
#### HTTPS RSA Certificate

- Schema name: `RSACSRExtensions`
- Type: object

Certificate profile configuration for HTTPS RSA certificates.
- No Additional Properties
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
####### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the basic constraints extension is enabled.

####### ca

- Schema name: `Ca`
- Type: boolean
- Default: false

Whether this certificate can act as a certificate authority.

####### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: true

Whether this extension is marked as critical.

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
####### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the extended key usage extension is enabled.

####### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: true

Whether this extension is marked as critical.

####### usages

- Schema name: `Usages`
- Type: array of string
- Default: ["SERVER_AUTH", "CLIENT_AUTH"]

Array of extended key usage purposes for the certificate.
- No Additional Items

######## Each item of this array must be:

- Type: string

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
####### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the key usage extension is enabled.

####### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: true

Whether this extension is marked as critical.

####### digital_signature

- Schema name: `Digital Signature`
- Type: boolean
- Default: true

Whether the key can be used for digital signatures.

####### key_encipherment

- Schema name: `Key Encipherment`
- Type: boolean
- Default: true

Whether the key can be used for key encipherment.

####### key_agreement

- Schema name: `Key Agreement`
- Type: boolean
- Default: true

Whether the key can be used for key agreement.

##### key_length

- Schema name: `Key Length`
- Type: integer
- Default: 2048

RSA key length in bits.

##### key_type

- Schema name: `Key Type`
- Type: string
- Default: "RSA"

Type of cryptographic key (RSA).

##### lifetime

- Schema name: `Lifetime`
- Type: integer
- Default: 397

Certificate validity period in days.

##### digest_algorithm

- Schema name: `Digest Algorithm`
- Type: string
- Default: "SHA256"

Hash algorithm for certificate signing.

#### HTTPS ECC Certificate

- Schema name: `ECCCSRExtensions`
- Type: object

Certificate profile configuration for HTTPS ECC certificates.
- No Additional Properties
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
####### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the basic constraints extension is enabled.

####### ca

- Schema name: `Ca`
- Type: boolean
- Default: false

Whether this certificate can act as a certificate authority.

####### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: true

Whether this extension is marked as critical.

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
####### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the extended key usage extension is enabled.

####### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: true

Whether this extension is marked as critical.

####### usages

- Schema name: `Usages`
- Type: array of string
- Default: ["SERVER_AUTH", "CLIENT_AUTH"]

Array of extended key usage purposes for the certificate.
- No Additional Items

######## Each item of this array must be:

- Type: string

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
####### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the key usage extension is enabled.

####### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: true

Whether this extension is marked as critical.

####### digital_signature

- Schema name: `Digital Signature`
- Type: boolean
- Default: true

Whether the key can be used for digital signatures.

##### ec_curve

- Schema name: `Ec Curve`
- Type: string
- Default: "SECP384R1"

Elliptic curve to use for key generation.

##### key_type

- Schema name: `Key Type`
- Type: string
- Default: "EC"

Type of cryptographic key (ECC).

##### lifetime

- Schema name: `Lifetime`
- Type: integer
- Default: 397

Certificate validity period in days.

##### digest_algorithm

- Schema name: `Digest Algorithm`
- Type: string
- Default: "SHA256"

Hash algorithm for certificate signing.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
