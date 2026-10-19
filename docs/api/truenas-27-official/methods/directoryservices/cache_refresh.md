---
title: directoryservices.cache_refresh
kind: method
source_rst: _sources/api_methods_directoryservices.cache_refresh.rst.txt
source_html: api_methods_directoryservices.cache_refresh.html
required_roles:
  - DIRECTORY_SERVICE_WRITE
---

# directoryservices.cache_refresh

## Summary

This method refreshes the directory services cache for users and groups that is used as a backing for [user.query](../user/query.md) and [group.query](../group/query.md) methods. The first cache fill in an Active Directory domain may take a significant amount of time to complete and so it is performed within a job. The most likely situation in which a user may desire to refresh the directory services cache is after new users or groups are added to a remote directory server with the intention to have said users or groups appear in the results of the aforementioned account-related methods.

A cache refresh is not required in order to use newly-added users and groups in permissions and ACL related methods. Likewise, a cache refresh will not resolve issues with users being unable to authenticate to shares.

This method is a job.

## Required Roles

- `DIRECTORY_SERVICE_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
