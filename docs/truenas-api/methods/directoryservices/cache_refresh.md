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

This method refreshes the directory services cache for users and groups that is used as a backing for `user.query` and `group.query` methods. The first cache fill in an Active Directory domain may take a significant amount of time to complete and so it is performed as within a job. The most likely situation in which a user may desire to refresh the directory services cache is after new users or groups to a remote directory server with the intention to have said users or groups appear in the results of the aforementioned account-related methods.

A cache refresh is not required in order to use newly-added users and groups for in permissions and ACL related methods. Likewise, a cache refresh will not resolve issues with users being unable to authenticate to shares.

This method is a job.

## Required Roles

- `DIRECTORY_SERVICE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
