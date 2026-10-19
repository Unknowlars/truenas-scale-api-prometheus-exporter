---
title: acme.dns.authenticator.update
kind: method
source_rst: _sources/api_methods_acme.dns.authenticator.update.rst.txt
source_html: api_methods_acme.dns.authenticator.update.html
required_roles:
  - NETWORK_INTERFACE_WRITE
---

# acme.dns.authenticator.update

## Summary

Update DNS Authenticator of `id`.

## Required Roles

- `NETWORK_INTERFACE_WRITE`

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

ID of the DNS authenticator to update.

#### Parameter 2: dns_authenticator_update

<a id="Call_parameters_items_i1"></a>
#### dns_authenticator_update

- Schema name: `dns_authenticator_update`
- Type: object

Updated DNS authenticator configuration data.
- No Additional Properties
<a id="headingCall_parameters_items_i1_attributes"></a>
<a id="Call_parameters_items_i1_attributes"></a>
##### attributes

- Schema name: `Attributes`

Authentication credentials and configuration for the DNS provider.
<a id="Call_parameters_items_i1_attributes_oneOf"></a>
###### One of

<a id="tab-pane_Call_parameters_items_i1_attributes_oneOf_i0"></a>
###### [CloudFlareSchema](#tab-pane_Call_parameters_items_i1_attributes_oneOf_i0)

- Schema name: `CloudFlareSchema`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i1_attributes_oneOf_i0_authenticator"></a>
<a id="Call_parameters_items_i1_attributes_oneOf_i0_authenticator"></a>
###### authenticator (required)

- Schema name: `Authenticator`
- Type: const

DNS authenticator type identifier for Cloudflare.
- Specific value: `"cloudflare"`

<a id="headingCall_parameters_items_i1_attributes_oneOf_i0_cloudflare_email"></a>
<a id="Call_parameters_items_i1_attributes_oneOf_i0_cloudflare_email"></a>
###### cloudflare_email

- Schema name: `Cloudflare Email`
- Default: null

Cloudflare Email.
<a id="Call_parameters_items_i1_attributes_oneOf_i0_cloudflare_email_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_attributes_oneOf_i0_cloudflare_email_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_attributes_oneOf_i0_cloudflare_email_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i1_attributes_oneOf_i0_cloudflare_email_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_attributes_oneOf_i0_cloudflare_email_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_attributes_oneOf_i0_api_key"></a>
<a id="Call_parameters_items_i1_attributes_oneOf_i0_api_key"></a>
###### api_key

- Schema name: `Api Key`
- Default: ""

API Key.
<a id="Call_parameters_items_i1_attributes_oneOf_i0_api_key_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_attributes_oneOf_i0_api_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_attributes_oneOf_i0_api_key_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i1_attributes_oneOf_i0_api_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_attributes_oneOf_i0_api_key_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_attributes_oneOf_i0_api_token"></a>
<a id="Call_parameters_items_i1_attributes_oneOf_i0_api_token"></a>
###### api_token

- Schema name: `Api Token`
- Default: ""

API Token.
<a id="Call_parameters_items_i1_attributes_oneOf_i0_api_token_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_attributes_oneOf_i0_api_token_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_attributes_oneOf_i0_api_token_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i1_attributes_oneOf_i0_api_token_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_attributes_oneOf_i0_api_token_anyOf_i1)

- Type: null

<a id="tab-pane_Call_parameters_items_i1_attributes_oneOf_i1"></a>
###### [DigitalOceanSchema](#tab-pane_Call_parameters_items_i1_attributes_oneOf_i1)

- Schema name: `DigitalOceanSchema`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i1_attributes_oneOf_i1_authenticator"></a>
<a id="Call_parameters_items_i1_attributes_oneOf_i1_authenticator"></a>
###### authenticator (required)

- Schema name: `Authenticator`
- Type: const

DNS authenticator type identifier for DigitalOcean.
- Specific value: `"digitalocean"`

<a id="headingCall_parameters_items_i1_attributes_oneOf_i1_digitalocean_token"></a>
<a id="Call_parameters_items_i1_attributes_oneOf_i1_digitalocean_token"></a>
###### digitalocean_token (required)

- Schema name: `Digitalocean Token`
- Type: string

