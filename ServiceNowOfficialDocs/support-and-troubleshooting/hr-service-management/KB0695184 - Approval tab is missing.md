---
title: "Approval tab is missing"
aliases:
  - KB0695184
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695184
kb_number: KB0695184
last_modified: 2024-04-07
---

## Approval tab is missing

  

### Issue

# Symptoms

* * *

Approval tab is missing from HR case record

# Release

* * *

Kingston

# Cause

* * *

In approver related list "Omit if empty" checked box was checked.

As a result for the HR payroll case which does not have any approvers, the approver tab itself was not showing.

# Resolution

* * *

Uncheck the checkbox:"Omit if empty" 

This will enable to show approver tab always.

# Additional Information

* * *

Please check the following doc link for details:

[Configure list controls](https://docs.servicenow.com/csh?topicname=t_ConfigureListControls.html&version=latest "Configure list controls")
