---
title: "Disocovery - separate decvice IP's updating same switch device after every discovery."
aliases:
  - KB0723715
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723715
kb_number: KB0723715
last_modified: 2024-04-07
---

## Disocovery - separate decvice IP's updating same switch device after every discovery.

  

### Issue

On executing discovery for individual switch devices, it is updating same switch device for multiple separate devices. The issue is about the invalid classification of the devices. When discovery tries to discover a device, it updates it based on the name which is getting updated as same for all devices due to OOTB regex expression. This article will demonstrate on the investigations and probable use cases, hence in future, if discovery updates the same for multiple IP's then this can be one of the cause and worth trying to fix.

### Release

-   Connect to ServiceNow instance.
-   Initiate quick discovery or scheduled discovery for windows devices for 2 or more switch devices one by one.
-   Discovery identifies the device with Identification Criteria = 'name' 
-   Wait for discovery to complete the discovery. 
-   One discovery completes, it updates the same device again and again for different IP's 

### Cause

The problem is identified with the naming convention of the devices. The devices are named as **_SLC-IDF1.2-SW01,_** **_SLC-IDF1.1-SW01_** and so on. There is OOTB property called [glide.discovery.fqdn.regex](https://docs.servicenow.com/csh?topicname=r_DiscoveryProperties.html&version=latest "glide.discovery.fqdn.regex") which parse the name to pick the first name separated by dots as the hostname and the rest of the names as the domain name. Thus, in this case, the name will always be **_SLC-IDF1_**. As the identification is happening based on name, it updates the same device again and again for all the IP's.

### Resolution

Changing the naming convention of the device helps to resolve the issue. Also _**Regular Expression: ^(\[^.\]+)\\.((?:\[^.\]+\\.)+\[^.\]+)$**_ can be modified but this change applies to all the devices thus it is recommended to avoid changing the regex.

#
