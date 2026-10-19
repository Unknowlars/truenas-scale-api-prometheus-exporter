---
title: certificate.create
kind: method
source_rst: _sources/api_methods_certificate.create.rst.txt
source_html: api_methods_certificate.create.html
required_roles:
  - CERTIFICATE_WRITE
---

# certificate.create

## Summary

Create a new Certificate

Certificates are classified under following types and the necessary keywords to be passed for `create_type` attribute to create the respective type of certificate

1) Imported Certificate - CERTIFICATE_CREATE_IMPORTED

2) Certificate Signing Request - CERTIFICATE_CREATE_CSR

3) Imported Certificate Signing Request - CERTIFICATE_CREATE_IMPORTED_CSR

4) ACME Certificate - CERTIFICATE_CREATE_ACME

By default, created CSRs use RSA keys. If an Elliptic Curve Key is desired, it can be specified with the `key_type` attribute. If the `ec_curve` attribute is not specified for the Elliptic Curve Key, then default to using "SECP384R1" curve.

A type is selected by the Certificate Service based on `create_type`. The rest of the values in `data` are validated accordingly and finally a certificate is made based on the selected type.

`cert_extensions` can be specified to set X509v3 extensions.

.. examples(websocket)::

Create an ACME based certificate

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "certificate.create", "params": [{ "tos": true, "csr_id": 1, "acme_directory_uri": "https://acme-staging-v02.api.letsencrypt.org/directory", "name": "acme_certificate", "dns_mapping": { "domain1.com": "1" }, "create_type": "CERTIFICATE_CREATE_ACME" }] }

Create an Imported Certificate Signing Request

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "certificate.create", "params": [{ "name": "csr", "CSR": "CSR string", "privatekey": "Private key string", "create_type": "CERTIFICATE_CREATE_IMPORTED_CSR" }] }

This method is a job.

## Required Roles

