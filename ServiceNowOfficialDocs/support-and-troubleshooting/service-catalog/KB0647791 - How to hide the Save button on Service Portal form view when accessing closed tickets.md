---
title: "How to hide the Save button on Service Portal form view when accessing closed tickets"
aliases:
  - KB0647791
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0647791
kb_number: KB0647791
last_modified: 2024-04-07
---

## How to hide the Save button on Service Portal form view when accessing closed tickets

  

### Issue

How to hide the Save button on Service Portal form view when accessing closed tickets

  
  

# Issue

* * *

If you do not want a user to update a closed record, you might consider hiding the blue Save button on Service Portal form view when accessing records in a closed state. However, in Service Portal, the blue Save’ button is always visible.

# Resolution / Workaround

* * *

In a base instance, you currently cannot hide the Save button without modifying the form widget, which would require you to clone the widget and then script a condition to check against the State value of the record. One option is to clone the form widget and remove the button entirely, and instead use a UI Action for the Incident table on the form to do a conditional check against the State value. The blue Save button will be gone from the cloned form on the right side, and a new gray Save UI action will appear on the bottom-left for records not equal to 7 (the base instance value for "closed").

![](sys_attachment.do?sys_id=c3a8a82edb02b450e515c22305961909)

Note that the blue Save button is now gone and the Save UI Action shows only on records that are not Closed.