DigitalOcean Token.
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i1_attributes_oneOf_i2"></a>
###### [OVHSchema](#tab-pane_Call_parameters_items_i1_attributes_oneOf_i2)

- Schema name: `OVHSchema`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i1_attributes_oneOf_i2_authenticator"></a>
<a id="Call_parameters_items_i1_attributes_oneOf_i2_authenticator"></a>
###### authenticator (required)

- Schema name: `Authenticator`
- Type: const

DNS authenticator type identifier for OVH.
- Specific value: `"OVH"`

<a id="headingCall_parameters_items_i1_attributes_oneOf_i2_application_key"></a>
<a id="Call_parameters_items_i1_attributes_oneOf_i2_application_key"></a>
###### application_key (required)

- Schema name: `Application Key`
- Type: string

OVH Application Key.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i1_attributes_oneOf_i2_application_secret"></a>
<a id="Call_parameters_items_i1_attributes_oneOf_i2_application_secret"></a>
###### application_secret (required)

- Schema name: `Application Secret`
- Type: string

OVH Application Secret.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i1_attributes_oneOf_i2_consumer_key"></a>
<a id="Call_parameters_items_i1_attributes_oneOf_i2_consumer_key"></a>
###### consumer_key (required)

- Schema name: `Consumer Key`
- Type: string

OVH Consumer Key.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i1_attributes_oneOf_i2_endpoint"></a>
<a id="Call_parameters_items_i1_attributes_oneOf_i2_endpoint"></a>
###### endpoint (required)

- Schema name: `Endpoint`
- Type: enum (of string)

OVH Endpoint.
###### Must be one of:

- "ovh-eu"
- "ovh-ca"
- "ovh-us"
- "kimsufi-eu"
- "kimsufi-ca"
- "soyoustart-eu"
- "soyoustart-ca"

<a id="tab-pane_Call_parameters_items_i1_attributes_oneOf_i3"></a>
###### [Route53Schema](#tab-pane_Call_parameters_items_i1_attributes_oneOf_i3)

- Schema name: `Route53Schema`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i1_attributes_oneOf_i3_authenticator"></a>
<a id="Call_parameters_items_i1_attributes_oneOf_i3_authenticator"></a>
###### authenticator (required)

- Schema name: `Authenticator`
- Type: const

DNS authenticator type identifier for AWS Route 53.
- Specific value: `"route53"`

<a id="headingCall_parameters_items_i1_attributes_oneOf_i3_access_key_id"></a>
<a id="Call_parameters_items_i1_attributes_oneOf_i3_access_key_id"></a>
###### access_key_id (required)

- Schema name: `Access Key Id`
- Type: string

AWS Access Key ID.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i1_attributes_oneOf_i3_secret_access_key"></a>
<a id="Call_parameters_items_i1_attributes_oneOf_i3_secret_access_key"></a>
###### secret_access_key (required)

- Schema name: `Secret Access Key`
- Type: string

AWS Secret Access Key.
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i1_attributes_oneOf_i4"></a>
###### [ShellSchema](#tab-pane_Call_parameters_items_i1_attributes_oneOf_i4)

- Schema name: `ShellSchema`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i1_attributes_oneOf_i4_authenticator"></a>
<a id="Call_parameters_items_i1_attributes_oneOf_i4_authenticator"></a>
###### authenticator (required)

- Schema name: `Authenticator`
- Type: const

DNS authenticator type identifier for custom shell scripts.
- Specific value: `"shell"`

<a id="headingCall_parameters_items_i1_attributes_oneOf_i4_script"></a>
<a id="Call_parameters_items_i1_attributes_oneOf_i4_script"></a>
###### script (required)

- Schema name: `Script`
- Type: string
- Type: Format: file-path

Authentication Script.

<a id="headingCall_parameters_items_i1_attributes_oneOf_i4_user"></a>
<a id="Call_parameters_items_i1_attributes_oneOf_i4_user"></a>
###### user

- Schema name: `User`
- Type: string
- Default: "nobody"

Running user.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i1_attributes_oneOf_i4_timeout"></a>
<a id="Call_parameters_items_i1_attributes_oneOf_i4_timeout"></a>
###### timeout

- Schema name: `Timeout`
- Type: integer
- Default: 60

Script Timeout.
- Value must be greater or equal to `5`

