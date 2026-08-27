---
title: "Creating a new HR case and searching for  an employee, it loads forever and nothing show up."
aliases:
  - KB0813212
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813212
kb_number: KB0813212
last_modified: 2025-09-03
---

## Creating a new HR case and searching for an employee, it loads forever and nothing show up.

  

### Issue

While creating a new case and searching for an employee it loads forever and nothing show up.

Search by case number/name/emailid, same results.

### Resolution

  
check for System Property "glide.rest.global.honor\_snc\_internal\_flag" if its set to true.  
Setting is to false, fixed the issue.  
  
Please see below documentation on the property mentioned above to understand what is used for and learn how you can provide the access required.  
  
https://docs.servicenow.com/csh?topicname=c\_RESTAPI.html&version=latest  
https://docs.servicenow.com/csh?topicname=c\_RESTAPI.html&version=latest  
https://docs.servicenow.com/csh?topicname=c\_RESTAPI.html&version=latest
