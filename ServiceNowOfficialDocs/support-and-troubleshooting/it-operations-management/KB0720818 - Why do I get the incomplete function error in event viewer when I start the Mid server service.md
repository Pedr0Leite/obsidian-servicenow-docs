---
title: "Why do I get the \"incomplete function\" error in event viewer when I start the Mid server service?"
aliases:
  - KB0720818
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720818
kb_number: KB0720818
last_modified: 2024-04-07
---

## Why do I get the "incomplete function" error in event viewer when I start the Mid server service?

  

### Issue

-   Why do I get the "incomplete function" error in the event viewer when I start the Mid server service?

### Resolution

-   The logon account associated with the mid server service needs to be able to access the JRE associated with the service. This file is present as part of the agent folder. Please ensure the account provided as a logon account for the service has permission to access the folder.  
      
    
-   On the mid server host machine, please check the following:  
      
    -   In the command prompt, type in services. Right-click on the service and select properties.
    -   Click the logon tab, note the account provided for logon.
    -   Navigate to the agent folder for the Mid server, right-click, and select properties.
    -   In the Security tab, ensure the group that the logon account is part of is listed with access to the agent folder.
