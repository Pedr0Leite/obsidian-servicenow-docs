---
title: "PostgreSQL Pattern detecting the default running instance for 'hostname"
aliases:
  - KB0781629
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781629
kb_number: KB0781629
last_modified: 2025-01-16
---

## PostgreSQL Pattern detecting the default running instance for 'hostname'

  

### Issue

During a discovery it creates and updates CMDB records when it detects a running instance at the PostgreSQL level.

Per our docs it collects the name PostgreSQL instance@_hostname._ However, as by default we see in the related tree of several CIs with 'PostgreSQL' with in the cmdb\_ci\_db\_postgresql\_instance table.

### Cause

Out of box we see this:

Step 19. **Set label**  
  
Value: **$instance**   
Name: **$name**

This is the Output example:  
**'PostgreSQL'**

In the related tree of the CI we see there are several PostgreSQL, listed in the cmdb\_ci\_db\_postgresql\_instance.

### Resolution

Do the following if you prefer to have the PostgreSQL pattern to populate the PostgreSQL@instance name.

Step 19. **Set label**  
_added the following:_  
Value: **$instance + "@" + $computer\_system.primaryHostname**  
Name: **$name**

This is the Output example:  
'**PostgreSQL@mikecamba**'
