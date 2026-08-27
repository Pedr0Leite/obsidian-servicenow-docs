---
title: "Survey invitations/instances are not being generated."
aliases:
  - KB0866632
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0866632
kb_number: KB0866632
last_modified: 2024-04-08
---

## Survey invitations/instances are not being generated.

  

### Issue

Survey invitations/instances are not being generated

### Release

All

### Cause

"Auto assessment business rule" associated with the trigger condition should be an 'after' BR and the function in the script should be function onAfter(){}

### Resolution

Please make sure that the "Auto assessment business rule" associated with the trigger condition is an 'after' BR and the function in the script should be function onAfter(){}
