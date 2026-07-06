---
title: "Error while loading  xlsx file  in LOAD DATA for doing transform map"
aliases:
  - KB0791790
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791790
kb_number: KB0791790
last_modified: 2024-04-20
---

## Error while loading xlsx file in LOAD DATA for doing transform map

  

### Issue

Customer needs to update  records on a table table via import. While selecting the Import set table and trying to attach Excel file an error (attached the error message) is throwing and the Excel file is not getting attached for transform mapping. The same error can be seen in all instances too. When trying to add the file to a HI ticket it also raises the same issue.

![](sys_attachment.do?sys_id=6fd943da1b8ac414d01143f6fe4bcbe2)

### Cause

The customer must have installed in your network Symantec DLP (Data Loss Policy) Prevention or a related third party product which does not allow the file to be uploaded.

### Resolution

The next URLs describe a product that is not ours and unfortunately, it is out of our scope to fix

The fact that the same file cannot be uploaded on HI portal is another proof that the customer's system is blocking this file outside their organisation.  
  

The customer has to Contact their own IT support team or Symantec DLP support and they will clarify why the file is blocked.
