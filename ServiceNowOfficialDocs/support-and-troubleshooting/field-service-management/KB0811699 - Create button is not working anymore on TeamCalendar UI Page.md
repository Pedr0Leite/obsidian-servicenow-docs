---
title: "Create button is not working anymore on TeamCalendar UI Page"
aliases:
  - KB0811699
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0811699
kb_number: KB0811699
last_modified: 2024-04-07
---

## Create button is not working anymore on TeamCalendar UI Page

  

### Issue

Manager ->Team Calendar is not working properly. When trying to add an event either through "Create" button or through double clicking on any user's time entry, it is not working.

### Cause

The issue is happening since **UI Page `$managerSchedule`** (nav\_to.do?uri=sys\_ui\_page.do?sys\_id=4fb4c91cc3fb2200467f10c422d3aee6) has been customised 

### Resolution

Check the Client script of the UI Page nav\_to.do?uri=sys\_ui\_page.do?sys\_id=4fb4c91cc3fb2200467f10c422d3aee6 .

If you will see that the old **GlideModalFormSetWidth** is loaded using an addLateLoadEvent, then update this part of the code accordingly by changing this line of the Client Script field from:

fileref.setAttribute("src", "scripts/classes/GlideModalFormSetWidth.js");

To:

fileref.setAttribute("src", "scripts/classes/MatchingRuleGlideModalFormSetWidth.js");

**Please Note** : The same issue can also occur for Agent ->Team calendar as well and for that check for UI page - $agentSchedule - nav\_to.do?uri=sys\_ui\_page.do?sys\_id=380a20dbc3671200467f10c422d3ae4a and  perform similar update to fix the issue
