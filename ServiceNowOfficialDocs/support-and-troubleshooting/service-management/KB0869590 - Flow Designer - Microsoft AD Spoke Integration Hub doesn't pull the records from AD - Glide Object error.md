---
title: "Flow Designer - Microsoft AD Spoke Integration Hub doesn't pull the records from AD - Glide Object error"
aliases:
  - KB0869590
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0869590
kb_number: KB0869590
last_modified: 2024-02-26
---

## Flow Designer - Microsoft AD Spoke Integration Hub doesn't pull the records from AD - Glide Object error

  

### Issue

Microsoft AD Spoke helps to Create, delete, and manage objects in Microsoft Active Directory, such as users, groups, and computers. Microsoft AD spoke provides actions to automate Microsoft Active Directory tasks when events occur in the Now Platform.

Actions include -->[AD Spoke Actions](https://docs.servicenow.com/bundle/paris-servicenow-platform/page/administer/integrationhub/concept/microsoft-ad-spoke.htmlc "AD Spoke Actions")

This KB talks about a scenario where the "Is user in group" action of AD spoke containing the username as input to the action fails to retrieve the user details from AD into ServiceNow

### Cause

The cause of the issue is the custom fields created on the sys\_user table which is actually holding the user details. The default field used in the spoke inputs doesn't contain any value and so sys id is passed automatically as the input to payload step in the action which is causing the issue with the create payload step output in the AD spoke leading to incorrect user details to the next step

### Resolution

Make sure correct user fields are passed to the action inputs of the "is user in group" action to search for the users in the AD group. The custom fields which contain the id or user details should be passed as the inputs to this action so the payload step is executed with correct output leading to proper details to the lookup step in the action
