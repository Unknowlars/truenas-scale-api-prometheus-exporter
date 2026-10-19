---
title: sharing.smb.getacl
kind: method
source_rst: _sources/api_methods_sharing.smb.getacl.rst.txt
source_html: api_methods_sharing.smb.getacl.html
required_roles:
  - SHARING_SMB_READ
---

# sharing.smb.getacl

## Required Roles

- `SHARING_SMB_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: smb_getacl

<a id="Call_parameters_items_i0"></a>
#### smb_getacl

- Schema name: `smb_getacl`
- Type: object

SharingSMBGetaclArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_share_name"></a>
<a id="Call_parameters_items_i0_share_name"></a>
##### share_name (required)

- Schema name: `Share Name`
- Type: string

Name of the SMB share to retrieve ACL for.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `SMBShareAcl`
- Type: object

The updated SMB share ACL configuration.
- No Additional Properties
<a id="headingReturn_value_share_name"></a>
<a id="Return_value_share_name"></a>
#### share_name (required)

- Schema name: `Share Name`
- Type: string

Name of the SMB share.
- Must be at least `1` characters long

<a id="headingReturn_value_share_acl"></a>
<a id="Return_value_share_acl"></a>
#### share_acl

- Schema name: `Share Acl`
- Type: array of object
- Default:
```json
[
  {
    "ae_perm": "FULL",
    "ae_type": "ALLOWED",
    "ae_who_sid": "S-1-1-0",
    "ae_who_id": null,
    "ae_who_str": null
  }
]
```

List of SMB share ACL entries.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_share_acl_items"></a>
##### SMBShareAclEntry

- Schema name: `SMBShareAclEntry`
- Type: object

An SMB Share ACL Entry that grants or denies specific permissions to a principal. You can identify the principal by a SID (`ae_who_sid`), or Unix ID (`ae_who_id`).
- No Additional Properties
<a id="headingReturn_value_share_acl_items_ae_perm"></a>
<a id="Return_value_share_acl_items_ae_perm"></a>
###### ae_perm (required)

- Schema name: `Ae Perm`
- Type: enum (of string)

Permissions granted or denied to the principal. NOTE: this may appear as CUSTOM on read if user has manually edited the share ACL through unsupported means. In this case users will be required to set it to a supported value on update.
###### Must be one of:

- "FULL"
- "CHANGE"
- "READ"
- "CUSTOM"

<a id="headingReturn_value_share_acl_items_ae_type"></a>
<a id="Return_value_share_acl_items_ae_type"></a>
###### ae_type (required)

- Schema name: `Ae Type`
- Type: enum (of string)

The type of SMB share ACL entry. This value determines whether the permissions (ae_perm) are granted (ALLOWED) or denied (DENIED).
###### Must be one of:

- "ALLOWED"
- "DENIED"

<a id="headingReturn_value_share_acl_items_ae_who_sid"></a>
<a id="Return_value_share_acl_items_ae_who_sid"></a>
###### ae_who_sid

- Schema name: `Ae Who Sid`
- Default: null

The SID of the principal to whom this ACL entry applies.
<a id="Return_value_share_acl_items_ae_who_sid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_share_acl_items_ae_who_sid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_share_acl_items_ae_who_sid_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_share_acl_items_ae_who_sid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_share_acl_items_ae_who_sid_anyOf_i1)

- Type: null

<a id="headingReturn_value_share_acl_items_ae_who_id"></a>
<a id="Return_value_share_acl_items_ae_who_id"></a>
###### ae_who_id

- Default: null

The Unix ID of the principal to whom this ACL entry applies.
<a id="Return_value_share_acl_items_ae_who_id_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_share_acl_items_ae_who_id_anyOf_i0"></a>
###### [SMBShareAclEntryWhoId](#tab-pane_Return_value_share_acl_items_ae_who_id_anyOf_i0)

- Schema name: `SMBShareAclEntryWhoId`
- Type: object
- No Additional Properties
<a id="headingReturn_value_share_acl_items_ae_who_id_anyOf_i0_id_type"></a>
<a id="Return_value_share_acl_items_ae_who_id_anyOf_i0_id_type"></a>
###### id_type (required)

- Schema name: `Id Type`
- Type: enum (of string)

The type of Unix ID. If the type is `USER`, the `xid` value refers to a Unix UID. If the type is `GROUP`, the `xid` value refers to a Unix GID.
###### Must be one of:

- "USER"
- "GROUP"

<a id="headingReturn_value_share_acl_items_ae_who_id_anyOf_i0_id"></a>
<a id="Return_value_share_acl_items_ae_who_id_anyOf_i0_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unix user ID (UID) or group ID (GID) depending on the `id_type` field.
- Value must be greater or equal to `0` and lesser or equal to `2147483647`

<a id="tab-pane_Return_value_share_acl_items_ae_who_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_share_acl_items_ae_who_id_anyOf_i1)

- Type: null

<a id="headingReturn_value_share_acl_items_ae_who_str"></a>
<a id="Return_value_share_acl_items_ae_who_str"></a>
###### ae_who_str

- Schema name: `Ae Who Str`
- Default: null

The User or group name of the principal to whom this ACL entry applies.
<a id="Return_value_share_acl_items_ae_who_str_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_share_acl_items_ae_who_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_share_acl_items_ae_who_str_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_share_acl_items_ae_who_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_share_acl_items_ae_who_str_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
