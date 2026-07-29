---
title: " HRM Case Acceptance Widget Missing After Task Configuration Setup"
aliases:
  - KB2626675
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2626675
kb_number: KB2626675
last_modified: 2026-01-03
---

## HRM Case Acceptance Widget Missing After Task Configuration Setup

  

### Issue

After creating a Task Configuration, the HRM Case Acceptance widget no longer appears in the My Task ticket view, although additional fields are visible.  
Guidance is needed on how to add the HRM Case Acceptance widget to the new Task Configuration so it displays as before.

### Release

Yokohama

### Cause

When both To-dos and Task Configurations exist for the same record type, Task Configuration takes precedence and overrides widget mappings from the To-dos Configuration.

The HRM Case Acceptance widget is not automatically included in the new Task Configuration.

### Resolution

-   **Understand Default Behavior**  
    The priority badge is part of the standard playbook design for in-progress activities.
    
-   **Why Overrides Don’t Work**  
    Setting "Prioritized" to "No" in Playbook Activity Overrides does not remove the badge. This is because the priority badge is part of the standard playbook design for in-progress activities, and configuration changes to the "Prioritized" field alone do not override the default UI behavior. To address this, you must use the Playbook Experience Builder to edit default ActivityUI settings and hide the priority label, as configuration alone cannot achieve this for HR tasks.
    
-   **Available Options**
    
    -   Use Playbook Experience Builder to edit default ActivityUI settings and hide the priority label. _(Applies to all playbook activities, not just HR tasks.)_
        
    -   For targeted changes, customize HR workspace pages. 
        
-   **Important Note**  
    Hiding the badge for HR tasks requires UI customization, as configuration alone cannot achieve this.