<a id="headingCall_parameters_items_i1_attributes_oneOf_i4_delay"></a>
<a id="Call_parameters_items_i1_attributes_oneOf_i4_delay"></a>
###### delay

- Schema name: `Delay`
- Type: integer
- Default: 60

Propagation delay.
- Value must be greater or equal to `10`

<a id="headingCall_parameters_items_i1_name"></a>
<a id="Call_parameters_items_i1_name"></a>
##### name

- Schema name: `Name`
- Type: string

Human-readable name for the DNS authenticator.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `DNSAuthenticatorEntry`
- Type: object

The updated DNS authenticator configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the DNS authenticator.

<a id="headingReturn_value_attributes"></a>
<a id="Return_value_attributes"></a>
#### attributes (required)

- Schema name: `Attributes`

Authentication credentials and configuration (masked for security).
<a id="Return_value_attributes_oneOf"></a>
##### One of

<a id="tab-pane_Return_value_attributes_oneOf_i0"></a>
###### [CloudFlareSchema](#tab-pane_Return_value_attributes_oneOf_i0)

- Schema name: `CloudFlareSchema`
- Type: object
- No Additional Properties
<a id="headingReturn_value_attributes_oneOf_i0_authenticator"></a>
<a id="Return_value_attributes_oneOf_i0_authenticator"></a>
###### authenticator (required)

- Schema name: `Authenticator`
- Type: const

DNS authenticator type identifier for Cloudflare.
- Specific value: `"cloudflare"`

<a id="headingReturn_value_attributes_oneOf_i0_cloudflare_email"></a>
<a id="Return_value_attributes_oneOf_i0_cloudflare_email"></a>
###### cloudflare_email

- Schema name: `Cloudflare Email`
- Default: null

Cloudflare Email.
<a id="Return_value_attributes_oneOf_i0_cloudflare_email_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_attributes_oneOf_i0_cloudflare_email_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_attributes_oneOf_i0_cloudflare_email_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_attributes_oneOf_i0_cloudflare_email_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_attributes_oneOf_i0_cloudflare_email_anyOf_i1)

- Type: null

<a id="headingReturn_value_attributes_oneOf_i0_api_key"></a>
<a id="Return_value_attributes_oneOf_i0_api_key"></a>
###### api_key

- Schema name: `Api Key`
- Default: ""

API Key.
<a id="Return_value_attributes_oneOf_i0_api_key_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_attributes_oneOf_i0_api_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_attributes_oneOf_i0_api_key_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_attributes_oneOf_i0_api_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_attributes_oneOf_i0_api_key_anyOf_i1)

- Type: null

<a id="headingReturn_value_attributes_oneOf_i0_api_token"></a>
<a id="Return_value_attributes_oneOf_i0_api_token"></a>
###### api_token

- Schema name: `Api Token`
- Default: ""

API Token.
<a id="Return_value_attributes_oneOf_i0_api_token_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_attributes_oneOf_i0_api_token_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_attributes_oneOf_i0_api_token_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_attributes_oneOf_i0_api_token_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_attributes_oneOf_i0_api_token_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_attributes_oneOf_i1"></a>
###### [DigitalOceanSchema](#tab-pane_Return_value_attributes_oneOf_i1)

- Schema name: `DigitalOceanSchema`
- Type: object
- No Additional Properties
<a id="headingReturn_value_attributes_oneOf_i1_authenticator"></a>
<a id="Return_value_attributes_oneOf_i1_authenticator"></a>
###### authenticator (required)

- Schema name: `Authenticator`
- Type: const

DNS authenticator type identifier for DigitalOcean.
- Specific value: `"digitalocean"`

<a id="headingReturn_value_attributes_oneOf_i1_digitalocean_token"></a>
<a id="Return_value_attributes_oneOf_i1_digitalocean_token"></a>
###### digitalocean_token (required)

- Schema name: `Digitalocean Token`
- Type: string

DigitalOcean Token.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_attributes_oneOf_i2"></a>
###### [OVHSchema](#tab-pane_Return_value_attributes_oneOf_i2)

- Schema name: `OVHSchema`
- Type: object
- No Additional Properties
<a id="headingReturn_value_attributes_oneOf_i2_authenticator"></a>
<a id="Return_value_attributes_oneOf_i2_authenticator"></a>
###### authenticator (required)

