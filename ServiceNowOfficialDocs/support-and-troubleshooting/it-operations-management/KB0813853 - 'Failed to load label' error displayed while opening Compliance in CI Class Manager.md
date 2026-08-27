---
title: "Failed to load label' error displayed while opening Compliance in CI Class Manager"
aliases:
  - KB0813853
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813853
kb_number: KB0813853
last_modified: 2025-04-07
---

## 'Failed to load label' error displayed while opening Compliance in CI Class Manager

  

### Issue

When the user navigates to CI Class Manager, selects 'Windows Server' from the hierarchy, then opens 'Compliance', '**Failed to load label**.' error messages are displayed. The error appears to be displayed only within the CI Class Manager interface.

### Release

-   Madrid

### Cause

-   Missing ACL for sys\_db\_object.

### Resolution

1) Check if the ACL for sys\_db\_object is present on the instance by navigating to the below and expect to observe the records as displayed in the screenshot

-   https://<instance\_name>.service-now.com/sys\_security\_acl.do?sys\_id=8cdc8e25c0a8016625211306d25f57ed  
      
      
    

              ![](sys_attachment.do?sys_id=832f5489db0c70905a959c41ba96193f)  
  

2) If no records are found from the above, navigate to the plugins page from the navigator and look if the plugin "**High Security Settings**" is installed.

              ![](sys_attachment.do?sys_id=1b2f5489db0c70905a959c41ba961940)  
  

3) When observed that it is not installed, Install the plugin or import the ACL from OOB, which will fix the issue.
