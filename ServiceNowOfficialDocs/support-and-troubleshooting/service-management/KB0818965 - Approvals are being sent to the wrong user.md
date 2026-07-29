---
title: "Approvals are being sent to the wrong user"
aliases:
  - KB0818965
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818965
kb_number: KB0818965
last_modified: 2024-04-08
---

## Approvals are being sent to the wrong user

  

### Issue

Approvals are being sent to the wrong person's manager. The user was expecting the approval to be sent to manager 'A', but they are being sent to manager 'B' instead.

### Resolution

It was found that while the Request (REQ) record currently says "Bucky Barnes" is the requested\_for user, really - when the REQ's audit history was opened, it was originally requested for user "Steve Rogers":

-   /sys\_history\_line\_list.do?sysparm\_query=%3Dea5f40eadb138450f129e66505961970%5ElabelSTARTSWITHreq

As mentioned above via the link provided, the original requested\_for value is what is used by the workflow to generate approvals. This is why there is confusion. "Bucky Barnes" is what is shown currently, but that is misleading. At the start of the REQ, the requested\_for value was set to user "Steve Rogers", and so the workflow used this:

-   /nav\_to.do?uri=sys\_user.do?sys\_id=6308557c0fa6350078a7244be1050ec5

Therefore, the pull of Steve Rogers' manager is as follows:

Steve Rogers ➛ Nick Fury  
  
This, then, is working as expected per the configuration as Nick Fury was pulled for approvals.
