---
title: certificate.query
kind: method
source_rst: _sources/api_methods_certificate.query.rst.txt
source_html: api_methods_certificate.query.html
required_roles:
  - CERTIFICATE_READ
---

# certificate.query

## Required Roles

- `CERTIFICATE_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filters

<a id="Call_parameters_items_i0"></a>
#### filters

- Schema name: `filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i0_items"></a>
- Type: object

Examples:

```json
[
    [
        "name",
        "=",
        "bob"
    ]
]
```
Examples:

```json
[
    [
        "OR",
        [
            [
                "name",
                "=",
                "bob"
            ],
            [
                "name",
                "=",
                "larry"
            ]
        ]
    ]
]
```

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object
- Default:
```json
{
  "extra": {},
  "order_by": [],
  "select": [],
  "count": false,
  "get": false,
  "offset": 0,
  "limit": 0,
  "force_sql_filters": false
}
```

Query options including pagination, ordering, and additional parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i1_extra"></a>
<a id="Call_parameters_items_i1_extra"></a>
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

<a id="headingCall_parameters_items_i1_order_by"></a>
<a id="Call_parameters_items_i1_order_by"></a>
##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_order_by_items"></a>
- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

<a id="headingCall_parameters_items_i1_select"></a>
<a id="Call_parameters_items_i1_select"></a>
##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items"></a>
<a id="Call_parameters_items_i1_select_items_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i1)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items_anyOf_i1_items"></a>
- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

<a id="headingCall_parameters_items_i1_count"></a>
<a id="Call_parameters_items_i1_count"></a>
##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

<a id="headingCall_parameters_items_i1_get"></a>
<a id="Call_parameters_items_i1_get"></a>
##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

<a id="headingCall_parameters_items_i1_offset"></a>
<a id="Call_parameters_items_i1_offset"></a>
##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0`

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0` and lesser or equal to `10000`

<a id="headingCall_parameters_items_i1_force_sql_filters"></a>
<a id="Call_parameters_items_i1_force_sql_filters"></a>
##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items"></a>
###### CertificateEntry

- Schema name: `CertificateEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_id"></a>
<a id="Return_value_anyOf_i0_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this certificate entry.

<a id="headingReturn_value_anyOf_i0_items_type"></a>
<a id="Return_value_anyOf_i0_items_type"></a>
###### type (required)

- Schema name: `Type`
- Type: integer

Internal certificate type identifier used to determine certificate capabilities.

<a id="headingReturn_value_anyOf_i0_items_name"></a>
<a id="Return_value_anyOf_i0_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for this certificate. Must be unique and contain only alphanumeric characters, dashes, and underscores.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_certificate"></a>
<a id="Return_value_anyOf_i0_items_certificate"></a>
###### certificate (required)

- Schema name: `Certificate`

PEM-encoded X.509 certificate data. `null` for certificate signing requests (CSR) that have not yet been signed.
<a id="Return_value_anyOf_i0_items_certificate_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_certificate_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_certificate_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_certificate_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_certificate_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_privatekey"></a>
<a id="Return_value_anyOf_i0_items_privatekey"></a>
###### privatekey (required)

- Schema name: `Privatekey`

PEM-encoded private key corresponding to the certificate. `null` if no private key is available or for imported certificates without keys.
<a id="Return_value_anyOf_i0_items_privatekey_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_privatekey_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_privatekey_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_privatekey_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_privatekey_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_CSR"></a>
<a id="Return_value_anyOf_i0_items_CSR"></a>
###### CSR (required)

- Schema name: `Csr`

PEM-encoded Certificate Signing Request (CSR) data. `null` for imported certificates or completed ACME certificates.
<a id="Return_value_anyOf_i0_items_CSR_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_CSR_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_CSR_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_CSR_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_CSR_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_acme_uri"></a>
<a id="Return_value_anyOf_i0_items_acme_uri"></a>
###### acme_uri (required)

- Schema name: `Acme Uri`

ACME directory server URI used for automated certificate management. `null` for non-ACME certificates.
<a id="Return_value_anyOf_i0_items_acme_uri_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_acme_uri_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_acme_uri_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_acme_uri_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_acme_uri_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_domains_authenticators"></a>
<a id="Return_value_anyOf_i0_items_domains_authenticators"></a>
###### domains_authenticators (required)

- Schema name: `Domains Authenticators`

Mapping of domain names to ACME DNS authenticator IDs for domain validation. `null` for non-ACME certificates.
<a id="Return_value_anyOf_i0_items_domains_authenticators_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_domains_authenticators_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_domains_authenticators_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i0_items_domains_authenticators_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_domains_authenticators_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_renew_days"></a>
<a id="Return_value_anyOf_i0_items_renew_days"></a>
###### renew_days (required)

- Schema name: `Renew Days`

Number of days before expiration to attempt automatic renewal. Only applicable for ACME certificates. `null` for non-renewable certificates.
<a id="Return_value_anyOf_i0_items_renew_days_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_renew_days_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_renew_days_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_renew_days_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_renew_days_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_acme"></a>
<a id="Return_value_anyOf_i0_items_acme"></a>
###### acme (required)

- Schema name: `Acme`

ACME registration and account information used for certificate lifecycle management. `null` for non-ACME certificates.
<a id="Return_value_anyOf_i0_items_acme_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_acme_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_acme_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i0_items_acme_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_acme_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_add_to_trusted_store"></a>
<a id="Return_value_anyOf_i0_items_add_to_trusted_store"></a>
###### add_to_trusted_store (required)

- Schema name: `Add To Trusted Store`
- Type: boolean

Whether this certificate should be added to the system's trusted certificate store.

<a id="headingReturn_value_anyOf_i0_items_root_path"></a>
<a id="Return_value_anyOf_i0_items_root_path"></a>
###### root_path (required)

- Schema name: `Root Path`
- Type: string

Filesystem path where certificate-related files are stored.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_certificate_path"></a>
<a id="Return_value_anyOf_i0_items_certificate_path"></a>
###### certificate_path (required)

- Schema name: `Certificate Path`

Filesystem path to the certificate file (.crt). `null` if no certificate is available.
<a id="Return_value_anyOf_i0_items_certificate_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_certificate_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_certificate_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_certificate_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_certificate_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_privatekey_path"></a>
<a id="Return_value_anyOf_i0_items_privatekey_path"></a>
###### privatekey_path (required)

- Schema name: `Privatekey Path`

