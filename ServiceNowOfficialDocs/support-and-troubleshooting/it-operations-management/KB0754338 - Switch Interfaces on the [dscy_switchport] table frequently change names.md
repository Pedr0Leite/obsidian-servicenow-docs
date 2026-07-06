---
title: "Switch Interfaces on the [dscy_switchport] table frequently change names"
aliases:
  - KB0754338
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754338
kb_number: KB0754338
last_modified: 2025-04-07
---

## Switch Interfaces on the \[dscy\_switchport\] table frequently change names

  

### Issue

On the \[dscy\_switchport\] table, the record names are frequently updated during discovery although they are expected to remain the same. The sys\_id and mac addresses do not change. This can be verified by enabling auditing on the \[dscy\_switchport.name\] field.

### Cause

From [Cisco](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst6500/ios/12-2SX/configuration/guide/book/ifindx.html "Cisco"):

> The SNMP ifIndex persistence feature provides an interface index (ifIndex) value that is retained and used when the switch reboots. The ifIndex value is a unique identifying number associated with a physical or logical interface.  
>   
> There is no requirement in the relevant RFCs that the correspondence between particular ifIndex values and their interfaces be maintained when the switch reboots, but many applications (for example, device inventory, billing, and fault detection) require maintenance of this correspondence.  
>   
> You can poll the switch at regular intervals to correlate the interfaces to the ifIndexes, but it is not practical to poll constantly. The SNMP ifIndex persistence feature provides permanent ifIndex values, which eliminates the need to poll interfaces.  
>   
> The following definitions are based on RFC 2233, "The Interfaces Group MIB using SMIv2." The following terms are values in the Interfaces MIB (IF-MIB):  
>   
> • **ifIndex** — A unique number (greater than zero) that identifies each interface for SNMP identification of that interface.  
>   
> • ifName — The text-based name of the interface, for example, "ethernet 3/1."  
>   
> • ifDescr — A description of the interface. Recommended information for this description includes the name of the manufacturer, the product name, and the version of the interface hardware and software.

### Resolution

The customer's Network/Infrastructure team should enable ifIndex persistence between reboots.
