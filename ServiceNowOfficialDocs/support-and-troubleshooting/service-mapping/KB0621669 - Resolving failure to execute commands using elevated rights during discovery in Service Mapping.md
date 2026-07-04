---
title: "Resolving failure to execute commands using elevated rights during discovery in Service Mapping"
aliases:
  - KB0621669
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621669
kb_number: KB0621669
last_modified: 2024-04-07
---

## Resolving failure to execute commands using elevated rights during discovery in Service Mapping

  

### Issue

Resolving failure to execute commands using elevated rights during discovery in Service Mapping 

Symptoms

* * *

  

-   The business service map displays the warning icon (![](sys_attachment.do?sys_id=9d49e0eedb02b450e515c223059619fd)) on top or instead of the configuration item.
-   The following error message displays for the configuration item: 
    
    Failed to execute command using sudo on host <host IP address>
    

Possible Cause

* * *

The user configured on the server is not allowed to run commands with elevated rights, for example, sudo.   

  
Resolution

* * *

Make sure that the user is configured correctly on the target server to discover the user with commands requiring a privileged user. See [Service Mapping commands requiring a privileged user](https://docs.servicenow.com/csh?topicname=r_CommandsnCredentials.html&version=latest "Service Mapping commands requiring a privileged user"). 

Alternatively, if you use SSH key credentials, create a new credential record for them under **Service Mapping > Administration > Credentials**.
