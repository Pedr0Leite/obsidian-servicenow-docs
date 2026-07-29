---
title: "HR Case Priority Incorrect When Created from Email Using Predictive Intelligence"
aliases:
  - KB2657086
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2657086
kb_number: KB2657086
last_modified: 2025-12-17
---

## HR Case Priority Incorrect When Created from Email Using Predictive Intelligence

  

### Issue

When an HR Case is created from an email, Predictive Intelligence categorizes the COE and assigns the HR Service, but the case priority does not match the value configured in the HR Service template. For example, the HR Service template sets priority to 3 - Moderate, but the case is created with 4 - Low, causing SLAs dependent on priority to not trigger as expected.

### Release

Any

### Cause

This occurs because when a field (such as priority) is set by the inbound email action, the HR Service template does not overwrite it during case creation. The logic in the script include sn\_hr\_core.hr\_TemplateUtils (line 45) skips updating fields already populated by the inbound email action. This is by design.

### Resolution

To address the issue:

-   Review the script include sn\_hr\_core.hr\_TemplateUtils.
-   Modify the logic to allow overwriting the priority field even if it was set by the inbound email action.
-   Validate the change in a lower environment before applying to production.
-   Refer to DEF0683136 and PRB1894083 for tracking the defect and associated discussions.
-   If customization is not preferred, continue using the provided workaround or adjust business rules to handle priority updates post-case creation.
