---
title: filesystem.getacl
kind: method
source_rst: _sources/api_methods_filesystem.getacl.rst.txt
source_html: api_methods_filesystem.getacl.html
required_roles:
  - FILESYSTEM_ATTRS_READ
---

# filesystem.getacl

## Summary

Return ACL of a given path. This may return a POSIX1e ACL or a NFSv4 ACL. The ACL type is indicated by the `acltype` key.

## Required Roles

- `FILESYSTEM_ATTRS_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: path

<a id="Call_parameters_items_i0"></a>
#### path

- Schema name: `path`
- Type: string

Absolute filesystem path to get ACL information for.
- Must be at least `1` characters long

#### Parameter 2: simplified

<a id="Call_parameters_items_i1"></a>
#### simplified

- Schema name: `simplified`
- Type: boolean
- Default: true

Whether to return simplified/basic permission sets instead of advanced permissions.

#### Parameter 3: resolve_ids

<a id="Call_parameters_items_i2"></a>
#### resolve_ids

- Schema name: `resolve_ids`
- Type: boolean
- Default: false

Whether to resolve numeric user/group IDs to names in the response.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`

ACL information for the requested filesystem path.
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [NFS4ACLResult](#tab-pane_Return_value_anyOf_i0)

- Schema name: `NFS4ACLResult`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_path"></a>
<a id="Return_value_anyOf_i0_path"></a>
###### path (required)

- Schema name: `Path`
- Type: string

Absolute filesystem path this ACL information applies to.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_user"></a>
<a id="Return_value_anyOf_i0_user"></a>
###### user (required)

- Schema name: `User`

Username of the file/directory owner or `null` if unresolved.
<a id="Return_value_anyOf_i0_user_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_user_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_user_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_user_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_user_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_group"></a>
<a id="Return_value_anyOf_i0_group"></a>
###### group (required)

- Schema name: `Group`

Group name of the file/directory group or `null` if unresolved.
<a id="Return_value_anyOf_i0_group_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_group_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_group_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_group_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_group_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_uid"></a>
<a id="Return_value_anyOf_i0_uid"></a>
###### uid (required)

- Schema name: `Uid`

Numeric user ID for file/directory ownership or `null` to preserve existing.
<a id="Return_value_anyOf_i0_uid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_uid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_uid_anyOf_i0)

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

<a id="tab-pane_Return_value_anyOf_i0_uid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_uid_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_gid"></a>
<a id="Return_value_anyOf_i0_gid"></a>
###### gid (required)

- Schema name: `Gid`

Numeric group ID for file/directory ownership or `null` to preserve existing.
<a id="Return_value_anyOf_i0_gid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_gid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_gid_anyOf_i0)

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

<a id="tab-pane_Return_value_anyOf_i0_gid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_gid_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_acltype"></a>
<a id="Return_value_anyOf_i0_acltype"></a>
###### acltype (required)

- Schema name: `Acltype`
- Type: const

ACL type identifier for NFS4 access control lists.
- Specific value: `"NFS4"`

<a id="headingReturn_value_anyOf_i0_acl"></a>
<a id="Return_value_anyOf_i0_acl"></a>
###### acl (required)

- Schema name: `Acl`
- Type: array of object

Array of NFS4 Access Control Entries defining permissions.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_acl_items"></a>
###### NFS4ACE

- Schema name: `NFS4ACE`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_acl_items_tag"></a>
<a id="Return_value_anyOf_i0_acl_items_tag"></a>
###### tag (required)

- Schema name: `Tag`
- Type: enum (of string)

Subject type for this ACE. `owner@`: File/directory owner `group@`: File/directory primary group `everyone@`: All users `USER`: Specific user account `GROUP`: Specific group
###### Must be one of:

- "owner@"
- "group@"
- "everyone@"
- "USER"
- "GROUP"

<a id="headingReturn_value_anyOf_i0_acl_items_type"></a>
<a id="Return_value_anyOf_i0_acl_items_type"></a>
###### type (required)

- Schema name: `Type`
- Type: enum (of string)

Access control type. `ALLOW`: Grant the specified permissions `DENY`: Explicitly deny the specified permissions
###### Must be one of:

- "ALLOW"
- "DENY"

<a id="headingReturn_value_anyOf_i0_acl_items_perms"></a>
<a id="Return_value_anyOf_i0_acl_items_perms"></a>
###### perms (required)

- Schema name: `Perms`

Permissions granted or denied by this ACE.
<a id="Return_value_anyOf_i0_acl_items_perms_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_acl_items_perms_anyOf_i0"></a>
###### [NFS4ACE_AdvancedPerms](#tab-pane_Return_value_anyOf_i0_acl_items_perms_anyOf_i0)

- Schema name: `NFS4ACE_AdvancedPerms`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_acl_items_perms_anyOf_i0_READ_DATA"></a>
<a id="Return_value_anyOf_i0_acl_items_perms_anyOf_i0_READ_DATA"></a>
###### READ_DATA

- Schema name: `Read Data`
- Type: boolean
- Default: false

Permission to read file data or list directory contents.

<a id="headingReturn_value_anyOf_i0_acl_items_perms_anyOf_i0_WRITE_DATA"></a>
<a id="Return_value_anyOf_i0_acl_items_perms_anyOf_i0_WRITE_DATA"></a>
###### WRITE_DATA

- Schema name: `Write Data`
- Type: boolean
- Default: false

Permission to write file data or create files in directory.

<a id="headingReturn_value_anyOf_i0_acl_items_perms_anyOf_i0_APPEND_DATA"></a>
<a id="Return_value_anyOf_i0_acl_items_perms_anyOf_i0_APPEND_DATA"></a>
###### APPEND_DATA

- Schema name: `Append Data`
- Type: boolean
- Default: false

Permission to append data to files or create subdirectories.

<a id="headingReturn_value_anyOf_i0_acl_items_perms_anyOf_i0_READ_NAMED_ATTRS"></a>
<a id="Return_value_anyOf_i0_acl_items_perms_anyOf_i0_READ_NAMED_ATTRS"></a>
###### READ_NAMED_ATTRS

- Schema name: `Read Named Attrs`
- Type: boolean
- Default: false

Permission to read named attributes (extended attributes).

<a id="headingReturn_value_anyOf_i0_acl_items_perms_anyOf_i0_WRITE_NAMED_ATTRS"></a>
<a id="Return_value_anyOf_i0_acl_items_perms_anyOf_i0_WRITE_NAMED_ATTRS"></a>
###### WRITE_NAMED_ATTRS

- Schema name: `Write Named Attrs`
- Type: boolean
- Default: false

Permission to write named attributes (extended attributes).

<a id="headingReturn_value_anyOf_i0_acl_items_perms_anyOf_i0_EXECUTE"></a>
<a id="Return_value_anyOf_i0_acl_items_perms_anyOf_i0_EXECUTE"></a>
###### EXECUTE

- Schema name: `Execute`
- Type: boolean
- Default: false

Permission to execute files or traverse directories.

<a id="headingReturn_value_anyOf_i0_acl_items_perms_anyOf_i0_DELETE"></a>
<a id="Return_value_anyOf_i0_acl_items_perms_anyOf_i0_DELETE"></a>
###### DELETE

- Schema name: `Delete`
- Type: boolean
- Default: false

Permission to delete the file or directory.

<a id="headingReturn_value_anyOf_i0_acl_items_perms_anyOf_i0_DELETE_CHILD"></a>
<a id="Return_value_anyOf_i0_acl_items_perms_anyOf_i0_DELETE_CHILD"></a>
###### DELETE_CHILD

- Schema name: `Delete Child`
- Type: boolean
- Default: false

Permission to delete child files within a directory.

<a id="headingReturn_value_anyOf_i0_acl_items_perms_anyOf_i0_READ_ATTRIBUTES"></a>
<a id="Return_value_anyOf_i0_acl_items_perms_anyOf_i0_READ_ATTRIBUTES"></a>
###### READ_ATTRIBUTES

- Schema name: `Read Attributes`
- Type: boolean
- Default: false

Permission to read basic file attributes (size, timestamps, etc.).

<a id="headingReturn_value_anyOf_i0_acl_items_perms_anyOf_i0_WRITE_ATTRIBUTES"></a>
<a id="Return_value_anyOf_i0_acl_items_perms_anyOf_i0_WRITE_ATTRIBUTES"></a>
###### WRITE_ATTRIBUTES

- Schema name: `Write Attributes`
- Type: boolean
- Default: false

Permission to write basic file attributes.

<a id="headingReturn_value_anyOf_i0_acl_items_perms_anyOf_i0_READ_ACL"></a>
<a id="Return_value_anyOf_i0_acl_items_perms_anyOf_i0_READ_ACL"></a>
###### READ_ACL

- Schema name: `Read Acl`
- Type: boolean
- Default: false

Permission to read the Access Control List.

<a id="headingReturn_value_anyOf_i0_acl_items_perms_anyOf_i0_WRITE_ACL"></a>
<a id="Return_value_anyOf_i0_acl_items_perms_anyOf_i0_WRITE_ACL"></a>
###### WRITE_ACL

- Schema name: `Write Acl`
- Type: boolean
- Default: false

Permission to modify the Access Control List.

<a id="headingReturn_value_anyOf_i0_acl_items_perms_anyOf_i0_WRITE_OWNER"></a>
<a id="Return_value_anyOf_i0_acl_items_perms_anyOf_i0_WRITE_OWNER"></a>
###### WRITE_OWNER

- Schema name: `Write Owner`
- Type: boolean
- Default: false

Permission to change the file owner.

<a id="headingReturn_value_anyOf_i0_acl_items_perms_anyOf_i0_SYNCHRONIZE"></a>
<a id="Return_value_anyOf_i0_acl_items_perms_anyOf_i0_SYNCHRONIZE"></a>
###### SYNCHRONIZE

- Schema name: `Synchronize`
- Type: boolean
- Default: false

Permission to use the file/directory as a synchronization primitive.

<a id="tab-pane_Return_value_anyOf_i0_acl_items_perms_anyOf_i1"></a>
###### [NFS4ACE_BasicPerms](#tab-pane_Return_value_anyOf_i0_acl_items_perms_anyOf_i1)

- Schema name: `NFS4ACE_BasicPerms`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_acl_items_perms_anyOf_i1_BASIC"></a>
<a id="Return_value_anyOf_i0_acl_items_perms_anyOf_i1_BASIC"></a>
###### BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic permission level for NFS4 ACE. `FULL_CONTROL`: Full read, write, execute, and administrative permissions `MODIFY`: Read, write, and execute permissions `READ`: Read-only permissions `TRAVERSE`: Execute/traverse permissions only
###### Must be one of:

- "FULL_CONTROL"
- "MODIFY"
- "READ"
- "TRAVERSE"

<a id="headingReturn_value_anyOf_i0_acl_items_flags"></a>
<a id="Return_value_anyOf_i0_acl_items_flags"></a>
###### flags (required)

- Schema name: `Flags`

Inheritance and other behavioral flags for this ACE.
<a id="Return_value_anyOf_i0_acl_items_flags_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_acl_items_flags_anyOf_i0"></a>
###### [NFS4ACE_AdvancedFlags](#tab-pane_Return_value_anyOf_i0_acl_items_flags_anyOf_i0)

- Schema name: `NFS4ACE_AdvancedFlags`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_acl_items_flags_anyOf_i0_FILE_INHERIT"></a>
<a id="Return_value_anyOf_i0_acl_items_flags_anyOf_i0_FILE_INHERIT"></a>
###### FILE_INHERIT

- Schema name: `File Inherit`
- Type: boolean
- Default: false

Apply this ACE to files within directories.

<a id="headingReturn_value_anyOf_i0_acl_items_flags_anyOf_i0_DIRECTORY_INHERIT"></a>
<a id="Return_value_anyOf_i0_acl_items_flags_anyOf_i0_DIRECTORY_INHERIT"></a>
###### DIRECTORY_INHERIT

- Schema name: `Directory Inherit`
- Type: boolean
- Default: false

Apply this ACE to subdirectories within directories.

<a id="headingReturn_value_anyOf_i0_acl_items_flags_anyOf_i0_NO_PROPAGATE_INHERIT"></a>
<a id="Return_value_anyOf_i0_acl_items_flags_anyOf_i0_NO_PROPAGATE_INHERIT"></a>
###### NO_PROPAGATE_INHERIT

- Schema name: `No Propagate Inherit`
- Type: boolean
- Default: false

Do not propagate inheritance beyond immediate children.

<a id="headingReturn_value_anyOf_i0_acl_items_flags_anyOf_i0_INHERIT_ONLY"></a>
<a id="Return_value_anyOf_i0_acl_items_flags_anyOf_i0_INHERIT_ONLY"></a>
###### INHERIT_ONLY

- Schema name: `Inherit Only`
- Type: boolean
- Default: false

This ACE only affects inheritance, not the object itself.

<a id="headingReturn_value_anyOf_i0_acl_items_flags_anyOf_i0_INHERITED"></a>
<a id="Return_value_anyOf_i0_acl_items_flags_anyOf_i0_INHERITED"></a>
###### INHERITED

- Schema name: `Inherited`
- Type: boolean
- Default: false

This ACE was inherited from a parent directory.

<a id="tab-pane_Return_value_anyOf_i0_acl_items_flags_anyOf_i1"></a>
###### [NFS4ACE_BasicFlags](#tab-pane_Return_value_anyOf_i0_acl_items_flags_anyOf_i1)

- Schema name: `NFS4ACE_BasicFlags`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_acl_items_flags_anyOf_i1_BASIC"></a>
<a id="Return_value_anyOf_i0_acl_items_flags_anyOf_i1_BASIC"></a>
###### BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic inheritance behavior for NFS4 ACE. `INHERIT`: Apply to child files and directories `NOINHERIT`: Do not apply to child objects
###### Must be one of:

- "INHERIT"
- "NOINHERIT"

<a id="headingReturn_value_anyOf_i0_acl_items_id"></a>
<a id="Return_value_anyOf_i0_acl_items_id"></a>
###### id

- Schema name: `Id`
- Default: null

UID or GID when `tag` is "USER" or "GROUP". `null` for special entries.
<a id="Return_value_anyOf_i0_acl_items_id_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_acl_items_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_acl_items_id_anyOf_i0)

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

<a id="tab-pane_Return_value_anyOf_i0_acl_items_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_acl_items_id_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_acl_items_who"></a>
<a id="Return_value_anyOf_i0_acl_items_who"></a>
###### who

- Schema name: `Who`
- Default: null

Username or group name when `tag` is "USER" or "GROUP". `null` for special entries.
<a id="Return_value_anyOf_i0_acl_items_who_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_acl_items_who_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_acl_items_who_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_acl_items_who_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_acl_items_who_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_acl_items_who_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_anyOf_i0_acl_items_who_anyOf_i2)

- Type: null

<a id="headingReturn_value_anyOf_i0_aclflags"></a>
<a id="Return_value_anyOf_i0_aclflags"></a>
###### aclflags (required)

- Schema name: `NFS4ACL_Flags`
- Type: object

NFS4 ACL behavioral flags for inheritance and protection.
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_aclflags_autoinherit"></a>
<a id="Return_value_anyOf_i0_aclflags_autoinherit"></a>
###### autoinherit

- Schema name: `Autoinherit`
- Type: boolean
- Default: false

Whether inheritance is automatically applied from parent directories.

<a id="headingReturn_value_anyOf_i0_aclflags_protected"></a>
<a id="Return_value_anyOf_i0_aclflags_protected"></a>
###### protected

- Schema name: `Protected`
- Type: boolean
- Default: false

Whether the ACL is protected from inheritance modifications.

<a id="headingReturn_value_anyOf_i0_aclflags_defaulted"></a>
<a id="Return_value_anyOf_i0_aclflags_defaulted"></a>
###### defaulted

- Schema name: `Defaulted`
- Type: boolean
- Default: false

Whether this ACL was created by default rules rather than explicit configuration.

<a id="headingReturn_value_anyOf_i0_trivial"></a>
<a id="Return_value_anyOf_i0_trivial"></a>
###### trivial (required)

- Schema name: `Trivial`
- Type: boolean

Whether this ACL is a simple/trivial ACL equivalent to POSIX permissions.

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [POSIXACLResult](#tab-pane_Return_value_anyOf_i1)

- Schema name: `POSIXACLResult`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_path"></a>
<a id="Return_value_anyOf_i1_path"></a>
###### path (required)

- Schema name: `Path`
- Type: string

Absolute filesystem path this ACL information applies to.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_user"></a>
<a id="Return_value_anyOf_i1_user"></a>
###### user (required)

- Schema name: `User`

Username of the file/directory owner or `null` if unresolved.
<a id="Return_value_anyOf_i1_user_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_user_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_user_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i1_user_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_user_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_group"></a>
<a id="Return_value_anyOf_i1_group"></a>
###### group (required)

- Schema name: `Group`

Group name of the file/directory group or `null` if unresolved.
<a id="Return_value_anyOf_i1_group_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_group_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_group_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i1_group_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_group_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_uid"></a>
<a id="Return_value_anyOf_i1_uid"></a>
###### uid (required)

- Schema name: `Uid`

Numeric user ID for file/directory ownership or `null` to preserve existing.
<a id="Return_value_anyOf_i1_uid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_uid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_uid_anyOf_i0)

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

<a id="tab-pane_Return_value_anyOf_i1_uid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_uid_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_gid"></a>
<a id="Return_value_anyOf_i1_gid"></a>
###### gid (required)

- Schema name: `Gid`

Numeric group ID for file/directory ownership or `null` to preserve existing.
<a id="Return_value_anyOf_i1_gid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_gid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_gid_anyOf_i0)

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

<a id="tab-pane_Return_value_anyOf_i1_gid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_gid_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_acltype"></a>
<a id="Return_value_anyOf_i1_acltype"></a>
###### acltype (required)

- Schema name: `Acltype`
- Type: const

ACL type identifier for POSIX.1e access control lists.
- Specific value: `"POSIX1E"`

<a id="headingReturn_value_anyOf_i1_acl"></a>
<a id="Return_value_anyOf_i1_acl"></a>
###### acl (required)

- Schema name: `Acl`
- Type: array of object

Array of POSIX Access Control Entries defining permissions.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_acl_items"></a>
###### POSIXACE

- Schema name: `POSIXACE`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_acl_items_tag"></a>
<a id="Return_value_anyOf_i1_acl_items_tag"></a>
###### tag (required)

- Schema name: `Tag`
- Type: enum (of string)

Subject type for this POSIX ACE. `USER_OBJ`: File/directory owner `GROUP_OBJ`: File/directory primary group `OTHER`: All other users `MASK`: Maximum permissions for named users and groups `USER`: Specific user account `GROUP`: Specific group
###### Must be one of:

- "USER_OBJ"
- "GROUP_OBJ"
- "OTHER"
- "MASK"
- "USER"
- "GROUP"

<a id="headingReturn_value_anyOf_i1_acl_items_perms"></a>
<a id="Return_value_anyOf_i1_acl_items_perms"></a>
###### perms (required)

- Schema name: `POSIXACE_Perms`
- Type: object

Read, write, and execute permissions for this ACE.
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_acl_items_perms_READ"></a>
<a id="Return_value_anyOf_i1_acl_items_perms_READ"></a>
###### READ (required)

- Schema name: `Read`
- Type: boolean

Permission to read file contents or list directory contents.

<a id="headingReturn_value_anyOf_i1_acl_items_perms_WRITE"></a>
<a id="Return_value_anyOf_i1_acl_items_perms_WRITE"></a>
###### WRITE (required)

- Schema name: `Write`
- Type: boolean

Permission to write file contents or create/delete files in directory.

<a id="headingReturn_value_anyOf_i1_acl_items_perms_EXECUTE"></a>
<a id="Return_value_anyOf_i1_acl_items_perms_EXECUTE"></a>
###### EXECUTE (required)

- Schema name: `Execute`
- Type: boolean

Permission to execute files or traverse directories.

<a id="headingReturn_value_anyOf_i1_acl_items_default"></a>
<a id="Return_value_anyOf_i1_acl_items_default"></a>
###### default (required)

- Schema name: `Default`
- Type: boolean

Whether this is a default ACE that applies to newly created child objects.

<a id="headingReturn_value_anyOf_i1_acl_items_id"></a>
<a id="Return_value_anyOf_i1_acl_items_id"></a>
###### id

- Schema name: `Id`
- Default: null

Numeric user or group ID when tag is `USER` or `GROUP`. `null` for object entries.
<a id="Return_value_anyOf_i1_acl_items_id_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_acl_items_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_acl_items_id_anyOf_i0)

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

<a id="tab-pane_Return_value_anyOf_i1_acl_items_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_acl_items_id_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_acl_items_who"></a>
<a id="Return_value_anyOf_i1_acl_items_who"></a>
###### who

- Schema name: `Who`
- Default: null

Username or group name when tag is `USER` or `GROUP`. `null` for object entries.
<a id="Return_value_anyOf_i1_acl_items_who_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_acl_items_who_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_acl_items_who_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_acl_items_who_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_acl_items_who_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i1_acl_items_who_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_anyOf_i1_acl_items_who_anyOf_i2)

- Type: null

<a id="headingReturn_value_anyOf_i1_trivial"></a>
<a id="Return_value_anyOf_i1_trivial"></a>
###### trivial (required)

- Schema name: `Trivial`
- Type: boolean

Whether this ACL is a simple/trivial ACL equivalent to standard POSIX permissions.

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [DISABLED_ACLResult](#tab-pane_Return_value_anyOf_i2)

- Schema name: `DISABLED_ACLResult`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_path"></a>
<a id="Return_value_anyOf_i2_path"></a>
###### path (required)

- Schema name: `Path`
- Type: string

Absolute filesystem path this ACL information applies to.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_user"></a>
<a id="Return_value_anyOf_i2_user"></a>
###### user (required)

- Schema name: `User`

Username of the file/directory owner or `null` if unresolved.
<a id="Return_value_anyOf_i2_user_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_user_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_user_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i2_user_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_user_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_group"></a>
<a id="Return_value_anyOf_i2_group"></a>
###### group (required)

- Schema name: `Group`

Group name of the file/directory group or `null` if unresolved.
<a id="Return_value_anyOf_i2_group_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_group_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_group_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i2_group_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_group_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_uid"></a>
<a id="Return_value_anyOf_i2_uid"></a>
###### uid (required)

- Schema name: `Uid`

Numeric user ID for file/directory ownership or `null` to preserve existing.
<a id="Return_value_anyOf_i2_uid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_uid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_uid_anyOf_i0)

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

<a id="tab-pane_Return_value_anyOf_i2_uid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_uid_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_gid"></a>
<a id="Return_value_anyOf_i2_gid"></a>
###### gid (required)

- Schema name: `Gid`

Numeric group ID for file/directory ownership or `null` to preserve existing.
<a id="Return_value_anyOf_i2_gid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_gid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_gid_anyOf_i0)

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

<a id="tab-pane_Return_value_anyOf_i2_gid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_gid_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_acltype"></a>
<a id="Return_value_anyOf_i2_acltype"></a>
###### acltype (required)

- Schema name: `Acltype`
- Type: const

ACL type identifier indicating access control lists are disabled.
- Specific value: `"DISABLED"`

<a id="headingReturn_value_anyOf_i2_acl"></a>
<a id="Return_value_anyOf_i2_acl"></a>
###### acl (required)

- Schema name: `Acl`
- Type: null

Always `null` when ACLs are disabled on the filesystem.

<a id="headingReturn_value_anyOf_i2_trivial"></a>
<a id="Return_value_anyOf_i2_trivial"></a>
###### trivial (required)

- Schema name: `Trivial`
- Type: const

Always `true` when ACLs are disabled - only basic POSIX permissions apply.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
