---
title: "Flow designer action deleting role gives error \"Unknown error occurred while deleting the record\" "
aliases:
  - KB0760287
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0760287
kb_number: KB0760287
last_modified: 2026-01-05
---

## Flow designer action deleting role gives error "Unknown error occurred while deleting the record"

  

### Issue

Flow designer action deleting role gives error "Unknown error occurred while deleting the record"

### Release

### Cause

This happens when the flow is set to Run as System.

### Resolution

Set the Run as to User who initiates the session and make sure this user has rights to delete roles.
