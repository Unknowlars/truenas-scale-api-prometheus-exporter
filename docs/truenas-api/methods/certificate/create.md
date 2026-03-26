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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: certificate_create

#### certificate_create

- Schema name: `certificate_create`
- Type: object

CertificateCreateArgs parameters.
- No Additional Properties
##### name (required)

- Schema name: `Name`
- Type: string

Certificate name.
- Must be at least `1` characters long
- Must be at most `120` characters long

##### create_type (required)

- Schema name: `Create Type`
- Type: enum (of string)

Type of certificate creation operation.

##### add_to_trusted_store

- Schema name: `Add To Trusted Store`
- Type: boolean
- Default: false

Whether to add this certificate to the trusted certificate store.

##### certificate

- Schema name: `Certificate`
- Default: null

PEM-encoded certificate to import or `null`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### privatekey

- Schema name: `Privatekey`
- Default: null

PEM-encoded private key to import or `null`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### CSR

- Schema name: `Csr`
- Default: null

PEM-encoded certificate signing request to import or `null`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### key_length

- Schema name: `Key Length`
- Default: null

RSA key length in bits or `null`.
###### Any of

####### Option 1

- Type: enum (of integer)

####### Option 2

- Type: null

##### key_type

- Schema name: `Key Type`
- Type: enum (of string)
- Default: "RSA"

Type of cryptographic key to generate.

##### ec_curve

- Schema name: `Ec Curve`
- Type: enum (of string)
- Default: "SECP384R1"

Elliptic curve to use for EC keys.

##### passphrase

- Schema name: `Passphrase`
- Default: null

Passphrase to protect the private key or `null`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### city

- Schema name: `City`
- Default: null

City or locality name for certificate subject or `null`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### common

- Schema name: `Common`
- Default: null

Common name for certificate subject or `null`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### country

- Schema name: `Country`
- Default: null

Country name for certificate subject or `null`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### email

- Schema name: `Email`
- Default: null

Email address for certificate subject or `null`.
###### Any of

####### Option 1

- Type: string
- Type: Format: email

####### Option 2

- Type: null

##### organization

- Schema name: `Organization`
- Default: null

Organization name for certificate subject or `null`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### organizational_unit

- Schema name: `Organizational Unit`
- Default: null

Organizational unit for certificate subject or `null`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### state

- Schema name: `State`
- Default: null

State or province name for certificate subject or `null`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### digest_algorithm

- Schema name: `Digest Algorithm`
- Type: enum (of string)
- Default: "SHA256"

Hash algorithm for certificate signing.

##### san

- Schema name: `San`
- Type: array of string

Subject alternative names for the certificate.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

##### cert_extensions

- Schema name: `CertificateExtensions`
- Type: object

Certificate extensions configuration.
- No Additional Properties
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
####### ca

- Schema name: `Ca`
- Type: boolean
- Default: false

Whether this certificate is authorized to sign other certificates as a Certificate Authority (CA).

####### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: false

Whether the Basic Constraints X.509 extension is present in the certificate.

####### path_length

- Schema name: `Path Length`
- Default: null

Maximum number of intermediate CA certificates that may follow this certificate in a valid certificate chain. `null` indicates no path length constraint.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: null

####### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: false

Whether the Basic Constraints extension is marked as critical. If `true`, applications that do not understand this extension must reject the certificate.

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
####### usages

- Schema name: `Usages`
- Type: array of enum (of string)

Array of Extended Key Usage (EKU) purposes that define what the certificate may be used for (e.g., 'SERVER*AUTH', 'CLIENT*AUTH', 'CODE_SIGNING').
- No Additional Items

######## Each item of this array must be:

- Type: enum (of string)

####### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: false

Whether the Extended Key Usage X.509 extension is present in the certificate.

####### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: false

Whether the Extended Key Usage extension is marked as critical. If `true`, applications that do not understand this extension must reject the certificate.

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
####### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: false

Whether the Key Usage X.509 extension is present in the certificate.

####### digital_signature

- Schema name: `Digital Signature`
- Type: boolean
- Default: false

Whether the certificate may be used for digital signatures to verify identity or integrity.

####### content_commitment

- Schema name: `Content Commitment`
- Type: boolean
- Default: false

Whether the certificate may be used for non-repudiation (proving content commitment).

####### key_encipherment