- Schema name: `Authenticator`
- Type: const

DNS authenticator type identifier for OVH.
- Specific value: `"OVH"`

<a id="headingReturn_value_attributes_oneOf_i2_application_key"></a>
<a id="Return_value_attributes_oneOf_i2_application_key"></a>
###### application_key (required)

- Schema name: `Application Key`
- Type: string

OVH Application Key.
- Must be at least `1` characters long

<a id="headingReturn_value_attributes_oneOf_i2_application_secret"></a>
<a id="Return_value_attributes_oneOf_i2_application_secret"></a>
###### application_secret (required)

- Schema name: `Application Secret`
- Type: string

OVH Application Secret.
- Must be at least `1` characters long

<a id="headingReturn_value_attributes_oneOf_i2_consumer_key"></a>
<a id="Return_value_attributes_oneOf_i2_consumer_key"></a>
###### consumer_key (required)

- Schema name: `Consumer Key`
- Type: string

OVH Consumer Key.
- Must be at least `1` characters long

<a id="headingReturn_value_attributes_oneOf_i2_endpoint"></a>
<a id="Return_value_attributes_oneOf_i2_endpoint"></a>
###### endpoint (required)

- Schema name: `Endpoint`
- Type: enum (of string)

OVH Endpoint.
###### Must be one of:

- "ovh-eu"
- "ovh-ca"
- "ovh-us"
- "kimsufi-eu"
- "kimsufi-ca"
- "soyoustart-eu"
- "soyoustart-ca"

<a id="tab-pane_Return_value_attributes_oneOf_i3"></a>
###### [Route53Schema](#tab-pane_Return_value_attributes_oneOf_i3)

- Schema name: `Route53Schema`
- Type: object
- No Additional Properties
<a id="headingReturn_value_attributes_oneOf_i3_authenticator"></a>
<a id="Return_value_attributes_oneOf_i3_authenticator"></a>
###### authenticator (required)

- Schema name: `Authenticator`
- Type: const

DNS authenticator type identifier for AWS Route 53.
- Specific value: `"route53"`

<a id="headingReturn_value_attributes_oneOf_i3_access_key_id"></a>
<a id="Return_value_attributes_oneOf_i3_access_key_id"></a>
###### access_key_id (required)

- Schema name: `Access Key Id`
- Type: string

AWS Access Key ID.
- Must be at least `1` characters long

<a id="headingReturn_value_attributes_oneOf_i3_secret_access_key"></a>
<a id="Return_value_attributes_oneOf_i3_secret_access_key"></a>
###### secret_access_key (required)

- Schema name: `Secret Access Key`
- Type: string

AWS Secret Access Key.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_attributes_oneOf_i4"></a>
###### [ShellSchema](#tab-pane_Return_value_attributes_oneOf_i4)

- Schema name: `ShellSchema`
- Type: object
- No Additional Properties
<a id="headingReturn_value_attributes_oneOf_i4_authenticator"></a>
<a id="Return_value_attributes_oneOf_i4_authenticator"></a>
###### authenticator (required)

- Schema name: `Authenticator`
- Type: const

DNS authenticator type identifier for custom shell scripts.
- Specific value: `"shell"`

<a id="headingReturn_value_attributes_oneOf_i4_script"></a>
<a id="Return_value_attributes_oneOf_i4_script"></a>
###### script (required)

- Schema name: `Script`
- Type: string
- Type: Format: file-path

Authentication Script.

<a id="headingReturn_value_attributes_oneOf_i4_user"></a>
<a id="Return_value_attributes_oneOf_i4_user"></a>
###### user

- Schema name: `User`
- Type: string
- Default: "nobody"

Running user.
- Must be at least `1` characters long

<a id="headingReturn_value_attributes_oneOf_i4_timeout"></a>
<a id="Return_value_attributes_oneOf_i4_timeout"></a>
###### timeout

- Schema name: `Timeout`
- Type: integer
- Default: 60

Script Timeout.
- Value must be greater or equal to `5`

<a id="headingReturn_value_attributes_oneOf_i4_delay"></a>
<a id="Return_value_attributes_oneOf_i4_delay"></a>
###### delay

- Schema name: `Delay`
- Type: integer
- Default: 60

Propagation delay.
- Value must be greater or equal to `10`

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the DNS authenticator.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
