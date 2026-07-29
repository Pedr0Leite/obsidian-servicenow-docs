---
title: "Why are duplicate entries created in the 'sys_history_line' table?"
aliases:
  - KB0691454
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0691454
kb_number: KB0691454
last_modified: 2024-04-19
---

## Why are duplicate entries created in the 'sys\_history\_line' table?

  

### Issue

# Symptoms

* * *

Duplication entries created in 'sys\_history\_line' table for same audited (for example incident) record with same user.

# Release

* * *

Any supported release.

# Cause

* * *

Duplicate entries created in 'sys\_history\_line' table, when the users are viewing the audited (for example incident) record, but having different domain / Date format / Language / Time Zone.

This is expected design behavior, because new sys\_history\_set would be built based on the domain / Date format / Language / Time Zone of the user.

# Resolution

* * *

Though the sys\_history\_line record appears as duplicate, actually they are not, as they will have different set field ('sys\_history\_set'), this is an expected design behavior.

# Additional Information

* * *

[Audit history and History set](https://docs.servicenow.com/csh?topicname=c_DiffBtwnAuditHistSets.html&version=latest "Audit history and History set")

[History List](https://docs.servicenow.com/csh?topicname=r_HistoryList.html&version=latest "History List")
