---
title: "HR Cases Missing \"Subject Person\" and \"Opened For\" Fields When Created from Agent Workspace"
aliases:
  - KB2656755
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2656755
kb_number: KB2656755
last_modified: 2025-12-17
---

## HR Cases Missing "Subject Person" and "Opened For" Fields When Created from Agent Workspace

  

### Issue

HR cases created from the Agent Workspace may have missing values in the Subject Person and Opened For fields. This typically occurs when the Subject Person and HR Service fields are cleared and re-selected during case creation, leading to incomplete or empty key fields.

### Release

Any

### Cause

The issue occurs because selecting the HR Service from the dropdown after clearing the Subject Person does not trigger the required event to populate these fields. Typing and selecting the service works as expected.

### Resolution

The issue exists in Out-of-the-Box (OOB) instances; a Problem Record (PRB1851081) has been logged for investigation.

Workaround:

-   After removing the Subject Person, select a different HR Service or refresh the page before proceeding.
-   Alternatively, type and select the HR Service instead of clicking from the dropdown.
