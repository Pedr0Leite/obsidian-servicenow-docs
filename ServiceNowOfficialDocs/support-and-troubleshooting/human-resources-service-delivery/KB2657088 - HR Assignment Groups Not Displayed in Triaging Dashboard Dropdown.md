---
title: "HR Assignment Groups Not Displayed in Triaging Dashboard Dropdown"
aliases:
  - KB2657088
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2657088
kb_number: KB2657088
last_modified: 2025-12-17
---

## HR Assignment Groups Not Displayed in Triaging Dashboard Dropdown

  

### Issue

HR Assignment groups are not visible for selection in the Assignment Group section of the Triaging Dashboard. Only one HR group appears in the dropdown, and when selecting users, only sys IDs are shown instead of usernames.

### Release

Any

### Cause

-   The OOTB filter for Assignment groups uses the condition:
    
    ```
    parent=ff0370019f22120047a2d126c42e702b^ORname=HR
    ```
    
-   The sys\_id of the parent HR group in the instance differs from the OOTB value, causing only one group to appear.
-   The issue where usernames display as sys IDs after duplicating the dashboard is a separate OOTB defect (PRB1902466).

### Resolution

To resolve the issue:

-   Duplicate the Triaging Dashboard page.
-   Update the Data Broker condition “Fetch HR Assignment groups” to select the correct parent group named HR.
-   Validate that HR Assignment groups appear in the dropdown.
-   Monitor PRB1902466 for updates regarding the sys ID display issue.
