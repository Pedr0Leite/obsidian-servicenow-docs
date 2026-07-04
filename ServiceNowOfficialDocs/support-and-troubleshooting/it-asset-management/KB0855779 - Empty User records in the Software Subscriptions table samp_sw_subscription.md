---
title: "Empty \"User\" records in the \"Software Subscriptions\" table \"samp_sw_subscription\""
aliases:
  - KB0855779
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0855779
kb_number: KB0855779
last_modified: 2024-04-08
---

## Empty "User" records in the "Software Subscriptions" table "samp\_sw\_subscription"

  

### Issue

-   User field is observed to be empty for few records in the "samp\_sw\_subscription" table.  
      
        ![](sys_attachment.do?sys_id=998c3085db40f8d022e0fb243996196b)  
      
    
-   When a particular user is marked under "assigned to" in the SAAS tools for a subscription, how is Servicenow mapping to that same person ?  
      
    
-   Based on which data, the user id is identified in Servicenow ?  
      
    
-   How the user related information gets populated on "samp\_sw\_subscription" table ?

### Release

-   All

### Resolution

-   The "User" is identified using the "User principal name" when the subscription is created.  
      
    
-   The "User principal name" is considered as the email and is used to query the servicenow "Users" table.  
      
    
-   If no record is found in the "Users" table, the "User principle name" is trimmed to have only the "Username" and this "Username" is used to query the "Users" table.  
      
    
-   The "Users" field will be empty if no record is found either with email or with the username in the "Users" table.  
      
    
-   In short, even if the "User principal name" is not empty, the "User" field will be empty if there are no "Users" on this instance with the "User principal name" as their email id or with the same username.
