---
title: " When a user submits survey via Email New Assessment Instance is created rather than updating exisintg Assessment instance"
aliases:
  - KB0778533
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778533
kb_number: KB0778533
last_modified: 2024-04-08
---

## When a user submits survey via Email New Assessment Instance is created rather than updating exisintg Assessment instance

  

### Issue

When a user submits survey via Email New Assessment Instance is created rather than updating exisintg Assessment instance

### Resolution

This issue is occuring because the associated notification has a mail script defined which is creating a new Survey instance rather than updating the existing survey instance when submitting a Survey via Email.

  
We suggest referencing the logic implemented in OOB (Assessment: Survey User Invite) notification below which queries the correct survey instance for the Requestor:  
/nav\_to.do?uri=sysevent\_email\_action.do?sys\_id=634a4ae0d7011100828320300e6103c9  
  
  
var link = new AssessmentUtils().getAssessmentInstanceURL(current.sys\_id);  
var url = '[' + link + '](<' + link + '>)';  
template.print(url);
