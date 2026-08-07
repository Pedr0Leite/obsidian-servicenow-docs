---
title: "Non-ITIL approvers are unable to see information in the approval summarizer"
aliases:
  - KB0717838
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0717838
kb_number: KB0717838
last_modified: 2024-04-07
---

## Non-ITIL approvers are unable to see information in the approval summarizer

  

### Issue

# Symptoms

* * *

When a non-itil user is an approver for a SC Request he/she is not able to see the summary of the RITMs on the approval record. 

# Release

* * *

Jakarta Patch 9b

# Cause

* * *

This can be caused by a before query business rule on sc\_req\_item table that is restricting non-itil users from seeing RITMs. 

# Resolution

* * *

Disable or modify the before query business rule.
