---
title: "Changes occurred to access control rules (ACLs) for the Label Entry table"
aliases:
  - KB0639956
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0639956
kb_number: KB0639956
last_modified: 2026-05-06
---

## Issue

Changes occurred to access control rules (ACLs) for the Label Entry table

## Resolution

This change should not affect access for internal authenticated users.

If this upgrade does affect user access or if the ACL has been customised and the related Customer Update \[sys\_update\_xml\] entry was removed, create a new read ACL on the Label Entry table without any roles. This will restore public read access.

To create a "**no roles**" ACL on the **Label Entry** table:

1.  Go to /sys\_security\_acl\_list.do and click **New**.  
      
    
2.  Create a new ACL with the following values:  
        **Operation**: read  
        **Name**: label\_entry  
      
    
3.  Click **Save**.
