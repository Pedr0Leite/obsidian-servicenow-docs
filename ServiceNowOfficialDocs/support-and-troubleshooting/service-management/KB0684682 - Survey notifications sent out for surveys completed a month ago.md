---
title: "Survey notifications sent out for surveys completed a month ago"
aliases:
  - KB0684682
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0684682
kb_number: KB0684682
last_modified: 2024-12-31
---

## Survey notifications sent out for surveys completed a month ago

  

### Issue

Survey notifications sent out for surveys completed a month ago

Old survey notification

Late survey notification

### Cause

There is a custom business rules on the event - **survey\_response.poor\_feedback** which gets triggered when there is an insert or update on asmt\_assessment\_instance

### Resolution

Deactivate custom business rule or modify to add a condition for checking the asmt\_assessment\_instance state. It should not trigger if the state is **Canceled.**