Filesystem path to the private key file (.key). `null` if no private key is available.
<a id="Return_value_anyOf_i0_items_privatekey_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_privatekey_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_privatekey_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_privatekey_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_privatekey_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_csr_path"></a>
<a id="Return_value_anyOf_i0_items_csr_path"></a>
###### csr_path (required)

- Schema name: `Csr Path`

Filesystem path to the certificate signing request file (.csr). `null` if no CSR is available.
<a id="Return_value_anyOf_i0_items_csr_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_csr_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_csr_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_csr_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_csr_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_cert_type"></a>
<a id="Return_value_anyOf_i0_items_cert_type"></a>
###### cert_type (required)

- Schema name: `Cert Type`
- Type: string

Human-readable certificate type, typically 'CERTIFICATE' for standard certificates.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_cert_type_existing"></a>
<a id="Return_value_anyOf_i0_items_cert_type_existing"></a>
###### cert_type_existing (required)

- Schema name: `Cert Type Existing`
- Type: boolean

Whether this is an existing certificate (imported or generated).

<a id="headingReturn_value_anyOf_i0_items_cert_type_CSR"></a>
<a id="Return_value_anyOf_i0_items_cert_type_CSR"></a>
###### cert_type_CSR (required)

- Schema name: `Cert Type Csr`
- Type: boolean

Whether this entry represents a Certificate Signing Request (CSR) rather than a signed certificate.

<a id="headingReturn_value_anyOf_i0_items_cert_type_CA"></a>
<a id="Return_value_anyOf_i0_items_cert_type_CA"></a>
###### cert_type_CA (required)

- Schema name: `Cert Type Ca`
- Type: boolean

Whether this certificate is a Certificate Authority (CA) certificate.

<a id="headingReturn_value_anyOf_i0_items_chain_list"></a>
<a id="Return_value_anyOf_i0_items_chain_list"></a>
###### chain_list (required)

- Schema name: `Chain List`
- Type: array of string

Array of PEM-encoded certificates in the certificate chain, starting with the leaf certificate.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_chain_list_items"></a>
- Type: string
- Must be at most `2147483647` characters long

<a id="headingReturn_value_anyOf_i0_items_key_length"></a>
<a id="Return_value_anyOf_i0_items_key_length"></a>
###### key_length (required)

- Schema name: `Key Length`

Size of the cryptographic key in bits. `null` if key information is unavailable.
<a id="Return_value_anyOf_i0_items_key_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_key_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_key_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_key_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_key_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_key_type"></a>
<a id="Return_value_anyOf_i0_items_key_type"></a>
###### key_type (required)

- Schema name: `Key Type`

Type of cryptographic key algorithm (e.g., 'RSA', 'EC', 'DSA'). `null` if key information is unavailable.
<a id="Return_value_anyOf_i0_items_key_type_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_key_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_key_type_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_key_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_key_type_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_country"></a>
<a id="Return_value_anyOf_i0_items_country"></a>
###### country (required)

- Schema name: `Country`

ISO 3166-1 alpha-2 country code from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i0_items_country_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_country_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_country_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_country_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_country_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_state"></a>
<a id="Return_value_anyOf_i0_items_state"></a>
###### state (required)

- Schema name: `State`

State or province name from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i0_items_state_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_state_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_state_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_state_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_state_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_city"></a>
<a id="Return_value_anyOf_i0_items_city"></a>
###### city (required)

- Schema name: `City`

City or locality name from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i0_items_city_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_city_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_city_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_city_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_city_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_organization"></a>
<a id="Return_value_anyOf_i0_items_organization"></a>
###### organization (required)

- Schema name: `Organization`

Organization name from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i0_items_organization_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_organization_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_organization_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_organization_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_organization_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_organizational_unit"></a>
<a id="Return_value_anyOf_i0_items_organizational_unit"></a>
###### organizational_unit (required)

- Schema name: `Organizational Unit`

Organizational unit from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i0_items_organizational_unit_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_organizational_unit_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_organizational_unit_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_organizational_unit_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_organizational_unit_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_common"></a>
<a id="Return_value_anyOf_i0_items_common"></a>
###### common (required)

- Schema name: `Common`

Common name (CN) from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i0_items_common_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_common_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_common_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_common_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_common_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_san"></a>
<a id="Return_value_anyOf_i0_items_san"></a>
###### san (required)

- Schema name: `San`

Subject Alternative Names (SAN) from the certificate extension. `null` if no SAN extension is present.
<a id="Return_value_anyOf_i0_items_san_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_san_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_san_anyOf_i0)

- Type: array of string
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_san_anyOf_i0_items"></a>
- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_san_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_san_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_email"></a>
<a id="Return_value_anyOf_i0_items_email"></a>
###### email (required)

- Schema name: `Email`

Email address from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i0_items_email_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_email_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_email_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_email_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_email_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_DN"></a>
<a id="Return_value_anyOf_i0_items_DN"></a>
###### DN (required)

- Schema name: `Dn`

Distinguished Name (DN) of the certificate subject in RFC 2253 format. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i0_items_DN_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_DN_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_DN_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_DN_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_DN_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_subject_name_hash"></a>
<a id="Return_value_anyOf_i0_items_subject_name_hash"></a>
###### subject_name_hash (required)

- Schema name: `Subject Name Hash`

Hash of the certificate subject name. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i0_items_subject_name_hash_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_subject_name_hash_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_subject_name_hash_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_subject_name_hash_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_subject_name_hash_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_extensions"></a>
<a id="Return_value_anyOf_i0_items_extensions"></a>
###### extensions (required)

- Schema name: `Extensions`
- Type: object

X.509 certificate extensions parsed into a dictionary structure.

<a id="headingReturn_value_anyOf_i0_items_digest_algorithm"></a>
<a id="Return_value_anyOf_i0_items_digest_algorithm"></a>
###### digest_algorithm (required)

- Schema name: `Digest Algorithm`

Cryptographic hash algorithm used for certificate signing (e.g., 'SHA256'). `null` if unavailable.
<a id="Return_value_anyOf_i0_items_digest_algorithm_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_digest_algorithm_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_digest_algorithm_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_digest_algorithm_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_digest_algorithm_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_lifetime"></a>
<a id="Return_value_anyOf_i0_items_lifetime"></a>
###### lifetime (required)

- Schema name: `Lifetime`

Certificate validity period in seconds. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i0_items_lifetime_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_lifetime_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_lifetime_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_lifetime_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_lifetime_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_from"></a>
<a id="Return_value_anyOf_i0_items_from"></a>
###### from (required)

- Schema name: `From`

