---
title: "Request item workflow not triggering on some request with multiple requested items."
aliases:
  - KB0657629
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657629
kb_number: KB0657629
last_modified: 2025-08-15
---

## Request item workflow not triggering on some request with multiple requested items.

  

### Issue

Issue Summary  

* * *

Request item workflow not triggering on some request with multiple requested items.  

Most Probable Cause  

* * *

Workflow on Request is not providing enough time for the system to trigger workflows for its child requested items.  

Solution Proposed  

* * *

Adding a 5 second timer to the parent request workflow will give enough time for the system to analyze and run all the business rules to trigger workflow on the child RITM's.  

### Release

### Resolution
