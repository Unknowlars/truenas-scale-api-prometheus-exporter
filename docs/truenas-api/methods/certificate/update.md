---
title: certificate.update
kind: method
source_rst: _sources/api_methods_certificate.update.rst.txt
source_html: api_methods_certificate.update.html
required_roles:
  - CERTIFICATE_WRITE
---

# certificate.update

## Summary

Update certificate of `id`

Only name attribute can be updated.

.. examples(websocket)::

Update a certificate of `id`

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "certificate.update", "params": [ 1, { "name": "updated_name" } ] }

This method is a job.

## Required Roles

- `CERTIFICATE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the certificate to update.

#### Parameter 2: certificate_update

#### certificate_update

- Schema name: `certificate_update`
- Type: object

Updated certificate configuration data.
- No Additional Properties
##### renew_days

- Schema name: `Renew Days`
- Type: integer

Days before expiration to attempt renewal.
- Value must be greater or equal to `1` and lesser or equal to `30`

##### add_to_trusted_store

- Schema name: `Add To Trusted Store`
- Type: boolean

Whether to add this certificate to the trusted certificate store.

##### name

- Schema name: `Name`
- Type: string

Certificate name.
- Must be at least `1` characters long
- Must be at most `120` characters long

### Return value

- Schema name: `CertificateEntry`
- Type: object

The updated certificate configuration.
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