- Schema name: `Key Encipherment`
- Type: boolean
- Default: false

Whether the certificate's public key may be used for encrypting symmetric keys.

####### data_encipherment

- Schema name: `Data Encipherment`
- Type: boolean
- Default: false

Whether the certificate's public key may be used for directly encrypting raw data.

####### key_agreement

- Schema name: `Key Agreement`
- Type: boolean
- Default: false

Whether the certificate's public key may be used for key agreement protocols (e.g., Diffie-Hellman).

####### key_cert_sign

- Schema name: `Key Cert Sign`
- Type: boolean
- Default: false

Whether the certificate may be used to sign other certificates (CA functionality).

####### crl_sign

- Schema name: `Crl Sign`
- Type: boolean
- Default: false

Whether the certificate may be used to sign Certificate Revocation Lists (CRLs).

####### encipher_only

- Schema name: `Encipher Only`
- Type: boolean
- Default: false

Whether the public key may only be used for encryption when `key_agreement` is also set.

####### decipher_only

- Schema name: `Decipher Only`
- Type: boolean
- Default: false

Whether the public key may only be used for decryption when `key_agreement` is also set.

####### extension_critical

- Schema name: `Extension Critical`
- Type: boolean
- Default: false

Whether the Key Usage extension is marked as critical. If `true`, applications that do not understand this extension must reject the certificate.

##### acme_directory_uri

- Schema name: `Acme Directory Uri`
- Default: null

ACME directory URI to be used for ACME certificate creation.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### csr_id

- Schema name: `Csr Id`
- Default: null

CSR to be used for ACME certificate creation.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### tos

- Schema name: `Tos`
- Default: null

Set this when creating an ACME certificate to accept terms of service of the ACME service.
###### Any of

####### Option 1

- Type: boolean

####### Option 2

- Type: null

##### dns_mapping

- Schema name: `Dns Mapping`
- Type: object

A mapping of domain to ACME DNS Authenticator ID for each domain listed in SAN or common name of the CSR.
###### Additional Properties

Each additional property must conform to the following schema
- Type: integer

##### renew_days

- Schema name: `Renew Days`
- Type: integer
- Default: 10

Number of days before the certificate expiration date to attempt certificate renewal. If certificate renewal fails, renewal will be reattempted every day until expiration.
- Value must be greater or equal to `1` and lesser or equal to `30`

### Return value

- Schema name: `CertificateEntry`
- Type: object

The created certificate configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this certificate entry.

#### type (required)

- Schema name: `Type`
- Type: integer

Internal certificate type identifier used to determine certificate capabilities.

#### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for this certificate. Must be unique and contain only alphanumeric characters, dashes, and underscores.
- Must be at least `1` characters long

#### certificate (required)

- Schema name: `Certificate`

PEM-encoded X.509 certificate data. `null` for certificate signing requests (CSR) that have not yet been signed.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### privatekey (required)

- Schema name: `Privatekey`

PEM-encoded private key corresponding to the certificate. `null` if no private key is available or for imported certificates without keys.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### CSR (required)

- Schema name: `Csr`

PEM-encoded Certificate Signing Request (CSR) data. `null` for imported certificates or completed ACME certificates.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### acme_uri (required)

- Schema name: `Acme Uri`

ACME directory server URI used for automated certificate management. `null` for non-ACME certificates.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### domains_authenticators (required)

- Schema name: `Domains Authenticators`

Mapping of domain names to ACME DNS authenticator IDs for domain validation. `null` for non-ACME certificates.
##### Any of

###### Option 1

- Type: object

###### Option 2

- Type: null

#### renew_days (required)

- Schema name: `Renew Days`

Number of days before expiration to attempt automatic renewal. Only applicable for ACME certificates. `null` for non-renewable certificates.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### acme (required)

- Schema name: `Acme`

ACME registration and account information used for certificate lifecycle management. `null` for non-ACME certificates.
##### Any of

###### Option 1

- Type: object

###### Option 2

- Type: null

#### add_to_trusted_store (required)

- Schema name: `Add To Trusted Store`
- Type: boolean

Whether this certificate should be added to the system's trusted certificate store.

#### root_path (required)

- Schema name: `Root Path`
- Type: string

Filesystem path where certificate-related files are stored.
- Must be at least `1` characters long

#### certificate_path (required)

