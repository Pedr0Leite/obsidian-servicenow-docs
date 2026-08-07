---
title: "Selecting the reference icon on a form does not display the popup if a blank user criteria is set on the widget"
aliases:
  - KB0684023
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0684023
kb_number: KB0684023
last_modified: 2025-05-22
---

## Selecting the reference icon on a form does not display the popup if a blank user criteria is set on the widget

  

### Issue

When a user selects a reference icon lookup from Service Portal, no popup displays on the page.

![Service Portal reference icon lookup](sys_attachment.do?sys_id=3dfba92f97252a500af678ce2153af87 "Service Portal reference icon lookup")

### Release

Jakarta Patch 2

### Cause

This is caused by PRB1068750 - Service Portal.

Users lose access to Service Portal pages, widgets, or instances upon activation of user criteria if the Explicit Roles plugin is not enabled, which should be fixed from Jakarta Patch 2 onwards.

The cause is empty user criteria records being associated to the widget.

![Service Portal form widget showing empty user criteria](/sys_attachment.do?sys_id=75fba92f97252a500af678ce2153af85 "Service Portal form widget showing empty user criteria")

### Resolution

If you experience nothing being displayed when a reference icon is clicked in the portal, or a widget is not displayed, you can check to see if there are any blank user criteria set under the **Can View** related list of the widget.

For example, if a user clicks on the **i** icon from a catalog item on Service Portal, which is a reference to the Users table, and there is no popup displaying the user's record, check on the **Form** widget's **Can View** related list for any blank user criteria set.

You can disassociate the blank user criteria set under the **Can View** related list under the problematic widget.
