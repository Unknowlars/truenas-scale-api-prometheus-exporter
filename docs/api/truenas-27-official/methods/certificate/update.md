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

Update certificate of `id`.

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

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the certificate to update.

#### Parameter 2: certificate_update

<a id="Call_parameters_items_i1"></a>
#### certificate_update

- Schema name: `certificate_update`
- Type: object

Updated certificate configuration data.
- No Additional Properties
<a id="headingCall_parameters_items_i1_renew_days"></a>
<a id="Call_parameters_items_i1_renew_days"></a>
##### renew_days

- Schema name: `Renew Days`
- Type: integer

Days before expiration to attempt renewal.
- Value must be greater or equal to `1` and lesser or equal to `30`

<a id="headingCall_parameters_items_i1_add_to_trusted_store"></a>
<a id="Call_parameters_items_i1_add_to_trusted_store"></a>
##### add_to_trusted_store

- Schema name: `Add To Trusted Store`
- Type: boolean

Whether to add this certificate to the trusted certificate store.

<a id="headingCall_parameters_items_i1_name"></a>
<a id="Call_parameters_items_i1_name"></a>
##### name

- Schema name: `Name`
- Type: string

Certificate name.
- Must be at least `1` characters long
- Must be at most `120` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `CertificateEntry`
- Type: object

The updated certificate configuration.
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
- Must be at most `2147483647` characters long

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
- Must be at most `2147483647` characters long

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
- Must be at most `2147483647` characters long

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
- Must be at most `2147483647` characters long

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
- Must be at most `2147483647` characters long

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
