---
title: "CSM Contacts on Email CC are not able to add additional comments to a Case "
aliases:
  - KB0831349
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0831349
kb_number: KB0831349
last_modified: 2026-06-25
---

## CSM Contacts on Email CC are not able to add additional comments to a Case

  

### Issue

Contacts that are added to the Email CC list from a Case are not able to add additional comments to the Case when they attempt to reply the email.

When a Contact on the CC list replies to the Case email:

-   The reply is not added to the Case
-   The inbound email processing fails
-   The following error appears in the system logs:

```
Unable to locate sn_customerservice_case <sys_id> for inbound email processing.
The users replying to the email do not have access to the Case record.
```

### Release

  All

### Cause

The users replying to the email do not have access to the Case record.

When the inbound email processor runs, it executes a `GlideRecord` query on the Case table. This triggers the out-of-box "Case query for customer" _Before Query_ Business Rule, which calls the following Script Include method:

```
global.CSQueryBRUtil().addCaseQueryBR(current);
```

By design, inbound email processing impersonates the user who sends the email. If that user does not have access to the Case record, the system cannot locate or update it during email processing.

This behavior can be confirmed by impersonating the affected user and attempting to open the Case record directly. The system will display the message "Record not found."

As a validation test only, disabling the OOB _Before Query_ Business Rule "Case query for customer" allows the email reply to be processed successfully. However, this is not recommended as a solution, as the behavior aligns with platform security design.

### Resolution

This behavior is by platform design.

For `sn_customerservice_case` records, Contacts with the `sn.customerservice.customer` role can only view and update Cases they personally created. They do not have access to Cases created by other users.

**Resolution Options**

1.  Grant Case Access  
    Contacts must have access to the Case records in order to update them (including via email replies). Ensure the appropriate access controls or sharing rules are in place.
2.  Create a Custom Role (Recommended)  
    Create a custom role that meets your business requirements and grants the necessary access to Customer Service Cases without modifying out-of-box behavior.

To proceed with implementing a custom role, refer to the ServiceNow documentation for guidance on properly configuring roles, ACLs, and access controls.

### Related Links

[Creating Custom User Roles docs page](https://docs.servicenow.com/csh?topicname=creating-custom-csm-user-roles.html&version=latest)