Certificate validity start date in ISO 8601 format. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i0_items_from_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_from_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_from_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_from_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_from_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_until"></a>
<a id="Return_value_anyOf_i0_items_until"></a>
###### until (required)

- Schema name: `Until`

Certificate validity end date in ISO 8601 format. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i0_items_until_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_until_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_until_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_until_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_until_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_serial"></a>
<a id="Return_value_anyOf_i0_items_serial"></a>
###### serial (required)

- Schema name: `Serial`

Certificate serial number. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i0_items_serial_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_serial_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_serial_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_serial_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_serial_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_chain"></a>
<a id="Return_value_anyOf_i0_items_chain"></a>
###### chain (required)

- Schema name: `Chain`

Whether this certificate has an associated certificate chain. `null` if unavailable.
<a id="Return_value_anyOf_i0_items_chain_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_chain_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_chain_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_anyOf_i0_items_chain_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_chain_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_fingerprint"></a>
<a id="Return_value_anyOf_i0_items_fingerprint"></a>
###### fingerprint (required)

- Schema name: `Fingerprint`

SHA-256 fingerprint of the certificate in hexadecimal format. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i0_items_fingerprint_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_fingerprint_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_fingerprint_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_fingerprint_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_fingerprint_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_expired"></a>
<a id="Return_value_anyOf_i0_items_expired"></a>
###### expired (required)

- Schema name: `Expired`

Whether the certificate has expired. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i0_items_expired_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_expired_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_expired_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_anyOf_i0_items_expired_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_expired_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_parsed"></a>
<a id="Return_value_anyOf_i0_items_parsed"></a>
###### parsed (required)

- Schema name: `Parsed`
- Type: boolean

