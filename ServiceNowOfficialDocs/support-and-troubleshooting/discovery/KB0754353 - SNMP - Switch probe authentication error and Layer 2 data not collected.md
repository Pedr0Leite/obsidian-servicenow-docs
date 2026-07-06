---
title: "SNMP - Switch probe authentication error and Layer 2 data not collected"
aliases:
  - KB0754353
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754353
kb_number: KB0754353
last_modified: 2025-06-23
---

## SNMP - Switch probe authentication error and Layer 2 data not collected

  

### Issue

SNMP - Switch probes fail with authentication errors on Cisco devices. However other probes are successful for the same devices. Alternatively, network switch and router patterns will run successfully, however, layer 2 information will not be collected for the device.

The following error message can be seen in the input returned, for probes:

<table style="height: 13px; width: 100%; border-collapse: collapse; background-color: #ecedbe; border-style: none;" border="0"><tbody><tr style="height: 13px;"><td style="width: 100%; height: 13px;">Target is blacklisted. No valid credential found for type [SNMPv3]</td></tr></tbody></table>

### Release

All currently supported releases.

### Cause

See following cisco discussions:

[https://community.cisco.com/t5/network-management/multiple-snmp-v3-command-to-type-at-one-time/m-p/1475610#M70892](https://community.cisco.com/t5/network-management/multiple-snmp-v3-command-to-type-at-one-time/m-p/1475610#M70892)

[https://community.cisco.com/t5/network-management/vlan-bridge-mib-and-snmpv3-contexts/td-p/1589698](https://community.cisco.com/t5/network-management/vlan-bridge-mib-and-snmpv3-contexts/td-p/1589698)

For SNMPv1 and SNMPv2c cisco uses community name indexing. This allow us to get VLAN specific information. In SNMPv3, contexts are used instead. Each VLAN will require the context to be passed so that the BRIDGE-MIB will return the requested information for the specified VLAN. Not all versions of IOS support contexts. Changes to the running config through CLI must be made in order to request context information for each VLAN. If the switch is not configured, discovery will not collect vlan spefic information via SNMPv3.

### Resolution

Per the Cisco document provided, configure the account to be able to request context information.

To configure the account, run the following command on the Cisco interface:

<table style="height: 13px; width: 100%; border-collapse: collapse; background-color: #ecedbe; border-style: none; border-color: #ffff0a;"><tbody><tr style="height: 13px;"><td style="width: 100%; height: 13px;">snmp-server group &lt;yourV3groupName&gt; v3 auth context vlan- match prefix</td></tr></tbody></table>

**Note:** the above should be done by the network team managing the device/credential and other commands may be required as well, therefore please review the Cisco documentation before running any commands. The command needs to be edited for the proper group name or updated to allow access to the user directly.
