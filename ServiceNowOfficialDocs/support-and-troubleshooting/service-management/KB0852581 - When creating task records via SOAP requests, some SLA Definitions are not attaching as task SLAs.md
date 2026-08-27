---
title: "When creating task records via SOAP requests, some SLA Definitions are not attaching as task SLAs"
aliases:
  - KB0852581
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0852581
kb_number: KB0852581
last_modified: 2024-04-08
---

## When creating task records via SOAP requests, some SLA Definitions are not attaching as task SLAs

  

### Issue

The user had some issues with SLA Definitions attaching as task SLAs _only_ when the parent task record was created via SOAP request. Creating task records via the Platform UI did not replicate the issue (SLA Definitions attached fine as task SLAs when using this method).

### Resolution

It was found that within the localhost logs of the instance, many errors were being thrown including large stack-traces which all pointed to the user's custom process (custom Script Includes and Business Rules).   
  
The user was gently reminded that Support engineers are experts in OOB behavior and specialize in resolving OOB break-fix behaviors. Unfortunately, the debugging and implementation of customization like this is not in the engineer's area of expertise.  
  
It was recommended that the user continue the investigation internally with the development team who created and should, therefore, also support the custom process.
