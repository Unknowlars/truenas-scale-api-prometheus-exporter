---
title: zfs.resource.query
kind: method
source_rst: _sources/api_methods_zfs.resource.query.rst.txt
source_html: api_methods_zfs.resource.query.html
required_roles:
  - ZFS_RESOURCE_READ
---

# zfs.resource.query

## Summary

Query ZFS resources (datasets and volumes) with flexible filtering options.

This method provides a high-performance interface for retrieving information about ZFS resources, including their properties, hierarchical relationships, and metadata. The query can be customized to retrieve specific resources, properties, and control the output format.

Raises: ValidationError: If: - Snapshot paths are provided (snapshots not currently supported) - Overlapping paths are provided with get_children=True - Requested paths don't exist (errno.ENOENT)

Examples: # Query all resources with default properties query()

# Query specific resources with all properties query({"paths": ["tank/documents", "tank/media"]})

# Query with specific properties and children query({ "paths": ["tank"], "properties": ["mounted", "compression", "used"], "get_children": True })

# Get hierarchical view of resources query({"paths": ["tank"], "nest_results": True, "get_children": True})

## Required Roles

- `ZFS_RESOURCE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`
- Type: object
- Default:
```json
{
  "paths": [],
  "properties": [],
  "get_user_properties": false,
  "get_source": true,
  "nest_results": false,
  "get_children": false
}
```

Query parameters for retrieving ZFS resource information.
- No Additional Properties
##### paths

- Schema name: `Paths`
- Type: array of string
- Default: []

