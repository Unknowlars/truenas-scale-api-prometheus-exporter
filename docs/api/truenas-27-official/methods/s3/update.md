---
title: s3.update
kind: method
source_rst: _sources/api_methods_s3.update.rst.txt
source_html: api_methods_s3.update.html
required_roles:
  - SHARING_S3_WRITE
---

# s3.update

## Summary

Update the S3 service configuration.

Changing the listeners, the reactor thread count or the region restarts the S3 service, draining in-flight requests for up to 30 seconds. Every other change applies with a reload, the certificate included: a different one, or the UI certificate changing while the service follows it, rotates in place.

## Required Roles

- `SHARING_S3_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

<a id="Call_parameters_items_i0"></a>
#### data

- Schema name: `data`
- Type: object

S3 service configuration changes to apply.
- No Additional Properties
<a id="headingCall_parameters_items_i0_listeners"></a>
<a id="Call_parameters_items_i0_listeners"></a>
##### listeners

- Schema name: `Listeners`
- Type: array of object

Where the S3 service listens, at most eight entries, each an address and port served in plaintext or over TLS. An empty list listens on every address on port 9000 in plaintext. Changing it restarts the service.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_listeners_items"></a>
###### S3Listener

- Schema name: `S3Listener`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_listeners_items_address"></a>
<a id="Call_parameters_items_i0_listeners_items_address"></a>
###### address (required)

- Schema name: `Address`
- Type: string

IP address to listen on, from `s3.bindip_choices`: a static address, a loopback or a wildcard.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_listeners_items_port"></a>
<a id="Call_parameters_items_i0_listeners_items_port"></a>
###### port

- Schema name: `Port`
- Type: integer
- Default: 9000

TCP port to listen on.
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="headingCall_parameters_items_i0_listeners_items_tls"></a>
<a id="Call_parameters_items_i0_listeners_items_tls"></a>
###### tls

- Schema name: `Tls`
- Type: boolean
- Default: false

Serve this address over TLS with `certificate`, which must then be set. Plaintext otherwise. A multi-homed system may serve a storage network in the clear and a management network over TLS.

<a id="headingCall_parameters_items_i0_servers"></a>
<a id="Call_parameters_items_i0_servers"></a>
##### servers

- Schema name: `Servers`
- Type: integer

Reactor threads serving the listen addresses, each with its own io_uring ring and every address shared between them. At most twelve, and no more than the system has CPUs. Each thread carries its own connection pool and buffering, so more of them cost memory. Changing it restarts the service.
- Value must be greater or equal to `1` and lesser or equal to `12`

<a id="headingCall_parameters_items_i0_certificate"></a>
<a id="Call_parameters_items_i0_certificate"></a>
##### certificate

- Schema name: `Certificate`

ID of the certificate the TLS listeners serve. `null` serves them with the UI certificate (`system.general.ui_certificate`), so a renewal or a change there reaches the S3 service too.
<a id="Call_parameters_items_i0_certificate_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_certificate_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_certificate_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i0_certificate_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_certificate_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_region"></a>
<a id="Call_parameters_items_i0_region"></a>
##### region

- Schema name: `Region`
- Type: string

Region name echoed to clients: at most 63 characters of lowercase letters, digits and hyphens, `us-east-1` shaped. Empty accepts whatever a client signs for.
- Must match regular expression: `^[a-z0-9-]*$`
- Must be at most `63` characters long

<a id="headingCall_parameters_items_i0_log_level"></a>
<a id="Call_parameters_items_i0_log_level"></a>
##### log_level

- Schema name: `Log Level`
- Type: enum (of string)

Least serious log record the S3 service keeps. `INFO` adds one record per request.
###### Must be one of:

- "ERROR"
- "WARNING"
- "NOTICE"
- "INFO"
- "DEBUG"

<a id="headingCall_parameters_items_i0_default_audit"></a>
<a id="Call_parameters_items_i0_default_audit"></a>
##### default_audit

- Schema name: `Default Audit`

Actions audited on every bucket that does not set its own `audit`, or `ALL`. An empty list audits nothing. Also the only mask that can select `CreateBucket` and `ListAllMyBuckets`: a create precedes its bucket's registration, and listing buckets is account-scoped, so neither ever consults a bucket's own mask. NOTE: this is a licensed feature.
<a id="Call_parameters_items_i0_default_audit_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_default_audit_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_default_audit_anyOf_i0)

- Type: array of enum (of string)
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_default_audit_anyOf_i0_items"></a>
- Type: enum (of string)
###### Must be one of:

- "GetObject"
- "PutObject"
- "DeleteObject"
- "GetObjectTagging"
- "PutObjectTagging"
- "DeleteObjectTagging"
- "ListBucket"
- "GetBucketLocation"
- "ListBucketMultipartUploads"
- "ListMultipartUploadParts"
- "AbortMultipartUpload"
- "PutObjectRetention"
- "PutObjectLegalHold"
- "ListAllMyBuckets"
- "GetObjectAcl"
- "PutObjectAcl"
- "GetBucketAcl"
- "PutBucketAcl"
- "PutBucketVersioning"
- "CreateBucket"
- "DeleteBucket"

<a id="tab-pane_Call_parameters_items_i0_default_audit_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_default_audit_anyOf_i1)

- Type: const
- Specific value: `"ALL"`

<a id="headingCall_parameters_items_i0_default_audit_overflow"></a>
<a id="Call_parameters_items_i0_default_audit_overflow"></a>
##### default_audit_overflow

- Schema name: `Default Audit Overflow`
- Type: enum (of string)

What an audited request gets when no audit record slot is free, on buckets that do not set their own. `DROP` sheds the record, `BACKPRESSURE` answers the client with a retryable 503.
###### Must be one of:

- "DROP"
- "BACKPRESSURE"

<a id="headingCall_parameters_items_i0_global_grants"></a>
<a id="Call_parameters_items_i0_global_grants"></a>
##### global_grants

- Schema name: `Global Grants`
- Type: array of object

Grants that apply to every bucket, replacing the current list.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_global_grants_items"></a>
###### S3Grant

- Schema name: `S3Grant`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_global_grants_items_principal_type"></a>
<a id="Call_parameters_items_i0_global_grants_items_principal_type"></a>
###### principal_type (required)

- Schema name: `Principal Type`
- Type: enum (of string)

Who the grant applies to. A user, a group, or everyone with a valid access key.
###### Must be one of:

- "USER"
- "GROUP"
- "EVERYONE"

<a id="headingCall_parameters_items_i0_global_grants_items_xid"></a>
<a id="Call_parameters_items_i0_global_grants_items_xid"></a>
###### xid

- Schema name: `Xid`
- Default: null

The uid of the user or the gid of the group. Required for `USER` and `GROUP`, forbidden for `EVERYONE`.
<a id="Call_parameters_items_i0_global_grants_items_xid_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_global_grants_items_xid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_global_grants_items_xid_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i0_global_grants_items_xid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_global_grants_items_xid_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_global_grants_items_access"></a>
<a id="Call_parameters_items_i0_global_grants_items_access"></a>
###### access (required)

- Schema name: `Access`
- Type: enum (of string)

What the grant allows. `READONLY`, `WRITEONLY` and `READWRITE` allow the matching operations. `DENY` refuses every operation for the principal and outranks the bucket owner.
###### Must be one of:

- "READONLY"
- "WRITEONLY"
- "READWRITE"
- "DENY"

<a id="headingCall_parameters_items_i0_managed_root_dataset"></a>
<a id="Call_parameters_items_i0_managed_root_dataset"></a>
##### managed_root_dataset

- Schema name: `Managed Root Dataset`
- Type: string

Path where datasets for S3 buckets created through S3 protocol CreateBucket requests are created, for example `tank/s3`. The path is a dataset name, not a mount point, and the dataset must already exist. If this field is empty (the default), S3 protocol CreateBucket requests are refused.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `S3Entry`
- Type: object

The updated S3 service configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Placeholder identifier. Not used as there is only one.

<a id="headingReturn_value_listeners"></a>
<a id="Return_value_listeners"></a>
#### listeners

- Schema name: `Listeners`
- Type: array of object
- Default: []

Where the S3 service listens, at most eight entries, each an address and port served in plaintext or over TLS. An empty list listens on every address on port 9000 in plaintext. Changing it restarts the service.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_listeners_items"></a>
##### S3Listener

- Schema name: `S3Listener`
- Type: object
- No Additional Properties
<a id="headingReturn_value_listeners_items_address"></a>
<a id="Return_value_listeners_items_address"></a>
###### address (required)

- Schema name: `Address`
- Type: string

IP address to listen on, from `s3.bindip_choices`: a static address, a loopback or a wildcard.
- Must be at least `1` characters long

<a id="headingReturn_value_listeners_items_port"></a>
<a id="Return_value_listeners_items_port"></a>
###### port

- Schema name: `Port`
- Type: integer
- Default: 9000

TCP port to listen on.
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="headingReturn_value_listeners_items_tls"></a>
<a id="Return_value_listeners_items_tls"></a>
###### tls

- Schema name: `Tls`
- Type: boolean
- Default: false

Serve this address over TLS with `certificate`, which must then be set. Plaintext otherwise. A multi-homed system may serve a storage network in the clear and a management network over TLS.

<a id="headingReturn_value_servers"></a>
<a id="Return_value_servers"></a>
#### servers

- Schema name: `Servers`
- Type: integer
- Default: 1

Reactor threads serving the listen addresses, each with its own io_uring ring and every address shared between them. At most twelve, and no more than the system has CPUs. Each thread carries its own connection pool and buffering, so more of them cost memory. Changing it restarts the service.
- Value must be greater or equal to `1` and lesser or equal to `12`

<a id="headingReturn_value_certificate"></a>
<a id="Return_value_certificate"></a>
#### certificate

- Schema name: `Certificate`
- Default: null

ID of the certificate the TLS listeners serve. `null` serves them with the UI certificate (`system.general.ui_certificate`), so a renewal or a change there reaches the S3 service too.
<a id="Return_value_certificate_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_certificate_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_certificate_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_certificate_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_certificate_anyOf_i1)

- Type: null

<a id="headingReturn_value_region"></a>
<a id="Return_value_region"></a>
#### region

- Schema name: `Region`
- Type: string
- Default: ""

Region name echoed to clients: at most 63 characters of lowercase letters, digits and hyphens, `us-east-1` shaped. Empty accepts whatever a client signs for.
- Must match regular expression: `^[a-z0-9-]*$`
- Must be at most `63` characters long

<a id="headingReturn_value_log_level"></a>
<a id="Return_value_log_level"></a>
#### log_level

- Schema name: `Log Level`
- Type: enum (of string)
- Default: "NOTICE"

Least serious log record the S3 service keeps. `INFO` adds one record per request.
##### Must be one of:

- "ERROR"
- "WARNING"
- "NOTICE"
- "INFO"
- "DEBUG"

<a id="headingReturn_value_default_audit"></a>
<a id="Return_value_default_audit"></a>
#### default_audit

- Schema name: `Default Audit`
- Default: []

Actions audited on every bucket that does not set its own `audit`, or `ALL`. An empty list audits nothing. Also the only mask that can select `CreateBucket` and `ListAllMyBuckets`: a create precedes its bucket's registration, and listing buckets is account-scoped, so neither ever consults a bucket's own mask. NOTE: this is a licensed feature.
<a id="Return_value_default_audit_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_default_audit_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_default_audit_anyOf_i0)

- Type: array of enum (of string)
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_default_audit_anyOf_i0_items"></a>
- Type: enum (of string)
###### Must be one of:

- "GetObject"
- "PutObject"
- "DeleteObject"
- "GetObjectTagging"
- "PutObjectTagging"
- "DeleteObjectTagging"
- "ListBucket"
- "GetBucketLocation"
- "ListBucketMultipartUploads"
- "ListMultipartUploadParts"
- "AbortMultipartUpload"
- "PutObjectRetention"
- "PutObjectLegalHold"
- "ListAllMyBuckets"
- "GetObjectAcl"
- "PutObjectAcl"
- "GetBucketAcl"
- "PutBucketAcl"
- "PutBucketVersioning"
- "CreateBucket"
- "DeleteBucket"

<a id="tab-pane_Return_value_default_audit_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_default_audit_anyOf_i1)

- Type: const
- Specific value: `"ALL"`

<a id="headingReturn_value_default_audit_overflow"></a>
<a id="Return_value_default_audit_overflow"></a>
#### default_audit_overflow

- Schema name: `Default Audit Overflow`
- Type: enum (of string)
- Default: "DROP"

What an audited request gets when no audit record slot is free, on buckets that do not set their own. `DROP` sheds the record, `BACKPRESSURE` answers the client with a retryable 503.
##### Must be one of:

- "DROP"
- "BACKPRESSURE"

<a id="headingReturn_value_global_grants"></a>
<a id="Return_value_global_grants"></a>
#### global_grants

- Schema name: `Global Grants`
- Type: array of object
- Default: []

Grants that apply to every bucket. A `DENY` here suspends the principal everywhere, outranking every bucket grant. Listing buckets never needs one of these.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_global_grants_items"></a>
##### S3GrantEntry

- Schema name: `S3GrantEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_global_grants_items_principal_type"></a>
<a id="Return_value_global_grants_items_principal_type"></a>
###### principal_type (required)

