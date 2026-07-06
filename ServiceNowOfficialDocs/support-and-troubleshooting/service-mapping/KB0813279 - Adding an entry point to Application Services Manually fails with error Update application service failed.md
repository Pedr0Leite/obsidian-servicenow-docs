---
title: "Adding an entry point to Application Services Manually fails with error \"Update application service failed\""
aliases:
  - KB0813279
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813279
kb_number: KB0813279
last_modified: 2024-04-07
---

## Adding an entry point to Application Services Manually fails with error "Update application service failed"

  

### Issue

When attempting to add an entry point to Application Services Manually, the following error is thrown:

Update application service failed

Steps to reproduce:

  
1) Open

Configuration->Application Services->Application Services

2) Click New  
3) Fill the form and save  
4) Add entry point  
5) Update

6) Error appears:

Update application service failed

### Cause

In syslog, check if you see the following similar error when attempting to manually add the CI into the Application Service:

identification\_engine : Output = {"items":\[{"sysId":"Unknown","identifierEntrySysId":"Unknown","errors":\[{"error":"REQUIRED\_ATTRIBUTE\_EMPTY","message":"Missing mandatory field \[operational\_status\] in table \[cmdb\_ci\_endpoint\_manual\]. Add input value for mandatory field in payload"},{"error":"ABANDONED","message":"Too many other errors"}\],"identificationAttempts":\[{"attemptResult":"NO\_MATCH","identifierName":"Manual EndPoint","attributes":\["endpoint\_identifier"\],"searchOnTable":"cmdb\_ci\_endpoint\_manual"}\]}\],"relations":\[\]}

If that's the case, then the flow requests this filed \[operational\_status\] as mandatory because this entry was set to Mandatory for CMDB\_Ci table. OOTB this entry is not mandatory. When creating BS the flow looks for this mandatory entry in request. 

### Resolution

To resolve the issue we have two options:

  
Uncheck mandatory set from \[operational\_status\] or set to false following system property: "glide.required.attribute.enabled"
