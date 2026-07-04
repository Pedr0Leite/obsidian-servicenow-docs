---
title: "KB Service Portal Review of User Criteria: Change to kb_view_customer status"
aliases:
  - KB0827377
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0827377
kb_number: KB0827377
last_modified: 2024-04-08
---

## Text

### Audience

Instance Administrators

  

### Overview

ServiceNow has proactively disabled the public UI page by setting the active property of the **kb\_view\_customer** record to **false** where we have observed increased KB article transaction volume.

  

### Details

To revert the change, log in as an administrator and follow these steps:

1.  Access the sys\_public table and look for the _kb\_view\_customer_ record:  
      
    Example:  
    -   https://**<instance-name>.**service-now.com/sys\_public\_list.do?sysparm\_query=page%3Dkb\_view\_customer (Commercial)  
          
        
    -   https://**<instance-name>.**servicenowservices.com/sys\_public\_list.do?sysparm\_query=page%3Dkb\_view\_customer (GCC)
2.  Set the active value to **True**

  

### Additional information

For additional info, please review the contents of [KB0824691](/kb_view.do?sysparm_article=KB0824691).