A list of zfs filesystem or volume paths to be queried. In almost all scenarios, you should provide a path of what you want to query. By providing path(s) here, it allows the API to apply optimizations so that the requested information is retrieved as efficiently and quickly as possible. Example 1: {"paths": ["tank/foo"]} will query the relevant information for this resource only. Example 2: {"paths": ["tank/foo", "dozer/test"]} will query the relevant information for these resources only. NOTE: paths must be non-overlapping if `get_children` is True. (i.e. this won't work and will raise a validation error) { "paths": ["tank/foo1", "tank/foo1/foo2"], "get_children": True }
- All items must be unique
- No Additional Items

###### Each item of this array must be:

- Type: string

##### properties

- Schema name: `Properties`
- Default: []

A list of zfs properties to be retrieved. Defaults to an empty list which will return a default set of zfs properties. Setting this to None will retrieve no zfs properties.
###### Any of

####### Option 1

- Type: array of string
- No Additional Items

######## Each item of this array must be:

- Type: string

####### Option 2

- Type: null

##### get_user_properties

- Schema name: `Get User Properties`
- Type: boolean
- Default: false

Retrieve user properties for zfs resource(s).

##### get_source

- Schema name: `Get Source`
- Type: boolean
- Default: true

Hidden field to retrieve source information for a zfs property. NOTE: This should only ever be toggled by internal consumers and you should know what you're doing by toggling this to False.

##### nest_results

- Schema name: `Nest Results`
- Type: boolean
- Default: false

Return a nested object that associates all children to their respective parents in the filesystem. By default, each zfs resource is returned as a separate item in the array and is not associated to its parent.

##### get_children

- Schema name: `Get Children`
- Type: boolean
- Default: false

Retrieve children information for the zfs resource.

### Return value

- Schema name: `Result`
- Type: array of object
- No Additional Items

#### Each item of this array must be:

#### ZFSResourceEntry

- Schema name: `ZFSResourceEntry`
- Type: object
- No Additional Properties
##### createtxg (required)

- Schema name: `Createtxg`
- Type: integer

Transaction group when resource was created.

##### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for the resource.

##### name (required)

- Schema name: `Name`
- Type: string

The name of the zfs resource.

##### pool (required)

- Schema name: `Pool`
- Type: string

The name of the zpool that the zfs resouce is associated to.

##### properties (required)

- Schema name: `ZFSPropertiesEntry`
- Type: object

The zfs properties for the resource.
- No Additional Properties
###### aclinherit

- Schema name: `Aclinherit`
- Type: object

Controls how ACEs are inherited for new files/directories.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### SourceValue

- Schema name: `SourceValue`
- Type: object
- No Additional Properties
########## type (required)

- Schema name: `Type`
- Type: enum (of string)

The source type.

########## value (required)

- Schema name: `Value`

The source value.
########### Any of

############ Option 1

- Type: string

############ Option 2

- Type: null

######### Option 2

- Type: string

######### Option 1

- Type: null

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### aclmode

- Schema name: `Aclmode`
- Type: object

Determines how ACLs are modified during chmod operations.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### acltype

- Schema name: `Acltype`
- Type: object

Specifies type of ACL to use (off, nfsv4, posix).
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### atime

- Schema name: `Atime`
- Type: object

Controls whether access time is updated on file reads.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### canmount

- Schema name: `Canmount`
- Type: object

Controls whether filesystem can be mounted.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### casesensitivity

- Schema name: `Casesensitivity`
- Type: object

Determines filename matching algorithm sensitivity.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### defaultgroupobjquota

- Schema name: `Defaultgroupobjquota`
- Type: object

Default object quota for new groups.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### defaultgroupquota

- Schema name: `Defaultgroupquota`
- Type: object

Default space quota for new groups.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### defaultprojectobjquota

- Schema name: `Defaultprojectobjquota`
- Type: object

Default object quota for new projects.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### defaultprojectquota

- Schema name: `Defaultprojectquota`
- Type: object

Default space quota for new projects.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### defaultuserobjquota

- Schema name: `Defaultuserobjquota`
- Type: object

Default object quota for new users.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### defaultuserquota

- Schema name: `Defaultuserquota`
- Type: object

Default space quota for new users.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### devices

- Schema name: `Devices`
- Type: object

Controls whether device files can be opened.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### direct

- Schema name: `Direct`
- Type: object

Controls direct I/O behavior (standard or always).
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### dnodesize

- Schema name: `Dnodesize`
- Type: object

Controls dnode size for new objects.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### exec

- Schema name: `Exec`
- Type: object

Controls whether programs can be executed from filesystem.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### filesystem_count

- Schema name: `Filesystem Count`
- Type: object

(READ-ONLY): Count of child filesystems.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### filesystem_limit

- Schema name: `Filesystem Limit`
- Type: object

Maximum number of child filesystems allowed.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### longname

- Schema name: `Longname`
- Type: object

Controls support for long filenames.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### mounted

- Schema name: `Mounted`
- Type: object

(READ-ONLY): Property indicating if filesystem is mounted.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### mountpoint

- Schema name: `Mountpoint`
- Type: object

Controls mount point used for this filesystem.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### nbmand

- Schema name: `Nbmand`
- Type: object

Controls non-blocking mandatory locking behavior.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### normalization

- Schema name: `Normalization`
- Type: object

Unicode normalization property for filenames.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### overlay

- Schema name: `Overlay`
- Type: object

Controls overlay mount behavior.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### quota

- Schema name: `Quota`
- Type: object

Limits space consumed by dataset and descendants.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### recordsize

- Schema name: `Recordsize`
- Type: object

Maximum block size for files in this filesystem.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### refquota

- Schema name: `Refquota`
- Type: object

Limits space consumed by dataset itself (no descendants).
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### refreservation

- Schema name: `Refreservation`
- Type: object

Minimum space reserved for volume itself.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### relatime

- Schema name: `Relatime`
- Type: object

Controls relative access time updates.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### setuid

- Schema name: `Setuid`
- Type: object

Controls setuid/setgid bit respect on executable files.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### sharenfs

- Schema name: `Sharenfs`
- Type: object

Controls NFS sharing options for the filesystem.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### sharesmb

- Schema name: `Sharesmb`
- Type: object

Controls SMB/CIFS sharing options for the filesystem.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### snapdir

- Schema name: `Snapdir`
- Type: object

Controls snapshot directory visibility (hidden or visible).
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### special_small_blocks

- Schema name: `Special Small Blocks`
- Type: object

Size threshold for storing blocks on special vdevs.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### utf8only

- Schema name: `Utf8Only`
- Type: object

Controls whether only UTF-8 filenames are allowed.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### version

- Schema name: `Version`
- Type: object

(READ-ONLY): Filesystem version number.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### volmode

- Schema name: `Volmode`
- Type: object

Controls volume mode (default, geom, dev, none).
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### vscan

- Schema name: `Vscan`
- Type: object

Controls virus scanning behavior.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### xattr

- Schema name: `Xattr`
- Type: object

Controls extended attribute behavior (on, off, sa, dir).
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### zoned

- Schema name: `Zoned`
- Type: object

Controls whether filesystem is managed from a zone.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### available

- Schema name: `Available`
- Type: object

Amount of space available to dataset and its children.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### checksum

- Schema name: `Checksum`
- Type: object

Controls checksum algorithm used to verify data integrity.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### compression

- Schema name: `Compression`
- Type: object

Controls compression algorithm used for this dataset.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### compressratio

- Schema name: `Compressratio`
- Type: object

(READ-ONLY): Property showing achieved compression ratio.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### context

- Schema name: `Context`
- Type: object

SELinux security context for the dataset.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### copies

- Schema name: `Copies`
- Type: object

Controls number of copies of data stored (1, 2, or 3).
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### createtxg

- Schema name: `Createtxg`
- Type: object

(READ-ONLY): Transaction group when dataset was created.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### creation

- Schema name: `Creation`
- Type: object

(READ-ONLY): Timestamp when dataset was created.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### dedup

- Schema name: `Dedup`
- Type: object

Controls data deduplication for the dataset.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### defcontext

- Schema name: `Defcontext`
- Type: object

SELinux default security context for new files.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### encryption

- Schema name: `Encryption`
- Type: object

Controls encryption cipher suite for the dataset.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### encryptionroot

- Schema name: `Encryptionroot`
- Type: object

(READ-ONLY): Property showing encryption root dataset.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### fscontext

- Schema name: `Fscontext`
- Type: object

SELinux filesystem security context.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### guid

- Schema name: `Guid`
- Type: object

(READ-ONLY): Globally unique identifier for the dataset.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### keyformat

- Schema name: `Keyformat`
- Type: object

Encryption key format (raw, hex, or passphrase).
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### keylocation

- Schema name: `Keylocation`
- Type: object

Location where encryption key is stored.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### keystatus

- Schema name: `Keystatus`
- Type: object

(READ-ONLY): Encryption key status (available/unavailable).
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### logbias

- Schema name: `Logbias`
- Type: object

Controls ZIL write behavior (latency or throughput).
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### logicalreferenced

- Schema name: `Logicalreferenced`
- Type: object

(READ-ONLY): Logical space referenced by dataset.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### logicalused

- Schema name: `Logicalused`
- Type: object

(READ-ONLY): Logical space used by dataset and descendants.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### mlslabel

- Schema name: `Mlslabel`
- Type: object

Multi-level security label for the dataset.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### objsetid

- Schema name: `Objsetid`
- Type: object

(READ-ONLY): Object set identifier for the dataset.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### origin

- Schema name: `Origin`
- Type: object

(READ-ONLY): Snapshot this dataset was cloned from.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### pbkdf2iters

- Schema name: `Pbkdf2Iters`
- Type: object

Number of PBKDF2 iterations for key derivation.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### prefetch

- Schema name: `Prefetch`
- Type: object

Controls prefetch behavior (all, metadata, or none).
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### primarycache

- Schema name: `Primarycache`
- Type: object

Controls primary cache usage (all, metadata, or none).
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### readonly

- Schema name: `Readonly`
- Type: object

Controls whether dataset can be modified.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### receive_resume_token

- Schema name: `Receive Resume Token`
- Type: object

(READ-ONLY): Token for resuming interrupted zfs receive.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### redact_snaps

- Schema name: `Redact Snaps`
- Type: object

(READ-ONLY): List of redaction snapshots.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### redundant_metadata

- Schema name: `Redundant Metadata`
- Type: object

Controls redundant metadata storage (all or most).
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### refcompressratio

- Schema name: `Refcompressratio`
- Type: object

(READ-ONLY): Compression ratio for referenced data.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### referenced

- Schema name: `Referenced`
- Type: object

(READ-ONLY): Space referenced by this dataset.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### reservation

- Schema name: `Reservation`
- Type: object

Minimum space reserved for dataset and descendants.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### rootcontext

- Schema name: `Rootcontext`
- Type: object

SELinux root directory security context.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### secondarycache

- Schema name: `Secondarycache`
- Type: object

Controls secondary cache usage (all, metadata, or none).
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### snapdev

- Schema name: `Snapdev`
- Type: object

Controls snapshot device visibility (hidden or visible).
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### snapshot_count

- Schema name: `Snapshot Count`
- Type: object

(READ-ONLY): Count of snapshots in this dataset.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### snapshot_limit

- Schema name: `Snapshot Limit`
- Type: object

Maximum number of snapshots allowed.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### snapshots_changed

- Schema name: `Snapshots Changed`
- Type: object

(READ-ONLY): Property indicating snapshot changes.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### sync

- Schema name: `Sync`
- Type: object

Controls synchronous write behavior (standard, always, disabled).
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### type

- Schema name: `Type`

(READ-ONLY): Type of ZFS dataset (filesystem, volume, etc).
####### Any of

######## PropertyValue

- Schema name: `PropertyValue`
- Type: object
- No Additional Properties
######### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

######### source (required)

The source from where this property received its value.
########## Any of

########### Option 1

- Type: object

########### Option 2

- Type: null

######### value (required)

- Schema name: `Value`

The parsed raw value of the property.
########## Any of

########### Option 1

- Type: integer

########### Option 2

- Type: number

########### Option 3

- Type: string

########### Option 4

- Type: boolean

########### Option 5

- Type: null

######## Option 2

- Type: object

######## Option 1

- Type: null

######## Option 2

- Type: integer

######## Option 1

- Type: number

######## Option 2

- Type: string

######## Option 3

- Type: boolean

######## Option 4

- Type: null

######## Option 5

- Type: null

###### used

- Schema name: `Used`
- Type: object

(READ-ONLY): Space used by dataset and descendants.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### usedbychildren

- Schema name: `Usedbychildren`
- Type: object

(READ-ONLY): Space used by child datasets.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### usedbydataset

- Schema name: `Usedbydataset`
- Type: object

(READ-ONLY): Space used by this dataset itself.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### usedbyrefreservation

- Schema name: `Usedbyrefreservation`
- Type: object

(READ-ONLY): Space used by refreservation.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### usedbysnapshots

- Schema name: `Usedbysnapshots`
- Type: object

(READ-ONLY): Space used by snapshots.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### written

- Schema name: `Written`
- Type: object

(READ-ONLY): Space referenced since previous snapshot.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### volblocksize

- Schema name: `Volblocksize`
- Type: object

Block size for volume (typically 8K or 16K).
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### volsize

- Schema name: `Volsize`
- Type: object

Logical size of the volume.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

###### volthreading

- Schema name: `Volthreading`
- Type: object

Controls volume threading behavior.
- No Additional Properties
####### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

####### source (required)

The source from where this property received its value.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### value (required)

- Schema name: `Value`

The parsed raw value of the property.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: number

######### Option 3

- Type: string

######### Option 4

- Type: boolean

######### Option 5

- Type: null

##### type (required)

- Schema name: `Type`
- Type: enum (of string)

The type of ZFS resource.

##### user_properties (required)

- Schema name: `User Properties`

Custom metadata properties with colon-separated names (max 256 chars).
###### Any of

####### Option 1

- Type: object
######## Additional Properties

Each additional property must conform to the following schema
- Type: string

####### Option 2

- Type: null

##### children (required)

- Schema name: `Children`

The children of this zfs resource.
###### Any of

####### Option 1

- Type: array
- No Additional Items

######## Each item of this array must be:

- Type: object

####### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
