---
title: "Employee Center portal popular items and menu item is not visible ."
aliases:
  - KB2940702
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2940702
kb_number: KB2940702
last_modified: 2026-04-17
---

## Employee Center portal popular items and menu item is not visible .

  

### Issue

**Problem**  
Employee Center portal popular items and menu are not working after the Zurich patch7 upgrade. 

### Release

NA

### Cause

**Root Cause**  
The root cause was an inactive taxonomy configuration in the portal. Specifically, the 'Employee' taxonomy was not active in the Stage instance, causing the menu and popular items to remain hidden. Activating this taxonomy resolved the issue.  
  

### Resolution

**Steps to Resolve**  
1\. Verify the taxonomy configuration in the portal. Ensure the 'Employee' taxonomy is inactive in the instance.

2\. Navigate to the m2m\_sp\_portal\_taxonomy page for the specific taxonomy record (sys\_id: 47694e3b731d3010c94f54eb7df6a751) to confirm activation.

3\. Activate the taxonomy if it is not already active.

4\. Verify that the menu and popular items become visible after activation.

5\. Confirm the resolution by checking the portal in the dev instance, where the taxonomy is active and functioning as expected.
