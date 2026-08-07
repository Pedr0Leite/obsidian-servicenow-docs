---
title: "Recipient list on survey Dynamic creation issue"
aliases:
  - KB0812354
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0812354
kb_number: KB0812354
last_modified: 2025-04-17
---

## Recipient list on survey Dynamic creation issue

  

### Issue

Customer is experiencing an issue with Recipient list on survey Dynamic creation issue  
  
When you try to create on reception list a dynamic list based on filter , but even if you change the filter nothing appear on the related list recipients.  
It works like expected when you do a manual import.

Steps to Reproduce:  
  
Navigate to Survey Administration > Recipient List   
Create a dynamic list based on filter

select values in the field below

Table: sys\_user

User Field:Email

Condition:Email contains <value>

  
Click on refresh recipient list

Current: The recipient related list is not populated.

Expected: The recipient related list is populated with Users who meet the condition defined.

### Cause

  
THE 'User Field' value is not defined correctly.  
  
I could reproduce the issue OOB with the same definitions customer had.  
  
However after I have modified the 'User Field' and selected the 'sys\_id', this functions correctly.

### Resolution

  
Change the 'User Field' value to sys\_id.  
  
  
  
  

### Related Links

You can also refer to the documentation below:

  
https://docs.servicenow.com/csh?topicname=t\_TargetCommCreateRecipientList.html&version=latest
