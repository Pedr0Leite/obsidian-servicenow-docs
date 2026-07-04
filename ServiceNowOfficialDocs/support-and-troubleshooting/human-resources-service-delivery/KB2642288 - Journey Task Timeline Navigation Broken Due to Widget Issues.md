---
title: "Journey Task Timeline Navigation Broken Due to Widget Issues"
aliases:
  - KB2642288
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2642288
kb_number: KB2642288
last_modified: 2026-01-02
---

## Journey Task Timeline Navigation Broken Due to Widget Issues

  

### Issue

The Journey Task Timeline functionality is broken; clicking does not return to the previous page as expected.

-   Suspected issue with a mix of Out-of-Box (OOB) and custom widgets, particularly around the HRM To-dos Summary widget.
-   Problems encountered when placing the standard ticket tab in Page Designer; custom widget replacement did not resolve the issue.

### Release

Any

### Cause

-   Missing code updates in the HRM Task widget due to an incomplete upgrade (related to PRB1606083).
-   Customizations and mixed widget usage contributed to navigation failures.

### Resolution

-   Code modifications were applied to the HRM Task widget, restoring expected navigation functionality.
-   A new defect (PRB1840453) was logged to address this issue.
-   As a workaround, import the fixed XML file into other instances until the defect is officially addressed.
-   Reverting widgets to OOB versions and comparing behaviors with a Personal Developer Instance (PDI) can help validate fixes.
