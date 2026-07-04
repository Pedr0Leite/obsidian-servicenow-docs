---
title: "Manager and Agent Calendar do not populate groups and members alphabetically"
aliases:
  - KB0812511
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0812511
kb_number: KB0812511
last_modified: 2024-04-08
---

## Manager and Agent Calendar do not populate groups and members alphabetically

  

### Issue

Drop Down list containing All Groups in the Team Calendar does not show groups. Also, the users listed on the calendar are not in alphabetical order.

Steps to Reproduce:

-   Log in to the instance
-   Go to Agent Calendar from the Application Navigator
-   You will see that Users are not listed in alphabetical order.
-   Click on the Groups on the top left, you will see that the groups will not be listed in alphabetical order.

### Cause

The Script Includes: CalendarRestHelper has been customized.

### Resolution

To fix the issue, revert this Script Includes: CalendarRestHelper to OOB version.
