---
title: "Event Management Dashboard \"Prioritize by\" option."
aliases:
  - KB0758066
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758066
kb_number: KB0758066
last_modified: 2024-04-07
---

## Event Management Dashboard "Prioritize by" option.

  

### Issue

-   Event Management Dashboard does not show t"Prioritize by" option along with the drop-down to select the alert shorting.
-   Go to Event management-> select Dashboard.

                  ![](sys_attachment.do?sys_id=b52a84bcdb4cf0d022e0fb24399619bc)

### Release

-   All

### Cause

-   Service group OOB that is called "All" and apparently the group has deleted it.
-   The back end logic was relying on the sys\_id(0e7a06157f10310016181ccebefa91ce)of this group.  
       Creating a new one will not help because we are also relying on the sys\_id so a new one will not help.

### Resolution

-   Access the XML file from the attachment of the KB.
-   Export the XML into the instance and open the dashboard from the below URL.

                    https://<<instancename>>.service-now.com/nav\_to.do?uri=%2F$sw\_dashboards.do

  
                 ![](sys_attachment.do?sys_id=312a84bcdb4cf0d022e0fb24399619bb)
