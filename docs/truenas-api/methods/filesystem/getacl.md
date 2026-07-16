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

Return ACL of a given path. This may return a POSIX1e ACL or a NFSv4 ACL. The acl type is indicated by the `acltype` key.

`simplified` - effect of this depends on ACL type on underlying filesystem. In the case of NFSv4 ACLs simplified permissions and flags are returned for ACL entries where applicable. NFSv4 errata below. In the case of POSIX1E ACls, this setting has no impact on returned ACL.

`resolve_ids` - adds additional `who` key to each ACL entry, that converts the numeric id to a user name or group name. In the case of owner@ and group@ (NFSv4) or USER_OBJ and GROUP_OBJ (POSIX1E), st_uid or st_gid will be converted from stat() return for file. In the case of MASK (POSIX1E), OTHER (POSIX1E), everyone@ (NFSv4), key `who` will be included, but set to null. In case of failure to resolve the id to a name, `who` will be set to null. This option should only be used if resolving ids to names is required.

Errata about ACLType NFSv4:

`simplified` returns a shortened form of the ACL permset and flags where applicable. If permissions have been simplified, then the `perms` object will contain only a single `BASIC` key with a string describing the underlying permissions set.

`TRAVERSE` sufficient rights to traverse a directory, but not read contents.

`READ` sufficient rights to traverse a directory, and read file contents.

`MODIFIY` sufficient rights to traverse, read, write, and modify a file.

`FULL_CONTROL` all permissions.

If the permisssions do not fit within one of the pre-defined simplified permissions types, then the full ACL entry will be returned.

## Required Roles

