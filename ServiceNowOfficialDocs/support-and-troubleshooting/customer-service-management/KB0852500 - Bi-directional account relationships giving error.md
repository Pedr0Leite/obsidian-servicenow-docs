---
title: "Bi-directional account relationships giving error"
aliases:
  - KB0852500
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0852500
kb_number: KB0852500
last_modified: 2023-12-29
---

## Bi-directional account relationships giving error

  

### Issue

Created a new type for Account Relationships that can help to show some extra data in some cases. So, its look like:  
Account From: Account 1 (Can view Data of Account 2)  
Case Sharing: Data Sharing  
Account To: Account 2 (Share Data for Account 1).  
  
This works fine. But, in some cases there is a need of bi-directional sharing data. So, while to trying to crreate something like below after creating above,   
Account From: Account 2 (Can view Data of Account 1)  
Case Sharing: Data Sharing  
Account To: Account 1 (Share Data for Account 2).  
  
gives the following error:  
Unique Key violation detected by database ((conn=74323) Duplicate entry 'XXXXXXXXXX for key 'from\_company')  
Error MessageInvalid update

### Cause

The error is expected because a bi directional relationship has already been established and accounts have been associated with it.  
So, creating another one from account2->account1 is simply a duplicate which system does not allow.

### Resolution

No need to create another bi-directional relationship once its already created between 2 accounts.
