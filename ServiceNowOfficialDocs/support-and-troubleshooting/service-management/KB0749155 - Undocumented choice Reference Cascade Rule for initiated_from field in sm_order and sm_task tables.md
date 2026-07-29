---
title: "Undocumented choice Reference Cascade Rule for initiated_from field in sm_order and sm_task tables"
aliases:
  - KB0749155
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749155
kb_number: KB0749155
last_modified: 2024-04-07
---

## Undocumented choice Reference Cascade Rule for initiated\_from field in sm\_order and sm\_task tables

  

### Issue

# Symptoms

There is an undocumented choice Reference Cascade Rule for initiated\_from field in sm\_order and sm\_task tables. The documentation did not have an explanation for it.

# Release

All available releases

# Cause

It is an invalid Reference Cascade rule. Reference Cascade rule for initiated\_from field is not suppose to have any restriction when the referencing record is deleted. 

# Resolution

The value "restrain" actually is not a valid value in the DB, therefore the behavior defaults to none - not having any cascade effect (expected behavior). If this value is set to "restrict", the behavior will start restricting cascade deletion when the referencing record is deleted, which we is not intended. So no action is required to resolve the issue.

# Additional Information

[https://docs.servicenow.com/csh?topicname=t\_CascadeDeleteRules.html&version=latest](https://docs.servicenow.com/csh?topicname=t_CascadeDeleteRules.html&version=latest)
