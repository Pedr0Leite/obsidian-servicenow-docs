---
title: "How to make all Survey options 'modules' available in the navigator while searching"
aliases:
  - KB0818164
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818164
kb_number: KB0818164
last_modified: 2024-10-08
---

## How to make all Survey options 'modules' available in the navigator while searching

  

### Issue

The Survey plugin is activated but all modules are not available in the Navigator application menu's -> Survey.

### Cause

Check for OOB 'application menu' page for the survey is enabled or disabled.

### Resolution

1.  Inorder to get all the OOB application menu's in the navigator while searching, please activate the OOB pages which should be  set to 'True'.  
      
    
2.  Please find the below URL to navigate to the page:  
      
    https://<<Instance\_name.service-now.com>>/sys\_app\_application.do?sys\_id=93947cbad72011005e8da3eb5e610374  
      
    
3.  Check the required Module's are 'Active'.

### Related Links

Please refer to the below document for more information:

[https://docs.servicenow.com/csh?topicname=test-steps-app-navigator-category.html&version=latest#atf-application-visibility](https://docs.servicenow.com/csh?topicname=test-steps-app-navigator-category.html&version=latest#atf-application-visibility)
