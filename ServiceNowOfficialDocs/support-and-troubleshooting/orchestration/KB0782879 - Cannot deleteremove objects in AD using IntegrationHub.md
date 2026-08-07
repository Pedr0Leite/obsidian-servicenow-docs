---
title: "Cannot delete/remove objects in AD using IntegrationHub"
aliases:
  - KB0782879
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0782879
kb_number: KB0782879
last_modified: 2025-01-16
---

## Cannot delete/remove objects in AD using IntegrationHub

  

### Issue

In this case, security groups couldn't be deleted from AD using delete AD object action. But this can happen with any AD object.

### Release

London+

### Resolution

The object to be deleted is queried first. Once the object is fetched, we run the DeleteTree() method on the object to delete the object and its children.  
Ensure the configured credentials have permission to run the DeleteTree() operation.
