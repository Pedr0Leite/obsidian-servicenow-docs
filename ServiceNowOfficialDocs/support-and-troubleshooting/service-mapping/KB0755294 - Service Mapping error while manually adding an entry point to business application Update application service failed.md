---
title: "Service Mapping error while manually adding an entry point to business application \"Update application service failed\"
aliases:
  - KB0755294
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755294
kb_number: KB0755294
last_modified: 2024-04-07
---

## Issue

# Symptoms

While manually adding entry point to a business application, we noticed an error: "Update application service failed"

# Release

All releases

# Steps to reproduce

1\. Navigate to the application service.   
2\. Try adding an entry point.   
3\. Click on view map.   
4\. This would throw an error 'Update application service failed' 

# Cause

Check the system logs with source 'identification\_engine'. You will see below errors.

identification\_engine : Output = {"items":\[{"sysId":"Unknown","identifierEntrySysId":"Unknown","errors":\[{"error":"REQUIRED\_ATTRIBUTE\_EMPTY","message":"Missing mandatory field \[assigned\_to\] in table \[cmdb\_ci\_endpoint\_manual\]. Add input value for mandatory field in payload"},{"error":"ABANDONED","message":"Too many other errors"}\],"identificationAttempts":\[{"attemptResult":"NO\_MATCH","identifierName":"Manual EndPoint","attributes":\["endpoint\_identifier"\],"searchOnTable":"cmdb\_ci\_endpoint\_manual"}\]}\],"relations":\[\]} 

See if there are any fields set to mandatory in the table \[cmdb\_ci\_endpoint\_manual\]. 

In this case, the fields 'u\_source' & 'assigned\_to' values are set to mandatory in the table \[cmdb\_ci\_endpoint\_manual\] table.

# Resolution

Set mandatory = false for the fields mentioned in the error message.

(or)

Set the property "glide.required.attribute.enabled" to false.  
Flag for enforcing required attributes during identification and reconciliation so that attributes cannot be null.  
Default : True