- `FILESYSTEM_ATTRS_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: path

#### path

- Schema name: `path`
- Type: string

Absolute filesystem path to get ACL information for.
- Must be at least `1` characters long

#### Parameter 2: simplified

#### simplified

- Schema name: `simplified`
- Type: boolean
- Default: true

Whether to return simplified/basic permission sets instead of advanced permissions.

#### Parameter 3: resolve_ids

#### resolve_ids

- Schema name: `resolve_ids`
- Type: boolean
- Default: false

Whether to resolve numeric user/group IDs to names in the response.

### Return value

- Schema name: `Result`

ACL information for the requested filesystem path.
#### Any of

##### NFS4ACLResult

- Schema name: `NFS4ACLResult`
- Type: object
- No Additional Properties
###### path (required)

- Schema name: `Path`
- Type: string

Absolute filesystem path this ACL information applies to.
- Must be at least `1` characters long

###### user (required)

- Schema name: `User`

Username of the file/directory owner or `null` if unresolved.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

###### group (required)

- Schema name: `Group`

Group name of the file/directory group or `null` if unresolved.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

###### uid (required)

- Schema name: `Uid`

Numeric user ID for file/directory ownership or `null` to preserve existing.
####### Any of

######## Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

######## Option 2

- Type: null

###### gid (required)

- Schema name: `Gid`

Numeric group ID for file/directory ownership or `null` to preserve existing.
####### Any of

######## Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

######## Option 2

- Type: null

###### acltype (required)

- Schema name: `Acltype`
- Type: const

ACL type identifier for NFS4 access control lists.

###### acl (required)

- Schema name: `Acl`
- Type: array of object

Array of NFS4 Access Control Entries defining permissions.
- No Additional Items

####### Each item of this array must be:

####### NFS4ACE

- Schema name: `NFS4ACE`
- Type: object
- No Additional Properties
######## tag (required)

- Schema name: `Tag`
- Type: enum (of string)

Subject type for this ACE. `owner@`: File/directory owner `group@`: File/directory primary group `everyone@`: All users `USER`: Specific user account `GROUP`: Specific group

######## type (required)

- Schema name: `Type`
- Type: enum (of string)

Access control type. `ALLOW`: Grant the specified permissions `DENY`: Explicitly deny the specified permissions

######## perms (required)

- Schema name: `Perms`

Permissions granted or denied by this ACE.
######### Any of

########## NFS4ACE_AdvancedPerms

- Schema name: `NFS4ACE_AdvancedPerms`
- Type: object
- No Additional Properties
########### READ_DATA

- Schema name: `Read Data`
- Type: boolean
- Default: false

Permission to read file data or list directory contents.

########### WRITE_DATA

- Schema name: `Write Data`
- Type: boolean
- Default: false

Permission to write file data or create files in directory.

########### APPEND_DATA

- Schema name: `Append Data`
- Type: boolean
- Default: false

Permission to append data to files or create subdirectories.

########### READ_NAMED_ATTRS

- Schema name: `Read Named Attrs`
- Type: boolean
- Default: false

Permission to read named attributes (extended attributes).

########### WRITE_NAMED_ATTRS

- Schema name: `Write Named Attrs`
- Type: boolean
- Default: false

Permission to write named attributes (extended attributes).

########### EXECUTE

- Schema name: `Execute`
- Type: boolean
- Default: false

Permission to execute files or traverse directories.

########### DELETE

- Schema name: `Delete`
- Type: boolean
- Default: false

Permission to delete the file or directory.

########### DELETE_CHILD

- Schema name: `Delete Child`
- Type: boolean
- Default: false

Permission to delete child files within a directory.

########### READ_ATTRIBUTES

- Schema name: `Read Attributes`
- Type: boolean
- Default: false

Permission to read basic file attributes (size, timestamps, etc.).

########### WRITE_ATTRIBUTES

- Schema name: `Write Attributes`
- Type: boolean
- Default: false

Permission to write basic file attributes.

########### READ_ACL

- Schema name: `Read Acl`
- Type: boolean
- Default: false

Permission to read the Access Control List.

########### WRITE_ACL

- Schema name: `Write Acl`
- Type: boolean
- Default: false

Permission to modify the Access Control List.

########### WRITE_OWNER

- Schema name: `Write Owner`
- Type: boolean
- Default: false

Permission to change the file owner.

########### SYNCHRONIZE

- Schema name: `Synchronize`
- Type: boolean
- Default: false

Permission to use the file/directory as a synchronization primitive.

########## NFS4ACE_BasicPerms

- Schema name: `NFS4ACE_BasicPerms`
- Type: object
- No Additional Properties
########### BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic permission level for NFS4 ACE. `FULL_CONTROL`: Full read, write, execute, and administrative permissions `MODIFY`: Read, write, and execute permissions `READ`: Read-only permissions `TRAVERSE`: Execute/traverse permissions only

######## flags (required)

- Schema name: `Flags`

Inheritance and other behavioral flags for this ACE.
######### Any of

########## NFS4ACE_AdvancedFlags

- Schema name: `NFS4ACE_AdvancedFlags`
- Type: object
- No Additional Properties
########### FILE_INHERIT

- Schema name: `File Inherit`
- Type: boolean
- Default: false

Apply this ACE to files within directories.

########### DIRECTORY_INHERIT

- Schema name: `Directory Inherit`
- Type: boolean
- Default: false

Apply this ACE to subdirectories within directories.

########### NO_PROPAGATE_INHERIT

- Schema name: `No Propagate Inherit`
- Type: boolean
- Default: false

Do not propagate inheritance beyond immediate children.

########### INHERIT_ONLY

- Schema name: `Inherit Only`
- Type: boolean
- Default: false

This ACE only affects inheritance, not the object itself.

########### INHERITED

- Schema name: `Inherited`
- Type: boolean
- Default: false

This ACE was inherited from a parent directory.

########## NFS4ACE_BasicFlags

- Schema name: `NFS4ACE_BasicFlags`
- Type: object
- No Additional Properties
########### BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic inheritance behavior for NFS4 ACE. `INHERIT`: Apply to child files and directories `NOINHERIT`: Do not apply to child objects

######## id

- Schema name: `Id`
- Default: null

UID or GID when `tag` is "USER" or "GROUP". `null` for special entries.
######### Any of

########## Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

########## Option 2

- Type: null

######## who

- Schema name: `Who`
- Default: null

Username or group name when `tag` is "USER" or "GROUP". `null` for special entries.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: string
- Must be at least `1` characters long

########## Option 3

- Type: null

###### aclflags (required)

- Schema name: `NFS4ACL_Flags`
- Type: object

NFS4 ACL behavioral flags for inheritance and protection.
- No Additional Properties
####### autoinherit

- Schema name: `Autoinherit`
- Type: boolean
- Default: false

Whether inheritance is automatically applied from parent directories.

####### protected

- Schema name: `Protected`
- Type: boolean
- Default: false

Whether the ACL is protected from inheritance modifications.

####### defaulted

- Schema name: `Defaulted`
- Type: boolean
- Default: false

Whether this ACL was created by default rules rather than explicit configuration.

###### trivial (required)

- Schema name: `Trivial`
- Type: boolean

Whether this ACL is a simple/trivial ACL equivalent to POSIX permissions.

##### POSIXACLResult

- Type: string
- Must be at least `1` characters long

##### DISABLED_ACLResult

- Type: null

##### Option 1

- Type: string
- Must be at least `1` characters long

##### Option 2

- Type: null

##### Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

##### Option 2

- Type: null

##### Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

##### Option 2

- Type: null

##### Option 1

- Schema name: `NFS4ACE_AdvancedPerms`
- Type: object
- No Additional Properties
###### READ_DATA

- Schema name: `Read Data`
- Type: boolean
- Default: false

Permission to read file data or list directory contents.

###### WRITE_DATA

- Schema name: `Write Data`
- Type: boolean
- Default: false

Permission to write file data or create files in directory.

###### APPEND_DATA

- Schema name: `Append Data`
- Type: boolean
- Default: false

Permission to append data to files or create subdirectories.

###### READ_NAMED_ATTRS

- Schema name: `Read Named Attrs`
- Type: boolean
- Default: false

Permission to read named attributes (extended attributes).

###### WRITE_NAMED_ATTRS

- Schema name: `Write Named Attrs`
- Type: boolean
- Default: false

Permission to write named attributes (extended attributes).

###### EXECUTE

- Schema name: `Execute`
- Type: boolean
- Default: false

Permission to execute files or traverse directories.

###### DELETE

- Schema name: `Delete`
- Type: boolean
- Default: false

Permission to delete the file or directory.

###### DELETE_CHILD

- Schema name: `Delete Child`
- Type: boolean
- Default: false

Permission to delete child files within a directory.

###### READ_ATTRIBUTES

- Schema name: `Read Attributes`
- Type: boolean
- Default: false

Permission to read basic file attributes (size, timestamps, etc.).

###### WRITE_ATTRIBUTES

- Schema name: `Write Attributes`
- Type: boolean
- Default: false

Permission to write basic file attributes.

###### READ_ACL

- Schema name: `Read Acl`
- Type: boolean
- Default: false

Permission to read the Access Control List.

###### WRITE_ACL

- Schema name: `Write Acl`
- Type: boolean
- Default: false

Permission to modify the Access Control List.

###### WRITE_OWNER

- Schema name: `Write Owner`
- Type: boolean
- Default: false

Permission to change the file owner.

###### SYNCHRONIZE

- Schema name: `Synchronize`
- Type: boolean
- Default: false

Permission to use the file/directory as a synchronization primitive.

##### Option 2

- Schema name: `NFS4ACE_BasicPerms`
- Type: object
- No Additional Properties
###### BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic permission level for NFS4 ACE. `FULL_CONTROL`: Full read, write, execute, and administrative permissions `MODIFY`: Read, write, and execute permissions `READ`: Read-only permissions `TRAVERSE`: Execute/traverse permissions only

##### NFS4ACE_AdvancedPerms

- Schema name: `NFS4ACE_AdvancedFlags`
- Type: object
- No Additional Properties
###### FILE_INHERIT

- Schema name: `File Inherit`
- Type: boolean
- Default: false

Apply this ACE to files within directories.

###### DIRECTORY_INHERIT

- Schema name: `Directory Inherit`
- Type: boolean
- Default: false

Apply this ACE to subdirectories within directories.

###### NO_PROPAGATE_INHERIT

- Schema name: `No Propagate Inherit`
- Type: boolean
- Default: false

Do not propagate inheritance beyond immediate children.

###### INHERIT_ONLY

- Schema name: `Inherit Only`
- Type: boolean
- Default: false

This ACE only affects inheritance, not the object itself.

###### INHERITED

- Schema name: `Inherited`
- Type: boolean
- Default: false

This ACE was inherited from a parent directory.

##### NFS4ACE_BasicPerms

- Schema name: `NFS4ACE_BasicFlags`
- Type: object
- No Additional Properties
###### BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic inheritance behavior for NFS4 ACE. `INHERIT`: Apply to child files and directories `NOINHERIT`: Do not apply to child objects

##### NFS4ACE_AdvancedFlags

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

##### NFS4ACE_BasicFlags

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: string
- Must be at least `1` characters long

##### Option 1

- Type: null

##### Option 2

- Schema name: `POSIXACLResult`
- Type: object
- No Additional Properties
###### path (required)

- Schema name: `Path`
- Type: string

Absolute filesystem path this ACL information applies to.
- Must be at least `1` characters long

###### user (required)

- Schema name: `User`

Username of the file/directory owner or `null` if unresolved.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

###### group (required)

- Schema name: `Group`

Group name of the file/directory group or `null` if unresolved.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

###### uid (required)

- Schema name: `Uid`

Numeric user ID for file/directory ownership or `null` to preserve existing.
####### Any of

######## Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

######## Option 2

- Type: null

###### gid (required)

- Schema name: `Gid`

Numeric group ID for file/directory ownership or `null` to preserve existing.
####### Any of

######## Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

######## Option 2

- Type: null

###### acltype (required)

- Schema name: `Acltype`
- Type: const

ACL type identifier for POSIX.1e access control lists.

###### acl (required)

- Schema name: `Acl`
- Type: array of object

Array of POSIX Access Control Entries defining permissions.
- No Additional Items

####### Each item of this array must be:

####### POSIXACE

- Schema name: `POSIXACE`
- Type: object
- No Additional Properties
######## tag (required)

- Schema name: `Tag`
- Type: enum (of string)

Subject type for this POSIX ACE. `USER_OBJ`: File/directory owner `GROUP_OBJ`: File/directory primary group `OTHER`: All other users `MASK`: Maximum permissions for named users and groups `USER`: Specific user account `GROUP`: Specific group

######## perms (required)

- Schema name: `POSIXACE_Perms`
- Type: object

Read, write, and execute permissions for this ACE.
- No Additional Properties
######### READ (required)

- Schema name: `Read`
- Type: boolean

Permission to read file contents or list directory contents.

######### WRITE (required)

- Schema name: `Write`
- Type: boolean

Permission to write file contents or create/delete files in directory.

######### EXECUTE (required)

- Schema name: `Execute`
- Type: boolean

Permission to execute files or traverse directories.

######## default (required)

- Schema name: `Default`
- Type: boolean

Whether this is a default ACE that applies to newly created child objects.

######## id

- Schema name: `Id`
- Default: null

Numeric user or group ID when tag is `USER` or `GROUP`. `null` for object entries.
######### Any of

########## Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

########## Option 2

- Type: null

######## who

- Schema name: `Who`
- Default: null

Username or group name when tag is `USER` or `GROUP`. `null` for object entries.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: string
- Must be at least `1` characters long

########## Option 3

- Type: null

###### trivial (required)

- Schema name: `Trivial`
- Type: boolean

Whether this ACL is a simple/trivial ACL equivalent to standard POSIX permissions.

##### Option 3

- Type: string
- Must be at least `1` characters long

##### Option 1

- Type: null

##### Option 2

- Type: string
- Must be at least `1` characters long

##### Option 1

- Type: null

##### Option 2

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

##### Option 1

- Type: null

##### Option 2

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

##### Option 1

- Type: null

##### Option 2

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: string
- Must be at least `1` characters long

##### Option 2

- Type: null

##### Option 3

- Schema name: `DISABLED_ACLResult`
- Type: object
- No Additional Properties
###### path (required)

- Schema name: `Path`
- Type: string

Absolute filesystem path this ACL information applies to.
- Must be at least `1` characters long

###### user (required)

- Schema name: `User`

Username of the file/directory owner or `null` if unresolved.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

###### group (required)

- Schema name: `Group`

Group name of the file/directory group or `null` if unresolved.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

###### uid (required)

- Schema name: `Uid`

Numeric user ID for file/directory ownership or `null` to preserve existing.
####### Any of

######## Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

######## Option 2

- Type: null

###### gid (required)

- Schema name: `Gid`

Numeric group ID for file/directory ownership or `null` to preserve existing.
####### Any of

######## Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

######## Option 2

- Type: null

###### acltype (required)

- Schema name: `Acltype`
- Type: const

ACL type identifier indicating access control lists are disabled.

###### acl (required)

- Schema name: `Acl`
- Type: null

Always `null` when ACLs are disabled on the filesystem.

###### trivial (required)

- Schema name: `Trivial`
- Type: const

Always `true` when ACLs are disabled - only basic POSIX permissions apply.

##### Option 1

- Type: string
- Must be at least `1` characters long

##### Option 2

- Type: null

##### Option 1

- Type: string
- Must be at least `1` characters long

##### Option 2

- Type: null

##### Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

##### Option 2

- Type: null

##### Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

##### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
