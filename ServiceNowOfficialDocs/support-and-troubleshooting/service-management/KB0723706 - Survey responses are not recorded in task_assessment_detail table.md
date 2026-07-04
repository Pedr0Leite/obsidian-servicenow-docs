---
title: "Survey responses are not recorded in task_assessment_detail table"
aliases:
  - KB0723706
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723706
kb_number: KB0723706
last_modified: 2025-12-09
---

## Survey responses are not recorded in task\_assessment\_detail table

  

### Issue

# Symptoms

* * *

Survey responses are not found in the task\_assessment\_detail table

# Release

* * *

Kingston

# Cause

* * *

The Legacy survey trigger condition was active and the legacy survey URLs were sent to the users

# Resolution

* * *

The Legacy survey trigger condition was active and the legacy survey URLs were sent to the users.

Due to this reason, the survey responses were stored in the 'survey\_response' table and not in the task\_assessment\_detail table.

To resolve the issue we need to turn the legacy survey trigger conditions to active false.
