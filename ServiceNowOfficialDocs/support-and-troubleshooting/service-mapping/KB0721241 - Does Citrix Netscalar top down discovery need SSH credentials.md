---
title: "Does Citrix Netscalar top down discovery need SSH credentials?"
aliases:
  - KB0721241
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0721241
kb_number: KB0721241
last_modified: 2024-04-07
---

## Does Citrix Netscalar top down discovery need SSH credentials?

  

### Issue

Generally, the discovery of network devices including Citrix Netscalar is done via SNMP but, during the top down discovery or during the creation of a business service map, there would be an additional need for SSH credentials as well for accessing the netscalar device.

### Release

All Version.

### Resolution

The Citrix Netscaler pattern needs ssh access to the LB and to run the following commands to create connections:  

1.  show vserver | grep $name 
2.  show cs policy 
3.  show cs vserver $name 
4.  show cs action 

Connections to server farm: 

-   show lb vserver $name 

Regarding the permissions, the "show" command is a netscaler command.   
The user would need to be able to login to the target via SSH and run the commands above.