- Schema name: `Principal Type`
- Type: enum (of string)

Who the grant applies to. A user, a group, or everyone with a valid access key.
###### Must be one of:

- "USER"
- "GROUP"
- "EVERYONE"

<a id="headingReturn_value_global_grants_items_xid"></a>
<a id="Return_value_global_grants_items_xid"></a>
###### xid

- Schema name: `Xid`
- Default: null

The uid of the user or the gid of the group. Required for `USER` and `GROUP`, forbidden for `EVERYONE`.
<a id="Return_value_global_grants_items_xid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_global_grants_items_xid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_global_grants_items_xid_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_global_grants_items_xid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_global_grants_items_xid_anyOf_i1)

- Type: null

<a id="headingReturn_value_global_grants_items_access"></a>
<a id="Return_value_global_grants_items_access"></a>
###### access (required)

- Schema name: `Access`
- Type: enum (of string)

What the grant allows. `READONLY`, `WRITEONLY` and `READWRITE` allow the matching operations. `DENY` refuses every operation for the principal and outranks the bucket owner.
###### Must be one of:

- "READONLY"
- "WRITEONLY"
- "READWRITE"
- "DENY"

<a id="headingReturn_value_global_grants_items_name"></a>
<a id="Return_value_global_grants_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Name of the user or group the grant applies to, resolved for display. Empty for `EVERYONE`.

<a id="headingReturn_value_managed_root_dataset"></a>
<a id="Return_value_managed_root_dataset"></a>
#### managed_root_dataset

- Schema name: `Managed Root Dataset`
- Type: string
- Default: ""

Path where datasets for S3 buckets created through S3 protocol CreateBucket requests are created, for example `tank/s3`. The path is a dataset name, not a mount point, and the dataset must already exist. If this field is empty (the default), S3 protocol CreateBucket requests are refused.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
