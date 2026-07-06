---
title: "When discovery is performed for a router using its management IP address, the CI's IP address field gets populated with the private IP of the host instead of the management IP."
aliases:
  - KB0755771
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755771
kb_number: KB0755771
last_modified: 2026-07-04
---

## When discovery is performed for a router using its management IP address, the CI's IP address field gets populated with the private IP of the host instead of the management IP.

  

### Issue

 

When discovery is performed for a router using its management IP address, the CI's IP address field gets populated with the private IP of the host instead of the management IP

### Release

ALL

### Cause

The host's Private IP is updated at the end of Discovery, and we can verify it in the CI's XML data. If we are running a discovery against an IP  (Management IP), in the CI's XML, we would see the IP (Private IP) appearing. The script is doing this, including "IPAddressFixup". It has been present out of the box.

Once the pattern sets the IP Address to the Management IP, a script include 'IPAddressFixup' is executed to replace the IP with one of the NIC IP addresses. This script include is actually controlled by the two properties.

1.  glide.discovery.enforce\_ip\_sync (OOB value is 'true')
2.  glide.discovery.exclude\_ip\_sync\_classes(OOB value is 'cmdb\_ci\_lb')

This property values can be comma separated. If we don't want to replace the Management IP, we can add cmdb\_ci\_netgear to the values list in this property. So that this script include will not map NIC IP to IP Address field. But again, this script include code has bug where it is not ignoring the classes which are added to the property. If condition gets failed here. Result of if (heirarchy.contains(exclude\_ip\_sync\_classes\[i\])) is 'undefined' and syncClass = true  
  
OOB code in script include: 'IPAddressFixup'  
for (var i = 0; i < exclude\_ip\_sync\_classes.length && syncClass ; i++)  
if (heirarchy.contains(exclude\_ip\_sync\_classes\[i\]))  
syncClass = false;

### Resolution

-   Added cmdb\_ci\_netgear to the Property 'glide.discovery.exclude\_ip\_sync\_classes'

![](sys_attachment.do?sys_id=411dc5fa97fdcb105ad8f6e11153af5e)

-   Fixed the code issue in the script include "IPAdressFixup"

**Modified one**:  
for (var i = 0; i < exclude\_ip\_sync\_classes.length && syncClass ; i++)  
{  
**gs.info("SDBUG " +exclude\_ip\_sync\_classes\[i\]);**  
if (heirarchy.contains(exclude\_ip\_sync\_classes\[i\]))  
syncClass = false;  
}  
  
![](sys_attachment.do?sys_id=011dc5fa97fdcb105ad8f6e11153af2e)  
  
  
  
With the above two changes, executed discovery and Management IP is not changed after the discovery.
