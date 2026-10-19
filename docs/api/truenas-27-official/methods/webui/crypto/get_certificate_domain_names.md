---
title: webui.crypto.get_certificate_domain_names
kind: method
source_rst: _sources/api_methods_webui.crypto.get_certificate_domain_names.rst.txt
source_html: api_methods_webui.crypto.get_certificate_domain_names.html
required_roles:
  - READONLY_ADMIN
---

# webui.crypto.get_certificate_domain_names

## Summary

Return the domain names associated with a certificate.

This includes the Common Name (if set) followed by any Subject Alternative Names (SANs).

## Required Roles

- `READONLY_ADMIN`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: cert_id

<a id="Call_parameters_items_i0"></a>
#### cert_id

- Schema name: `cert_id`
- Type: integer

ID of the certificate to extract domain names from.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array

Array of domain names found in the certificate (CN and SAN entries).
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
