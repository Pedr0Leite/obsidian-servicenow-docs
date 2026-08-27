---
title: "Survey is not assigning to users as expected."
aliases:
  - KB0790911
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790911
kb_number: KB0790911
last_modified: 2024-04-08
---

## Survey is not assigning to users as expected.

  

### Issue

We have a survey that won't work when we enable public access.

### Cause

Duplicate assessable record.

### Resolution

In the instance there are two assessable records for the impacted survey. In an out of box instance, if there are two assessable records for the same survey the same behavior is seen when trying to take the survey. To resolve this issue, please remove the duplicate assessable record for the impacted survey.
