---
title: "Knowledge Search Screen Not Displaying After Xanadu Upgrade"
aliases:
  - KB2650880
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2650880
kb_number: KB2650880
last_modified: 2026-01-02
---

## Knowledge Search Screen Not Displaying After Xanadu Upgrade

  

### Issue

After upgrading to the Xanadu release, the Employee Center's knowledge search screen stopped displaying correctly. When selecting a knowledge base from the Employee Center home screen, the expected knowledge search screen does not appear. Investigation found changes to the Knowledge Bases Browse widget record in the Service Portal after the upgrade.

### Release

Xanadu

### Cause

A defect (PRB1827639) introduced in the Xanadu release caused incorrect redirection when selecting a knowledge base in Employee Center due to updates in the Knowledge Bases Browse widget.

### Resolution

To restore the previous knowledge search screen behavior:

1.  Clone the widget:
    -   Navigate to Service Portal > Widgets.
    -   Locate Knowledge Bases Browse and clone it.
2.  Make the widget editable:
    -   Open the cloned widget and ensure it is set to editable.
3.  Modify the client controller:
    -   In the Client Controller field, comment out the following lines:
        -   Line 28
        -   Line 31
        -   Line 32
    -   Save the changes.
4.  Replace the original widget:
    -   Update the Employee Center page to use the modified widget instead of the original.
5.  Plan for permanent fix:
    -   The defect will be resolved in Xanadu Patch 8, Yokohama Patch 2, and Zurich release. Schedule an upgrade when available.
