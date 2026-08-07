---
title: "Priority Badge Visible on Playbook Activities After Xanadu Upgrade"
aliases:
  - KB2626648
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2626648
kb_number: KB2626648
last_modified: 2026-02-25
---

## Priority Badge Visible on Playbook Activities After Xanadu Upgrade

  

### Issue

After the Xanadu upgrade, a priority badge appears on playbook activities in the HR Agent Workspace. Users want to understand:

-   Why the badge is displayed
-   Its significance
-   How to disable or hide it

Attempts to disable the badge using Playbook Activity Overrides (setting “Prioritized” to “No”) did not work as expected.

### Release

Xanadu

### Cause

-   The priority badge is default behavior for in-progress activities in playbooks.
-   In the Xanadu release, this badge was made more prominent for better visibility.
-   Playbook Activity Overrides cannot selectively hide the priority badge for HR tasks; UI customization is required for granular control.

### Resolution

-   The priority badge is part of the standard playbook design for in-progress activities.
-   Setting "Prioritized" to "No" in Playbook Activity Overrides does not remove the badge.
-   Available Options
    -   -   Use Playbook Experience Builder to edit default ActivityUI settings and hide the priority label. _(Applies to all playbook activities)_ Playbook Experience Builder Link: /now/builder/ui/edit/experience/ac22dd54c35a201098c960bc0eba8fed/51ddfb5ac3113010948404186e40dd09/11ddbb5ac3113010948404186e40dd25
        -   Customize HR workspace pages for targeted changes. Reference Documentation [https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB1433649](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1433649)
        -   Hiding the badge only for HR tasks requires UI customization, as configuration alone cannot achieve this.
