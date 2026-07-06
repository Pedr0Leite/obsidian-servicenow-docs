---
title: "Troubleshooting 'In-reply-to' emails that are being classified as 'new' and do not find the target record"
aliases:
  - KB0759068
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759068
kb_number: KB0759068
last_modified: 2025-02-12
---

## Troubleshooting 'In-reply-to' emails that are being classified as 'new' and do not find the target record

  

### Issue

Scenario:

1.  User A sends email to a ServiceNow instance, and cc's User B.
2.  User As email creates a record in the target table, but because the insert was on a custom variable, not current.insert(), the target table and target record fields in the email record are not filled.
3.  User B clicks 'reply' in their email program, and sends it to User A and the instance.
4.  User B's email arrives in the instance (and contains an In-Reply-To header referencing User A's email, which exists in the system from step 1.
5.  Email from step 3 above, classifies as a 'NEW' receive type and does not find the target record.

### Release

Applies to all versions.

### Cause

On the very first email sent in, the inbound action must set the 'target' and 'target table' in the email. Then when the second email comes in, it has the target to tie back to the ticket associated. If a custom variable is used on the inbound action, it will never set the target and target table of the email.  If an in-reply-to email is sent in, it will only use the first email matching and if there is no target, it will classify as a new and run the new inbound actions.

### Resolution

1.  On the 'New' inbound action being used to process the first email sent in, it needs to use the 'current.insert()' variable in the script.  Do not use a custom variable.    
      
    Note: custom variables do not update the source 'sys\_email' record with target and target table.  This affects the in-reply-to process for 'update' for the second email sent in.
2.  Example:

Message-ID from Email 1:<XXXXXXXXXXXXXXXX@xxxxxxxxxx.Server.outlook.com>

Headers from Email 2:  
References:<XXXXXXXXXXXXXXXX@xxxxxxxxxx.Server.outlook.com>  
In-Reply-To:<XXXXXXXXXXXXXXXX@xxxxxxxxxx.Server.outlook.com>

In order for Email 2 to find the target record, it needs to reference it from Email 1.  For this to work, it's critical for Email 1 to contain the target record reference.
