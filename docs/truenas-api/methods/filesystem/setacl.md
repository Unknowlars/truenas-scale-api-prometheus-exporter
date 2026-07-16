---
title: filesystem.setacl
kind: method
source_rst: _sources/api_methods_filesystem.setacl.rst.txt
source_html: api_methods_filesystem.setacl.html
required_roles:
  - FILESYSTEM_ATTRS_WRITE
---

# filesystem.setacl

## Summary

Set ACL of a given path. Takes the following parameters: `path` full path to directory or file.

`dacl` ACL entries. Formatting depends on the underlying `acltype`. NFS4ACL requires NFSv4 entries. POSIX1e requires POSIX1e entries.

`uid` the desired UID of the file user. If set to None (the default), then user is not changed.

`user` the desired username for the file user. If set to None, then user is not changed.

Note about interaction between `uid` and `user`: One and only one of these parameters should be set, and _only_ if the API consumer wishes to change the owner on the file / directory.

`gid` the desired GID of the file group. If set to None (the default), then group is not changed.

`group` the desired groupname for the file group. If set to None (the default), then group is not changed.

Note about interaction between `gid` and `group`: One and only one of these parameters should be set, and _only_ if the API consumer wishes to change the owner on the file / directory.

WARNING: if user, uid, group, or gid is specified in a recursive operation then the owning user, group, or both for _all_ files will be changed.

`recursive` apply the ACL recursively

`traverse` traverse filestem boundaries (ZFS datasets)

`strip` convert ACL to trivial. ACL is trivial if it can be expressed as a file mode without losing any access rules.

`canonicalize` reorder ACL entries so that they are in concanical form as described in the Microsoft documentation MS-DTYP 2.4.5 (ACL). This only applies to NFSv4 ACLs.

The following notes about ACL entries are necessarily terse. If more detail is requried please consult relevant TrueNAS documentation.

Notes about NFSv4 ACL entry fields:

`tag` refers to the type of principal to whom the ACL entries applies. USER and GROUP have conventional meanings. `owner@` refers to the owning user of the file, `group@` refers to the owning group of the file, and `everyone@` refers to ALL users (including the owning user and group)..

`id` refers to the numeric user id or group id associatiated with USER or GROUP entries.

`who` a user or group name may be specified in lieu of numeric ID for USER or GROUP entries

`type` may be ALLOW or DENY. Deny entries take precedence over allow when the ACL is evaluated.

`perms` permissions allowed or denied by the entry. May be set as a simlified BASIC type or more complex type detailing specific permissions.

`flags` inheritance flags determine how this entry will be presented (if at all) on newly-created files or directories within the specified path. Only valid for directories.

Notes about posix1e ACL entry fields:

`default` the ACL entry is in the posix default ACL (will be copied to new files and directories) created within the directory where it is set. These are _NOT_ evaluated when determining access for the file on which they're set. If default is false then the entry applies to the posix access ACL, which is used to determine access to the directory, but is not inherited on new files / directories.

`tag` the type of principal to whom the ACL entry apples. USER and GROUP have conventional meanings USER_OBJ refers to the owning user of the file and is also denoted by "user" in conventional POSIX UGO permissions. GROUP_OBJ refers to the owning group of the file and is denoted by "group" in the same. OTHER refers to POSIX other, which applies to all users and groups who are not USER_OBJ or GROUP_OBJ. MASK sets maximum permissions granted to all USER and GROUP entries. A valid POSIX1 ACL entry contains precisely one USER_OBJ, GROUP_OBJ, OTHER, and MASK entry for the default and access list.

`id` refers to the numeric user id or group id associatiated with USER or GROUP entries.

`who` a user or group name may be specified in lieu of numeric ID for USER or GROUP entries

`perms` - object containing posix permissions.

This method is a job.

## Required Roles

