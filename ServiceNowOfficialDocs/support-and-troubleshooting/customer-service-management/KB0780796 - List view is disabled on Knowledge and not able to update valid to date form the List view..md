---
title: "List view is disabled on Knowledge and not able to update valid to date form the List view."
aliases:
  - KB0780796
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780796
kb_number: KB0780796
last_modified: 2025-04-02
---

## List view is disabled on Knowledge and not able to update valid to date form the List view.

  

### Issue

How to enable the List view to be able to update the fields.

### Release

All environments

### Resolution

  
To Enable the List edit and control, find the below details:  
  
\- Go to Navigator and go to the list view of knowledge articles.  
\- Click on configure List control.  
\- Here change the value for - List edit type from "Disable list control " to Save immediately (Cell mode edit). Please find the screenshot below for reference.  
  
![](sys_attachment.do?sys_id=af884c41dbc038d0fec4fb2439961933)  
  
**Note : If the Article versioning is enabled the also enable this system property to update it from the List view without creating the new version:**

-   **glide.knowman.versioning.enable\_minor\_edits**    **and set this to "True".**

  

  

  

### Related Links

  

Please find the documentation for the System property below:

[https://docs.servicenow.com/csh?topicname=article-versioning.html&version=latest](https://docs.servicenow.com/csh?topicname=article-versioning.html&version=latest "article-versioning")
