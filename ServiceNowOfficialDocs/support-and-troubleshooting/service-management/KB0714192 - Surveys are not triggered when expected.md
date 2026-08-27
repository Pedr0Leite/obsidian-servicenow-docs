---
title: "Surveys are not triggered when expected"
aliases:
  - KB0714192
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714192
kb_number: KB0714192
last_modified: 2024-04-07
---

## Surveys are not triggered when expected

  

### Issue

Surveys are not triggered on the Payroll Table when the condition is met.

### Release

Kingston Patch 8 +

### Cause

The User field is set to 'Opened for'; however, opened for is not populated. The user field should be a populated user reference field and the user should be active for the survey instance to be created. 

### Resolution

1.  Populate the 'Opened for' field or use Requester for the user field.
