---
title: "How to cancel a flow context automatically when conditions are met"
aliases:
  - KB0750702
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750702
kb_number: KB0750702
last_modified: 2025-08-11
---

## How to cancel a flow context automatically when conditions are met

  

### Issue

Learn how to cancel an running flow context on any table when specific conditions are met. 

### Release

All Flow Designer supported versions

### Resolution

The default Cancel UI action on the flow context table (sys\_flow\_context) cancels flows manually. To automate this process, create a business rule on the table where you want to cancel flows: 

1.  Go to **System Definition** > **Business Rules.**
2.  Select **New**.
3.  Define the conditions that trigger flow cancellation.
4.  Add this script to the business rule:

var referer = GlideTransaction.get().getRequest().getHeader("referer");

action.setredirectURL(referer);

var gpa = new sn\_ph.GlideProcessAutomation(current.sys\_id);

gpa.cancel("manually by "+ gs.getSession().getUserName());`   `
