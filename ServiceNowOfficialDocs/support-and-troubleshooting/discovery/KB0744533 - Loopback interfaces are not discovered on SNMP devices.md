---
title: "Loopback interfaces are not discovered on SNMP devices"
aliases:
  - KB0744533
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0744533
kb_number: KB0744533
last_modified: 2024-04-07
---

## Loopback interfaces are not discovered on SNMP devices

  

### Issue

# Overview

  
Loopback interfaces are intentionally not recorded for SNMP devices out of box due to the **SNMPIdentityInfoParser** Script Include.

![](/sys_attachment.do?sys_id=21ba6ca6db42b450e515c223059619ce)

The code states that if an **SNMP - Identity** probe payload returns a device interface with an **ifType** value of **24,** then it will not be recorded.

# Example

Below is an example of an **SNMP - Identity** probe input payload for SNMP device **10.0.0.1**:

This interface returned with an **ifType** value of 24, so it will not be recorded. Notice the identifying **ifIndex** value in this case is set to 8, but will vary by device.       
<ifEntry instance=".8">  
<ifIndex type="SnmpInt32">**8**</ifIndex>  
<ifDescr type="SnmpOctetString">Loopback0</ifDescr>  
<ifType type="SnmpInt32">**24**</ifType>  
<ifPhysAddress type="SnmpOctetString"/>  
<ifAdminStatus type="SnmpInt32">1</ifAdminStatus>  
<ifOperStatus type="SnmpInt32">1</ifOperStatus>

Using the **ifIndex** value, look further down the payload for the **ipAdEntIfIndex** with the same value. This will be the IP address that is not recorded.  
<ipAddrEntry instance=".10.0.0.1">  
<ipAdEntAddr type="SnmpIPAddress">10.0.0.1</ipAdEntAddr>  
<ipAdEntIfIndex type="SnmpInt32">**8**</ipAdEntIfIndex>   
<ipAdEntNetMask type="SnmpIPAddress">255.255.255.255</ipAdEntNetMask>  
</ipAddrEntry>