- Schema name: `Certificate Path`

Filesystem path to the certificate file (.crt). `null` if no certificate is available.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

#### privatekey_path (required)

- Schema name: `Privatekey Path`

Filesystem path to the private key file (.key). `null` if no private key is available.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

#### csr_path (required)

- Schema name: `Csr Path`

Filesystem path to the certificate signing request file (.csr). `null` if no CSR is available.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

#### cert_type (required)

- Schema name: `Cert Type`
- Type: string

Human-readable certificate type, typically 'CERTIFICATE' for standard certificates.
- Must be at least `1` characters long

#### cert_type_existing (required)

- Schema name: `Cert Type Existing`
- Type: boolean

Whether this is an existing certificate (imported or generated).

#### cert_type_CSR (required)

- Schema name: `Cert Type Csr`
- Type: boolean

Whether this entry represents a Certificate Signing Request (CSR) rather than a signed certificate.

#### cert_type_CA (required)

- Schema name: `Cert Type Ca`
- Type: boolean

Whether this certificate is a Certificate Authority (CA) certificate.

#### chain_list (required)

- Schema name: `Chain List`
- Type: array of string

Array of PEM-encoded certificates in the certificate chain, starting with the leaf certificate.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### key_length (required)

- Schema name: `Key Length`

Size of the cryptographic key in bits. `null` if key information is unavailable.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### key_type (required)

- Schema name: `Key Type`

Type of cryptographic key algorithm (e.g., 'RSA', 'EC', 'DSA'). `null` if key information is unavailable.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

#### country (required)

- Schema name: `Country`

ISO 3166-1 alpha-2 country code from the certificate subject. `null` if not specified.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### state (required)

- Schema name: `State`

State or province name from the certificate subject. `null` if not specified.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### city (required)

- Schema name: `City`

City or locality name from the certificate subject. `null` if not specified.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### organization (required)

- Schema name: `Organization`

Organization name from the certificate subject. `null` if not specified.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### organizational_unit (required)

- Schema name: `Organizational Unit`

Organizational unit from the certificate subject. `null` if not specified.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### common (required)

- Schema name: `Common`

Common name (CN) from the certificate subject. `null` if not specified.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### san (required)

- Schema name: `San`

Subject Alternative Names (SAN) from the certificate extension. `null` if no SAN extension is present.
##### Any of

###### Option 1

- Type: array of string
- No Additional Items

####### Each item of this array must be:

- Type: string

###### Option 2

- Type: null

#### email (required)

- Schema name: `Email`

Email address from the certificate subject. `null` if not specified.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### DN (required)

- Schema name: `Dn`

Distinguished Name (DN) of the certificate subject in RFC 2253 format. `null` if certificate parsing failed.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### subject_name_hash (required)

- Schema name: `Subject Name Hash`

Hash of the certificate subject name. `null` if certificate parsing failed.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### extensions (required)

- Schema name: `Extensions`
- Type: object

X.509 certificate extensions parsed into a dictionary structure.

#### digest_algorithm (required)

- Schema name: `Digest Algorithm`

Cryptographic hash algorithm used for certificate signing (e.g., 'SHA256'). `null` if unavailable.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### lifetime (required)

- Schema name: `Lifetime`

Certificate validity period in seconds. `null` if certificate parsing failed.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### from (required)

- Schema name: `From`

Certificate validity start date in ISO 8601 format. `null` if certificate parsing failed.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### until (required)

- Schema name: `Until`

Certificate validity end date in ISO 8601 format. `null` if certificate parsing failed.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### serial (required)

- Schema name: `Serial`

Certificate serial number. `null` if certificate parsing failed.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### chain (required)

- Schema name: `Chain`

Whether this certificate has an associated certificate chain. `null` if unavailable.
##### Any of

###### Option 1

- Type: boolean

###### Option 2

- Type: null

#### fingerprint (required)

- Schema name: `Fingerprint`

SHA-256 fingerprint of the certificate in hexadecimal format. `null` if certificate parsing failed.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### expired (required)

- Schema name: `Expired`

Whether the certificate has expired. `null` if certificate parsing failed.
##### Any of

###### Option 1

- Type: boolean

###### Option 2

- Type: null

#### parsed (required)

- Schema name: `Parsed`
- Type: boolean

Whether the certificate data was successfully parsed and validated.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
