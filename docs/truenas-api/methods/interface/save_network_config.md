---
title: interface.save_network_config
kind: method
source_rst: _sources/api_methods_interface.save_network_config.rst.txt
source_html: api_methods_interface.save_network_config.html
required_roles:
  - NETWORK_INTERFACE_WRITE
---

# interface.save_network_config

## Summary

Saves network configuration settings to prevent network isolation during interface changes.

This method provides a path for remediation when interface modifications would remove network connectivity. It accepts a configuration object containing network settings that will be validated and applied to the global network configuration.

This makes 2 assumptions: 1. `interface.create`/`update`/`delete` must have been called before calling this method. 2. This method must be called before `interface.commit` is called.

This method exists for the predominant scenario for new users: 1. Fresh install SCALE. 2. All interfaces start DHCPv4 (v6 is ignored for now). 3. One of the interfaces receives an IP address. 4. Along with the IP, the kernel receives a default route (by design, of course). 5. User goes to configure this interface as having a static IP address. 6. As we go through and "commit" the changes, we remove the default route because it exists in the kernel FIB but doesn't exist in the database. 7. IF the user is connecting via layer3, then they will lose all access to the TrueNAS and never be able to finalize the changes to the network because we ripped out the default route which is how they were communicating to begin with.

In the above scenario, we're going to try and prevent this by doing the following: 1. Fresh install SCALE. 2. All interfaces start DHCPv4. 3. Default route is received. 4. User configures an interface. 5. When user pushes "Test Changes" (`interface.commit`), webUI will call `interface.network_config_to_be_removed` BEFORE `interface.commit`. 6. If `interface.network_config_to_be_removed` returns any fields, then webUI will open a new modal dialog that gives the end-user ample warning describing the situation. Furthermore, the modal will allow the user to input a default gateway and nameservers. 7. If user gives gateway, webUI will call this method providing the info and we'll validate accordingly. 8. OR if user doesn't give gateway, they will need to "confirm" this is desired. 9. The network configuration provided (gateway and nameservers) will be stored in the same in-memory cache that we use for storing the interface changes and will be rolled back accordingly in this plugin just like everything else.

There are a few other scenarios where this is beneficial, but the one listed above is seen most often by end-users/support team.

## Required Roles

- `NETWORK_INTERFACE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: config

#### config

- Schema name: `config`
- Type: object

InterfaceSaveNetworkConfigArgs parameters.
- No Additional Properties
##### ipv4gateway (required)

- Schema name: `Ipv4Gateway`
- Type: string

IPv4 address of the default gateway to save.

##### nameserver1

- Schema name: `Nameserver1`

Primary DNS server.
###### Any of

####### Option 1

- Type: const

####### Option 2

- Type: string

##### nameserver2

- Schema name: `Nameserver2`

Secondary DNS server.
###### Any of

####### Option 1

- Type: const

####### Option 2

- Type: string

##### nameserver3

- Schema name: `Nameserver3`

Tertiary DNS server.
###### Any of

####### Option 1

- Type: const

####### Option 2

- Type: string

### Return value

- Schema name: `Result`
- Type: null

No return value for successful save default route operation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
