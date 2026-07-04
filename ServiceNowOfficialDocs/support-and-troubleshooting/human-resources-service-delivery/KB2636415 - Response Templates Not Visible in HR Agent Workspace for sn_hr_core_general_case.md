---
title: "Response Templates Not Visible in HR Agent Workspace for sn_hr_core_general_case"
aliases:
  - KB2636415
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2636415
kb_number: KB2636415
last_modified: 2026-01-03
---

## Response Templates Not Visible in HR Agent Workspace for sn\_hr\_core\_general\_case

  

### Issue

Response templates are not visible in HR Agent Workspace for the table sn\_hr\_core\_general\_case, while templates for sn\_hr\_core\_case work as expected.

-   Attempts to configure new response templates and update table configurations did not resolve the issue.
-   The response template panel remains stuck on "Loading", even for admin users.
-   Suspected missing configuration or system error preventing access to response templates for certain tables.

### Release

Any Release

### Cause

Incorrect configuration in Table Configuration and Search Action Configuration for the affected table (sn\_hr\_core\_general\_case) prevented the response template panel from loading.

### Resolution

Applied the following configuration changes to enable response templates for sn\_hr\_core\_general\_case:

1.  Set Allow search with empty search text to True.
2.  Removed the Short Description field from the Search field tab.
3.  Updated Search Resource Configuration to Response Template (Email).
4.  Set Current Table to sn\_hr\_core\_general\_case.
5.  Set Response Record Table to sn\_templated\_snip\_note\_template.
6.  Verified that response templates load correctly after these changes.

The configuration was then migrated to production using an Update Set.
