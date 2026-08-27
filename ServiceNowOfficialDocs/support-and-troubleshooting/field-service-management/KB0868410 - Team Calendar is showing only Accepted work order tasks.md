---
title: "Team Calendar is showing only Accepted work order tasks"
aliases:
  - KB0868410
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0868410
kb_number: KB0868410
last_modified: 2023-11-18
---

## Team Calendar is showing only Accepted work order tasks

  

### Issue

-   Work Order Tasks are showing on the Field Service / Team Calendar only when the task status is Accepted.

### Release

-   Paris

### Cause

-   The Event configuration has only the ACCEPTED state in the "Agent\_schedule\_task\_config" for the Work Orders due to which only the ACCEPTED state tasks gets displayed.

### Resolution

1.  Please set the Event configuration 'Agent\_schedule\_task\_config' as per your requirement in order to fix the issue.