- `FILESYSTEM_ATTRS_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filesystem_acl

#### filesystem_acl

- Schema name: `filesystem_acl`
- Type: object

FilesystemSetaclArgs parameters.
- No Additional Properties
##### path (required)

- Schema name: `Path`
- Type: string

Absolute filesystem path to set ACL on.
- Must be at least `1` characters long

##### dacl (required)

- Schema name: `Dacl`

Array of Access Control Entries to apply to the filesystem object.
###### Any of

####### Option 1

- Type: array of object
- No Additional Items

######## Each item of this array must be:

######## NFS4ACE

- Schema name: `NFS4ACE`
- Type: object
- No Additional Properties
######### tag (required)

- Schema name: `Tag`
- Type: enum (of string)

Subject type for this ACE. `owner@`: File/directory owner `group@`: File/directory primary group `everyone@`: All users `USER`: Specific user account `GROUP`: Specific group

######### type (required)

- Schema name: `Type`
- Type: enum (of string)

Access control type. `ALLOW`: Grant the specified permissions `DENY`: Explicitly deny the specified permissions

######### perms (required)

- Schema name: `Perms`

Permissions granted or denied by this ACE.
########## Any of

########### NFS4ACE_AdvancedPerms

- Schema name: `NFS4ACE_AdvancedPerms`
- Type: object
- No Additional Properties
############ READ_DATA

- Schema name: `Read Data`
- Type: boolean
- Default: false

Permission to read file data or list directory contents.

############ WRITE_DATA

- Schema name: `Write Data`
- Type: boolean
- Default: false

Permission to write file data or create files in directory.

############ APPEND_DATA

- Schema name: `Append Data`
- Type: boolean
- Default: false

Permission to append data to files or create subdirectories.

############ READ_NAMED_ATTRS

- Schema name: `Read Named Attrs`
- Type: boolean
- Default: false

Permission to read named attributes (extended attributes).

############ WRITE_NAMED_ATTRS

- Schema name: `Write Named Attrs`
- Type: boolean
- Default: false

Permission to write named attributes (extended attributes).

############ EXECUTE

- Schema name: `Execute`
- Type: boolean
- Default: false

Permission to execute files or traverse directories.

############ DELETE

- Schema name: `Delete`
- Type: boolean
- Default: false

Permission to delete the file or directory.

############ DELETE_CHILD

- Schema name: `Delete Child`
- Type: boolean
- Default: false

Permission to delete child files within a directory.

############ READ_ATTRIBUTES

- Schema name: `Read Attributes`
- Type: boolean
- Default: false

Permission to read basic file attributes (size, timestamps, etc.).

############ WRITE_ATTRIBUTES

- Schema name: `Write Attributes`
- Type: boolean
- Default: false

Permission to write basic file attributes.

############ READ_ACL

- Schema name: `Read Acl`
- Type: boolean
- Default: false

Permission to read the Access Control List.

############ WRITE_ACL

- Schema name: `Write Acl`
- Type: boolean
- Default: false

Permission to modify the Access Control List.

############ WRITE_OWNER

- Schema name: `Write Owner`
- Type: boolean
- Default: false

Permission to change the file owner.

############ SYNCHRONIZE

- Schema name: `Synchronize`
- Type: boolean
- Default: false

Permission to use the file/directory as a synchronization primitive.

########### NFS4ACE_BasicPerms

- Schema name: `NFS4ACE_BasicPerms`
- Type: object
- No Additional Properties
############ BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic permission level for NFS4 ACE. `FULL_CONTROL`: Full read, write, execute, and administrative permissions `MODIFY`: Read, write, and execute permissions `READ`: Read-only permissions `TRAVERSE`: Execute/traverse permissions only

######### flags (required)

- Schema name: `Flags`

Inheritance and other behavioral flags for this ACE.
########## Any of

########### NFS4ACE_AdvancedFlags

- Schema name: `NFS4ACE_AdvancedFlags`
- Type: object
- No Additional Properties
############ FILE_INHERIT

- Schema name: `File Inherit`
- Type: boolean
- Default: false

Apply this ACE to files within directories.

############ DIRECTORY_INHERIT

- Schema name: `Directory Inherit`
- Type: boolean
- Default: false

Apply this ACE to subdirectories within directories.

############ NO_PROPAGATE_INHERIT

- Schema name: `No Propagate Inherit`
- Type: boolean
- Default: false

Do not propagate inheritance beyond immediate children.

############ INHERIT_ONLY

- Schema name: `Inherit Only`
- Type: boolean
- Default: false

This ACE only affects inheritance, not the object itself.

############ INHERITED

- Schema name: `Inherited`
- Type: boolean
- Default: false

This ACE was inherited from a parent directory.

########### NFS4ACE_BasicFlags

- Schema name: `NFS4ACE_BasicFlags`
- Type: object
- No Additional Properties
############ BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic inheritance behavior for NFS4 ACE. `INHERIT`: Apply to child files and directories `NOINHERIT`: Do not apply to child objects

######### id

- Schema name: `Id`
- Default: null

UID or GID when `tag` is "USER" or "GROUP". `null` for special entries.
########## Any of

########### Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

########### Option 2

- Type: null

######### who

- Schema name: `Who`
- Default: null

Username or group name when `tag` is "USER" or "GROUP". `null` for special entries.
########## Any of

########### Option 1

- Type: string

########### Option 2

- Type: string
- Must be at least `1` characters long

########### Option 3

- Type: null

####### Option 2

- Schema name: `NFS4ACE_AdvancedPerms`
- Type: object
- No Additional Properties
######## READ_DATA

- Schema name: `Read Data`
- Type: boolean
- Default: false

Permission to read file data or list directory contents.

######## WRITE_DATA

- Schema name: `Write Data`
- Type: boolean
- Default: false

Permission to write file data or create files in directory.

######## APPEND_DATA

- Schema name: `Append Data`
- Type: boolean
- Default: false

Permission to append data to files or create subdirectories.

######## READ_NAMED_ATTRS

- Schema name: `Read Named Attrs`
- Type: boolean
- Default: false

Permission to read named attributes (extended attributes).

######## WRITE_NAMED_ATTRS

- Schema name: `Write Named Attrs`
- Type: boolean
- Default: false

Permission to write named attributes (extended attributes).

######## EXECUTE

- Schema name: `Execute`
- Type: boolean
- Default: false

Permission to execute files or traverse directories.

######## DELETE

- Schema name: `Delete`
- Type: boolean
- Default: false

Permission to delete the file or directory.

######## DELETE_CHILD

- Schema name: `Delete Child`
- Type: boolean
- Default: false

Permission to delete child files within a directory.

######## READ_ATTRIBUTES

- Schema name: `Read Attributes`
- Type: boolean
- Default: false

Permission to read basic file attributes (size, timestamps, etc.).

######## WRITE_ATTRIBUTES

- Schema name: `Write Attributes`
- Type: boolean
- Default: false

Permission to write basic file attributes.

######## READ_ACL

- Schema name: `Read Acl`
- Type: boolean
- Default: false

Permission to read the Access Control List.

######## WRITE_ACL

- Schema name: `Write Acl`
- Type: boolean
- Default: false

Permission to modify the Access Control List.

######## WRITE_OWNER

- Schema name: `Write Owner`
- Type: boolean
- Default: false

Permission to change the file owner.

######## SYNCHRONIZE

- Schema name: `Synchronize`
- Type: boolean
- Default: false

Permission to use the file/directory as a synchronization primitive.

####### NFS4ACE_AdvancedPerms

- Schema name: `NFS4ACE_BasicPerms`
- Type: object
- No Additional Properties
######## BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic permission level for NFS4 ACE. `FULL_CONTROL`: Full read, write, execute, and administrative permissions `MODIFY`: Read, write, and execute permissions `READ`: Read-only permissions `TRAVERSE`: Execute/traverse permissions only

####### NFS4ACE_BasicPerms

- Schema name: `NFS4ACE_AdvancedFlags`
- Type: object
- No Additional Properties
######## FILE_INHERIT

- Schema name: `File Inherit`
- Type: boolean
- Default: false

Apply this ACE to files within directories.

######## DIRECTORY_INHERIT

- Schema name: `Directory Inherit`
- Type: boolean
- Default: false

Apply this ACE to subdirectories within directories.

######## NO_PROPAGATE_INHERIT

- Schema name: `No Propagate Inherit`
- Type: boolean
- Default: false

Do not propagate inheritance beyond immediate children.

######## INHERIT_ONLY

- Schema name: `Inherit Only`
- Type: boolean
- Default: false

This ACE only affects inheritance, not the object itself.

######## INHERITED

- Schema name: `Inherited`
- Type: boolean
- Default: false

This ACE was inherited from a parent directory.

####### NFS4ACE_AdvancedFlags

- Schema name: `NFS4ACE_BasicFlags`
- Type: object
- No Additional Properties
######## BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic inheritance behavior for NFS4 ACE. `INHERIT`: Apply to child files and directories `NOINHERIT`: Do not apply to child objects

####### NFS4ACE_BasicFlags

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

####### Option 1

- Type: null

####### Option 2

- Type: string

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

####### Option 3

- Type: array of object
- No Additional Items

######## Each item of this array must be:

######## POSIXACE

- Schema name: `POSIXACE`
- Type: object
- No Additional Properties
######### tag (required)

- Schema name: `Tag`
- Type: enum (of string)

Subject type for this POSIX ACE. `USER_OBJ`: File/directory owner `GROUP_OBJ`: File/directory primary group `OTHER`: All other users `MASK`: Maximum permissions for named users and groups `USER`: Specific user account `GROUP`: Specific group

######### perms (required)

- Schema name: `POSIXACE_Perms`
- Type: object

Read, write, and execute permissions for this ACE.
- No Additional Properties
########## READ (required)

- Schema name: `Read`
- Type: boolean

Permission to read file contents or list directory contents.

########## WRITE (required)

- Schema name: `Write`
- Type: boolean

Permission to write file contents or create/delete files in directory.

########## EXECUTE (required)

- Schema name: `Execute`
- Type: boolean

Permission to execute files or traverse directories.

######### default (required)

- Schema name: `Default`
- Type: boolean

Whether this is a default ACE that applies to newly created child objects.

######### id

- Schema name: `Id`
- Default: null

Numeric user or group ID when tag is `USER` or `GROUP`. `null` for object entries.
########## Any of

########### Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

########### Option 2

- Type: null

######### who

- Schema name: `Who`
- Default: null

Username or group name when tag is `USER` or `GROUP`. `null` for object entries.
########## Any of

########### Option 1

- Type: string

########### Option 2

- Type: string
- Must be at least `1` characters long

########### Option 3

- Type: null

####### Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

####### Option 2

- Type: null

####### Option 1

- Type: string

####### Option 2

- Type: string
- Must be at least `1` characters long

####### Option 3

- Type: null

##### options

- Schema name: `FilesystemSetAclOptions`
- Type: object
- Default:
```json
{
  "stripacl": false,
  "recursive": false,
  "traverse": false,
  "canonicalize": true,
  "validate_effective_acl": true
}
```

Configuration options for ACL setting behavior.
- No Additional Properties
###### stripacl

- Schema name: `Stripacl`
- Type: boolean
- Default: false

Whether to remove the ACL entirely and revert to basic POSIX permissions.

###### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to apply ACL changes recursively to all child files and directories.

###### traverse

- Schema name: `Traverse`
- Type: boolean
- Default: false

Whether to traverse filesystem boundaries during recursive operations.

###### canonicalize

- Schema name: `Canonicalize`
- Type: boolean
- Default: true

Whether to reorder ACL entries in Windows canonical order.

###### validate_effective_acl

- Schema name: `Validate Effective Acl`
- Type: boolean
- Default: true

Whether to validate that the users/groups granted access in the ACL can actually access the path or parent path.

##### nfs41_flags

- Schema name: `NFS4ACL_Flags`
- Type: object
- Default:
```json
{
  "autoinherit": false,
  "protected": false,
  "defaulted": false
}
```

NFS4 ACL flags for inheritance and protection behavior.
- No Additional Properties
###### autoinherit

- Schema name: `Autoinherit`
- Type: boolean
- Default: false

Whether inheritance is automatically applied from parent directories.

###### protected

- Schema name: `Protected`
- Type: boolean
- Default: false

Whether the ACL is protected from inheritance modifications.

###### defaulted

- Schema name: `Defaulted`
- Type: boolean
- Default: false

Whether this ACL was created by default rules rather than explicit configuration.

##### uid

- Schema name: `Uid`
- Default: -1

Numeric user ID to set as owner or `null` to preserve existing.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

####### Option 2

- Type: null

##### user

- Schema name: `User`
- Default: null

Username to set as owner or `null` to preserve existing.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### gid

- Schema name: `Gid`
- Default: -1

Numeric group ID to set as group or `null` to preserve existing.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

####### Option 2

- Type: null

##### group

- Schema name: `Group`
- Default: null

Group name to set as group or `null` to preserve existing.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### acltype

- Schema name: `Acltype`
- Default: null

ACL type to use or `null` to auto-detect from filesystem capabilities.
###### Any of

####### Option 1

- Type: enum (of string)

####### Option 2

- Type: null

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
