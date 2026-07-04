---
title: "Dynamics 365/Power Apps Direct Integration: \"Validate Connection\" UI Action Not Working"
aliases:
  - KB2728444
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2728444
kb_number: KB2728444
last_modified: 2026-02-10
---

## Issue

Validate the connection UI action is not working for dynamics365 and Power Apps direct integration when the download activity check box is checked

## Resolution

In the Power Platform Admin Center:   
  
1\. Navigate to Environments and select the appropriate environment.  
2\. Go to Settings > Users + permissions > Security roles.  
3\. Select the security role assigned to the user requesting the token.  
4\. Under Miscellaneous Privileges (use the dropdown to select "Show all privileges" or "Show only assigned privileges"), verify whether prvReadRecordAuditHistory is present.  
  
Note: The ServiceNow product documentation expects the user to have the "Dynamics 365 Administrator" role. However, this alone does not grant in-app privileges such as prvReadRecordAuditHistory, which must be assigned through a Dataverse security role within the environment.  
  
In this case, the System Administrator role was provided to the user fetching the token, which does include the required prvReadRecordAuditHistory privilege. Request the token again if required.  
  
This will ultimately have to be reviewed and resolved on the Dynamics side.