Whether the certificate data was successfully parsed and validated.

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [CertificateEntry](#tab-pane_Return_value_anyOf_i1)

- Schema name: `CertificateEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_id"></a>
<a id="Return_value_anyOf_i1_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this certificate entry.

<a id="headingReturn_value_anyOf_i1_type"></a>
<a id="Return_value_anyOf_i1_type"></a>
###### type (required)

- Schema name: `Type`
- Type: integer

Internal certificate type identifier used to determine certificate capabilities.

<a id="headingReturn_value_anyOf_i1_name"></a>
<a id="Return_value_anyOf_i1_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for this certificate. Must be unique and contain only alphanumeric characters, dashes, and underscores.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_certificate"></a>
<a id="Return_value_anyOf_i1_certificate"></a>
###### certificate (required)

- Schema name: `Certificate`

PEM-encoded X.509 certificate data. `null` for certificate signing requests (CSR) that have not yet been signed.
<a id="Return_value_anyOf_i1_certificate_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_certificate_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_certificate_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i1_certificate_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_certificate_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_privatekey"></a>
<a id="Return_value_anyOf_i1_privatekey"></a>
###### privatekey (required)

- Schema name: `Privatekey`

PEM-encoded private key corresponding to the certificate. `null` if no private key is available or for imported certificates without keys.
<a id="Return_value_anyOf_i1_privatekey_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_privatekey_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_privatekey_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i1_privatekey_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_privatekey_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_CSR"></a>
<a id="Return_value_anyOf_i1_CSR"></a>
###### CSR (required)

- Schema name: `Csr`

PEM-encoded Certificate Signing Request (CSR) data. `null` for imported certificates or completed ACME certificates.
<a id="Return_value_anyOf_i1_CSR_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_CSR_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_CSR_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i1_CSR_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_CSR_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_acme_uri"></a>
<a id="Return_value_anyOf_i1_acme_uri"></a>
###### acme_uri (required)

- Schema name: `Acme Uri`

ACME directory server URI used for automated certificate management. `null` for non-ACME certificates.
<a id="Return_value_anyOf_i1_acme_uri_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_acme_uri_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_acme_uri_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_acme_uri_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_acme_uri_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_domains_authenticators"></a>
<a id="Return_value_anyOf_i1_domains_authenticators"></a>
###### domains_authenticators (required)

- Schema name: `Domains Authenticators`

Mapping of domain names to ACME DNS authenticator IDs for domain validation. `null` for non-ACME certificates.
<a id="Return_value_anyOf_i1_domains_authenticators_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_domains_authenticators_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_domains_authenticators_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_domains_authenticators_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_domains_authenticators_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_renew_days"></a>
<a id="Return_value_anyOf_i1_renew_days"></a>
###### renew_days (required)

- Schema name: `Renew Days`

Number of days before expiration to attempt automatic renewal. Only applicable for ACME certificates. `null` for non-renewable certificates.
<a id="Return_value_anyOf_i1_renew_days_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_renew_days_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_renew_days_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_renew_days_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_renew_days_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_acme"></a>
<a id="Return_value_anyOf_i1_acme"></a>
###### acme (required)

- Schema name: `Acme`

ACME registration and account information used for certificate lifecycle management. `null` for non-ACME certificates.
<a id="Return_value_anyOf_i1_acme_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_acme_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_acme_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_acme_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_acme_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_add_to_trusted_store"></a>
<a id="Return_value_anyOf_i1_add_to_trusted_store"></a>
###### add_to_trusted_store (required)

- Schema name: `Add To Trusted Store`
- Type: boolean

Whether this certificate should be added to the system's trusted certificate store.

<a id="headingReturn_value_anyOf_i1_root_path"></a>
<a id="Return_value_anyOf_i1_root_path"></a>
###### root_path (required)

- Schema name: `Root Path`
- Type: string

Filesystem path where certificate-related files are stored.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_certificate_path"></a>
<a id="Return_value_anyOf_i1_certificate_path"></a>
###### certificate_path (required)

- Schema name: `Certificate Path`

Filesystem path to the certificate file (.crt). `null` if no certificate is available.
<a id="Return_value_anyOf_i1_certificate_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_certificate_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_certificate_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i1_certificate_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_certificate_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_privatekey_path"></a>
<a id="Return_value_anyOf_i1_privatekey_path"></a>
###### privatekey_path (required)

- Schema name: `Privatekey Path`

Filesystem path to the private key file (.key). `null` if no private key is available.
<a id="Return_value_anyOf_i1_privatekey_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_privatekey_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_privatekey_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i1_privatekey_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_privatekey_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_csr_path"></a>
<a id="Return_value_anyOf_i1_csr_path"></a>
###### csr_path (required)

- Schema name: `Csr Path`

Filesystem path to the certificate signing request file (.csr). `null` if no CSR is available.
<a id="Return_value_anyOf_i1_csr_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_csr_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_csr_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i1_csr_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_csr_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_cert_type"></a>
<a id="Return_value_anyOf_i1_cert_type"></a>
###### cert_type (required)

- Schema name: `Cert Type`
- Type: string

Human-readable certificate type, typically 'CERTIFICATE' for standard certificates.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_cert_type_existing"></a>
<a id="Return_value_anyOf_i1_cert_type_existing"></a>
###### cert_type_existing (required)

- Schema name: `Cert Type Existing`
- Type: boolean

Whether this is an existing certificate (imported or generated).

<a id="headingReturn_value_anyOf_i1_cert_type_CSR"></a>
<a id="Return_value_anyOf_i1_cert_type_CSR"></a>
###### cert_type_CSR (required)

- Schema name: `Cert Type Csr`
- Type: boolean

Whether this entry represents a Certificate Signing Request (CSR) rather than a signed certificate.

<a id="headingReturn_value_anyOf_i1_cert_type_CA"></a>
<a id="Return_value_anyOf_i1_cert_type_CA"></a>
###### cert_type_CA (required)

- Schema name: `Cert Type Ca`
- Type: boolean

Whether this certificate is a Certificate Authority (CA) certificate.

<a id="headingReturn_value_anyOf_i1_chain_list"></a>
<a id="Return_value_anyOf_i1_chain_list"></a>
###### chain_list (required)

- Schema name: `Chain List`
- Type: array of string

Array of PEM-encoded certificates in the certificate chain, starting with the leaf certificate.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_chain_list_items"></a>
- Type: string
- Must be at most `2147483647` characters long

<a id="headingReturn_value_anyOf_i1_key_length"></a>
<a id="Return_value_anyOf_i1_key_length"></a>
###### key_length (required)

- Schema name: `Key Length`

Size of the cryptographic key in bits. `null` if key information is unavailable.
<a id="Return_value_anyOf_i1_key_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_key_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_key_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_key_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_key_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_key_type"></a>
<a id="Return_value_anyOf_i1_key_type"></a>
###### key_type (required)

- Schema name: `Key Type`

Type of cryptographic key algorithm (e.g., 'RSA', 'EC', 'DSA'). `null` if key information is unavailable.
<a id="Return_value_anyOf_i1_key_type_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_key_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_key_type_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i1_key_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_key_type_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_country"></a>
<a id="Return_value_anyOf_i1_country"></a>
###### country (required)

- Schema name: `Country`

ISO 3166-1 alpha-2 country code from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i1_country_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_country_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_country_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_country_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_country_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_state"></a>
<a id="Return_value_anyOf_i1_state"></a>
###### state (required)

- Schema name: `State`

State or province name from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i1_state_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_state_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_state_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_state_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_state_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_city"></a>
<a id="Return_value_anyOf_i1_city"></a>
###### city (required)

- Schema name: `City`

City or locality name from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i1_city_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_city_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_city_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_city_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_city_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_organization"></a>
<a id="Return_value_anyOf_i1_organization"></a>
###### organization (required)

- Schema name: `Organization`

Organization name from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i1_organization_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_organization_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_organization_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_organization_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_organization_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_organizational_unit"></a>
<a id="Return_value_anyOf_i1_organizational_unit"></a>
###### organizational_unit (required)

- Schema name: `Organizational Unit`

Organizational unit from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i1_organizational_unit_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_organizational_unit_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_organizational_unit_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_organizational_unit_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_organizational_unit_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_common"></a>
<a id="Return_value_anyOf_i1_common"></a>
###### common (required)

- Schema name: `Common`

Common name (CN) from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i1_common_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_common_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_common_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_common_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_common_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_san"></a>
<a id="Return_value_anyOf_i1_san"></a>
###### san (required)

- Schema name: `San`

Subject Alternative Names (SAN) from the certificate extension. `null` if no SAN extension is present.
<a id="Return_value_anyOf_i1_san_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_san_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_san_anyOf_i0)

- Type: array of string
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_san_anyOf_i0_items"></a>
- Type: string

<a id="tab-pane_Return_value_anyOf_i1_san_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_san_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_email"></a>
<a id="Return_value_anyOf_i1_email"></a>
###### email (required)

- Schema name: `Email`

Email address from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i1_email_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_email_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_email_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_email_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_email_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_DN"></a>
<a id="Return_value_anyOf_i1_DN"></a>
###### DN (required)

- Schema name: `Dn`

Distinguished Name (DN) of the certificate subject in RFC 2253 format. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i1_DN_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_DN_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_DN_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i1_DN_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_DN_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_subject_name_hash"></a>
<a id="Return_value_anyOf_i1_subject_name_hash"></a>
###### subject_name_hash (required)

- Schema name: `Subject Name Hash`

Hash of the certificate subject name. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i1_subject_name_hash_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_subject_name_hash_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_subject_name_hash_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_subject_name_hash_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_subject_name_hash_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_extensions"></a>
<a id="Return_value_anyOf_i1_extensions"></a>
###### extensions (required)

- Schema name: `Extensions`
- Type: object

X.509 certificate extensions parsed into a dictionary structure.

<a id="headingReturn_value_anyOf_i1_digest_algorithm"></a>
<a id="Return_value_anyOf_i1_digest_algorithm"></a>
###### digest_algorithm (required)

- Schema name: `Digest Algorithm`

Cryptographic hash algorithm used for certificate signing (e.g., 'SHA256'). `null` if unavailable.
<a id="Return_value_anyOf_i1_digest_algorithm_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_digest_algorithm_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_digest_algorithm_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_digest_algorithm_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_digest_algorithm_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_lifetime"></a>
<a id="Return_value_anyOf_i1_lifetime"></a>
###### lifetime (required)

- Schema name: `Lifetime`

Certificate validity period in seconds. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i1_lifetime_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_lifetime_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_lifetime_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_lifetime_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_lifetime_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_from"></a>
<a id="Return_value_anyOf_i1_from"></a>
###### from (required)

- Schema name: `From`

Certificate validity start date in ISO 8601 format. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i1_from_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_from_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_from_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_from_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_from_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_until"></a>
<a id="Return_value_anyOf_i1_until"></a>
###### until (required)

- Schema name: `Until`

Certificate validity end date in ISO 8601 format. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i1_until_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_until_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_until_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_until_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_until_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_serial"></a>
<a id="Return_value_anyOf_i1_serial"></a>
###### serial (required)

- Schema name: `Serial`

Certificate serial number. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i1_serial_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_serial_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_serial_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_serial_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_serial_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_chain"></a>
<a id="Return_value_anyOf_i1_chain"></a>
###### chain (required)

- Schema name: `Chain`

Whether this certificate has an associated certificate chain. `null` if unavailable.
<a id="Return_value_anyOf_i1_chain_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_chain_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_chain_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_anyOf_i1_chain_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_chain_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_fingerprint"></a>
<a id="Return_value_anyOf_i1_fingerprint"></a>
###### fingerprint (required)

- Schema name: `Fingerprint`

SHA-256 fingerprint of the certificate in hexadecimal format. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i1_fingerprint_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_fingerprint_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_fingerprint_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_fingerprint_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_fingerprint_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_expired"></a>
<a id="Return_value_anyOf_i1_expired"></a>
###### expired (required)

- Schema name: `Expired`

Whether the certificate has expired. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i1_expired_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_expired_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_expired_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_anyOf_i1_expired_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_expired_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_parsed"></a>
<a id="Return_value_anyOf_i1_parsed"></a>
###### parsed (required)

- Schema name: `Parsed`
- Type: boolean

Whether the certificate data was successfully parsed and validated.

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items"></a>
###### CertificateQueryResultItem

- Schema name: `CertificateQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_id"></a>
<a id="Return_value_anyOf_i2_items_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for this certificate entry.

<a id="headingReturn_value_anyOf_i2_items_type"></a>
<a id="Return_value_anyOf_i2_items_type"></a>
###### type

- Schema name: `Type`
- Type: integer

Internal certificate type identifier used to determine certificate capabilities.

<a id="headingReturn_value_anyOf_i2_items_name"></a>
<a id="Return_value_anyOf_i2_items_name"></a>
###### name

- Schema name: `Name`
- Type: string

Human-readable name for this certificate. Must be unique and contain only alphanumeric characters, dashes, and underscores.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_certificate"></a>
<a id="Return_value_anyOf_i2_items_certificate"></a>
###### certificate

- Schema name: `Certificate`

PEM-encoded X.509 certificate data. `null` for certificate signing requests (CSR) that have not yet been signed.
<a id="Return_value_anyOf_i2_items_certificate_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_certificate_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_certificate_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_certificate_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_certificate_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_privatekey"></a>
<a id="Return_value_anyOf_i2_items_privatekey"></a>
###### privatekey

- Schema name: `Privatekey`

PEM-encoded private key corresponding to the certificate. `null` if no private key is available or for imported certificates without keys.
<a id="Return_value_anyOf_i2_items_privatekey_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_privatekey_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_privatekey_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_privatekey_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_privatekey_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_CSR"></a>
<a id="Return_value_anyOf_i2_items_CSR"></a>
###### CSR

- Schema name: `Csr`

PEM-encoded Certificate Signing Request (CSR) data. `null` for imported certificates or completed ACME certificates.
<a id="Return_value_anyOf_i2_items_CSR_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_CSR_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_CSR_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_CSR_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_CSR_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_acme_uri"></a>
<a id="Return_value_anyOf_i2_items_acme_uri"></a>
###### acme_uri

- Schema name: `Acme Uri`

ACME directory server URI used for automated certificate management. `null` for non-ACME certificates.
<a id="Return_value_anyOf_i2_items_acme_uri_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_acme_uri_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_acme_uri_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_acme_uri_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_acme_uri_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_domains_authenticators"></a>
<a id="Return_value_anyOf_i2_items_domains_authenticators"></a>
###### domains_authenticators

- Schema name: `Domains Authenticators`

Mapping of domain names to ACME DNS authenticator IDs for domain validation. `null` for non-ACME certificates.
<a id="Return_value_anyOf_i2_items_domains_authenticators_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_domains_authenticators_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_domains_authenticators_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i2_items_domains_authenticators_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_domains_authenticators_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_renew_days"></a>
<a id="Return_value_anyOf_i2_items_renew_days"></a>
###### renew_days

- Schema name: `Renew Days`

Number of days before expiration to attempt automatic renewal. Only applicable for ACME certificates. `null` for non-renewable certificates.
<a id="Return_value_anyOf_i2_items_renew_days_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_renew_days_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_renew_days_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_renew_days_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_renew_days_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_acme"></a>
<a id="Return_value_anyOf_i2_items_acme"></a>
###### acme

- Schema name: `Acme`

ACME registration and account information used for certificate lifecycle management. `null` for non-ACME certificates.
<a id="Return_value_anyOf_i2_items_acme_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_acme_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_acme_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i2_items_acme_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_acme_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_add_to_trusted_store"></a>
<a id="Return_value_anyOf_i2_items_add_to_trusted_store"></a>
###### add_to_trusted_store

- Schema name: `Add To Trusted Store`
- Type: boolean

Whether this certificate should be added to the system's trusted certificate store.

<a id="headingReturn_value_anyOf_i2_items_root_path"></a>
<a id="Return_value_anyOf_i2_items_root_path"></a>
###### root_path

- Schema name: `Root Path`
- Type: string

Filesystem path where certificate-related files are stored.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_certificate_path"></a>
<a id="Return_value_anyOf_i2_items_certificate_path"></a>
###### certificate_path

- Schema name: `Certificate Path`

Filesystem path to the certificate file (.crt). `null` if no certificate is available.
<a id="Return_value_anyOf_i2_items_certificate_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_certificate_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_certificate_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_certificate_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_certificate_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_privatekey_path"></a>
<a id="Return_value_anyOf_i2_items_privatekey_path"></a>
###### privatekey_path

- Schema name: `Privatekey Path`

Filesystem path to the private key file (.key). `null` if no private key is available.
<a id="Return_value_anyOf_i2_items_privatekey_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_privatekey_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_privatekey_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_privatekey_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_privatekey_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_csr_path"></a>
<a id="Return_value_anyOf_i2_items_csr_path"></a>
###### csr_path

- Schema name: `Csr Path`

Filesystem path to the certificate signing request file (.csr). `null` if no CSR is available.
<a id="Return_value_anyOf_i2_items_csr_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_csr_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_csr_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_csr_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_csr_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_cert_type"></a>
<a id="Return_value_anyOf_i2_items_cert_type"></a>
###### cert_type

- Schema name: `Cert Type`
- Type: string

Human-readable certificate type, typically 'CERTIFICATE' for standard certificates.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_cert_type_existing"></a>
<a id="Return_value_anyOf_i2_items_cert_type_existing"></a>
###### cert_type_existing

- Schema name: `Cert Type Existing`
- Type: boolean

Whether this is an existing certificate (imported or generated).

<a id="headingReturn_value_anyOf_i2_items_cert_type_CSR"></a>
<a id="Return_value_anyOf_i2_items_cert_type_CSR"></a>
###### cert_type_CSR

- Schema name: `Cert Type Csr`
- Type: boolean

Whether this entry represents a Certificate Signing Request (CSR) rather than a signed certificate.

<a id="headingReturn_value_anyOf_i2_items_cert_type_CA"></a>
<a id="Return_value_anyOf_i2_items_cert_type_CA"></a>
###### cert_type_CA

- Schema name: `Cert Type Ca`
- Type: boolean

Whether this certificate is a Certificate Authority (CA) certificate.

<a id="headingReturn_value_anyOf_i2_items_chain_list"></a>
<a id="Return_value_anyOf_i2_items_chain_list"></a>
###### chain_list

- Schema name: `Chain List`
- Type: array of string

Array of PEM-encoded certificates in the certificate chain, starting with the leaf certificate.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_chain_list_items"></a>
- Type: string
- Must be at most `2147483647` characters long

<a id="headingReturn_value_anyOf_i2_items_key_length"></a>
<a id="Return_value_anyOf_i2_items_key_length"></a>
###### key_length

- Schema name: `Key Length`

Size of the cryptographic key in bits. `null` if key information is unavailable.
<a id="Return_value_anyOf_i2_items_key_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_key_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_key_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_key_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_key_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_key_type"></a>
<a id="Return_value_anyOf_i2_items_key_type"></a>
###### key_type

- Schema name: `Key Type`

Type of cryptographic key algorithm (e.g., 'RSA', 'EC', 'DSA'). `null` if key information is unavailable.
<a id="Return_value_anyOf_i2_items_key_type_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_key_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_key_type_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_key_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_key_type_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_country"></a>
<a id="Return_value_anyOf_i2_items_country"></a>
###### country

- Schema name: `Country`

ISO 3166-1 alpha-2 country code from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i2_items_country_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_country_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_country_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_country_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_country_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_state"></a>
<a id="Return_value_anyOf_i2_items_state"></a>
###### state

- Schema name: `State`

State or province name from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i2_items_state_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_state_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_state_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_state_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_state_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_city"></a>
<a id="Return_value_anyOf_i2_items_city"></a>
###### city

- Schema name: `City`

City or locality name from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i2_items_city_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_city_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_city_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_city_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_city_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_organization"></a>
<a id="Return_value_anyOf_i2_items_organization"></a>
###### organization

- Schema name: `Organization`

Organization name from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i2_items_organization_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_organization_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_organization_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_organization_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_organization_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_organizational_unit"></a>
<a id="Return_value_anyOf_i2_items_organizational_unit"></a>
###### organizational_unit

- Schema name: `Organizational Unit`

Organizational unit from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i2_items_organizational_unit_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_organizational_unit_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_organizational_unit_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_organizational_unit_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_organizational_unit_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_common"></a>
<a id="Return_value_anyOf_i2_items_common"></a>
###### common

- Schema name: `Common`

Common name (CN) from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i2_items_common_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_common_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_common_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_common_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_common_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_san"></a>
<a id="Return_value_anyOf_i2_items_san"></a>
###### san

- Schema name: `San`

Subject Alternative Names (SAN) from the certificate extension. `null` if no SAN extension is present.
<a id="Return_value_anyOf_i2_items_san_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_san_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_san_anyOf_i0)

- Type: array of string
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_san_anyOf_i0_items"></a>
- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_san_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_san_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_email"></a>
<a id="Return_value_anyOf_i2_items_email"></a>
###### email

- Schema name: `Email`

Email address from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i2_items_email_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_email_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_email_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_email_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_email_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_DN"></a>
<a id="Return_value_anyOf_i2_items_DN"></a>
###### DN

- Schema name: `Dn`

Distinguished Name (DN) of the certificate subject in RFC 2253 format. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i2_items_DN_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_DN_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_DN_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_DN_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_DN_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_subject_name_hash"></a>
<a id="Return_value_anyOf_i2_items_subject_name_hash"></a>
###### subject_name_hash

- Schema name: `Subject Name Hash`

Hash of the certificate subject name. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i2_items_subject_name_hash_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_subject_name_hash_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_subject_name_hash_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_subject_name_hash_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_subject_name_hash_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_extensions"></a>
<a id="Return_value_anyOf_i2_items_extensions"></a>
###### extensions

- Schema name: `Extensions`
- Type: object

X.509 certificate extensions parsed into a dictionary structure.

<a id="headingReturn_value_anyOf_i2_items_digest_algorithm"></a>
<a id="Return_value_anyOf_i2_items_digest_algorithm"></a>
###### digest_algorithm

- Schema name: `Digest Algorithm`

Cryptographic hash algorithm used for certificate signing (e.g., 'SHA256'). `null` if unavailable.
<a id="Return_value_anyOf_i2_items_digest_algorithm_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_digest_algorithm_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_digest_algorithm_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_digest_algorithm_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_digest_algorithm_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_lifetime"></a>
<a id="Return_value_anyOf_i2_items_lifetime"></a>
###### lifetime

- Schema name: `Lifetime`

Certificate validity period in seconds. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i2_items_lifetime_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_lifetime_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_lifetime_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_lifetime_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_lifetime_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_from"></a>
<a id="Return_value_anyOf_i2_items_from"></a>
###### from

- Schema name: `From`

Certificate validity start date in ISO 8601 format. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i2_items_from_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_from_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_from_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_from_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_from_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_until"></a>
<a id="Return_value_anyOf_i2_items_until"></a>
###### until

- Schema name: `Until`

Certificate validity end date in ISO 8601 format. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i2_items_until_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_until_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_until_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_until_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_until_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_serial"></a>
<a id="Return_value_anyOf_i2_items_serial"></a>
###### serial

- Schema name: `Serial`

Certificate serial number. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i2_items_serial_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_serial_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_serial_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_serial_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_serial_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_chain"></a>
<a id="Return_value_anyOf_i2_items_chain"></a>
###### chain

- Schema name: `Chain`

Whether this certificate has an associated certificate chain. `null` if unavailable.
<a id="Return_value_anyOf_i2_items_chain_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_chain_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_chain_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_anyOf_i2_items_chain_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_chain_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_fingerprint"></a>
<a id="Return_value_anyOf_i2_items_fingerprint"></a>
###### fingerprint

- Schema name: `Fingerprint`

SHA-256 fingerprint of the certificate in hexadecimal format. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i2_items_fingerprint_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_fingerprint_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_fingerprint_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_fingerprint_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_fingerprint_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_expired"></a>
<a id="Return_value_anyOf_i2_items_expired"></a>
###### expired

- Schema name: `Expired`

Whether the certificate has expired. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i2_items_expired_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_expired_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_expired_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_anyOf_i2_items_expired_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_expired_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_parsed"></a>
<a id="Return_value_anyOf_i2_items_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: boolean

Whether the certificate data was successfully parsed and validated.

<a id="tab-pane_Return_value_anyOf_i3"></a>
##### [CertificateQueryResultItem](#tab-pane_Return_value_anyOf_i3)

- Schema name: `CertificateQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i3_id"></a>
<a id="Return_value_anyOf_i3_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for this certificate entry.

<a id="headingReturn_value_anyOf_i3_type"></a>
<a id="Return_value_anyOf_i3_type"></a>
###### type

- Schema name: `Type`
- Type: integer

Internal certificate type identifier used to determine certificate capabilities.

<a id="headingReturn_value_anyOf_i3_name"></a>
<a id="Return_value_anyOf_i3_name"></a>
###### name

- Schema name: `Name`
- Type: string

Human-readable name for this certificate. Must be unique and contain only alphanumeric characters, dashes, and underscores.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i3_certificate"></a>
<a id="Return_value_anyOf_i3_certificate"></a>
###### certificate

- Schema name: `Certificate`

PEM-encoded X.509 certificate data. `null` for certificate signing requests (CSR) that have not yet been signed.
<a id="Return_value_anyOf_i3_certificate_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_certificate_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_certificate_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i3_certificate_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_certificate_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_privatekey"></a>
<a id="Return_value_anyOf_i3_privatekey"></a>
###### privatekey

- Schema name: `Privatekey`

PEM-encoded private key corresponding to the certificate. `null` if no private key is available or for imported certificates without keys.
<a id="Return_value_anyOf_i3_privatekey_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_privatekey_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_privatekey_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i3_privatekey_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_privatekey_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_CSR"></a>
<a id="Return_value_anyOf_i3_CSR"></a>
###### CSR

- Schema name: `Csr`

PEM-encoded Certificate Signing Request (CSR) data. `null` for imported certificates or completed ACME certificates.
<a id="Return_value_anyOf_i3_CSR_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_CSR_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_CSR_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i3_CSR_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_CSR_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_acme_uri"></a>
<a id="Return_value_anyOf_i3_acme_uri"></a>
###### acme_uri

- Schema name: `Acme Uri`

ACME directory server URI used for automated certificate management. `null` for non-ACME certificates.
<a id="Return_value_anyOf_i3_acme_uri_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_acme_uri_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_acme_uri_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_acme_uri_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_acme_uri_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_domains_authenticators"></a>
<a id="Return_value_anyOf_i3_domains_authenticators"></a>
###### domains_authenticators

- Schema name: `Domains Authenticators`

Mapping of domain names to ACME DNS authenticator IDs for domain validation. `null` for non-ACME certificates.
<a id="Return_value_anyOf_i3_domains_authenticators_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_domains_authenticators_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_domains_authenticators_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_domains_authenticators_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_domains_authenticators_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_renew_days"></a>
<a id="Return_value_anyOf_i3_renew_days"></a>
###### renew_days

- Schema name: `Renew Days`

Number of days before expiration to attempt automatic renewal. Only applicable for ACME certificates. `null` for non-renewable certificates.
<a id="Return_value_anyOf_i3_renew_days_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_renew_days_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_renew_days_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i3_renew_days_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_renew_days_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_acme"></a>
<a id="Return_value_anyOf_i3_acme"></a>
###### acme

- Schema name: `Acme`

ACME registration and account information used for certificate lifecycle management. `null` for non-ACME certificates.
<a id="Return_value_anyOf_i3_acme_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_acme_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_acme_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_acme_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_acme_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_add_to_trusted_store"></a>
<a id="Return_value_anyOf_i3_add_to_trusted_store"></a>
###### add_to_trusted_store

- Schema name: `Add To Trusted Store`
- Type: boolean

Whether this certificate should be added to the system's trusted certificate store.

<a id="headingReturn_value_anyOf_i3_root_path"></a>
<a id="Return_value_anyOf_i3_root_path"></a>
###### root_path

- Schema name: `Root Path`
- Type: string

Filesystem path where certificate-related files are stored.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i3_certificate_path"></a>
<a id="Return_value_anyOf_i3_certificate_path"></a>
###### certificate_path

- Schema name: `Certificate Path`

Filesystem path to the certificate file (.crt). `null` if no certificate is available.
<a id="Return_value_anyOf_i3_certificate_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_certificate_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_certificate_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i3_certificate_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_certificate_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_privatekey_path"></a>
<a id="Return_value_anyOf_i3_privatekey_path"></a>
###### privatekey_path

- Schema name: `Privatekey Path`

Filesystem path to the private key file (.key). `null` if no private key is available.
<a id="Return_value_anyOf_i3_privatekey_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_privatekey_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_privatekey_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i3_privatekey_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_privatekey_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_csr_path"></a>
<a id="Return_value_anyOf_i3_csr_path"></a>
###### csr_path

- Schema name: `Csr Path`

Filesystem path to the certificate signing request file (.csr). `null` if no CSR is available.
<a id="Return_value_anyOf_i3_csr_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_csr_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_csr_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i3_csr_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_csr_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_cert_type"></a>
<a id="Return_value_anyOf_i3_cert_type"></a>
###### cert_type

- Schema name: `Cert Type`
- Type: string

Human-readable certificate type, typically 'CERTIFICATE' for standard certificates.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i3_cert_type_existing"></a>
<a id="Return_value_anyOf_i3_cert_type_existing"></a>
###### cert_type_existing

- Schema name: `Cert Type Existing`
- Type: boolean

Whether this is an existing certificate (imported or generated).

<a id="headingReturn_value_anyOf_i3_cert_type_CSR"></a>
<a id="Return_value_anyOf_i3_cert_type_CSR"></a>
###### cert_type_CSR

- Schema name: `Cert Type Csr`
- Type: boolean

Whether this entry represents a Certificate Signing Request (CSR) rather than a signed certificate.

<a id="headingReturn_value_anyOf_i3_cert_type_CA"></a>
<a id="Return_value_anyOf_i3_cert_type_CA"></a>
###### cert_type_CA

- Schema name: `Cert Type Ca`
- Type: boolean

Whether this certificate is a Certificate Authority (CA) certificate.

<a id="headingReturn_value_anyOf_i3_chain_list"></a>
<a id="Return_value_anyOf_i3_chain_list"></a>
###### chain_list

- Schema name: `Chain List`
- Type: array of string

Array of PEM-encoded certificates in the certificate chain, starting with the leaf certificate.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i3_chain_list_items"></a>
- Type: string
- Must be at most `2147483647` characters long

<a id="headingReturn_value_anyOf_i3_key_length"></a>
<a id="Return_value_anyOf_i3_key_length"></a>
###### key_length

- Schema name: `Key Length`

Size of the cryptographic key in bits. `null` if key information is unavailable.
<a id="Return_value_anyOf_i3_key_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_key_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_key_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i3_key_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_key_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_key_type"></a>
<a id="Return_value_anyOf_i3_key_type"></a>
###### key_type

- Schema name: `Key Type`

Type of cryptographic key algorithm (e.g., 'RSA', 'EC', 'DSA'). `null` if key information is unavailable.
<a id="Return_value_anyOf_i3_key_type_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_key_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_key_type_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i3_key_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_key_type_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_country"></a>
<a id="Return_value_anyOf_i3_country"></a>
###### country

- Schema name: `Country`

ISO 3166-1 alpha-2 country code from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i3_country_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_country_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_country_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_country_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_country_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_state"></a>
<a id="Return_value_anyOf_i3_state"></a>
###### state

- Schema name: `State`

State or province name from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i3_state_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_state_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_state_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_state_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_state_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_city"></a>
<a id="Return_value_anyOf_i3_city"></a>
###### city

- Schema name: `City`

City or locality name from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i3_city_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_city_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_city_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_city_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_city_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_organization"></a>
<a id="Return_value_anyOf_i3_organization"></a>
###### organization

- Schema name: `Organization`

Organization name from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i3_organization_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_organization_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_organization_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_organization_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_organization_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_organizational_unit"></a>
<a id="Return_value_anyOf_i3_organizational_unit"></a>
###### organizational_unit

- Schema name: `Organizational Unit`

Organizational unit from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i3_organizational_unit_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_organizational_unit_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_organizational_unit_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_organizational_unit_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_organizational_unit_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_common"></a>
<a id="Return_value_anyOf_i3_common"></a>
###### common

- Schema name: `Common`

Common name (CN) from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i3_common_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_common_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_common_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_common_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_common_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_san"></a>
<a id="Return_value_anyOf_i3_san"></a>
###### san

- Schema name: `San`

Subject Alternative Names (SAN) from the certificate extension. `null` if no SAN extension is present.
<a id="Return_value_anyOf_i3_san_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_san_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_san_anyOf_i0)

- Type: array of string
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i3_san_anyOf_i0_items"></a>
- Type: string

<a id="tab-pane_Return_value_anyOf_i3_san_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_san_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_email"></a>
<a id="Return_value_anyOf_i3_email"></a>
###### email

- Schema name: `Email`

Email address from the certificate subject. `null` if not specified.
<a id="Return_value_anyOf_i3_email_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_email_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_email_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_email_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_email_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_DN"></a>
<a id="Return_value_anyOf_i3_DN"></a>
###### DN

- Schema name: `Dn`

Distinguished Name (DN) of the certificate subject in RFC 2253 format. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i3_DN_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_DN_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_DN_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i3_DN_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_DN_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_subject_name_hash"></a>
<a id="Return_value_anyOf_i3_subject_name_hash"></a>
###### subject_name_hash

- Schema name: `Subject Name Hash`

Hash of the certificate subject name. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i3_subject_name_hash_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_subject_name_hash_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_subject_name_hash_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i3_subject_name_hash_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_subject_name_hash_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_extensions"></a>
<a id="Return_value_anyOf_i3_extensions"></a>
###### extensions

- Schema name: `Extensions`
- Type: object

X.509 certificate extensions parsed into a dictionary structure.

<a id="headingReturn_value_anyOf_i3_digest_algorithm"></a>
<a id="Return_value_anyOf_i3_digest_algorithm"></a>
###### digest_algorithm

- Schema name: `Digest Algorithm`

Cryptographic hash algorithm used for certificate signing (e.g., 'SHA256'). `null` if unavailable.
<a id="Return_value_anyOf_i3_digest_algorithm_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_digest_algorithm_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_digest_algorithm_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_digest_algorithm_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_digest_algorithm_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_lifetime"></a>
<a id="Return_value_anyOf_i3_lifetime"></a>
###### lifetime

- Schema name: `Lifetime`

Certificate validity period in seconds. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i3_lifetime_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_lifetime_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_lifetime_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i3_lifetime_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_lifetime_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_from"></a>
<a id="Return_value_anyOf_i3_from"></a>
###### from

- Schema name: `From`

Certificate validity start date in ISO 8601 format. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i3_from_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_from_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_from_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_from_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_from_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_until"></a>
<a id="Return_value_anyOf_i3_until"></a>
###### until

- Schema name: `Until`

Certificate validity end date in ISO 8601 format. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i3_until_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_until_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_until_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_until_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_until_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_serial"></a>
<a id="Return_value_anyOf_i3_serial"></a>
###### serial

- Schema name: `Serial`

Certificate serial number. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i3_serial_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_serial_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_serial_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i3_serial_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_serial_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_chain"></a>
<a id="Return_value_anyOf_i3_chain"></a>
###### chain

- Schema name: `Chain`

Whether this certificate has an associated certificate chain. `null` if unavailable.
<a id="Return_value_anyOf_i3_chain_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_chain_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_chain_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_anyOf_i3_chain_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_chain_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_fingerprint"></a>
<a id="Return_value_anyOf_i3_fingerprint"></a>
###### fingerprint

- Schema name: `Fingerprint`

SHA-256 fingerprint of the certificate in hexadecimal format. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i3_fingerprint_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_fingerprint_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_fingerprint_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_fingerprint_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_fingerprint_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_expired"></a>
<a id="Return_value_anyOf_i3_expired"></a>
###### expired

- Schema name: `Expired`

Whether the certificate has expired. `null` if certificate parsing failed.
<a id="Return_value_anyOf_i3_expired_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_expired_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_expired_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_anyOf_i3_expired_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_expired_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_parsed"></a>
<a id="Return_value_anyOf_i3_parsed"></a>
###### parsed

- Schema name: `Parsed`
- Type: boolean

Whether the certificate data was successfully parsed and validated.

<a id="tab-pane_Return_value_anyOf_i4"></a>
##### [Option 5](#tab-pane_Return_value_anyOf_i4)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
