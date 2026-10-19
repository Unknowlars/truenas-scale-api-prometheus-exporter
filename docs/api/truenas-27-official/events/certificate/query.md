---
title: certificate.query
kind: event
source_rst: _sources/api_events_certificate.query.rst.txt
source_html: api_events_certificate.query.html
required_roles:
  - CERTIFICATE_READ
---

# certificate.query

## Summary

Sent on certificate changes.

## Required Roles

- `CERTIFICATE_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `CertificateAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `CertificateEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this certificate entry.

<a id="headingADDED_fields_type"></a>
<a id="ADDED_fields_type"></a>
##### type (required)

- Schema name: `Type`
- Type: integer

Internal certificate type identifier used to determine certificate capabilities.

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for this certificate. Must be unique and contain only alphanumeric characters, dashes, and underscores.
- Must be at least `1` characters long

<a id="headingADDED_fields_certificate"></a>
<a id="ADDED_fields_certificate"></a>
##### certificate (required)

- Schema name: `Certificate`

PEM-encoded X.509 certificate data. `null` for certificate signing requests (CSR) that have not yet been signed.
<a id="ADDED_fields_certificate_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_certificate_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_certificate_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_ADDED_fields_certificate_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_certificate_anyOf_i1)

- Type: null

<a id="headingADDED_fields_privatekey"></a>
<a id="ADDED_fields_privatekey"></a>
##### privatekey (required)

- Schema name: `Privatekey`

PEM-encoded private key corresponding to the certificate. `null` if no private key is available or for imported certificates without keys.
<a id="ADDED_fields_privatekey_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_privatekey_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_privatekey_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_ADDED_fields_privatekey_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_privatekey_anyOf_i1)

- Type: null

<a id="headingADDED_fields_CSR"></a>
<a id="ADDED_fields_CSR"></a>
##### CSR (required)

- Schema name: `Csr`

PEM-encoded Certificate Signing Request (CSR) data. `null` for imported certificates or completed ACME certificates.
<a id="ADDED_fields_CSR_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_CSR_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_CSR_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_ADDED_fields_CSR_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_CSR_anyOf_i1)

- Type: null

<a id="headingADDED_fields_acme_uri"></a>
<a id="ADDED_fields_acme_uri"></a>
##### acme_uri (required)

- Schema name: `Acme Uri`

ACME directory server URI used for automated certificate management. `null` for non-ACME certificates.
<a id="ADDED_fields_acme_uri_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_acme_uri_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_acme_uri_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_acme_uri_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_acme_uri_anyOf_i1)

- Type: null

<a id="headingADDED_fields_domains_authenticators"></a>
<a id="ADDED_fields_domains_authenticators"></a>
##### domains_authenticators (required)

- Schema name: `Domains Authenticators`

Mapping of domain names to ACME DNS authenticator IDs for domain validation. `null` for non-ACME certificates.
<a id="ADDED_fields_domains_authenticators_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_domains_authenticators_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_domains_authenticators_anyOf_i0)

- Type: object

<a id="tab-pane_ADDED_fields_domains_authenticators_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_domains_authenticators_anyOf_i1)

- Type: null

<a id="headingADDED_fields_renew_days"></a>
<a id="ADDED_fields_renew_days"></a>
##### renew_days (required)

- Schema name: `Renew Days`

Number of days before expiration to attempt automatic renewal. Only applicable for ACME certificates. `null` for non-renewable certificates.
<a id="ADDED_fields_renew_days_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_renew_days_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_renew_days_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_renew_days_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_renew_days_anyOf_i1)

- Type: null

<a id="headingADDED_fields_acme"></a>
<a id="ADDED_fields_acme"></a>
##### acme (required)

- Schema name: `Acme`

ACME registration and account information used for certificate lifecycle management. `null` for non-ACME certificates.
<a id="ADDED_fields_acme_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_acme_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_acme_anyOf_i0)

- Type: object

<a id="tab-pane_ADDED_fields_acme_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_acme_anyOf_i1)

- Type: null

<a id="headingADDED_fields_add_to_trusted_store"></a>
<a id="ADDED_fields_add_to_trusted_store"></a>
##### add_to_trusted_store (required)

- Schema name: `Add To Trusted Store`
- Type: boolean

Whether this certificate should be added to the system's trusted certificate store.

<a id="headingADDED_fields_root_path"></a>
<a id="ADDED_fields_root_path"></a>
##### root_path (required)

- Schema name: `Root Path`
- Type: string

Filesystem path where certificate-related files are stored.
- Must be at least `1` characters long

<a id="headingADDED_fields_certificate_path"></a>
<a id="ADDED_fields_certificate_path"></a>
##### certificate_path (required)

- Schema name: `Certificate Path`

Filesystem path to the certificate file (.crt). `null` if no certificate is available.
<a id="ADDED_fields_certificate_path_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_certificate_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_certificate_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_certificate_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_certificate_path_anyOf_i1)

- Type: null

<a id="headingADDED_fields_privatekey_path"></a>
<a id="ADDED_fields_privatekey_path"></a>
##### privatekey_path (required)

- Schema name: `Privatekey Path`

Filesystem path to the private key file (.key). `null` if no private key is available.
<a id="ADDED_fields_privatekey_path_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_privatekey_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_privatekey_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_privatekey_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_privatekey_path_anyOf_i1)

- Type: null

<a id="headingADDED_fields_csr_path"></a>
<a id="ADDED_fields_csr_path"></a>
##### csr_path (required)

- Schema name: `Csr Path`

Filesystem path to the certificate signing request file (.csr). `null` if no CSR is available.
<a id="ADDED_fields_csr_path_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_csr_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_csr_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_csr_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_csr_path_anyOf_i1)

- Type: null

<a id="headingADDED_fields_cert_type"></a>
<a id="ADDED_fields_cert_type"></a>
##### cert_type (required)

- Schema name: `Cert Type`
- Type: string

Human-readable certificate type, typically 'CERTIFICATE' for standard certificates.
- Must be at least `1` characters long

<a id="headingADDED_fields_cert_type_existing"></a>
<a id="ADDED_fields_cert_type_existing"></a>
##### cert_type_existing (required)

- Schema name: `Cert Type Existing`
- Type: boolean

Whether this is an existing certificate (imported or generated).

<a id="headingADDED_fields_cert_type_CSR"></a>
<a id="ADDED_fields_cert_type_CSR"></a>
##### cert_type_CSR (required)

- Schema name: `Cert Type Csr`
- Type: boolean

Whether this entry represents a Certificate Signing Request (CSR) rather than a signed certificate.

<a id="headingADDED_fields_cert_type_CA"></a>
<a id="ADDED_fields_cert_type_CA"></a>
##### cert_type_CA (required)

- Schema name: `Cert Type Ca`
- Type: boolean

Whether this certificate is a Certificate Authority (CA) certificate.

<a id="headingADDED_fields_chain_list"></a>
<a id="ADDED_fields_chain_list"></a>
##### chain_list (required)

- Schema name: `Chain List`
- Type: array of string

Array of PEM-encoded certificates in the certificate chain, starting with the leaf certificate.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_chain_list_items"></a>
- Type: string
- Must be at most `2147483647` characters long

<a id="headingADDED_fields_key_length"></a>
<a id="ADDED_fields_key_length"></a>
##### key_length (required)

- Schema name: `Key Length`

Size of the cryptographic key in bits. `null` if key information is unavailable.
<a id="ADDED_fields_key_length_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_key_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_key_length_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_key_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_key_length_anyOf_i1)

- Type: null

<a id="headingADDED_fields_key_type"></a>
<a id="ADDED_fields_key_type"></a>
##### key_type (required)

- Schema name: `Key Type`

Type of cryptographic key algorithm (e.g., 'RSA', 'EC', 'DSA'). `null` if key information is unavailable.
<a id="ADDED_fields_key_type_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_key_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_key_type_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_key_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_key_type_anyOf_i1)

- Type: null

<a id="headingADDED_fields_country"></a>
<a id="ADDED_fields_country"></a>
##### country (required)

- Schema name: `Country`

ISO 3166-1 alpha-2 country code from the certificate subject. `null` if not specified.
<a id="ADDED_fields_country_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_country_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_country_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_country_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_country_anyOf_i1)

- Type: null

<a id="headingADDED_fields_state"></a>
<a id="ADDED_fields_state"></a>
##### state (required)

- Schema name: `State`

State or province name from the certificate subject. `null` if not specified.
<a id="ADDED_fields_state_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_state_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_state_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_state_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_state_anyOf_i1)

- Type: null

<a id="headingADDED_fields_city"></a>
<a id="ADDED_fields_city"></a>
##### city (required)

- Schema name: `City`

City or locality name from the certificate subject. `null` if not specified.
<a id="ADDED_fields_city_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_city_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_city_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_city_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_city_anyOf_i1)

- Type: null

<a id="headingADDED_fields_organization"></a>
<a id="ADDED_fields_organization"></a>
##### organization (required)

- Schema name: `Organization`

Organization name from the certificate subject. `null` if not specified.
<a id="ADDED_fields_organization_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_organization_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_organization_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_organization_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_organization_anyOf_i1)

- Type: null

<a id="headingADDED_fields_organizational_unit"></a>
<a id="ADDED_fields_organizational_unit"></a>
##### organizational_unit (required)

- Schema name: `Organizational Unit`

Organizational unit from the certificate subject. `null` if not specified.
<a id="ADDED_fields_organizational_unit_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_organizational_unit_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_organizational_unit_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_organizational_unit_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_organizational_unit_anyOf_i1)

- Type: null

<a id="headingADDED_fields_common"></a>
<a id="ADDED_fields_common"></a>
##### common (required)

- Schema name: `Common`

Common name (CN) from the certificate subject. `null` if not specified.
<a id="ADDED_fields_common_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_common_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_common_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_common_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_common_anyOf_i1)

- Type: null

<a id="headingADDED_fields_san"></a>
<a id="ADDED_fields_san"></a>
##### san (required)

- Schema name: `San`

Subject Alternative Names (SAN) from the certificate extension. `null` if no SAN extension is present.
<a id="ADDED_fields_san_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_san_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_san_anyOf_i0)

- Type: array of string
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_san_anyOf_i0_items"></a>
- Type: string

<a id="tab-pane_ADDED_fields_san_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_san_anyOf_i1)

- Type: null

<a id="headingADDED_fields_email"></a>
<a id="ADDED_fields_email"></a>
##### email (required)

- Schema name: `Email`

Email address from the certificate subject. `null` if not specified.
<a id="ADDED_fields_email_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_email_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_email_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_email_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_email_anyOf_i1)

- Type: null

<a id="headingADDED_fields_DN"></a>
<a id="ADDED_fields_DN"></a>
##### DN (required)

- Schema name: `Dn`

Distinguished Name (DN) of the certificate subject in RFC 2253 format. `null` if certificate parsing failed.
<a id="ADDED_fields_DN_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_DN_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_DN_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_ADDED_fields_DN_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_DN_anyOf_i1)

- Type: null

<a id="headingADDED_fields_subject_name_hash"></a>
<a id="ADDED_fields_subject_name_hash"></a>
##### subject_name_hash (required)

- Schema name: `Subject Name Hash`

Hash of the certificate subject name. `null` if certificate parsing failed.
<a id="ADDED_fields_subject_name_hash_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_subject_name_hash_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_subject_name_hash_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_subject_name_hash_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_subject_name_hash_anyOf_i1)

- Type: null

<a id="headingADDED_fields_extensions"></a>
<a id="ADDED_fields_extensions"></a>
##### extensions (required)

- Schema name: `Extensions`
- Type: object

X.509 certificate extensions parsed into a dictionary structure.

<a id="headingADDED_fields_digest_algorithm"></a>
<a id="ADDED_fields_digest_algorithm"></a>
##### digest_algorithm (required)

- Schema name: `Digest Algorithm`

Cryptographic hash algorithm used for certificate signing (e.g., 'SHA256'). `null` if unavailable.
<a id="ADDED_fields_digest_algorithm_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_digest_algorithm_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_digest_algorithm_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_digest_algorithm_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_digest_algorithm_anyOf_i1)

- Type: null

<a id="headingADDED_fields_lifetime"></a>
<a id="ADDED_fields_lifetime"></a>
##### lifetime (required)

- Schema name: `Lifetime`

Certificate validity period in seconds. `null` if certificate parsing failed.
<a id="ADDED_fields_lifetime_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_lifetime_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_lifetime_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_lifetime_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_lifetime_anyOf_i1)

- Type: null

<a id="headingADDED_fields_from"></a>
<a id="ADDED_fields_from"></a>
##### from (required)

- Schema name: `From`

Certificate validity start date in ISO 8601 format. `null` if certificate parsing failed.
<a id="ADDED_fields_from_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_from_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_from_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_from_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_from_anyOf_i1)

- Type: null

<a id="headingADDED_fields_until"></a>
<a id="ADDED_fields_until"></a>
##### until (required)

- Schema name: `Until`

Certificate validity end date in ISO 8601 format. `null` if certificate parsing failed.
<a id="ADDED_fields_until_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_until_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_until_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_until_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_until_anyOf_i1)

- Type: null

<a id="headingADDED_fields_serial"></a>
<a id="ADDED_fields_serial"></a>
##### serial (required)

- Schema name: `Serial`

Certificate serial number. `null` if certificate parsing failed.
<a id="ADDED_fields_serial_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_serial_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_serial_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_serial_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_serial_anyOf_i1)

- Type: null

<a id="headingADDED_fields_chain"></a>
<a id="ADDED_fields_chain"></a>
##### chain (required)

- Schema name: `Chain`

Whether this certificate has an associated certificate chain. `null` if unavailable.
<a id="ADDED_fields_chain_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_chain_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_chain_anyOf_i0)

- Type: boolean

<a id="tab-pane_ADDED_fields_chain_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_chain_anyOf_i1)

- Type: null

<a id="headingADDED_fields_fingerprint"></a>
<a id="ADDED_fields_fingerprint"></a>
##### fingerprint (required)

- Schema name: `Fingerprint`

SHA-256 fingerprint of the certificate in hexadecimal format. `null` if certificate parsing failed.
<a id="ADDED_fields_fingerprint_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_fingerprint_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_fingerprint_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_fingerprint_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_fingerprint_anyOf_i1)

- Type: null

<a id="headingADDED_fields_expired"></a>
<a id="ADDED_fields_expired"></a>
##### expired (required)

- Schema name: `Expired`

Whether the certificate has expired. `null` if certificate parsing failed.
<a id="ADDED_fields_expired_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_expired_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_expired_anyOf_i0)

- Type: boolean

<a id="tab-pane_ADDED_fields_expired_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_expired_anyOf_i1)

- Type: null

<a id="headingADDED_fields_parsed"></a>
<a id="ADDED_fields_parsed"></a>
##### parsed (required)

- Schema name: `Parsed`
- Type: boolean

Whether the certificate data was successfully parsed and validated.

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `CertificateChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `CertificateEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this certificate entry.

<a id="headingCHANGED_fields_type"></a>
<a id="CHANGED_fields_type"></a>
##### type (required)

- Schema name: `Type`
- Type: integer

Internal certificate type identifier used to determine certificate capabilities.

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for this certificate. Must be unique and contain only alphanumeric characters, dashes, and underscores.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_certificate"></a>
<a id="CHANGED_fields_certificate"></a>
##### certificate (required)

- Schema name: `Certificate`

PEM-encoded X.509 certificate data. `null` for certificate signing requests (CSR) that have not yet been signed.
<a id="CHANGED_fields_certificate_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_certificate_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_certificate_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_CHANGED_fields_certificate_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_certificate_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_privatekey"></a>
<a id="CHANGED_fields_privatekey"></a>
##### privatekey (required)

- Schema name: `Privatekey`

PEM-encoded private key corresponding to the certificate. `null` if no private key is available or for imported certificates without keys.
<a id="CHANGED_fields_privatekey_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_privatekey_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_privatekey_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_CHANGED_fields_privatekey_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_privatekey_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_CSR"></a>
<a id="CHANGED_fields_CSR"></a>
##### CSR (required)

- Schema name: `Csr`

PEM-encoded Certificate Signing Request (CSR) data. `null` for imported certificates or completed ACME certificates.
<a id="CHANGED_fields_CSR_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_CSR_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_CSR_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_CHANGED_fields_CSR_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_CSR_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_acme_uri"></a>
<a id="CHANGED_fields_acme_uri"></a>
##### acme_uri (required)

- Schema name: `Acme Uri`

ACME directory server URI used for automated certificate management. `null` for non-ACME certificates.
<a id="CHANGED_fields_acme_uri_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_acme_uri_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_acme_uri_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_acme_uri_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_acme_uri_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_domains_authenticators"></a>
<a id="CHANGED_fields_domains_authenticators"></a>
##### domains_authenticators (required)

- Schema name: `Domains Authenticators`

Mapping of domain names to ACME DNS authenticator IDs for domain validation. `null` for non-ACME certificates.
<a id="CHANGED_fields_domains_authenticators_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_domains_authenticators_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_domains_authenticators_anyOf_i0)

- Type: object

<a id="tab-pane_CHANGED_fields_domains_authenticators_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_domains_authenticators_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_renew_days"></a>
<a id="CHANGED_fields_renew_days"></a>
##### renew_days (required)

- Schema name: `Renew Days`

Number of days before expiration to attempt automatic renewal. Only applicable for ACME certificates. `null` for non-renewable certificates.
<a id="CHANGED_fields_renew_days_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_renew_days_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_renew_days_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_renew_days_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_renew_days_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_acme"></a>
<a id="CHANGED_fields_acme"></a>
##### acme (required)

- Schema name: `Acme`

ACME registration and account information used for certificate lifecycle management. `null` for non-ACME certificates.
<a id="CHANGED_fields_acme_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_acme_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_acme_anyOf_i0)

- Type: object

<a id="tab-pane_CHANGED_fields_acme_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_acme_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_add_to_trusted_store"></a>
<a id="CHANGED_fields_add_to_trusted_store"></a>
##### add_to_trusted_store (required)

- Schema name: `Add To Trusted Store`
- Type: boolean

Whether this certificate should be added to the system's trusted certificate store.

<a id="headingCHANGED_fields_root_path"></a>
<a id="CHANGED_fields_root_path"></a>
##### root_path (required)

- Schema name: `Root Path`
- Type: string

Filesystem path where certificate-related files are stored.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_certificate_path"></a>
<a id="CHANGED_fields_certificate_path"></a>
##### certificate_path (required)

- Schema name: `Certificate Path`

Filesystem path to the certificate file (.crt). `null` if no certificate is available.
<a id="CHANGED_fields_certificate_path_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_certificate_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_certificate_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_certificate_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_certificate_path_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_privatekey_path"></a>
<a id="CHANGED_fields_privatekey_path"></a>
##### privatekey_path (required)

- Schema name: `Privatekey Path`

Filesystem path to the private key file (.key). `null` if no private key is available.
<a id="CHANGED_fields_privatekey_path_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_privatekey_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_privatekey_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_privatekey_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_privatekey_path_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_csr_path"></a>
<a id="CHANGED_fields_csr_path"></a>
##### csr_path (required)

- Schema name: `Csr Path`

Filesystem path to the certificate signing request file (.csr). `null` if no CSR is available.
<a id="CHANGED_fields_csr_path_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_csr_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_csr_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_csr_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_csr_path_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_cert_type"></a>
<a id="CHANGED_fields_cert_type"></a>
##### cert_type (required)

- Schema name: `Cert Type`
- Type: string

Human-readable certificate type, typically 'CERTIFICATE' for standard certificates.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_cert_type_existing"></a>
<a id="CHANGED_fields_cert_type_existing"></a>
##### cert_type_existing (required)

- Schema name: `Cert Type Existing`
- Type: boolean

Whether this is an existing certificate (imported or generated).

<a id="headingCHANGED_fields_cert_type_CSR"></a>
<a id="CHANGED_fields_cert_type_CSR"></a>
##### cert_type_CSR (required)

- Schema name: `Cert Type Csr`
- Type: boolean

Whether this entry represents a Certificate Signing Request (CSR) rather than a signed certificate.

<a id="headingCHANGED_fields_cert_type_CA"></a>
<a id="CHANGED_fields_cert_type_CA"></a>
##### cert_type_CA (required)

- Schema name: `Cert Type Ca`
- Type: boolean

Whether this certificate is a Certificate Authority (CA) certificate.

<a id="headingCHANGED_fields_chain_list"></a>
<a id="CHANGED_fields_chain_list"></a>
##### chain_list (required)

- Schema name: `Chain List`
- Type: array of string

Array of PEM-encoded certificates in the certificate chain, starting with the leaf certificate.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_chain_list_items"></a>
- Type: string
- Must be at most `2147483647` characters long

<a id="headingCHANGED_fields_key_length"></a>
<a id="CHANGED_fields_key_length"></a>
##### key_length (required)

- Schema name: `Key Length`

Size of the cryptographic key in bits. `null` if key information is unavailable.
<a id="CHANGED_fields_key_length_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_key_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_key_length_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_key_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_key_length_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_key_type"></a>
<a id="CHANGED_fields_key_type"></a>
##### key_type (required)

- Schema name: `Key Type`

Type of cryptographic key algorithm (e.g., 'RSA', 'EC', 'DSA'). `null` if key information is unavailable.
<a id="CHANGED_fields_key_type_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_key_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_key_type_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_key_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_key_type_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_country"></a>
<a id="CHANGED_fields_country"></a>
##### country (required)

- Schema name: `Country`

ISO 3166-1 alpha-2 country code from the certificate subject. `null` if not specified.
<a id="CHANGED_fields_country_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_country_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_country_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_country_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_country_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_state"></a>
<a id="CHANGED_fields_state"></a>
##### state (required)

- Schema name: `State`

State or province name from the certificate subject. `null` if not specified.
<a id="CHANGED_fields_state_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_state_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_state_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_state_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_state_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_city"></a>
<a id="CHANGED_fields_city"></a>
##### city (required)

- Schema name: `City`

City or locality name from the certificate subject. `null` if not specified.
<a id="CHANGED_fields_city_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_city_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_city_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_city_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_city_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_organization"></a>
<a id="CHANGED_fields_organization"></a>
##### organization (required)

- Schema name: `Organization`

Organization name from the certificate subject. `null` if not specified.
<a id="CHANGED_fields_organization_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_organization_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_organization_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_organization_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_organization_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_organizational_unit"></a>
<a id="CHANGED_fields_organizational_unit"></a>
##### organizational_unit (required)

- Schema name: `Organizational Unit`

Organizational unit from the certificate subject. `null` if not specified.
<a id="CHANGED_fields_organizational_unit_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_organizational_unit_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_organizational_unit_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_organizational_unit_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_organizational_unit_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_common"></a>
<a id="CHANGED_fields_common"></a>
##### common (required)

- Schema name: `Common`

Common name (CN) from the certificate subject. `null` if not specified.
<a id="CHANGED_fields_common_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_common_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_common_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_common_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_common_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_san"></a>
<a id="CHANGED_fields_san"></a>
##### san (required)

- Schema name: `San`

Subject Alternative Names (SAN) from the certificate extension. `null` if no SAN extension is present.
<a id="CHANGED_fields_san_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_san_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_san_anyOf_i0)

- Type: array of string
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_san_anyOf_i0_items"></a>
- Type: string

<a id="tab-pane_CHANGED_fields_san_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_san_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_email"></a>
<a id="CHANGED_fields_email"></a>
##### email (required)

- Schema name: `Email`

Email address from the certificate subject. `null` if not specified.
<a id="CHANGED_fields_email_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_email_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_email_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_email_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_email_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_DN"></a>
<a id="CHANGED_fields_DN"></a>
##### DN (required)

- Schema name: `Dn`

Distinguished Name (DN) of the certificate subject in RFC 2253 format. `null` if certificate parsing failed.
<a id="CHANGED_fields_DN_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_DN_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_DN_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_CHANGED_fields_DN_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_DN_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_subject_name_hash"></a>
<a id="CHANGED_fields_subject_name_hash"></a>
##### subject_name_hash (required)

- Schema name: `Subject Name Hash`

Hash of the certificate subject name. `null` if certificate parsing failed.
<a id="CHANGED_fields_subject_name_hash_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_subject_name_hash_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_subject_name_hash_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_subject_name_hash_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_subject_name_hash_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_extensions"></a>
<a id="CHANGED_fields_extensions"></a>
##### extensions (required)

- Schema name: `Extensions`
- Type: object

X.509 certificate extensions parsed into a dictionary structure.

<a id="headingCHANGED_fields_digest_algorithm"></a>
<a id="CHANGED_fields_digest_algorithm"></a>
##### digest_algorithm (required)

- Schema name: `Digest Algorithm`

Cryptographic hash algorithm used for certificate signing (e.g., 'SHA256'). `null` if unavailable.
<a id="CHANGED_fields_digest_algorithm_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_digest_algorithm_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_digest_algorithm_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_digest_algorithm_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_digest_algorithm_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_lifetime"></a>
<a id="CHANGED_fields_lifetime"></a>
##### lifetime (required)

- Schema name: `Lifetime`

Certificate validity period in seconds. `null` if certificate parsing failed.
<a id="CHANGED_fields_lifetime_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_lifetime_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_lifetime_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_lifetime_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_lifetime_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_from"></a>
<a id="CHANGED_fields_from"></a>
##### from (required)

- Schema name: `From`

Certificate validity start date in ISO 8601 format. `null` if certificate parsing failed.
<a id="CHANGED_fields_from_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_from_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_from_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_from_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_from_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_until"></a>
<a id="CHANGED_fields_until"></a>
##### until (required)

- Schema name: `Until`

Certificate validity end date in ISO 8601 format. `null` if certificate parsing failed.
<a id="CHANGED_fields_until_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_until_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_until_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_until_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_until_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_serial"></a>
<a id="CHANGED_fields_serial"></a>
##### serial (required)

- Schema name: `Serial`

Certificate serial number. `null` if certificate parsing failed.
<a id="CHANGED_fields_serial_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_serial_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_serial_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_serial_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_serial_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_chain"></a>
<a id="CHANGED_fields_chain"></a>
##### chain (required)

- Schema name: `Chain`

Whether this certificate has an associated certificate chain. `null` if unavailable.
<a id="CHANGED_fields_chain_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_chain_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_chain_anyOf_i0)

- Type: boolean

<a id="tab-pane_CHANGED_fields_chain_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_chain_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_fingerprint"></a>
<a id="CHANGED_fields_fingerprint"></a>
##### fingerprint (required)

- Schema name: `Fingerprint`

SHA-256 fingerprint of the certificate in hexadecimal format. `null` if certificate parsing failed.
<a id="CHANGED_fields_fingerprint_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_fingerprint_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_fingerprint_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_fingerprint_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_fingerprint_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_expired"></a>
<a id="CHANGED_fields_expired"></a>
##### expired (required)

- Schema name: `Expired`

Whether the certificate has expired. `null` if certificate parsing failed.
<a id="CHANGED_fields_expired_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_expired_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_expired_anyOf_i0)

- Type: boolean

<a id="tab-pane_CHANGED_fields_expired_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_expired_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_parsed"></a>
<a id="CHANGED_fields_parsed"></a>
##### parsed (required)

- Schema name: `Parsed`
- Type: boolean

Whether the certificate data was successfully parsed and validated.

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `CertificateRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
