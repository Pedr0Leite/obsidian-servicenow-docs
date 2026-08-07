---
title: "Comments and Work Notes not transferring when a Case is transferred"
aliases:
  - KB0999742
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0999742
kb_number: KB0999742
last_modified: 2025-09-03
---

## Comments and Work Notes not transferring when a Case is transferred

  

### Issue

Comments and Work Notes not transferring when a Case is transferred

### Resolution

This issue may happen because of a customization to the OOB Query Business Rule called "Restrict query" or a different custom Query BR.

The logic behind the Transfer Case functionality will perform a GlideRecord query which is affected by any Query BRs that you have set up.  
  
Because the customized Query BR restricts access to the newly created HR Case, the worknotes/comments are not able to be transferred.  
  
Once you revert the customized version of the Query BR or disable your custom one, everything will work without issue. Please note that customizations are not supported by ServiceNow Support. If you need the functionality that your custom query BR provides, you will need to review with your internal development team on a different way to implement it or customize how the transfer itself works. If you need further assistance with your implementation we recommend reaching out on the community forums or to our paid professional services team.