- `CERTIFICATE_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: certificate_create

<a id="Call_parameters_items_i0"></a>
#### certificate_create

- Schema name: `certificate_create`
- Type: object

CertificateCreateArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_name"></a>
<a id="Call_parameters_items_i0_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Certificate name.
- Must be at least `1` characters long
- Must be at most `120` characters long

<a id="headingCall_parameters_items_i0_create_type"></a>
<a id="Call_parameters_items_i0_create_type"></a>
##### create_type (required)

- Schema name: `Create Type`
- Type: enum (of string)

Type of certificate creation operation.
###### Must be one of:

- "CERTIFICATE_CREATE_IMPORTED"
- "CERTIFICATE_CREATE_CSR"
- "CERTIFICATE_CREATE_IMPORTED_CSR"
- "CERTIFICATE_CREATE_ACME"

<a id="headingCall_parameters_items_i0_add_to_trusted_store"></a>
<a id="Call_parameters_items_i0_add_to_trusted_store"></a>
##### add_to_trusted_store

- Schema name: `Add To Trusted Store`
- Type: boolean
- Default: false

Whether to add this certificate to the trusted certificate store.

<a id="headingCall_parameters_items_i0_certificate"></a>
<a id="Call_parameters_items_i0_certificate"></a>
##### certificate

- Schema name: `Certificate`
- Default: null

PEM-encoded certificate to import or `null`.
<a id="Call_parameters_items_i0_certificate_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_certificate_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_certificate_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_certificate_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_certificate_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_privatekey"></a>
<a id="Call_parameters_items_i0_privatekey"></a>
##### privatekey

- Schema name: `Privatekey`
- Default: null

PEM-encoded private key to import or `null`.
<a id="Call_parameters_items_i0_privatekey_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_privatekey_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_privatekey_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_privatekey_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_privatekey_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_CSR"></a>
<a id="Call_parameters_items_i0_CSR"></a>
##### CSR

- Schema name: `Csr`
- Default: null

PEM-encoded certificate signing request to import or `null`.
<a id="Call_parameters_items_i0_CSR_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_CSR_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_CSR_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_CSR_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_CSR_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_key_length"></a>
<a id="Call_parameters_items_i0_key_length"></a>
##### key_length

- Schema name: `Key Length`
- Default: null

RSA key length in bits or `null`.
<a id="Call_parameters_items_i0_key_length_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_key_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_key_length_anyOf_i0)

- Type: enum (of integer)
###### Must be one of:

- 2048
- 4096

<a id="tab-pane_Call_parameters_items_i0_key_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_key_length_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_key_type"></a>
<a id="Call_parameters_items_i0_key_type"></a>
##### key_type

- Schema name: `Key Type`
- Type: enum (of string)
- Default: "RSA"

Type of cryptographic key to generate.
###### Must be one of:

- "RSA"
- "EC"

<a id="headingCall_parameters_items_i0_ec_curve"></a>
<a id="Call_parameters_items_i0_ec_curve"></a>
##### ec_curve

- Schema name: `Ec Curve`
- Type: enum (of string)
- Default: "SECP384R1"

Elliptic curve to use for EC keys.
###### Must be one of:

- "SECP256R1"
- "SECP384R1"
- "SECP521R1"
- "ed25519"

<a id="headingCall_parameters_items_i0_passphrase"></a>
<a id="Call_parameters_items_i0_passphrase"></a>
##### passphrase

- Schema name: `Passphrase`
- Default: null

Passphrase to protect the private key or `null`.
<a id="Call_parameters_items_i0_passphrase_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_passphrase_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_passphrase_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_passphrase_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_passphrase_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_city"></a>
<a id="Call_parameters_items_i0_city"></a>
##### city

- Schema name: `City`
- Default: null

City or locality name for certificate subject or `null`.
<a id="Call_parameters_items_i0_city_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_city_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_city_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_city_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_city_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_common"></a>
<a id="Call_parameters_items_i0_common"></a>
##### common

- Schema name: `Common`
- Default: null

Common name for certificate subject or `null`.
<a id="Call_parameters_items_i0_common_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_common_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_common_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_common_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_common_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_country"></a>
<a id="Call_parameters_items_i0_country"></a>
##### country

- Schema name: `Country`
- Default: null

Country name for certificate subject or `null`.
<a id="Call_parameters_items_i0_country_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_country_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_country_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_country_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_country_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_email"></a>
<a id="Call_parameters_items_i0_email"></a>
##### email

- Schema name: `Email`
- Default: null

Email address for certificate subject or `null`.
<a id="Call_parameters_items_i0_email_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_email_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_email_anyOf_i0)

- Type: string
- Type: Format: email

<a id="tab-pane_Call_parameters_items_i0_email_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_email_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_organization"></a>
<a id="Call_parameters_items_i0_organization"></a>
##### organization

- Schema name: `Organization`
- Default: null

Organization name for certificate subject or `null`.
<a id="Call_parameters_items_i0_organization_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_organization_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_organization_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_organization_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_organization_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_organizational_unit"></a>
<a id="Call_parameters_items_i0_organizational_unit"></a>
##### organizational_unit

- Schema name: `Organizational Unit`
- Default: null

Organizational unit for certificate subject or `null`.
<a id="Call_parameters_items_i0_organizational_unit_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_organizational_unit_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_organizational_unit_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_organizational_unit_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_organizational_unit_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_state"></a>
<a id="Call_parameters_items_i0_state"></a>
##### state

- Schema name: `State`
- Default: null

State or province name for certificate subject or `null`.
<a id="Call_parameters_items_i0_state_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_state_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_state_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_state_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_state_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_digest_algorithm"></a>
<a id="Call_parameters_items_i0_digest_algorithm"></a>
##### digest_algorithm

- Schema name: `Digest Algorithm`
- Type: enum (of string)
- Default: "SHA256"

Hash algorithm for certificate signing.
###### Must be one of:

- "SHA224"
- "SHA256"
- "SHA384"
- "SHA512"

<a id="headingCall_parameters_items_i0_san"></a>
<a id="Call_parameters_items_i0_san"></a>
##### san

- Schema name: `San`
- Type: array of string

Subject alternative names for the certificate.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_san_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_cert_extensions"></a>
<a id="Call_parameters_items_i0_cert_extensions"></a>
##### cert_extensions

- Schema name: `CertificateExtensions`
- Type: object

Certificate extensions configuration.
- No Additional Properties
<a id="headingCall_parameters_items_i0_cert_extensions_BasicConstraints"></a>
<a id="Call_parameters_items_i0_cert_extensions_BasicConstraints"></a>
###### BasicConstraints

- Schema name: `BasicConstraintsModel`
- Type: object
- Default:
```json
{
  "ca": false,
  "enabled": false,
  "path_length": null,
  "extension_critical": false
}
```

Basic Constraints extension configuration for certificate authority capabilities.
- No Additional Properties
<a id="headingCall_parameters_items_i0_cert_extensions_BasicConstraints_ca"></a>
<a id="Call_parameters_items_i0_cert_extensions_BasicConstraints_ca"></a>
###### ca

- Schema name: `Ca`
- Type: boolean
- Default: false

Whether this certificate is authorized to sign other certificates as a Certificate Authority (CA).

<a id="headingCall_parameters_items_i0_cert_extensions_BasicConstraints_enabled"></a>
<a id="Call_parameters_items_i0_cert_extensions_BasicConstraints_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: false

Whether the Basic Constraints X.509 extension is present in the certificate.

<a id="headingCall_parameters_items_i0_cert_extensions_BasicConstraints_path_length"></a>
<a id="Call_parameters_items_i0_cert_extensions_BasicConstraints_path_length"></a>
###### path_length

- Schema name: `Path Length`
- Default: null

Maximum number of intermediate CA certificates that may follow this certificate in a valid certificate chain. `null` indicates no path length constraint.
<a id="Call_parameters_items_i0_cert_extensions_BasicConstraints_path_length_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_cert_extensions_BasicConstraints_path_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_cert_extensions_BasicConstraints_path_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i0_cert_extensions_BasicConstraints_path_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_cert_extensions_BasicConstraints_path_length_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_cert_extensions_BasicConstraints_extension_critical"></a>
<a id="Call_parameters_items_i0_cert_extensions_BasicConstraints_extension_critical"></a>
###### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: false

Whether the Basic Constraints extension is marked as critical. If `true`, applications that do not understand this extension must reject the certificate.

<a id="headingCall_parameters_items_i0_cert_extensions_ExtendedKeyUsage"></a>
<a id="Call_parameters_items_i0_cert_extensions_ExtendedKeyUsage"></a>
###### ExtendedKeyUsage

- Schema name: `ExtendedKeyUsageModel`
- Type: object
- Default:
```json
{
  "usages": [],
  "enabled": false,
  "extension_critical": false
}
```

Extended Key Usage extension configuration specifying certificate purposes.
- No Additional Properties
<a id="headingCall_parameters_items_i0_cert_extensions_ExtendedKeyUsage_usages"></a>
<a id="Call_parameters_items_i0_cert_extensions_ExtendedKeyUsage_usages"></a>
###### usages

- Schema name: `Usages`
- Type: array of enum (of string)

Array of Extended Key Usage (EKU) purposes that define what the certificate may be used for (e.g., 'SERVER*AUTH', 'CLIENT*AUTH', 'CODE_SIGNING').
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_cert_extensions_ExtendedKeyUsage_usages_items"></a>
- Type: enum (of string)
###### Must be one of:

- "ANY_EXTENDED_KEY_USAGE"
- "CERTIFICATE_TRANSPARENCY"
- "CLIENT_AUTH"
- "CODE_SIGNING"
- "EMAIL_PROTECTION"
- "IPSEC_IKE"
- "KERBEROS_PKINIT_KDC"
- "OCSP_SIGNING"
- "SERVER_AUTH"
- "SMARTCARD_LOGON"
- "TIME_STAMPING"

<a id="headingCall_parameters_items_i0_cert_extensions_ExtendedKeyUsage_enabled"></a>
<a id="Call_parameters_items_i0_cert_extensions_ExtendedKeyUsage_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: false

Whether the Extended Key Usage X.509 extension is present in the certificate.

<a id="headingCall_parameters_items_i0_cert_extensions_ExtendedKeyUsage_extension_critical"></a>
<a id="Call_parameters_items_i0_cert_extensions_ExtendedKeyUsage_extension_critical"></a>
###### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: false

Whether the Extended Key Usage extension is marked as critical. If `true`, applications that do not understand this extension must reject the certificate.

<a id="headingCall_parameters_items_i0_cert_extensions_KeyUsage"></a>
<a id="Call_parameters_items_i0_cert_extensions_KeyUsage"></a>
###### KeyUsage

- Schema name: `KeyUsageModel`
- Type: object
- Default:
```json
{
  "enabled": false,
  "digital_signature": false,
  "content_commitment": false,
  "key_encipherment": false,
  "data_encipherment": false,
  "key_agreement": false,
  "key_cert_sign": false,
  "crl_sign": false,
  "encipher_only": false,
  "decipher_only": false,
  "extension_critical": false
}
```

Key Usage extension configuration defining permitted cryptographic operations.
- No Additional Properties
<a id="headingCall_parameters_items_i0_cert_extensions_KeyUsage_enabled"></a>
<a id="Call_parameters_items_i0_cert_extensions_KeyUsage_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: false

Whether the Key Usage X.509 extension is present in the certificate.

<a id="headingCall_parameters_items_i0_cert_extensions_KeyUsage_digital_signature"></a>
<a id="Call_parameters_items_i0_cert_extensions_KeyUsage_digital_signature"></a>
###### digital_signature

- Schema name: `Digital Signature`
- Type: boolean
- Default: false

Whether the certificate may be used for digital signatures to verify identity or integrity.

<a id="headingCall_parameters_items_i0_cert_extensions_KeyUsage_content_commitment"></a>
<a id="Call_parameters_items_i0_cert_extensions_KeyUsage_content_commitment"></a>
###### content_commitment

- Schema name: `Content Commitment`
- Type: boolean
- Default: false

Whether the certificate may be used for non-repudiation (proving content commitment).

<a id="headingCall_parameters_items_i0_cert_extensions_KeyUsage_key_encipherment"></a>
<a id="Call_parameters_items_i0_cert_extensions_KeyUsage_key_encipherment"></a>
###### key_encipherment

- Schema name: `Key Encipherment`
- Type: boolean
- Default: false

Whether the certificate's public key may be used for encrypting symmetric keys.

<a id="headingCall_parameters_items_i0_cert_extensions_KeyUsage_data_encipherment"></a>
<a id="Call_parameters_items_i0_cert_extensions_KeyUsage_data_encipherment"></a>
###### data_encipherment

- Schema name: `Data Encipherment`
- Type: boolean
- Default: false

Whether the certificate's public key may be used for directly encrypting raw data.

<a id="headingCall_parameters_items_i0_cert_extensions_KeyUsage_key_agreement"></a>
<a id="Call_parameters_items_i0_cert_extensions_KeyUsage_key_agreement"></a>
###### key_agreement

- Schema name: `Key Agreement`
- Type: boolean
- Default: false

Whether the certificate's public key may be used for key agreement protocols (e.g., Diffie-Hellman).

<a id="headingCall_parameters_items_i0_cert_extensions_KeyUsage_key_cert_sign"></a>
<a id="Call_parameters_items_i0_cert_extensions_KeyUsage_key_cert_sign"></a>
###### key_cert_sign

- Schema name: `Key Cert Sign`
- Type: boolean
- Default: false

Whether the certificate may be used to sign other certificates (CA functionality).

<a id="headingCall_parameters_items_i0_cert_extensions_KeyUsage_crl_sign"></a>
<a id="Call_parameters_items_i0_cert_extensions_KeyUsage_crl_sign"></a>
###### crl_sign

- Schema name: `Crl Sign`
- Type: boolean
- Default: false

Whether the certificate may be used to sign Certificate Revocation Lists (CRLs).

<a id="headingCall_parameters_items_i0_cert_extensions_KeyUsage_encipher_only"></a>
<a id="Call_parameters_items_i0_cert_extensions_KeyUsage_encipher_only"></a>
###### encipher_only

- Schema name: `Encipher Only`
- Type: boolean
- Default: false

Whether the public key may only be used for encryption when `key_agreement` is also set.

<a id="headingCall_parameters_items_i0_cert_extensions_KeyUsage_decipher_only"></a>
<a id="Call_parameters_items_i0_cert_extensions_KeyUsage_decipher_only"></a>
###### decipher_only

- Schema name: `Decipher Only`
- Type: boolean
- Default: false

Whether the public key may only be used for decryption when `key_agreement` is also set.

<a id="headingCall_parameters_items_i0_cert_extensions_KeyUsage_extension_critical"></a>
<a id="Call_parameters_items_i0_cert_extensions_KeyUsage_extension_critical"></a>
###### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: false

Whether the Key Usage extension is marked as critical. If `true`, applications that do not understand this extension must reject the certificate.

<a id="headingCall_parameters_items_i0_acme_directory_uri"></a>
<a id="Call_parameters_items_i0_acme_directory_uri"></a>
##### acme_directory_uri

- Schema name: `Acme Directory Uri`
- Default: null

ACME directory URI to be used for ACME certificate creation.
<a id="Call_parameters_items_i0_acme_directory_uri_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_acme_directory_uri_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_acme_directory_uri_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_acme_directory_uri_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_acme_directory_uri_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_csr_id"></a>
<a id="Call_parameters_items_i0_csr_id"></a>
##### csr_id

- Schema name: `Csr Id`
- Default: null

CSR to be used for ACME certificate creation.
<a id="Call_parameters_items_i0_csr_id_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_csr_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_csr_id_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i0_csr_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_csr_id_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_tos"></a>
<a id="Call_parameters_items_i0_tos"></a>
##### tos

- Schema name: `Tos`
- Default: null

Set this when creating an ACME certificate to accept terms of service of the ACME service.
<a id="Call_parameters_items_i0_tos_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_tos_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_tos_anyOf_i0)

- Type: boolean

<a id="tab-pane_Call_parameters_items_i0_tos_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_tos_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_dns_mapping"></a>
<a id="Call_parameters_items_i0_dns_mapping"></a>
##### dns_mapping

- Schema name: `Dns Mapping`
- Type: object

A mapping of domain to ACME DNS Authenticator ID for each domain listed in SAN or common name of the CSR.
<a id="headingCall_parameters_items_i0_dns_mapping_additionalProperties"></a>
<a id="Call_parameters_items_i0_dns_mapping_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Type: integer

<a id="headingCall_parameters_items_i0_renew_days"></a>
<a id="Call_parameters_items_i0_renew_days"></a>
##### renew_days

- Schema name: `Renew Days`
- Type: integer
- Default: 10

Number of days before the certificate expiration date to attempt certificate renewal. If certificate renewal fails, renewal will be reattempted every day until expiration.
- Value must be greater or equal to `1` and lesser or equal to `30`

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `CertificateEntry`
- Type: object

The created certificate configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this certificate entry.

<a id="headingReturn_value_type"></a>
<a id="Return_value_type"></a>
#### type (required)

- Schema name: `Type`
- Type: integer

Internal certificate type identifier used to determine certificate capabilities.

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for this certificate. Must be unique and contain only alphanumeric characters, dashes, and underscores.
- Must be at least `1` characters long

<a id="headingReturn_value_certificate"></a>
<a id="Return_value_certificate"></a>
#### certificate (required)

- Schema name: `Certificate`

PEM-encoded X.509 certificate data. `null` for certificate signing requests (CSR) that have not yet been signed.
<a id="Return_value_certificate_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_certificate_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_certificate_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_certificate_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_certificate_anyOf_i1)

- Type: null

<a id="headingReturn_value_privatekey"></a>
<a id="Return_value_privatekey"></a>
#### privatekey (required)

- Schema name: `Privatekey`

PEM-encoded private key corresponding to the certificate. `null` if no private key is available or for imported certificates without keys.
<a id="Return_value_privatekey_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_privatekey_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_privatekey_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_privatekey_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_privatekey_anyOf_i1)

- Type: null

<a id="headingReturn_value_CSR"></a>
<a id="Return_value_CSR"></a>
#### CSR (required)

- Schema name: `Csr`

PEM-encoded Certificate Signing Request (CSR) data. `null` for imported certificates or completed ACME certificates.
<a id="Return_value_CSR_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_CSR_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_CSR_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_CSR_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_CSR_anyOf_i1)

- Type: null

<a id="headingReturn_value_acme_uri"></a>
<a id="Return_value_acme_uri"></a>
#### acme_uri (required)

- Schema name: `Acme Uri`

ACME directory server URI used for automated certificate management. `null` for non-ACME certificates.
<a id="Return_value_acme_uri_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_acme_uri_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_acme_uri_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_acme_uri_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_acme_uri_anyOf_i1)

- Type: null

<a id="headingReturn_value_domains_authenticators"></a>
<a id="Return_value_domains_authenticators"></a>
#### domains_authenticators (required)

- Schema name: `Domains Authenticators`

Mapping of domain names to ACME DNS authenticator IDs for domain validation. `null` for non-ACME certificates.
<a id="Return_value_domains_authenticators_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_domains_authenticators_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_domains_authenticators_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_domains_authenticators_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_domains_authenticators_anyOf_i1)

- Type: null

<a id="headingReturn_value_renew_days"></a>
<a id="Return_value_renew_days"></a>
#### renew_days (required)

- Schema name: `Renew Days`

Number of days before expiration to attempt automatic renewal. Only applicable for ACME certificates. `null` for non-renewable certificates.
<a id="Return_value_renew_days_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_renew_days_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_renew_days_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_renew_days_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_renew_days_anyOf_i1)

- Type: null

<a id="headingReturn_value_acme"></a>
<a id="Return_value_acme"></a>
#### acme (required)

- Schema name: `Acme`

ACME registration and account information used for certificate lifecycle management. `null` for non-ACME certificates.
<a id="Return_value_acme_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_acme_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_acme_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_acme_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_acme_anyOf_i1)

- Type: null

<a id="headingReturn_value_add_to_trusted_store"></a>
<a id="Return_value_add_to_trusted_store"></a>
#### add_to_trusted_store (required)

- Schema name: `Add To Trusted Store`
- Type: boolean

Whether this certificate should be added to the system's trusted certificate store.

<a id="headingReturn_value_root_path"></a>
<a id="Return_value_root_path"></a>
#### root_path (required)

- Schema name: `Root Path`
- Type: string

Filesystem path where certificate-related files are stored.
- Must be at least `1` characters long

<a id="headingReturn_value_certificate_path"></a>
<a id="Return_value_certificate_path"></a>
#### certificate_path (required)

- Schema name: `Certificate Path`

Filesystem path to the certificate file (.crt). `null` if no certificate is available.
<a id="Return_value_certificate_path_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_certificate_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_certificate_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_certificate_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_certificate_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_privatekey_path"></a>
<a id="Return_value_privatekey_path"></a>
#### privatekey_path (required)

- Schema name: `Privatekey Path`

Filesystem path to the private key file (.key). `null` if no private key is available.
<a id="Return_value_privatekey_path_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_privatekey_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_privatekey_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_privatekey_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_privatekey_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_csr_path"></a>
<a id="Return_value_csr_path"></a>
#### csr_path (required)

- Schema name: `Csr Path`

Filesystem path to the certificate signing request file (.csr). `null` if no CSR is available.
<a id="Return_value_csr_path_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_csr_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_csr_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_csr_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_csr_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_cert_type"></a>
<a id="Return_value_cert_type"></a>
#### cert_type (required)

- Schema name: `Cert Type`
- Type: string

Human-readable certificate type, typically 'CERTIFICATE' for standard certificates.
- Must be at least `1` characters long

<a id="headingReturn_value_cert_type_existing"></a>
<a id="Return_value_cert_type_existing"></a>
#### cert_type_existing (required)

- Schema name: `Cert Type Existing`
- Type: boolean

Whether this is an existing certificate (imported or generated).

<a id="headingReturn_value_cert_type_CSR"></a>
<a id="Return_value_cert_type_CSR"></a>
#### cert_type_CSR (required)

- Schema name: `Cert Type Csr`
- Type: boolean

Whether this entry represents a Certificate Signing Request (CSR) rather than a signed certificate.

<a id="headingReturn_value_cert_type_CA"></a>
<a id="Return_value_cert_type_CA"></a>
#### cert_type_CA (required)

- Schema name: `Cert Type Ca`
- Type: boolean

Whether this certificate is a Certificate Authority (CA) certificate.

<a id="headingReturn_value_chain_list"></a>
<a id="Return_value_chain_list"></a>
#### chain_list (required)

- Schema name: `Chain List`
- Type: array of string

Array of PEM-encoded certificates in the certificate chain, starting with the leaf certificate.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_chain_list_items"></a>
- Type: string

<a id="headingReturn_value_key_length"></a>
<a id="Return_value_key_length"></a>
#### key_length (required)

- Schema name: `Key Length`

Size of the cryptographic key in bits. `null` if key information is unavailable.
<a id="Return_value_key_length_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_key_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_key_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_key_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_key_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_key_type"></a>
<a id="Return_value_key_type"></a>
#### key_type (required)

- Schema name: `Key Type`

Type of cryptographic key algorithm (e.g., 'RSA', 'EC', 'DSA'). `null` if key information is unavailable.
<a id="Return_value_key_type_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_key_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_key_type_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_key_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_key_type_anyOf_i1)

- Type: null

<a id="headingReturn_value_country"></a>
<a id="Return_value_country"></a>
#### country (required)

- Schema name: `Country`

ISO 3166-1 alpha-2 country code from the certificate subject. `null` if not specified.
<a id="Return_value_country_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_country_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_country_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_country_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_country_anyOf_i1)

- Type: null

<a id="headingReturn_value_state"></a>
<a id="Return_value_state"></a>
#### state (required)

- Schema name: `State`

State or province name from the certificate subject. `null` if not specified.
<a id="Return_value_state_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_state_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_state_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_state_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_state_anyOf_i1)

- Type: null

<a id="headingReturn_value_city"></a>
<a id="Return_value_city"></a>
#### city (required)

- Schema name: `City`

City or locality name from the certificate subject. `null` if not specified.
<a id="Return_value_city_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_city_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_city_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_city_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_city_anyOf_i1)

- Type: null

<a id="headingReturn_value_organization"></a>
<a id="Return_value_organization"></a>
#### organization (required)

- Schema name: `Organization`

Organization name from the certificate subject. `null` if not specified.
<a id="Return_value_organization_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_organization_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_organization_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_organization_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_organization_anyOf_i1)

- Type: null

<a id="headingReturn_value_organizational_unit"></a>
<a id="Return_value_organizational_unit"></a>
#### organizational_unit (required)

- Schema name: `Organizational Unit`

Organizational unit from the certificate subject. `null` if not specified.
<a id="Return_value_organizational_unit_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_organizational_unit_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_organizational_unit_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_organizational_unit_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_organizational_unit_anyOf_i1)

- Type: null

<a id="headingReturn_value_common"></a>
<a id="Return_value_common"></a>
#### common (required)

- Schema name: `Common`

Common name (CN) from the certificate subject. `null` if not specified.
<a id="Return_value_common_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_common_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_common_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_common_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_common_anyOf_i1)

- Type: null

<a id="headingReturn_value_san"></a>
<a id="Return_value_san"></a>
#### san (required)

- Schema name: `San`

Subject Alternative Names (SAN) from the certificate extension. `null` if no SAN extension is present.
<a id="Return_value_san_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_san_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_san_anyOf_i0)

- Type: array of string
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_san_anyOf_i0_items"></a>
- Type: string

<a id="tab-pane_Return_value_san_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_san_anyOf_i1)

- Type: null

<a id="headingReturn_value_email"></a>
<a id="Return_value_email"></a>
#### email (required)

- Schema name: `Email`

Email address from the certificate subject. `null` if not specified.
<a id="Return_value_email_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_email_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_email_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_email_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_email_anyOf_i1)

- Type: null

<a id="headingReturn_value_DN"></a>
<a id="Return_value_DN"></a>
#### DN (required)

- Schema name: `Dn`

Distinguished Name (DN) of the certificate subject in RFC 2253 format. `null` if certificate parsing failed.
<a id="Return_value_DN_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_DN_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_DN_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_DN_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_DN_anyOf_i1)

- Type: null

<a id="headingReturn_value_subject_name_hash"></a>
<a id="Return_value_subject_name_hash"></a>
#### subject_name_hash (required)

- Schema name: `Subject Name Hash`

Hash of the certificate subject name. `null` if certificate parsing failed.
<a id="Return_value_subject_name_hash_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_subject_name_hash_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_subject_name_hash_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_subject_name_hash_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_subject_name_hash_anyOf_i1)

- Type: null

<a id="headingReturn_value_extensions"></a>
<a id="Return_value_extensions"></a>
#### extensions (required)

- Schema name: `Extensions`
- Type: object

X.509 certificate extensions parsed into a dictionary structure.

<a id="headingReturn_value_digest_algorithm"></a>
<a id="Return_value_digest_algorithm"></a>
#### digest_algorithm (required)

- Schema name: `Digest Algorithm`

Cryptographic hash algorithm used for certificate signing (e.g., 'SHA256'). `null` if unavailable.
<a id="Return_value_digest_algorithm_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_digest_algorithm_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_digest_algorithm_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_digest_algorithm_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_digest_algorithm_anyOf_i1)

- Type: null

<a id="headingReturn_value_lifetime"></a>
<a id="Return_value_lifetime"></a>
#### lifetime (required)

- Schema name: `Lifetime`

Certificate validity period in seconds. `null` if certificate parsing failed.
<a id="Return_value_lifetime_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_lifetime_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_lifetime_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_lifetime_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_lifetime_anyOf_i1)

- Type: null

<a id="headingReturn_value_from"></a>
<a id="Return_value_from"></a>
#### from (required)

- Schema name: `From`

Certificate validity start date in ISO 8601 format. `null` if certificate parsing failed.
<a id="Return_value_from_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_from_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_from_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_from_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_from_anyOf_i1)

- Type: null

<a id="headingReturn_value_until"></a>
<a id="Return_value_until"></a>
#### until (required)

- Schema name: `Until`

Certificate validity end date in ISO 8601 format. `null` if certificate parsing failed.
<a id="Return_value_until_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_until_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_until_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_until_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_until_anyOf_i1)

- Type: null

<a id="headingReturn_value_serial"></a>
<a id="Return_value_serial"></a>
#### serial (required)

- Schema name: `Serial`

Certificate serial number. `null` if certificate parsing failed.
<a id="Return_value_serial_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_serial_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_serial_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_serial_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_serial_anyOf_i1)

- Type: null

<a id="headingReturn_value_chain"></a>
<a id="Return_value_chain"></a>
#### chain (required)

- Schema name: `Chain`

Whether this certificate has an associated certificate chain. `null` if unavailable.
<a id="Return_value_chain_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_chain_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_chain_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_chain_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_chain_anyOf_i1)

- Type: null

<a id="headingReturn_value_fingerprint"></a>
<a id="Return_value_fingerprint"></a>
#### fingerprint (required)

- Schema name: `Fingerprint`

SHA-256 fingerprint of the certificate in hexadecimal format. `null` if certificate parsing failed.
<a id="Return_value_fingerprint_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_fingerprint_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_fingerprint_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_fingerprint_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_fingerprint_anyOf_i1)

- Type: null

<a id="headingReturn_value_expired"></a>
<a id="Return_value_expired"></a>
#### expired (required)

- Schema name: `Expired`

Whether the certificate has expired. `null` if certificate parsing failed.
<a id="Return_value_expired_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_expired_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_expired_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_expired_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_expired_anyOf_i1)

- Type: null

<a id="headingReturn_value_parsed"></a>
<a id="Return_value_parsed"></a>
#### parsed (required)

- Schema name: `Parsed`
- Type: boolean

Whether the certificate data was successfully parsed and validated.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
