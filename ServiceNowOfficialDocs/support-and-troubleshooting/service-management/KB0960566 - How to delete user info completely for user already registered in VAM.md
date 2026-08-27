---
title: "How to delete user info completely for user already registered in VAM"
aliases:
  - KB0960566
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960566
kb_number: KB0960566
last_modified: 2025-01-02
---

## How to delete user info completely for user already registered in VAM

  

### Summary

During VAM user registeration if any user is not completely registered successfully for some reason, when they want to use same e-mail address to registered again, after input the mail address, the below error will show up on the screen.

VAM user Registration Screen Error " The email you entered is awaiting activation."

![](sys_attachment.do?sys_id=a03f20601b7320107a5933f2cd4bcb33)

https://<Instance name>.service-now.com/vam?id=vm\_registration

  

  

### Release

Any version of Vaccine Administration

### Instructions

In order to delete an external user completely from the system, need to delete the records from the following tables.  
1\. sys\_user or csm\_consumer\_user (Both the lists will lead to the same record only.)  
2\. csm\_consumer  
3\. user\_registration\_request  
  
Once the above records corresponding to the external user are deleted, the customer should be able to re-register the same user.
